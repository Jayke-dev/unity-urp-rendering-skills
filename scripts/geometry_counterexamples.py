#!/usr/bin/env python3
"""Synthetic geometry counterexamples, not a Unity scene or a water certificate."""
import json
import math


def above_floor_ray_impossible(eye_y, direction_y, floor_y):
    """Sufficient impossibility condition for t>=0 and triangles entirely above floor."""
    if any(type(x) not in (int, float) or not math.isfinite(x) for x in (eye_y, direction_y, floor_y)):
        raise ValueError("finite scalar geometry required")
    return eye_y < floor_y and direction_y <= 0


def polygon_inradius(circumradius, sides):
    """Regular polygon centred at the origin; does not model arbitrary water meshes."""
    if type(sides) is not int or sides < 3:
        raise ValueError("sides must be integer >=3")
    if type(circumradius) not in (int, float) or not math.isfinite(circumradius) or circumradius <= 0:
        raise ValueError("positive finite circumradius required")
    return circumradius * math.cos(math.pi / sides)


def main():
    radius, sides = 10.0, 6
    inner = polygon_inradius(radius, sides)
    # Along the normal of an edge of the regular polygon, between edge and circle.
    witness_radius = (inner + radius) / 2
    print(json.dumps({
        "synthetic": True,
        "skirt": {"eye_y": 1.0, "direction_y": -0.1, "floor_y": 4.0,
                  "above_floor_ray_impossible": above_floor_ray_impossible(1.0, -0.1, 4.0)},
        "regular_polygon": {"sides": sides, "circumradius": radius,
                            "inradius": inner, "edge_normal_witness_radius": witness_radius,
                            "witness_inside_circle_but_outside_polygon": inner < witness_radius < radius},
        "limit": "No transformed triangles, raster coverage, animation, water material or live visibility proof.",
    }, indent=2))


if __name__ == "__main__":
    main()
