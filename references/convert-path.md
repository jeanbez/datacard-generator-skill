# Convert path — MODCON or Genesis v1.2 → v2.0.0

Read this when asked to convert an existing card. The field-level mapping it
implements is in [v12-to-v20-map.md](v12-to-v20-map.md).

**Which script.** A **Genesis v1.2** card goes through
`convert_v12_to_v20.py` (add `--spine` for registry mode). A **MODCON** card
goes through `convert_modcon_to_genesis.py` first, then that output through
`convert_v12_to_v20.py` — the enum mapping lives in one place.

`convert_v12_to_v20.py` keeps the original: it refuses to write over its
input and saves the source as `<out>.v1.2-source.md`.
(`convert_modcon_to_genesis.py` does not — keep your own copy of the MODCON
card, or run it with `--json` first.) v2 is a provisional
upgrade, so that file is the rollback path — do not delete it.

1. Run the converter with `--json` and capture the report:
   - `mapped` — what it rewrote mechanically.
   - `reported` — values v2 cannot represent unambiguously. **Prompt for each.**
     (`convert_v12_to_v20.py` only.)
   - `orphans` — fields with no v2 home, with their old values.
   - `missing_required` — required fields it could not fill. **Prompt for each.**
   - `convert_v12_to_v20.py` also reports `invalid` — if non-empty the written
     card **does not validate** and no prompt will fix it; resolve those first.
     `convert_modcon_to_genesis.py` emits a deliberately v1.2-shaped card and
     does not validate at all, so hop 2 is the only validation gate.
2. After prompting the user for the fields in `missing_required`, **compose
   the final YAML inline** — apply the answered values to the converter's
   `mapped` output. Do NOT rerun `convert_modcon_to_genesis.py` after prompts;
   the converter only reads the v1 source and cannot re-integrate user
   answers.
3. Set `discoverability.datacard.creation_method = "Hybrid"`,
   `template_version = "2.0.0"` (`"2.1.0"` with `--spine`), `datacard_version = "1.0.0"`, and **append** a
   new `change_log` entry `{change_date: today, datacard_version: "1.0.0",
   summary: "Converted from …"}`. Never overwrite `change_log[0]` — that is the
   original creation record.
4. **Fill the markdown body** using `references/body-fill-guide.md`.
5. **Cross-check every identifier via live APIs** (step 7 of the Generate path).
6. **Compute the filename and write the datacard** (step 8 of the Generate path).
7. Run the validator (step 9 of the Generate path).
8. Present the review summary (step 11 of the Generate path).
