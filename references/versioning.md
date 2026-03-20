# SPECULA Versioning Rules

This repository follows semantic versioning (`MAJOR.MINOR.PATCH`) for all SPECULA artifacts.

## Constitution Versioning

Increase:
- `PATCH` for wording clarifications that do not alter behavior.
- `MINOR` when adding non-breaking principles, constraints, or metadata.
- `MAJOR` when changing or removing principles/constraints that can alter governance outcomes.

## State Machine Versioning

Increase:
- `PATCH` for non-behavioral edits (descriptions, metadata).
- `MINOR` for additive changes (new optional states/transitions) compatible with existing flows.
- `MAJOR` when changing transition logic, guard behavior, terminal states, or compatibility assumptions.

## Compatibility Rules

- A state machine should reference a constitution with the same major version unless explicitly documented.
- Breaking constitution changes require re-validating all dependent state machines.
- Integration tests must run on every `MINOR` and `MAJOR` update.

## Recommended Release Process

1. Update artifact versions in JSON files.
2. Run validator against templates and project examples.
3. Document migration notes for any `MAJOR` change.
4. Tag release with `vX.Y.Z`.
