---
# ============================================================================
# GENESIS MISSION DATA CARD v2.0.0
# ============================================================================
#
# This data card describes datasets ingested or created within the Genesis
# Mission. It is designed for human and machine authorship and ingestion
# across all sensitivity levels and publication states — from raw in-workflow
# data through published and archived datasets.
#
# XCard Template:
#   This data card template is designed to be used within the Genesis Mission
#   xCard framework. xCards are structured metadata and narrative assets that
#   describe  research objects, including datasets, models and AI agents. The
#   top-level xCard block defines the xCard type. For datasets, the xCard type
#   is "dataset".
#
# INTENDED CAPABILITIES:
#   The top-level data card capabilities to declare the intended use and guide
#   authors on which fields to fill in, and determine  the required fields.
#   * supports_discoverability: "Yes" - required for all data cards. Indicates
#   whether the dataset described in the data card is intended to be
#   discoverable in catalogs and repositories, to support basic findability.
#   This is a high-level indication of whether the dataset is intended to be
#   discoverable, and does not necessarily indicate that the dataset is
#   currently discoverable or that it meets all criteria for discoverability.
#   `discoverability_required` fields are required  for all data cards.
#   * supports_accessibility: "Yes"|"No" - "Yes" is optional, but recommended,
#   for all data cards. Indicates whether the dataset described in the data
#   card is intended to be shared or accessed by others, whether internally
#   within a project or organization, with external collaborators, or
#   publicly. This is a high-level indication of whether the dataset is
#   intended to be accessible, and does not necessarily indicate that the
#   dataset is currently accessible or that it meets all criteria for
#   accessibility. `accessibility_required`  fields are required for all data
#   cards with supports_accessibility = "Yes".
#   * supports_interoperability: "Yes"|"No" - "Yes" is optional, but
#   recommended, for all data cards. Indicates whether the dataset described
#   in the data card is intended to be interoperable, meaning it is intended
#   to be integrated with other datasets or systems, or used in combination
#   with other datasets. This is a high-level indication of whether the
#   dataset is intended to be interoperable, and does not necessarily indicate
#   that the dataset is currently interoperable or that it meets all criteria
#   for interoperability. `interoperability_required` fields are required for
#   all data cards  with supports_interoperability = "Yes".
#   * supports_reusability: "Yes"|"No" - "Yes" is optional, but recommended,
#   for all data cards. Indicates whether the dataset described in the data
#   card is intended to be reusable, meaning it is intended to be reused by
#   others for the same or different purposes. This is a high-level indication
#   of whether the dataset is intended to be reusable, and does not
#   necessarily indicate that the dataset is currently reusable or that it
#   meets all criteria for reusability. `reusability_required` fields are
#   required for all  data cards with supports_reusability = "Yes".
#   * supports_governed_use: "Yes"|"No" - "Yes" is optional, but strongly
#   recommended, for all data cards. Indicates whether the dataset described
#   in the data card is intended to be shared or accessed under specific
#   governance or oversight, such as datasets that are subject to security
#   controls, export control, or other types of formal review and approval
#   processes. This is a high-level indication of whether the dataset is
#   intended to be shared or accessed under specific governance or oversight.
#   The governance fields includes sensitivity and control metadata that  are
#   not just descriptive; they help determine what can be shown,  to whom, at
#   what level of detail, whether an asset is broadly discoverable  or only
#   partially visible, and whether access should be allowed,  restricted, or
#   routed for additional review.  The "Yes" response does not necessarily
#   indicate that the dataset is currently shared or accessed under specific
#   governance or oversight, or that it meets all criteria for governed use.
#   `governed_use_required` fields are required for all data cards with
#   supports_governed_use = "Yes".
#   * supports_ai_usability: "Yes"|"No" - "Yes" is optional, but strongly
#   recommended, for all data cards. Indicates whether the dataset described
#   in the data card is intended to be used for AI training, evaluation, or
#   other AI-related purposes. This is a high-level indication of whether the
#   dataset is intended to be used for AI purposes, and does not necessarily
#   indicate that the dataset is currently used for AI purposes or that it
#   meets all criteria for AI usability. `ai_usability_required` fields are
#   required for all data cards with  supports_ai_usability = "Yes".
#
# FIELD ANNOTATIONS:
#   [required] — Required for all datacards, regardless of intended use or
#   sharing level and use.
#   [situational_required] — Required based on the values for other fields,
#   but may not be required in all cases.
#   [if_applicable] — Optional. These fields may not be applicable to all
#   datasets,  but should be included when relevant and available to provide
#   important context for users, both humans and machines.
#   [recommended] — Strongly recommended, but not required. These fields may
#   provide additional context or information about the dataset,  but are not
#   strictly necessary for understanding or using the dataset.
#   [discoverability_required] — required for supports_discoverability = "Yes"
#   data cards.
#   [discoverability_if_applicable] — Optional for supports_discoverability =
#   "Yes" data cards; populate if applicable to support discoverability, but
#   may be removed/left blank if not yet known or not applicable.
#   [accessibility_required] — Required for supports_accessibility = "Yes"
#   data cards.
#   [accessibility_if_applicable] — Optional for supports_accessibility =
#   "Yes" data cards; populate if applicable to support accessibility, but may
#   be removed/left blank if not yet known or not applicable.
#   [interoperability_required] — Required for supports_interoperability =
#   "Yes" data cards.
#   [interoperability_if_applicable] — Optional for supports_interoperability
#   = "Yes" data cards; populate if applicable to support interoperability,
#   but may be removed/left blank if not yet known or not applicable.
#   [reusability_required] — Required for supports_reusability = "Yes" data
#   cards.
#   [reusability_if_applicable] — Optional for supports_reusability = "Yes"
#   data cards; populate if applicable to support reusability, but may be
#   removed/left blank if not yet known or not applicable.
#   [governed_use_required] — Required for supports_governed_use = "Yes" data
#   cards.
#   [governed_use_if_applicable] — Optional for supports_governed_use = "Yes"
#   data cards; strongly recommended to populate if applicable to support
#   governed use, but may be removed/left blank if not yet known or not
#   applicable.
#   [ai_usability_required] — Required for supports_ai_usability = "Yes" data
#   cards.
#   [ai_usability_if_applicable] — Optional for supports_ai_usability = "Yes"
#   data cards; strongly recommended to populate if applicable to support AI
#   usability, but may be removed/left blank if not yet known or not
#   applicable.
#
# PLACEHOLDER CONVENTIONS:
#   ${VALUE} — fill in your value;
#   __VALUE__ — fill in if applicable; delete; leave blank; or replace with
#   'not_applicable' if this field definitively does not apply.
#   not_applicable — use when a field definitively does not apply (distinct
#   from blank, which means "not yet known")
#
# NOTE ON null vs. not_applicable:
#   Blank / __VALUE__ = information not yet known or not yet captured.
#   not_applicable = this field definitively does not apply to this dataset.
#   This distinction enables automated completeness scoring and catalog
#   quality metrics.
#
# NOTE ON SENSITIVITY:
#   This template has two independent sensitivity sections:
#   discoverability.datacard.sensitivity — sensitivity of THIS DATA CARD
#   DOCUMENT; discoverability.sensitivity — sensitivity of THE DATASET ITSELF.
#   These are intentionally independent and will often differ. Example: an
#   open data card (discoverability.datacard.sensitivity.overall_sensitivity =
#   Public) may describe a classified dataset
#   (discoverability.sensitivity.overall_sensitivity = Classified). Do not
#   assume they should match. Set each based on its own subject.
#
# NOTE ON LICENSES AND GOVERNANCE:
#   A public/open license is not always the governing instrument for use, some
#   controlled datasets may not have an SPDX-style reuse license at all, and
#   use may instead be governed by contract, agreement, institutional review,
#   or repository policy.
#
# NOTE ON WORKFLOW STATE vs. RELEASE STATUS:
#   discoverability.workflow.state describes the technical/processing
#   lifecycle position of the data itself (Raw → Archived);
#   discoverability.release_status describes the publication and governance
#   state of the dataset record (Draft → Deprecated). These should be
#   logically consistent. Common alignments:
#   - workflow.state=Raw|Processing|QA|Analysis → release_status=Draft
#   - workflow.state=Review → release_status=Under_Review
#   - workflow.state=Embargo|Published → release_status=Approved|Published
#   - workflow.state=Archived → release_status=Deprecated|Published
#
# SCHEMA VALIDATION:
#   A companion JSON Schema for machine validation is available at:
#   https://gitlab.com/amsc2/modcon/dbs/data-cards/ (refer to the README.md
#   for usage instructions). Validate your data card before submission using
#   the Genesis LinkML data card validator (refer to README.md for
#   instructions) or any JSON Schema-compatible YAML validator.
#
# FUTURE EXTENSIONS:
#   This template will evolve. Fields under consideration for future versions
#   include ontology alignment, interoperability standards (DCAT, schema.org),
#   audience classification, consent typing and catalog-managed collection
#   membership. See https://gitlab.com/amsc2/modcon/dbs/data-
#   cards/-/milestones for the roadmap.
#
# ============================================================================

# Auto-generated fillable template for GenesisDatacardClass
# Generated by gen_annotated_template.py from datacard_schema/src/genesis_datacard/schema/genesis_datacard.yaml
# Placeholder convention: ${VALUE} = required, __VALUE__ = optional/if-applicable

xCard:  # Metadata that describes the xCard
  card_type: dataset  # [required]
