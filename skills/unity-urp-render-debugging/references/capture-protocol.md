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

## Separate verdicts

`DIAGNOSTIC_VALID` means the setup and files met the experiment contract. It can coexist with `PRESERVATION_FAIL`. A Unity test process returning success is not itself a visual-quality verdict. Report diagnostic validity, repair effect, preservation and art acceptance independently.
