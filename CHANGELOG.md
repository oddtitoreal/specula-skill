# Changelog

All notable changes to this project are documented in this file.

## [0.1.1] - 2026-03-20

### Fixed
- Aligned `templates/example-state-machine.json` with state-machine schema enum:
  `guards[].action_on_violation` now uses `log` instead of invalid `warn`.

### Notes
- This patch release ensures template validation passes with `jsonschema` enabled.

## [0.1.0] - 2026-03-20

### Added
- Initial SPECULA constitutional governance core
- Constitution and state machine JSON schemas
- Validation tool for constitution/state-machine consistency and integration
- Example templates for constitution and state machine artifacts
- Versioning guidance for governance artifacts
- SPECULA manifesto layer (`SPECULA-MANIFESTO.md`)
- SPECULA method layer (`METHOD.md`)
- Domain example: `examples/luxury-fashion-brand/` with validation output

### Changed
- Documentation aligned to implemented v0.1 scope
- Validation CLI standardized on `--state-machine`

### Known Limitations
- Workflow orchestration validation not included (planned v0.2)
- Prompt playbook/template generation not included (planned v0.2)
- Runtime execution trace validation not included (planned v0.2+)
- Identity/memory framework not included (planned v0.3+)