supports_discoverability: ${"Yes|No"}  # [required] "Yes" is required for all datacards to indicate whether the dataset  described in the datacard is intended to be discoverable in catalogs and repositories. Does not necessarily indicate that the dataset is currently discoverable or that it meets all criteria for discoverability.
supports_accessibility: ${"Yes|No"}  # [required] "Yes" | "No" - Indicates whether the dataset described in the datacard is intended to be shared or accessed by others,  whether internally within a project or organization, with external collaborators, or publicly. Does not necessarily indicate that the dataset is currently accessible or that it meets all criteria for accessibility.
supports_interoperability: ${"Yes|No"}  # [required] "Yes" | "No" - Indicates whether the dataset described in the datacard is intended to be interoperable,  meaning it is intended to be integrated with other datasets or systems, or used in combination with other datasets. Does not necessarily indicate that the dataset is currently interoperable or that it meets all criteria for interoperability.
supports_reusability: ${"Yes|No"}  # [required] "Yes" | "No" - Indicates whether the dataset described in the datacard is intended to be reusable,  meaning it is intended to be reused by others for the same or different purposes. Does not necessarily indicate that the dataset is currently reusable or that it meets all criteria for reusability.
supports_governed_use: ${"Yes|No"}  # [required] "Yes" | "No" - Indicates whether the dataset described in the datacard is intended to be shared or accessed  under specific governance or oversight, such as datasets that are subject to security controls, export control, IRB oversight, or other types of formal review and approval processes. Does not necessarily indicate that the dataset is currently shared or accessed under specific governance or oversight, or that it meets all criteria for governed use.
supports_ai_usability: ${"Yes|No"}  # [required] "Yes" | "No" - Indicates whether the dataset described in the datacard is intended to be used for AI training, evaluation, or other AI-related purposes. Does not necessarily indicate that the dataset is currently used for AI purposes or that it meets all criteria for AI usability.
discoverability:  # [discoverability_required] ###---Discoverability---### Metadata fields that support the discoverability of the dataset, a key aspect of the FAIR principles and essential for enabling users to find the dataset in catalogs and repositories. These fields provide critical information that can enhance the data's discoverability and help users understand its relevance and suitability for their needs. The discoverability capability is required for all datacards to support basic findability in catalogs and repositories.
  datacard:  # [discoverability_required] Metadata about the datacard itself (not the dataset),  including its sensitivity, creation method, and change log.
    template_version: "2.0.0"  # [discoverability_required] Current version is 2.0.0; the version of the datacard template used to create this datacard.
    datacard_version: "1.0.0"  # [discoverability_required] Replace default value with the version of the datacard itself,  which should be incremented when the datacard is meaningfully updated. Use semantic versioning: MAJOR.MINOR.PATCH e.g., 1.0 → 1.1 for content updates; 1.x -> 2.0 for structural changes
    filename: "genesis_datacard_${SNAKE_CASE_DATASET_NAME}.md"  # [discoverability_required] The filename of the data card document, follow naming convention: "genesis_datacard_${SNAKE_CASE_DATASET_NAME}$.md" where ${SNAKE_CASE_DATASET_NAME} is the dataset name in snake_case format. Use "genesis_datacard_other_${SNAKE_CASE_DATASET_NAME}$.md" for datasets that are not part of a Genesis project or sub-project.
    language: "en"  # [discoverability_required] Replace default value, 'en', with the language of the datacard content,  following ISO 639-1 codes. e.g., en | es | fr | de | zh | ru | ar | pt | ja | ko
    id:  # [discoverability_if_applicable] A unique identifier for the datacard document itself, distinct from the dataset identifier. Assign if the datacard is registered in a catalog or repository independently of the dataset. If one of type or value is provided, the other must also be provided.
      type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
      value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
    sensitivity:  # [discoverability_required] Sensitivity of the DATA CARD itself, which may differ from the sensitivity of the dataset  it describes. Populate based on the sensitivity of the data card content alone,  not the dataset. See NOTE ON SENSITIVITY above. NOTE: Sensitivity terminology is still under Genesis governance review. Vocabulary may evolve.
      overall_sensitivity: ${OVERALL_SENSITIVITY}  # [discoverability_required] Human-readable top-level sensitivity posture of the data card (for `discoverability.datacard.sensitivity`), or the dataset (for `discoverability.sensitivity`) - do not automatically set the overall sensitivity of the  data card and dataset sensitivity to the same value, as they may differ. The field value is based on the authoritative source markings and metadata fields. This is a summary field only and does not replace the authoritative fields such as the classification_status, classification_level, export_control_basis, or privacy_control_basis fields. Authoritative source markings and metadata fields should be used for access control and governance decisions. Use "Public" for unclassified, non-sensitive assets that can be shared publicly. Allowed values: Public | Unclassified_Uncontrolled | CUI | UCNI | Classified | Legacy_Controlled | Mixed | Other_Controlled
      source_marking_string: ${SOURCE_MARKING_STRING}  # [discoverability_required] Exact marking/banner/control text as it appears on the source artifact or in the authoritative review/release output, if applicable. The artifact is either the data card (for `discoverability.datacard.sensitivity`), or the dataset (for `discoverability.sensitivity`). Provides the authoritative source marking information for the asset,  which is critical for ensuring proper handling and access controls based on the sensitivity of the asset. If no source markings apply to the asset, this field should be filled with "not_applicable". If the asset has multiple source markings, list them separated by // with no spaces. This field does not replace the individual metadata fields for classification status,  classification level, export control basis, or privacy control basis,  which should still be filled out based on the authoritative source markings. e.g., not_applicable | CUI//SP-EXPT//NOFORN | SECRET//RD//SIGMA 15 | OFFICIAL USE ONLY
      source_marking_scheme: ${SOURCE_MARKING_SCHEME}  # [discoverability_required] Identifies the authoritative source marking regime, for the source_marking_string field. Use "None" for unclassified, non-sensitive assets that can be shared publicly. If a Legacy_OUO is unresolved to a current standard marking, the `normalized_control_basis`  should be populated as "Legacy_Needs_Mapping" to indicate that the control basis is legacy  and needs interpretation for governance purposes. Allowed values: DOE_CUI | DOE_UCNI | EO13526_Classified | AEA_RD_FRD_TFNI | DOD_CUI | DHS_CUI | Legacy_OUO | Legacy_Site_Specific | Other_Agency | None
      classified_status: ${"Yes|No"}  # [discoverability_required] Indicates whether the asset is classified.
      classification_level: __CLASSIFICATION_LEVEL__  # [situational_required] Official classification level, if the asset is classified. Required if classified_status is "Yes". Allowed values: Top_Secret | Secret | Confidential
      classification_category: []  # [situational_required] Official classification category, if the asset is classified. Required if classified_status = "Yes". If present, at least one specified category must be included. Allowed values: NSI | RD | FRD | TFNI | Other_Classified
      classified_control_markings: []  # [discoverability_if_applicable] Additional classified dissemination/caveat/handling markings appearing with classified content. List all that apply, each as a separate entry.  This provides important context for handling and access controls for classified assets. e.g., NOFORN | CNWDI | SIGMA 15 | ORCON | REL TO USA, GBR
      cui_status: ${"Yes|No"}  # [discoverability_required] Indicates whether the asset is Controlled Unclassified Information (CUI).
      cui_basic_categories: []  # [discoverability_if_applicable] Basic CUI categories applicable to this asset, if it is CUI. Use the DOE/ISOO-authoritative CUI Basic categories or subcategories. List all that apply, each as a separate entry.  This provides important context for handling and access controls for CUI assets.
      cui_specified_categories: []  # [situational_required] Specified CUI categories applicable to this asset, if it is CUI. At least one specified category is required if cui_status = "Yes" or ucni_status = "Yes". If present, at least one specified category must be included. Use the DOE/ISOO-authoritative CUI Specified categories or subcategories. List all that apply, each as a separate entry.  This provides important context for handling and access controls for CUI assets.
      cui_limited_dissemination_controls: []  # [discoverability_if_applicable] Applicable CUI limited dissemination controls. Ordering/formatting should follow authoritative agency guidance. If cui_limited_dissemination_controls contains NOFORN, REL TO..., DISPLAY ONLY..., or similar controls, then governed_use.non_sensitivity_governance_metadata.foreign_national_access_status should be consistent with those controls. e.g., NOFORN | REL TO USA, GBR | DISPLAY ONLY USA, GBR | RELIDO | [other authoritative values.]
      ucni_status: ${"Yes|No"}  # [discoverability_required] Indicates whether the asset contains UCNI. UCNI is represented separately and should not be treated as an ordinary CUI category value. This provides important context for handling and access controls for UCNI assets.
      uk_mda_status: __UK_MDA_STATUS__  # [discoverability_if_applicable] Indicates whether the asset is subject to UK Ministry of Defence Assessment (MDA)-specific handling. Optional and may be used where relevant to local/site governance. Allowed values: "Yes" | "No" | Unknown | not_applicable
      legacy_label_source: []  # [discoverability_if_applicable] Preserves deprecated or local historical control labels such as OUO, SBU,  or site-specific legacy markings as provenance/source information only. If source_marking_scheme = Legacy_OUO, legacy_label_source should be populated with the corresponding legacy OUO labels. Provide as a list of unique entries if multiple legacy labels apply. e.g., OUO | SBU | Legacy_Site_Marking
      normalized_control_basis: []  # [discoverability_if_applicable] Optional interpreted control basis used for governance where source materials contain legacy, mixed, or non-standard constructs.  If present, it must be populated with at least one value. Provide as a list of unique entries if multiple control bases apply. This does not replace authoritative source markings. If source_marking_scheme = Legacy_OUO and the legacy marking is unresolved to a current standard marking,  this should be populated as "Legacy_Needs_Mapping" to indicate that the control basis is legacy and needs  interpretation for governance purposes. Allowed values: Classified | CUI | UCNI | Public_Release_Approved | Legacy_Needs_Mapping | Other_Controlled
    creation_method: ${CREATION_METHOD}  # [discoverability_required] The method by which the datacard was created, following a controlled vocabulary. This provides context on how the datacard was generated and can inform trust and maintenance practices. Allowed values: Manual | Automated | Hybrid
    created_date: "${YYYY-MM-DD}"  # [discoverability_required] The date the datacard was first created, in ISO 8601 format (YYYY-MM-DD). Provides temporal context for the datacard and can be used for tracking its age and relevance.
    updated_date: "__YYYY-MM-DD__"  # [discoverability_if_applicable] The date the datacard was last updated, in ISO 8601 format (YYYY-MM-DD). Date of most recent update; revise on every change to the datacard, including minor edits and version updates. This provides temporal context for the datacard and can be used for tracking its currency and maintenance.
    change_log:  # [discoverability_required] Running history of meaningful changes to this datacard. Add a new entry every time the datacard is updated. Do not overwrite or delete prior entries. If there have been no changes since creation, include a single entry with the creation date and the summary 'Initial creation'.
    - change_date: ${CHANGE_DATE}  # [discoverability_required] The date of a specific change to the datacard, in ISO 8601 format (YYYY-MM-DD).
      datacard_version: "1.0.0"  # [discoverability_required] Replace default value with the version of the updated version,  which should be incremented when the datacard is meaningfully updated.  Use semantic versioning: MAJOR.MINOR.PATCH e.g., 1.0 → 1.1 for content updates;  1.x -> 2.0 for structural changes.
      summary: ${SUMMARY}  # [discoverability_required] A brief description of what was changed in a specific update to the datacard and why. Update this text for all subsequent revisions. This provides context for each change and can be used for understanding the evolution of the datacard over time. Brief description of what changed and why. e.g., Initial creation | Updated license to CC-BY-4.0 | Added checksum after file transfer to OSTI | Corrected collection end date
    created_by:  # [discoverability_required] All individuals, organizations, AI models, or software tools that created or updated this datacard.  List in chronological order of the contribution — e.g., if an AI model generated the initial draft and a person then edited it, list the AI model first followed by the person. This provides important provenance information about the datacard and can inform trust and maintenance practices.
    - contribution_date: ${CONTRIBUTION_DATE}  # The ISO 8601 date of this specific contribution
      description: __DESCRIPTION__  # [if_applicable] Detailed description of the entity.
      creator:  # [discoverability_required] Container for the agent (person, organization, AI model, or software tool) responsible for this contribution.
        person:  # [if_applicable] A human individual.
          given_name: ${GIVEN_NAME}  # [situational_required] The given name(s) of a person.
          family_name: ${FAMILY_NAME}  # [situational_required] The family name(s) of a person.
          orcid: __ORCID__  # [if_applicable, recommended] The ORCID identifier for a person, in URL format. e.g., https://orcid.org/0000-0002-5755-8449
          email: __EMAIL__  # [if_applicable] The email address of a person.
          affiliation:  # [if_applicable, recommended] An organization with which a person is affiliated.
            name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
            ror_id: __ROR_ID__  # [if_applicable, recommended] The ROR identifier for an organization, in URL format. e.g., https://ror.org/02vwzrd76
          role: []  # [situational_required] The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
        organization:  # [if_applicable] An organization or group of individuals.
          name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
          ror_id: __ROR_ID__  # [if_applicable, recommended] The ROR identifier for an organization, in URL format. e.g., https://ror.org/02vwzrd76
          role: []  # The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
        ai_model:  # [if_applicable] An AI model.
          name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
          version: __VERSION__  # [if_applicable, recommended] Replace default with the version of the AI model, if applicable.
          accessed_date: ${ACCESSED_DATE}  # [situational_required] The ISO 8601 date when the AI model was accessed for use in creating or updating the datacard.
          identifier:  # [interoperability_if_applicable] Unique identifier for an external resource, such as a DOI, ARK, or other identifier. If one of `type` or `value` is provided, the other must also be provided.
            type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
            value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
          role: []  # The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
          relationship: ${RELATIONSHIP}  # [situational_required] The relationship of this AI model to the datacard or dataset Allowed values: is_cited_by | cites | in_series | is_supplement_to | is_supplemented_by | is_continued_by | continues | describes | is_described_by | has_metadata | is_metadata_for | has_version | is_version_of | is_previous_version_of | is_part_of | has_part | is_published_in | is_referenced_by | references | is_documented_by | documents | is_compiled_by | compiles | is_variant_form_of | is_original_form_of | is_identical_to | is_reviewed_by | reviews | is_derived_from | is_source_of | is_required_by | requires | obsoletes | is_obsoleted_by | is_collected_by | collects | is_translation_of | has_translation | other | generates | is_generated_by | processes | is_processed_by | analyzes | is_analyzed_by | is_trained_on | is_used_for_training | is_evaluated_on | is_used_for_evaluation | tested_on | validated_on | fine_tuned_from | has_evaluation
        software:  # [if_applicable] Software associated with this dataset, if any.  This can include links to software tools, libraries, or frameworks that were used to generate, process, or analyze the dataset,  which can provide users with additional context and insights about the dataset.
          name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
          version: __VERSION__  # [if_applicable, recommended] Replace default with the version of the software tool, if applicable.
          identifier:  # [interoperability_if_applicable] Unique identifier for an external resource, such as a DOI, ARK, or other identifier. If one of `type` or `value` is provided, the other must also be provided.
            type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
            value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
          role: []  # [situational_required] The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
          relationship: ${RELATIONSHIP}  # [situational_required] The relationship of this software to the datacard or dataset. Allowed values: is_cited_by | cites | in_series | is_supplement_to | is_supplemented_by | is_continued_by | continues | describes | is_described_by | has_metadata | is_metadata_for | has_version | is_version_of | is_previous_version_of | is_part_of | has_part | is_published_in | is_referenced_by | references | is_documented_by | documents | is_compiled_by | compiles | is_variant_form_of | is_original_form_of | is_identical_to | is_reviewed_by | reviews | is_derived_from | is_source_of | is_required_by | requires | obsoletes | is_obsoleted_by | is_collected_by | collects | is_translation_of | has_translation | other | generates | is_generated_by | processes | is_processed_by | analyzes | is_analyzed_by | is_trained_on | is_used_for_training | is_evaluated_on | is_used_for_evaluation | tested_on | validated_on | fine_tuned_from | has_evaluation
  identification:  # [discoverability_required] Key metadata fields that uniquely identify this dataset.
    name: ${NAME}  # Human-readable name or local string key for the entity.
    project: "genesis"  # [discoverability_required] Replace default value if necessary with a single human-readable name from the project this dataset belongs to.  May be a Genesis project or sub-project, or a non-Genesis project or sub-project. Use the same name in the datacard filename. e.g., genesis | genesis-fusion | genesis-lightsource | nuclear-physics
    version: "1.0.0"  # [discoverability_required] Dataset version using semantic versioning: MAJOR.MINOR.PATCH Increment MAJOR for breaking changes, MINOR for additions, PATCH for corrections. Start at 1.0.0 for first release. See supersedes / superseded_by below for linking versions, and stewardship.versioning_strategy for how versions are managed.
    primary_id:  # [discoverability_required] Primary identifier block for this dataset. This is the main identifier for the dataset and should be globally unique and resolvable if possible. Strongly recommended to use a persistent identifier (PID) such as a DOI or ARK. If one of `type` or `value` is provided, the other must also be provided.
      type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
      value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
    additional_ids:  # [discoverability_if_applicable] Additional identifiers for this dataset.
    - type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
      value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
    supersedes:  # [discoverability_if_applicable] Identifier of the prior version this dataset replaces. If one of type or value is provided, the other must also be provided.
      type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
      value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
    superseded_by:  # [discoverability_if_applicable] Identifier of the newer version that replaces this dataset. If one of type or value is provided, the other must also be provided.
      type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
      value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
    parent_collection:  # [discoverability_if_applicable] Class collection or experimental campaign this dataset belongs to. Use when this dataset is one of many in a larger organized collection or ensemble.
      name: ${NAME}  # Human-readable name or local string key for the entity.
      identifier:  # [interoperability_if_applicable] Unique identifier for an external resource, such as a DOI, ARK, or other identifier. If one of `type` or `value` is provided, the other must also be provided.
        type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
        value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
  dataset_description:  # [discoverability_required] Required, essential metadata fields that provide a high-level description of the dataset,  including its science domain, a description, and keywords.
    science_domain: []  # [discoverability_if_applicable] Based on OSTI Subject Areas, scientific domains or disciplines this dataset primarily relates to. Extends the the list of OSTI Subject Areas with an Other category for datasets that do not fit into the OSTI list. Those using E-Link can map to their own taxonomy. Allowed values: Biology and Medicine | Chemistry | Energy Storage, Conversion, and Utilization | Engineering | Environmental Sciences | Fission and Nuclear Technologies | Fossil Fuels | Geosciences | Materials | Mathematics and Computing | National Defense | Physics | Power Generation and Distribution | Renewable Energy | Other
    dataset_summary: ${DATASET_SUMMARY}  # [discoverability_required] A brief summary of the dataset. Recommend 1-3 sentences that provide a high-level overview of the dataset, its purpose, and its potential applications. This should be a concise overview that provides users with a quick  understanding of what the dataset is about and whether it may be relevant to their needs. Write for a broad scientific audience unfamiliar with your project.
    purpose: __PURPOSE__  # [discoverability_if_applicable] The purpose for which the dataset was created. Include the scientific question or problem it was intended to address.
    collection_methodology: __COLLECTION_METHODOLOGY__  # [discoverability_if_applicable] How was data acquired? e.g., Experimental sensors | Computational simulation | Human annotation | Derived from prior datasets
    data_characteristics: __DATA_CHARACTERISTICS__  # [discoverability_if_applicable] Describe key structural and content characteristics: scale, dimensionality, temporal coverage, spatial resolution.
    limitations: __LIMITATIONS__  # [discoverability_if_applicable, recommended] Known limitations, gaps, or caveats users should be aware of before using this dataset.
    tags:  # [discoverability_if_applicable] Structured tags block for catalog filtering and discovery,  including project, science, object_type.
      project: ${PROJECT}  # [situational_required] Replace default value if necessary with a single human-readable name from the project this dataset belongs to.  May be a Genesis project or sub-project, or a non-Genesis project or sub-project. Use the same name in the datacard filename. e.g., genesis | genesis-fusion | genesis-lightsource | nuclear-physics
      science: __SCIENCE__  # [discoverability_if_applicable] More specific scientific domain, sub-discipline, or topic. e.g., lightsource | fusion | materials | biology | synchrotron light source science | magnetic confinement fusion | materials under extreme conditions
      object_type: ${OBJECT_TYPE}  # [discoverability_required] The type of object described by this datacard. Allowed values: Dataset | Model | Software | AI_Agent | Infrastructure | Resource | Other
    task_category: []  # [discoverability_if_applicable] Primary task category or categories for this dataset. Helps ML practitioners find relevant datasets in the catalog. e.g., classification | regression | segmentation | detection | generation | translation | summarization | ranking | anomaly_detection | clustering | reinforcement_learning | other
    task_subcategory: []  # [discoverability_if_applicable] More specific task subcategory or subcategories. e.g., binary_classification | multi_class_classification | multi_label_classification | image_segmentation | object_detection | time_series_forecasting | named_entity_recognition | question_answering
    keywords: []  # [discoverability_required] Terms that describe this dataset and aid discovery. Include domain terms, methods, instruments, and relevant ontology terms.
  product_type: "Dataset"  # [discoverability_required] Replace default value if necessary with the extended from OSTI Product Types. Select the single best-fit. Allowed values: Accomplishment Report | Book | Conference | Dataset | Factsheet | Journal_Article | Miscellaneous | Other | Patent | Program_Document | Software_Manual | Thesis/Dissertation | Technical_Report | Patent_Application | Collection | Computer_Related | Model | Agent
  dataset_type: __DATASET_TYPE__  # [discoverability_if_applicable] OSTI DOE Dataset Type code. Only valid value is "Instrument" for datasets that are instrument data products. If the dataset is not an instrument data product, this field should be null. Allowed values: Instrument
  release_status: ${RELEASE_STATUS}  # [discoverability_required] The release status of the dataset This provides important context about the lifecycle stage of the dataset  and can inform users about its readiness for use. Allowed values: Draft | Under_Review | Approved | Published | Deprecated
  dataset_publisher:  # [situational_required] The publisher of the dataset, described by a name and ror_id if available. Required for datasets with release_status = Approved | Published This provides important provenance information about the dataset and can inform trust and maintenance practices.
    name: ${NAME}  # Human-readable name or local string key for the entity.
    description: __DESCRIPTION__  # [if_applicable] Detailed description of the entity.
    ror_id: __ROR_ID__  # [if_applicable, recommended] The ROR identifier for an organization, in URL format. e.g., https://ror.org/02vwzrd76
  contact:  # [discoverability_required] Contact information for questions about access to or use of this dataset. This can provide users with a direct point of contact for inquiries about the dataset, which can facilitate communication and support responsible use of the data. Perfer a person, but an organization can be provided.
  - person:  # [if_applicable] A human individual.
      given_name: ${GIVEN_NAME}  # [situational_required] The given name(s) of a person.
      family_name: ${FAMILY_NAME}  # [situational_required] The family name(s) of a person.
      orcid: __ORCID__  # [if_applicable, recommended] The ORCID identifier for a person, in URL format. e.g., https://orcid.org/0000-0002-5755-8449
      email: __EMAIL__  # [if_applicable] The email address of a person.
      affiliation:  # [if_applicable, recommended] An organization with which a person is affiliated.
        name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
        ror_id: __ROR_ID__  # [if_applicable, recommended] The ROR identifier for an organization, in URL format. e.g., https://ror.org/02vwzrd76
      role: []  # [situational_required] The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
    organization:  # [if_applicable] An organization or group of individuals.
      name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
      ror_id: __ROR_ID__  # [if_applicable, recommended] The ROR identifier for an organization, in URL format. e.g., https://ror.org/02vwzrd76
      role: []  # The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
    valid_until: __VALID_UNTIL__  # [discoverability_if_applicable] Date after which this contact may no longer be valid., in ISO 8601 format (YYYY-MM-DD). Use for project-bound contacts (students, postdocs, term staff).
    succession_note: __SUCCESSION_NOTE__  # [discoverability_if_applicable] Who to contact if this contact is no longer reachable. e.g., Contact the ORNL data management office at data@ornl.gov
  additional_contacts:  # [discoverability_if_applicable] Additional contacts such as an instrument PI, data steward, or other relevant individuals. Can include person or organization agent_types for the Contact.
  - person:  # [if_applicable] A human individual.
      given_name: ${GIVEN_NAME}  # [situational_required] The given name(s) of a person.
      family_name: ${FAMILY_NAME}  # [situational_required] The family name(s) of a person.
      orcid: __ORCID__  # [if_applicable, recommended] The ORCID identifier for a person, in URL format. e.g., https://orcid.org/0000-0002-5755-8449
      email: __EMAIL__  # [if_applicable] The email address of a person.
      affiliation:  # [if_applicable, recommended] An organization with which a person is affiliated.
        name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
        ror_id: __ROR_ID__  # [if_applicable, recommended] The ROR identifier for an organization, in URL format. e.g., https://ror.org/02vwzrd76
      role: []  # [situational_required] The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
    organization:  # [if_applicable] An organization or group of individuals.
      name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
      ror_id: __ROR_ID__  # [if_applicable, recommended] The ROR identifier for an organization, in URL format. e.g., https://ror.org/02vwzrd76
      role: []  # The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
    valid_until: __VALID_UNTIL__  # [discoverability_if_applicable] Date after which this contact may no longer be valid., in ISO 8601 format (YYYY-MM-DD). Use for project-bound contacts (students, postdocs, term staff).
    succession_note: __SUCCESSION_NOTE__  # [discoverability_if_applicable] Who to contact if this contact is no longer reachable. e.g., Contact the ORNL data management office at data@ornl.gov
  authors:  # [discoverability_required] At least one author required when release_status = Approved | Published.
  - person:  # [if_applicable] A human individual.
      given_name: ${GIVEN_NAME}  # [situational_required] The given name(s) of a person.
      family_name: ${FAMILY_NAME}  # [situational_required] The family name(s) of a person.
      orcid: __ORCID__  # [if_applicable, recommended] The ORCID identifier for a person, in URL format. e.g., https://orcid.org/0000-0002-5755-8449
      email: __EMAIL__  # [if_applicable] The email address of a person.
      affiliation:  # [if_applicable, recommended] An organization with which a person is affiliated.
        name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
        ror_id: __ROR_ID__  # [if_applicable, recommended] The ROR identifier for an organization, in URL format. e.g., https://ror.org/02vwzrd76
      role: []  # [situational_required] The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
    organization:  # [if_applicable] An organization or group of individuals.
      name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
      ror_id: __ROR_ID__  # [if_applicable, recommended] The ROR identifier for an organization, in URL format. e.g., https://ror.org/02vwzrd76
      role: []  # The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
    ai_model:  # [if_applicable] An AI model.
      name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
      version: __VERSION__  # [if_applicable, recommended] Replace default with the version of the AI model, if applicable.
      accessed_date: ${ACCESSED_DATE}  # [situational_required] The ISO 8601 date when the AI model was accessed for use in creating or updating the datacard.
      identifier:  # [interoperability_if_applicable] Unique identifier for an external resource, such as a DOI, ARK, or other identifier. If one of `type` or `value` is provided, the other must also be provided.
        type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
        value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
      role: []  # The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
      relationship: ${RELATIONSHIP}  # [situational_required] The relationship of this AI model to the datacard or dataset Allowed values: is_cited_by | cites | in_series | is_supplement_to | is_supplemented_by | is_continued_by | continues | describes | is_described_by | has_metadata | is_metadata_for | has_version | is_version_of | is_previous_version_of | is_part_of | has_part | is_published_in | is_referenced_by | references | is_documented_by | documents | is_compiled_by | compiles | is_variant_form_of | is_original_form_of | is_identical_to | is_reviewed_by | reviews | is_derived_from | is_source_of | is_required_by | requires | obsoletes | is_obsoleted_by | is_collected_by | collects | is_translation_of | has_translation | other | generates | is_generated_by | processes | is_processed_by | analyzes | is_analyzed_by | is_trained_on | is_used_for_training | is_evaluated_on | is_used_for_evaluation | tested_on | validated_on | fine_tuned_from | has_evaluation
    software:  # [if_applicable] Software associated with this dataset, if any.  This can include links to software tools, libraries, or frameworks that were used to generate, process, or analyze the dataset,  which can provide users with additional context and insights about the dataset.
      name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
      version: __VERSION__  # [if_applicable, recommended] Replace default with the version of the software tool, if applicable.
      identifier:  # [interoperability_if_applicable] Unique identifier for an external resource, such as a DOI, ARK, or other identifier. If one of `type` or `value` is provided, the other must also be provided.
        type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
        value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
      role: []  # [situational_required] The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
      relationship: ${RELATIONSHIP}  # [situational_required] The relationship of this software to the datacard or dataset. Allowed values: is_cited_by | cites | in_series | is_supplement_to | is_supplemented_by | is_continued_by | continues | describes | is_described_by | has_metadata | is_metadata_for | has_version | is_version_of | is_previous_version_of | is_part_of | has_part | is_published_in | is_referenced_by | references | is_documented_by | documents | is_compiled_by | compiles | is_variant_form_of | is_original_form_of | is_identical_to | is_reviewed_by | reviews | is_derived_from | is_source_of | is_required_by | requires | obsoletes | is_obsoleted_by | is_collected_by | collects | is_translation_of | has_translation | other | generates | is_generated_by | processes | is_processed_by | analyzes | is_analyzed_by | is_trained_on | is_used_for_training | is_evaluated_on | is_used_for_evaluation | tested_on | validated_on | fine_tuned_from | has_evaluation
  contributors:  # [discoverability_if_applicable] Supporting contributors who are not primary authors. e.g., sample preparers, annotators, reviewers, submitters. For draft or in-workflow data, populate with known contributors.
  - person:  # [if_applicable] A human individual.
      given_name: ${GIVEN_NAME}  # [situational_required] The given name(s) of a person.
      family_name: ${FAMILY_NAME}  # [situational_required] The family name(s) of a person.
      orcid: __ORCID__  # [if_applicable, recommended] The ORCID identifier for a person, in URL format. e.g., https://orcid.org/0000-0002-5755-8449
      email: __EMAIL__  # [if_applicable] The email address of a person.
      affiliation:  # [if_applicable, recommended] An organization with which a person is affiliated.
        name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
        ror_id: __ROR_ID__  # [if_applicable, recommended] The ROR identifier for an organization, in URL format. e.g., https://ror.org/02vwzrd76
      role: []  # [situational_required] The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
    organization:  # [if_applicable] An organization or group of individuals.
      name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
      ror_id: __ROR_ID__  # [if_applicable, recommended] The ROR identifier for an organization, in URL format. e.g., https://ror.org/02vwzrd76
      role: []  # The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
    ai_model:  # [if_applicable] An AI model.
      name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
      version: __VERSION__  # [if_applicable, recommended] Replace default with the version of the AI model, if applicable.
      accessed_date: ${ACCESSED_DATE}  # [situational_required] The ISO 8601 date when the AI model was accessed for use in creating or updating the datacard.
      identifier:  # [interoperability_if_applicable] Unique identifier for an external resource, such as a DOI, ARK, or other identifier. If one of `type` or `value` is provided, the other must also be provided.
        type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
        value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
      role: []  # The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
      relationship: ${RELATIONSHIP}  # [situational_required] The relationship of this AI model to the datacard or dataset Allowed values: is_cited_by | cites | in_series | is_supplement_to | is_supplemented_by | is_continued_by | continues | describes | is_described_by | has_metadata | is_metadata_for | has_version | is_version_of | is_previous_version_of | is_part_of | has_part | is_published_in | is_referenced_by | references | is_documented_by | documents | is_compiled_by | compiles | is_variant_form_of | is_original_form_of | is_identical_to | is_reviewed_by | reviews | is_derived_from | is_source_of | is_required_by | requires | obsoletes | is_obsoleted_by | is_collected_by | collects | is_translation_of | has_translation | other | generates | is_generated_by | processes | is_processed_by | analyzes | is_analyzed_by | is_trained_on | is_used_for_training | is_evaluated_on | is_used_for_evaluation | tested_on | validated_on | fine_tuned_from | has_evaluation
    software:  # [if_applicable] Software associated with this dataset, if any.  This can include links to software tools, libraries, or frameworks that were used to generate, process, or analyze the dataset,  which can provide users with additional context and insights about the dataset.
      name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
      version: __VERSION__  # [if_applicable, recommended] Replace default with the version of the software tool, if applicable.
      identifier:  # [interoperability_if_applicable] Unique identifier for an external resource, such as a DOI, ARK, or other identifier. If one of `type` or `value` is provided, the other must also be provided.
        type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
        value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
      role: []  # [situational_required] The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
      relationship: ${RELATIONSHIP}  # [situational_required] The relationship of this software to the datacard or dataset. Allowed values: is_cited_by | cites | in_series | is_supplement_to | is_supplemented_by | is_continued_by | continues | describes | is_described_by | has_metadata | is_metadata_for | has_version | is_version_of | is_previous_version_of | is_part_of | has_part | is_published_in | is_referenced_by | references | is_documented_by | documents | is_compiled_by | compiles | is_variant_form_of | is_original_form_of | is_identical_to | is_reviewed_by | reviews | is_derived_from | is_source_of | is_required_by | requires | obsoletes | is_obsoleted_by | is_collected_by | collects | is_translation_of | has_translation | other | generates | is_generated_by | processes | is_processed_by | analyzes | is_analyzed_by | is_trained_on | is_used_for_training | is_evaluated_on | is_used_for_evaluation | tested_on | validated_on | fine_tuned_from | has_evaluation
  sponsor_organizations:  # [discoverability_required] Organizations that funded or sponsored this dataset.
  - name: ${NAME}  # [discoverability_required] The name of the sponsoring organization. E.g., DOE Office of Science | NNSA | NSF
    ror_id: __ROR_ID__  # [discoverability_if_applicable, recommended] The ROR ID of the sponsoring organization, if available. E.g., https://ror.org/02vwzrd76 e.g., https://ror.org/02vwzrd76
    award_number: __AWARD_NUMBER__  # [discoverability_if_applicable, recommended] Award number(s) associated with the funding for this dataset. e.g., DE-AC05-00OR22725
    funding_source: __FUNDING_SOURCE__  # [discoverability_if_applicable, recommended] Funder or sponsor of the research that produced this dataset. Allowed values: DOE_Program_SC | DOE_Program_NNSA | LDRD | WFO | CRADA | Other_Federal | State_Government | Subcontract | Industry | Nonprofit | Internal | Other
    program: __PROGRAM__  # [discoverability_if_applicable, recommended] The program or initiative under which this dataset was created. e.g., Advanced Scientific Computing Research | Predictive Science Academic Alliance Program | Fusion Energy Sciences
  sponsoring_doe_program_office: __SPONSORING_DOE_PROGRAM_OFFICE__  # [discoverability_if_applicable] The DOE program office that sponsored or funded the research that produced this dataset. e.g., Office of Science | National Nuclear Security Administration | Office of Energy Efficiency and Renewable Energy
  sponsoring_doe_subprogram: __SPONSORING_DOE_SUBPROGRAM__  # [discoverability_if_applicable] The DOE subprogram that sponsored or funded the research that produced this dataset. e.g., Advanced Scientific Computing Research | Predictive Science Academic Alliance Program | Fusion Energy Sciences
  research_organizations:  # [discoverability_required] Organizations that created or collected the data.
  - name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
    ror_id: __ROR_ID__  # [if_applicable, recommended] The ROR ID of the research organization, if available. E.g., https://ror.org/02vwzrd76 e.g., https://ror.org/02vwzrd76
    role: []  # [discoverability_if_applicable] The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
  facilities:  # [discoverability_if_applicable] User facilities, HPC centers, or research infrastructure used to collect, process, or store the dataset.
  - name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
    ror_id: __ROR_ID__  # [if_applicable, recommended] The ROR ID of the facility, if available. E.g., https://ror.org/02vwzrd76 e.g., https://ror.org/02vwzrd76
    role: []  # The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
    location:  # [discoverability_if_applicable] Point location for facility-based experimental data, if applicable. description: should include the place name and, location details.
      description: ${DESCRIPTION}  # [if_applicable] Detailed description of the entity.
      ror_id: __ROR_ID__  # [if_applicable, recommended] The ROR ID of the location, if available. E.g., https://ror.org/02vwzrd76 e.g., https://ror.org/02vwzrd76
  sensitivity:  # [discoverability_required] Sensitivity of the DATASET, which may differ from the sensitivity of the data card.  Populate based on the sensitivity of the dataset alone, not the data card.  See NOTE ON SENSITIVITY above.  NOTE: Sensitivity terminology is still under Genesis governance review. Vocabulary may evolve.
    overall_sensitivity: ${OVERALL_SENSITIVITY}  # [discoverability_required] Human-readable top-level sensitivity posture of the data card (for `discoverability.datacard.sensitivity`), or the dataset (for `discoverability.sensitivity`) - do not automatically set the overall sensitivity of the  data card and dataset sensitivity to the same value, as they may differ. The field value is based on the authoritative source markings and metadata fields. This is a summary field only and does not replace the authoritative fields such as the classification_status, classification_level, export_control_basis, or privacy_control_basis fields. Authoritative source markings and metadata fields should be used for access control and governance decisions. Use "Public" for unclassified, non-sensitive assets that can be shared publicly. Allowed values: Public | Unclassified_Uncontrolled | CUI | UCNI | Classified | Legacy_Controlled | Mixed | Other_Controlled
    source_marking_string: ${SOURCE_MARKING_STRING}  # [discoverability_required] Exact marking/banner/control text as it appears on the source artifact or in the authoritative review/release output, if applicable. The artifact is either the data card (for `discoverability.datacard.sensitivity`), or the dataset (for `discoverability.sensitivity`). Provides the authoritative source marking information for the asset,  which is critical for ensuring proper handling and access controls based on the sensitivity of the asset. If no source markings apply to the asset, this field should be filled with "not_applicable". If the asset has multiple source markings, list them separated by // with no spaces. This field does not replace the individual metadata fields for classification status,  classification level, export control basis, or privacy control basis,  which should still be filled out based on the authoritative source markings. e.g., not_applicable | CUI//SP-EXPT//NOFORN | SECRET//RD//SIGMA 15 | OFFICIAL USE ONLY
    source_marking_scheme: ${SOURCE_MARKING_SCHEME}  # [discoverability_required] Identifies the authoritative source marking regime, for the source_marking_string field. Use "None" for unclassified, non-sensitive assets that can be shared publicly. If a Legacy_OUO is unresolved to a current standard marking, the `normalized_control_basis`  should be populated as "Legacy_Needs_Mapping" to indicate that the control basis is legacy  and needs interpretation for governance purposes. Allowed values: DOE_CUI | DOE_UCNI | EO13526_Classified | AEA_RD_FRD_TFNI | DOD_CUI | DHS_CUI | Legacy_OUO | Legacy_Site_Specific | Other_Agency | None
    classified_status: ${"Yes|No"}  # [discoverability_required] Indicates whether the asset is classified.
    classification_level: __CLASSIFICATION_LEVEL__  # [situational_required] Official classification level, if the asset is classified. Required if classified_status is "Yes". Allowed values: Top_Secret | Secret | Confidential
    classification_category: []  # [situational_required] Official classification category, if the asset is classified. Required if classified_status = "Yes". If present, at least one specified category must be included. Allowed values: NSI | RD | FRD | TFNI | Other_Classified
    classified_control_markings: []  # [discoverability_if_applicable] Additional classified dissemination/caveat/handling markings appearing with classified content. List all that apply, each as a separate entry.  This provides important context for handling and access controls for classified assets. e.g., NOFORN | CNWDI | SIGMA 15 | ORCON | REL TO USA, GBR
    cui_status: ${"Yes|No"}  # [discoverability_required] Indicates whether the asset is Controlled Unclassified Information (CUI).
    cui_basic_categories: []  # [discoverability_if_applicable] Basic CUI categories applicable to this asset, if it is CUI. Use the DOE/ISOO-authoritative CUI Basic categories or subcategories. List all that apply, each as a separate entry.  This provides important context for handling and access controls for CUI assets.
    cui_specified_categories: []  # [situational_required] Specified CUI categories applicable to this asset, if it is CUI. At least one specified category is required if cui_status = "Yes" or ucni_status = "Yes". If present, at least one specified category must be included. Use the DOE/ISOO-authoritative CUI Specified categories or subcategories. List all that apply, each as a separate entry.  This provides important context for handling and access controls for CUI assets.
    cui_limited_dissemination_controls: []  # [discoverability_if_applicable] Applicable CUI limited dissemination controls. Ordering/formatting should follow authoritative agency guidance. If cui_limited_dissemination_controls contains NOFORN, REL TO..., DISPLAY ONLY..., or similar controls, then governed_use.non_sensitivity_governance_metadata.foreign_national_access_status should be consistent with those controls. e.g., NOFORN | REL TO USA, GBR | DISPLAY ONLY USA, GBR | RELIDO | [other authoritative values.]
    ucni_status: ${"Yes|No"}  # [discoverability_required] Indicates whether the asset contains UCNI. UCNI is represented separately and should not be treated as an ordinary CUI category value. This provides important context for handling and access controls for UCNI assets.
    uk_mda_status: __UK_MDA_STATUS__  # [discoverability_if_applicable] Indicates whether the asset is subject to UK Ministry of Defence Assessment (MDA)-specific handling. Optional and may be used where relevant to local/site governance. Allowed values: "Yes" | "No" | Unknown | not_applicable
    legacy_label_source: []  # [discoverability_if_applicable] Preserves deprecated or local historical control labels such as OUO, SBU,  or site-specific legacy markings as provenance/source information only. If source_marking_scheme = Legacy_OUO, legacy_label_source should be populated with the corresponding legacy OUO labels. Provide as a list of unique entries if multiple legacy labels apply. e.g., OUO | SBU | Legacy_Site_Marking
    normalized_control_basis: []  # [discoverability_if_applicable] Optional interpreted control basis used for governance where source materials contain legacy, mixed, or non-standard constructs.  If present, it must be populated with at least one value. Provide as a list of unique entries if multiple control bases apply. This does not replace authoritative source markings. If source_marking_scheme = Legacy_OUO and the legacy marking is unresolved to a current standard marking,  this should be populated as "Legacy_Needs_Mapping" to indicate that the control basis is legacy and needs  interpretation for governance purposes. Allowed values: Classified | CUI | UCNI | Public_Release_Approved | Legacy_Needs_Mapping | Other_Controlled
  workflow:  # [discoverability_required] Describes the technical and processing lifecycle position of the dataset.  discoverability.workflow.state — describes the technical/processing lifecycle position of the data itself (raw → archived) reusability.release_status — describes the publication and governance state of the dataset record (draft → deprecated) These should be logically consistent. Common alignments: discoverability.workflow.state=Raw|Processing|QA|Analysis → reusability.release_status=Draft discoverability.workflow.state=Review → reusability.release_status=Under_Review discoverability.workflow.state=Embargo|Published → reusability.release_status=Approved|Published discoverability.workflow.state=Archived → reusability.release_status=Deprecated|Published
    state: ${STATE}  # [discoverability_required] Current lifecycle position of the data itself, following StateEnum controlled vocabulary. Allowed values: Raw | Processing | QA | Analysis | Review | Embargo | Published | Archived | not_applicable
    is_intermediate: __"Yes|No"__  # [discoverability_if_applicable, recommended] Whether this dataset is an intermediate output, as opposed to a final deliverable. "No" if this is final.
    pipeline_stage: __PIPELINE_STAGE__  # [discoverability_if_applicable, recommended] Freetext position in processing pipeline. e.g., raw telemetry, pre-calibration | post-detector, pre-reconstruction | post-reconstruction, pre-analysis
    embargo_until: "__YYYY-MM-DD__"  # [situational_required] Required if state=Embargo. ISO 8601 date after which release is permitted.
