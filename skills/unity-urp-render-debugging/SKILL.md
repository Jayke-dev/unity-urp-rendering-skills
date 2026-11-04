---
name: unity-urp-render-debugging
description: Debug Unity URP render regressions when adding or replacing terrain in an existing scene, especially foreground pixel changes, static-batch draw geometry, water occlusion, first-render material state and scene-unload cleanup. Use for preservation-sensitive VR rendering; this is not a generic terrain generator or proven Quest performance recipe.
---

# Unity URP render debugging

Optimise for the requested visible result. A passing diagnostic establishes only its named observation; it does not make a candidate visually acceptable.

## Choose the relevant reference

- Pixel regressions, sorting, masks, baseline instability or first-render materials: [capture-protocol.md](references/capture-protocol.md).
- Effective material tags changing when the rendering pipeline selects a SubShader: [selection-aware-material-guards.md](references/selection-aware-material-guards.md).
- Landscape gaps, water sightlines, winding or unconvincing mountain forms: [terrain-and-water.md](references/terrain-and-water.md).
- Imported/live mesh disagreement, static batching, readback ownership or scene exit: [gpu-and-lifecycle.md](references/gpu-and-lifecycle.md).
- Clone counterfactuals, route-dependent visibility, transition overlays or reconstructed references: [causal-experiments.md](references/causal-experiments.md).
- Procedural normal/lighting errors on skew coordinates, or textures assigned but not visibly contributing: [normal-metrics-and-material-response.md](references/normal-metrics-and-material-response.md).
- Authored imports, unequal coordinate frames, copied-scene dependency checks or load/capture clocks: [authored-scene-integration.md](references/authored-scene-integration.md).
- Repeated replacement failures, hidden additive terrain, or surface-overlay proposals: [preservation-first-design.md](references/preservation-first-design.md).
- Frame Debugger/replay attribution or capability-tool validation: [replay-capability-checks.md](references/replay-capability-checks.md). Its draft-review lessons are not native debugger validation.

## Establish the contract before a repair

Record what must remain unchanged, what may improve, the representative views and the final visual criterion. Exact pixel equality was a source-project requirement, not a universal mandate. Use the user's actual tolerances; never quietly change them to make a test pass.

Pin Unity/URP versions, device/backend, camera projection and pose, actual colour/depth format, AA, active render pipeline and relevant shader/material state. Local Metal results do not prove Quest results.

Separate five verdicts: diagnostic validity, functional correctness, preservation, visual quality and target-device performance. Unknown evidence stays unknown. Keep the original first-frame/repeat failures visible.

## Make the next experiment decisive

State a hypothesis, the controlled variable and which implementation decision each result changes. Prefer one reversible change to owned objects over global camera, shader or borrowed-renderer changes. A counterfactual camera arm is a diagnostic; adopting it requires validation against the original accepted baseline.

Capture a fixed representative cohort before an expensive all-view run. Keep the baseline and control comparable within the same process when feasible, repeat and reverse conditions, and render ordinary RGB subjects before diagnostic mask overrides. Restore state before the next condition. Same-frame capture helps with temporal variation but cannot exclude per-render lighting, ordering or pipeline work.

If the evidence supports a product repair, implement it and compare the visible outcome. Another diagnostic needs a decision that existing evidence cannot answer. After repeated repairs without meaningful gain, reconsider the design or expose a concrete constraint conflict instead of extending an unlimited diagnostic chain. This is a stopping heuristic, not a fixed universal experiment budget.

## Avoid the expensive false shortcuts

- Lower error counts against a changed baseline are not preservation.
- Exact geometry or material values do not imply equivalent draw context, batch state or shading.
- A CPU centre ray is not the GPU's multisample rasterisation, alpha test, LOD or deformed geometry.
- A mesh that fits the triangle budget can still obstruct water or look wrong.
- A geometry overlap is not automatically a visible collision; a visibility exemption still needs a live, render-path-specific justification.
- A hash of unchanged references or counts does not prove unchanged buffer contents.
- A copied material or changed render queue is a hypothesis, not a portable fix.
- Hiding new geometry while leaving the original retired does not recreate the baseline. An additive architecture is an alternative to test, not proof that retirement caused the old failure.
- Zero protected-pixel differences with mostly hidden new terrain do not satisfy a visible landscape brief. Surface detail and silhouette need separate judgments.

## Finish with product evidence

Report the repair, same-reference before/after metrics, inspected visual differences and unresolved failures. For a credible candidate, run the project's full fixed-view checks, verify cleanup/restoration and inspect the images. Keep target-headset stereo, appearance, performance and memory checks separate from desktop results.

The supporting case study and official API links live two levels above this skill in the repository. They are optional provenance; the skill and its references remain usable when the skill directory is copied alone.
