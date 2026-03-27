#!/usr/bin/env python3
"""
SPECULA Validation Tool (v0.1.2 / v0.2-scaffold)

Validates SPECULA governance structures against JSON schemas and consistency rules.

CAPABILITIES (v0.1):
- Constitution schema compliance
- State machine consistency checking
- Guard-to-principle mapping
- Constitution/state machine integration verification

CAPABILITIES (v0.2-scaffold — in progress):
- Workflow orchestration validation (structure only, not runtime execution)
  validate_workflow() checks: required phase sequence, prerequisite mapping,
  validation gate presence, and dual-role requirement fields.

PLANNED (v0.2 full):
- Prompt playbook generation from constitution + state machine
- Runtime wrapper bridge for framework MVP compatibility

PLANNED (v0.3+):
- Runtime execution trace validation
- Identity/memory framework validation
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, List

try:
    from jsonschema import Draft7Validator
except ImportError:  # pragma: no cover - dependency is optional at runtime
    Draft7Validator = None

class SPECULAValidator:
    """Validates SPECULA governance structures."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self._schema_warning_emitted = False

        script_dir = Path(__file__).resolve().parent
        repo_root = script_dir.parent
        self.constitution_schema_path = repo_root / "references" / "schemas-constitution.json"
        self.state_machine_schema_path = repo_root / "references" / "schemas-statemachine.json"

    def _load_json(self, path: str) -> Any:
        """Load JSON from disk and raise a ValueError with clear context on failure."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:  # pylint: disable=broad-except
            raise ValueError(f"Failed to load JSON from {path}: {e}") from e

    def _validate_schema(self, data: Any, schema_path: Path, label: str) -> bool:
        """
        Validate a JSON object against a JSON Schema when jsonschema is available.
        Returns True when valid or when schema validation is skipped.
        """
        if Draft7Validator is None:
            if not self._schema_warning_emitted:
                self.warnings.append(
                    "python package 'jsonschema' is not installed; schema validation skipped"
                )
                self._schema_warning_emitted = True
            return True

        if not schema_path.exists():
            self.warnings.append(f"Schema file not found for {label}: {schema_path}")
            return True

        try:
            schema = self._load_json(str(schema_path))
        except ValueError as e:
            self.errors.append(str(e))
            return False

        validator = Draft7Validator(schema)
        schema_errors = sorted(validator.iter_errors(data), key=lambda err: list(err.path))

        if not schema_errors:
            return True

        for err in schema_errors:
            path = ".".join(str(item) for item in err.path) or "<root>"
            self.errors.append(f"{label} schema violation at {path}: {err.message}")
        return False

    def validate_constitution(self, constitution_path: str) -> bool:
        """Validate a constitution file."""
        print(f"Validating constitution: {constitution_path}")
        try:
            constitution = self._load_json(constitution_path)
        except ValueError as e:
            self.errors.append(str(e))
            return False

        self._validate_schema(
            constitution,
            self.constitution_schema_path,
            "constitution",
        )

        # Check required fields
        required = ["constitution_id", "version", "principles"]
        for field in required:
            if field not in constitution:
                self.errors.append(f"Missing required field: {field}")

        # Validate principles structure
        if "principles" in constitution:
            for principle in constitution["principles"]:
                if "id" not in principle or "name" not in principle:
                    self.errors.append(f"Principle missing id or name: {principle}")

                # Check operationalization
                if "operationalized_as" in principle:
                    if not isinstance(principle["operationalized_as"], list):
                        self.errors.append(
                            f"Principle {principle.get('id')} must operationalize as list"
                        )
                else:
                    self.warnings.append(
                        f"Principle {principle.get('id')} not operationalized (no checks defined)"
                    )

        # Validate constraints reference principles
        if "constraints" in constitution:
            principle_ids = {p.get("id") for p in constitution.get("principles", [])}
            for constraint in constitution["constraints"]:
                if (
                    "principle" in constraint
                    and constraint["principle"] not in principle_ids
                ):
                    self.errors.append(
                        f"Constraint {constraint.get('id')} references non-existent principle: {constraint['principle']}"
                    )

        # Validate conflict resolution
        if "conflict_resolution" in constitution:
            strategy = constitution["conflict_resolution"].get("strategy")
            if strategy == "priority_order":
                if "priority_order" not in constitution["conflict_resolution"]:
                    self.errors.append(
                        "Conflict resolution strategy 'priority_order' requires priority_order field"
                    )

        # Check for cycles in principles (soft check)
        if "constraints" in constitution:
            constraint_count = len(constitution["constraints"])
            if constraint_count > 100:
                self.warnings.append(
                    f"Large number of constraints ({constraint_count}) - consider simplification"
                )

        return len(self.errors) == 0

    def validate_state_machine(self, sm_path: str) -> bool:
        """Validate a state machine file."""
        print(f"Validating state machine: {sm_path}")
        try:
            sm = self._load_json(sm_path)
        except ValueError as e:
            self.errors.append(str(e))
            return False

        self._validate_schema(
            sm,
            self.state_machine_schema_path,
            "state machine",
        )

        # Check required fields
        required = ["id", "initial_state", "states"]
        for field in required:
            if field not in sm:
                self.errors.append(f"Missing required field: {field}")

        # Validate initial state exists
        if "initial_state" in sm and "states" in sm:
            if sm["initial_state"] not in sm["states"]:
                self.errors.append(f"Initial state '{sm['initial_state']}' not defined in states")

        # Validate transitions reference existing states
        if "transitions" in sm and "states" in sm:
            state_ids = set(sm["states"].keys())
            seen_transition_ids = set()
            for transition in sm["transitions"]:
                transition_id = transition.get("id")
                if transition_id:
                    if transition_id in seen_transition_ids:
                        self.errors.append(f"Duplicate transition id found: {transition_id}")
                    seen_transition_ids.add(transition_id)

                for field in ["from_state", "to_state"]:
                    if field in transition and transition[field] not in state_ids:
                        self.errors.append(
                            f"Transition {transition.get('id')} references non-existent state: {transition[field]}"
                        )

        # Check for terminal states
        terminal_states = [
            s_id for s_id, s in sm.get("states", {}).items() if s.get("type") == "terminal"
        ]
        if not terminal_states:
            self.warnings.append("No terminal (success) states defined - may cause infinite loops")

        # Validate state transitions allowed_transitions matches actual transitions
        for state_id, state in sm.get("states", {}).items():
            allowed = state.get("allowed_transitions", [])
            if allowed:
                for allowed_state in allowed:
                    if allowed_state not in sm.get("states", {}):
                        self.errors.append(
                            f"State {state_id} references non-existent allowed state: {allowed_state}"
                        )

        # Check explicit guards have both id and principle (principle optional, but warn if missing)
        if "guards" in sm:
            for guard in sm["guards"]:
                if not guard.get("id"):
                    self.errors.append(f"Guard with missing id: {guard}")
                if not guard.get("principle"):
                    self.warnings.append(
                        f"Guard {guard.get('id')} is not linked to a constitutional principle"
                    )

        # Detect unreachable states via transition graph
        if "states" in sm and sm.get("initial_state"):
            reachable = set()
            adjacency = {state_id: set() for state_id in sm["states"].keys()}

            for state_id, state in sm["states"].items():
                for to_state in state.get("allowed_transitions", []):
                    if to_state in adjacency:
                        adjacency[state_id].add(to_state)

            for transition in sm.get("transitions", []):
                from_state = transition.get("from_state")
                to_state = transition.get("to_state")
                if from_state in adjacency and to_state in adjacency:
                    adjacency[from_state].add(to_state)

            stack = [sm["initial_state"]]
            while stack:
                current = stack.pop()
                if current in reachable:
                    continue
                reachable.add(current)
                stack.extend(adjacency.get(current, []))

            for state_id in sm["states"].keys():
                if state_id not in reachable:
                    self.warnings.append(f"State '{state_id}' is unreachable from initial_state")

        return len(self.errors) == 0

    def validate_integration(self, constitution_path: str, sm_path: str) -> bool:
        """Validate that constitution and state machine work together."""
        print("Validating constitution-state machine integration...")

        try:
            constitution = self._load_json(constitution_path)
            sm = self._load_json(sm_path)
        except ValueError as e:
            self.errors.append(str(e))
            return False

        # Check that all principles are operationalized in state machine
        principle_ids = {p.get("id") for p in constitution.get("principles", [])}
        guard_principles = {g.get("principle") for g in sm.get("guards", [])}

        for principle in principle_ids:
            if principle not in guard_principles:
                self.warnings.append(f"Principle {principle} not implemented as guard in state machine")

        # Check constraints mapped to at least one guard principle
        for constraint in constitution.get("constraints", []):
            principle = constraint.get("principle")
            if principle and principle not in guard_principles:
                self.warnings.append(
                    f"Constraint {constraint.get('id')} principle '{principle}' has no mapped guard"
                )

        return len(self.errors) == 0

    def validate_workflow(self, workflow_path: str) -> bool:
        """Validate a Specula workflow definition (v0.2-scaffold).

        A Specula workflow file is a JSON document that describes how a project
        moves through the canonical phase sequence, who the validation roles are,
        and what prerequisites must be satisfied before each phase can begin.

        This method validates the *structure* of the workflow (not runtime execution).
        Full runtime validation is planned for v0.2 final.

        Expected workflow schema (minimum):
        {
          "workflow_id": "<string>",
          "project_id": "<string>",
          "phases": [
            {
              "phase": "<phase_id>",            # must be one of SPECULA_PHASES
              "prerequisites": [...],            # list of phase_ids
              "validation_roles": [...],         # at least 2 distinct roles
              "mode": "<mode>"                   # optional, documented
            }
          ]
        }
        """
        SPECULA_PHASES = {"0", "1", "1.5", "2", "3", "4", "5", "6"}
        print(f"Validating workflow: {workflow_path}")
        try:
            workflow = self._load_json(workflow_path)
        except ValueError as e:
            self.errors.append(str(e))
            return False

        # Required top-level fields
        for field in ("workflow_id", "project_id", "phases"):
            if field not in workflow:
                self.errors.append(f"Workflow missing required field: '{field}'")

        phases = workflow.get("phases", [])
        if not isinstance(phases, list) or len(phases) == 0:
            self.errors.append("Workflow 'phases' must be a non-empty list")
            return len(self.errors) == 0

        seen_phases = set()
        for idx, phase_entry in enumerate(phases):
            if not isinstance(phase_entry, dict):
                self.errors.append(f"Workflow phases[{idx}] must be an object")
                continue

            phase_id = str(phase_entry.get("phase", "")).strip()
            if not phase_id:
                self.errors.append(f"Workflow phases[{idx}] is missing 'phase' field")
                continue

            if phase_id not in SPECULA_PHASES:
                self.errors.append(
                    f"Workflow phases[{idx}] has unknown phase '{phase_id}'. "
                    f"Valid phases: {sorted(SPECULA_PHASES)}"
                )

            if phase_id in seen_phases:
                self.errors.append(f"Workflow phases[{idx}] duplicates phase '{phase_id}'")
            seen_phases.add(phase_id)

            # Dual-role validation requirement: at least 2 distinct roles must be named
            validation_roles = phase_entry.get("validation_roles", [])
            if not isinstance(validation_roles, list):
                self.errors.append(f"Phase '{phase_id}': 'validation_roles' must be a list")
            else:
                unique_roles = {str(r).strip().lower() for r in validation_roles if str(r).strip()}
                if len(unique_roles) < 2:
                    self.errors.append(
                        f"Phase '{phase_id}': 'validation_roles' must name at least 2 distinct roles "
                        "(dual-validation requirement). Found: "
                        + str(list(unique_roles) or ["(none)"])
                    )

            # Prerequisites must reference known phases
            prerequisites = phase_entry.get("prerequisites", [])
            if not isinstance(prerequisites, list):
                self.errors.append(f"Phase '{phase_id}': 'prerequisites' must be a list")
            else:
                for prereq in prerequisites:
                    prereq_str = str(prereq).strip()
                    if prereq_str not in SPECULA_PHASES:
                        self.errors.append(
                            f"Phase '{phase_id}': prerequisite '{prereq_str}' is not a valid Specula phase"
                        )

        # Warn if Phase 5 (community co-creation) does not explicitly list dissent_protocol
        phase_5_entries = [p for p in phases if str(p.get("phase", "")).strip() == "5"]
        for p5 in phase_5_entries:
            if "dissent_protocol" not in p5:
                self.warnings.append(
                    "Phase '5' (Community Co-Creation) does not declare 'dissent_protocol'. "
                    "This field is strongly recommended to prevent theater consultation."
                )

        # Warn if Phase 6 (Guardian) does not declare re_speculation_trigger
        phase_6_entries = [p for p in phases if str(p.get("phase", "")).strip() == "6"]
        for p6 in phase_6_entries:
            if "re_speculation_trigger" not in p6:
                self.warnings.append(
                    "Phase '6' (Guardian) does not declare 're_speculation_trigger'. "
                    "Specify which divergence_level values trigger a mandatory re-speculation cycle."
                )

        return len(self.errors) == 0

    def print_report(self):
        """Print validation report."""
        print("\n" + "=" * 70)
        print("SPECULA VALIDATION REPORT")
        print("=" * 70)

        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  - {error}")

        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  - {warning}")

        if not self.errors and not self.warnings:
            print("\n✅ All validations passed!")

        print("\n" + "=" * 70)
        return len(self.errors) == 0


def main():
    parser = argparse.ArgumentParser(description="SPECULA Governance Framework Validator")
    parser.add_argument("--constitution", help="Path to constitution JSON file")
    parser.add_argument("--state-machine", help="Path to state machine JSON file")
    parser.add_argument(
        "--workflow",
        help="Path to a Specula workflow JSON file (v0.2-scaffold). "
             "Validates phase sequence, prerequisites, and dual-role requirements.",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    args = parser.parse_args()

    validator = SPECULAValidator(verbose=args.verbose)

    # Run validations
    valid = True

    if args.constitution:
        if not validator.validate_constitution(args.constitution):
            valid = False

    if args.state_machine:
        if not validator.validate_state_machine(args.state_machine):
            valid = False

    if args.constitution and args.state_machine:
        if not validator.validate_integration(args.constitution, args.state_machine):
            valid = False

    if args.workflow:
        if not validator.validate_workflow(args.workflow):
            valid = False

    validator.print_report()

    sys.exit(0 if valid else 1)


if __name__ == "__main__":
    main()