accessibility:  # [accessibility_required] ###---Accessibility---### Metadata fields that support the accessibility of the dataset. These fields provide critical information about how to access the dataset,  including any restrictions or requirements for access. The accessibility capability is required for datacards of datasets that are intended to be shared or accessed by others,  whether internally within a project or organization, with external collaborators, or publicly.
  access_policy:  # [accessibility_required] Describes who can access this dataset and under what conditions. access_policy.access_level describes the dataset's access sensitivity — the same subject as sensitivity.overall_sensitivity. Reproduced here for access control systems that evaluate this block independently. See NOTE ON SENSITIVITY TIERS above.
    access_level: ${ACCESS_LEVEL}  # [accessibility_required] The access level of the dataset. This provides important context about who can access the dataset and can inform users about potential barriers to access and use. This does not replace the authoritative source markings and metadata fields for classification, CUI, or other sensitivity designations,  which should still be filled out based on the authoritative source markings. Allowed values: Open | Restricted | Controlled
    access_restrictions: __ACCESS_RESTRICTIONS__  # [accessibility_if_applicable] Freetext description of any specific access restrictions or requirements for the dataset, beyond what is indicated by the classification and sensitivity markings. This can provide more detailed information about who is allowed to access the  dataset and under what conditions, which can inform users about potential barriers to access and use. e.g., Requires signed DUA | None - publicly accessible | Access limited to cleared personnel with need-to-know | Requires two-factor authentication and secure VPN access
    authorization_required: []  # [accessibility_if_applicable] List of authorizations required. When formal authorization is required to access the datase. Allowed values: Account | User_Agreement | Data_Use_Agreement | Sponsor_Approval | Export_Control_Review | IRB_Approval | Other
    intended_partner_classes: []  # [accessibility_if_applicable] The intended partner classes/types (list) that are expected to access and use this dataset, if applicable. If absent, or null, this field is not yet known or determined.  Use an empty list if definitively no specific partner classes are targeted. Use Public if this dataset is intended for broad public use without restrictions. Allowed values: Internal_Team | Tri_Lab | DOE_NNSA_Lab | Federal_Partner | Contractor | Academic_Researchers | External_Research_Partner | Industry_Partner | Public | Other
    approved_environments: []  # [accessibility_if_applicable] Approved environments for accessing or using the dataset, if applicable. Use an empty list ([]) if there are no specific approved environments or if the dataset is publicly accessible. null or absent means it has not yet been determined whether approved environments are required. This can inform users about where they are allowed to access and use the dataset,  which can be important for compliance with security requirements. Allowed values: JUCE | Classified Enclave | CUI Approved Enclave | Cloud Enclave (Authorized)
    policy_url: __POLICY_URL__  # [accessibility_if_applicable] URL to the official access policy or data use agreement governing this dataset. This can provide users with direct access to the full terms and conditions for using the dataset, which can inform their understanding of legal and ethical requirements.
    policy_text: __POLICY_TEXT__  # [accessibility_if_applicable] Inline summary if no policy_url exists. This can provide users with a quick overview of the key terms and conditions  for using the dataset, which can inform their understanding of legal and ethical requirements.
  access:  # [accessibility_required] Access Endpoints information.  This can include the current location/landingpage, and intended repository information,  such as access instructions and APIs. Intended to provide information on how to access the dataset for humans and machines.
    current_location: ${CURRENT_LOCATION}  # [accessibility_required] Where the data physically resides right now. Use for in-workflow data not yet deposited in a repository,  or for any dataset with a known internal or external storage path. e.g., /mnt/ecs/scientific-data/project/dataset/ | /lustre/orion/proj-shared/dataset/ | s3://genesis-bucket/dataset/
    publicly_facing_landing_page_url: __PUBLICLY_FACING_LANDING_PAGE_URL__  # [accessibility_if_applicable] A publicly facing URL that provides information about the dataset and how to access it. It may differ from the current_location if the dataset is not yet publicly released or if the current_location is an internal storage path. This can provide users with a direct point of access for learning more about the dataset and how to obtain it.
    intended_repositories:  # [accessibility_if_applicable] Repositories you intend to deposit or have deposited this dataset in.  The managing repository or catalog system will resolve and populate repository-assigned fields at ingest (see repository_managed slot).  Repositories may be institutional, project-owned, community, or national  (e.g., Zenodo, institutional data repository, project data store).
    - name: ${NAME}  # Human-readable name or local string key for the entity.
      access_level: ${ACCESS_LEVEL}  # [accessibility_required] The access level of the dataset. This provides important context about who can access the dataset and can inform users about potential barriers to access and use. This does not replace the authoritative source markings and metadata fields for classification, CUI, or other sensitivity designations,  which should still be filled out based on the authoritative source markings. Allowed values: Open | Restricted | Controlled
      is_primary: __"Yes|No"__  # [accessibility_if_applicable] Whether this is the primary or authoritative location for the dataset. Only one IntendedRepository should be marked as primary.  This can help users identify the most reliable or official source for accessing the dataset,  especially if there are multiple access points or repositories where the data is available.
      date_deposited: __DATE_DEPOSITED__  # [accessibility_if_applicable] The date when the dataset was deposited in the repository, in ISO 8601 format (YYYY-MM-DD). Can inform users about the currency of the data.
      data_services:  # [accessibility_if_applicable] APIs available for accessing the dataset, if any. This can provide users with information about programmatic access options for the dataset,  which can facilitate integration into workflows.
      - name: ${NAME}  # The name of the data service or API endpoint. e.g., REST API | GraphQL endpoint
        endpoint: __ENDPOINT__  # [accessibility_if_applicable] The URL or connection string for an API endpoint that provides access to the dataset. Provide users with direct access to programmatic interfaces for working with the dataset. Useful for enabling machine-actionable data documentation.
        documentation_url: __DOCUMENTATION_URL__  # [accessibility_if_applicable] URL to documentation for the API or access method. This can provide users with important information about how to use the API or access method effectively,  which can facilitate integration into AI/ML workflows and other data processing pipelines. Useful for enabling machine-actionable data documentation.
        authentication: __AUTHENTICATION__  # [accessibility_if_applicable] Whether authentication is required to access the dataset through this endpoint. Informs users about potential barriers to access and can help them prepare \ for any necessary credentials or permissions needed to work with the dataset. Allowed values: None | API_Key | OAuth2 | SAML | Certificate | OpenID_Connect | Basic_Auth | Bearer_Token | Other
        version: __VERSION__  # Version of software, tool, or library.
        rate_limit: __RATE_LIMIT__  # [accessibility_if_applicable] Any rate limits or access restrictions for the API endpoint. Informs users about potential limitations on how frequently they can access the dataset  through the API, which can help them plan their data processing and analysis workflows accordingly. e.g., 1000 requests/hour | 5000 requests/day | 1000 requests/hour and no more than 100 concurrent connections
  dataset_scale:  # [accessibility_if_applicable] These fields describe the scale of the dataset, w hich is important for users to understand the scope and potential  resource requirements for using the dataset. 
    record_count: __RECORD_COUNT__  # [accessibility_if_applicable] The number of records or rows in the dataset.
    record_unit: __RECORD_UNIT__  # [accessibility_if_applicable] The unit of measurement for the record count, such as samples, files, records, timesteps, images, tokens, other).
    compressed_bytes: __COMPRESSED_BYTES__  # [accessibility_if_applicable] The size of the dataset in bytes when compressed.
    uncompressed_bytes: __UNCOMPRESSED_BYTES__  # [accessibility_if_applicable] The size of the dataset in bytes when uncompressed.
