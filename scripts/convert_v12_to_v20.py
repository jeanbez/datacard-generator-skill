# /// script
# requires-python = ">=3.10"
# dependencies = ["linkml>=1.9.3", "pyyaml>=6.0"]
# ///
"""Convert a Genesis Mission Datacard v1.2 to v2.0.0.

The mapping is documented in `references/v12-to-v20-map.md`, which is the
reference to read first; this script is its implementation.

Three kinds of outcome, and the distinction is the point:

  mapped     rewritten mechanically (enum renames, version fields, xCard)
  reported   a value v2 cannot represent unambiguously. Carried into the
             report with its old value so a human decides. Never guessed.
  orphans    no v2 home at all. Reported rather than silently dropped.

Schema validation is upstream's `linkml.validator` against the vendored
v2.0.0 schema, so "required property" results are folded into the report:
a converted card that still needs human input says which fields.

No findings are suppressed. v1.2 needed a workaround because its
dataset_publisher rule fired on every card — its precondition used
`in_subset`, which is not a value test. v2.0.0 replaced that with two
`equals_string` rules, so the rule is correct and every result here is real.

Run it with uv; dependencies are declared inline:

    uv run scripts/convert_v12_to_v20.py <card>.md [--json] [--out FILE]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from dataclasses import dataclass, field
from datetime import date, datetime, time
from pathlib import Path
from typing import Any

import yaml

SKILL_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = Path(__file__).resolve().parent / "genesis_datacard.yaml"
TARGET_CLASS = "GenesisDatacardClass"

# --spine validates against the provisional overlay instead. See that file's
# header: the spine exists because the xCards registry reads pre-container
# paths and cannot be changed.
SPINE_SCHEMA_PATH = Path(__file__).resolve().parent / "genesis_datacard_v2_1_provisional.yaml"
SPINE_TARGET_CLASS = "GenesisDatacardSpinedClass"

# The registry's SensitivityLevel is only general | reviewed | restricted |
# unknown, and it uses it for access filtering. Map conservatively: anything
# controlled becomes `restricted`, because under-restricting is the dangerous
# direction. `Mixed` means part of the dataset is controlled, so it is not
# `general` either.
#
# Note the registry treats `unknown` as PUBLIC-visible (Clearance.PUBLIC covers
# {GENERAL, UNKNOWN}), so leaving this unset is NOT the safe default — an
# unmappable value must become `restricted`.
_SENSITIVITY = {
    "Public": "general",
    "Unclassified_Uncontrolled": "general",
    "CUI": "restricted",
    "UCNI": "restricted",
    "Classified": "restricted",
    "Legacy_Controlled": "restricted",
    "Other_Controlled": "restricted",
    "Mixed": "restricted",
}


TEMPLATE_VERSION = "2.0.0"
# A card carrying the provisional spine is no longer a plain v2.0.0 card, so it
# declares the provisional template version instead.
PROVISIONAL_TEMPLATE_VERSION = "2.1.0"
# v2 splits the two: datacard_version is the card's own version, so a v1.2
# card (which only ever carried the template version here) starts at 1.0.0.
INITIAL_DATACARD_VERSION = "1.0.0"

ROLE_MAP = {"Data_Curation": "Data_Curator", "Data_Collection": "Investigation"}

RELATIONSHIP_MAP = {
    "used_to_create": "generates",
    "used_to_process": "processes",
    "used_to_analyze": "analyzes",
    "recorded_by": "collects",
    "trained_on": "is_trained_on",
    "evaluated_on": "is_evaluated_on",
    "is_based_on": "is_derived_from",
}

PRIVACY_MAP = {"HIPPA": "HIPAA"}

# v2 dropped `description` from six classes (four lost `is_a: NamedThing`, two
# lost the inherited slot). These are the slot names that carry them, so a
# `description` directly inside one of these is no longer legal. Keyed on the
# parent slot rather than the key name, because `description` is still legal on
# TemporalCoverage, SpatialCoverage, MissingDataCodes, Location, Dataset,
# SourceDataset, Publisher, Feature, Creator and DomainMetadata.
DESCRIPTION_DROPPED_UNDER = (
    "identification", "organization", "sponsor_organizations",
    "research_organizations", "facilities", "facility", "data_services",
)

# Single value in v1.2, list in v2.0. Wrapping is lossless, so these are
# mapped rather than reported.
NOW_MULTIVALUED = ("contact", "science_domain", "missing_data_codes", "agreement_type")

# The six GenesisDatacardSpinedClass attributes, cleared before every projection
# so a stale block cannot outlive its source.
SPINE_KEYS = ("datacard", "identification", "categorization", "dataset_info",
              "license", "description")

# MaintainerAgentClass accepts only person or organization; v1.2's AgentClass
# also allowed ai_model and software, which have no v2 home here.
MAINTAINER_ALLOWED = ("person", "organization")

PRODUCT_TYPE_MAP = {"Data": "Dataset"}
# v2 splits Paper_or_Proceedings into Journal_Article and Conference, and the
# old value cannot tell them apart.
PRODUCT_TYPE_REPORT = {
    "Paper_or_Proceedings": "v2 splits this into Journal_Article and Conference; pick one",
}

DATASET_TYPE_MEANING = {
    "AS": "Automated Software", "FP": "Figure/Plot", "GD": "Genome/Genetic Data",
    "I": "Interactive Resource", "IG": "Integrated Genomic Resources", "IM": "Image",
    "IP": "Instrumentation/Protocols", "MD": "Model", "MM": "Multimedia",
    "ND": "Numeric Data", "SM": "Specialized Mix",
}
DATASET_TYPE_HINT = {
    "IP": "nearest candidate for v2 `Instrument`, but IP meant protocols and specs, not an instrument data product",
    "MD": "`product_type: Model` may now be the right home",
    "SM": "`product_type: Collection` may now be the right home",
    "AS": "`product_type: Computer_Related` may now be the right home",
}


@dataclass
class Report:
    genesis: dict
    mapped: list[str] = field(default_factory=list)
    reported: list[str] = field(default_factory=list)
    orphans: list[str] = field(default_factory=list)
    missing_required: list[str] = field(default_factory=list)
    invalid: list[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return {
            "mapped": self.mapped,
            "reported": self.reported,
            "orphans": self.orphans,
            "missing_required": self.missing_required,
            "invalid": self.invalid,
        }


def _isoformat_dates(value: Any) -> Any:
    """Render YAML date/time scalars as ISO strings; the schema wants strings."""
    if isinstance(value, dict):
        return {k: _isoformat_dates(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_isoformat_dates(v) for v in value]
    if isinstance(value, (date, datetime, time)):
        return value.isoformat()
    return value


def load_card(path: Path) -> tuple[dict, str]:
    """Return (frontmatter, markdown body) for a .md card, or (data, '') for .yaml."""
    text = Path(path).read_text(encoding="utf-8")
    if path.suffix in {".yaml", ".yml"}:
        return _isoformat_dates(yaml.safe_load(text)), ""
    parts = re.split(r"^---\s*$", text, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        raise ValueError(f"{path}: expected YAML frontmatter delimited by `---` lines")
    data = yaml.safe_load(parts[1])
    if not isinstance(data, dict):
        raise ValueError(f"{path}: frontmatter is not a YAML mapping")
    return _isoformat_dates(data), parts[2]


def _walk(node: Any, path: str, report: Report, parent_slot: str = "") -> Any:
    """Rewrite enum values wherever they appear, recording each change.

    `parent_slot` is the slot name this node sits under, which is how the
    description-dropped-in-v2 classes are identified without a schema.
    """
    if isinstance(node, list):
        return [_walk(v, f"{path}[{i}]", report, parent_slot) for i, v in enumerate(node)]
    if not isinstance(node, dict):
        return node

    out: dict[str, Any] = {}
    for key, value in node.items():
        here = f"{path}.{key}" if path else key

        # `role` lists live inside every agent sub-block (person, organization,
        # ai_model, software), so rewrite them wherever they turn up.
        if key == "role" and isinstance(value, list):
            new = []
            for v in value:
                if v in ROLE_MAP:
                    report.mapped.append(f"{here}: {v} -> {ROLE_MAP[v]}")
                    new.append(ROLE_MAP[v])
                else:
                    new.append(v)
            out[key] = new
            continue

        # `relationship` covers both the deleted ExtendedRelationshipEnum on
        # agents and RelationshipTypeEnum on related resources. The two value
        # sets are disjoint, so one map is unambiguous.
        if key == "relationship" and isinstance(value, str) and value in RELATIONSHIP_MAP:
            report.mapped.append(f"{here}: {value} -> {RELATIONSHIP_MAP[value]}")
            out[key] = RELATIONSHIP_MAP[value]
            continue

        if key in NOW_MULTIVALUED and value is not None and not isinstance(value, list):
            report.mapped.append(f"{here}: wrapped as a list (multivalued in v2)")
            out[key] = [_walk(value, f"{here}[0]", report, key)]
            continue

        if key == "maintainer" and isinstance(value, dict):
            bad = [k for k in value if k not in MAINTAINER_ALLOWED]
            if bad:
                report.reported.append(
                    f"{here} uses {', '.join(bad)}: v2 narrows maintainer to "
                    "MaintainerAgentClass, which allows only person or organization"
                )
            kept = {k: v for k, v in value.items() if k in MAINTAINER_ALLOWED}
            if len(kept) > 1:
                # MaintainerAgentClass carries two rules: person present implies
                # organization absent, and the converse. Keeping both writes a card
                # that fails validation with an opaque anyOf dump naming neither.
                report.reported.append(
                    f"{here} carries both person and organization: v2 allows exactly "
                    "one, so the organization was dropped — if it was the real "
                    "maintainer, swap it back in and drop the person"
                )
                kept = {"person": kept["person"]}
            if kept:
                # _walk, not a bare copy: the kept subtree still holds v1.2 enums
                # (a maintainer role of Data_Curation) that need rewriting.
                out[key] = _walk(kept, here, report, key)
            continue

        if key == "need_to_know_basis":
            report.orphans.append(
                f"{here} = {value!r} (dropped: the slot and NeedToKnowBasisEnum are gone from v2; "
                "record the governance rationale elsewhere if it still applies)"
            )
            continue

        # privacy_control_basis is multivalued in both versions, so a scalar
        # test never fired and HIPPA survived into v2. Handle both shapes.
        if key == "privacy_control_basis":
            if isinstance(value, list):
                new = []
                for v in value:
                    if v in PRIVACY_MAP:
                        report.mapped.append(f"{here}: {v} -> {PRIVACY_MAP[v]}")
                        new.append(PRIVACY_MAP[v])
                    else:
                        new.append(v)
                out[key] = new
            elif isinstance(value, str) and value in PRIVACY_MAP:
                report.mapped.append(f"{here}: {value} -> {PRIVACY_MAP[value]}")
                out[key] = PRIVACY_MAP[value]
            else:
                out[key] = value
            continue

        # --- 3. approved_environments became an enum; free text cannot be mapped
        if key == "approved_environments" and value:
            report.reported.append(
                f"{here} = {value!r}: v2 ranges this over ApprovedEnvironmentEnum "
                "(JUCE | Classified Enclave | CUI Approved Enclave | "
                "Cloud Enclave (Authorized)). Free text cannot be mapped to one, "
                "so the slot is dropped — re-enter it if it still applies"
            )
            continue

        # --- 2. a `description` directly under one of these slots is illegal in v2
        if key == "description" and parent_slot in DESCRIPTION_DROPPED_UNDER:
            text = str(value)
            preview = text if len(text) <= 100 else text[:97] + "..."
            report.reported.append(
                f"{here} removed (v2 drops description from this class). Text was: "
                f"{preview!r} — move it into a slot the class still has, or into "
                "the card's narrative body"
            )
            continue

        out[key] = _walk(value, here, report, key)
    return out


def convert(v12: dict, *, spine: bool = False) -> Report:
    report = Report(genesis={})
    g = _walk(v12, "", report)

    # xCard is required in v2; card_type is fixed to `dataset` for every
    # Genesis data card (the schema pins it with equals_string).
    if "xCard" not in g:
        g = {"xCard": {"card_type": "dataset"}, **g}
        report.mapped.append("xCard: added {card_type: dataset} (required in v2)")

    d = g.get("discoverability") or {}
    card = d.get("datacard") or {}

    if card:
        target = PROVISIONAL_TEMPLATE_VERSION if spine else TEMPLATE_VERSION
        if card.get("template_version") != target:
            report.mapped.append(
                f"discoverability.datacard.template_version: "
                f"{card.get('template_version')!r} -> {target!r}"
            )
            card["template_version"] = target
        old_dv = card.get("datacard_version")
        card["datacard_version"] = INITIAL_DATACARD_VERSION
        report.mapped.append(
            f"discoverability.datacard.datacard_version: {old_dv!r} -> "
            f"{INITIAL_DATACARD_VERSION!r} (v2 makes this the card's own version, "
            "not the template's; increment it on future edits)"
        )
        # Historical entries are left alone: each records which version that
        # change produced, and rewriting them all to 1.0.0 erases the history
        # the log exists for. Only the card's own version resets.

    pt = d.get("product_type")
    if pt in PRODUCT_TYPE_MAP:
        report.mapped.append(f"discoverability.product_type: {pt} -> {PRODUCT_TYPE_MAP[pt]}")
        d["product_type"] = PRODUCT_TYPE_MAP[pt]
    elif pt in PRODUCT_TYPE_REPORT:
        report.reported.append(f"discoverability.product_type = {pt!r}: {PRODUCT_TYPE_REPORT[pt]}")
        d.pop("product_type", None)

    dt = d.get("dataset_type")
    if dt is not None:
        meaning = DATASET_TYPE_MEANING.get(dt, "unrecognised v1.2 code")
        hint = DATASET_TYPE_HINT.get(dt)
        note = f"discoverability.dataset_type = {dt!r} ({meaning}): v2 keeps only `Instrument`"
        report.reported.append(note + (f"; {hint}" if hint else "; leave null unless this is an instrument data product"))
        d.pop("dataset_type", None)

    if spine:
        projected, notes = project_spine(g)
        # Clear every spine key, then merge. The projection is derived, so it
        # wins — but merging alone only replaced the keys the projection
        # produced, so a block whose container source had been removed survived
        # from an earlier run while the report said it was absent, and the
        # registry read the stale copy.
        g = {k: v for k, v in g.items() if k not in SPINE_KEYS}
        g = {**g, **projected}
        report.mapped.append(
            f"xCards registry spine projected ({len(projected)} blocks) — provisional, "
            "not an upstream v2.1 release"
        )
        report.reported.extend(notes)

    report.genesis = g
    schema_missing, invalid = _validate(g, spine=spine)
    report.missing_required = sorted(schema_missing)
    report.invalid = invalid
    return report


def project_spine(g: dict) -> tuple[dict, list[str]]:
    """Project the xCards registry spine from the capability containers.

    The spine duplicates facts the containers already hold, at the top-level
    paths the registry reads. It is a projection, never a source of truth: on
    any disagreement the container wins. Every value is derived, so nothing
    here is ever prompted for or invented.
    """
    d = g.get("discoverability") or {}
    card = d.get("datacard") or {}
    ident = d.get("identification") or {}
    desc = d.get("dataset_description") or {}
    tags = desc.get("tags") or {}
    structure = (g.get("interoperability") or {}).get("data_structure") or {}

    science = desc.get("science_domain")
    if isinstance(science, list):
        science = science[0] if science else None

    spine: dict[str, Any] = {}
    notes: list[str] = []

    if card.get("id") or card.get("datacard_version"):
        block: dict[str, Any] = {}
        if (card.get("id") or {}).get("value"):
            block["id"] = {"value": card["id"]["value"]}
        if card.get("datacard_version"):
            block["datacard_version"] = card["datacard_version"]
        spine["datacard"] = block

    if ident.get("name"):
        spine["identification"] = {"name": ident["name"]}
        if ident.get("version"):
            spine["identification"]["version"] = ident["version"]
    else:
        notes.append(
            "spine: identification.name could not be projected — the registry's "
            "validator errors without a title"
        )

    summary = desc.get("dataset_summary")
    if summary:
        spine["description"] = {"summary": summary}
    else:
        notes.append("spine: no dataset_summary to project — the registry records an empty description")

    # v2 deliberately splits these two, and the schema says so: DataCardClass
    # .sensitivity is "the sensitivity of the DATA CARD itself ... not the
    # dataset", while DiscoverabilityClass.sensitivity is the dataset's. The
    # registry filters *access to the dataset*, so the dataset's block governs —
    # and where they disagree the stricter of the two wins, because a CUI dataset
    # described by a deliberately shareable Public card is the normal
    # arrangement and the reason v2 separated them.
    _ORDER = {"general": 0, "reviewed": 1, "restricted": 2}
    candidates = [
        (d.get("sensitivity") or {}).get("overall_sensitivity"),
        (card.get("sensitivity") or {}).get("overall_sensitivity"),
    ]
    risk = None
    for overall in [c for c in candidates if c]:
        mapped = _SENSITIVITY.get(overall)
        if mapped is None:
            # Unmappable: restrict rather than leave it unset, since the registry
            # reads an absent risk tag as UNKNOWN and serves that to PUBLIC.
            risk = "restricted"
            notes.append(
                f"spine: overall_sensitivity {overall!r} has no mapping to the "
                "registry's general|reviewed|restricted — projected `restricted`, "
                "because an unset tag reads as UNKNOWN which the registry treats "
                "as publicly visible"
            )
            break
        if risk is None or _ORDER[mapped] > _ORDER[risk]:
            risk = mapped

    # overall_sensitivity is a display/discovery summary — the vendored schema
    # says in so many words that it is "not ... the sole governance basis". The
    # control status flags are, and nothing stops a card pairing
    # `overall_sensitivity: Public` with `cui_status: Yes`: the schema's rules
    # all have overall_sensitivity as their precondition, so there is no reverse
    # check. Escalate on the flags, in either block.
    flagged = []
    for s in (d.get("sensitivity") or {}, card.get("sensitivity") or {}):
        flagged += [k for k in ("classified_status", "cui_status", "ucni_status")
                    if s.get(k) == "Yes"]
        # Legacy_Controlled and Other_Controlled have no status flag at all, so
        # the three above would leave those two categories relying on
        # overall_sensitivity alone. source_marking_scheme is required and is
        # the authoritative marking regime; normalized_control_basis is the
        # interpreted control basis. A genuinely public card carries the
        # scheme's own `None` value and either no basis or Public_Release_Approved.
        if s.get("source_marking_scheme") not in (None, "", "None"):
            flagged.append("source_marking_scheme")
        if set(s.get("normalized_control_basis") or []) - {"Public_Release_Approved"}:
            flagged.append("normalized_control_basis")
    if flagged and risk != "restricted":
        notes.append(
            f"spine: {sorted(set(flagged))} say Yes while overall_sensitivity maps to "
            f"{risk!r} — projected `restricted`; reconcile the sensitivity block"
        )
        risk = "restricted"

    cat: dict[str, Any] = {}
    tag_block = {k: v for k, v in (("project", tags.get("project")), ("science", science), ("risk", risk)) if v}
    if tag_block:
        cat["tags"] = tag_block
    for key in ("task_category", "task_subcategory"):
        if desc.get(key):
            # Copy, don't share: a shared list makes yaml.safe_dump emit an
            # anchor in the spine and an alias in the container, so deleting
            # the spine by hand leaves an undefined alias and the card stops
            # parsing entirely.
            cat[key] = list(desc[key])
    if cat:
        spine["categorization"] = cat
    for missing in ("project", "science"):
        if not tag_block.get(missing):
            notes.append(f"spine: categorization.tags.{missing} absent — the registry warns, and strict mode fails")
    if not tag_block.get("risk"):
        notes.append(
            "spine: categorization.tags.risk absent — no sensitivity to project, and the "
            "registry reads an absent tag as UNKNOWN, which it serves to PUBLIC"
        )

    lic = (g.get("reusability") or {}).get("license") or {}
    lic_block = {k: lic[k] for k in ("spdx_id", "name", "url") if lic.get(k)}
    if lic_block:
        spine["license"] = lic_block
    else:
        notes.append("spine: no license to project — the registry records no license")

    formats = structure.get("formats") or []
    if formats:
        spine["dataset_info"] = {"data_formats": list(formats)}
        if structure.get("modalities"):
            # The registry's IOContract.modalities is the semantic typing the
            # composer reads; without it the dataset registers untyped.
            spine["dataset_info"]["modalities"] = list(structure["modalities"])
        # No warning on unknown formats: the registry falls back to
        # application/x-<token>, so nothing is ever dropped from output_modes. A
        # local copy of its MIME table had diverged in both directions and was
        # producing false claims either way.
    else:
        notes.append(
            "spine: no formats to project — output_modes stays empty and the dataset "
            "registers but is not composable"
        )

    return spine, notes


def _validate(data: dict, *, spine: bool = False) -> tuple[set[str], list[str]]:
    """Validate the converted card and split the findings two ways.

    Returns (missing_required, invalid): fields the mapping could not fill, and
    every other finding — bad enums, unexpected keys, pattern and rule
    violations. Both are returned because reporting only the first silently
    writes invalid cards.
    """
    from linkml.validator import validate_file

    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False, encoding="utf-8") as fh:
        yaml.safe_dump(data, fh, sort_keys=False, allow_unicode=True)
        tmp = Path(fh.name)

    schema = SPINE_SCHEMA_PATH if spine else SCHEMA_PATH
    # The provisional overlay imports the vendored schema by bare name. The
    # linkml CLI resolves that against the schema file's directory, but the
    # Python API resolves it against the process cwd, so run from there. Both
    # paths here are absolute, so nothing else is affected.
    cwd = Path.cwd()
    try:
        os.chdir(schema.parent)
        result = validate_file(
            str(tmp),
            schema=str(schema),
            target_class=SPINE_TARGET_CLASS if spine else TARGET_CLASS,
        )
    finally:
        os.chdir(cwd)
        tmp.unlink(missing_ok=True)

    missing: set[str] = set()
    invalid: list[str] = []
    for item in result.results:
        message = str(item.message)
        match = re.match(r"'([^']+)' is a required property", message)
        if not match:
            # Not "a value is missing" — the card breaks the schema in a way no
            # prompt fixes. Dropping these reported a clean conversion of an
            # invalid card.
            invalid.append(message)
            continue
        where = re.search(r" in (/\S*)$", message)
        prefix = (where.group(1).strip("/").replace("/", ".") + ".") if where and where.group(1) != "/" else ""
        missing.add(f"{prefix}{match.group(1)}")
    return missing, invalid


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Convert a Genesis Datacard v1.2 to v2.0.0.")
    p.add_argument("file", type=Path, help="v1.2 datacard (.md or .yaml)")
    p.add_argument("--out", type=Path, help="write the converted card here")
    p.add_argument("--json", dest="emit_json", action="store_true", help="machine-readable report")
    p.add_argument("--spine", action="store_true",
                   help="also project the provisional xCards registry spine and set "
                        "template_version 2.1.0 (not an upstream release; to register, "
                        "run export_xcard.py on the result)")
    p.add_argument("--preserve-body", action="store_true",
                   help="carry the markdown body across unchanged (it is v1.2 prose; review it)")
    p.add_argument("--no-keep-source", action="store_true",
                   help="do not keep a copy of the v1.2 source beside the output "
                        "(the default keeps one, because v2 is a provisional upgrade)")
    args = p.parse_args(argv)

    data, body = load_card(args.file)
    report = convert(data, spine=args.spine)

    if args.out:
        # v2 is a provisional upgrade, so the v1.2 original has to survive it.
        # Refuse to write over the source rather than destroying the only copy.
        if args.out.resolve() == args.file.resolve():
            sys.stderr.write(
                f"refusing to overwrite the v1.2 source at {args.file}. "
                "Choose a different --out; the original is the rollback path.\n"
            )
            return 2

        kept: Path | None = None
        if not args.no_keep_source:
            kept = args.out.with_name(args.out.stem + ".v1.2-source" + args.file.suffix)
            if kept.resolve() != args.file.resolve():
                kept.write_text(args.file.read_text(encoding="utf-8"), encoding="utf-8")

        # Record where the card came from, in the card, so the rollback path
        # survives being moved away from this terminal.
        if kept is not None:
            card_block = ((report.genesis.get("discoverability") or {}).get("datacard"))
            if isinstance(card_block, dict):
                # A new entry, not an edit to log[0]: that is the chronologically
                # first entry, and appending there made the original creation
                # record claim to be today's conversion.
                # .get, not .setdefault: a `change_log:` key holding null makes
                # setdefault return None and the entry vanish silently.
                log = card_block.get("change_log")
                if not isinstance(log, list):
                    if log not in (None, ""):
                        # Don't discard it silently: the schema needs a list, but
                        # whatever prose was here is the card's only history.
                        report.orphans.append(
                            f"discoverability.datacard.change_log = {log!r} "
                            "(replaced: v2 needs a list of entries — fold this text "
                            "into a change_log entry's summary)"
                        )
                        # The validation report was computed before this swap, so
                        # it still carries the is-not-of-type-array error for a
                        # card that is now valid. Drop that one finding.
                        report.invalid = [
                            m for m in report.invalid
                            if "/discoverability/datacard/change_log" not in m
                        ]
                    log = card_block["change_log"] = []
                log.append({
                    "change_date": date.today().isoformat(),
                    "datacard_version": INITIAL_DATACARD_VERSION,
                    "summary": f"Converted from Genesis v1.2; source kept as {kept.name}",
                })

        text = "---\n" + yaml.safe_dump(report.genesis, sort_keys=False, allow_unicode=True) + "---\n"
        if args.preserve_body and body:
            text += body
        args.out.write_text(text, encoding="utf-8")
        if kept is not None:
            report.mapped.append(f"v1.2 source kept at {kept.name} (rollback path)")

    if args.emit_json:
        print(json.dumps(report.as_dict(), indent=2))
    else:
        for label, items in (("mapped", report.mapped), ("needs a decision", report.reported),
                             ("orphaned", report.orphans), ("still missing", report.missing_required)):
            print(f"\n{label} ({len(items)}):")
            for i in items:
                print(f"  - {i}")
        if report.invalid:
            print(f"\nINVALID — the written card does not validate ({len(report.invalid)}):")
            for message in report.invalid:
                print(f"  - {message}")
            print("\nFix these before using the card; a missing-required prompt will not.")
    # A missing required property fails linkml-validate just as an invalid value
    # does, so `convert && register` must not proceed on either.
    return 1 if (report.invalid or report.missing_required) else 0


if __name__ == "__main__":
    sys.exit(main())
