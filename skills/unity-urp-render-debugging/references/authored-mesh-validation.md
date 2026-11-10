# Authored mesh interchange and preservation

Use this reference when a generated mesh passes source checks but fails export, normal storage, coverage or the actual image. The observations behind it are in the [10 November update](../../../evidence/update-2026-11-10.md), E52–E65 and E66–E68. This is a validation workflow, not a terrain generator.

## Validate the representation that the consumer receives

When the reference belongs to an engine, export it through that engine's actual producer. In the source case, a standalone exporter matched counts but not native mesh bytes; the native export reproduced the recorded reference. Matching counts or an independent runtime is insufficient for exact interchange.

Pin the successful producer, inputs, binary payload and generation receipt. Reuse unchanged geometry for a material-only derivative only after checking those dependencies. Keep the original generation provenance; changed bake or render outputs still need their own validation.

Check the installed API actually called. A callable Python mesh method need not appear in an RNA function registry. A successful capability query also does not establish that a later mesh mutation preserves a previously acquired UV wrapper. Reacquire the layer and read back its exact content after relevant attribute edits. The observed old-path failure and revised-path success support that defensive practice, without uniquely proving the historical cause.

Separate normal direction, storage fidelity, projection coverage and appearance. Use a scale-independent direction metric while retaining the declared limit. In one bounded static-mesh case, a different native normal representation preserved every float32 component, then the bake failed an independent coverage gate. That storage result is not a portable recipe for every Blender version or animated mesh.

## Keep logical geometry distinct from render attributes

Normal or tangent discontinuities may require multiple render vertices at one logical vertex. Do not force a tangent sign or silently change a protected normal to make the frame builder pass.

An attribute split needs an explicit per-corner map back to logical geometry. Verify positions, UVs, winding, primitive order and protected attribute bits on the encoded payload. Transfer a logical-domain proof only through that checked map. A raw render-index graph with attribute seams is not itself the same manifold disk.

In the source case, one diagnostic representation used 2,113 logical vertices and 2,152 render vertices; a later smoothed diagnostic used 2,144. Both had 3,804 triangles. Those counts describe different frozen meshes, not interchangeable identities or recommended budgets. Successful encoding and logical coverage did not turn either rejected artwork into an accepted factory output.

## Replay the failed bake before changing its window

Use the original query, numerical conversions, segment endpoints and frozen mesh. Reproduce its miss counts before proposing a remedy. Intersections beyond a segment endpoint explain a specific coverage failure; they do not by themselves establish intended-surface identity or uniqueness.

Revalidate after geometry changes. A projection window that passed one mesh later missed 16 of 660,900 rays on a revised mesh. A bounded owned HIGH-surface correction then cleared those misses with the original window and zero-miss requirement. Neither a local bound nor the earlier successful bake replaced complete coverage on the changed surface.

## Judge the image separately

Keep the material, normal-map state and vegetation population comparable when testing macroform. In three representative views, exact repeats, water comparisons and candidate/control confinement passed while art remained rejected. The old-control versus OFF failures also remained visible.

The smoother diagnostic reduced the sheer-panel appearance seen in an earlier diagnostic. Its matched A/B baseline was still the earlier control mesh, not that intermediate panel mesh. Describe cross-run visual observations separately from same-baseline pixel measurements. Preserve abrupt ends, weak ridge hierarchy and poor full-frame vegetation impact as unresolved defects; do not hide them behind export or mesh-proof success.