interoperability:  # [interoperability_required] ###---Interoperability---### These fields are intended to enable users to integrate the dataset with other datasets or systems,  or use it in combination with other datasets. These fields provide critical information about the meaning, data representation and structure, provenance, related resources and integrity of the dataset.
  data_structure:  # [interoperability_required] Fields describing the format, encoding, and structure of the dataset.
    formats: []  # [interoperability_required] File formats included in this dataset. e.g., csv | json | parquet | hdf5 | netcdf | jpeg | png | tiff | wav | mp3 | mp4 | avi | application/octet-stream | binary
    encoding: __ENCODING__  # [interoperability_if_applicable] Character encoding for text-based formats. UTF-8 strongly recommended. Use not_applicable for binary formats. e.g., UTF-8 | ASCII | Latin-1 | not_applicable
    schema_version: __SCHEMA_VERSION__  # [interoperability_if_applicable] Version of the data schema used in this dataset. Distinct from datacard_version. Increment when the data schema changes,  even if the datacard version remains the same.
    modalities: []  # [interoperability_required] Data modalities present. e.g., tabular | image | time-series | text | graph | point-cloud
    features:  # [interoperability_required] Primary variables, fields, or features. IMPORTANT: choose ONE form and use it consistently — do not mix. For basic discoverability — flat string list: e.g.,    name: temperature   name: pressure   name: timestamp   name: label To enhance interoperability, reuse, and AI-readiness (replace flat list above).   - name: temperature       description: Sample temperature at time of measurement       data_type: float       unit: Kelvin       range: "273.15 - 373.15"
    - name: ${NAME}  # The name of the feature or variable.
      description: __DESCRIPTION__  # [if_applicable] Detailed description of the entity.
      data_type: __DATA_TYPE__  # [interoperability_if_applicable] The data type of a feature or variable, following a controlled vocabulary from  (e.g., float, int, string, boolean, datetime, other). This can provide important information about the nature of the data and can inform users about how to interpret and work with the dataset.
      unit: __UNIT__  # [interoperability_if_applicable] The unit of measurement for a feature. This can provide important context for interpreting the values of the feature.
      range: __RANGE__  # [interoperability_if_applicable] The range of values for a feature. This can provide important information about the expected values for a feature  and can inform users about how to work with the data effectively.
    splits: []  # [interoperability_if_applicable] Dataset splits if pre-divided. Information about splits within the dataset. This can provide important context for how the dataset is structured for data-driven modeling  and can inform users about how to use the data effectively for model training and evaluation. e.g., train | test | validation. e.g., train | test | validation
    language: "en"  # [interoperability_if_applicable] The language(s) represented in the dataset, using the ISO 639-1 language codes. E.g., en | es | fr | zh e.g., en | es | fr | de | zh | ru | ar | pt | ja | ko
    spatial_coverage:  # [interoperability_if_applicable] Spatial coverage block for geospatial datasets, if applicable. This can include a description and slots for the bounding box coordinates. such as bounding boxes, place names, or other location-based metadata that can inform users  about the spatial context of the data.
      description: __DESCRIPTION__  # [if_applicable] Detailed description of the spatial coverage.
      geo_location_box:  # [interoperability_if_applicable] Geographic bounding box for geospatial datasets, if applicable. Container for elements describing the west_bound_longitude, east_bound_longitude, south_bound_latitude, and north_bound_latitude in decimal degrees. e.g., west_bound_longitude: -125.0, east_bound_longitude: -66.5, south_bound_latitude: 24.0, north_bound_latitude: 49.0 for continental US
        west_bound_longitude: __WEST_BOUND_LONGITUDE__  # [interoperability_if_applicable] Westernmost longitude in decimal degrees for geospatial datasets.
        east_bound_longitude: __EAST_BOUND_LONGITUDE__  # [interoperability_if_applicable] Easternmost longitude in decimal degrees for geospatial datasets.
        south_bound_latitude: __SOUTH_BOUND_LATITUDE__  # [interoperability_if_applicable] Southernmost latitude in decimal degrees for geospatial datasets.
        north_bound_latitude: __NORTH_BOUND_LATITUDE__  # [interoperability_if_applicable] Northernmost latitude in decimal degrees for geospatial datasets.
    temporal_coverage:  # [interoperability_if_applicable] Temporal coverage for time-based datasets, if applicable. Container for elements describing the start_date and end_date of the dataset's temporal coverage in ISO 8601 format (YYYY-MM-DD). NOTE: distinct from dates.data_collection_start/end, which describe when collection occurred. Use temporal_coverage when the dataset describes a specific historical or projected time period that differs from when collection happened. e.g., start_date: 2020-01-01, end_date: 2020-12-31 for a dataset covering the year 2020.
      start_date: __START_DATE__  # [interoperability_if_applicable] Start date of the dataset's temporal coverage in ISO 8601 format (YYYY-MM-DD).
      end_date: __END_DATE__  # [interoperability_if_applicable] End date of the dataset's temporal coverage in ISO 8601 format (YYYY-MM-DD).
      description: __DESCRIPTION__  # [interoperability_if_applicable] Detailed description of the temporal coverage.
  provenance:  # [interoperability_required] Provenance information about the dataset, including its origin, history,  and any transformations/processing it has undergone. Provides important context for understanding the dataset and can inform users  about its reliability and suitability for their intended use and facilitate reuse  and reproducibility.
    was_generated_by: ${WAS_GENERATED_BY}  # [interoperability_required] High-level description of the generating process. Even a one-line answer dramatically improves catalog value. e.g., Neutron scattering experiment at SNS Beamline 1B | Monte Carlo simulation using MCNP 6.2 | Derived from raw telemetry via calibration pipeline v2.1
    source_data:  # [interoperability_if_applicable] Source datasets this dataset was derived from.  Captures the relationship and provenance information  about the source datasets.
    - name: ${NAME}  # The name of the source dataset.
      description: __DESCRIPTION__  # [if_applicable] Detailed description of the entity.
      identifier:  # [interoperability_if_applicable] Unique identifier for an external resource, such as a DOI, ARK, or other identifier. If one of `type` or `value` is provided, the other must also be provided.
        type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
        value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
      relationship: __RELATIONSHIP__  # [interoperability_if_applicable] The relationship of the source dataset to the current dataset. Allowed values: is_cited_by | cites | in_series | is_supplement_to | is_supplemented_by | is_continued_by | continues | describes | is_described_by | has_metadata | is_metadata_for | has_version | is_version_of | is_previous_version_of | is_part_of | has_part | is_published_in | is_referenced_by | references | is_documented_by | documents | is_compiled_by | compiles | is_variant_form_of | is_original_form_of | is_identical_to | is_reviewed_by | reviews | is_derived_from | is_source_of | is_required_by | requires | obsoletes | is_obsoleted_by | is_collected_by | collects | is_translation_of | has_translation | other | generates | is_generated_by | processes | is_processed_by | analyzes | is_analyzed_by | is_trained_on | is_used_for_training | is_evaluated_on | is_used_for_evaluation | tested_on | validated_on | fine_tuned_from | has_evaluation
    processing_steps: ${PROCESSING_STEPS}  # [interoperability_required] Key processing, cleaning, calibration, or transformation steps applied to produce this dataset. Describe any processing steps, transformations, or cleaning that have been applied to the dataset. This can provide important context for understanding the dataset and can inform users  about its reliability and suitability for their intended use.
    instrumentation: __INSTRUMENTATION__  # [interoperability_if_applicable] Instruments, sensors, detectors, or equipment used to collect the data, if applicable. Include make, model, and version where relevant. This can provide important context for understanding the dataset. e.g., Neutron scattering experiment using a He-3 position-sensitive detector at SNS Beamline 1B | Data collected using a Tektronix TDS2024C oscilloscope | Satellite remote sensing data from the MODIS instrument on the Terra satellite
    simulation_details: __SIMULATION_DETAILS__  # [interoperability_if_applicable] For simulation-derived data: code, simulation setup, version, key parameters, and configuration for simulated datasets, if applicable. This can provide important context for understanding the dataset and can inform users about its reliability and suitability for their intended use. e.g., Monte Carlo simulation using MCNP 6.2 with a 10x10x10 grid, 1 million particles, and physics models X, Y, Z | Molecular dynamics simulation using LAMMPS version 3Mar2020 with the following input script: ... | Climate model simulation using the Community Earth System Model (CESM) version 2.1 with the following configuration: ...
    software_environment:  # [interoperability_if_applicable] Software environment block used to generate or process this dataset,  Captures details about os, container, and hpc environment. Captures what is needed for computational reproducibility, including software environment details  for datasets that are generated or processed using specific software tools.
      os: __OS__  # [interoperability_if_applicable] Operating system used in the software environment for generating or processing this dataset. e.g., RHEL 8.6 | Ubuntu 22.04
      compiler: __COMPILER__  # [interoperability_if_applicable] Compiler used in the software environment for generating or processing this dataset. e.g., GCC 11.3.0 | Intel oneAPI 2023.1 | Clang 14.0.6
      container: __CONTAINER__  # [interoperability_if_applicable] Containerization technology used in the software environment  for generating or processing this dataset. e.g., docker://registry/image:tag | singularity://registry/image:tag | Docker 20.10.12 | Singularity 3.8.7
      hpc_environment: __HPC_ENVIRONMENT__  # [interoperability_if_applicable] HPC environment or platform used in the software environment for generating  or processing this dataset. e.g., Orion HPC at Oak Ridge National Laboratory sourcing the following environment modules: python/3.10, cuda/11.8, openmpi/4.1 | Summit HPC at Oak Ridge National Laboratory sourcing the following environment modules: python/3.9, cuda/11.4, openmpi/4.0 | NERSC Cori supercomputer using the following environment modules: python/3.8, cuda/11.2, openmpi/4.0
      notes: __NOTES__  # [interoperability_if_applicable] Additional environment details, key library versions, or reference to a full environment manifest. e.g., See requirements.txt in dataset root | numpy 1.24, pytorch 2.0.1, h5py 3.8.0
  dates:  # [interoperability_if_applicable] Fields for important dataset dates metadata, including collection, issued, and modified dates.
    data_collection_start: "__YYYY-MM-DD__"  # [interoperability_if_applicable] The date when data collection for this dataset started, in ISO 8601 format (YYYY-MM-DD).
    data_collection_end: "__YYYY-MM-DD__"  # [interoperability_if_applicable] The date when data collection for this dataset ended, in ISO 8601 format (YYYY-MM-DD).
    issued: __ISSUED__  # [interoperability_if_applicable] The ISO 8601 (YYYY-MM-DD) date the dataset was first publicly released.
    modified: __MODIFIED__  # [interoperability_if_applicable] The ISO 8601 (YYYY-MM-DD) date the dataset was most recently modified.
  semantic_layer:  # [interoperability_if_applicable] Required for federated or cross-domain use. Populate schema_url at minimum. Contains elements to provide a machine-readable semantic layer for the dataset.
    schema_url: __SCHEMA_URL__  # [interoperability_if_applicable] URL pointing to the schema or ontology that defines the semantic layer for this dataset. URL to a formal schema for this dataset, e.g., URL to a JSON Schema | XML Schema | NeXus application definition "not_applicable" if there is no formal schema or ontology for this dataset. Be explicit if there is no formal schema or ontology (e.g., "not_applicable") rather than leaving this field blank. This can provide users with access to the formal definitions and relationships that underpin the dataset's semantic layer. e.g., https://example.com/schema/dataset_semantic_layer.json | https://example.com/ontology/dataset_semantic_layer.owl | not_applicable
    semantic_context: []  # [interoperability_if_applicable] A human-readable description of the semantic context and structure of the dataset. Semantic conventions applied. This can provide users with important information about the meaning and relationships  of the data elements within the dataset,  which can inform their understanding and use of the dataset for AI/ML applications. e.g., NetCDF CF Conventions 1.10 | NeXus NXmonopd | Custom schema with the following key classes and relationships: ...
  related_resources:  # [interoperability_if_applicable] Related Resources: Links to related datasets, publications, software, and AI models. 
    datasets:  # [interoperability_if_applicable] Related datasets, if any.  This can include links to other datasets that are relevant to understanding and using the dataset effectively,  such as source datasets, derived datasets, or complementary datasets.
    - name: ${NAME}  # Human-readable name or local string key for the entity.
      description: __DESCRIPTION__  # [if_applicable] Detailed description of the entity.
      identifier:  # [interoperability_if_applicable] Unique identifier for an external resource, such as a DOI, ARK, or other identifier. If one of `type` or `value` is provided, the other must also be provided.
        type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
        value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
      relationship: __RELATIONSHIP__  # [interoperability_if_applicable] Relationship to other datasets or resources. This can include links to related datasets, publications, software, or other resources  that are relevant to understanding and using the dataset effectively. Allowed values: is_cited_by | cites | in_series | is_supplement_to | is_supplemented_by | is_continued_by | continues | describes | is_described_by | has_metadata | is_metadata_for | has_version | is_version_of | is_previous_version_of | is_part_of | has_part | is_published_in | is_referenced_by | references | is_documented_by | documents | is_compiled_by | compiles | is_variant_form_of | is_original_form_of | is_identical_to | is_reviewed_by | reviews | is_derived_from | is_source_of | is_required_by | requires | obsoletes | is_obsoleted_by | is_collected_by | collects | is_translation_of | has_translation | other | generates | is_generated_by | processes | is_processed_by | analyzes | is_analyzed_by | is_trained_on | is_used_for_training | is_evaluated_on | is_used_for_evaluation | tested_on | validated_on | fine_tuned_from | has_evaluation
    publications:  # [interoperability_if_applicable] Publications associated with this dataset, if any.  This can include links to scholarly articles, conference papers, or other publications that describe the dataset or its use,  which can provide users with additional context and insights about the dataset.
    - value: ${VALUE}  # The value of the identifier, following the format specified by the 'type' field.
      type: ${TYPE}  # [if_applicable] The type of the Identifier. Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
      relationship: ${RELATIONSHIP}  # [interoperability_if_applicable] Relationship to other datasets or resources. This can include links to related datasets, publications, software, or other resources  that are relevant to understanding and using the dataset effectively. Allowed values: is_cited_by | cites | in_series | is_supplement_to | is_supplemented_by | is_continued_by | continues | describes | is_described_by | has_metadata | is_metadata_for | has_version | is_version_of | is_previous_version_of | is_part_of | has_part | is_published_in | is_referenced_by | references | is_documented_by | documents | is_compiled_by | compiles | is_variant_form_of | is_original_form_of | is_identical_to | is_reviewed_by | reviews | is_derived_from | is_source_of | is_required_by | requires | obsoletes | is_obsoleted_by | is_collected_by | collects | is_translation_of | has_translation | other | generates | is_generated_by | processes | is_processed_by | analyzes | is_analyzed_by | is_trained_on | is_used_for_training | is_evaluated_on | is_used_for_evaluation | tested_on | validated_on | fine_tuned_from | has_evaluation
    software:  # [if_applicable] Software associated with this dataset, if any.  This can include links to software tools, libraries, or frameworks that were used to generate, process, or analyze the dataset,  which can provide users with additional context and insights about the dataset.
    - name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
      version: __VERSION__  # [if_applicable, recommended] Replace default with the version of the software tool, if applicable.
      identifier:  # [interoperability_if_applicable] Unique identifier for an external resource, such as a DOI, ARK, or other identifier. If one of `type` or `value` is provided, the other must also be provided.
        type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
        value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
      role: []  # [situational_required] The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
      relationship: ${RELATIONSHIP}  # [situational_required] The relationship of this software to the datacard or dataset. Allowed values: is_cited_by | cites | in_series | is_supplement_to | is_supplemented_by | is_continued_by | continues | describes | is_described_by | has_metadata | is_metadata_for | has_version | is_version_of | is_previous_version_of | is_part_of | has_part | is_published_in | is_referenced_by | references | is_documented_by | documents | is_compiled_by | compiles | is_variant_form_of | is_original_form_of | is_identical_to | is_reviewed_by | reviews | is_derived_from | is_source_of | is_required_by | requires | obsoletes | is_obsoleted_by | is_collected_by | collects | is_translation_of | has_translation | other | generates | is_generated_by | processes | is_processed_by | analyzes | is_analyzed_by | is_trained_on | is_used_for_training | is_evaluated_on | is_used_for_evaluation | tested_on | validated_on | fine_tuned_from | has_evaluation
    ai_models:  # [interoperability_if_applicable] AI models associated with this dataset, if any.  This can include links to AI models that were trained on, evaluated using, or otherwise related to the dataset,  which can provide users with additional context and insights about the dataset.
    - name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
      version: __VERSION__  # [if_applicable, recommended] Replace default with the version of the AI model, if applicable.
      accessed_date: ${ACCESSED_DATE}  # [situational_required] The ISO 8601 date when the AI model was accessed for use in creating or updating the datacard.
      identifier:  # [interoperability_if_applicable] Unique identifier for an external resource, such as a DOI, ARK, or other identifier. If one of `type` or `value` is provided, the other must also be provided.
        type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
        value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
      role: []  # The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
      relationship: ${RELATIONSHIP}  # [situational_required] The relationship of this AI model to the datacard or dataset Allowed values: is_cited_by | cites | in_series | is_supplement_to | is_supplemented_by | is_continued_by | continues | describes | is_described_by | has_metadata | is_metadata_for | has_version | is_version_of | is_previous_version_of | is_part_of | has_part | is_published_in | is_referenced_by | references | is_documented_by | documents | is_compiled_by | compiles | is_variant_form_of | is_original_form_of | is_identical_to | is_reviewed_by | reviews | is_derived_from | is_source_of | is_required_by | requires | obsoletes | is_obsoleted_by | is_collected_by | collects | is_translation_of | has_translation | other | generates | is_generated_by | processes | is_processed_by | analyzes | is_analyzed_by | is_trained_on | is_used_for_training | is_evaluated_on | is_used_for_evaluation | tested_on | validated_on | fine_tuned_from | has_evaluation
  domain_metadata:  # [interoperability_if_applicable] Captures domain-specific metadata that may be relevant for understanding and using the dataset effectively. This can include fields that are specific to certain scientific domains or types of data,  which can provide users with important context and insights about the dataset. Domain-specific metadata fields supplement the supports_discoverability card and should not replace the common metadata expected by the datacard.
    name: ${NAME}  # Human-readable name or local string key for the entity.
    description: __DESCRIPTION__  # [if_applicable] Detailed description of the entity.
    science_domain: []  # [discoverability_if_applicable] Based on OSTI Subject Areas, scientific domains or disciplines this dataset primarily relates to. Extends the the list of OSTI Subject Areas with an Other category for datasets that do not fit into the OSTI list. Those using E-Link can map to their own taxonomy. Allowed values: Biology and Medicine | Chemistry | Energy Storage, Conversion, and Utilization | Engineering | Environmental Sciences | Fission and Nuclear Technologies | Fossil Fuels | Geosciences | Materials | Mathematics and Computing | National Defense | Physics | Power Generation and Distribution | Renewable Energy | Other
    schema_reference:  # [interoperability_if_applicable] Reference to a schema or controlled vocabulary that defines the domain-specific metadata fields used in the domain_metadata block. This can provide users with information about the structure and semantics of the domain-specific metadata,  which can inform their understanding of the dataset and how to work with the domain-specific metadata.
      type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
      value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
      version: __VERSION__  # Version of software, tool, or library.
    fields:  # Field names, their corresponding values, data types, units, and descriptions for domain-specific metadata.
    - name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
      field_value: ${FIELD_VALUE}  # [situational_required] The value for a specific domain metadata field.
      data_type: __DATA_TYPE__  # [situational_required] The data type of a feature or variable, following a controlled vocabulary from  (e.g., float, int, string, boolean, datetime, other). This can provide important information about the nature of the data and can inform users about how to interpret and work with the dataset.
      unit: __UNIT__  # [situational_required] The unit of measurement for a feature. This can provide important context for interpreting the values of the feature.
      description: __DESCRIPTION__  # [if_applicable] A detailed description of the domain-specific metadata field.
