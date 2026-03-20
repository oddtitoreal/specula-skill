---
name: specula-method
description: |
  Comprehensive technical guide to SPECULA — a systematic framework for AI governance, control logic, and operational architecture. Use this skill whenever users need to: implement SPECULA governance structures, design AI constitutions and state machines, work with JSON schemas and system specifications, validate SPECULA compliance, architect multi-phase AI workflows, or understand foundational governance principles. Triggers include: references to "SPECULA", "AI constitution", "control logic", "state machine governance", "operational protocols", "system architecture for AI", governance design patterns, or any technical governance/control framework for AI systems. Ideal for researchers, architects, and practitioners designing governed AI systems.
compatibility: |
  - Deep technical understanding of AI systems architecture
  - Knowledge of state machines and control systems
  - Familiarity with JSON schema validation
  - Systems thinking for multi-phase workflows
---

# SPECULA Method Technical Reference

SPECULA is a comprehensive framework for **governance, control, and operational architecture** of AI systems. It provides systematic approaches to constitution-based governance, state machine control logic, and technical implementation specifications.

## Quick Navigation

- **[Foundations](#foundations)** — Conceptual underpinnings and governance principles
- **[AI Constitution](#ai-constitution)** — Values, principles, behavioral specifications
- **[Control Logic & State Machines](#control-logic--state-machines)** — Operational governance
- **[System Architecture](#system-architecture)** — Input/output specifications and flows
- **[JSON Schemas](#json-schemas)** — Machine-readable specifications
- **[Prompt Playbook](#prompt-playbook)** — Practical implementation templates
- **[Technical Implementation Guide](#technical-implementation-guide)** — Step-by-step integration

---

## Foundations

SPECULA rests on core principles:

### Core Philosophy
- **Constitution-First Design**: Explicit governance structures precede implementation
- **Control Through Logic**: State machines enforce governance rules operationally
- **Layered Specification**: From high-level principles to machine-readable schemas
- **Versioning & Precedence**: Clear governance rules for specification conflicts

### Key Concepts

**The Specula Stack** (from abstract to concrete):
1. Conceptual Principles (why)
2. AI Constitution (what values/behaviors)
3. State Machine Logic (how control flows)
4. System Architecture (technical implementation)
5. JSON Schemas (machine validation)
6. Prompt Templates (operational execution)

---

## AI Constitution

An AI Constitution in SPECULA defines:

### Structure
```
Constitution {
  principles: [Principle]
  values: [Value]
  constraints: [Constraint]
  behavioral_specs: [BehavioralSpec]
  failure_modes: [FailureMode]
}
```

### Example Components

**Principle Example**:
- Name: "Transparency in Reasoning"
- Description: "AI must articulate its decision process"
- Enforcement: State machine checkpoint requiring reasoning trace

**Value Example**:
- Core belief about what matters (e.g., "User autonomy", "System reliability")
- Operationalized as constraints in state machines

**Constraint Example**:
- Bounds on behavior (e.g., "Cannot override user preferences without explicit consent")
- Checked at state transitions

### Implementation

To create a constitution:
1. **Identify stakeholder values** — what principles matter?
2. **Formalize as constraints** — how do principles restrict behavior?
3. **Map to state transitions** — where do constraints apply?
4. **Define failure modes** — what happens if violated?
5. **Test against scenarios** — does it work in practice?

---

## Control Logic & State Machines

SPECULA uses **finite state machines** as the operational enforcement layer for governance.

### State Machine Architecture

```
StatesMachine {
  initial_state: State
  states: {
    state_name: State
  }
  transitions: [Transition]
  guards: [Guard]
  actions: [Action]
}
```

### State Definition
```json
{
  "id": "state_identifier",
  "name": "Descriptive Name",
  "type": "normal|terminal|error",
  "entry_actions": ["action1", "action2"],
  "exit_guards": [
    {
      "condition": "constraint to check",
      "on_fail": "action_or_state"
    }
  ],
  "allowed_transitions": ["state_a", "state_b"]
}
```

### Guard Conditions

Guards enforce constitutional constraints at state transitions:

```json
{
  "id": "guard_transparency_check",
  "applies_at": "decision_output",
  "condition": "reasoning_trace != null AND confidence_score > threshold",
  "action_on_violation": "escalate_to_human_review",
  "error_message": "Cannot output decision without reasoning trace"
}
```

### Transition Definition
```json
{
  "id": "transition_process_to_decision",
  "from_state": "processing",
  "to_state": "decision_output",
  "trigger": "processing_complete",
  "preconditions": ["all_guards_pass"],
  "actions": ["log_decision", "record_timestamp"]
}
```

### Multi-Phase Workflows

SPECULA workflows are sequences of state machines:

```json
{
  "workflow_id": "governance_workflow_v1",
  "phases": [
    {
      "phase": 1,
      "name": "input_validation",
      "state_machine": "input_validation_sm",
      "on_success": "proceed_to_phase_2",
      "on_failure": "escalate"
    },
    {
      "phase": 2,
      "name": "decision_logic",
      "state_machine": "decision_logic_sm",
      "constitutional_checks": ["transparency", "consistency"]
    },
    {
      "phase": 3,
      "name": "output_generation",
      "state_machine": "output_sm",
      "constitutional_checks": ["user_autonomy", "harm_prevention"]
    }
  ]
}
```

---

## System Architecture

### Input Specification

SPECULA defines structured inputs:

```json
{
  "input_schema": {
    "request_id": "UUID",
    "timestamp": "ISO8601",
    "user_context": {
      "user_id": "string",
      "permissions": ["list"],
      "preferences": {}
    },
    "query": {
      "content": "string",
      "type": "query_type",
      "context_tags": ["tag1", "tag2"],
      "constitutional_scope": ["principle1", "principle2"]
    },
    "constraints": {
      "max_reasoning_depth": "integer",
      "required_confidence": "float[0,1]",
      "escalation_thresholds": {}
    }
  }
}
```

### Output Architecture

Governed outputs include:

```json
{
  "output_schema": {
    "request_id": "UUID",
    "timestamp": "ISO8601",
    "response": {
      "content": "string",
      "type": "response_type",
      "confidence": "float[0,1]"
    },
    "governance_trace": {
      "constitutional_checks": [
        {
          "check_id": "transparency_check_1",
          "passed": true,
          "reasoning": "Decision includes reasoning trace"
        }
      ],
      "guards_applied": ["guard_1", "guard_2"],
      "state_transitions": ["state_a", "state_b", "state_c"]
    },
    "reasoning": {
      "decision_logic": "string",
      "alternatives_considered": ["alt1", "alt2"],
      "confidence_justification": "string"
    },
    "metadata": {
      "processing_time_ms": "integer",
      "model_version": "string",
      "framework_version": "SPECULA_v2.3"
    }
  }
}
```

### Data Flow

```
Input Validation → Constitutional Assessment → Decision Logic → Guard Checks → Output Generation → Governance Trace
```

---

## JSON Schemas

SPECULA governance is machine-readable via JSON schemas.

### Constitution Schema
See `references/schemas-constitution.json` for the full schema defining:
- Principles structure
- Values definition
- Constraints specification
- Behavioral requirements
- Failure mode definitions

### State Machine Schema
See `references/schemas-statemachine.json` for:
- State definitions
- Transition rules
- Guard conditions
- Action specifications

### Workflow Schema
See `references/schemas-workflow.json` for:
- Multi-phase orchestration
- Phase dependencies
- Constitutional mappings

### Validation

To validate a system against SPECULA:
```bash
python scripts/validate_specula.py \
  --constitution constitution.json \
  --state_machine sm.json \
  --workflow workflow.json
```

---

## Prompt Playbook

SPECULA provides **system prompts and phase templates** for operational implementation.

### System Prompt Template

```
You are operating under the SPECULA governance framework.

Constitution Principles:
{CONSTITUTION.PRINCIPLES}

Current State: {CURRENT_STATE}
Allowed Transitions: {ALLOWED_TRANSITIONS}

Required Checks:
{REQUIRED_GUARDS}

Output Format:
{OUTPUT_SCHEMA}

Constraints:
- All decisions MUST include reasoning trace
- Confidence scores must be justified
- Constitutional violations trigger escalation
```

### Phase Prompts

**Phase 1: Input Validation**
- Validate input against schema
- Check user permissions
- Identify constitutional scope

**Phase 2: Decision Logic**
- Apply decision rules
- Generate alternatives
- Calculate confidence

**Phase 3: Constitutional Checks**
- Verify all guards pass
- Check principle alignment
- Log governance trace

**Phase 4: Output Generation**
- Format per output schema
- Include reasoning
- Prepare escalation if needed

See `templates/prompt-playbook-v1.md` for full templates.

---

## Technical Implementation Guide

### Step 1: Define Your Constitution

Start by articulating governance principles:

```json
{
  "constitution": {
    "id": "my_system_v1",
    "principles": [
      {
        "id": "principle_transparency",
        "name": "Transparency in Decision-Making",
        "description": "All outputs must include reasoning",
        "operationalized_as": ["reasoning_trace_required", "confidence_justification"]
      }
    ],
    "version": "1.0"
  }
}
```

### Step 2: Design State Machines

Map each operational phase:

```json
{
  "id": "decision_flow_sm",
  "initial_state": "input_received",
  "states": {
    "input_received": {
      "entry_actions": ["log_input", "validate_schema"],
      "allowed_transitions": ["validation_passed", "validation_failed"]
    },
    "validation_passed": {
      "allowed_transitions": ["constitutional_assessment"]
    },
    "constitutional_assessment": {
      "entry_actions": ["apply_guards", "check_principles"],
      "allowed_transitions": ["checks_passed", "checks_failed"]
    },
    "decision_generation": {
      "entry_actions": ["invoke_logic"],
      "allowed_transitions": ["output_ready"]
    },
    "output_ready": {
      "type": "terminal",
      "entry_actions": ["format_output", "record_trace"]
    },
    "validation_failed": {
      "type": "error",
      "entry_actions": ["escalate", "log_error"]
    }
  },
  "transitions": [
    {
      "from": "input_received",
      "to": "validation_passed",
      "trigger": "schema_valid AND permissions_ok",
      "actions": ["advance"]
    },
    {
      "from": "validation_passed",
      "to": "constitutional_assessment",
      "trigger": "proceed",
      "guards": [{"condition": "all_fields_present"}]
    }
  ]
}
```

### Step 3: Integrate Governance Checks

Map constitutional principles to guards:

```json
{
  "guards": [
    {
      "id": "guard_transparency",
      "principle": "principle_transparency",
      "check": "reasoning_trace != null AND confidence_score >= 0.7",
      "on_fail": "request_human_review"
    },
    {
      "id": "guard_consistency",
      "principle": "principle_consistency",
      "check": "decision_aligns_with_history AND no_contradictions",
      "on_fail": "flag_for_review"
    }
  ]
}
```

### Step 4: Implement Output Governance

Ensure all outputs include governance trace:

```json
{
  "response": {
    "content": "...",
    "governance_trace": {
      "constitutional_audit": [
        {"check": "transparency", "status": "pass"},
        {"check": "consistency", "status": "pass"}
      ],
      "state_path": ["input_received", "validation_passed", "constitutional_assessment", "decision_generation"],
      "guards_applied": ["guard_transparency", "guard_consistency"],
      "timestamp": "2026-01-15T10:30:00Z"
    }
  }
}
```

### Step 5: Validate and Test

Use provided validation scripts:

```bash
# Validate schema compliance
python scripts/validate_specula.py --constitution constitution.json

# Test state machine transitions
python scripts/test_state_machine.py --sm state_machine.json

# Full system test
python scripts/test_workflow.py --workflow workflow.json
```

---

## Common Patterns

### Pattern 1: Multi-Stakeholder Governance

When multiple stakeholders have different principles:

```json
{
  "constitution": {
    "stakeholders": ["admin", "user", "auditor"],
    "principles": {
      "admin": ["system_stability", "efficiency"],
      "user": ["autonomy", "transparency"],
      "auditor": ["compliance", "auditability"]
    },
    "conflict_resolution": "weighted_voting"
  }
}
```

### Pattern 2: Escalation Chains

Define what happens when guards fail:

```json
{
  "escalation_policy": {
    "level_1": "log_and_continue",
    "level_2": "flag_for_review",
    "level_3": "request_human_intervention",
    "level_4": "block_and_alert"
  }
}
```

### Pattern 3: Audit Trails

Ensure complete traceability:

```json
{
  "audit_requirements": {
    "log_all_transitions": true,
    "record_guards_evaluated": true,
    "capture_reasoning": true,
    "timestamp_precision": "millisecond"
  }
}
```

---

## Resources

- **Full Schemas**: See `references/` directory for JSON schemas
- **Templates**: See `templates/` directory for example payloads
- **Validation Scripts**: See `scripts/` directory for tooling
- **Official Repo**: https://github.com/oddtitoreal/specula-framework

## Versioning

This skill reflects **SPECULA Method v2.3** and follows the framework's precedence and versioning rules.

For version history, see `references/versioning.md`.

---

## Integration Examples

### Example 1: Simple Decision System

```json
{
  "constitution": {
    "principles": ["transparency", "accuracy"]
  },
  "state_machine": {
    "states": ["receive_input", "validate", "decide", "output"],
    "guards": [
      {"state": "output", "check": "confidence > 0.8"}
    ]
  }
}
```

### Example 2: Complex Multi-Phase Workflow

```json
{
  "workflow": {
    "phases": [
      {"name": "intake", "sm": "intake_sm"},
      {"name": "analysis", "sm": "analysis_sm", "requires": ["transparency_check"]},
      {"name": "decision", "sm": "decision_sm"},
      {"name": "delivery", "sm": "delivery_sm", "guard": "guard_final_audit"}
    ]
  }
}
```

---

## FAQ & Troubleshooting

**Q: How do I handle conflicting constitutional principles?**
A: Use the Conflict Resolution system defined in your constitution. SPECULA supports weighted voting, priority ordering, or stakeholder arbitration.

**Q: Can I modify state machines at runtime?**
A: No — SPECULA enforces schema validation to prevent unauthorized modifications. Changes require formal versioning and re-validation.

**Q: How do I audit a system for SPECULA compliance?**
A: Use `scripts/validate_specula.py` and review the governance trace in outputs. All decisions must include full constitutional audit logs.

**Q: What's the difference between guards and constraints?**
A: **Guards** are operational checks at state transitions. **Constraints** are semantic bounds defined in the constitution.

---

## Next Steps

1. **Define your constitution** — articulate governance principles
2. **Design state machines** — map operational flows
3. **Validate schemas** — ensure compliance
4. **Test workflows** — verify behavior
5. **Deploy with audit** — capture all governance traces
6. **Iterate** — refine based on operational feedback

For detailed implementation, see the referenced documents in this skill.
