#!/usr/bin/env python3
"""Synthetic planning/evidence counterexamples; no Unity or image certification."""
import json
import math


def grid_counts(columns, rows):
    if any(type(n) is not int or n < 2 for n in (columns, rows)):
        raise ValueError("grid dimensions must be integers >= 2")
    return columns * rows, 2 * (columns - 1) * (rows - 1)


def interval_order(ridge, background):
    """Order of two independent scalar intervals, not ownership of MSAA samples."""
    for bounds in (ridge, background):
        if not isinstance(bounds, (tuple, list)) or len(bounds) != 2:
            raise ValueError("two endpoints required")
        if any(type(x) not in (int, float) or not math.isfinite(x) for x in bounds):
            raise ValueError("finite numeric endpoints required")
        if not 0 <= bounds[0] <= bounds[1] <= 1:
            raise ValueError("ordered weights in [0, 1] required")
    if ridge[1] <= background[0]:
        return "ORDER_ESTABLISHED_UNDER_ASSUMPTIONS"
    if ridge[0] > background[1]:
        return "ORDER_CONTRADICTED_UNDER_ASSUMPTIONS"
    return "UNRESOLVED"


def pixels_per_angular_texel(width, half_fov, theta, angular_step):
    """Horizontal perspective derivative; all angles in radians, step local/small."""
    values = (width, half_fov, theta, angular_step)
    if any(type(x) not in (int, float) or not math.isfinite(x) for x in values):
        raise ValueError("finite numeric inputs required")
    if width <= 0 or not 0 < half_fov < math.pi / 2 or abs(theta) > half_fov or angular_step <= 0:
        raise ValueError("invalid perspective domain")
    return width * angular_step / (2 * math.tan(half_fov) * math.cos(theta) ** 2)


def example():
    # Invented uncertainty ranges contain true ridge=.26 > background=.25.
    ridge, background = (.24, .28), (.23, .27)
    half_fov = math.radians(50)
    return {
        "scope": "Synthetic arithmetic only; not a scene, render or coverage certificate",
        "grid_under_caps": {"vertices": grid_counts(100, 23)[0],
                            "triangles": grid_counts(100, 23)[1],
                            "vertex_cap": 2730, "triangle_cap": 4540},
        "overlapping_intervals": {"true_ridge": .26, "true_background": .25,
                                  "existential_check_passes": ridge[0] <= background[1],
                                  "robust_order": interval_order(ridge, background)},
        "perspective_edge_to_centre_density_ratio": (
            pixels_per_angular_texel(1200, half_fov, half_fov, .001)
            / pixels_per_angular_texel(1200, half_fov, 0, .001)),
    }


if __name__ == "__main__":
    print(json.dumps(example(), indent=2))