reusability:  # [reusability_required] ###---Reusability---### Metadata fields that support the reusability of the dataset, and enables users to reuse the dataset for the same or different purposes. These fields provide critical information about the authorship, license, stewardship, and data quality of the dataset. The reusability capability is required for datacards of datasets that are intended to be reusable.
  license:  # [reusability_if_applicable] Block to capture a license under which the dataset is released. This indicates the legal permissions and restrictions associated with using the dataset and can inform users about how they are allowed to use, share, and build upon the data. A public/open license is not always the governing instrument for use, some controlled datasets may not have an SPDX-style reuse license at all, and use may instead be governed by contract, agreement, institutional review, or repository policy.
    spdx_id: __SPDX_ID__  # [reusability_if_applicable] The SPDX license identifier for the dataset, use the SPDX license identifier: https://spdx.org/licenses/ Use "Other" if not in SPDX registry.  Use "Pending" if not yet assigned. This provides a standardized way to indicate the license for the dataset and can inform users about the legal permissions and restrictions associated with using the data. e.g., CC-BY-4.0 | CC0-1.0 | Apache-2.0 | MIT | Other | Pending
    name: __NAME__  # [reusability_if_applicable] The human-readable name of the license.
    url: __URL__  # [reusability_if_applicable] URL to a license. This can provide users with direct access to the full terms and conditions,  which can inform their understanding of legal and ethical requirements.
    known_contractual_rights: __KNOWN_CONTRACTUAL_RIGHTS__  # [reusability_if_applicable] Any known contractual rights or obligations associated with this dataset  that may not be fully captured by the license or access policy information. This can include information about data sharing agreements,  third-party restrictions, or other legal considerations that users should be  aware of when working with the dataset. DOE/NNSA datasets may have complex contractual arrangements that  impact how the data can be used and shared beyond license terms. e.g., Government has unlimited rights | Contractor retains rights with government license
  additional_licenses:  # [reusability_if_applicable] Additional licenses governing this dataset, if multiple licenses apply. This can provide users with a more complete understanding of the legal permissions  and restrictions associated with using the dataset,  especially in cases where different parts of the dataset may be subject to different licenses.
  - spdx_id: __SPDX_ID__  # [reusability_if_applicable] The SPDX license identifier for the dataset, use the SPDX license identifier: https://spdx.org/licenses/ Use "Other" if not in SPDX registry.  Use "Pending" if not yet assigned. This provides a standardized way to indicate the license for the dataset and can inform users about the legal permissions and restrictions associated with using the data. e.g., CC-BY-4.0 | CC0-1.0 | Apache-2.0 | MIT | Other | Pending
    name: __NAME__  # [reusability_if_applicable] The human-readable name of the license.
    url: __URL__  # [reusability_if_applicable] URL to a license. This can provide users with direct access to the full terms and conditions,  which can inform their understanding of legal and ethical requirements.
    known_contractual_rights: __KNOWN_CONTRACTUAL_RIGHTS__  # [reusability_if_applicable] Any known contractual rights or obligations associated with this dataset  that may not be fully captured by the license or access policy information. This can include information about data sharing agreements,  third-party restrictions, or other legal considerations that users should be  aware of when working with the dataset. DOE/NNSA datasets may have complex contractual arrangements that  impact how the data can be used and shared beyond license terms. e.g., Government has unlimited rights | Contractor retains rights with government license
  stewardship:  # [reusability_if_applicable] Stewardship & Versioning metadata to capture information about dataset maintenance, updates, versioning, and reviews. This can provide users with important information about how the dataset is maintained and updated over time. NOTE ON VERSIONING: Three fields work together to describe versioning: discoverability.identification.version — the version number of this dataset; discoverability.identification.supersedes / discoverability.identification.superseded_by  — links to prior and successor versions; reusability.stewardship.versioning_strategy — how versioning is managed over time.
    level: __LEVEL__  # [reusability_if_applicable] The stewardship level of the dataset from a controlled vocabulary, StewardshipLevelEnum, indicating the management level of stewardship. Allowed values: Project_Managed | Repository_Managed | Externally_Managed | not_applicable
    maintainer:  # [reusability_if_applicable] Person or organization responsible for ongoing maintenance of the dataset over time, if different from the contact. This can provide users with a point of contact for ongoing maintenance and updates to the dataset,  which can facilitate communication and support responsible use of the data.
      person:  # [if_applicable] A human individual.
        given_name: ${GIVEN_NAME}  # [situational_required] The given name(s) of a person.
        family_name: ${FAMILY_NAME}  # [situational_required] The family name(s) of a person.
        orcid: __ORCID__  # [if_applicable, recommended] The ORCID identifier for a person, in URL format. e.g., https://orcid.org/0000-0002-5755-8449
        email: __EMAIL__  # [if_applicable] The email address of a person.
        affiliation:  # [if_applicable, recommended] An organization with which a person is affiliated.
          name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
          ror_id: __ROR_ID__  # [if_applicable, recommended] The ROR identifier for an organization, in URL format. e.g., https://ror.org/02vwzrd76
        role: []  # [situational_required] The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
      organization:  # [if_applicable] An organization or group of individuals.
        name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
        ror_id: __ROR_ID__  # [if_applicable, recommended] The ROR identifier for an organization, in URL format. e.g., https://ror.org/02vwzrd76
        role: []  # The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
    update_frequency: __UPDATE_FREQUENCY__  # [reusability_if_applicable] How often the dataset is updated or expected to be updated, if applicable. Allowed values: None | Ad_Hoc | Monthly | Quarterly | Annually | Continuously | Other
    retention_policy: __RETENTION_POLICY__  # [reusability_if_applicable] Information about the dataset's retention policy, including how long the dataset will be retained  and any conditions for its removal or archiving. Provides users with important information about the longevity of the dataset  and can inform their decisions about using and citing the data. e.g., Retained for 10 years per DOE data management policy
    versioning_strategy: __VERSIONING_STRATEGY__  # [reusability_if_applicable] The strategy for managing dataset versions over time, such as semantic versioning, date-based versioning, or custom versioning schemes. e.g., New version created for each major update; minor updates appended to existing version with date suffix | Semantic versioning; all versions retained in Zenodo | Major versions only; prior versions available on request
  data_quality:  # [reusability_required] Provides information about the quality of the dataset, including any known issues, limitations, or uncertainties that may affect its suitability for AI/ML applications.
    completeness: ${COMPLETENESS}  # [reusability_required] Information about the completeness of the dataset, including any known gaps, missing values,  or limitations in the data that may affect its suitability for use. e.g., All detector channels present; 2% of timesteps missing | Missing due to sensor downtime for 5% of samples | Dataset is complete with no known gaps or missing values | not_applicable
    known_issues: ${KNOWN_ISSUES}  # [reusability_required] Any known issues or limitations with the dataset that may affect its suitability for use. Be explicit if there are no known issues or limitations (e.g., "not_applicable") rather than leaving this field blank. e.g., Sensor drift observed after 2023-06-01T12:00:00Z | Sensor calibration drift affects accuracy of measurements after June 2023 | Data from Facility X may have quality issues due to known equipment problems during the data collection period | not_applicable
    validation_methods: ${VALIDATION_METHODS}  # [reusability_required] Information about any validation methods or processes that have been applied to the dataset to assess its quality and suitability for use. Be explicit if there are no validation methods or processes (e.g., "not_applicable") rather than leaving this field blank. e.g., Cross-validated against NIST SRM 640f | Dataset validated against ground truth measurements from Facility Y | Data quality assessed using method Z with the following results: ... | not_applicable
    noise_characteristics: __NOISE_CHARACTERISTICS__  # [reusability_if_applicable] Information about the noise characteristics of the dataset. Be explicit if there are no known noise issues or characteristics (e.g., "not_applicable")  rather than leaving this field blank. e.g., Signal-to-noise ratio (SNR) of 20 dB across all channels | Noise level increases by 5% after June 2023 due to equipment degradation | Dataset has low noise levels with no known issues | not_applicable
    uncertainty_notes: __UNCERTAINTY_NOTES__  # [reusability_if_applicable] Any known uncertainties or limitations in the dataset that may affect its suitability for use. Be explicit if there are no known uncertainties or limitations (e.g., "not_applicable")  rather than leaving this field blank. e.g., Measurement uncertainty ±0.5% (k=2) per ISO/IEC Guide 98-3 | Uncertainty increases to ±10% for measurements taken after June 2023 due to equipment degradation | Dataset has low uncertainty with no known issues | not_applicable
    missing_data_codes:  # [reusability_if_applicable] If the dataset contains missing values, list the missing codes and their meanings.  This can provide users with important information about how missing data is represented in the dataset,  which can inform their decisions about how to handle missing values when used.
    - code: ${CODE}  # [situational_required] The code used in the dataset to indicate a missing or null value. e.g., -9999 | NULL
      description: ${DESCRIPTION}  # [situational_required] A description of what the missing data code represents.
  citation:  # [situational_required] Citation information for the dataset, if applicable. Required when release_status = Approved | Published. This can provide users with the necessary information to properly cite  the dataset in their work.
    report_number: __REPORT_NUMBER__  # [reusability_if_applicable] Report number or other unique identifier for the dataset. This can provide users with an additional identifier for the dataset that can be used  in citations and references. e.g., SAND2024-XXXXX | LAUR-XX-XXXXX | ORNL/TM-2024/XXXXX
    preferred_citation:  # [reusability_if_applicable] Fields that can be used to create full, preferred/recommended citation in bibtex format for the dataset. The fields author, title, year, publisher are required if preferred_citation is provided. At least one of doi or url must be provided if preferred_citation is provided.
      author: ${AUTHOR}  # [situational_required] Author(s) of the dataset, if applicable.  author: is intended as a component of a bibtex citation when preferred_citation is provided. Required when a preferred_citation is provided.
      title: ${TITLE}  # [situational_required] Title of the dataset, if applicable. title: is intended as a component of a bibtex citation when preferred_citation is provided. Required when a preferred_citation is provided.
      year: ${YEAR}  # [situational_required] Year of publication or release of the dataset, if applicable. year: is intended as a component of a bibtex citation when preferred_citation is provided Required when a preferred_citation is provided. This can provide users with temporal context for the dataset, which can inform their understanding of its relevance and currency.
      publisher: __PUBLISHER__  # [reusability_if_applicable] Publisher or distributing organization for the dataset. publisher: is intended as a component of a bibtex citation when preferred_citation is provided This can provide users with information about the organization responsible for distributing the dataset.
      howpublished: __HOWPUBLISHED__  # [situational_required] How the dataset was published or released. how_published: is intended as a component of a bibtex citation when preferred_citation is provided e.g., Online | In Repository | As Supplementary Material
      doi: __DOI__  # [reusability_if_applicable] Digital Object Identifier (DOI) for the dataset. doi: is intended as a component of a bibtex citation when preferred_citation is provided Required when a preferred_citation is provided. This can provide users with a persistent identifier for the dataset that can be used in citations and references.
      url: __URL__  # [reusability_if_applicable] A url that resolves to the dataset landing page or other primary reference for the dataset, which can be used in citations and for users to access the dataset. url: is intended to correspond to the bibtex url field, and should be populated with the same value.
      eprinttype: __EPRINTTYPE__  # [reusability_if_applicable] The type of eprint identifier provided in the url field. eprinttype: is intended as a component of a bibtex citation when preferred_citation is provided. e.g., arXiv | report_number | pubmed
      eprint: __EPRINT__  # [reusability_if_applicable] The eprint identifier for the dataset. Value with correspond to the format of the eprinttype provided (e.g., arXiv, report_number, pubmed). eprint: is intended as a component of a bibtex citation when preferred_citation is provided. e.g., 1234.56789 | SAND2024-XXXXX
      note: __NOTE__  # [reusability_if_applicable] Additional notes related to the preferred citation, if any. Is intended to align with bibtex "note" field when preferred_citation is provided. For legacy bibtex entries that don't accept eprinttype and eprint and that need to support an ark or other identifiers that don't fit cleanly into the existing fields, the note field can be used to capture this information in a free-text format. include a note: field use this format for the note field: note: Available at ark:/12345/abcde
  integrity:  # [reusability_required] Contains elements describing checksums enable automated validation of data integrity after transfer or storage.
    checksum_available: __"Yes|No"__  # [reusability_if_applicable] Whether a checksum is available for this dataset,  which can be used to verify the integrity of the data after transfer or storage.
    checksum_type: __CHECKSUM_TYPE__  # [situational_required] The type of checksum available for this dataset. Required if checksum_available="Yes". This can provide users with information about the method used to generate the checksum,  which can inform their decisions about how to use the checksum for data integrity verification.
    checksum_value: __CHECKSUM_VALUE__  # [situational_required] The value of the checksum for this dataset, if applicable. Required if checksum_available="Yes". This can be used by users to verify the integrity of the data after  transfer or storage by comparing the provided checksum value with a newly  generated checksum from the transferred or stored data.
    fixity_policy: __FIXITY_POLICY__  # [reusability_if_applicable] Information about the fixity policy for this dataset,  including how often fixity checks are performed and any specific procedures  or tools used for fixity verification. e.g., Monthly sha256 verification via repository integrity service
