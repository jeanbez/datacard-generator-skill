# /// script
# requires-python = ">=3.10"
# dependencies = ["jsonschema>=4.18", "pyyaml>=6.0"]
# ///
"""Export a Genesis datacard as an xCard registry submission.

The HPDF xCard registry picks a validation profile from a card's top-level
keys: `xCard` selects the xCard spine profile (xcard.schema.json), while
`supports_*` and the capability containers select the Genesis LinkML profile.
A card carrying both is rejected as "profile markers are ambiguous" — and
Genesis v2 requires both, so a full v2 card can never register.

This writes the spine-profile document the registry does accept, derived from
the full card. The full card stays the authoritative record; the export is a
projection of it and is never edited by hand.

Usage:
    uv run -q scripts/export_xcard.py CARD.md [--out OUT.md]

Exits 1 if the export does not satisfy the vendored xcard.schema.json.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path

import yaml

from convert_v12_to_v20 import project_spine

SCHEMA_PATH = Path(__file__).resolve().parent / "xcard.schema.json"

# Keys that make the registry route a card to the LinkML profile. The export
# must carry none of them, or the registry rejects it as ambiguous.
LINKML_MARKERS = frozenset({
    "supports_discoverability", "supports_accessibility", "supports_interoperability",
    "supports_reusability", "supports_governed_use", "supports_ai_usability",
    "discoverability", "accessibility", "interoperability", "reusability",
    "governed_use", "ai_usability",
})

# Genesis RelationshipTypeEnum -> xcard.schema.json relationship type. Anything
# unmapped becomes `references`, the one type that asserts nothing it can't back.
RELATIONSHIPS = {
    "is_derived_from": "derived_from",
    "is_part_of": "part_of",
    "has_part": "has_part",
    "requires": "requires",
    "obsoletes": "supersedes",
    "is_obsoleted_by": "superseded_by",
}

MIME = {
    "csv": "text/csv",
    "json": "application/json",
    "hdf5": "application/x-hdf5",
    "netcdf": "application/x-netcdf",
    "parquet": "application/vnd.apache.parquet",
}


def _str(v):
    return v.isoformat() if isinstance(v, (date, datetime)) else v


def _target(ident: dict) -> str:
    value = str(ident.get("value", ""))
    return f"https://doi.org/{value}" if ident.get("type") == "doi" else value


def _agent_name(agent: dict) -> str | None:
    if p := agent.get("person"):
        return " ".join(x for x in (p.get("given_name"), p.get("family_name")) if x)
    if o := agent.get("organization"):
        return o.get("name")
    return None


def export(g: dict) -> dict:
    d = g.get("discoverability") or {}
    card, ident = d.get("datacard") or {}, d.get("identification") or {}
    desc = d.get("dataset_description") or {}
    acc, inter = g.get("accessibility") or {}, g.get("interoperability") or {}
    reuse, gov = g.get("reusability") or {}, g.get("governed_use") or {}
    ai = (g.get("ai_usability") or {}).get("ai_usage")
    ds = inter.get("data_structure") or {}

    # Reuse the spine projection's risk: it already applies the stricter-wins
    # and status-flag rules, so a controlled dataset cannot export as general.
    spine, _ = project_spine(g)
    risk = ((spine.get("categorization") or {}).get("tags") or {}).get("risk")

    x: dict = {
        "xCard": {"card_type": "data", "version": str(card.get("template_version", ""))},
        "id": (card.get("id") or {}).get("value") or Path(card.get("filename", "")).stem,
        "name": ident.get("name"),
        "description": desc.get("dataset_summary"),
        "science": list(desc.get("science_domain") or []),
        "keywords": list(desc.get("keywords") or []),
        "sensitivity": risk or "unreviewed",
        "developed_by": [n for n in map(_agent_name, d.get("authors") or []) if n],
        "last_updated": _str(card.get("updated_date") or card.get("created_date")),
    }
    if ident.get("version"):
        x["version"] = str(ident["version"])
    if pid := ident.get("primary_id"):
        x["persistent_id"] = _target(pid)
    if pub := d.get("dataset_publisher"):
        provider = {"organization": pub.get("name")}
        if url := (acc.get("access") or {}).get("publicly_facing_landing_page_url"):
            provider["url"] = url
        x["provider"] = provider
    if lic := reuse.get("license"):
        x["license"] = {k: lic[k] for k in ("spdx_id", "name", "url") if lic.get(k)}

    # Governance only from governed_use. Without it the card asserts nothing
    # about export control or privacy, so neither does the export.
    nsg = gov.get("non_sensitivity_governance_metadata") or {}
    if nsg:
        privacy = nsg.get("privacy") or {}
        x["governance"] = {k: v for k, v in (
            ("export_control_status", (nsg.get("export_control") or {}).get("export_control_status")),
            ("privacy_pii", privacy.get("pii_status")),
            ("privacy_phi", privacy.get("phi_status")),
        ) if v}
        x["governance"]["review_provenance"] = list(gov.get("review_provenance_companion") or [])

    rr = inter.get("related_resources") or {}
    rels = [{"type": RELATIONSHIPS.get(p.get("relationship"), "references"),
             "target": _target(p), "target_label": f"publication ({p.get('relationship')})"}
            for p in rr.get("publications") or []]
    for kind in ("datasets", "software", "ai_models"):
        for r in rr.get(kind) or []:
            if (r.get("identifier") or {}).get("value"):
                rels.append({"type": RELATIONSHIPS.get(r.get("relationship"), "references"),
                             "target": _target(r["identifier"]),
                             "target_label": f"{r.get('name')} ({r.get('relationship')})"})
    if rels:
        x["relationships"] = rels

    formats = [str(f) for f in ds.get("formats") or []]
    io = {"input_modes": [],
          "output_modes": [MIME.get(f.lower(), f"application/x-{f.lower()}") for f in formats],
          "modalities": list(ds.get("modalities") or []),
          "task_tags": list(desc.get("task_category") or []) + list(desc.get("task_subcategory") or [])}
    role = {"Yes": "intermediate", "No": "final"}.get((d.get("workflow") or {}).get("is_intermediate"))
    if role:
        io["dataset_role"] = role
    x["io_contract"] = io

    ext: dict = {"formats": formats, "schema_fields": list(ds.get("features") or [])}
    if ai:
        ext["ai_usage"] = ai
    x["extension"] = ext
    return {k: v for k, v in x.items() if v not in (None, "", [])}


def validate(x: dict) -> list[str]:
    from jsonschema import Draft202012Validator

    validator = Draft202012Validator(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))
    errors = [f"/{'/'.join(map(str, e.absolute_path))}: {e.message}" for e in validator.iter_errors(x)]
    if leaked := sorted(x.keys() & LINKML_MARKERS):
        errors.append(f"carries LinkML profile markers {leaked}; the registry rejects it as ambiguous")
    return errors


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Export a Genesis datacard as an xCard registry submission.")
    p.add_argument("card", type=Path, help="full Genesis datacard (.md)")
    p.add_argument("--out", type=Path, help="default: <card>.xcard.md beside the card")
    args = p.parse_args(argv)

    _, fm, body = args.card.read_text(encoding="utf-8").split("---\n", 2)
    x = export(yaml.safe_load(fm))
    if errors := validate(x):
        sys.stderr.write("export does not satisfy xcard.schema.json:\n" + "\n".join(errors) + "\n")
        return 1

    out = args.out or args.card.with_name(args.card.stem + ".xcard.md")
    note = (f"> Registry export of `{args.card.name}`, generated by export_xcard.py. "
            "The full Genesis datacard is the authoritative record; regenerate this file "
            "rather than editing it.\n\n")
    out.write_text("---\n" + yaml.safe_dump(x, sort_keys=False, allow_unicode=True, width=1000)
                   + "---\n" + note + body.lstrip("\n"), encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
