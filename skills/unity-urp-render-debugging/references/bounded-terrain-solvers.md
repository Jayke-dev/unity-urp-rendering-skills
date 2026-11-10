# Bounded terrain feasibility before another render

Use this reference when repeated numerical or budget repairs produce no accepted terrain. It distils source and actual-data failures, not a general optimiser or a proven rendering recipe. See E69–E73 in the [10 November update](../../../evidence/update-2026-11-10.md).

## Check necessity before improving convergence

Put consequences of existing acceptance constraints into early selection. If a required crest gap is `a - b >= g`, valid bounds imply `b <= upper(a) - g` and `a >= lower(b) + g`. Propagation narrows a necessary region; it does not replace the final crest test.

In the source case, including an existing crest-gap consequence made two required valley visibility regions empty at the selected layout. More height iterations could not repair that placement. Nonempty necessary regions would not prove feasibility. To reject an entire movement domain, additionally prove that the retained rows, supports, exclusions and bounds are invariant throughout that domain. A contradiction at one point is not a global geometry impossibility.

First verify the arithmetic producing the constraints. An earlier apparent neighboring-segment obstruction came from mixing represented floating-point coordinates with exact arithmetic. Rationalising the represented coordinates corrected the calculation without moving them or relaxing a threshold. Do not preserve the old obstruction as a geometric fact after correcting its cause.

If a different owned point must move, review every affected trace, parent mapping, UV embedding and coverage bridge before implementation. A four-face, one-trace proof does not automatically cover a fifteen-face point shared by two traces. Protected geometry and final acceptance remain governed by the original contract.

## Preserve an independent exact gate

A small public coupled-constraint example can explain why one-row updates alternate while a joint step succeeds. It cannot predict actual iteration count, resource completion or landscape feasibility. Keep the original true-merit calculation, global failure checks, rounded final representation and independent exact verification.

Share expensive full-bound evaluations across row gradients when their inputs are identical; do not omit checks outside the selected rows' support. In the case study, those global checks could refuse a probe even when its selected local rows looked valid.

Retain old positive fixtures. A new three-row mechanism passed its own example but refused an existing positive narrow fixture because its computed direction failed a proposal residual check. A reviewed QR arithmetic change restored the unchanged fixture. This cleared a source-level blocker, not the actual landscape constraints. Do not loosen an acceptance threshold or alter the positive fixture to conceal the regression.

## Account for the complete bounded attempt

Reserve enough operations, bytes and time for independent final verification before starting each stage. Use one root counter across admission, derivation, hashing, selection, numerical work and final checks. Keep cumulative allocation, retained memory, process RSS and GPU product memory distinct. A charged-byte reduction is not measured device memory savings.

Avoid real work rather than lowering its fee. Canonical key-order reuse reduced charged allocation for one retained-record digest schedule by 277,330,142 bytes while preserving hashes. Other costs were excluded, and a later actual run still stopped before producing a tuple. A microbenchmark or partial schedule does not establish whole-attempt capacity.

For reusable score storage, allocate owned bounded containers once, recompute every score from live inputs, reset excluded entries, and detach returned results. Test cold and warm calls on different inputs, foreign ownership, failure paths and object reuse. Remaining float, label, sort and result allocations still need honest charges. A zero-coefficient fixture that showed no saving must remain recorded even if a structurally representative fixture later shows one.

Retain stage-start costs, accepted/rejected steps, actual current merit and the blocking resource axis. The last logged pre-trial margin can be stale; label a read-only observation of an already evaluated internal state separately from a new proposal. An internal iterate is not an accepted tuple.

## End a failed route with a decision

Do not rerun a closed attempt merely because it almost fits a budget. Select one correction supported by its failure: arithmetic, allocation, convergence or layout necessity. After finite source review, either run one freshly identified actual attempt or report the specific blocker. Avoid repeatedly proving unchanged identity controls.

At the latest included actual attempt, the QR method accepted six internal steps, then stopped on operation headroom with negative merit. No accepted tuple, new asset or new render resulted. The subsequent crest/layout finding explains why changing the selection problem is more useful than another accounting-only retry at that same placement. Full geometry, pixel, visual and target-device acceptance remain separate.