governed_use:  # [governed_use_required] ###---Governed Use---### Metadata fields that support the governed use of the dataset, which is essential for ensuring that the dataset is shared and accessed in compliance with applicable regulations, policies, and ethical considerations, and for enabling responsible use of the dataset by others. The governed_use capability is required for datacards of datasets that are intended to be shared or accessed  under specific governance or oversight, such as datasets that are subject to security controls,  export control, or other types of formal review and approval processes.
  use_governance:  # [governed_use_required] Information block to guide appropriate use and prevent misuse of this dataset.
    current_use: ${CURRENT_USE}  # [governed_use_required] What is this dataset actively being used for right now? Distinct from intended_use.
    intended_use: __INTENDED_USE__  # [governed_use_if_applicable, recommended] Purpose and intended use stated to enable users to make a decision as to the suitability of this work  (e.g., lab protocol, machine learning model, software) to their experimental problem or own use case. e.g., ML training | physics analysis | benchmarking | visualization
    permitted_use: __PERMITTED_USE__  # [governed_use_if_applicable, recommended] Uses this dataset is suitable for, beyond the intended use. Genesis governance expects explicit permitted use metadata at the governance level, which is why this field is distinct from intended_use. Be explicit about what this dataset is suitable for, to guide users and prevent misuse. e.g., AI workflows | research and publication | internal analysis | educational use
    out_of_scope_use: __OUT_OF_SCOPE_USE__  # [governed_use_if_applicable, recommended] Uses this dataset should NOT be applied to. e.g., clinical decision-making | real-time control systems
    prohibited_use: __PROHIBITED_USE__  # [governed_use_if_applicable, recommended] Uses that are explicitly prohibited for this dataset, either due to ethical considerations, safety concerns, or other governance reasons. Be explicit about what this dataset should not be used for, to guide users and prevent misuse. e.g., commercial use | AI workflows | redistribution | use by foreign nationals | clinical decision-making | real-time control systems
  non_sensitivity_governance_metadata:  # [governed_use_required] Governance-relevant metadata that may affect  sharing/use decisions but is not part of the source sensitivity/marking block itself. This refers to the non-sensitivity governance as it applies to the dataset,  which may be distinct from the sensitivity or classification of the source data from which it was derived.
    export_control:  # [governed_use_required] Includes fields related to export control considerations for the dataset, if applicable. Provides users with important information about any export control restrictions or requirements that may apply to the dataset.
      export_control_status: ${EXPORT_CONTROL_STATUS}  # [governed_use_required] The export control status of the dataset. Allowed values: "Yes" | "No" | Pending_Review | Unknown
      export_control_basis: __EXPORT_CONTROL_BASIS__  # [situational_required] The basis for the export control status. Required is `export_control_status` = "Yes". Allowed values: ITAR | EAR | DOE_Nuclear_Export_Control | Other | not_applicable
      foreign_national_access_status: __FOREIGN_NATIONAL_ACCESS_STATUS__  # [governed_use_if_applicable] Governance-facing outcome field indicating whether foreign national access is allowed, restricted, prohibited, or conditional, based on the combined effect of applicable export, classification, dissemination, agreement, or other source-authoritative constraints. This is not an export-only field. Allowed values: Allowed | Restricted | Prohibited | Conditional | Unknown
    privacy:  # [governed_use_required] Includes fields related to privacy considerations for the dataset. Provides users with important information about any privacy restrictions or requirements that may apply to the dataset.
      privacy_status: ${PRIVACY_STATUS}  # [governed_use_required] The privacy status of the dataset. Allowed values: "Yes" | "No" | Pending_Review | Unknown
      pii_status: ${PII_STATUS}  # [governed_use_required] Whether the dataset contains personally identifiable information (PII).   Allowed values: "Yes" | "No" | Pending_Review | Unknown
      phi_status: __PHI_STATUS__  # [governed_use_if_applicable] Whether the dataset contains protected health information (PHI). Use quotes to distinguish from boolean values. Allowed values: "Yes" | "No" | Pending_Review | Unknown
      privacy_control_basis: []  # [governed_use_if_applicable] The basis for the privacy status.  Be explicit about the privacy regime(s) - e.g. use "not_applicable" if no privacy regime applies. Allowed values: HIPAA | Privacy_Act | Human_Subjects | Other_Regulated_Privacy | Site_Specific | not_applicable
      privacy_regime_notes: __PRIVACY_REGIME_NOTES__  # [governed_use_if_applicable] Optional notes for privacy regimes or handling nuances not captured by controlled values. Provides users with important context about the privacy considerations and requirements that may apply to the dataset.
    rights_release_records:  # [governed_use_required] Information about rights release records for the dataset. Provides users with important information about any rights or permissions associated with the dataset.
      ip_restriction_type: __IP_RESTRICTION_TYPE__  # [governed_use_if_applicable] The type of intellectual property (IP) restriction that applies to the dataset, if any.  Allowed values: Proprietary | Limited_Rights | Restricted_Rights | Government_Purpose_Rights | Unlimited_Rights | Third_Party_Licensed | None
      agreement_required: ${"Yes|No"}  # [governed_use_required] Whether an agreement (e.g., data use agreement, license agreement, nondisclosure agreement) is required to access or use the dataset.
      agreement_type: []  # [situational_required] The type of agreement required to access or use the dataset. Required is `agreement_required` = "Yes". Allowed values: DUA | CRADA | MOU | NDA | LICENSE | WFO | OTHER
      public_release_status: ${PUBLIC_RELEASE_STATUS}  # [governed_use_required] The public release status of the dataset. Allowed values: Approved | Pending | Not_Approved | Requires_STI_Review
      record_status: ${RECORD_STATUS}  # [governed_use_required] The record status of the dataset. Allowed values: Federal_Record | Contractor_Record | Non_Record | Mixed | Unknown
  compliance:  # [governed_use_required] Populate when release_status = Under_Review | Approved | Published. Include with `Unknown` values for Draft datasets  Acts as a holder for confirmation of compliance with relevant policies,  standards, and requirements for the dataset.
    doe_data_management_plan: ${DOE_DATA_MANAGEMENT_PLAN}  # [governed_use_required] Whether the dataset is in compliance with a DOE Data Management Plan (DMP). Allowed values: "Yes" | "No" | Unknown | not_applicable
    osti_elink2_metadata_compliant: ${OSTI_ELINK2_METADATA_COMPLIANT}  # [governed_use_required] Whether the dataset is compliant with OSTI's E-Link 2.0 metadata requirements. Allowed values: "Yes" | "No" | Unknown | not_applicable
    irb_approved: ${IRB_APPROVED}  # [governed_use_required] Whether the dataset has been approved by an Institutional Review Board (IRB). Allowed values: "Yes" | "No" | Unknown | not_applicable
  review_provenance_companion:  # [governed_use_if_applicable, recommended] Reviews or assessments of the dataset, if any. Running history of all formal reviews. Add one entry per review stage in chronological order. Do not overwrite earlier entries when adding new ones. This block extends the Genesis Sensitivity V2 review_provenance_companion (which only accepts a single review) by allowing multiple review records to be captured in a structured format,  which is especially useful for datasets that have undergone multiple reviews or have complex provenance histories. Provides users with insights into the quality and reliability of the dataset.
  - source_review_reference: __SOURCE_REVIEW_REFERENCE__  # [governed_use_if_applicable, recommended] Identifier or citation for the authoritative review/release/source document. e.g., internal_qa | security | export_control | irb | quality_assessment | partner | publication | other
    review_purpose: __REVIEW_PURPOSE__  # [governed_use_if_applicable, recommended] The purpose or focus of the review, such as export control, IRB, security, quality assessment, or other.       Provides users with important context about the nature of the review and what aspects of the dataset were evaluated,  which can inform their understanding of the dataset's quality and reliability. e.g., Export control review prior to public release | Institutional Review Board (IRB) review for human subjects research | Internal security review for sensitive data handling | Quality assessment review for data integrity and accuracy
    source_review_authority: __SOURCE_REVIEW_AUTHORITY__  # [governed_use_if_applicable] Office, system, or authority of record for the source sensitivity determination. Provides users with information about the official authority responsible for the review,  which can inform their confidence in the dataset's quality and reliability. e.g., DOE Office of Export Control | Institutional Review Board at XYZ University | Internal security review board
    review_contact_name: __REVIEW_CONTACT_NAME__  # [governed_use_if_applicable] Human point of contact, if appropriate to capture. This can provide users with a point of contact for questions about the review process and its outcomes,  which can facilitate communication and support responsible use of the data.
    review_contact_email: __REVIEW_CONTACT_EMAIL__  # [governed_use_if_applicable] Contact email, if appropriate to capture. Provides users with a point of contact for questions about the review process and its outcomes,  which can facilitate communication and support responsible use of the data.
    reviewed_by:  # [governed_use_if_applicable] Person or role responsible for conducting the review, if applicable. Provides users with information about the expertise and credibility of the reviewers,  which can inform their confidence in the dataset's quality and reliability.
      person:  # [if_applicable] A human individual.
        given_name: ${GIVEN_NAME}  # [situational_required] The given name(s) of a person.
        family_name: ${FAMILY_NAME}  # [situational_required] The family name(s) of a person.
        orcid: __ORCID__  # [if_applicable, recommended] The ORCID identifier for a person, in URL format. e.g., https://orcid.org/0000-0002-5755-8449
        email: __EMAIL__  # [if_applicable] The email address of a person.
        affiliation:  # [if_applicable, recommended] An organization with which a person is affiliated.
          name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
          ror_id: __ROR_ID__  # [if_applicable, recommended] The ROR identifier for an organization, in URL format. e.g., https://ror.org/02vwzrd76
        role: []  # [situational_required] The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
      organization:  # [if_applicable] An organization or group of individuals.
        name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
        ror_id: __ROR_ID__  # [if_applicable, recommended] The ROR identifier for an organization, in URL format. e.g., https://ror.org/02vwzrd76
        role: []  # The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
      ai_model:  # [if_applicable] An AI model.
        name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
        version: __VERSION__  # [if_applicable, recommended] Replace default with the version of the AI model, if applicable.
        accessed_date: ${ACCESSED_DATE}  # [situational_required] The ISO 8601 date when the AI model was accessed for use in creating or updating the datacard.
        identifier:  # [interoperability_if_applicable] Unique identifier for an external resource, such as a DOI, ARK, or other identifier. If one of `type` or `value` is provided, the other must also be provided.
          type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
          value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
        role: []  # The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
        relationship: ${RELATIONSHIP}  # [situational_required] The relationship of this AI model to the datacard or dataset Allowed values: is_cited_by | cites | in_series | is_supplement_to | is_supplemented_by | is_continued_by | continues | describes | is_described_by | has_metadata | is_metadata_for | has_version | is_version_of | is_previous_version_of | is_part_of | has_part | is_published_in | is_referenced_by | references | is_documented_by | documents | is_compiled_by | compiles | is_variant_form_of | is_original_form_of | is_identical_to | is_reviewed_by | reviews | is_derived_from | is_source_of | is_required_by | requires | obsoletes | is_obsoleted_by | is_collected_by | collects | is_translation_of | has_translation | other | generates | is_generated_by | processes | is_processed_by | analyzes | is_analyzed_by | is_trained_on | is_used_for_training | is_evaluated_on | is_used_for_evaluation | tested_on | validated_on | fine_tuned_from | has_evaluation
      software:  # [if_applicable] Software associated with this dataset, if any.  This can include links to software tools, libraries, or frameworks that were used to generate, process, or analyze the dataset,  which can provide users with additional context and insights about the dataset.
        name: ${NAME}  # [situational_required] Human-readable name or local string key for the entity.
        version: __VERSION__  # [if_applicable, recommended] Replace default with the version of the software tool, if applicable.
        identifier:  # [interoperability_if_applicable] Unique identifier for an external resource, such as a DOI, ARK, or other identifier. If one of `type` or `value` is provided, the other must also be provided.
          type: __TYPE__  # [if_applicable, recommended] The type of the identifier (e.g., DOI, UUID). Allowed values: ark | doi | handle | local | purl | url | urn | uuid | other | unregistered
          value: __VALUE__  # [if_applicable, recommended] The value of the identifier, following the format specified by the 'type' field.
        role: []  # [situational_required] The function of an entity or agent with respect to another entity or resource. Allowed values: Conceptualization | Contact_Person | Contributor | Creator | Data_Curator | Data_Manager | Distributor | Editor | Formal_Analysis | Funding_Acquisition | Hosting_Institution | Investigation | Methodology | Producer | Project_Administration | Project_Leader | Project_Manager | Project_Member | Publisher | Registration_Agency | Registration_Authority | Related_Person | Researcher | Research_Group | Resources | Rights_Holder | Software | Sponsor | Supervision | Translator | Validation | Visualization | Work_Package_Leader | Writing_Original_Draft | Writing_Review_Editing | Other
        relationship: ${RELATIONSHIP}  # [situational_required] The relationship of this software to the datacard or dataset. Allowed values: is_cited_by | cites | in_series | is_supplement_to | is_supplemented_by | is_continued_by | continues | describes | is_described_by | has_metadata | is_metadata_for | has_version | is_version_of | is_previous_version_of | is_part_of | has_part | is_published_in | is_referenced_by | references | is_documented_by | documents | is_compiled_by | compiles | is_variant_form_of | is_original_form_of | is_identical_to | is_reviewed_by | reviews | is_derived_from | is_source_of | is_required_by | requires | obsoletes | is_obsoleted_by | is_collected_by | collects | is_translation_of | has_translation | other | generates | is_generated_by | processes | is_processed_by | analyzes | is_analyzed_by | is_trained_on | is_used_for_training | is_evaluated_on | is_used_for_evaluation | tested_on | validated_on | fine_tuned_from | has_evaluation
    decontrol_or_declassify_on: __DECONTROL_OR_DECLASSIFY_ON__  # [governed_use_if_applicable] For sensitive datasets, the date when the dataset can be decontrolled or declassified, if applicable. Provides users with information about when the dataset may become more widely available and can inform their decisions about using and citing the data.
    review_date: __REVIEW_DATE__  # [governed_use_if_applicable] The date when the review was conducted or completed, in ISO 8601 format (YYYY-MM-DD).
    comments: __COMMENTS__  # [governed_use_if_applicable, recommended] Additional comments or notes about the review, if any. Provides insights about the review process and its outcomes.
