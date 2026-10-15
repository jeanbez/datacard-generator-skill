# datacard-generator

An agent skill that writes **Genesis Mission Datacards** (schema v2.0.0 + xCard
spine) for scientific datasets. Point it at a dataset folder and it fills in the card,
asking you for what it can't work out. It also converts older MODCON v1 and
Genesis v1.2 cards.

## Install

Clone it into your agent's skills folder:

```bash
# Claude Code
git clone https://github.com/jeanbez/datacard-generator-skill.git \
  ~/.claude/skills/datacard-generator

# other agents
git clone https://github.com/jeanbez/datacard-generator-skill.git \
  ~/.agents/skills/datacard-generator
```

To update later, run `git pull` in that folder.

The scripts run with [uv](https://docs.astral.sh/uv/) (`brew install uv`), which
installs their dependencies automatically.

Then ask your agent to "create a datacard for /path/to/dataset".

## Stable or provisional

The skill asks which kind of card you want:

- **Stable** (default): an official Genesis v2.0.0 datacard.
- **Provisional**: the same card plus extra fields the xCard registry needs,
  labelled template version `2.1.0`. This is **not an official Genesis
  release**; use it only if you need to register the card now.

To register a provisional card, the skill writes a second file,
`<card>.xcard.md`, and that is the file you submit to the registry. Keep the
full card as the official record.
