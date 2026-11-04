# Normal metrics and actual material response

Use this when procedural terrain shading uses curved/skew UV or plan coordinates, or a detailed texture asset appears plain in the final view.

## Derivatives along skew axes are not orthogonal components

For a local plan mapping p(u,v) = (x,y), let p_u and p_v be its two derivative columns and h_u,h_v the sampled scalar derivatives. The world gradient g satisfies:

```text
J = [ p_u  p_v ]
J.transpose * g = [ h_u, h_v ]
g = inverse(J.transpose) * [ h_u, h_v ]
```

Dividing each derivative by its axis length gives two directional derivatives. Treating those as coefficients of an orthonormal tangent frame is valid only when that frame really is orthogonal. Normalizing the two axes does not make them perpendicular. The same issue affects normal-map inputs, world lighting and physical-scale filtering.

The [synthetic helper](../../../scripts/skew_gradient_counterexample.py) demonstrates this with an invented affine plane. For p_u=(1,0), p_v=(1,1) and h=x, the correct gradient is (1,0); a normalized-axis reconstruction gives (1.5,0.5). The helper solves a local 2D algebra problem; it is not a terrain normal baker, conditioning certificate or Unity shader test.

Use known world-X/world-Y and rotated analytic planes at nonorthogonal, nonuniformly scaled coordinates to exercise the actual production conversion. Compare against a separately derived answer. Test edges, finite outputs and degenerate inputs, and preserve the project's rule for unusable metrics. Do not hide invalid directions by clamping NaNs. A helper-only test cannot establish that callers use its output in the correct lighting or tangent basis.

After solving the plan gradient, still account for the actual surface frame, tangent handedness and normal-map convention. A horizontal projection can be an approximation on steep terrain. Do not label it identical to imported MikkTSpace without appropriate evidence.

In the source case, 33 passing checks missed a real skew-gradient error. Corrected production-path checks passed, geometry stayed unchanged, and bakes were deterministic. The subsequent image still missed the visual target. A demonstrated math repair is not proof that it explains every prior render defect or is sufficient for the art goal.

## Establish which path supplies ordinary RGB

Distinguish these evidence levels:

| Observation | Establishes at most |
|---|---|
| Mesh/material/texture serialized in the scene | Source or asset assignment |
| Noncollapsed UVs and expected combined triangles | Relevant stored geometry exists |
| Key-colour mask with overridden material/fog/AA | Rasterization through that diagnostic path |
| Ordinary-RGB response to a controlled material change | The changed material path contributes to the tested image, subject to controls |
| Strict protected-region comparisons and real art review | Their named preservation and visual results |

A key mask can expose geometry that contributes differently under ordinary material, depth, fog, AA or compositing. Expected texture references do not prove current GPU binding. Conversely, plain output does not prove an older fallback image is covering the surface.

Before another texture recipe, name the specific occlusion-versus-material decision a bounded test would change. Where authorized, keep the normal camera/pipeline path and ordinary references, make one reversible test-owned or scoped material intervention, restore state, and validate repeated controls. A visible response supports that path's contribution; no response alone does not uniquely prove occlusion, because a rejected pass, stale binding or ineffective intervention can also produce it. Require an effective positive control and valid capture evidence before attribution.

The source case reached only offline assignment/UV/key-mask review at this update's cutoff. A later visibility plan was pending, so this is experimental guidance, not a newly validated material-attribution tool. Keep baseline repeat/control/reload failures visible, and never force queues or relax masks merely to make the hypothesis appear true.