ai_usability:  # [ai_usability_required] ###---AI Usability---### Metadata fields that support the AI usability of the dataset, These fields provide critical information about the allowed ai use for AI purposes, as well as  any restrictions, biases, risks, safety considerations, and other factors related to using the dataset  for AI purposes. The ai_usability capability is required for datacards of datasets  that are intended to be used for AI training, evaluation, or other AI-related purposes.
  ai_usage:  # [ai_usability_required] Describes whether and how this dataset may be used in AI/ML workflows. Be explicit — these fields are read by automated pipeline tooling. This can provide important information about the suitability of the dataset for  AI/ML applications and can inform users about any specific considerations or  restrictions related to using the dataset in AI/ML workflows. 
    training_use_status: ${TRAINING_USE_STATUS}  # [ai_usability_required] The status of whether this dataset can be used for training in AI/ML workflows. Allowed values: "Yes" | "No" | Conditional
    training_use_conditions: __TRAINING_USE_CONDITIONS__  # [situational_required] If training_use_status is "Conditional", this field is required and  describes the specific conditions or restrictions that must be met for the dataset to be used for training AI models. This can provide users with important information about any limitations or considerations  they should be aware of when using the dataset for training AI models.
    inference_use_status: ${INFERENCE_USE_STATUS}  # [ai_usability_required] The status of whether this dataset can be used for inference in AI/ML workflows. Allowed values: "Yes" | "No" | Conditional
    inference_use_conditions: __INFERENCE_USE_CONDITIONS__  # [situational_required] If inference_use_status is "Conditional", this field is required and describes the specific conditions or restrictions that must be met for the dataset to be used for inference with AI models. This can provide users with important information about any limitations or considerations they should be aware of when using the dataset for inference with AI models.
    evaluation_use_status: ${EVALUATION_USE_STATUS}  # [ai_usability_required] The status of whether this dataset can be used for evaluation in AI/ML workflows. Allowed values: "Yes" | "No" | Conditional
    evaluation_use_conditions: __EVALUATION_USE_CONDITIONS__  # [situational_required] If evaluation_use_status is "Conditional", this field is required and describes the specific conditions or restrictions that must be met for the dataset to be used for evaluation of AI models. This can provide users with important information about any limitations or considerations they should be aware of when using the dataset for evaluation of AI models.
    restrictions: ${RESTRICTIONS}  # [ai_usability_required] Any specific restrictions or conditions related to using this dataset in AI/ML workflows, if applicable. Be explicit if there are no applicable restrictions (e.g., "not_applicable") rather than leaving this field blank. This can provide users with important information about any limitations or considerations they should be aware of when using the dataset in AI/ML applications. e.g., Not for clinical decision-making | Dataset is intended for research purposes only and should not be used for commercial applications. | Dataset is subject to data use agreement restrictions that limit its use to non-commercial research purposes. | not_applicable
    bias_risks: ${BIAS_RISKS}  # [ai_usability_required] Any known or potential bias risks associated with using this dataset in AI/ML workflows. Be explicit if there are no known or potential bias risks (e.g., "not_applicable") rather than leaving this field blank. e.g., Dataset is predominantly from one demographic group, which may introduce bias in AI models trained on this data. | Overrepresents samples from facility X, which may lead to biased model performance. | not_applicable
    safety_considerations: ${SAFETY_CONSIDERATIONS}  # [ai_usability_required] Any known or potential safety considerations associated with using this dataset in AI/ML workflows. Be explicit if there are no known or potential safety considerations (e.g., "not_applicable") rather than leaving this field blank. e.g., Contains personally identifiable information (PII) that could pose privacy risks if not handled properly. | Dataset includes sensitive information that could be misused if not properly safeguarded. | not_applicable
    human_review_required: ${"Yes|No"}  # [ai_usability_required] Whether human review is recommended when using this dataset in AI/ML workflows,  based on factors such as data quality, completeness, relevance, and any known risks or considerations. This can provide users with guidance on whether they should incorporate human review  into their AI/ML workflows when working with this dataset,  which can help mitigate potential risks and ensure responsible use of the data.
---

### Instructions  
<INSTRUCTIONS: Provide relevant information regarding your dataset in this file.  The information can be a combination of values in YAML sections and text blocks in the markdown section.  For the markdown text, replace all Examples, and [!TODO], and REPLACE: ... placeholder tags with the appropriate information for your dataset. Be sure to remove the header TODO and INSTRUCTION tags once you have completed the data card.  In each section you can complete YAML values as available.  Required fields are marked.>  
  
