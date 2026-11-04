# Authored geometry, scene dependencies and capture clocks

Use this when integrating an authored mountain/backdrop into an existing scene with protected geometry. Separate a successful bake, Unity import, geometry validation, dependency validation, capture completion and visual acceptance. Failure at one stage does not erase earlier verified assets or authorize calling later stages passed.

## Equal import settings do not guarantee equal frames

Record the actual renderer/mesh frames after import. In the source case, two readable imports exposed identical scale and axis options but differed in two nonzero matrix entries by about 1.8e-7. Both were finite affine with positive determinant. That was an observed disagreement, not proof of an exporter or importer bug and not a signed-zero equivalence.

If the contract requires identical frames, do not silently round them equal. Where the user permits changing new geometry, an explicit adapter can convert only that geometry to the protected original frame. For original linear/translation parts A_o, t_o and new parts A_n, t_n:

```text
M = inverse(A_o) * A_n
b = inverse(A_o) * (t_n - t_o)
p_new_in_original_frame = M * p_new + b
n_new_in_original_frame = normalize(inverse(M).transpose * n_new)
tangent_xyz_in_original_frame = normalize(M * tangent_xyz)
```

These formulas describe the reviewed positive-determinant branch. Tangent w stayed unchanged there; mirror support was not assumed. The implementation used double intermediates followed by float32 storage. Reject unsupported/nonfinite/degenerate inputs and recheck the stored result against the real contract. A finite inverse is not a universal guarantee for ill-conditioned transforms.

Preserve protected original attributes by copying their bits; do not run them through the new adapter. Keep an unchanged equal-frame fast path when its original bit-copy semantics matter. Check source boundary IDs for unique correspondence, snap only the new boundary to protected original positions, and verify cracks, bounds, partition, area, budget and save/reload results. Independent tests should use noncommuting/sheared/translated frames and a separately derived reference to catch wrong multiplication order and wrong normal transforms. Test tolerances do not become pixel or original-attribute tolerances.

The source adapter passed actual Unity geometry/foot/bounds and mesh save/reload checks. That did not itself establish any render result.

## A dependency-set exception needs a witness

Unity's [GetDependencies API](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityeditor/assetdatabase/getdependencies) distinguishes direct and recursive references; recursive results include the requested root. API references are not necessarily build-required. The documentation does not establish a particular scene's actual graph.

A root in a recursive closure is not proof of a positive-length cycle. If a copied scene unexpectedly depends on its source, retain the raw observation. A textual GUID search cannot exclude binary or transitive references. Before changing the contract, collect direct edges in a bounded same-process graph and reconcile its reachable sets with the recorded recursive closures. Do not synthesize self-edges from recursive-root membership.

In the source case, the original had an actual two-edge return path. A reviewed witness-based rule then validated the copy and variant dependency sets. Unexplained edges, incomplete evidence, unexpected foreign roots or changed source identities still stopped the build. This was an explicit contract correction, not permission to delete every inconvenient scene path.

Keep real files/metas/GUIDs and baseline descriptors stable across collection. Some already-present Unity virtual/builtin entries may have no ordinary disk file; label that limited identity evidence instead of inventing byte hashes or applying a general missing-file exemption. Graph reachability is not runtime causality or visual correctness.

## Loading has its own clock

Log elapsed monotonic time, frame count, async completion/progress, scene identity and relevant callbacks. Use an elapsed-time load deadline appropriate to the harness, then establish the capture epoch after confirmed completion. If a pending load times out, report and handle its ownership explicitly; do not silently abandon callbacks or leave a later activation behind.

One source run stopped at a 600-frame cap. A later run loaded in 0.449 seconds over 1,154 frames. This shows that frame count and wall time were not interchangeable in that run; it does not reconstruct the earlier missing timeline. Fixing the clock allowed capture to begin but exposed an independent repeat-image failure.

When geometry/dependency build checks already pass, retain their hashes and reuse those exact assets for a capture-only correction where the project allows it. A capture-clock change does not inherently require rebaking the terrain. Reuse still needs source identity, safe staging and cleanup checks; it is not permission for automatic retries.
