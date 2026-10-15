---
name: datacard-generator
description: "Generate Genesis Mission Datacard v2.0.0 documentation for scientific datasets by introspecting a directory and filling the structured template. Use when the user asks to create a datacard, dataset card, dataset documentation, dataset metadata, document a dataset, or prepare a dataset for sharing. Supports six capability dimensions (discoverability, accessibility, interoperability, reusability, governed_use, ai_usability) — pick which ones apply via `supports_*` flags. Also converts MODCON v1 and Genesis v1.2 datacards to v2.0.0."
allowed-tools: Bash(*) Read WebSearch WebFetch
metadata:
  version: 2.1.0
---

# Generating Datacards

Generate a Genesis Mission Datacard v2.0.0 by introspecting a dataset
directory and filling both the YAML frontmatter and the markdown narrative
body of the canonical template, prompting the user for fields that
introspection can't infer.

The skill also has a one-shot **Convert** path for migrating an existing
MODCON v1 or Genesis v1.2 datacard to v2.0.0.

**Validation is upstream's `linkml-validate`** against the vendored schema
(`scripts/genesis_datacard.yaml`); this skill ships no validator. Rules
the schema cannot express are eye checks (`references/validation-rules.md`).

## Workflow

Copy this checklist and check off steps as you go.

```
Progress:
- [ ] 1. Gather context (dataset_path now; `supports_*` capabilities after step 2, with evidence)
- [ ] 2. Run python3 scripts/introspect.py on the dataset directory
- [ ] 3. Load capability-specific guidance
- [ ] 4. Auto-fill YAML from introspect output
- [ ] 5. Confirm dataset readiness level with the user (optional)
- [ ] 6. Prompt for remaining required fields in batches
- [ ] 7. Cross-check every ORCID/ROR/DOI/OSTI identifier via live APIs
- [ ] 8. Compute filename and write the datacard (YAML + markdown body)
- [ ] 9. Validate with linkml-validate
- [ ] 10. Address findings; re-validate
- [ ] 11. Present review summary
```

### 1. Gather context

**Ask for the dataset path now.** Do not answer the capability questions
below cold — first run step 2 (introspect), then come back and propose
each `supports_*` answer with evidence from what introspection found.

- **Dataset path** — directory to document. Ask for this now.
- **Which schema target?** Ask once, and default to `stable`:
  - **`stable`** — Genesis Datacard v2.0.0. Publishable. Use this unless the
    card must be registered now.
  - **`provisional`** — template `2.1.0`: v2.0.0 plus the xCards registry
    spine; registering needs the step 10 export. **Not an upstream
    release**, so never pick it silently.
- **Which capabilities does this dataset support?** (after step 2 — see
  the note at its end). Genesis v2 has six capability containers.
  Propose a default for each, backed by an introspection finding, and ask
  the user to confirm Yes/No:
  - `supports_discoverability` — **always Yes** (schema enforces this). Identification, description, project, release status, contacts, authorship. Minimum core fields.
  - `supports_accessibility` — Yes if the dataset is meant to be accessed/shared. Adds access_policy and access (both required; `access.current_location` required inside), dataset_scale.
  - `supports_interoperability` — Yes if the dataset uses standard formats, structured features, controlled vocabularies, or has documented provenance. Adds data_structure, dates, semantic_layer, provenance, related_resources.
  - `supports_reusability` — Yes if the dataset is licensed for downstream use. Adds license, citation, integrity, stewardship, data_quality.
  - `supports_governed_use` — Yes if the dataset has access restrictions, PII, export control, or formal review requirements. Adds use_governance, non_sensitivity_governance_metadata, compliance (all three required) and review_provenance_companion. The two `sensitivity` blocks live under `discoverability` and are required either way.
  - `supports_ai_usability` — Yes if the dataset is suitable for AI/ML training, inference, or evaluation. Adds ai_usage policy block.

Each `supports_X = Yes` triggers a required `X` block in the YAML and a corresponding set of required fields. Each `supports_X = No` omits that block entirely.

### 2. Introspect the directory

