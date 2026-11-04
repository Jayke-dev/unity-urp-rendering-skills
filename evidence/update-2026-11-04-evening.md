# 4 November evening: a real metric correction, limited visual gain

Evidence cutoff: **2026-11-04 18:20 UTC**, through reviewed R157 evidence. R158 and later work are excluded. This continues the [afternoon snapshot](update-2026-11-04-afternoon.md); [E33–E37 aggregate evidence and report hashes](update-2026-11-04-evening.json) preserve the source/test/bake/render distinctions.

The environment remains Unity 6000.3.26f1 / URP 17.3.0 / desktop Metal on an **unaccepted reconstructed reference**. No completed landscape, preservation approval or Quest result is claimed.

## Passing tests had missed a skew-coordinate error

All 33 existing generator checks and the chosen recipe proxies passed. Independent review then sampled a known world-X ramp through the actual plan directions. The gradient reconstruction was wrong because it treated two skew directional derivatives as perpendicular tangent components. Error norms at the reviewed samples ranged from about 0.15 to 1.14 (E33).

The correction used the full plan Jacobian rather than axis lengths alone. Forty-three independent checks passed, including analytic plane/skew/rotation cases through the production macro/detail paths. Geometry, UVs and boundary IDs remained unchanged. The horizontal detail-normal projection still does not prove agreement with steep surface tangents or imported MikkTSpace (E34).

**Reusable lesson:** use known analytic fields to test coordinate conversions in the real path. Tests of helper signs, scalar lengths and recipe statistics can all pass while world-space shading directions are wrong. The new [synthetic skew-gradient example](../scripts/skew_gradient_counterexample.py) demonstrates the algebra with independent invented data; it neither copies nor certifies the project generator.

## Deterministic output did not deliver the target appearance

Two fresh single-thread Blender bakes matched exactly in PNG/digest content and all 14 finite exported numeric arrays. FBX container timestamp identity was not required. Unity then passed all 47 build checks and collected another 72 actual images (E35–E36).

Image review found a smoother ridge and partly reduced block-like shading, but pale plain slopes still dominated. Readable rock/grass/gully detail, layered depth and the terminal ridge shape remained below target. The approved recipe ended; another art recipe was not automatically started.

Validation still had **52 INVALID entries and zero acceptance-gate evaluations**. Foreground, water and foot preservation were NOT_EVALUATED. Bake determinism, improved source mathematics and completed image collection do not convert that into acceptance. Cross-run visual inspection is not a same-process pixel-causality test.

## Assigned textures are not proof of visible colour contribution

A new hypothesis was raised: an older background layer might cover the new terrain. Offline source/asset review found that the combined variant contains only the original foot strips plus the authored upper mesh; the old upper triangles are excluded. New albedo/normal assets are assigned, UVs are not collapsed and a diagnostic key mask shows the upper surface in both views (E37).

Those are useful checks, but **the layering hypothesis remains unconfirmed**. The mask changes material, fog and AA; it establishes rasterization under that diagnostic path, not contribution to ordinary RGB. Serialized texture assignments are also not live GPU binding evidence. Source review did not establish a separate fallback plane, but that is not a complete runtime census.

The next decision was a bounded ordinary-RGB response/visibility plan, before more art changes. No such native intervention was completed at this cutoff. Do not infer a unique shader, UV, fog or occlusion cause from plain-looking output, key masks or small comparison differences.

Read [normal metrics and material response](../skills/unity-urp-render-debugging/references/normal-metrics-and-material-response.md). No private images, geometry, matrices, experimental shaders or model/session identifiers are published.
