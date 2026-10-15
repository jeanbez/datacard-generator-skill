# Validation extras

Schema validation is upstream's `linkml-validate` against
`scripts/genesis_datacard.yaml` (see SKILL.md step 9). This skill ships no
validator of its own.

The rules below are the ones the schema cannot express. Nothing checks them
for you — confirm each by eye before you call a card done.

## Filename rule (warn)

`datacard.filename` must equal `genesis_datacard_<snake_case(identification.name)>.md`,
where `snake_case` lowercases the dataset name, replaces any non-alphanumeric
run with a single underscore, and strips a leading or trailing underscore —
the schema's own pattern on `filename` rejects both.

- Severity: `warn` (informational; doesn't block validation)
- Path checked (v2): `discoverability.datacard.filename` ↔ `discoverability.identification.name`
- Legacy path checked: `datacard.filename` ↔ `identification.name` (for v1-shaped datacards)

## Workflow ↔ release_status alignment (warn)

The workflow state of the dataset should align with its release status. Mismatches
are not errors but should be flagged.

| `workflow.state` | Typical `release_status` |
|---|---|
| `Raw` / `Processing` / `QA` / `Analysis` | `Draft` |
| `Review` | `Under_Review` |
| `Embargo` / `Published` | `Approved` or `Published` |
| `Archived` | `Deprecated` or `Published` |

- Severity: `warn`
- Paths checked (v2): `discoverability.workflow.state` ↔ `discoverability.release_status`
- Legacy paths checked: `workflow.state` ↔ `release_status`

## Why the schema cannot express these

`scripts/genesis_datacard.yaml` covers required fields, enums, and format
patterns. It does not express:

- **Severity.** A LinkML result is pass/fail. The filename mismatch and the
  workflow/release misalignment are advisory — a card can be correct and
  still trip them — so they are not schema rules.
- **Cross-field slug computation.** The filename rule needs
  `snake_case(identification.name)` computed and compared against
  `filename`; the schema can only check the filename's own pattern.
- **Recommendation vs constraint.** The workflow/release pairings are
  typical, not required. Cards in transitional states are valid.

## The publisher rule — fixed in v2.0.0, do not work around it

**Every validator finding is real. Nothing here is suppressed.**

This note exists because the opposite used to be true, and the old
workaround is dangerous to carry forward. In v1.2 the rule
"publisher is required when release_status is Approved or Published" wrote
its precondition as `in_subset: [Approved, Published]`. In LinkML
`in_subset` declares subset membership of a schema element rather than
testing a value, so the precondition was vacuous and
`'dataset_publisher' is a required property` fired on **every** card,
Draft included. The skill therefore told agents to ignore it unless the card
was Approved or Published.

v2.0.0 replaces that with two separate `equals_string` rules, one per
status. The rule is now correct, so ignoring the error would hide a genuine
missing publisher on a published card.

## Quote your Yes/No

Unquoted `Yes` and `No` are YAML booleans, and every one of these slots has
range `string` or a `Yes`/`No` enum. One unquoted value cascades: a card with
bare flags throws `True is not of type 'string'` a dozen times. Quote the six
`supports_*` flags, the six `sensitivity` statuses (`classified_status`,
`cui_status`, `ucni_status` in both sensitivity blocks), every `*_use_status`,
every governance Yes/No, and the three that are none of those —
`reusability.integrity.checksum_available`,
`discoverability.workflow.is_intermediate` and
`accessibility.access.intended_repositories[].is_primary` — as the template
does.

## Quote your versions

Every version slot is a `string` with pattern `^\d+\.\d+(\.\d+)?$`, and a
two-component value written bare is a YAML float: `version: 1.0` fails with
`1.0 is not of type 'string'`. (A three-component `1.0.0` is already a string,
which is why this only bites the short form — and the short form is what both
"start at 1.0" and a model ID like `gpt-5.5` produce.) Quote
`identification.version`, `datacard.template_version`,
`datacard.datacard_version`, `change_log[].datacard_version`,
`created_by[].creator.ai_model.version`, `.software.version`,
`related_resources.software[].version` and `data_structure.schema_version`.

## Quote `citation.preferred_citation.year`

Range `string`, pattern `^\d{4}$`. It is not date-shaped, so the rule below
does not catch it, and the prompt asks for structured fields rather than a
BibTeX string — which is exactly what produces `year: 2019` as a YAML int and
`2019 is not of type 'string'`. Write `year: "2019"`.

## Quote your dates

`created_date: 2026-09-21` unquoted is a YAML date object, not a string.
Quote every date, as the template does. Most date slots
(`change_date`, `valid_until`, `review_date`, `contribution_date`,
`accessed_date`, `start_date`, `end_date`, `date_deposited`,
`dates.issued`, `dates.modified`, `decontrol_or_declassify_on`) have range
`string` with a `^\d{4}-\d{2}-\d{2}$` pattern, and `linkml-validate`
rejects an unquoted value with `is not of type 'string'`. The remaining
five (`created_date`, `updated_date`, `embargo_until`,
`data_collection_start`, `data_collection_end`) have range `date`,
so quote them for consistency with the template rather than to satisfy the
validator.
