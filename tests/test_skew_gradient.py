import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    "skew_example", Path(__file__).resolve().parents[1] / "scripts/skew_gradient_counterexample.py"
)
example = importlib.util.module_from_spec(spec)
spec.loader.exec_module(example)


class SkewGradientTests(unittest.TestCase):
    def test_known_x_plane_rejects_orthogonal_assumption(self):
        du, dv = (1, 0), (1, 1)
        self.assertEqual(example.world_gradient(du, dv, 1, 1), (1, 0))
        wrong = example.incorrect_orthogonal_assumption(du, dv, 1, 1)
        self.assertAlmostEqual(wrong[0], 1.5)
        self.assertAlmostEqual(wrong[1], 0.5)

    def test_independent_plane_derivatives_on_rotated_scaled_skew_frames(self):
        expected = (2.25, -3.5)
        for du, dv in [((2, 1), (-1, 3)), ((1, 4), (3, 2)), ((-2, 0), (1, 0.5))]:
            with self.subTest(du=du, dv=dv):
                hu = sum(a * b for a, b in zip(expected, du))
                hv = sum(a * b for a, b in zip(expected, dv))
                actual = example.world_gradient(du, dv, hu, hv)
                for got, want in zip(actual, expected):
                    self.assertAlmostEqual(got, want)

    def test_nonuniform_orthogonal_frame_and_zero_field(self):
        self.assertEqual(example.world_gradient((2, 0), (0, 5), 6, -10), (3, -2))
        self.assertEqual(example.world_gradient((2, 1), (1, 3), 0, 0), (0, 0))

    def test_wrong_method_agrees_when_axes_really_are_orthogonal(self):
        du, dv = (3, 4), (-8, 6)
        correct = example.world_gradient(du, dv, 7, -2)
        wrong = example.incorrect_orthogonal_assumption(du, dv, 7, -2)
        for a, b in zip(correct, wrong):
            self.assertAlmostEqual(a, b)

    def test_singular_and_unrepresentable_determinants_are_rejected(self):
        for du, dv in [((1, 2), (2, 4)), ((0, 0), (1, 0)), ((1e308, 0), (0, 1e308))]:
            with self.assertRaises(ValueError):
                example.world_gradient(du, dv, 1, 1)

    def test_missing_malformed_and_nonfinite_inputs_are_rejected(self):
        for bad in (None, [], [1], [1, 2, 3], [True, 1], [float("nan"), 1], [1, "x"]):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                example.world_gradient(bad, (0, 1), 1, 1)
        for bad in (True, float("inf"), "1", 10**1000):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                example.world_gradient((1, 0), (0, 1), bad, 0)

    def test_nonfinite_result_is_rejected(self):
        with self.assertRaises(ValueError):
            example.world_gradient((1e-308, 0), (0, 1), 10, 0)
