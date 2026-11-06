# Controlled captures and first-render state

## Compare to the original contract

Use B for the never-installed accepted baseline, O for installed-but-OFF, C for a control configuration and R for the candidate. Check B versus O separately: an OFF difference is a real baseline failure even if the ON image looks better. Retain first images, repeats, reversals and raw failures.

For a sorting or queue experiment, compare C and R against the **same original reference**. If you also introduce an alternate camera baseline B', report both R' versus B' and B' versus B. A low first count cannot excuse a large second count. In the source case a camera arm reduced within-arm errors to 2/27 while moving the baseline by 74/69 pixels. Those are two different claims.

Cross-process baselines in the case drifted substantially despite matching semantic mask membership. Match process, scene, camera, target, reference and pixel cohort before calling a difference an improvement. If that cannot be established, report the comparison as inconclusive. Repeat noise is information, not an automatic subtraction allowance.

## Subjects first, masks second

Create ordinary RGB captures for all arms before overriding materials or other render state to derive masks. Keep water mask membership, interior water colour, foreground preservation and protected UI/entrance pixels separate. A whole-image colour difference is not a water visibility mask.

Document RGB and mask target descriptors separately, including sample count. Verify the actual allocated depth/stencil format, not just the constructor request. One observed target requested 24-bit depth and resolved to `D32_SFloat_S8_UInt`; a 24-bit integer-depth tie calculation would have modelled the wrong target.

Same-frame comparisons do not eliminate work performed separately by each render. Equal CPU-observable shadow matrices, light values or probe coefficients rule out changes only in those observables. They do not prove identical GPU textures/constants or exclude all lighting causes.

## Sorting evidence has a narrow meaning

An owned diagnostic camera may test Default, FrontToBack and NoDistanceSort while preserving the acceptance camera. Inspect the pinned pipeline source and actual GPU behaviour; these modes need not differ equally on every backend. A changed result supports order dependence. It does not by itself establish coplanarity, equal depth, a batching defect or a unique foreground surface.

A CPU depth census must identify actual draw identity and material slot, represent culling/LOD/alpha/deformation uncertainty, and retain unprocessed or no-hit rays. Do not merge distinct surfaces simply because both hits are near triangle edges. Genuine shared-edge adjacency is different from a distinct nonshared boundary. Do not count mutually exclusive LODs as simultaneously drawn surfaces. Centre-ray results do not certify multisample coverage.

## First-render shader topology is separate from material values

In one pinned URP run, both the original and copied material reported one unnamed pass before the first render and nine named passes afterwards. Stored property-name inventories and keywords did not change. That supports a shared effective shader-topology transition; the engine-internal cause and complete value parity were not established by that names-only diagnostic.

Keep distinct guards for source/copy identity, values, textures and transforms, queue, keywords, active pass topology, and per-material pass-enable state. A source/copy-only comparison can miss both changing together. Freeze the states that the contract requires to remain invariant and allow only specifically validated topology transitions. Check actual shader source and the pinned public APIs; an enabled-state query alone is not proof that a pass exists. Do not discard the first render, warm up until green or exempt all material drift.

Later work isolated a selected-SubShader tag change at the same first-render boundary and validated a V3-only correction while retaining non-tag preservation checks. Read [selection-aware-material-guards.md](selection-aware-material-guards.md) for the tested approach and its limits; pass-layout observations alone were insufficient to establish it.

## Separate verdicts

`DIAGNOSTIC_VALID` means the setup and files met the experiment contract. It can coexist with `PRESERVATION_FAIL`. A Unity test process returning success is not itself a visual-quality verdict. Report diagnostic validity, repair effect, preservation and art acceptance independently.

Require non-vacuous execution evidence for the claim being tested. A resource/shadow guard can refuse before drawing while pass-off images remain exact. Pair original/owned identity redraws with actual pass-record/execution counters and an effective positive-control arm. Later isolated-fixture functional checks passed while ten memory rows remained UNKNOWN, so the overall result correctly stayed INVALID. Existing diagnostic authorization must explicitly cover any collection under an unknown budget; it is not implied by these lessons.

Match the launch filter to the reviewed source or compiled/discovered test entry, then require the expected nonzero test count and image outputs. One capture process exited zero after a method rename but selected no tests. Its successful asset build remained reusable; only capture needed correction.

## Antialiasing response does not certify sample ownership

A later fourteen-image trial had exact repeats, unchanged water/foot comparisons and 31 strict foreground residuals. All 31 showed an owned-colour response at four samples, with none detected at those locations at one sample. This supports a partial/background-coverage explanation at that view. It does not establish exclusive sample ownership, absence of presence effects or permission to waive the residuals. No detected response is not proof of absence.

If a scalar weight has an uncertainty interval, `ridge.low <= background.high` means a desired ordering is compatible with some values; it is not established for all values. Under independent interval assumptions, `ridge.high <= background.low` establishes that scalar ordering, but still not subset identity of actual MSAA samples. Overlapping intervals remain unresolved. The synthetic [planning examples](../../../scripts/planning_counterexamples.py) illustrate the logic, not a GPU coverage estimator. Keep the actual acceptance contract separate.


## Separate first-render variation from installation

When B versus O fails, retain B and add a never-installed repeat B1 before installation, then capture O in the same controlled flow. Report all three comparisons: B–B1, B1–O and B–O. Do not replace the official first baseline with the repeat.

One actual control reported B–B1 = 2 pixels (at most 1/255 channel change) and B1–O = 0. Installation added no observed difference in that sequence. The original B–O assertion still failed. This supports a first-render/repeat explanation for that observation; it neither identifies an engine mechanism nor permits automatic warm-up, tolerance changes or noise subtraction.

Validate frame presence, dimensions and complete array lengths before saving or comparing pixels. Missing/short evidence is INVALID, never a zero count or comparison of a convenient prefix. Compute the three counts from the same complete frames. Contradictory summary counts are invalid: if B1 equals O exactly, their differences from B must be equal. A zero installation delta alongside a recorded first-frame failure is a narrower observation than an all-contract pass.


## Separate preview collection from acceptance

A strict harness may stop on reference instability before reaching the candidate. When the user still needs images to judge art, a separately scoped observation mode can collect them while preserving the strict failure. It must not inherit the strict test's PASS authority.

In the source case, an explicitly reviewed observation mode completed 72 pictures but retained 52 INVALID entries. It recorded zero acceptance-gate evaluations: preservation was NOT_EVALUATED, not zero failures or PASS. All image comparisons and raw failure entries remained available; loading, missing evidence, material, ownership and cleanup faults still stopped collection. The strict mode stayed unchanged.

Track collection completion, planned/actual renders, valid/invalid comparison arms, acceptance evaluated/not-evaluated and cleanup independently. One early helper said schedule-complete after 6 of 24 renders; a later corrected sequence retained exact completion counts. Do not turn diagnostic completion into acceptance, skip missing arms or apply the observation-only continuation rule to unsafe faults.

Art review may use an INVALID preview to reject plain slopes or an abrupt ridge ending. It cannot establish protected-pixel, water or original-foot preservation. Conversely, a texture asset containing noise or bands does not prove those features read at the actual viewing distance. Inspect the final images before choosing a texture, UV, fog, normal or shader repair; do not claim an untested mechanism from appearance alone.
