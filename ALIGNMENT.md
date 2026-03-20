# Alignment Matrix: specula-skill vs specula-framework vs specula-method

## Purpose

This document defines how `specula-skill` aligns with:
- `specula-framework` (private delivery + runtime profile)
- `specula-method` (open methodological profile)

It also defines explicit boundaries so repository scope remains honest.

## Canonical Sources

- Framework runtime canon: <https://github.com/oddtitoreal/specula-framework>
- Method canon (open): <https://github.com/oddtitoreal/specula-method>

When this repository diverges from either source, update this file.

## Scope Boundary (v0.1.x)

`specula-skill` currently provides the constitutional/state-machine governance layer:
- constitution artifacts
- state-machine artifacts
- schema validation and integration checks

`specula-skill` does **not** implement the full runtime profile used by `specula-framework`:
- no `MODE: <mode> | PHASE: <phase>` output contract
- no canonical `meta/payload` wrapper enforcement
- no phase-gating orchestrator (`0,1,1.5,2,3,4,5,6`)

## Terminology Mapping

| Canonical term (`specula-framework`) | In `specula-skill` v0.1.x | Status |
|---|---|---|
| Ethical Gate | Guard checks + escalation rules | Partial mapping |
| Refusal Register | Constraint violations + escalation/audit records | Conceptual mapping |
| Guardian | Not implemented in validator/runtime | Out of scope |
| Canonical modes (`exploration`, `ethical_gate`, etc.) | Not represented as runtime mode enum | Out of scope |
| `artifact_id/phase/mode` metadata wrapper | Not enforced | Out of scope |

## Artifact Profile Mapping

### Runtime profile (`specula-framework` + `specula-method` runtime-alignment)

- strict wrapper: `{"meta": {...}, "payload": {...}}`
- canonical `phase` and `mode` enums
- runtime sequence with phase advancement rules

### Skill profile (`specula-skill`)

- standalone constitution JSON
- standalone state-machine JSON
- integration validation across principle/guard mappings

These profiles are intentionally different in v0.1.x.

## Version Track Mapping

| Repository | Track | Notes |
|---|---|---|
| `specula-method` | `v1.x` (public method evolution) | Open conceptual + runtime-alignment docs |
| `specula-framework` | `v2.3` + `v2.4.5.x` references | Private delivery/runtime implementation track |
| `specula-skill` | `v0.1.x` | Technical subset for constitution/state-machine governance |

Current templates in this repo include `framework_version: SPECULA_v2.3` as compatibility reference for governance semantics.

## Attribution and License Boundary

`specula-method` requires attribution and is distributed under CC BY-SA 4.0.

This repository is MIT-licensed for its code/assets. If method text or substantial derivative content from `specula-method` is reused, attribution obligations remain applicable. See:
- <https://github.com/oddtitoreal/specula-method/blob/main/ATTRIBUTION.md>
- <https://github.com/oddtitoreal/specula-method/blob/main/LICENSE.md>

## Contributor Rules

Before merging changes that touch governance semantics:
1. Verify terminology alignment against `specula-framework/specs/terminology.md`.
2. Verify boundary honesty in `README.md` and `SKILL.md`.
3. Update this file if mappings or boundaries change.
4. Re-run validator on templates and examples.

## Planned Alignment Work

### v0.2 (planned)
- Add optional bridge schema for runtime wrapper compatibility (`meta/payload`).
- Add explicit mapping from canonical runtime modes to skill-level checks.

### v0.3+ (planned)
- Optional phase-aware validation profile aligned to method/framework runtime sequence.
- Extended identity/memory governance mappings.
