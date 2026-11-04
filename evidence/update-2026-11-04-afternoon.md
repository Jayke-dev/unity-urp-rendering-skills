# 4 November afternoon: rejected overlay, authored backdrop and honest previews

Evidence cutoff: **2026-11-04 16:00 UTC**, through completed R153 receipts. R154 and later proposals are excluded. This continues the [early 4 November snapshot](update-2026-11-04.md), which correctly recorded the overlay as unrendered at its earlier cutoff. [E27–E32 aggregates and report hashes](update-2026-11-04-afternoon.json) preserve the chronology.

All native results remain desktop Metal on Unity 6000.3.26f1 / URP 17.3.0 against an **unaccepted reconstructed reference**. No final landscape, full-view preservation or Quest result is claimed.

## The equal-depth overlay was tested and rejected

The first native smoke verified the full drawn slice and both owned mesh uploads with zero bit mismatches. It stopped after 6 of 24 images because the first reference repeat differed by two pixels; that arm was INVALID (E27).

A separately reviewed complete observation then collected all 24 images (E28):

| View / samples | Reference-repeat differences | Full-overlay differences | Arm result |
|---|---:|---:|---|
| Spawn / 1 | 2 | 13 | INVALID |
| Spawn / 4 | 0 | 54 | Reject overlay hypothesis |
| North / 1 | 0 | 0 | Observed match at this pose |
| North / 4 | 0 | 59 | Reject overlay hypothesis |

The north 4-sample full-overlay arm also had four water-key extra pixels; the subset arm had zero such extras. All subset extra-pixel counts were zero. These narrower observations do not rescue full-overlay equality. Stable 4-sample controls independently reject the tested exact hypothesis even while the overall test retains an INVALID arm. No unique rounding, shader or geometry mechanism was established.

**Time-saving conclusion:** stop this overlay route under the unchanged criteria. One single-sample match, small channel deltas and successful upload readback are not evidence of multisample coverage identity. No offset/tolerance/shader sweep was adopted as a rescue.

## Imported coordinate systems needed an explicit new-surface adapter

The original and authored imports exposed identical importer settings but differed numerically in two matrix entries, by at most about 1.8e-7. They were both finite proper-affine frames; this was not merely signed zero. The exact common-frame gate correctly stopped (E29).

The reviewed correction converted only the new upper surface into the original mesh frame. It preserved original foot attributes, transforms and bounds, used inverse-transpose normals and direction-transformed tangents in the positive-determinant branch, and snapped the new boundary to original bits. Actual Unity creation, geometry/foot checks and mesh save/reload passed. A different dependency check then stopped that run before images.

The conversion uses double arithmetic followed by float32 storage. It is not exact world-space identity or a universal conditioning guarantee. See [authored-scene integration](../skills/unity-urp-render-debugging/references/authored-scene-integration.md).

## A copied scene's dependency difference needed graph evidence

A byte-identical scene copy reported the original scene in its dependency set. An ASCII GUID search did not explain or exclude transitive/binary relationships. The reviewed contract collected a bounded direct-edge graph and checked its consistency with recursive closures; it did not simply delete the offending root.

The actual baseline had a two-edge self-reachability witness, not a direct self-edge. All six dependency rules and all 47 build checks passed, with no foreign scenes and the original snapshot intact (E30). This is dependency evidence, not runtime or image proof. Unity's [GetDependencies documentation](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityeditor/assetdatabase/getdependencies) distinguishes direct versus recursive references and notes recursive root inclusion; root inclusion alone is not a cycle witness.

## Capture deadlines should distinguish frames from elapsed time

The first image run reached a 600-frame load limit before any picture. It had no useful async-operation timeline or timeout wall time. After a reviewed correction, a load completed in **0.449 seconds while spanning 1,154 frames**. Capture timing began after confirmed load completion. The same verified assets were reused without another bake (E31).

This demonstrates why a frame counter is a poor substitute for an elapsed-time load budget in this harness. It does not retrospectively prove the earlier timeout's exact cause. The corrected run still stopped after six images on two repeat-pixel differences, before the new landscape was reached.

## Actual preview images now exist; acceptance still does not

A separately approved art-observation mode collected all **72 images** across baseline, copy-control and variant reloads at two courtyard views. Independent checks reproduced all 72 hashes and 62 raw comparison counts. Cleanup and exact isolated-file restoration passed (E32).

Collection completed, but the strict verdict remained **INVALID with 52 invalid entries**. Acceptance gates were not evaluated; foreground, water and foot preservation are unknown in this preview. The mode retains every mismatch and cannot report PASS. Safety, missing-evidence and cleanup faults still stop collection.

Actual images show a broader, rounder skyline and visible authored masses. They also show plain slopes, block-like tonal patches and an abrupt right-hand ridge ending. The baked albedo contains variation, but that does not establish visible detail at courtyard distance. No texture-binding, UV, fog, normal or shader cause was proved. The goal remains unfinished.

The reusable advance is separating **getting pictures for art review** from **claiming valid preservation evidence**. The preview mode is not a relaxation of the strict test. Read the extended [capture protocol](../skills/unity-urp-render-debugging/references/capture-protocol.md) and [preservation-first design](../skills/unity-urp-render-debugging/references/preservation-first-design.md). No private media, meshes, matrices, scene files or experimental shaders are published.
