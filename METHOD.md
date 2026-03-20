# SPECULA Method: Design Framework

## Overview

SPECULA method translates constitutional intent into operational governance.

## Three-Step Process

### Step 1: Define Constitutional Identity

Clarify what the AI system should preserve and how stakeholders prioritize values.

Outputs:
- principles
- constraints
- stakeholder model
- conflict resolution strategy

### Step 2: Operationalize as State Machine

Map principles to states, transitions, and guards.

Outputs:
- state machine flow
- guard checks bound to principles
- escalation paths for violations

### Step 3: Validate and Iterate

Verify structure, consistency, and constitution/state-machine alignment.

Outputs:
- validation report
- integration gaps
- refined governance artifacts

## Core Patterns

### Pattern 1: Constitutional Mapping

`Principle -> Constraint -> Guard -> Transition`

### Pattern 2: Multi-Stakeholder Alignment

Resolve conflicts using:
- priority order
- weighted voting
- escalation to human decision

### Pattern 3: Failure Recovery

On guard violation choose explicit behavior:
- log/warn
- block
- escalate
- retry

## Implementation References

- Templates: `templates/`
- Schemas: `references/`
- Validator: `scripts/validate_specula.py`
- Technical detail: `SKILL.md`
