"""Synthetic 2D plane example, not a Unity normal baker or conditioning proof."""
import json
import math


def _number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("expected a finite real number")
    try:
        result = float(value)
    except OverflowError as exc:
        raise ValueError("number does not fit a finite float") from exc
    if not math.isfinite(result):
        raise ValueError("expected a finite real number")
    return result


def _pair(value):
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        raise ValueError("expected a two-element vector")
    return tuple(_number(x) for x in value)


def world_gradient(plan_du, plan_dv, height_du, height_dv):
    """Solve J^T g = dh for a finite, numerically usable local 2D Jacobian.

    Does not bound error for an ill-conditioned frame or model a GPU tangent basis.
    """
    a, b = _pair(plan_du)
    c, d = _pair(plan_dv)
    hu, hv = _number(height_du), _number(height_dv)
    determinant = a * d - b * c
    if determinant == 0 or not math.isfinite(determinant):
        raise ValueError("unusable local Jacobian")
    gx = (d * hu - b * hv) / determinant
    gy = (a * hv - c * hu) / determinant
    if not all(math.isfinite(x) for x in (gx, gy)):
        raise ValueError("nonfinite reconstructed gradient")
    return gx, gy


def incorrect_orthogonal_assumption(plan_du, plan_dv, height_du, height_dv):
    """Intentionally wrong for skew axes: normalized directions treated as a basis."""
    axes = (_pair(plan_du), _pair(plan_dv))
    slopes = (_number(height_du), _number(height_dv))
    result = [0.0, 0.0]
    for axis, slope in zip(axes, slopes):
        length = math.hypot(*axis)
        if length == 0 or not math.isfinite(length):
            raise ValueError("unusable axis length")
        for i in range(2):
            result[i] += (slope / length) * (axis[i] / length)
    if not all(math.isfinite(x) for x in result):
        raise ValueError("nonfinite reconstructed gradient")
    return tuple(result)


if __name__ == "__main__":
    # p(u,v) = (u+v, v), h(x,y)=x: h_u=h_v=1.
    du, dv = (1, 0), (1, 1)
    print(json.dumps({
        "scope": "invented affine plane only; no Unity execution",
        "expected_world_gradient": [1, 0],
        "inverse_transpose_result": world_gradient(du, dv, 1, 1),
        "incorrect_normalized_axes_result": incorrect_orthogonal_assumption(du, dv, 1, 1),
    }, indent=2))
