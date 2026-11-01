# Evidence and limits

Evidence cutoff: **2026-11-01 02:55 UTC**, before the proposed entrance-sky visibility correction was implemented. Environment configuration: Unity 6000.3.26f1, URP 17.3.0; local native observations on Metal. Quest 3 was the project target, not the backend on which these measurements prove success.

This original snapshot is retained. The [dated addendum](update-2026-11-01.md) extends the evidence through 12:55 UTC, including a validated material correction and first actual V3 bake. Statements about proposals and zero bakes below describe the original cutoff, not the later status.

The machine-readable [observations](observations.json) contain curated aggregate excerpts and SHA-256 hashes of their source reports. Raw reports remain private because they include project paths and private artifact references. Hashes establish bindings for the author's audit; readers cannot independently reproduce Unity behaviour from hashes alone. Synthetic examples reproduce only the stated mathematical or evidence-handling mistakes.

| ID | Observation | Supported lesson | Not established |
|---|---|---|---|
| E01 | Exact live GPU draw slice matched all 8,586 tested corners, with zero position/normal/UV mismatch | Verify actual draw-space inputs | Pixel identity, portable readback or headset performance |
| E02 | Full 16-view run: 902 foreground changes, 39 gap columns; water and Entrance unchanged | Separate preserved subsystems from remaining failures | Overall render acceptance |
| E03 | Sorting arm reduced own-baseline errors 52→2 / 110→27, but changed original baseline 74 / 69 | Alternative baselines must be checked | A valid camera-switch fix or a unique depth mechanism |
| E04 | Every remaining gap column included non-upward rays below the permitted height floor | Above-floor skirts cannot fill those rays | Permission to change the floor or a complete terrain certificate |
| E05 | Scene-exit correction: 25 PlayMode checks passed without skips; both observed unload orders handled | Test real lifecycle ordering and cleanup | Visual acceptance |
| E06 | Matched queue comparison 52→45 / 110→59; six north-view pixels appeared only in trial | Partial measurable queue effect | Complete foreground preservation or a universal queue recommendation |
| E07 | First render changed both materials from one unnamed pass to nine named passes; stored names/keywords stable | Distinguish active shader topology from stored material state | Complete value parity or an engine-internal root cause |
| E08 | V3: 35 functional checks plus one readiness check passed; zero real V3 bakes at this stage | Functional readiness is separate from art/render acceptance | Finished mountain quality |
| E09 | Proposed far terrain actually intersected entrance sky geometry | Correlated zone visibility is not geometric separation | A validated sky-absence solution |

## What remains a proposal or interpretation?

The grounded far ridge, volcanic landforms and rock/grass texture design aimed to replace pale regular terraces. Source was implemented and checked, but there was no accepted V3 bake/render at the cutoff. The conditional sky-absence plan was reviewed, amended and awaiting specific release; no public claim here promotes it to an implemented fix.

The workflow advice to stop repeating ineffective diagnostics and prioritise a concrete visual intervention is a synthesis of the failed iteration pattern, not a measured reduction in model cost or development time. This repository aims to save rediscovery; it makes no quantified speedup claim.
