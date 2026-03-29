# Quick Start

**Your AI agent behaves inconsistently. It doesn't reflect your organization's values when edge cases arise.**

This validates a governance constitution and state machine in under 15 minutes.

## Step 1 — Install (2 min)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Step 2 — Validate a real example (3 min)

```bash
python3 scripts/validate_specula.py \
  --constitution examples/community-space-brand/constitution.json \
  --state-machine examples/community-space-brand/state-machine.json
```

This validates the governance artifacts for *Il posto delle fragole* — a community space in Pesaro built using the Specula Method. The constitution encodes five radical values (Abitabilità, Non giudizio, Abilitazione, Immaginazione in pratica, Comunità viva) as operational governance rules with explicit constraints and escalation paths.

→ [How brand values became governance rules](./examples/community-space-brand/brand-values.md)
→ [Full case study in specula-method](https://github.com/oddtitoreal/specula-method/tree/main/case-studies/case_study_posto_delle_fragole.md)

## Step 3 — Validate your own artifacts (10 min)

```bash
cp templates/example-constitution.json my-constitution.json
cp templates/example-state-machine.json my-state-machine.json
# edit both files to reflect your agent's values and operational flow
python3 scripts/validate_specula.py \
  --constitution my-constitution.json \
  --state-machine my-state-machine.json
```

The validator checks JSON structure, schema conformance, logical consistency within each artifact, and integration coherence between constitution and state machine.

## What next?

- **Understand the three layers**: [SKILL.md](./SKILL.md)
- **Compare both examples**: [examples/README.md](./examples/README.md)
- **Canonical runtime specs**: [specula-framework](https://github.com/oddtitoreal/specula-framework)
- **Learn the method behind the artifacts**: [specula-method](https://github.com/oddtitoreal/specula-method)
