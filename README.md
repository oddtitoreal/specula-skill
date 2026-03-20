# SPECULA Skill Repository

Technical repository for the SPECULA governance framework.

SPECULA helps design, operationalize, and validate AI governance through:
- AI constitutions (principles, values, constraints)
- state machine control logic
- JSON schemas
- validation tooling
- reusable templates

## Repository Layout

```text
specula-skill/
├── SKILL.md
├── README.md
├── requirements.txt
├── scripts/
│   └── validate_specula.py
├── references/
│   ├── schemas-constitution.json
│   ├── schemas-statemachine.json
│   └── versioning.md
├── templates/
│   ├── example-constitution.json
│   └── example-state-machine.json
└── docs/
    └── specula-documentazione.html
```

## Quick Start

### 1) Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Validate sample artifacts

```bash
python3 scripts/validate_specula.py \
  --constitution templates/example-constitution.json \
  --state-machine templates/example-state-machine.json
```

If everything is valid, the command exits with code `0`.

## Validator Behavior

`scripts/validate_specula.py` performs:
- JSON parsing checks
- JSON Schema validation (when `jsonschema` is installed)
- logical consistency checks for constitutions
- logical consistency checks for state machines
- constitution/state machine integration checks

Current output levels:
- `ERROR`: invalid artifact (non-zero exit)
- `WARNING`: potentially unsafe or incomplete configuration

## Templates

Use templates as a starting point:
- `templates/example-constitution.json`
- `templates/example-state-machine.json`

Adapt IDs, principles, guards, and transitions to your domain before production use.

## Notes

- Governance artifact versions follow semantic versioning; details in `references/versioning.md`.
- The HTML document in `docs/` is a supporting reference, not the source of truth.
- `SKILL.md` is the canonical skill definition for Codex/Codex-like agents.
