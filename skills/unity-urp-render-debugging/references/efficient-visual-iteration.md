# Shorten the loop from code to visible improvement

Use this when source tests and diagnostics accumulate while the rendered scene changes little. This is a retrospective workflow recommendation, not a measured speedup or a proven terrain-generation recipe.

## Give both reviewers the actual images

Before another visual proposal, give the implementation agent and supervisor the same small pack: a labelled target/reference, actual control, and actual candidate. Bind each to its stage, viewpoint and original file hash. A generated concept guides the permitted distant scenery; its foreground, water and sky do not expand the task.

Verify that the implementation agent actually receives image content. A path, caption, checksum or claim that a file exists is insufficient. In Claude Code, Read returns supported image files visually; inspect successful image tool results rather than relying only on self-attestation. The source case had explicitly prohibited image reads until the human authorized a narrow exception. Respect actual sharing permissions; do not infer permission to expose private scenes or logs.

Ask each reviewer independently for the largest visible gaps, what improved/was unchanged/worsened, and the next intervention ranked by expected visible effect. Distinguish an observation such as a pale flat-topped band from a hypothesis about clipping, fog or occlusion. If the reviewers disagree, resolve the view or evidence first. Refresh the pack after image-changing stages, not unrelated source corrections. Keep exact pixel analysis on original files: image tools can resize and recompress their display.

## Prove the visual approach with a small actual trial

Check the feasible angular window, occluding architecture, near/far depth, camera projection, clipping limits, material/fog response and asset budget before investing in a full recipe. Wider world-space depth buys volume and parallax; it does not create extra visible sky above an occluder. Do not spend the whole triangle budget on sampling a shape that reads as a wall.

Use a simple representative macro-form first. Judge broad shoulders, slope depth, skyline and endings from an actual representative view before adding fine noise, erosion, a normal map or a large atlas. Surface detail cannot repair a bad silhouette. More samples of the same narrow strip do not necessarily produce a convincing mountain. Scaling a whole landform can preserve its shape better than clipping each peak to a ceiling, but validate the final eroded/blended float32 geometry; thermal redistribution can raise local valleys.

A texture assignment is not an appearance test. If contribution is uncertain, make one bounded ordinary-RGB intervention with repeat and restoration controls. Once it establishes visible response at that view, stop repeating the complete-covering hypothesis there. Investigate why the real material reads poorly, retaining partial-occlusion and other-view uncertainty. See [material response](normal-metrics-and-material-response.md).

## Keep art and preservation as separate decisions

Judge the images as soon as valid collection permits. A rejected art result can stop a recipe even when preservation is unresolved. An attractive result cannot waive preservation. Keep opaque foreground, water and UI checks at the user's required standard.

If exact equality applies to antialiased boundaries where a changed background can legitimately contribute, define the intended contract early and independently of failed pixels. Do not repeatedly redesign all terrain merely to chase an unexamined edge policy. Mixed-AA response supports a bounded hypothesis, not exclusive sample ownership. A changed acceptance rule requires the project's actual authorization; preserve the old verdicts. See [capture protocol](capture-protocol.md).

Before the next expensive pass, state the changed decision and the failure it replaces. If another parameter adjustment would leave the dominant defect intact, revise the design. Do not prescribe a universal number of trials, mandatory diagnostic framework or fixed image count.

## Reuse evidence only where dependencies permit

| Changed dependency | Fresh evidence | Reuse where unchanged and verified |
|---|---|---|
| Capture entry/helper | Entry identity, affected checks, actual capture | Saved assets and successful build |
| Shader/material | Relevant import/state checks and actual RGB | Geometry and texture bytes |
| Geometry/asset recipe | Geometry, budget, necessary build and images | Tooling and unrelated feature evidence |
| Launcher/docs only | Affected tooling checks | Rendering assets; no Unity run solely for documentation |

Before launching, match the exact test filter to the reviewed implementation or compiled/discovered test list. Require the expected nonzero test count and expected image/receipt outputs afterwards. Exit zero with zero selected tests is no execution evidence. A corrected capture entry does not by itself invalidate a successful asset build.

Use one source owner and serial native execution where the project requires it. Bundle linked steps already covered by standing authorization, with concrete stop conditions; do not repeatedly ask for the same permission. Avoid reinstalling working MCP/CLI tooling unless a missing capability actually blocks the next decision. Keep current prompts compact: outcome, changed files, preserved contract, relevant evidence and stop condition.

## Audit time without inventing savings

Record per-invocation wall time and per-turn start/end, deduplicate retries and distinguish combined agent-hours, overlapping clock-hours and elapsed calendar time. Resumed CLI counters may be cumulative: verify field semantics before summing. The source audit found 31.84 worker-hours and 42.88 associated Codex hours; that establishes the recorded workload, not that all supervision was waste or that a particular percentage was avoidable. No controlled comparison measured how much faster this revised workflow would be.
