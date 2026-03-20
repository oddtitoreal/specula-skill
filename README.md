# SPECULA Governance Framework

![Version 0.1.0](https://img.shields.io/badge/version-0.1.0-blue)
![Status Initial Release](https://img.shields.io/badge/status-initial%20release-brightgreen)
![License MIT](https://img.shields.io/badge/license-MIT-green)

**Version**: 0.1.0  
**Release Date**: 2026-03-20  
**Status**: Initial Release - Constitutional Governance Core

## What This Is

Technical framework for designing and validating AI governance using:
- constitutional principles
- operational state-machine control logic
- explicit guard conditions
- schema and consistency validation

This repository is the technical core of SPECULA v0.1.

## What's In v0.1.0

- Constitutional design patterns (principles, values, constraints)
- State machine operationalization (states, transitions, guards)
- Guard condition specification and mapping
- JSON schema validation (constitution + state machine)
- Constitution/state machine integration checks
- Working templates and validator tool

## What's Not In v0.1.0

- Workflow orchestration validation (planned v0.2)
- Prompt playbook/template generation (planned v0.2)
- Runtime execution trace validation (planned v0.2+)
- Identity/memory frameworks (planned v0.3+)

## Repository Layout

```text
specula-skill/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── LICENSE
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

1. Install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Validate sample artifacts:

```bash
python3 scripts/validate_specula.py \
  --constitution templates/example-constitution.json \
  --state-machine templates/example-state-machine.json
```

3. Validate your own artifacts:

```bash
python3 scripts/validate_specula.py \
  --constitution your-constitution.json \
  --state-machine your-state-machine.json
```

## Validator Behavior

`/scripts/validate_specula.py` performs:
- JSON parsing checks
- JSON Schema validation (when `jsonschema` is installed)
- logical consistency checks for constitutions
- logical consistency checks for state machines
- constitution/state machine integration checks

Exit behavior:
- `0`: no validation errors
- `1`: one or more validation errors

Warnings are non-blocking but should be reviewed.

## Roadmap

### v0.1 (Current - 2026-03-20)
- Constitution and state machine design + validation core

### v0.2 (Q2 2026)
- Workflow validation
- Prompt playbook templates
- Brand-specific examples

### v0.3 (Q3 2026)
- Identity and memory frameworks
- Runtime trace extensions
- Governance performance metrics

### v1.0 (2027)
- Full platform integration
- Community extensions
- Production deployment guides

## Notes

- Governance artifact versioning rules: `references/versioning.md`
- Canonical technical reference for the skill: `SKILL.md`
- Templates are starting points and should be adapted per domain.