<INSTRUCTIONS: Considerations for filling out the data card: Deciding the appropriate resolution for documenting a scientific dataset in a data card can be complex. Data cards may describe single or multiple data files, datasets, or versions. Too granular, and there will be too many data cards; too broad, and details may be lost. Consider the use, audience, and documentation the data card needs to provide to maintain transparency without duplication. Reflect on these relationships to balance clarity, usability, and sustainability.>
  
<INSTRUCTIONS: The sections and questions in the markdown section of this data card template are meant to be a guide for the types of information that should be included in a data card. You can choose to answer all, some, or additional questions as appropriate for your dataset. The goal is to provide enough information for users (humans and machines) to understand the dataset and its context, but you can use your judgment to determine what information is most relevant and important to include.>  
  
<INSTRUCTIONS: Structure of the Markdown Section: Data readiness in a shared environment can be generally sorted into six high-level categories:
* Discoverable: The dataset is described with sufficient metadata to be found and understood by potential users. This is the REQUIRED minimum for any dataset to be shared.
* Accessible: The dataset is available for access, with clear instructions and any necessary permissions or agreements in place.
* Interoperable: The dataset is in a format and structure that can be easily used and integrated with other datasets and tools, with clear documentation of its schema and semantics.
* Reusable: The dataset is of sufficient quality, with clear licensing and provenance information, to be confidently reused by others for various purposes.
* Governed Use: The dataset has defined use governance, compliance information, and review history to ensure responsible use and manage risks.
* AI Usable: The dataset is suitable for use in AI and ML workflows, with clear, explicit information about AI usage.
These categories describe usability, interoperability, and governance characteristics.  They do NOT represent dataset quality, scientific merit, or value ranking.  
Prompts for data are generally organized into sections that support these efforts.  Some fields are required to be considered for use at each level and for making datasets available to tools targeting each level.  Requirements are labelled for each level.  
>  
  
<INSTRUCTIONS: metadata_key: [KEY_NAME] tags indicate that the information for the markdown section can be found in the corresponding key in the YAML metadata at the top of this file, and is for use in the human and the automated bi-directional generation from YAML-to-markdown, or markdown-to-YAML. You can choose to manually copy, or you can leave the placeholders and use an automation tool (such as an LLM) to populate the sections. If you choose to automatically populate the markdown sections from the YAML metadata, make sure to replace metadata_key: [KEY_NAME] tags in each relevant markdown section before sharing the data card, and note the LLM or AI agent used in the data card.creation_method section of the YAML frontmatter metadata.>
  
  
# Datacard for ${DATASET_NAME}  

**Last Updated**: [!TODO]<REPLACE: YYYY-MM-DD>  

### Machine Usability Snapshot  
  
| Intended Capability | DataCard Support |  
| ------ | ------ |  
| Discoverability| Yes/No |
| Accessibility| Yes/No |
| Interoperability| Yes/No |  
| Reusability| Yes/No | 
| Governed Use | Yes/No |  
| AI Usability| Yes/No |  
| License Clarity | Yes/No | 
| Checksum / Fixity | Yes/No |  
| Semantic Context | Yes/No |
  
  
# ---- Discoverable ----  

## Description

### Dataset Description [discoverability_required]  
[!TODO] <REPLACE: Provide a concise description of the dataset, including its purpose, scope, and context.><metadata_key: discoverability.dataset_description.dataset_summary>

### Domain and Purpose [discoverability_if_applicable]
[!TODO] <REPLACE: Describe the domain and the key research areas involved in collecting the dataset. Can list below> <metadata_key: discoverability.dataset_description.purpose><metadata_key: discoverability.dataset_description.science_domain><metadata_key: interoperability.domain_metadata.science_domain>

## Keywords [discoverability_required]  
[!TODO] <REPLACE: Provide a comma-separated list of keywords that describe the dataset and can help with discoverability.><metadata_key: discoverability.dataset_description.keywords>

## Sensitivity [discoverability_required]

### Security / Marking Considerations [discoverability_required]
[!TODO]<Describe classification, CUI marking, distribution limitations, and handling requirements.>
<metadata_key: discoverability.sensitivity.overall_sensitivity><metadata_key: discoverability.sensitivity.classified_status><metadata_key: discoverability.sensitivity.cui_status><metadata_key: discoverability.sensitivity.ucni_status>

## Context and Provenance [discoverability_required]

### Resources used, including funding and facilities, to create the dataset  
[!TODO] <REPLACE: Provide a list of the resources used to create the dataset, including funding sources, facilities, computing resources, and any other relevant resources. Facilities can include user facilities, national laboratories, research institutions, and other organizations that provided access to equipment, data, or expertise. Funding sources can include government agencies, private foundations, industry partners, and other organizations that provided financial support for the dataset creation. Computing resources can include high-performance computing clusters, cloud computing platforms, and other computational resources used for data processing and analysis. Include [ROR ID](https://ror.org/), grant numbers, contract numbers, or other identifiers as appropriate. Can list below><metadata_key: discoverability.sponsor_organizations><metadata_key: discoverability.sponsoring_doe_program_office><metadata_key: discoverability.sponsoring_doe_subprogram><metadata_key: discoverability.research_organizations><metadata_key: discoverability.facilities>

### Developed by [discoverability_required]
[!TODO] <REPLACE: A person or group that was primarily responsible for the creation and design of the dataset. It suggests a leading role, such as a Principal Investigator, in the development of the dataset. If available, provide the Name, [ORCID](https://orcid.org/), affiliation ([ROR ID](https://ror.org/)) and email address of the person or group responsible for the dataset.><metadata_key: discoverability.authors>

### Contributed by  [discoverability_if_applicable]
[!TODO] <REPLACE: Person, or group that provided input or support to the datasets development but may not have been the primary creators. Contributions can include sample collection, processing, analysis, documentation, and-or submission of the dataset. This suggests collaboration, where multiple parties might have played various roles in the dataset development. Can list below> <metadata_key: discoverability.contributors>

## Methods  [discoverability_if_applicable]
  
### Dataset generation, collection, and procedures  [discoverability_if_applicable] [interoperability_required]
[!TODO] <REPLACE: Describe how the dataset was generated or collected. For example, raw experimental measurements from user facilities, processed, physics-ready experimental data, outputs from computational simulations, or data derived from prior datasets? For each instrument, facility, or source used to generate and collect the data, what mechanisms or procedures were used for the data collection? If the data was derived, list and describe the source(s) and describe how they were used.>  <metadata_key: discoverability.dataset_description.collection_methodology><metadata_key: interoperability.provenance.processing_steps><metadata_key: interoperability.provenance.instrumentation><metadata_key: interoperability.provenance.simulation_details>

---  

# ---- Accessible ----  

## Sharing & Access  [accessibility_required]
[!TODO] <REPLACE:  Describe the sharing methods and any contact information for access. If applicable, include a legal rights statement, separate from or in addition to the license.><metadata_key: accessibility.access><metadata_key: accessibility.access_policy>  

---  

# ---- Interoperable ----  

## Data Structure

### Files & Structure  [interoperability_required]
[!TODO] <REPLACE: Summarize dataset organization, formats, and relationships between files.><metadata_key: discoverability.dataset_description.data_characteristics><metadata_key: accessibility.dataset_scale>

### Specialized formats or other abbreviations used  [interoperability_if_applicable]
[!TODO] <REPLACE: Describe any specialized data formats, abbreviations, or conventions used in the dataset or file. For example, if the dataset is in a specific file format (e.g., ROOT, HDDM, HDF5), or if there are any domain-specific abbreviations used in variable names or values.><metadata_key: interoperability.data_structure.formats>

## Related Resources [interoperability_if_applicable]
  
### Related datasets, standards, metadata, and ontologies [interoperability_if_applicable]
[!TODO] <REPLACE: If the dataset is related to or derived from other datasets, standards, metadata and ontologies, please list those datasets and describe the relationship. For example, This dataset was derived from [DATASET NAME] (DOI: [DATASET DOI]) by applying [TRANSFORMATION OR PROCESS].><metadata_key: interoperability.related_resources.datasets><metadata_key: interoperability.domain_metadata><metadata_key: interoperability.semantic_layer.schema_url><metadata_key: interoperability.semantic_layer.semantic_context>
  
### Related publications [interoperability_if_applicable]
[!TODO] <REPLACE: List any publications that are associated with the dataset, including DOIs, arXiv IDs, or URLs.><metadata_key: interoperability.related_resources.publications>
  
### Related software [interoperability_if_applicable]
[!TODO] <REPLACE: List any software that is associated with the dataset, including links or PIDs if available.><metadata_key: interoperability.related_resources.software>

### Related ai model [interoperability_if_applicable]
[!TODO] <REPLACE: List any AI models that are associated with the dataset, including links or PIDs if available.><metadata_key: interoperability.related_resources.ai_models>

## Understanding the Data [interoperability_required]

### List of variable name(s), description(s), unit(s), and value labels for each variable in the dataset/file.  [interoperability_required]
[!TODO] <REPLACE: If appropriate, replace the example table with a table listing each variable in the dataset or file, along with its description, unit, and any value labels if applicable.><metadata_key: interoperability.data_structure.features>
  
For example:  
| Variable Name | Description  | Unit  | Value Labels  |  
|---------------|---------------------------|-----------|-----------------------------|  
| temp  | Temperature measurement  | Celsius  | N/A  |  
| status  | Operational status  | N/A  | 0 = Off, 1 = On  |  

### Related Schemas or Ontologies [interoperability_if_applicable]
[!TODO] <REPLACE: list any relevant schemas, ontologies, or vocabularies.><metadata_key: interoperability.semantic_layer.schema_url><metadata_key: interoperability.semantic_layer.semantic_context>

### Codes used for missing data [interoperability_if_applicable] [reusability_if_applicable]
[!TODO] <REPLACE: Replace the example table of codes used to represent missing data in the dataset or file.><metadata_key: reusability.data_quality.missing_data_codes>
  
For example:  
| Code | Description  |  
|------|---------------------------|  
| -999 | Data not collected  |  
| -888 | Measurement error  |  


### Example of the contents  [interoperability_if_applicable]
[!TODO] <REPLACE: Optional. Provide a sample of the dataset or file, or a citation (in bibtex format) or link to where one can review an example of the contents. This can help users understand the structure and content of the dataset.>  

### Data Processing  [interoperability_required]
[!TODO] <REPLACE: Describe preprocessing, calibration, filtering, labeling, or transformations applied to the dataset.><metadata_key: interoperability.provenance.processing_steps>

### Software used to preprocess/ clean/ label the data  [interoperability_if_applicable]
[!TODO] <REPLACE: If the software used to preprocess, clean, or label the data is available, please provide a bibtex format, PID, link, or other access point, along with descriptions of any required packages or libraries to run the scripts.><metadata_key: interoperability.provenance.was_generated_by><metadata_key: interoperability.provenance.software_environment>

## Semantic / Schema Information  [interoperability_if_applicable]
[!TODO] <REPLACE: Describe schema, ontology alignment, semantic context, and controlled vocabularies. If no formal schema or ontology exists, this section may remain empty.  Examples may include:  JSON Schema or XML schema, NETCDF CF conventions, data dictionary or feature definitions, domain  ontologies like ENVO, controlled vocabularies, or units standards. For example:  schema_URL: "https://example.org/schema.json" or ontology_alignment: "http://purl.obolibrary.org/obo/ENVO_00002005"><metadata_key: interoperability.domain_metadata>

---  

# ---- Reusable ----  

## Citation  [reusability_if_applicable]
[!TODO] <REPLACE: Provide a recommended citation if known. Recommend bibtex format.><metadata_key: reusability.citation.preferred_citation>

## License and Usage Rights  [reusability_if_applicable]
[!TODO] <REPLACE: Describe the license under which the dataset is shared, and any usage and contractual rights or restrictions. If no formal license, describe specific permissions for reuse.><metadata_key: reusability.license.spdx_id><metadata_key: reusability.license.license_name> <metadata_key: reusability.license.license_url><metadata_key: reusability.additional_licenses>

## Maintenance & Updates  [reusability_if_applicable]
[!TODO] <REPLACE: Describe update expectations and stewardship responsibility.><metadata_key: reusability.stewardship.maintainer><metadata_key: reusability.stewardship.level><metadata_key: reusability.stewardship.update_frequency><metadata_key: reusability.stewardship.retention_policy>
<metadata_key: reusability.stewardship.versioning_strategy>

## Data Characteristics  [reusability_required] [interoperability_if_applicable]
[!TODO] <REPLACE: Describe variables or features, schema conventions, and missing data handling.><metadata_key: interoperability.data_structure.features><metadata_key: interoperability.data_structure.splits><metadata_key: interoperability.data_structure.spatial_coverage><metadata_key: interoperability.data_structure.temporal_coverage><metadata_key: interoperability.data_structure.modalities>
  
## Data Quality & Limitations  [reusability_required]
[!TODO] <REPLACE: Describe completeness, known issues, uncertainties, noise characteristics, and bias considerations.><metadata_key: reusability.data_quality.completeness><metadata_key: reusability.data_quality.known_issues><metadata_key: reusability.data_quality.validation_methods><metadata_key: reusability.data_quality.noise_characteristics><metadata_key: reusability.data_quality.uncertainty_notes><metadata_key: discoverability.dataset_description.limitations>

## Integrity & Versioning  [reusability_if_applicable]
[!TODO] <REPLACE: Describe checksum availability, fixity strategy, and dataset versioning approach.><metadata_key: reusability.integrity.checksum_available><metadata_key: reusability.integrity.checksum_type><metadata_key: reusability.integrity.checksum_value><metadata_key: reusability.integrity.fixity_policy><metadata_key: reusability.stewardship.versioning_strategy>

---  

# ---- Governed Use ----  

## Access and Permissions  [governed_use_required]
[!TODO] <REPLACE: Describe the dataset`s access posture and any high-level agreements or review constraints.><metadata_key: governed_use.non_sensitivity_governance_metadata.export_control.export_control_status><metadata_key: governed_use.non_sensitivity_governance_metadata.privacy.privacy_status><metadata_key: governed_use.non_sensitivity_governance_metadata.privacy.pii_status><metadata_key: governed_use.non_sensitivity_governance_metadata.privacy.phi_status><metadata_key: governed_use.non_sensitivity_governance_metadata.privacy.privacy_regime_notes><metadata_key: governed_use.compliance.doe_data_management_plan><metadata_key: governed_use.compliance.irb_approved>

## Access conditions   [governed_use_required]
[!TODO] <REPLACE: Describe any conditions that must be met to access the dataset, such as training requirements, proposal processes, collaboration requirements, data use agreements, etc.><metadata_key: governed_use.non_sensitivity_governance_metadata.rights_release_records.ip_restriction_type><metadata_key: governed_use.non_sensitivity_governance_metadata.rights_release_records.agreement_required><metadata_key: governed_use.non_sensitivity_governance_metadata.rights_release_records.agreement_type><metadata_key: governed_use.non_sensitivity_governance_metadata.rights_release_records.public_release_status><metadata_key: governed_use.non_sensitivity_governance_metadata.rights_release_records.record_status>

## Review Provenance [governed_use_if_applicable]

### Release review process  [governed_use_if_applicable]
[!TODO] <REPLACE: Describe the release review process for the dataset, including any institutional reviews, export control reviews, IRB reviews, or other review processes that were conducted before the dataset was released.><metadata_key: governed_use.review_provenance_companion> 

---  

# ---- AI Usable ----  

## AI / Machine Learning Considerations  [ai_usability_required]
[!TODO] <REPLACE: Describe appropriate AI/ML uses, restrictions, bias risks, and safety considerations.><metadata_key: ai_usability.ai_usage.training_use_allowed><metadata_key: ai_usability.ai_usage.inference_use_allowed><metadata_key: ai_usability.ai_usage.evaluation_use_allowed><metadata_key: ai_usability.ai_usage.restrictions><metadata_key: ai_usability.ai_usage.bias_risks><metadata_key: ai_usability.ai_usage.safety_considerations><metadata_key: ai_usability.ai_usage.human_review_required>
  
---  

# Additional Information  
[!TODO] <REPLACE: Optional. Include any relevant contextual notes.>  