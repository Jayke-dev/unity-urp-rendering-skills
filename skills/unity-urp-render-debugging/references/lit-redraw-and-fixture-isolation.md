# Lit redraw identity and synthetic fixture isolation

Use this for a late URP redraw that changes an existing lit surface even with the original material, or a synthetic test affected by rendering context. This is a tested local diagnostic sequence, not a portable render feature or a validated palace/Quest solution.

## Prove identity before judging a new material

Render an unchanged baseline, repeat, pass-off control, original-material redraw, owned-material identity redraw, a distinctive positive-control material, the active effect and restoration. Require actual execution of the relevant pass. A descriptor or shadow guard can refuse all drawing while producing identical pictures; that is a refusal, not successful identity rendering.

Keep control validity, functional pixel results, memory and final acceptance separate. A source-case synthetic run passed sixteen byte-exact RGBA comparisons and protected-area tests, but correctly remained INVALID because ten memory rows were unknown. Such diagnostic collection requires the project's explicit permission; it never creates an automatic unknown-budget exception.

## Matching geometry is insufficient for a lit draw

The earlier whole-mesh copy changed 32 protected pixels even with exact-order live geometry and original materials. Partitioning added other changes without removing those same residuals. Repeating geometry equality would not make that draw context neutral.

Separately, a direct original-material lit redraw changed 66,385 pixels in a synthetic fixture. Unity documents that `CommandBuffer.DrawRenderer` does not set up lighting-related shader inputs; lit results can therefore be undefined. Do not infer that reusing a material also recreates its original pipeline context. Inspect the pinned renderer's culling, sorting, per-object data, shader-pass selection, probes, lightmaps, shadow state and effective camera resources.

A renderer list built from the relevant frame's culling/drawing/filtering context is an approach to test, not a guarantee. In the source case it eventually produced exact original and owned-material redraws in an isolated fixture, including the statically batched case. At that early cutoff real-scene transfer was unproven; the later one-view result below extends it. Do not bypass light/shadow guards merely to reach the draw.

## A synthetic scene can inherit unintended context

An owned light configured with shadows disabled did not establish that all visible lights were owned or shadow-free. A later guard observed a shadow-casting light. Check the actual visible-light ownership and frame capabilities; asset/hardware shadow support, a light's shadow configuration and active frame shadow data are distinct facts.

For an Editor fixture whose scope permits it, a temporary lease over only the owned scene/camera culling masks can test isolation without disabling foreign lights or changing global settings. Verify collision/ownership assumptions and restore through failure and actual scene unload. Do not assume scene masks isolate ambient, sky, fog, reflection inputs, unenumerated scenes or all engine contributors.

Measure isolation-off versus the isolated reference as a fact, then repeat the isolated reference exactly. In the source test, off versus on changed 826 pixels, while the on repeat was exact. The subsequent identity successes belong to the new isolated reference. They do not repair the earlier failed baseline or identify the unique cause of its failure. The isolation-off control occurred within the new run; it did not recreate an old first frame.

Use a distinctive Key and active-effect arm to exclude a no-op success: in the tested fixture they changed 45,250 and 24,300 pixels respectively, with zero protected or masked hits. These counts describe one fixture, not reusable thresholds or landscape quality.

## Exercise real resource and lifecycle behavior

Inspect effective colour/depth descriptors and pass execution. Editor offscreen MSAA can use intermediate attachments; equality to a particular backbuffer handle is not a general imported-resource test. A hardcoded depth format also refused the tested platform's default. A specifically reviewed platform query or route correction must preserve the intended descriptor and ownership contract; do not silently drop the guard. Changed attachment routes may induce storage that remains unmeasured.

Bound simultaneously live GPU readbacks and verify consumption/retirement before issuing the next. The successful native fixture issued, consumed and retired twenty requests with maximum one live. GPU completion alone is not proof that its storage has retired. Retain referenced resources when settlement cannot be confirmed; cleanup exceptions must invalidate success rather than being logged and forgotten.

Await a real scene unload and check callbacks, subscriptions, instances and mask leases after it. Early aborts that merely request unloading and later show zero instances do not prove the intended unload path executed. In the successful fixture, that actual lifecycle gate was reached with no cleanup faults.

## Bridge to the real scene explicitly

Before transplanting this fixture result, establish the actual target scene's producer count, lighting, camera route, resource lifetime and unchanged-reference identity. A sixteen-record synthetic census is not a production capacity certificate. A source-configured shadow-casting sun is not an observed frame capability. A worst-case allocation scenario is not measured usage or a lower bound.

Keep resource unknowns sticky. Count known owned allocations under their declared rules; net memory deltas can hide gross allocations. Separate existing capture-buffer exclusions using exact disjoint measurement segments, not arbitrary reclassification. A charged estimate is still an estimate. Preserve the product budget and report UNKNOWN until supported measurements or bounds establish it.

Read only the corresponding dated case evidence when needed; no private renderer implementation, scene or native raw data is supplied by this repository.

## Later actual-palace result, with the same scope discipline

The late 6 November seven-frame run established one-view actual-palace original-material redraw identity: repeats/redraw/returns were byte-exact, while a positive control changed 34,042 pixels. This completes that specific bridge and should not be repeatedly re-proved without a relevant new failure. New landscape artwork was OFF. Full original scene gates, product memory and Quest acceptance remain unresolved. The [10 November addendum](../../../evidence/update-2026-11-10.md) preserves both this success and the older distinct failures.
