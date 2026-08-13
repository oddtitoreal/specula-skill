"""Semantic coverage tests for SPECULA skill examples.

These go beyond JSON-schema validity: they assert that every constitutional
principle and constraint in the *real* examples is actually enforced by a guard
that is attached to the runtime flow (a transition). This is the
principle -> constraint -> guard -> transition chain the skill promises.
"""
import importlib.util
import json
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
EXAMPLES = REPO / "examples"

# Load the validator module directly from scripts/ (no package install needed).
_spec = importlib.util.spec_from_file_location(
    "validate_specula", REPO / "scripts" / "validate_specula.py"
)
validate_specula = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(validate_specula)
SPECULAValidator = validate_specula.SPECULAValidator


def _example_dirs():
    return sorted(p for p in EXAMPLES.iterdir()
                  if p.is_dir() and (p / "constitution.json").exists()
                  and (p / "state-machine.json").exists())


def _run_validation(example_dir: Path):
    v = SPECULAValidator()
    const = str(example_dir / "constitution.json")
    sm = str(example_dir / "state-machine.json")
    v.validate_constitution(const)
    v.validate_state_machine(sm)
    v.validate_integration(const, sm)
    return v


def _is_real(example_dir: Path) -> bool:
    sm = json.loads((example_dir / "state-machine.json").read_text(encoding="utf-8"))
    return sm.get("metadata", {}).get("fictional_example") is False


REAL_EXAMPLES = [p for p in _example_dirs() if _is_real(p)]


@pytest.mark.parametrize("example_dir", REAL_EXAMPLES, ids=lambda p: p.name)
def test_all_constitutional_principles_have_guards(example_dir):
    v = _run_validation(example_dir)
    offenders = [w for w in v.warnings if "not implemented as guard" in w]
    assert not offenders, f"{example_dir.name}: {offenders}"


@pytest.mark.parametrize("example_dir", REAL_EXAMPLES, ids=lambda p: p.name)
def test_all_constraints_have_direct_guard_mapping(example_dir):
    v = _run_validation(example_dir)
    offenders = [w for w in v.warnings
                 if "no directly mapped guard" in w or "has no mapped guard" in w]
    assert not offenders, f"{example_dir.name}: {offenders}"


@pytest.mark.parametrize("example_dir", REAL_EXAMPLES, ids=lambda p: p.name)
def test_real_examples_have_zero_warnings(example_dir):
    v = _run_validation(example_dir)
    assert not v.errors, f"{example_dir.name} errors: {v.errors}"
    assert not v.warnings, f"{example_dir.name} warnings: {v.warnings}"


def test_habitability_guards_are_attached_to_runtime_flow():
    sm = json.loads(
        (EXAMPLES / "community-space-brand" / "state-machine.json").read_text(encoding="utf-8")
    )
    attached = {
        guard_id
        for transition in sm["transitions"]
        for guard_id in transition.get("guard_ids", [])
    }
    assert "guard_relational_quality" in attached
    assert "guard_activation_color_ratio" in attached
    assert "guard_living_community" in attached


def test_real_examples_exist():
    # Guard against silently testing nothing if the metadata flag changes.
    assert REAL_EXAMPLES, "no real (non-fictional) examples found to test"


def test_activation_color_ratio_respected_in_space_states():
    """Data must obey the hard constraint that guard_activation_color_ratio enforces:
    red (activation) never exceeds 5% in any declared space state."""
    sm = json.loads(
        (EXAMPLES / "community-space-brand" / "state-machine.json").read_text(encoding="utf-8")
    )
    offenders = {
        name: cfg["color_weight"].get("red", 0.0)
        for name, cfg in sm.get("space_states", {}).items()
        if cfg.get("color_weight", {}).get("red", 0.0) > 0.05
    }
    assert not offenders, f"space states exceeding 5% red: {offenders}"