Run `python3 scripts/introspect.py <dataset_path>` and capture the JSON. See
[references/introspection-commands.md](references/introspection-commands.md) for
what each output field means.

**Now return to the capability questions from step 1.** Propose an answer
for each `supports_*` flag backed by an introspection finding — e.g., "I
found a LICENSE file and CITATION.cff → I recommend
`supports_reusability=Yes`. No `train/`/`test/` splits detected →
`supports_ai_usability` optional." Confirm each with the user
([Yes/No]) before moving on to step 3.

### 2b. Resolve the DOI first (fast path)

**If introspection or the user surfaced a DOI, resolve it now** — one
request yields title, abstract, authors with ORCIDs/affiliations,
keywords, publisher, funding, often the OSTI ID. Follow § "Order of
operations: DOI first" and § DOI (incl. the **provenance gate** — a README
DOI is often a cited paper, not this dataset) in
`references/live-enrichment.md`. Carry the result into step 4 and present
it as one table. No DOI? Skip to step 3.

### 3. Load capability-specific guidance

Read `references/capability-prompts.md` (the per-capability prompt sequence).

For deep field-by-field explanation, load the relevant section of
`references/field_reference_guide_v2.0.0.md` only as needed (it is large).

### 4. Auto-fill the data card

**The template is the field reference, not a skeleton to copy** — ~130KB
/ ~35K tokens of commented guidance, none of which belongs in a finished
card. Never read it whole. Read only the section you need:

```bash
# Absolute path from the skill root; works from any cwd.
sed -n 'START,ENDp' <skill_root>/references/genesis_v2.0_template.md
```

Write the card directly, in template key order, with only the blocks the
`supports_*` flags turn on. Step 9 proves nothing required is missing.

**Where to save:** inside `<dataset_dir>/` by default; ask if the user
prefers elsewhere. Compute the filename via the Filename rule (§8 below).

Populate the YAML frontmatter using the decision table in
[references/autofill-table.md](references/autofill-table.md) — read it before
filling anything. It carries the DOI-precedence rule, the `supports_X`
mirroring rule, and which fields must be asked about rather than inferred.

### 5. Confirm dataset readiness level (optional)

If the user wants to indicate dataset readiness, ask them to set a level
(1, 2, or 3) as freetext in the datacard narrative. There is no dedicated
`dataset_readiness` YAML field in Genesis v2 — readiness is expressed
through the combination of `supports_*` flags that are set to `"Yes"`.

Heuristic (roughly: 1 `supports_*=Yes` → level 1, 2-3 → level 2, ≥4 → level 3):

- 1 = Discoverable (metadata only; `supports_discoverability=Yes` + perhaps `accessibility`)
- 2 = Interoperable & Reusable (also license, contacts, provenance; `supports_interoperability` and `supports_reusability`)
- 3 = AI-Ready & Trustworthy (also semantic layer, integrity, governed use; `supports_ai_usability` or `supports_governed_use`)

Confirm with the user.

### 6. Prompt for missing fields

Present auto-discovered values for confirmation. Then ask for unfilled
required fields. Ask **3-5 at a time** following the batches in
`references/capability-prompts.md`. Stop and confirm after each batch.

**Ask only for what is still empty.** Confirm step 2b values in one table;
a DOI never supplies `role[]`, `product_type`, `science_domain`,
access/governance decisions, or `provenance.was_generated_by` — still ask.

**Key vocabulary changes in v2** (full list in `references/lookup-tables.md`):

