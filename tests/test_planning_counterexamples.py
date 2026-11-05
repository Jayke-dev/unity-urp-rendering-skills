import importlib.util
import math
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    "planning", Path(__file__).resolve().parents[1] / "scripts/planning_counterexamples.py")
planning = importlib.util.module_from_spec(spec)
spec.loader.exec_module(planning)


class PlanningCounterexamples(unittest.TestCase):
    def test_regular_grids_fit_both_caps_without_using_maximum_vertices(self):
        for dimensions, expected in [((100, 23), (2300, 4356)),
                                     ((120, 20), (2400, 4522)),
                                     ((200, 12), (2400, 4378))]:
            actual = planning.grid_counts(*dimensions)
            self.assertEqual(actual, expected)
            self.assertLessEqual(actual[0], 2730)
            self.assertLessEqual(actual[1], 4540)

    def test_compatible_intervals_can_contain_the_wrong_true_order(self):
        ridge, background = (.24, .28), (.23, .27)
        self.assertTrue(ridge[0] <= .26 <= ridge[1])
        self.assertTrue(background[0] <= .25 <= background[1])
        self.assertGreater(.26, .25)
        self.assertTrue(ridge[0] <= background[1])
        self.assertEqual(planning.interval_order(ridge, background), "UNRESOLVED")

    def test_disjoint_and_touching_intervals(self):
        self.assertTrue(planning.interval_order((.1, .2), (.3, .4)).startswith("ORDER_ESTABLISHED"))
        self.assertTrue(planning.interval_order((.1, .3), (.3, .4)).startswith("ORDER_ESTABLISHED"))
        self.assertTrue(planning.interval_order((.4, .5), (.1, .3)).startswith("ORDER_CONTRADICTED"))
        self.assertEqual(planning.interval_order((.2, .4), (.3, .5)), "UNRESOLVED")

    def test_local_perspective_density_matches_independent_finite_difference(self):
        half_fov, width, step, epsilon = math.radians(50), 1200, .001, 1e-6
        def project(angle):
            return width / 2 * (1 + math.tan(angle) / math.tan(half_fov))
        for angle in (0, .2, -.4, half_fov):
            finite_difference = (project(angle + epsilon) - project(angle - epsilon)) / (2 * epsilon) * step
            actual = planning.pixels_per_angular_texel(width, half_fov, angle, step)
            self.assertAlmostEqual(actual, finite_difference, places=8)
        self.assertGreater(planning.example()["perspective_edge_to_centre_density_ratio"], 2)

    def test_invalid_domains_are_rejected(self):
        for dimensions in ((1, 3), (True, 4), (3.5, 4)):
            with self.assertRaises(ValueError):
                planning.grid_counts(*dimensions)
        for bounds in ((.5, .2), (-.1, .2), (0, 2), (0, float("nan")), (False, .2)):
            with self.assertRaises(ValueError):
                planning.interval_order(bounds, (.2, .3))
        for args in ((0, .5, 0, .1), (100, 2, 0, .1), (100, .5, 1, .1), (100, .5, 0, float("inf"))):
            with self.assertRaises(ValueError):
                planning.pixels_per_angular_texel(*args)
