import copy
import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


capture = load("check_capture_report")
geometry = load("geometry_counterexamples")
replay = load("replay_evidence_counterexamples")


class CaptureTests(unittest.TestCase):
    def setUp(self):
        self.report = json.loads((ROOT / "examples/partial-repair.json").read_text())

    def clean(self):
        self.report["scope"] = "full"
        self.report["visual_quality"] = "pass"
        for view in self.report["views"]:
            view["foreground_diff"] = 0

    def test_partial_effect_is_not_acceptance(self):
        result = capture.check(self.report)
        self.assertEqual(result["verdict"], "FAIL")
        self.assertEqual(len(result["reported_partial_improvements"]), 2)

    def test_shifted_baseline_makes_comparison_inconclusive(self):
        self.report["capture_integrity"]["same_reference"] = False
        result = capture.check(self.report)
        self.assertEqual(result["verdict"], "HOLD")
        self.assertEqual(result["reported_partial_improvements"], [])

    def test_repeat_noise_is_retained(self):
        self.report["views"][0]["baseline_repeat_diff"] = 2
        self.assertEqual(capture.check(self.report)["verdict"], "HOLD")

    def test_complete_declared_contract_can_pass(self):
        self.clean()
        self.assertEqual(capture.check(self.report)["verdict"], "PASS_REPORTED_GATES")

    def test_clean_representative_cohort_cannot_claim_full_acceptance(self):
        self.clean()
        self.report["scope"] = "representative"
        self.assertEqual(capture.check(self.report)["verdict"], "HOLD")

    def test_missing_view_cannot_pass(self):
        self.clean()
        self.report["views"].pop()
        self.assertEqual(capture.check(self.report)["verdict"], "HOLD")

    def test_off_baseline_failure_remains_visible(self):
        self.clean()
        self.report["views"][0]["installed_off_diff"] = 1
        self.assertEqual(capture.check(self.report)["verdict"], "FAIL")

    def test_pending_quality_prevents_pass(self):
        self.clean()
        self.report["visual_quality"] = "pending"
        self.assertEqual(capture.check(self.report)["verdict"], "HOLD")

    def test_explicit_user_tolerances_are_respected(self):
        self.clean()
        self.report["thresholds"]["foreground_diff"] = 3
        self.report["views"][0]["foreground_diff"] = 3
        self.assertEqual(capture.check(self.report)["verdict"], "PASS_REPORTED_GATES")

    def test_invalid_counts_and_missing_metrics_do_not_pass(self):
        for value in (True, -1, 1.5, float("nan"), "0", None):
            with self.subTest(value=value):
                report = copy.deepcopy(self.report)
                report["views"][0]["foreground_diff"] = value
                with self.assertRaises(ValueError):
                    capture.check(report)
        del self.report["views"][0]["water_mask_diff"]
        with self.assertRaises(ValueError):
            capture.check(self.report)

    def test_duplicate_views_are_invalid(self):
        self.report["views"].append(copy.deepcopy(self.report["views"][0]))
        with self.assertRaises(ValueError):
            capture.check(self.report)

    def test_cli_exit_codes_and_machine_readable_invalid_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "report.json"
            for expected, body in ((1, json.dumps(self.report)), (2, "[]"), (2, "bad json")):
                path.write_text(body)
                run = subprocess.run([sys.executable, str(ROOT / "scripts/check_capture_report.py"), str(path)], capture_output=True, text=True)
                self.assertEqual(run.returncode, expected)
                self.assertIn("verdict", json.loads(run.stdout))
            self.clean()
            path.write_text(json.dumps(self.report))
            run = subprocess.run([sys.executable, str(ROOT / "scripts/check_capture_report.py"), str(path)], capture_output=True, text=True)
            self.assertEqual(run.returncode, 0)


class GeometryTests(unittest.TestCase):
    def test_horizontal_and_downward_rays_cannot_reach_higher_floor(self):
        self.assertTrue(geometry.above_floor_ray_impossible(1, 0, 4))
        self.assertTrue(geometry.above_floor_ray_impossible(1, -1, 4))

    def test_upward_and_boundary_cases_are_not_declared_impossible(self):
        self.assertFalse(geometry.above_floor_ray_impossible(1, 1, 4))
        self.assertFalse(geometry.above_floor_ray_impossible(4, 0, 4))
        self.assertFalse(geometry.above_floor_ray_impossible(5, -1, 4))

    def test_polygon_circle_gap_is_real(self):
        inner = geometry.polygon_inradius(10, 6)
        witness = (inner + 10) / 2
        # Edge x=R*cos(pi/n), polygon extends toward x=0.
        self.assertGreater(witness, inner)
        self.assertLess(witness, 10)
        self.assertAlmostEqual(inner, 5 * math.sqrt(3))

    def test_nonfinite_or_degenerate_input_rejected(self):
        for value in (float("nan"), float("inf"), True):
            with self.assertRaises(ValueError):
                geometry.above_floor_ray_impossible(value, 0, 4)
        for sides in (0, 2, 3.5, True):
            with self.assertRaises(ValueError):
                geometry.polygon_inradius(10, sides)


class ReplayEvidenceTests(unittest.TestCase):
    def test_same_colour_write_is_invisible_to_last_transition(self):
        result = replay.colour_transition_vs_writer("black", [("a", "red"), ("b", "red")])
        self.assertEqual(result["last_colour_transition"], "a")
        self.assertEqual(result["last_writer"], "b")

    def test_outside_anchor_change_is_not_a_positive_control(self):
        before, after = ["red", "black"], ["red", "white"]
        self.assertNotEqual(before, after)
        self.assertEqual(replay.anchors_changed(before, after, [0]), 0)
        self.assertEqual(replay.anchors_changed(before, after, [1]), 1)

    def test_partial_enable_failure_cleans_up_and_preserves_exception(self):
        state = replay.PartialEnable()
        with self.assertRaisesRegex(RuntimeError, "side effect"):
            replay.enable_attempt_with_cleanup(state)
        self.assertFalse(state.enabled)

    def test_existing_ownership_is_not_claimed_or_disabled(self):
        state = replay.PartialEnable()
        state.enabled = True
        with self.assertRaises(ValueError):
            replay.enable_attempt_with_cleanup(state)
        self.assertTrue(state.enabled)

    def test_empty_or_invalid_anchors_are_not_accepted(self):
        for anchors in ([], [-1], [1], [True]):
            with self.assertRaises(ValueError):
                replay.anchors_changed(["a"], ["b"], anchors)
