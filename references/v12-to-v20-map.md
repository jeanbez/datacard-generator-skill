# Genesis Datacard v1.2 → v2.0.0 conversion map

The authoritative mapping used by `scripts/convert_v12_to_v20.py`. Every row
is either a mechanical rewrite or a **report** — a value the converter refuses
to guess and hands back for a human to decide. Nothing is silently dropped.

Derived by diffing the v1.2 schema against the vendored v2.0.0 one, not by hand.

## Structure

The six `supports_*` flags and their containers (`discoverability`,
`accessibility`, `interoperability`, `reusability`, `governed_use`,
`ai_usability`) are **unchanged**. No class was removed. Field paths carry over.

## Version fields

| v1.2 | v2.0.0 | Why |
|---|---|---|
| `template_version: "1.2"` | `"2.0.0"` | tracks the template |
| `datacard_version: "1.2"` | `"1.0.0"` | v2 splits these: `datacard_version` is now the **card's own** version, incremented when the card is meaningfully updated. A v1.2 card never had one, so conversion starts it at `1.0.0` and says so in the report. |

## Required in v2.0.0, absent from v1.2

Computed with `SchemaView.class_induced_slots` on both schemas — a plain
`attributes` diff misses these, because the slots live at the schema's top
level and four classes changed by losing `is_a: NamedThing`.

`xCard` / `XCardClass.card_type` are **required** and have no v1.2 source, so
the converter writes `{card_type: dataset}`, the value the schema pins with
`equals_string`.

These became required and have no v1.2 source, so they are **reported**, never
invented:

| slot | note |
|---|---|
| `PersonClass.given_name` | a v1.2 card with a mononym or initials-only author now fails |
| `PersonClass.family_name` | same |
| `DataCardClass.sensitivity` | the datacard's own sensitivity, distinct from the dataset's |
| `DatasetIdentificationClass.project` | `discoverability.identification.project` — **not** `tags.project`, which was already required in v1.2 |
| `AIUsageClass.human_review_required` | only when `supports_ai_usability=Yes` |
| `MissingDataCodesClass.description` | alongside `code`, which was already required |
| `DomainMetadataFieldValueClass.field_value` | `name` was already required |

`relationship` is now required on `ai_model` and `software` agent entries. A
v1.2 card that omitted it is reported.

**Relaxed in v2** — no converter work, but worth knowing: `ContactClass.person`
(an organization-only contact is now legal), `DataCardClass.id`,
`IdentifierClass.type` and `SchemaReferenceClass.type` are all optional now.

## Shape changes — these break every existing card

Found by diffing slot cardinality and ranges, not names. Wrapping a single
value in a list is lossless, so these are mapped, not reported.

| Path | v1.2 | v2.0.0 |
|---|---|---|
| `discoverability.contact` | single | **list** |
| `discoverability.dataset_description.science_domain` | single string | **list** |
| `reusability.data_quality.missing_data_codes` | single block | **list** |
| `governed_use` `agreement_type` | single | **list** |
| `approved_environments` | free string | `ApprovedEnvironmentEnum` (`JUCE`, `CUI Approved Enclave`, `Classified Enclave`, `Cloud Enclave (Authorized)`) |
| `maintainer` | `AgentClass` — person, organization, ai_model or software | `MaintainerAgentClass` — **person or organization only**; an ai_model or software maintainer is reported |

### `identification.description` is gone

Legal in v1.2, rejected by v2 (`Additional properties are not allowed`). v2's
`DatasetDescriptionClass` has no generic long-form slot — it has
`dataset_summary`, `purpose`, `data_characteristics` and `limitations`. Where
the prose belongs is a judgement, so the converter reports it with its text
rather than relocating it.

## Enum rewrites

### RoleEnum — two values deleted