- **`role[]` is CRediT plus DataCite** — 36 values in v2, multi-valued, and it
  lives **inside** the `person` / `organization` sub-block (Gotcha #8).
  `Data_Curation` and `Data_Collection` no longer exist: v2 has `Data_Curator`,
  `Creator`, `Investigation` and the rest. **Never assume a role — ask.** The
  schema does not require `role[]`, so an empty or guessed one passes silently.
- **Title_Case for all enums** — `Published` not `published`, `Hybrid` not `hybrid`.
- **Sensitivity** uses `OverallSensitivityEnum`, not a tier ladder (Gotcha #2).
- **Yes/No/Conditional** strings (not booleans) for
  `ai_usability.ai_usage.*_use_status` (renamed from `*_use_allowed`) and
  governance Yes/No fields; `Conditional` requires the matching
  `*_use_conditions` free-text field.
- **`science_domain` became a list** — a scalar now fails (Gotcha #9).

### 7. Cross-check identifiers via live APIs

**Not optional; do not write (step 8) without completing it** —
unverified identifiers silently misattribute authorship, funding, or DOIs.
Resolve EVERY ORCID, ROR, DOI, and OSTI award number — user-provided or
inferred, already populated or not — per `references/live-enrichment.md`
(plain HTTP, no API key; `WebFetch`, `curl`, or equivalent). If step 2b
resolved the DOI, this step **verifies rather than discovers**: confirm
seeded ORCIDs/affiliations, query OSTI by canonical OSTI ID (not a bare
`?doi=` search), and reuse the 2b response instead of re-resolving.

Enrich every path under § "Identifier paths to check" (grouped by
capability, so skip opted-out ones) and classify each outcome as that
section defines (clean match / mismatch / incomplete / does not resolve /
rate-limited). **Widespread network failure** — more than 2-3 consecutive
connection errors (not per-ID 404s) — means stop enrichment, tell the
user, and **mark the datacard as unverified** in the step 11 summary; do
not write with silently unverified identifiers.

Batch the fetches, then present ALL findings as one consolidated table
(§ Batching guidance). Do NOT prompt after each individual lookup.

### 8. Filename + write

**Filename rule:** `genesis_datacard_<snake_case(discoverability.identification.name)>.md`,
where `snake_case` lowercases the name, collapses non-alphanumeric runs to a
single `_`, and strips a leading or trailing `_` — the schema's pattern
rejects both, so `TrackML (2018)` must not emit `..._2018_.md`.

**Where to write it:** the dataset directory; the current directory only if
that is not writable. Never the session scratchpad — the card is the
deliverable and must outlive the session. Do not ask. Report the full path,
and if it is under `/tmp`, `/var/tmp` or `$TMPDIR`, say so — the user needs
to move it before it is reaped.

**What to write:** a card in the canonical template's structure
(`references/genesis_v2.0_template.md`), with **both halves filled**:

- **`xCard: {card_type: dataset}`** first. Required in v2 and fixed for every
  Genesis data card — never prompted, and a card without it fails validation.
- **YAML frontmatter** — fully populated from the workflow above. Set
  **all six `supports_*` flags, always** — every one is required. For a
  capability the user opted out of, write `supports_X: "No"` **and** omit the
  `X:` block. Omitting the flag itself fails validation.
- **The spine, on `provisional` only.** Six top-level blocks projected from
  the containers — never asked for, never invented. Projection, not a source
  of truth: if one disagrees with its container, the container wins.
  `scripts/convert_v12_to_v20.py --spine` does the same projection, so read
  `project_spine()` there rather than re-deriving it:

  | spine | from |
  |---|---|
  | `datacard.id.value`, `.datacard_version` | `discoverability.datacard.*` |
  | `identification.name`, `.version` | `discoverability.identification.*` |
  | `categorization.tags.project` | `dataset_description.tags.project` |
  | `categorization.tags.science` | `dataset_description.science_domain[0]` |
  | `categorization.task_category`, `.task_subcategory` | `dataset_description.*` |
  | `dataset_info.data_formats`, `.modalities` | `interoperability.data_structure.*` |
  | `license.spdx_id`, `.name`, `.url` | `reusability.license.*` |
  | `description.summary` | `dataset_description.dataset_summary` |
  | `categorization.tags.risk` | the **dataset's** sensitivity, not the card's — the registry filters access with this. Get the mapping from `references/lookup-tables.md` § "Projecting `tags.risk`" and follow it exactly; under-restricting here publishes controlled data. |

  Also add a `change_log` entry saying the card carries a provisional spine
  and is not an upstream v2.1 release, so it is greppable at migration time.

**Keep the v1.2 original when converting.** v2 is a provisional upgrade, so
the source is the rollback path: `convert_v12_to_v20.py` refuses to write
over its input and keeps a byte-identical copy as
`<out>.v1.2-source.md`, naming it in the card's `change_log`. Do not
delete it, and do not convert in place.
- **Markdown narrative body** — also fully filled. See
  [references/body-fill-guide.md](references/body-fill-guide.md) for the
  section-by-section mapping.

**Strip all placeholder markup before saving.** No `[!TODO]`, `<REPLACE:>`,
`<INSTRUCTIONS:>`, `<metadata_key:>`, `${VARIABLE}`, or `__VALUE__` tokens
should remain. Verify with:
`grep -E '\[!TODO\]|<REPLACE:|<INSTRUCTIONS:|<metadata_key:|\$\{|__VALUE__' <output_file>`

### 9. Validate

`linkml-validate` takes YAML, so split the frontmatter off first (uv
fetches linkml on demand):

```bash
awk 'NR>1 && /^---$/{exit} NR>1' <written_file> > /tmp/card.yaml
# stable:
uv run --with linkml linkml-validate \
  -s <skill_root>/scripts/genesis_datacard.yaml \
  -C GenesisDatacardClass /tmp/card.yaml
# provisional (spine): a card with no spine also passes this one
uv run --with linkml linkml-validate \
  -s <skill_root>/scripts/genesis_datacard_v2_1_provisional.yaml \
  -C GenesisDatacardSpinedClass /tmp/card.yaml
```

Run **exactly one** — whichever target step 1 chose.

Prints `No issues found`, or one `[ERROR]` per problem naming the JSON
path; exit 1 on failure. Enums: `references/lookup-tables.md`. Every
finding is real — v2.0.0 fixed the `dataset_publisher` rule that fired on
every v1.2 card, so nothing here is suppressed.

### 10. Address findings

Loop steps 6 → 7 → 8 → 9 until the only output left is `No issues found`
**Do not claim done
with un-addressed errors.** `warn` severity findings can stand
in the review summary but errors must be resolved.

On loop-back to step 7, re-enrich ONLY identifiers changed in this
iteration (§ Re-check-only-changed).

**`provisional`:** the xCard registry rejects every full card. Export and
submit per [references/registry-export.md](references/registry-export.md).

### 11. Review summary

Present:
- Auto-populated fields (count + brief list)
- User-provided fields (count + brief list)
- Empty / `not_applicable` fields (with reason)
- Validator warnings
- Suggestions for improvement (empty optional fields worth filling)

Ask if the user wants to revise any section before finishing.

---

## Convert path

Asked to convert an existing card — MODCON or Genesis v1.2 — follow
[references/convert-path.md](references/convert-path.md). It names which
script to run, how the four report lists drive the prompts, and how the v1.2
original is preserved as the rollback path.

---

## Gotchas (read before generating)

More in [references/gotchas.md](references/gotchas.md).

1. **`workflow.state` ≠ `release_status`.** Both are needed (under
   `discoverability.workflow.state` and `discoverability.release_status`).
   Recommended alignments are in `references/lookup-tables.md`.

2. **Sensitivity is no longer a tier ladder.** Use
   `OverallSensitivityEnum` (`Public | Unclassified_Uncontrolled | CUI |
   UCNI | Classified | Legacy_Controlled | Mixed | Other_Controlled`) on
   both `discoverability.datacard.sensitivity.overall_sensitivity` (the
   document) and `discoverability.sensitivity.overall_sensitivity` (the
   dataset) — independent, often different, never defaulted to match.

3. **`primary_id.type`** is not `doi` before a DOI is minted — use
   `ark`, `local`, or `unregistered`.

4. **`provenance.was_generated_by` and `.processing_steps`** are both
   required (when `supports_interoperability=Yes`) and often forgotten.

5. **`change_log` is append-only.** On re-runs, add a new entry plus
   `updated_date` bump. Never edit or delete prior entries. The field
   name inside each entry is `datacard_version`, and the card's own
   `datacard.datacard_version` (required, `"1.0.0"` at creation) bumps
   with it.

6. **`_repository` is system-owned.** Never populate it.

7. **`supports_discoverability` is always `"Yes"`.** The schema enforces
   this — every Genesis datacard has at least the discoverability block.

8. **`role[]` lives INSIDE the agent sub-block, not on the agent entry
   itself.** `AgentClass` — `created_by[].creator`, `authors`,
   `contributors`; `contact`/`additional_contacts` use `ContactClass`, person
   or organization only —
   is a tagged union of `person`/`organization`/`ai_model`/`software` with no
   top-level `role`. Each of the four carries its own `role[]`:
   ```yaml
   - contribution_date: "2026-07-01"
     creator:
       person: {given_name: Jane, family_name: Doe, role: [Data_Curator]}
   ```
   **`facilities` and `related_resources.software|ai_models` are NOT
   agents** — `FacilityClass`/`SoftwareClass`/`AIModelClass` take `name` and
   `role`/`relationship` directly on the entry. See `lookup-tables.md` for
   their required fields.

9. **`science_domain` is a **list** of closed, quoted-string-with-spaces
   values.** Both `discoverability.dataset_description.science_domain` and
   `interoperability.domain_metadata.science_domain` (that block is a
   `NamedThing` — needs `name` if written) use `ScienceDomainEnum`,
   whose values carry spaces (as `ProductTypeEnum` and
   `ApprovedEnvironmentEnum` also do) rather than `Title_Case` tokens. It was already a closed enum in v1.2 with the same 15
   values — what v2 changed is **single → multivalued**, so write
   `science_domain: ["Physics"]` even for one entry. A scalar fails. See
   `references/lookup-tables.md` for the list.

10. **`datacard.updated_date` is `if_applicable`, not required.** Leave it
    blank on initial creation — a card never updated has nothing to report.
    Set it only on a genuine update, alongside a new `change_log` entry
    (Gotcha #5).

11. **Never resolve a dataset DOI via OSTI `?doi=`.** A DOE prefix
    (`10.15485`, `10.11578`) tempts a jump straight to the OSTI API. Don't
    — `?doi=` can return several records that disagree on the funder, and
    OSTI carries fewer ORCIDs than DataCite. Always `doi.org` content
    negotiation first (step 2b); OSTI comes later, by canonical ID.

---

## References

- **Template (do not edit)**: [references/genesis_v2.0_template.md](references/genesis_v2.0_template.md)
- **Field reference (do not edit)**: [references/field_reference_guide_v2.0.0.md](references/field_reference_guide_v2.0.0.md)
- **Upstream provenance**: https://gitlab.osti.gov/genesis/data-cards, path
  `datacard_schema/src/genesis_datacard/schema/genesis_datacard.yaml`, vendored
  at commit `e29a6f0`.
- **LinkML schema** (validator source of truth): `scripts/genesis_datacard.yaml`
- **Per-capability prompts**: [references/capability-prompts.md](references/capability-prompts.md)
- **Body-fill guide**: [references/body-fill-guide.md](references/body-fill-guide.md)
- **Lookup tables** (enums, vocabularies): [references/lookup-tables.md](references/lookup-tables.md)
- **Validation extras** (warn-level rules): [references/validation-rules.md](references/validation-rules.md)
- **Live DOI/ORCID/ROR/OSTI enrichment**: [references/live-enrichment.md](references/live-enrichment.md)
- **Introspection commands**: [references/introspection-commands.md](references/introspection-commands.md)
- **Auto-fill decision table**: [references/autofill-table.md](references/autofill-table.md)
- **v1.2 → v2.0.0 conversion map**: [references/v12-to-v20-map.md](references/v12-to-v20-map.md)
- **Validation**: upstream `linkml-validate` (see step 9)
- **Provisional spine schema** (temporary): `scripts/genesis_datacard_v2_1_provisional.yaml`.
  **To remove it when upstream publishes a real v2.1:** delete that file,
  re-vendor `scripts/genesis_datacard.yaml` and the template, and point step 9
  back at `GenesisDatacardClass`.
- **Introspector**: `scripts/introspect.py`
- **Converters**: `scripts/convert_modcon_to_genesis.py` (MODCON → Genesis),
  `scripts/convert_v12_to_v20.py` (Genesis v1.2 → v2.0.0, `--spine` for provisional)
