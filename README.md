# datacard-generator 2.1.0

Skill version **2.1.0**, targeting **Genesis Mission Datacard schema v2.0.0**,
plus a provisional template **2.1.0** for cards that carry the xCards registry
spine. The skill version and the schema version are independent — a skill-only
fix would be 2.1.1 against an unchanged 2.0.0 schema. The version you have is in
`datacard-generator/SKILL.md` under `metadata.version`.

Generates **Genesis Mission Datacard v2.0.0** documentation for a scientific
dataset, converts MODCON v1 and Genesis v1.2 cards to v2.0.0, and exports a
card in the form the HPDF xCard registry accepts.

## What changed since 2.0.0

- **Provisional cards register.** New `scripts/export_xcard.py` writes
  `<card>.xcard.md`, the document the registry accepts (see below);
  `SKILL.md` step 10 points to `references/registry-export.md` for it.
  Verified against a live registry.
- **Provisional cards declare `template_version: "2.1.0"`**, in generation and
  in `convert_v12_to_v20.py --spine`. Stable cards stay at `2.0.0`.
- New `scripts/xcard.schema.json`: the registry's xCard schema, copied from the
  registry image, so exports are checked without a running registry.

## Install

Clone this repository into your agent's skills directory as `datacard-generator`:

```bash
# Claude Code
git clone --branch v2.1.0 https://github.com/jeanbez/datacard-generator-skill.git \
  ~/.claude/skills/datacard-generator

# other agent harnesses
git clone --branch v2.1.0 https://github.com/jeanbez/datacard-generator-skill.git \
  ~/.agents/skills/datacard-generator
```

The skill is then available as `datacard-generator`. Nothing else to configure.

## Requirement: uv

The scripts carry [PEP 723](https://peps.python.org/pep-0723/) inline
dependencies and are run with `uv`, which resolves them per-invocation — there
is no virtualenv to create and nothing to `pip install`:

```bash
uv run -q scripts/introspect.py /path/to/dataset
```

Install `uv` with `curl -LsSf https://astral.sh/uv/install.sh | sh` or
`brew install uv`. Without it, install `linkml>=1.9.3`, `pyyaml>=6.0` and
`jsonschema>=4.18` yourself and run the scripts with `python3`.

## Two modes: stable and provisional

Step 1 of the skill asks which you want. The choice is not cosmetic.

**`stable`** writes a plain v2.0.0 card and validates it against the vendored
upstream schema:

```bash
uv run -q --with linkml linkml-validate \
  -s scripts/genesis_datacard.yaml -C GenesisDatacardClass card.yaml
```

**`provisional`** writes template `2.1.0`: the v2.0.0 card plus an **xCards
registry spine** — six top-level blocks (`datacard`, `identification`,
`categorization`, `dataset_info`, `license`, `description`) duplicating values
that already live in the capability containers. It validates against a
different target:

```bash
uv run -q --with linkml linkml-validate \
  -s scripts/genesis_datacard_v2_1_provisional.yaml \
  -C GenesisDatacardSpinedClass card.yaml
```

Run **exactly one** of those. A spine-less card passes either schema, but a
spined card is rejected by the stable one (`Additional properties are not
allowed`). `linkml-validate` has no `.md` loader, so extract the frontmatter to
a `.yaml` first — the skill's step 9 gives the `awk` one-liner.

### Registering: submit the export, not the card

The HPDF xCard registry picks its validator from a card's top-level keys:
`xCard` selects its xCard spine schema, `supports_*` and the capability
containers select the Genesis LinkML schema, and a card with both is rejected
as "profile markers are ambiguous". Genesis v2 requires both, so **no full v2
card can register** — the registry answers `422 invalid_xcard` with no detail.

Export the submission instead:

```bash
uv run -q scripts/export_xcard.py genesis_datacard_<name>.md
```

It writes `genesis_datacard_<name>.xcard.md` beside the card, validated against
`scripts/xcard.schema.json`, and exits 1 naming each problem if it cannot. POST
that file to `/api/current/registry/data_card` with content type
`text/vnd.genesis.data-card+markdown`.

The export is a projection of the full card: fix the card and re-export rather
than editing it. ORCIDs, affiliations, contacts, sponsors, provenance, quality
notes, checksums and access rules survive only in the narrative body, so the
full card stays the authoritative record.

### Why the spine exists

The discovery engine's card parser reads pre-capability-container paths; a
correct v2.0.0 card parses there as `UNKNOWN` / `'Untitled'` without the spine.
The spine is a **projection, never a source of truth**. If a spine value ever
disagrees with its container, the container is right.

### Removing the spine when upstream ships a real v2.1

When the capability-container paths land upstream, delete:

- `scripts/genesis_datacard_v2_1_provisional.yaml`
- the `--spine` flag and `project_spine()` in `scripts/convert_v12_to_v20.py`
  (`export_xcard.py` reuses `project_spine()` for the sensitivity mapping, so
  move that logic into it first)
- the spine section of `SKILL.md` step 8, and step 1's mode question

Cards already written carry a dated `change_log` entry saying they hold a
provisional spine, so they are greppable at migration time.

## Honest status

Known limits, so you are not surprised by them:

- **The spine is provisional.** It is not an upstream v2.1 release, and the
  shape may not match whatever upstream eventually ships.
- **The registry rejects full v2 cards.** That is a registry routing bug, not
  something a card can fix; until it is fixed, register through the export.
- **Tests are not shipped.** The skill's pytest suite lives on the developer's
  disk only. It covers both converters, the two-hop MODCON path and the export,
  but this repository carries none of it. Treat converter output as a draft to
  read, not as finished.
- **Both converters report rather than guess.** They exit non-zero when
  anything needs a human: `missing_required` lists fields to prompt for,
  `reported` lists values v2 cannot represent unambiguously, `orphans` lists v1
  fields with no v2 home and their values. Read all three. The MODCON path runs
  through v1.2 first (`convert_modcon_to_genesis.py`, then
  `convert_v12_to_v20.py`); only the second hop validates.
- **Sensitivity is the one thing to check by hand.** The spine's
  `categorization.tags.risk` and the export's `sensitivity` control access
  filtering, and an absent or wrong value is as permissive as "public". Both take
  the stricter of the dataset's and the card's sensitivity, escalate to
  `restricted` on any control status flag or authoritative marking, and never
  leave it unset — but verify it on any controlled dataset before you register.
- **The export claims no governance it was not given.** Export-control and
  privacy flags are filled only from `governed_use`; a card without it registers
  without them.

## Upstream

The schema, template and field guide under `references/` and `scripts/` are
vendored byte-identical from the upstream `data-cards` repository at commit
`e29a6f0` (schema version 2.0.0). `scripts/xcard.schema.json` is copied from the
HPDF xCard registry image (genesis-discovery-engine revision `7fe6d044`). Do not
edit them locally — re-vendor instead.
