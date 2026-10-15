# Capability prompt batches

Per-capability field-prompt sequences used by SKILL.md (workflow step 6) when
interactively filling a datacard. Batches are 1–5 fields each and ordered
roughly by how often the answer is already known.

Each top-level key in the YAML below is a `supports_*` capability. The skill
loads ONLY the sections for capabilities the user opted into via the
`supports_*` flags in step 1. `discoverability` is always loaded (it is
schema-forced to Yes).

**Skip any field already filled.** These are the questions available to
ask, not a script to read start to finish — but "available" is not
"optional". **Assume every field here is required unless its own `ask` text
says otherwise** (`if_applicable`, `optional`, or "if/only when X"). A
`supports_X = No` skips that capability's batches entirely; nothing else is
skippable, and no batch is. Markers are deliberately absent: there is no
`[required]` tag to look for, because most fields here are required and a
missing tag used to read as "optional". When step 2b resolved a DOI, the
name, version, summary, keywords, authors, publisher and citation fields
are already populated — confirm them in one table instead of re-asking.

For comprehensive enum values, see `references/lookup-tables.md`.

## Prompts

```yaml
prompts:
  discoverability:
    # always Yes
    - title: "Identification"
      fields:
        - path: discoverability.identification.name
          ask: "Single human-readable name for this dataset (used in filename)."
        - path: discoverability.identification.project
          ask: "Project or sub-project this dataset belongs to (e.g., genesis-fusion)."
        - path: discoverability.identification.version
          ask: "Dataset version (semver), QUOTED — bare 1.0 is a YAML float and fails
            with `is not of type 'string'`. Start at \"1.0.0\" if first release."
        - path: discoverability.identification.primary_id.type
          ask: "Primary identifier type: doi | ark | handle | url | local | unregistered | purl | urn | uuid | other."
        - path: discoverability.identification.primary_id.value
          ask: "Primary identifier value (use ark, local, or unregistered pre-publication)."
        - path: discoverability.datacard.id.type
          ask: "Datacard document identifier type: doi | ark | handle | url | local | unregistered | purl | urn | uuid | other. Use 'local' pre-publication."
        - path: discoverability.datacard.id.value
          ask: "Datacard document identifier value (distinct from the dataset's primary_id above; a slug is fine pre-publication)."
    - title: "Description"
      fields:
        - path: discoverability.dataset_description.dataset_summary
          ask: "1–3 sentences in plain language for a broad scientific audience."
        - path: discoverability.dataset_description.keywords
          ask: "5–10 keywords. Ask comma-separated, but write one `- keyword` per
            line — `keywords` is required and multivalued."
    - title: "Object & dataset typing"
      fields:
        - path: discoverability.dataset_description.tags.object_type
          ask: "Object type: Dataset | Model | Software | AI_Agent | Infrastructure | Resource | Other."
        - path: discoverability.dataset_type
          ask: "Is this an instrument data product? If yes set `Instrument`, the
            only value v2 allows. If not, leave it null — the field is
            if_applicable. Do not ask this unless the dataset really is
            instrument output."
        - path: discoverability.product_type
          ask: "Product type (single best fit — `Dataset` for almost every datacard, but write it explicitly; the schema's ifabsent is not applied): Accomplishment Report
            | Agent | Book | Collection | Computer_Related | Conference | Dataset |
            Factsheet | Journal_Article | Miscellaneous | Model | Other | Patent |
            Patent_Application | Program_Document | Software_Manual |
            Technical_Report | Thesis/Dissertation."
    - title: "Lifecycle"
      fields:
        - path: discoverability.release_status
          ask: "Release status: Draft | Under_Review | Approved | Published | Deprecated."
        - path: discoverability.dataset_publisher.name
          ask: "Publishing organization (+ its ror_id if known). REQUIRED when
            release_status is Approved or Published — two schema rules enforce it,
            and the v1.2 false positive that made this safe to ignore is fixed."
        - path: discoverability.workflow.state
          ask: "Workflow state: Raw | Processing | QA | Analysis | Review | Embargo | Published | Archived | not_applicable."
        - path: discoverability.workflow.embargo_until
          ask: "If state is Embargo: the embargo end date (quoted YYYY-MM-DD).
            Required on Embargo, and must be ABSENT when state is Published."
    - title: "Contact person details"
      fields:
        - path: discoverability.contact[].person.given_name
          ask: "Given (first) name. NOTE `contact` is multivalued — write it as a
            list (`contact:` then `- person:`) even for a single contact, or
            validation fails with `is not of type 'array'`."
        - path: discoverability.contact[].person.family_name
          ask: "Family (last) name."
        - path: discoverability.contact[].person.email
          ask: "Email address for inquiries about this dataset."
        - path: discoverability.contact[].person.orcid
          ask: "ORCID iD for the contact person, if known (optional)."
        - path: discoverability.contact[].person.affiliation.name
          ask: "Affiliation organization name. The affiliation block is optional,
            but `name` is required once you write it."
    - title: "Creator agent details"
      fields:
        - path: discoverability.datacard.created_by[].creator.person.role
          ask: "Role(s) for this creator, if a person or organization (multi-valued).
            v2's RoleEnum is CRediT plus DataCite — 36 values; see
            lookup-tables.md. Never assume one: the schema does not require
            `role[]`, so a guess passes silently. Enter inside the
            person/organization sub-block, not at the creator entry level."
        - path: discoverability.datacard.created_by[].creator.ai_model.relationship
          ask: "If this creator is an ai_model: its relationship to the datacard
            creation process — generates (drafted it) | processes | analyzes |
            collects | is_trained_on | is_evaluated_on. Required on ai_model
            entries. v2 folded the old used_to_* vocabulary into
            RelationshipTypeEnum; see references/v12-to-v20-map.md."
        - path: discoverability.datacard.created_by[].creator.software.relationship
          ask: "If this creator is software: its relationship to the datacard
            creation process — generates | processes | analyzes | collects |
            is_trained_on | is_evaluated_on. Required on software entries."
    - title: "Categorization"
      fields:
        - path: discoverability.dataset_description.tags.project
          ask: "Project this dataset belongs to. Required once a `tags` block exists,
            and distinct from `identification.project`. This is also what the
            registry spine reads as `categorization.tags.project`."
        - path: discoverability.dataset_description.task_category
          ask: "ML task categories this dataset suits — a list, e.g.
            `- classification`, `- regression`, `- clustering`. ASK FOR THIS:
            the spine projects it to the registry's `task_tags`, and without
            them the Workflow Composer cannot use the dataset as a pipeline
            step. Omit only if no ML task applies."
        - path: discoverability.dataset_description.task_subcategory
          ask: "Narrower task descriptions — a list of free text, e.g.
            `- particle track reconstruction`. Also projected to task_tags."
        - path: discoverability.dataset_description.science_domain
          ask: "Scientific domain(s) — **a list**, multivalued in v2, even for one
            entry: `science_domain: [\"Physics\"]`. Values come from the closed
            ScienceDomainEnum list (quoted strings with spaces, not snake_case): \"Biology and Medicine\" | \"Chemistry\" | \"Energy Storage, Conversion, and Utilization\" | \"Engineering\" | \"Environmental Sciences\" | \"Fission and Nuclear Technologies\" | \"Fossil Fuels\" | \"Geosciences\" | \"Materials\" | \"Mathematics and Computing\" | \"National Defense\" | \"Physics\" | \"Power Generation and Distribution\" | \"Renewable Energy\" | \"Other\". See lookup-tables.md for descriptions."
    - title: "Sensitivity (dataset)"
      fields:
        - path: discoverability.sensitivity.overall_sensitivity
          ask: "Overall dataset sensitivity: Public | Unclassified_Uncontrolled |
            CUI | UCNI | Classified | Legacy_Controlled | Mixed | Other_Controlled."
        - path: discoverability.sensitivity.source_marking_string
          ask: "Source marking text, verbatim from the document if it carries one.
            Required. For an unmarked public dataset use \"not_applicable\"."
        - path: discoverability.sensitivity.source_marking_scheme
          ask: "Marking scheme. Required. For an unmarked public dataset use \"None\".
            Otherwise: AEA_RD_FRD_TFNI | DHS_CUI | DOD_CUI | DOE_CUI | DOE_UCNI |
            EO13526_Classified | Legacy_OUO | Legacy_Site_Specific | Other_Agency.
            If Legacy_OUO: `legacy_label_source` and `normalized_control_basis`
            are both required by rule — ask for them too, and both are LISTS.
            `normalized_control_basis` is a closed enum (see lookup-tables.md);
            `legacy_label_source` is free text."
        - path: discoverability.sensitivity.classified_status
          ask: "Classified? Yes | No (YesNoEnum — there is no Pending_Review or Unknown). Required. Must be
            \"Yes\" if overall_sensitivity is Classified, and \"No\" if it is CUI.
            If \"Yes\", `classification_level` (Top_Secret | Secret | Confidential)
            and `classification_category` (a LIST: NSI | RD | FRD | TFNI |
            Other_Classified) are both required by rule — ask for them too."
        - path: discoverability.sensitivity.cui_status
          ask: "CUI? Yes | No (YesNoEnum — there is no Pending_Review or Unknown). Required. Must be \"Yes\"
            if overall_sensitivity is CUI."
        - path: discoverability.sensitivity.ucni_status
          ask: "UCNI? Yes | No (YesNoEnum — there is no Pending_Review or Unknown). Required. Must be \"Yes\"
            if overall_sensitivity is UCNI. If \"Yes\", also fill
            `cui_specified_categories` (a LIST, e.g. [\"UCNI\"]) — a schema rule
            requires at least one, so UCNI is not represented by generic CUI
            fields alone. `cui_basic_categories` is a list too."
    - title: "Sensitivity (datacard document)"
      fields:
        - path: discoverability.datacard.sensitivity.overall_sensitivity
          ask: "Overall datacard document (independent of the dataset's) sensitivity: Public | Unclassified_Uncontrolled |
            CUI | UCNI | Classified | Legacy_Controlled | Mixed | Other_Controlled."
        - path: discoverability.datacard.sensitivity.source_marking_string
          ask: "Source marking text, verbatim from the document if it carries one.
            Required. For an unmarked public dataset use \"not_applicable\"."
        - path: discoverability.datacard.sensitivity.source_marking_scheme
          ask: "Marking scheme. Required. For an unmarked public dataset use \"None\".
            Otherwise: AEA_RD_FRD_TFNI | DHS_CUI | DOD_CUI | DOE_CUI | DOE_UCNI |
            EO13526_Classified | Legacy_OUO | Legacy_Site_Specific | Other_Agency.
            If Legacy_OUO: `legacy_label_source` and `normalized_control_basis`
            are both required by rule — ask for them too, and both are LISTS.
            `normalized_control_basis` is a closed enum (see lookup-tables.md);
            `legacy_label_source` is free text."
        - path: discoverability.datacard.sensitivity.classified_status
          ask: "Classified? Yes | No (YesNoEnum — there is no Pending_Review or Unknown). Required. Must be
            \"Yes\" if overall_sensitivity is Classified, and \"No\" if it is CUI.
            If \"Yes\", `classification_level` (Top_Secret | Secret | Confidential)
            and `classification_category` (a LIST: NSI | RD | FRD | TFNI |
            Other_Classified) are both required by rule — ask for them too."
        - path: discoverability.datacard.sensitivity.cui_status
          ask: "CUI? Yes | No (YesNoEnum — there is no Pending_Review or Unknown). Required. Must be \"Yes\"
            if overall_sensitivity is CUI."
        - path: discoverability.datacard.sensitivity.ucni_status
          ask: "UCNI? Yes | No (YesNoEnum — there is no Pending_Review or Unknown). Required. Must be \"Yes\"
            if overall_sensitivity is UCNI. If \"Yes\", also fill
            `cui_specified_categories` (a LIST, e.g. [\"UCNI\"]) — a schema rule
            requires at least one, so UCNI is not represented by generic CUI
            fields alone. `cui_basic_categories` is a list too."
    - title: "Authorship"
      fields:
        - path: discoverability.authors
          ask: "Primary authors and their role(s) (multi-valued). v2's RoleEnum is
            CRediT plus DataCite — 36 values, including a real `Creator`; see
            lookup-tables.md. Ask rather than assume. `role[]` goes inside each
            author's `person` or `organization` sub-block (e.g.
            `authors[].person.role`), not on the author entry itself."
    - title: "Organizational context"
      fields:
        - path: discoverability.sponsor_organizations
          ask: "Funding/sponsor organizations (name + ROR if known)."
        - path: discoverability.research_organizations
          ask: "Creating/collecting organizations (name + ROR if known)."

  accessibility:
    - title: "Access policy"
      fields:
        - path: accessibility.access_policy.access_level
          ask: "Dataset access level: Open | Restricted | Controlled."
        - path: accessibility.access_policy.authorization_required
          ask: "Authorization required (multi-valued): Account | User_Agreement |
            Data_Use_Agreement | Sponsor_Approval | Export_Control_Review |
            IRB_Approval | Other. Omit entirely if none is needed — but it is
            REQUIRED when access_level is Restricted or Controlled."
        - path: accessibility.access_policy.access_restrictions
          ask: "If authorization_required includes Other: describe the restriction.
            A schema rule requires this field on that exact value."
    - title: "Dataset scale"
      fields:
        - path: accessibility.dataset_scale.record_count
          ask: "Number of records (or files, or samples — depends on record_unit)."
        - path: accessibility.dataset_scale.record_unit
          ask: "Unit for record_count: samples | files | records | timesteps | images | tokens | other."
        - path: accessibility.dataset_scale.compressed_bytes
          ask: "Total compressed size in bytes (from `du` or stat sum)."
    - title: "Access location"
      fields:
        - path: accessibility.access.current_location
          ask: "Where the data physically resides right now (path or URL)."
        - path: accessibility.access.publicly_facing_landing_page_url
          ask: "Publicly facing landing page URL (if already published or deposited).
            Omit the field entirely if there is none: the pattern is
            `^https?://.+$` and `not_applicable` is NOT accepted here, unlike
            `access_policy.policy_url`."
        - path: accessibility.access.intended_repositories
          ask: "If the dataset is deposited in, or destined for, a repository:
            one entry per repository, each requiring `name` AND `access_level`
            (Open | Restricted | Controlled). Optional overall; `is_primary`,
            `date_deposited` and `data_services[]` (each needing a `name`) may
            also be filled. See lookup-tables.md."

  interoperability:
    - title: "Data structure"
      fields:
        - path: interoperability.data_structure.formats
          ask: "File formats present (e.g., CSV, HDF5, Parquet)."
        - path: interoperability.data_structure.modalities
          ask: "Data modalities — **a list**, multivalued (e.g. `- tabular`, `- image`,
            `- time-series`, `- text`)."
    - title: "Features"
      fields:
        - path: interoperability.data_structure.features
          ask: "Variable list as structured objects: name, data_type, unit, description, range."
    - title: "Dates"
      fields:
        - path: interoperability.dates.data_collection_start
          ask: "ISO 8601 date data collection began."
        - path: interoperability.dates.data_collection_end
          ask: "ISO 8601 date data collection ended."
    - title: "Provenance"
      fields:
        - path: interoperability.provenance.was_generated_by
          ask: "How was this dataset generated? (instrument, simulation, derivation)."
        - path: interoperability.provenance.source_data
          ask: "If this dataset is derived from others, list each source:
            `name` and `identifier` are both required per entry, plus
            `relationship: is_derived_from`. Multivalued. Leave empty for a
            dataset collected or simulated from scratch — free prose in
            was_generated_by is not a substitute for this structured field."
        - path: interoperability.provenance.processing_steps
          ask: "Key processing, cleaning, calibration, or transformation steps applied."
    - title: "Semantic layer"
      fields:
        - path: interoperability.semantic_layer.schema_url
          ask: "URL to formal schema for this dataset (if any)."
        - path: interoperability.semantic_layer.semantic_context
          ask: "Semantic conventions applied (e.g., NetCDF CF, NeXus) — **a list**,
            multivalued, one entry per line even for a single convention."

  reusability:
    - title: "License"
      fields:
        - path: reusability.license.spdx_id
          ask: "SPDX license identifier (e.g., CC-BY-4.0, MIT, Apache-2.0). Use
            `Other` (capital O — the rule that requires `name` keys on that
            exact value) if not in SPDX, or `Pending` if a license has not been
            assigned yet. If there is genuinely no license and none is planned,
            omit the whole `reusability.license` block: that validates clean
            even with supports_reusability=Yes, and is honest. Never invent one."
        - path: reusability.license.name
          ask: "Human-readable license name (e.g. 'Creative Commons Attribution 4.0
            International'). ALWAYS fill it when a license block exists. The
            schema tries to relax it (`LicenseClass.slot_usage.name.required:
            false`) but `gen-json-schema` does not honour that, so the validator
            step 9 runs reports `'name' is a required property in
            /reusability/license`. A separate rule also requires it when
            `spdx_id` is `Other` (capital O)."
    - title: "Citation"
      fields:
        - path: reusability.citation.preferred_citation
          ask: "Recommended citation as **structured fields, not a BibTeX string**:
            `author`, `title` and quoted `year` are the only required ones;
            `publisher`, `doi` and `url` are optional extras. Optional
            overall — the only Approved/Published requirements in the schema are
            dataset_publisher and authors. (The card's narrative body may render it
            as BibTeX; see references/body-fill-guide.md.)"
    - title: "Integrity"
      fields:
        - path: reusability.integrity.checksum_available
          ask: "Are checksums available? Yes | No."
        - path: reusability.integrity.checksum_type
          ask: "Checksum algorithm: sha256 | sha512 | md5 | other (sha256 recommended).
            Required when checksum_available is Yes."
        - path: reusability.integrity.checksum_value
          ask: "The checksum itself, or the path to a manifest of them. Required
            when checksum_available is Yes — see references/introspection-commands.md
            for how to compute it."
    - title: "Stewardship"
      fields:
        - path: reusability.stewardship.level
          ask: "Stewardship: Project_Managed | Repository_Managed | Externally_Managed | not_applicable."
        - path: reusability.stewardship.update_frequency
          ask: "Update frequency: None | Ad_Hoc | Monthly | Quarterly | Annually | Continuously | Other."
    - title: "Data quality"
      fields:
        - path: reusability.data_quality.completeness
          ask: "Be specific: 'All channels present; 2% timesteps missing due to instrument downtime on 2023-04-12'."
        - path: reusability.data_quality.known_issues
          ask: "Known issues, sensor drift, anomalies."
        - path: reusability.data_quality.validation_methods
          ask: "How was data quality validated? e.g., 'Cross-validated against NIST SRM 640f'."

  governed_use:
    - title: "Use governance"
      fields:
        - path: governed_use.use_governance.intended_use
          ask: "What is this dataset intended for?"
        - path: governed_use.use_governance.out_of_scope_use
          ask: "Uses this dataset should NOT be applied to."
        - path: governed_use.use_governance.current_use
          ask: "What is this dataset actively being used for right now? Distinct from
            intended_use."
        - path: governed_use.use_governance.permitted_use
          ask: "Uses this dataset is suitable for beyond the intended use. If a
            need-to-know or agreement basis governs access, record it here —
            `need_to_know_basis` and its enum were removed in v2."
    - title: "Export control"
      fields:
        - path: governed_use.non_sensitivity_governance_metadata.export_control.export_control_status
          ask: "Export control status: Yes | No | Pending_Review | Unknown."
        - path: governed_use.non_sensitivity_governance_metadata.export_control.export_control_basis
          ask: "Export control basis: ITAR | EAR | DOE_Nuclear_Export_Control | Other | not_applicable."
        - path: governed_use.non_sensitivity_governance_metadata.export_control.foreign_national_access_status
          ask: "Foreign national access: Allowed | Restricted | Prohibited | Conditional | Unknown."
    - title: "Privacy / PII / PHI"
      fields:
        - path: governed_use.non_sensitivity_governance_metadata.privacy.privacy_status
          ask: "Privacy status: Yes | No | Pending_Review | Unknown."
        - path: governed_use.non_sensitivity_governance_metadata.privacy.pii_status
          ask: "Is PII present? Yes | No | Pending_Review | Unknown."
        - path: governed_use.non_sensitivity_governance_metadata.privacy.phi_status
          ask: "Is PHI (HIPAA-covered health info) present? Yes | No | Pending_Review | Unknown."
    - title: "Rights & release"
      fields:
        - path: governed_use.non_sensitivity_governance_metadata.rights_release_records.ip_restriction_type
          ask: "IP restriction: Proprietary | Limited_Rights | Restricted_Rights | Government_Purpose_Rights | Unlimited_Rights | Third_Party_Licensed | None."
        - path: governed_use.non_sensitivity_governance_metadata.rights_release_records.agreement_required
          ask: "Is a data-use agreement required? Yes | No."
        - path: governed_use.non_sensitivity_governance_metadata.rights_release_records.agreement_type
          ask: "If agreement_required is Yes: which agreement(s) (multi-valued,
            at least one — a schema rule requires it on Yes). See
            lookup-tables.md for AgreementTypeEnum's values."
        - path: governed_use.non_sensitivity_governance_metadata.rights_release_records.public_release_status
          ask: "Public release status: Approved | Pending | Not_Approved | Requires_STI_Review."
        - path: governed_use.non_sensitivity_governance_metadata.rights_release_records.record_status
          ask: "Record status: Federal_Record | Contractor_Record | Non_Record | Mixed | Unknown."
    - title: "Compliance"
      fields:
        - path: governed_use.compliance.doe_data_management_plan
          ask: "Is a DOE Data Management Plan on file? Yes | No | Unknown | not_applicable."
        - path: governed_use.compliance.osti_elink2_metadata_compliant
          ask: "Is the metadata compliant with OSTI E-Link 2 API? Yes | No | Unknown | not_applicable."
        - path: governed_use.compliance.irb_approved
          ask: "IRB approval status: Yes | No | Unknown | not_applicable (use not_applicable for non-human-subject data)."

  ai_usability:
    - title: "AI/ML usage policy"
      fields:
        - path: ai_usability.ai_usage.training_use_status
          ask: "Training use status? Yes | No | Conditional. (renamed from training_use_allowed in v1.2) If Conditional, also fill training_use_conditions."
        - path: ai_usability.ai_usage.training_use_conditions
          ask: "Conditions under which training use is allowed (required only if training_use_status = Conditional)."
        - path: ai_usability.ai_usage.inference_use_status
          ask: "Inference use status? Yes | No | Conditional. (renamed from inference_use_allowed in v1.2) If Conditional, also fill inference_use_conditions."
        - path: ai_usability.ai_usage.inference_use_conditions
          ask: "Conditions under which inference use is allowed (required only if inference_use_status = Conditional)."
        - path: ai_usability.ai_usage.evaluation_use_status
          ask: "Evaluation use status? Yes | No | Conditional. (renamed from evaluation_use_allowed in v1.2) If Conditional, also fill evaluation_use_conditions."
        - path: ai_usability.ai_usage.evaluation_use_conditions
          ask: "Conditions under which evaluation use is allowed (required only if evaluation_use_status = Conditional)."
        - path: ai_usability.ai_usage.human_review_required
          ask: "Does AI use require human review? Yes | No."
    - title: "AI/ML risks"
      fields:
        - path: ai_usability.ai_usage.bias_risks
          ask: "Known bias risks (e.g., 'overrepresents samples from facility X'). Enter 'None' if none."
        - path: ai_usability.ai_usage.safety_considerations
          ask: "Safety considerations (e.g., 'outputs may be export-controlled'). Enter 'None' if none."
        - path: ai_usability.ai_usage.restrictions
          ask: "Any conditional-use restrictions. Enter 'None' if none."
```
