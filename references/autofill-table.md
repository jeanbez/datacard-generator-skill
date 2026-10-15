# Auto-fill decision table

Which fields the skill fills from introspection or a registry, and which it
must ask about. Paths use the v2 capability-container structure. A DOI record
from step 2b takes precedence over README/CITATION.cff for every field in
`references/live-enrichment.md` § "What to extract".

| Genesis field | Auto-fill if… | Otherwise |
|---|---|---|
| `xCard.card_type` | always → `dataset`, written first. Required in v2 and pinned by the schema with `equals_string`; a card without it fails validation | never prompt |
| `discoverability.datacard.created_date` | always (today, ISO 8601) | — |
| `discoverability.datacard.updated_date` | `if_applicable` — leave blank on initial creation; only set on subsequent edits (see SKILL.md Gotcha #10) | — |
| `discoverability.datacard.creation_method` | always → `"Hybrid"` (Title case in v2) | — |
| `discoverability.datacard.template_version` | always → `"2.0.0"` (the vendored template version) on `stable`; `"2.1.0"` on `provisional` (the card carries the spine) | — |
| `discoverability.datacard.datacard_version` | always → `"1.0.0"` on initial creation; bump alongside each new `change_log` entry. **Required** — the schema's `ifabsent` default is not applied by `linkml-validate`, so an omitted value fails | — |
| `discoverability.datacard.change_log[0]` | always (`change_date`, `datacard_version: "1.0.0"` — the card's own version, not the template's, "Initial creation" or "Converted from …") | — |
| `discoverability.datacard.filename` | computed from `discoverability.identification.name` (see SKILL.md §8 Filename rule) | — |
| `discoverability.datacard.language` | always → `en` (override if README is non-English) | — |
| `discoverability.datacard.created_by[]` | always (AI model first if Hybrid; see `references/gotchas.md`) | — |
| `discoverability.identification.name` | from README / CITATION.cff title | prompt |
| `discoverability.identification.version` | from CITATION.cff or default `"1.0"` | prompt |
| `discoverability.product_type` | never — `ProductTypeEnum` (see `references/lookup-tables.md`) | always prompt |
| `discoverability.datacard.id` | never — `IdentifierClass` (`{type: local, value: <slug>}` for pre-publication is a sensible default) | prompt |
| `discoverability.dataset_description.dataset_summary` | from README first paragraph | prompt |
| `discoverability.dataset_description.keywords` | from README / CITATION.cff | prompt |
| `interoperability.data_structure.formats` | introspect.py `formats` | prompt (requires `supports_interoperability=Yes`) |
| `interoperability.data_structure.features` | introspect.py `sample_columns` — always objects (`- name: x`), never bare strings | prompt |
| `interoperability.data_structure.splits` | introspect.py `splits_detected` | leave empty |
| `accessibility.dataset_scale.record_count` / `.compressed_bytes` | introspect.py | prompt (requires `supports_accessibility=Yes`) |
| `reusability.license.spdx_id` | introspect.py `license_hint`, mapped via `introspection-commands.md` §3.4 — never written verbatim: `spdx_id` has no pattern, so a whole sentence validates clean and lands in the spine | prompt (requires `supports_reusability=Yes`) |
| `reusability.license.name` | never | prompt whenever a `license` block is emitted. `gen-json-schema` ignores the schema's `slot_usage.name.required: false`, so `linkml-validate` requires it unconditionally — and a rule requires it anyway when `spdx_id` is `Other` |
| `discoverability.authors[]` | from CITATION.cff (ask for `role[]` — CRediT **plus DataCite** in v2, and never assumed — see `references/lookup-tables.md`) | prompt |
| `reusability.citation.preferred_citation` | from CITATION.cff bibtex | prompt at `[pub]` |
| `interoperability.provenance.was_generated_by` | always prompt (often forgotten) | — |
| `discoverability.dataset_description.science_domain` | never auto-filled — closed `ScienceDomainEnum` (see `references/lookup-tables.md`) | prompt |
| `ai_usability.ai_usage.training_use_status` / `.inference_use_status` / `.evaluation_use_status` | never auto-filled | prompt (`Yes \| No \| Conditional`); if `Conditional`, also prompt for the matching `*_use_conditions` free-text field |
| `_repository.*` | **NEVER** — system-owned | — |

For each `supports_X=Yes`, also write `supports_X: "Yes"` at the top level of
the YAML. The schema enforces that the matching `X:` block must exist when
`supports_X=Yes`.

Identifiers gathered here are **cross-checked live in step 7** — not optional.
