"""Criteria as hypotheses (v0.3): values stay fixed, the criteria that translate them are tested."""
import importlib.util
import json
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location(
    "validate_specula", REPO / "scripts" / "validate_specula.py"
)
validate_specula = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(validate_specula)
SPECULAValidator = validate_specula.SPECULAValidator


def _constitution(constraints, opted_in=True):
    data = {
        "constitution_id": "test_brand",
        "version": "1.0.0",
        "principles": [
            {"id": "principle_care", "name": "Care", "description": "d", "operationalized_as": ["care_check"]}
        ],
        "constraints": constraints,
    }
    if opted_in:
        data["criteria_as_hypotheses"] = True
    return data


def _validate(tmp_path, data, reference=None):
    path = tmp_path / "constitution.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    validator = SPECULAValidator(review_reference_date=reference)
    ok = validator.validate_constitution(str(path))
    return ok, validator


def _soft(**extra):
    base = {"id": "constraint_slow_programming", "constraint_type": "soft",
            "rule": "Prefer slow programming", "principle": "principle_care"}
    base.update(extra)
    return base


def test_hard_constraint_cannot_be_a_hypothesis(tmp_path):
    hard = {"id": "constraint_red_line", "constraint_type": "hard", "rule": "Never X",
            "principle": "principle_care", "status": "hypothesis"}
    ok, validator = _validate(tmp_path, _constitution([hard]))
    assert not ok
    assert any("red line" in e for e in validator.errors)


def test_opted_in_criterion_without_expected_effect_warns(tmp_path):
    ok, validator = _validate(tmp_path, _constitution([_soft()]))
    assert ok
    assert any("expected_effect" in w for w in validator.warnings)


def test_criterion_without_opt_in_is_not_checked(tmp_path):
    ok, validator = _validate(tmp_path, _constitution([_soft()], opted_in=False))
    assert ok
    assert not any("expected_effect" in w for w in validator.warnings)


def test_overdue_review_is_reported_only_with_reference_date(tmp_path):
    criterion = _soft(status="hypothesis", expected_effect="More returns",
                      review_date="2026-01-31", observed_effect=None)
    _, without_reference = _validate(tmp_path, _constitution([criterion]))
    assert not any("overdue" in w for w in without_reference.warnings)

    _, with_reference = _validate(tmp_path, _constitution([criterion]), date(2026, 3, 1))
    assert any("overdue" in w for w in with_reference.warnings)


def test_reviewed_criterion_is_not_overdue(tmp_path):
    criterion = _soft(status="confirmed", expected_effect="More returns",
                      review_date="2026-01-31", observed_effect="Returns up 12%")
    _, validator = _validate(tmp_path, _constitution([criterion]), date(2026, 3, 1))
    assert not any("overdue" in w for w in validator.warnings)
