---
name: specula-method
description: |
  Bilingual (IT/EN) technical implementation guide for the SPECULA governance
  framework (v0.1).

  Mandatory first question:
  - "Preferisci Italiano o English?"
  - "Do you prefer Italiano or English?"

  In scope: constitutional design, state machine patterns, guard conditions,
  governance integration patterns, and validation for constitutions/state machines.

  Out of scope (planned for v0.2+): workflow orchestration validation, prompt
  playbook generation, runtime execution frameworks, and identity/memory layers.
compatibility: |
  - AI systems architecture fundamentals
  - State machine design and control logic
  - JSON modeling and schema validation
---

# SPECULA Method - Bilingual Technical Guide (IT/EN)

## First Question / Prima Domanda

**Always start here.**

- EN: `Do you prefer Italiano or English?`
- IT: `Preferisci Italiano o English?`

After the answer:
- If `Italiano`: continue fully in Italian.
- If `English`: continue fully in English.
- If unclear/mixed: ask one short clarification and proceed.

## Scope Statement / Dichiarazione di Scope

### In Scope (v0.1) / Incluso (v0.1)

- Constitution design (principles, values, constraints)
- State machine operationalization (states, transitions, guards)
- Guard-to-principle mapping
- Multi-stakeholder governance patterns
- JSON schema validation for constitution and state machine artifacts
- Constitution/state-machine integration checks

### Out of Scope (future versions) / Fuori Scope (versioni future)

- Workflow orchestration schema/validation
- Prompt playbook templates
- Runtime execution trace validation
- Identity and memory frameworks

## Canonical Alignment / Allineamento Canonico

This skill aligns with:
- `specula-method` for public method semantics and phase narrative
- `specula-framework` for canonical runtime terminology

Current boundary in v0.1.x:
- This skill validates constitution + state-machine artifacts.
- It does not enforce runtime wrapper contracts (`meta/payload`) or phase-mode headers (`MODE | PHASE`).
- Detailed mapping is maintained in `ALIGNMENT.md`.

## Foundations / Fondamenti

EN:
SPECULA is a governance-first method for AI systems. It encodes policy intent as
operational constraints and validates consistency before deployment.

IT:
SPECULA è un metodo governance-first per sistemi AI. Traduce l'intento di policy
in vincoli operativi e verifica la coerenza prima del deployment.

Core principles / Principi chiave:
- Constitution-first design
- Operational enforcement through state logic
- Machine-readable governance artifacts
- Traceability and auditability

## AI Constitution / Costituzione AI

EN:
The constitution defines values, principles, constraints, and conflict resolution.

IT:
La costituzione definisce valori, principi, vincoli e risoluzione dei conflitti.

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

Implementation flow / Flusso di implementazione:
1. Identify stakeholder values / Identifica i valori degli stakeholder
2. Convert values into principles / Converti valori in principi
3. Operationalize with constraints / Operazionalizza con vincoli
4. Define conflict handling / Definisci gestione dei conflitti
5. Validate artifacts / Valida gli artefatti

## Control Logic & State Machines / Logica di Controllo e State Machine

EN:
State machines operationalize constitutional intent through explicit transitions and guards.

IT:
Le state machine operazionalizzano l'intento costituzionale tramite transizioni e guard esplicite.

```text
StateMachine {
  id: string
  initial_state: string
  states: map[state_id -> state]
  transitions?: [Transition]
  guards?: [Guard]
}
```

Rules / Regole:
- Transitions must target existing states
- At least one terminal state is recommended
- Guards should map to constitutional principles
- Unreachable states must be reviewed

## System Architecture / Architettura di Sistema

Typical governed flow / Flusso tipico governato:

```text
Input -> Validation -> Constitutional Assessment -> Decision -> Guard Checks -> Output
```

Recommended output fields / Campi output consigliati:
- response payload
- confidence + justification
- governance trace (checks and transitions)

## JSON Schemas / Schemi JSON

Available in v0.1 / Disponibili in v0.1:
- `references/schemas-constitution.json`
- `references/schemas-statemachine.json`

## Validation / Validazione

Use this command / Usa questo comando:

```bash
python3 scripts/validate_specula.py \
  --constitution constitution.json \
  --state-machine state-machine.json
```

Validator checks (v0.1) / Controlli validator (v0.1):
- JSON parse integrity
- Constitution schema + consistency checks
- State machine schema + consistency checks
- Integration checks (principles mapped to guards)

Exit behavior / Comportamento uscita:
- `0`: no validation errors
- `1`: one or more validation errors

## Technical Implementation Guide / Guida Tecnica di Implementazione

### Step 1 / Passo 1: Define Constitution / Definisci la Costituzione

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

### Step 2 / Passo 2: Design State Machine / Progetta la State Machine

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

### Step 3 / Passo 3: Validate and Iterate / Valida e Itera

```bash
python3 scripts/validate_specula.py \
  --constitution my-constitution.json \
  --state-machine my-state-machine.json
```

## Integration Examples / Esempi di Integrazione

Example 1 / Esempio 1: Simple decision flow
- principles: transparency, accuracy
- flow: input -> assess -> decide -> output
- output guard: block if no reasoning trace

Example 2 / Esempio 2: Multi-stakeholder governance
- stakeholders: user, operator, auditor
- conflict resolution: priority or weighted model
- escalation path: warn -> review -> block

## Common Patterns / Pattern Comuni

- `Principle -> Constraint -> Guard -> Transition`
- Separate hard vs soft constraints
- Keep transitions explicit for audits
- Add deterministic escalation states

## FAQ (IT/EN)

**Q/EN:** Can I validate workflows in v0.1?
**A/IT+EN:** No. In v0.1 validate only constitutions and state machines.

**Q/EN:** Difference between constraints and guards?
**A/IT+EN:** Constraints are policy intent in constitution; guards enforce checks in flow.

**Q/EN:** Must every guard have a principle?
**A/IT+EN:** Not mandatory, but recommended for traceability and audit clarity.

## Resources / Risorse

- Templates: `templates/example-constitution.json`, `templates/example-state-machine.json`
- Schemas: `references/schemas-constitution.json`, `references/schemas-statemachine.json`
- Versioning: `references/versioning.md`
- Validator: `scripts/validate_specula.py`