| v1.2 | v2.0.0 | Why |
|---|---|---|
| `Data_Curation` | `Data_Curator` | the card already asserted curation; the successor preserves that claim |
| `Data_Collection` | `Investigation` | CRediT defines Investigation as "performing the experiments, or data/evidence collection", so collection sits inside it |

v2 also adds DataCite roles (`Creator`, `Contact_Person`, `Data_Manager`, …).
Conversion does not retrofit them — it preserves what the old card claimed.
For **new** cards the skill prompts for the role and assumes no default.

### ExtendedRelationshipEnum — enum deleted, folded into RelationshipTypeEnum

v2 defines `generates` as "A (a tool, software, model, or agent) generates B",
so the directional sense is preserved rather than reinterpreted.

| v1.2 | v2.0.0 |
|---|---|
| `used_to_create` | `generates` |
| `used_to_process` | `processes` |
| `used_to_analyze` | `analyzes` |
| `recorded_by` | `collects` |
| `trained_on` | `is_trained_on` |
| `evaluated_on` | `is_evaluated_on` |

### ProductTypeEnum

| v1.2 | v2.0.0 |
|---|---|
| `Data` | `Dataset` |
| `Paper_or_Proceedings` | **report** — v2 splits this into `Journal_Article` and `Conference`; the old value cannot tell them apart |

### RelationshipTypeEnum

| v1.2 | v2.0.0 |
|---|---|
| `is_based_on` | `is_derived_from` — v2 defines it as "B is a source upon which A is based", which is what `is_based_on` meant |

### PrivacyControlBasisEnum

| v1.2 | v2.0.0 |
|---|---|
| `HIPPA` | `HIPAA` — upstream fixed the typo |

### DatasetTypeEnum — collapsed to one value

v2 keeps only `Instrument`, "for datasets that are instrument data products",
and the field is now `if_applicable`, so it is null for everything else. None of
the eleven v1.2 codes is equivalent:

| v1.2 | meaning | v2.0.0 |
|---|---|---|
| `IP` | Instrumentation/Protocols | **report** — the nearest candidate for `Instrument`, but it meant protocols and instrument specs, not an instrument's data product |
| `AS` | Automated Software | null, value reported |
| `MD` | Model | null, value reported — `product_type: Model` may now be the right home |
| `SM` | Specialized Mix | null, value reported — `product_type: Collection` may now be the right home |
| `I` | Interactive Resource | null, value reported |
| `FP` `GD` `IG` `IM` `MM` `ND` | figures, genomic, images, multimedia, numeric | null, value reported |

Because v2 widened `ProductTypeEnum` (adding `Model`, `Collection`,
`Computer_Related`, `Agent`), some of what `dataset_type` used to carry now
belongs in `product_type`. That is a judgement about the dataset, so the
converter reports the old code rather than relocating it.

## Orphans — no v2 home

| v1.2 | Note |
|---|---|
| `need_to_know_basis` | the slot **and** its `NeedToKnowBasisEnum` are gone from v2. Values were `Agreement_Defined`, `DGB_Exception_Waiver`, `Job_Duty`, `Mission_Need`, `Project_Program_Association`. Reported as an orphan with its value, so the governance rationale is not lost silently. |

## Fixed in v2: the publisher false positive

v1.2's "publisher is required when release_status = Approved or Published" rule
wrote its precondition as `in_subset: [Approved, Published]`. In LinkML
`in_subset` declares subset membership of a schema element, not a value test, so
the precondition was vacuous and the rule fired on **every** card, Draft
included. v2.0.0 replaces it with two `equals_string` rules, one per status.

The workaround this skill carried for v1.2 — treat that error as real only for
Approved or Published — is therefore **obsolete and must not be carried into
v2**. Left in place it would teach agents to ignore a now-correct error. The
converter suppresses nothing.

## Restored in v2

`interoperability.data_structure.temporal_coverage.description` exists again in
v2. It was removed from the v1.2 template as a defect — correct against v1.2,
wrong against v2 — so a converted card may carry it.
