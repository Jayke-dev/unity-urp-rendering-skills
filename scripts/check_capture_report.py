#!/usr/bin/env python3
"""Check declared aggregate render evidence; does not read images or prove GPU state."""
import argparse
import json
from pathlib import Path

METRICS = (
    "foreground_diff", "water_mask_diff", "water_colour_diff",
    "protected_diff", "gap_columns", "installed_off_diff",
)


def count(value, label):
    if type(value) is not int or value < 0:
        raise ValueError(f"{label} must be a nonnegative integer")
    return value


def check(report):
    """Return a tri-state verdict using explicit user-supplied thresholds."""
    if not isinstance(report, dict) or type(report.get("schema_version")) is not int or report["schema_version"] != 1:
        raise ValueError("schema_version must be integer 1")
    if report.get("scope") not in ("representative", "full"):
        raise ValueError("scope must be representative or full")
    required = report.get("required_view_ids")
    if not isinstance(required, list) or not required or any(not isinstance(x, str) or not x for x in required):
        raise ValueError("required_view_ids must be a nonempty list of names")
    if len(set(required)) != len(required):
        raise ValueError("required_view_ids contains duplicates")
    limits = report.get("thresholds")
    if not isinstance(limits, dict) or set(limits) != set(METRICS):
        raise ValueError("thresholds must explicitly specify each documented metric")
    for key in METRICS:
        count(limits[key], f"thresholds.{key}")
    flags = report.get("capture_integrity")
    if not isinstance(flags, dict):
        raise ValueError("capture_integrity missing")
    holds, failures, improvements = [], [], []
    for key in ("same_reference", "descriptors_unchanged", "all_subjects_before_masks"):
        if type(flags.get(key)) is not bool:
            raise ValueError(f"capture_integrity.{key} must be boolean")
        if not flags[key]:
            holds.append(f"capture integrity not established: {key}")
    views = report.get("views")
    if not isinstance(views, list) or not views:
        raise ValueError("views must be nonempty")
    names = []
    for view in views:
        if not isinstance(view, dict) or not isinstance(view.get("id"), str) or not view["id"]:
            raise ValueError("each view needs a nonempty id")
        name = view["id"]
        if name in names:
            raise ValueError("duplicate captured view id")
        if name not in required:
            raise ValueError(f"unexpected captured view: {name}")
        names.append(name)
        control = count(view.get("control_foreground_diff"), f"{name}.control_foreground_diff")
        for key in METRICS:
            value = count(view.get(key), f"{name}.{key}")
            if value > limits[key]:
                failures.append(f"{name}: {key}={value} exceeds {limits[key]}")
        for key in ("baseline_repeat_diff", "trial_repeat_diff"):
            if count(view.get(key), f"{name}.{key}") != 0:
                holds.append(f"{name}: {key} nonzero; comparison stability unresolved")
        if view["foreground_diff"] < control:
            improvements.append({"view": name, "control": control, "trial": view["foreground_diff"]})
    if set(names) != set(required):
        holds.append("required view coverage incomplete")
    for key in ("cleanup", "visual_quality"):
        value = report.get(key)
        if value not in ("pass", "fail", "pending"):
            raise ValueError(f"{key} must be pass, fail or pending")
        if value == "fail":
            failures.append(f"{key} failed")
        elif value == "pending":
            holds.append(f"{key} pending")
    comparison_valid = not any(
        "capture integrity" in x or "stability" in x or "coverage" in x for x in holds
    )
    if not comparison_valid:
        verdict = "HOLD"
    elif failures:
        verdict = "FAIL"
    elif holds or report["scope"] != "full":
        verdict = "HOLD"
    else:
        verdict = "PASS_REPORTED_GATES"
    if report["scope"] != "full":
        holds.append("representative cohort cannot establish full-view acceptance")
    return {
        "verdict": verdict,
        "comparison_valid_from_report": comparison_valid,
        "reported_partial_improvements": improvements if comparison_valid else [],
        "failures": failures,
        "holds": holds,
        "limit": "Checks supplied aggregate claims only; no independent image, scene, GPU or device verification.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    try:
        result = check(json.loads(args.report.read_text(encoding="utf-8")))
    except (ValueError, OSError) as exc:
        result = {"verdict": "HOLD", "input_error": str(exc)}
    print(json.dumps(result, indent=2))
    return {"PASS_REPORTED_GATES": 0, "FAIL": 1, "HOLD": 2}[result["verdict"]]


if __name__ == "__main__":
    raise SystemExit(main())
