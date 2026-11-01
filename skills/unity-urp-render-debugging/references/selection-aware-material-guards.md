# Selection-aware material guards

Use this when effective material tag queries change on the first render while shader/material references remain unchanged. This is a preservation problem, not automatically a material mutation.

## Distinguish declaration, selection and override

`Material.GetTag(key, false, default)` is selection-dependent: it queries the currently used SubShader, subject to material overrides. `Shader.FindSubshaderTagValue(index, key)` queries one indexed declaration. The two are not interchangeable. A shader reference or unchanged render-pipeline asset type is not a complete identifier for the current selection context.

In the pinned source scene, the first baseline render changed the observed active SubShader index from 2 to 0, pass count from 1 to 9, and three effective queried tags. Original/copy references and the vector of declared SubShader tags remained unchanged. The frozen effective-tag snapshot therefore rejected a benign selection change. This identifies the tested guard blocker; it does not prove the unique engine-internal cause of selection or exclude every possible material mutation.

## Avoid three incomplete fixes

- Comparing only original versus copy misses coordinated mutation of both.
- Accepting any value found anywhere in the shader's declarations can accept a value from the wrong current SubShader.
- Keeping a supposedly private witness material indefinitely does not make it immutable. Package or Editor callbacks can enumerate loaded materials without possessing your reference.

## The tested correction pattern

The V3 branch kept the old V2 rule unchanged and separated only effective `tag.*` facts from the ordinary bind snapshot. References, queues, textures, keywords, pass-enable states and other non-tag facts retained their checks. It also froze declared shader metadata.

At bind, a fresh never-drawn material constructed from the same shader supplied a current no-custom-override reference vector. Differences observable between the original and that vector were recorded as bind-time overrides. Subsequent checks used the frozen observable override where present, otherwise the freshly queried reference value. Both original and owned copy had to match that expectation. The implementation kept frozen managed data, not a long-lived reference material, and rejected incomplete vectors or changed declarations.

This is a conditional pattern, not a drop-in universal guard. A fresh material is an additional engine interaction with lifecycle and allocation cost. Validate that its selection matches the relevant material and that creating/querying it does not change the state being measured. Keep the probe alive only for the bounded synchronous check, then destroy it through the appropriate Unity lifecycle. Check cleanup after destruction actually completes.

## Validate the oracle independently

Two fresh materials agreeing does not prove their values are the correct selected declarations. The source diagnostic used an independently observed Editor active index plus indexed shader declarations, bracketed original/copy/selection facts around probe creation, preserved the original failing assertion and collected ten observations. All ten probes matched the indexed selected declaration, bracket facts stayed stable, and no probes remained after the cleanup wait.

That finite diagnostic supported implementation; it was not a product pass. The following corrected PlayMode suite passed all 20 checks, including the unchanged first-render scenario and mutation/cleanup cases. In that scenario the same 2→0 selection transition occurred, but the replacement reached Built/shown instead of the previous tag HOLD. A player-runtime compile separately excluded the test-only attachment method.

## State what the getters cannot prove

An override exactly equal to the currently selected value is observationally indistinguishable through these effective tag getters. A bind-hidden override may surface only after a later selection change; retain a specific HOLD instead of promising zero false positives. Selection changing between reads also invalidates a comparison unless the implementation's actual execution assumptions cover it.

Do not advertise enumeration of the serialized override map, universal shader behaviour or unmeasured allocation performance. Test the pinned target, actual materials, coordinated changes, observable override removal, missing vectors, declaration drift, cleanup and the original first-render sequence. A successful guard repair still needs the real imported assets and final fixed-view pixel/visual validation.
