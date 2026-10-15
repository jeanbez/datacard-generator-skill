# Registry export — submitting a card to the xCard registry

Read this at the end of SKILL.md step 10 (`provisional` only).

## Why the full card cannot be submitted

The HPDF xCard registry picks its validator from a card's top-level keys:
`xCard` selects its xCard spine schema, while `supports_*` and the capability
containers select the Genesis LinkML schema. A card with both is rejected as
"profile markers are ambiguous" — and Genesis v2 requires both, so every full
card is refused. The endpoint reports only a generic `422 invalid_xcard`
("does not satisfy the DataCard schema"), so the cause is not visible from
outside. The provisional spine does not help: it is shaped for the discovery
engine's parser, not for the registry's `xcard.schema.json`.

## Export

```bash
uv run -q <skill_root>/scripts/export_xcard.py <written_file>
```

It writes `<card>.xcard.md` beside the card, validated against the vendored
`scripts/xcard.schema.json`, and exits 1 naming each problem if it cannot.
Submit that file, never the full card:

- `POST /api/current/registry/data_card` to create,
  `PUT /api/current/registry/data_card/<id>` to replace
- content type `text/vnd.genesis.data-card+markdown`

## What the export carries

The export is a projection: fix the full card and re-export rather than
editing it. It carries name, summary, science domains, keywords, authors (as
names), DOI, version, license, related publications/datasets/software,
formats, column list, modalities, task tags and the AI-use policy, plus the
full narrative body.

It drops ORCIDs, affiliations, contacts, sponsors, provenance, quality notes,
checksums and access rules as structured fields — the narrative body keeps
them — so the full card stays the authoritative record.

- `sensitivity` comes from the same projection as the spine's `tags.risk`
  (`project_spine()`), so a controlled dataset cannot export as `general`.
- Export-control and privacy flags are filled only from `governed_use`; a card
  without it exports without them rather than asserting `No`.
- `xCard.version` is the card's `template_version` (`2.1.0` for provisional).

## Vendored schema

`scripts/xcard.schema.json` is copied from the HPDF xCard registry image
(genesis-discovery-engine revision `7fe6d044`). Re-copy it when the registry
updates.
