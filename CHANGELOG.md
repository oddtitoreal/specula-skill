# Changelog

All notable changes to this project are documented in this file.

## [0.2.0-scaffold] - 2026-03-27

### Added
- `validate_workflow()` method in `scripts/validate_specula.py` (v0.2-scaffold). Validates Specula workflow JSON files for: required top-level fields (`workflow_id`, `project_id`, `phases`), valid phase IDs against the canonical sequence, dual-role requirement (at least 2 distinct `validation_roles` per phase), valid prerequisite references, and Phase 5/6 specific warnings (missing `dissent_protocol`, missing `re_speculation_trigger`).
- `--workflow` CLI flag to invoke workflow validation from the command line.
- Updated module docstring to reflect v0.2-scaffold scope and planned v0.2 full / v0.3+ roadmap.

### Notes
- This scaffold release marks the start of v0.2 development. The `validate_workflow()` method validates structure only — runtime execution trace validation is planned for v0.2 full.
- Prompt playbook generation (also planned for v0.2) is not included in this scaffold.
- All v0.1.x validations (constitution, state machine, integration) remain unchanged and backward compatible.

## [0.1.2] - 2026-03-20

### Added
- `ALIGNMENT.md` with explicit mapping between `specula-skill`, `specula-framework`, and `specula-method`.

### Changed
- README updated to `v0.1.1` and clarified profile boundary and interoperability scope.
- SKILL documentation updated with canonical alignment section.
- `examples/luxury-fashion-brand/validation-results.txt` refreshed after schema-enabled validation.

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
