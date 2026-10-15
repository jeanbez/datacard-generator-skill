# Lookup tables

Human-readable reference for every fixed-vocabulary field in Genesis Datacard v2.
The canonical source for all enum values is `scripts/genesis_datacard.yaml`.
Load the relevant section when prompting for a constrained field.

---

## Datacard meta

### `datacard.creation_method`

How this datacard was most recently created or updated.

| Value | Meaning |
|---|---|
| `Manual` | Filled out entirely by hand by a human author |
| `Automated` | Generated entirely by a pipeline, script, or AI model with no human review |
| `Hybrid` | Initially generated automatically, then reviewed and edited by a human (most common) |

### `datacard.created_by[].creator` — AgentClass type slots

`AgentClass` uses a tagged union: populate exactly one of the four slots below; leave the others null.

| Slot | When to populate |
|---|---|
| `person` | A named human contributor — fill `given_name`, `family_name`, `email`, `orcid`, `affiliation` |
| `organization` | A team or org without a named individual — fill `name` and `ror_id` |
| `ai_model` | An AI/LLM model (e.g., Claude, GPT-4) — `name`, `accessed_date` (`YYYY-MM-DD`), `identifier` and `relationship` are **all required**; `version` only if the model ID carries a minor version (gotchas.md #3) |
| `software` | An automated pipeline or script — `name`, `identifier` and `relationship` are **all required**; `version` optional |

The `role[]` field on each agent uses the CRediT taxonomy (see People & Organizations section).

### `datacard.language`

ISO 639-1 two-letter code for the language of the datacard text. Free-text; no enum constraint.

Common values: `en` (English), `es` (Spanish), `fr` (French), `de` (German), `zh` (Chinese), `ja` (Japanese).

---

## Capability flags (NEW in v2)

Six `Yes | No` flags at the top level of `GenesisDatacardClass` gate which capability containers are required. All use `YesNoEnum`.

| Flag | Gates container | When to set `Yes` |
|---|---|---|
| `supports_discoverability` | `discoverability.*` | **Always Yes** — required by the schema for all datacards |
| `supports_accessibility` | `accessibility.*` | Dataset is shared or accessible to others (even internally) |
| `supports_interoperability` | `interoperability.*` | Dataset is intended to integrate with other datasets or systems |
| `supports_reusability` | `reusability.*` | Dataset may be reused by others; license and stewardship matter |
| `supports_governed_use` | `governed_use.*` | Any sensitivity, export control, PII, or formal governance applies |
| `supports_ai_usability` | `ai_usability.*` | Dataset is intended for AI/ML training, evaluation, or inference |

Setting a flag to `Yes` makes the corresponding container required in the schema.

---

## Sensitivity & security

### `OverallSensitivityEnum`

Applies to both `discoverability.datacard.sensitivity.overall_sensitivity` (the document)
and `discoverability.sensitivity.overall_sensitivity` (the data). These two are set
independently and often differ.

| Value | Meaning |
|---|---|
| `Public` | No restrictions; publicly shareable |
| `Unclassified_Uncontrolled` | Unclassified and not CUI; internal or limited distribution |
| `CUI` | Controlled Unclassified Information |
| `UCNI` | Unclassified Controlled Nuclear Information |
| `Classified` | Formally classified under EO 13526, AEA, or equivalent |
| `Legacy_Controlled` | Controlled under a legacy marking scheme (OUO, SBU, etc.) needing resolution |
| `Mixed` | Multiple sensitivity levels present; describe in narrative |
| `Other_Controlled` | Controlled under a regime not listed above |

### `ClassificationLevelEnum`

Required when `classified_status = Yes`.

| Value | Meaning |
|---|---|
| `Top_Secret` | Top Secret |
| `Secret` | Secret |
| `Confidential` | Confidential |

### `ClassificationCategoryEnum`

Required when `classified_status = Yes`. Multi-valued.

| Value | Meaning |
|---|---|
| `NSI` | National Security Information (EO 13526) |
| `RD` | Restricted Data (Atomic Energy Act) |
| `FRD` | Formerly Restricted Data |
| `TFNI` | Transclassified Foreign Nuclear Information |
| `Other_Classified` | Classified under another authority |

### `SourceMarkingSchemeEnum`

Identifies the authoritative source marking regime.

| Value | Meaning |
|---|---|
| `DOE_CUI` | DOE CUI marking scheme |
| `DOE_UCNI` | DOE UCNI marking scheme |
| `EO13526_Classified` | Classified per Executive Order 13526 |
| `AEA_RD_FRD_TFNI` | Atomic Energy Act — RD, FRD, or TFNI |
| `DOD_CUI` | DoD CUI marking scheme |
| `DHS_CUI` | DHS CUI marking scheme |
| `Legacy_OUO` | Legacy "Official Use Only" (pre-CUI) |
| `Legacy_Site_Specific` | Site-specific legacy marking not mapped to current standard |
| `Other_Agency` | Marking scheme from another agency |
| `None` | No source marking scheme applicable |

### `NormalizedControlBasisEnum`

**Required when `source_marking_scheme = Legacy_OUO`** (alongside
`legacy_label_source`, which is free text and also multivalued); otherwise
optional. Interpreted basis for governance
where source materials use legacy or mixed markings. Does not replace
authoritative source markings. Multi-valued.

| Value | Meaning |
|---|---|
| `Classified` | Basis is classification |
| `CUI` | Basis is CUI |
| `UCNI` | Basis is UCNI |
| `Public_Release_Approved` | Approved for public release |
| `Legacy_Needs_Mapping` | Legacy marking that has not yet been resolved to a current standard |
| `Other_Controlled` | Controlled under another basis |

### CUI markings

Common CUI markings (full registry: https://www.archives.gov/cui).

| Marking | Meaning |
|---|---|
| `CUI` | Generic Controlled Unclassified Information |
| `CUI//SP-PRVCY` | Privacy / PII |
| `CUI//SP-PROPIN` | Proprietary business information |
| `CUI//SP-EXPT` | Export controlled |
| `CUI//SP-LEI` | Law enforcement information |
| `CUI//SP-PRIVL` | Privilege (attorney-client, etc.) |

### Common Yes/No enums

| Enum name | Values | Used for |
|---|---|---|
| `YesNoEnum` | `Yes \| No` | Boolean fields with no uncertainty (e.g., `classified_status`, `cui_status`, `agreement_required`) |
| `YesNoConditionalEnum` | `Yes \| No \| Conditional` | AI usage status (`training_use_status`, `inference_use_status`, `evaluation_use_status` — renamed from `*_use_allowed` in v1.2) |
| `YesNoUnknownEnum` | `Yes \| No \| Unknown` | (no longer used by `ComplianceClass` as of v2.0.0 — see `YesNoUnknownNotApplicableEnum` below) |
| `YesNoUnknownNotApplicableEnum` | `Yes \| No \| Unknown \| not_applicable` | IRB approval; UKMD status; and, as of v2.0.0, `doe_data_management_plan` and `osti_elink2_metadata_compliant` (widened from `YesNoUnknownEnum`, all three now required) |
| `YesNoPendingUnknownEnum` | `Yes \| No \| Pending_Review \| Unknown` | Export control status, privacy/PII/PHI status |
| `UKMDAStatusEnum` | `Yes \| No \| Unknown \| not_applicable` | UK MDA-specific handling |

---

## Governance

Under `governed_use.*` when `supports_governed_use = Yes`.

### `ExportControlClass`

| Field | Enum / Type | Values |
|---|---|---|
| `export_control_status` | `YesNoPendingUnknownEnum` | `Yes \| No \| Pending_Review \| Unknown` |
| `export_control_basis` | `ExportControlBasisEnum` | `ITAR \| EAR \| DOE_Nuclear_Export_Control \| Other \| not_applicable` |
| `foreign_national_access_status` | `ForeignNationalAccessStatusEnum` | `Allowed \| Restricted \| Prohibited \| Conditional \| Unknown` |

### `PrivacyClass`

| Field | Enum / Type | Values |
|---|---|---|
| `privacy_status` | `YesNoPendingUnknownEnum` | `Yes \| No \| Pending_Review \| Unknown` |
| `pii_status` | `YesNoPendingUnknownEnum` | `Yes \| No \| Pending_Review \| Unknown` |
| `phi_status` | `YesNoPendingUnknownEnum` | `Yes \| No \| Pending_Review \| Unknown` |
| `privacy_control_basis[]` | `PrivacyControlBasisEnum` | `HIPAA \| Privacy_Act \| Human_Subjects \| Other_Regulated_Privacy \| Site_Specific \| not_applicable` |

Note: v1.2 spelled this `HIPPA`; upstream fixed the typo in v2.0.0. The field
is **multivalued**, so a converted card can carry a list of bases.

### `RightsReleaseRecordsClass`

| Field | Enum / Type | Values |
|---|---|---|
| `agreement_required` | `YesNoEnum` | `Yes \| No` |
| `agreement_type` | `AgreementTypeEnum` | `DUA \| CRADA \| MOU \| NDA \| LICENSE \| WFO \| OTHER` |
| `ip_restriction_type` | `IPRestrictionTypeEnum` | `Proprietary \| Limited_Rights \| Restricted_Rights \| Government_Purpose_Rights \| Unlimited_Rights \| Third_Party_Licensed \| None` |
| `public_release_status` | `PublicReleaseStatusEnum` | `Approved \| Pending \| Not_Approved \| Requires_STI_Review` |
| `record_status` | `RecordStatusEnum` | `Federal_Record \| Contractor_Record \| Non_Record \| Mixed \| Unknown` |

### `need_to_know_basis` — removed in v2.0.0

The slot **and** `NeedToKnowBasisEnum` are gone. v1.2's values were
`Mission_Need`, `Job_Duty`, `Project_Program_Association`,
`Agreement_Defined` and `DGB_Exception_Waiver`; v2 has no equivalent field.
A converted card reports it as an orphan with its value, so record the
governance rationale elsewhere if it still applies.

### `ComplianceClass`

All three fields are **required** as of v2.0.0 (`doe_data_management_plan` and
`osti_elink2_metadata_compliant` were widened from `YesNoUnknownEnum` to
`YesNoUnknownNotApplicableEnum` and are no longer optional).

| Field | Enum | Values |
|---|---|---|
| `irb_approved` | `YesNoUnknownNotApplicableEnum` | `Yes \| No \| Unknown \| not_applicable` |
| `doe_data_management_plan` | `YesNoUnknownNotApplicableEnum` | `Yes \| No \| Unknown \| not_applicable` |
| `osti_elink2_metadata_compliant` | `YesNoUnknownNotApplicableEnum` | `Yes \| No \| Unknown \| not_applicable` |

For datasets without human subjects, use `not_applicable` for `irb_approved`, not `No`.

### `review_provenance_companion[]` (SpecificReviewClass)

Running history of formal reviews. One entry per review; do not overwrite earlier entries.

Key fields (free-text — no enums on stage/status in v2):

| Field | Type | Notes |
|---|---|---|
| `source_review_reference` | string | Required — identifier or citation for the authoritative review document |
| `comments` | string | Recommended — summary of findings or outcome |
| `review_purpose` | string | e.g., `Export control review prior to public release` |
| `review_date` | ISO 8601 date or `not_applicable` | When the review was conducted |
| `source_review_authority` | string | Office or authority of record (e.g., `DOE Office of Export Control`) |
| `decontrol_or_declassify_on` | ISO 8601 date or `not_applicable` | When decontrol/declassification occurs |
| `reviewed_by` | `AgentClass` | Person or organization that conducted the review |

---

## Identification & identifiers

### `IdentifierTypeEnum`

Used for `identification.primary_id.type`, `identification.additional_ids[].type`,
`related_resources.publications[].type`, and all other identifier blocks.

| Value | Format | Notes |
|---|---|---|
| `doi` | `10.XXXXX/XXXXXXX` | Published datasets with a registered DOI |
| `ark` | `ark:/NAAN/shoulder+name` | Pre-publication datasets at ARK-enabled institutions |
| `handle` | `XXXXX/XXXXXXX` | Handle-based repositories |
| `url` | `https://...` | Stable URL as best available identifier |
| `purl` | `https://purl.org/...` | Persistent URL |
| `urn` | `urn:...` | Uniform Resource Name |
| `uuid` | RFC 4122 UUID | Internally assigned unique identifier |
| `local` | Any internal ID | Pre-publication datasets with only internal identifiers |
| `unregistered` | Any | Dataset exists but has no registered persistent ID (NEW in v2) |
| `other` | Any | Identifier systems not covered above |

### Extended identifier types for `additional_ids`

DOE-lab report-number formats (use `other` with a description if not listed):

| Format | Example | Source |
|---|---|---|
| SAND number | `SAND2024-XXXXX` | Sandia National Laboratories |
| LA-UR number | `LA-UR-XX-XXXXX` | Los Alamos National Laboratory |
| ORNL/TM | `ORNL/TM-YYYY/XXXXX` | Oak Ridge National Laboratory |

### `reusability.citation.preferred_citation`

Only `author`, `title` and `year` are required; `publisher`, `doi` and `url`
are not. `year` is a **string** with pattern `^\d{4}$` — write `year: "2019"`,
since a bare `2019` is a YAML int.

### `related_resources.publications[]`

Each entry requires **`value`, `type` AND `relationship`** — `relationship`
ranges over `RelationshipTypeEnum`, usually `is_described_by` (the paper that
describes this dataset), `cites` or `references`. The step-2b DOI path routes a
README's cited paper here, so this is the common shape, not an edge case.

`type` uses `IdentifierTypeEnum`. Common publication values:

| Value | When to use |
|---|---|
| `doi` | Published paper with a DOI |
| `ark` | ARK-identified publication |
| `url` | Web-accessible publication without a persistent ID |
| `other` | arXiv preprints, internal/institutional reports, etc. |

---

## Object & dataset typing

### `ObjectTypeEnum` (under `tags.object_type`)

| Value | Meaning |
|---|---|
| `Dataset` | Scientific dataset |
| `Model` | Computational or ML model |
| `Software` | Software package or library |
| `AI_Agent` | AI agent (LLM-based or otherwise) |
| `Infrastructure` | Computing infrastructure or environment |
| `Resource` | Other resource type |
| `Other` | Other digital object type |

Note: `Eval` and `Framework` from the v1 spec are not in v2; use `Other` or `Software` as appropriate.

### `ProductTypeEnum` (under `discoverability.product_type`)

Extended from OSTI product types. Select the single best fit. `Dataset` is
right for almost every datacard, but **write it explicitly** — the schema's
`ifabsent: Dataset` is not applied by `linkml-validate`, so an omitted
`product_type` fails as a missing required property. v1.2's `Data` and `Paper_or_Proceedings` **no longer exist** —
`Data` became `Dataset`, and `Paper_or_Proceedings` split into
`Journal_Article` and `Conference`, so a converted card is asked which.

| Value | Note |
|---|---|
| `Accomplishment Report` | |
| `Agent` | |
| `Book` | |
| `Collection` | |
| `Computer_Related` | |
| `Conference` | |
| `Dataset` | Scientific dataset — **the default for a datacard** |
| `Factsheet` | |
| `Journal_Article` | |
| `Miscellaneous` | |
| `Model` | |
| `Other` | |
| `Patent` | |
| `Patent_Application` | |
| `Program_Document` | |
| `Software_Manual` | |
| `Technical_Report` | |
| `Thesis/Dissertation` | |

### Projecting `tags.risk` (spine, `provisional` mode only)

The registry reads `categorization.tags.risk` to filter **access to the
dataset**, and its vocabulary is only `general | reviewed | restricted |
unknown`. Four rules, in order:

1. **Source is the dataset's block** — `discoverability.sensitivity
   .overall_sensitivity`, not `discoverability.datacard.sensitivity`
   (the *card's*). Where the two disagree, the **stricter wins**. A CUI
   dataset behind a deliberately shareable Public card is the normal
   arrangement, and the reason v2 separated the blocks.
2. `Public` and `Unclassified_Uncontrolled` → `general`. Every controlled
   category — `CUI`, `UCNI`, `Classified`, `Legacy_Controlled`,
   `Other_Controlled`, `Mixed` — → `restricted`, and so does any value with
   no mapping. `Mixed` means part of the dataset is controlled.
3. **The status flags override it.** If `classified_status`, `cui_status` or
   `ucni_status` is `Yes` in *either* block, `risk` is `restricted` whatever
   `overall_sensitivity` says. That slot is a display summary — the schema
   says so of it — and every `SensitivityClass` rule has it as a
   *precondition*, so nothing checks it against the flags. A card pairing
   `overall_sensitivity: Public` with `cui_status: Yes` is schema-legal.
4. **Never leave `risk` unset.** The registry reads an absent tag as
   `unknown`, and `Clearance.PUBLIC` covers `{general, unknown}` — so unset
   is exactly as permissive as `general`.

`scripts/convert_v12_to_v20.py`'s `project_spine()` implements all four; read
it rather than re-deriving them.

### `ScienceDomainEnum` (closed vocabulary, multivalued in v2)

`interoperability.domain_metadata` is a `NamedThing`: if you write that block
at all — e.g. to mirror `science_domain` into it — `domain_metadata.name` is
required.

Applies to `discoverability.dataset_description.science_domain` and
`interoperability.domain_metadata.science_domain`. Extends the OSTI Subject
Areas list. **These are quoted
string literals containing spaces (and, in one case, a comma) — not
`Title_Case` or `snake_case` tokens.** Copy the value verbatim, including
punctuation.

| Value | Meaning |
|---|---|
| `"Biology and Medicine"` | Biological and biomedical sciences |
| `"Chemistry"` | Chemical sciences |
| `"Energy Storage, Conversion, and Utilization"` | Batteries, fuel cells, energy conversion/storage systems |
| `"Engineering"` | Engineering disciplines |
| `"Environmental Sciences"` | Environmental and ecological sciences |
| `"Fission and Nuclear Technologies"` | Nuclear fission and related nuclear technologies |
| `"Fossil Fuels"` | Coal, oil, and natural gas |
| `"Geosciences"` | Earth sciences, geology, geophysics |
| `"Materials"` | Materials science |
| `"Mathematics and Computing"` | Mathematics, computer science, computing |
| `"National Defense"` | National defense-related science and technology |
| `"Physics"` | Physical sciences |
| `"Power Generation and Distribution"` | Electric power generation and grid distribution |
| `"Renewable Energy"` | Solar, wind, and other renewable energy sources |
| `"Other"` | Domain not covered by the above |

### `DatasetTypeEnum` — collapsed in v2.0.0

Applies to `discoverability.dataset_type`, now **`if_applicable`**. The only
permissible value is `Instrument`, for datasets that are instrument data
products. Anything else: leave the field null.

v1.2's eleven OSTI codes (`AS`, `FP`, `GD`, `I`, `IG`, `IM`, `IP`, `MD`,
`MM`, `ND`, `SM`) are all gone and **none maps to `Instrument`** — `IP` was
Instrumentation/Protocols, meaning specs rather than an instrument's output.
Conversion reports the old code for a human to place; some of what it carried
now belongs in `product_type` (`Model`, `Collection`, `Computer_Related`).

| Value | Meaning |
|---|---|
| `Instrument` | The dataset is an instrument data product |

---

## Lifecycle & governance

### `StateEnum` (under `discoverability.workflow.state`)

Describes the technical/processing lifecycle position of the data itself.

| Value | Meaning |
|---|---|
| `Raw` | Data as collected; no processing |
| `Processing` | Cleaning, transforming, reducing |
| `QA` | Quality assurance / validation |
| `Analysis` | Active scientific analysis |
| `Review` | Formal review (security, export, IRB) |
| `Embargo` | Complete but intentionally withheld; requires `embargo_until` date |
| `Published` | Publicly released |
| `Archived` | Preserved; no longer actively maintained |
| `not_applicable` | Workflow state does not apply |

### `ReleaseStatusEnum` (under `discoverability.release_status`)

Governance/publication lifecycle status.

| Value | Meaning |
|---|---|
| `Draft` | Work in progress; not ready for sharing |
| `Under_Review` | Submitted for formal review |
| `Approved` | Review complete; cleared for release |
| `Published` | Publicly released and accessible |
| `Deprecated` | Superseded or retired |

### Workflow ↔ release alignment

Mismatches generate a warning (not an error). Typical expected alignments:

| `workflow.state` | Expected `release_status` |
|---|---|
| `Raw`, `Processing`, `QA`, `Analysis` | `Draft` |
| `Review` | `Under_Review` |
| `Embargo`, `Published` | `Approved` or `Published` |
| `Archived` | `Deprecated` or `Published` |

### `AccessLevelEnum` (under `accessibility.access_policy.access_level`)

| Value | Meaning |
|---|---|
| `Open` | No restrictions on access |
| `Restricted` | Limited access; agreement or authentication required |
| `Controlled` | Tightly controlled access; explicit approval required |

### `AuthorizationRequiredEnum` (under `accessibility.access_policy.authorization_required[]`)

Multi-valued (as it was in v1.2). Omit the field or leave it empty if no authorization is needed.

| Value | Meaning |
|---|---|
| `Account` | Registered account required |
| `User_Agreement` | User agreement / terms of service |
| `Data_Use_Agreement` | Formal DUA required |
| `Sponsor_Approval` | Sponsor or PI approval required |
| `Export_Control_Review` | Export control review required |
| `IRB_Approval` | IRB approval required |
| `Other` | Describe in `access_restrictions` |

---

## People & organizations

### Agent type (authors, contributors, `created_by[].creator`)

All of these use `AgentClass` (tagged union — populate exactly one of `person` / `organization` / `ai_model` / `software`). See "`datacard.created_by[].creator` — AgentClass type slots" above for the full slot list and field guidance.

**Exception — `discoverability.contact` is a LIST of `ContactClass`, not an `AgentClass`.** Prefer a `person`; an `organization`-only contact is legal in v2 (two rules enforce "at least one of person/organization", and `person` itself is optional). Write it as a list even for a single contact: `contact:` then `- person:`. Alongside those, optional `valid_until` and `succession_note`. Do not prompt for an agent type when filling contact — go straight to `discoverability.contact[].person.*`.

**Exception — `reusability.stewardship.maintainer` is `MaintainerAgentClass`:**
`person` **or** `organization`, never `ai_model` or `software`, and two rules
make it exactly one of the two — a maintainer carrying both fails validation
with an opaque `anyOf` dump.

**Not agents at all.** `discoverability.facilities[]` (`FacilityClass`),
`interoperability.related_resources.software[]` (`SoftwareClass`) and
`.ai_models[]` (`AIModelClass`) take their fields **directly on the entry** —
`name` plus `role[]` or `relationship`, with no `person:`/`organization:`
sub-block. `AIModelClass` also requires `accessed_date` and `identifier`;
`SoftwareClass` requires `identifier`.

### `RoleEnum` — CRediT **plus DataCite** (authors, contributors, facilities, ai_models, software)

Multi-valued, and it lives **inside** the `person` / `organization` /
`ai_model` / `software` sub-block, never as a sibling of it.

**Never assume a role.** The schema does not require `role[]`, so an empty or
guessed one validates silently. Ask.

v2 keeps CRediT and adds DataCite contributor roles — 36 values. Two v1.2
values were **removed**: `Data_Curation` (use `Data_Curator`) and
`Data_Collection` (use `Investigation`, whose CRediT definition covers
"performing the experiments, or data/evidence collection"). v2 also adds a
real `Creator`, which is usually what an author is.

| Value |
|---|
| `Conceptualization` |
| `Contact_Person` |
| `Contributor` |
| `Creator` |
| `Data_Curator` |
| `Data_Manager` |
| `Distributor` |
| `Editor` |
| `Formal_Analysis` |
| `Funding_Acquisition` |
| `Hosting_Institution` |
| `Investigation` |
| `Methodology` |
| `Other` |
| `Producer` |
| `Project_Administration` |
| `Project_Leader` |
| `Project_Manager` |
| `Project_Member` |
| `Publisher` |
| `Registration_Agency` |
| `Registration_Authority` |
| `Related_Person` |
| `Research_Group` |
| `Researcher` |
| `Resources` |
| `Rights_Holder` |
| `Software` |
| `Sponsor` |
| `Supervision` |
| `Translator` |
| `Validation` |
| `Visualization` |
| `Work_Package_Leader` |
| `Writing_Original_Draft` |
| `Writing_Review_Editing` |

### `FundingSourceEnum` (NEW in v2)

Used in sponsor organization / funding blocks.

| Value | Meaning |
|---|---|
| `DOE_Program_SC` | DOE Office of Science program |
| `DOE_Program_NNSA` | DOE NNSA program |
| `LDRD` | Laboratory Directed Research and Development |
| `WFO` | Work for Others |
| `CRADA` | Cooperative Research and Development Agreement |
| `Other_Federal` | Other federal agency funding |
| `State_Government` | State government funding |
| `Subcontract` | Subcontract from another organization |
| `Industry` | Industry partner funding |
| `Nonprofit` | Nonprofit organization funding |
| `Internal` | Internal lab or project funding |
| `Other` | Other funding source |

### `IntendedPartnerClassEnum` (NEW in v2)

Used in `accessibility.access_policy.intended_partner_classes[]`. Multi-valued.

| Value | Meaning |
|---|---|
| `Internal_Team` | Same project or team |
| `Tri_Lab` | Tri-lab partner (e.g., SNL, LANL, LLNL) |
| `DOE_NNSA_Lab` | Other DOE/NNSA laboratory |
| `Federal_Partner` | Other federal agency partner |
| `Contractor` | Contractor organization |
| `Academic_Researchers` | University or academic institution |
| `External_Research_Partner` | Non-federal external research partner |
| `Industry_Partner` | Industry organization |
| `Public` | General public |
| `Other` | Other partner class |

---

## Stewardship & maintenance

Under `reusability.stewardship` when `supports_reusability = Yes`.

### `StewardshipLevelEnum`

| Value | Meaning |
|---|---|
| `Project_Managed` | Project team is the long-term steward |
| `Repository_Managed` | A repository (e.g., OSTI, Zenodo) is the long-term steward |
| `Externally_Managed` | An external entity manages stewardship |
| `not_applicable` | Stewardship level does not apply |

### `UpdateFrequencyEnum`

| Value | Meaning |
|---|---|
| `None` | Static dataset, no planned updates |
| `Ad_Hoc` | Updates as needed, no schedule |
| `Monthly` | Updated monthly |
| `Quarterly` | Updated quarterly |
| `Annually` | Updated annually |
| `Continuously` | Continuously updated (e.g., streaming or live datasets) |
| `Other` | Other cadence; describe in `versioning_strategy` |

---

## Reviews

Under `governed_use.review_provenance_companion[]` (SpecificReviewClass).

v2 uses free-text fields for review purpose and outcome rather than enums for stage and status. See the Governance section for field details. For historical cross-reference, common values used in v1 were:

**Stage (now free-text `review_purpose`):** internal_qa | security | export_control | irb | partner | publication | other

**Status (now free-text `comments` / narrative):** not_started | submitted | pending | approved | declined

---

## Provenance & relationships

Under `interoperability.*` when `supports_interoperability = Yes`.

### `RelationshipTypeEnum` — common subset (the enum has 53 values)

v2 merged the old base/extended split into one enum. The rows below are the
ones that come up most; see the schema for the full 53.

| Value | Meaning |
|---|---|
| `is_derived_from` | This dataset was derived from the related resource |
| `is_part_of` | This dataset is a component of the related collection |
| `has_part` | The related resource is a component of this dataset |
| `references` | This dataset references the related resource (no derivation) |
| `other` | Other relationship; describe in narrative |

### `ExtendedRelationshipEnum` — deleted in v2.0.0

v2 removed this enum and ranges `ai_model.relationship` and
`software.relationship` over `RelationshipTypeEnum` instead. The mapping,
which preserves the direction ("A generates B", where A is the tool):

| v1.2 | v2.0.0 |
|---|---|
| `used_to_create` | `generates` |
| `used_to_process` | `processes` |
| `used_to_analyze` | `analyzes` |
| `recorded_by` | `collects` |
| `trained_on` | `is_trained_on` |
| `evaluated_on` | `is_evaluated_on` |

`relationship` is **required** on `ai_model` and `software` entries. Unlike
v1.2's enum, `RelationshipTypeEnum` does include `other`.

### AI usage status (`AIUsageClass`) — renamed from `*_use_allowed` in v1.2

All three use `YesNoConditionalEnum` — string values, not booleans (changed from v1).
All three are **required**. When a status is `Conditional`, the matching
`*_use_conditions` free-text field becomes required (schema rule).

| Field | `Yes` | `No` | `Conditional` |
|---|---|---|---|
| `training_use_status` | Suitable for AI/ML training | Must not be used for training | Suitable under conditions in `training_use_conditions` |
| `inference_use_status` | Suitable for inference | Must not be used for inference | Suitable under conditions in `inference_use_conditions` |
| `evaluation_use_status` | Suitable for model evaluation | Must not be used for evaluation | Suitable under conditions in `evaluation_use_conditions` |

| Companion field | Type | Required when |
|---|---|---|
| `training_use_conditions` | free text | `training_use_status = "Conditional"` |
| `inference_use_conditions` | free text | `inference_use_status = "Conditional"` |
| `evaluation_use_conditions` | free text | `evaluation_use_status = "Conditional"` |

`human_review_required` uses `YesNoEnum`: `Yes | No`.

### `integrity.checksum_type`

Free-text field (no enum constraint); use standard values:

| Value | When to use |
|---|---|
| `sha256` | SHA-256 — recommended for new datasets |
| `sha512` | SHA-512 — when stronger collision resistance needed |
| `md5` | MD5 — not recommended for new datasets; legacy only |
| `other` | Custom hash — describe in `fixity_policy` |

### `data_structure.features[].data_type`

Free-text field; standard values:

`float` | `int` | `string` | `boolean` | `datetime` | `other`

### `dataset_scale.record_unit`

Free-text field; standard values:

`samples` | `files` | `records` | `timesteps` | `images` | `tokens` | `other`

---

## Access & APIs

Under `accessibility.*` when `supports_accessibility = Yes`.

### `AuthenticationTypeEnum` (under `accessibility.access.intended_repositories[].data_services[].authentication`)

There is no `api` slot on `IntendedRepositoryClass` — writing one fails with
`Additional properties are not allowed`. Each `intended_repositories[]` entry
requires `name` **and `access_level`** (`Open | Restricted | Controlled`); each
`data_services[]` entry requires a `name`.

| Value | Meaning |
|---|---|
| `None` | No authentication required |
| `API_Key` | API key required |
| `OAuth2` | OAuth 2.0 authentication |
| `SAML` | SAML-based authentication |
| `Certificate` | Client certificate required |
| `OpenID_Connect` | OpenID Connect (OIDC) |
| `Basic_Auth` | HTTP Basic authentication |
| `Bearer_Token` | Bearer token (e.g., JWT) |
| `Other` | Other authentication scheme |

---

## Licenses

Under `reusability.license` when `supports_reusability = Yes`.

### SPDX quick reference

Use the full SPDX registry (https://spdx.org/licenses/) for canonical identifiers. Common choices:

| `spdx_id` | Name |
|---|---|
| `CC0-1.0` | Creative Commons Zero (public domain dedication) |
| `CC-BY-4.0` | Creative Commons Attribution 4.0 |
| `CC-BY-SA-4.0` | CC Attribution-ShareAlike 4.0 |
| `MIT` | MIT License |
| `Apache-2.0` | Apache License 2.0 |
| `BSD-3-Clause` | BSD 3-Clause |
| `Other` | Custom — also fill `license.name` and `license.url`. Capital O: the `name`-required rule keys on that exact string |
| `Pending` | License not yet assigned |
