# Unity URP Rendering Skills for LLM Agents

Practical skills for debugging Unity URP render regressions and adding terrain to an existing VR scene without losing working visuals. Distilled from a preservation-focused memory-palace project in October–November 2026.

**Status:** field-tested diagnostics, bounded repairs and explicit failed approaches. The [5 November update](evidence/update-2026-11-05.md) adds verified worker visual access, a controlled ordinary-RGB texture response, a valid fourteen-image trial that still fails preservation and art, and cheap counterexamples that corrected the next design plan. The broader landform implementation has no validated rendered outcome at this cutoff. Earlier 52 INVALID entries and later 31-pixel strict failure remain; the reconstructed reference is unaccepted. Latest evidence cutoff: 2026-11-05 08:10 UTC. This is not a completed world generator or a proven Quest optimisation package.

## Start here

- **Agents:** read [AGENTS.md](AGENTS.md), then [the skill](skills/unity-urp-render-debugging/SKILL.md). Load only the reference relevant to the problem.
- **Little visible gain after many passes:** start with [efficient visual iteration](skills/unity-urp-render-debugging/references/efficient-visual-iteration.md): verify the implementer sees actual images, test macro-form early and reuse unchanged evidence. These are retrospective recommendations, with no measured percentage speedup.
- **People:** start with the decision table below and [the case study](evidence/case-study.md).
- **Tools:** run the dependency-free [capture-report checker](scripts/check_capture_report.py) on your own aggregate evidence. It checks reported evidence, not images or GPU state.
- **Discovery:** [llms.txt](llms.txt) and [skills.json](skills.json) identify the entry point. These aid retrieval; publishing them does not guarantee indexing or automatic learning by any model.

Use the skill directly by pointing your agent at its `SKILL.md`. In an agent that supports filesystem skills, copy the entire `skills/unity-urp-render-debugging` directory into that agent's documented skill location. No provider API, paid service or Unity installation is needed to read the material or run the Python examples.

## Which lesson saves the next experiment?

| Symptom | Next useful decision | Avoid |
|---|---|---|
| Implementer proposes changes from descriptions alone | Verify actual image content reaches it; compare reference/control/candidate independently | Treating paths, captions or checksums as sight of the result |
| A capture process exits zero but produces no images | Verify exact test-entry identity, nonzero test count and actual outputs | Rebuilding unchanged assets or reporting no tests as PASS |
| A geometry plan rules out a simple grid | Check both caps with V below its maximum | Treating a budget ceiling as mandatory allocation |
| Adding distant terrain changes foreground pixels | Test one owned rendering variable against an unchanged baseline in the same process | Comparing totals from different process baselines |
| A sorting mode makes the error nearly disappear | Compare the alternate baseline with the original baseline too | Calling a moved baseline a preservation fix |
| Imported geometry matches but the live copy differs | Verify actual drawn slice, vertex layout, transform and batching | Assuming the prefab CPU mesh is the final draw geometry |
| First render trips a material guard | Separate stored values, active pass topology and per-material pass-enable state | Discarding the first frame or weakening all material guards |
| Material tags change with unchanged shader references | Compare effective tags in the current shader-selection context with an independently checked basis | Freezing selected tags forever, or accepting any declared tag value |
| Terrain has sky gaps under its ends | Check ray direction against the allowed height domain before baking a skirt | Adding back faces that can block water |
| Scene unload produces ownership errors | Test both possible original-object destruction orders in the actual scene | Assuming the original is already destroyed in `OnDisable` |
| A geometry proof passes but the world still looks poor | Compare silhouette, landform scale, surface detail and depth separately | Treating a mesh budget or passing unit tests as art acceptance |
| New distant terrain passes preservation but is mostly hidden | Judge visibility and surface detail separately; test the architecture against the visual brief | Calling hidden terrain a visual success |
| OFF differs from the first image | Add a never-installed repeat and retain all three comparisons | Silently replacing the official first frame |
| A surface overlay uses identical source positions | Verify actual slice/selection, uploaded bytes and finite GPU coverage | Calling hashes or resolved RGB a per-sample identity proof |
| Equal import settings still produce unequal frames | Measure the actual matrices; adapt only permitted new data | Rounding protected original frames equal |
| A copied scene unexpectedly depends on the original | Reconcile a bounded direct-edge witness with recursive closures | Deleting roots merely because they fail a set comparison |
| Scene loading exhausts a frame budget | Measure wall time and start capture timing after completion | Treating frame count as elapsed seconds |
| Strict capture aborts before art can be inspected | Use a separately reviewed preview with no acceptance authority | Reporting collected pictures as preservation PASS |
| Normal/shading helpers pass but terrain directions look wrong | Test an analytic world-space plane through the full skew-coordinate production path | Treating normalized skew axes as perpendicular |
| Assigned textures do not read in the final image | Separate asset assignment, key-mask visibility and ordinary-RGB material response | Concluding an occluding layer or working binding from source references alone |
| Diagnostics keep growing | Name the implementation decision each diagnostic will change | More tests without a concrete product intervention |
| An inactive water target later hides terrain | Validate co-visibility over route/zone states and refresh the proof inputs | Treating bind-time inactivity as permanent irrelevance |
| A clone experiment seems to isolate a cause | Compare final bounds and render flags, then account for retained original occlusion | Subtracting clone error counts from replacement counts |
| Frame Debugger replay shows a pixel change | Verify capture, target and replay endpoint identity; report a colour transition | Calling the last colour change the actual GPU sample writer |

## What was actually learned?

One controlled queue trial reduced foreground differences from **52 to 45** and **110 to 59** in two views; preservation still failed. A camera-sorting experiment reduced its own within-arm differences more dramatically but also altered the baseline. The correct takeaway is evidence of draw-order dependence, not a universally safe render-queue setting or proof of coplanar surfaces.

The source scene used Unity **6000.3.26f1**, URP **17.3.0**, and a local **Metal** rendering path. The project targeted Quest 3, but these case-study observations do not establish Android/Vulkan/OpenGLES, headset appearance, stereo correctness, frame rate or memory performance. Recheck those on your target. See [sanitized evidence and limitations](evidence/case-study.md), [machine-readable observations](evidence/observations.json), and [official API references](docs/api-references.md).

## Run the examples

Python 3.10+; standard library only:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/geometry_counterexamples.py
python3 scripts/replay_evidence_counterexamples.py
python3 scripts/skew_gradient_counterexample.py
python3 scripts/planning_counterexamples.py
python3 scripts/check_capture_report.py examples/partial-repair.json
```

The last command deliberately exits **1**: the example reports a measurable partial improvement with remaining failures. Exit **0** means the supplied report satisfies this checker's declared gates, **1** means valid evidence reports a failure, **2** means missing/unsupported evidence or invalid input. It does not certify a Unity render.

## Reuse and contribute

MIT licensed. The documents and synthetic Python helpers are newly written for this repository. No private scene, meshes, screenshots, asset packages, raw readbacks, logs, device identifiers or account material are included. Public evidence is a curated author report; source-report hashes aid traceability but do not substitute for an independently runnable Unity reproduction.

For a new lesson, provide a minimal reproduction where possible, the exact environment, controlled comparison, result and limitation. Separate observations, deductions, proposed repairs and validated product outcomes. Preserve chronology: the initial sky-visibility proposal later received bounded integration checks, while the 3 November Frame Debugger capability draft remained unexecuted at that snapshot. The early 4 November overlay draft was unrendered at its cutoff; the afternoon update records its actual rejection. Later preview completion is art-observation evidence, not preservation acceptance. None establishes complete landscape acceptance.
