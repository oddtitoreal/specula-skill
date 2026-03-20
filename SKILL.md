---
name: specula-method
description: |
  Technical implementation guide for the SPECULA governance framework (v0.1).

  In scope: constitutional design, state machine patterns, guard conditions,
  governance integration patterns, and validation for constitutions/state machines.

  Out of scope (planned for v0.2+): workflow orchestration validation, prompt
  playbook generation, runtime execution frameworks, and identity/memory layers.

  Use this skill when designing AI governance with constitutions, constraints,
  guards, and operational state transitions.
compatibility: |
  - AI systems architecture fundamentals
  - State machine design and control logic
  - JSON modeling and schema validation
---

# SPECULA Method - Technical Implementation Guide

## Scope Statement

**What this skill covers (v0.1):**
- Constitution design (principles, values, constraints)
- State machine operationalization (states, transitions, guards)
- Guard-to-principle mapping
- Multi-stakeholder governance patterns
- JSON schema validation for constitution and state machine artifacts
- Constitution/state machine integration checks

**What is not included yet (planned for future versions):**
- Workflow orchestration schema/validation
- Prompt playbook templates
- Runtime execution trace validation
- Identity and memory frameworks

## Foundations

SPECULA is a governance-first method for AI systems.

Core principles:
- **Constitution-first design**: define governing intent before implementation
- **Operational enforcement**: use state transitions and guards to enforce intent
- **Machine-readable contracts**: represent governance as structured JSON artifacts
- **Auditability**: preserve explicit reasoning and decision traces

The practical stack:
1. Constitution (principles and constraints)
2. State machine (operational control logic)
3. Schemas (machine validation)
4. Validation tooling (consistency and integration checks)

## AI Constitution

A SPECULA constitution defines the governance contract.

```text
Constitution {
  constitution_id: string
  version: semver
  principles: [Principle]
  constraints: [Constraint]
  values?: [Value]
  failure_modes?: [FailureMode]
  conflict_resolution?: ConflictResolution
}
```

Implementation process:
1. Identify stakeholder values.
2. Convert values into explicit principles.
3. Operationalize principles with constraints.
4. Define conflict resolution and failure handling.
5. Validate with schema and integration checks.

## Control Logic & State Machines

State machines enforce constitutional intent during runtime decisions.

```text
StateMachine {
  id: string
  initial_state: string
  states: map[state_id -> state]
  transitions?: [Transition]
  guards?: [Guard]
}
```

Key operational rules:
- Every transition must point to existing states.
- Terminal states should exist to avoid endless loops.
- Guards should reference constitutional principles when possible.
- Unreachable states should be reviewed and justified.

## System Architecture

Typical governed flow:

```text
Input -> Validation -> Constitutional Assessment -> Decision -> Guard Checks -> Output
```

Recommended output shape includes:
- response payload
- confidence/justification
- governance trace (checks applied, transitions taken)

## JSON Schemas

SPECULA v0.1 provides these schemas:
- `references/schemas-constitution.json`
- `references/schemas-statemachine.json`

Use schema validation to enforce structural integrity before deeper logic checks.

## Validation

Use the validator for structure and integration checks:

```bash
python3 scripts/validate_specula.py \
  --constitution constitution.json \
  --state-machine state-machine.json
```

Validator checks in v0.1:
- JSON loading and parse integrity
- Constitution schema and consistency checks
- State machine schema and consistency checks
- Integration checks (principles mapped to guards)

Exit behavior:
- Exit `0`: no validation errors
- Exit `1`: one or more errors
- Warnings are non-blocking but should be reviewed

## Technical Implementation Guide

### Step 1: Define constitution

```json
{
  "constitution_id": "my_system_v1",
  "version": "1.0.0",
  "principles": [
    {
      "id": "principle_transparency",
      "name": "Transparency",
      "description": "All outputs include reasoning",
      "operationalized_as": ["reasoning_trace", "confidence_score"]
    }
  ]
}
```

### Step 2: Design state machine

```json
{
  "id": "decision_workflow_sm",
  "initial_state": "receive_input",
  "states": {
    "receive_input": {
      "id": "receive_input",
      "name": "Receive Input",
      "type": "normal",
      "allowed_transitions": ["constitutional_assessment"]
    },
    "constitutional_assessment": {
      "id": "constitutional_assessment",
      "name": "Constitutional Assessment",
      "type": "normal",
      "allowed_transitions": ["output_ready"]
    },
    "output_ready": {
      "id": "output_ready",
      "name": "Output Ready",
      "type": "terminal"
    }
  },
  "guards": [
    {
      "id": "guard_transparency",
      "condition": "reasoning_trace != null",
      "principle": "principle_transparency",
      "action_on_violation": "escalate"
    }
  ]
}
```

### Step 3: Validate and iterate

```bash
python3 scripts/validate_specula.py \
  --constitution my-constitution.json \
  --state-machine my-state-machine.json
```

If warnings appear, decide whether they are intentional design choices or defects.

## Integration Examples

### Example 1: Simple decision flow

- Constitution principles: transparency, accuracy
- State machine states: input -> assess -> decide -> output
- Guard at output: block if reasoning trace missing

### Example 2: Multi-stakeholder governance

- Stakeholders: user, operator, auditor
- Conflict resolution: priority order or weighted voting
- Escalation path: soft failure -> human review -> block output

## Common Patterns

Pattern 1: `Principle -> Constraint -> Guard -> Transition`

Pattern 2: Separate hard constraints (`block/escalate`) from soft constraints (`warn/log`).

Pattern 3: Keep transitions explicit when auditing is a requirement.

Pattern 4: Add deterministic escalation states for low-confidence or principle violations.

## FAQ

**Q: Can I validate workflows directly in v0.1?**
A: No. v0.1 validates constitutions and state machines only.

**Q: What is the difference between constraints and guards?**
A: Constraints live in the constitution (policy intent). Guards enforce checks in operational flow.

**Q: Do I need both schema and logical validation?**
A: Yes. Schema checks structure; logical checks reveal modeling issues and weak governance mappings.

**Q: Can a guard exist without a principle reference?**
A: Technically yes, but it should be justified; otherwise governance traceability weakens.

## Resources

- Templates: `templates/example-constitution.json`, `templates/example-state-machine.json`
- Schemas: `references/schemas-constitution.json`, `references/schemas-statemachine.json`
- Versioning rules: `references/versioning.md`
- Validator: `scripts/validate_specula.py`
