# Replay evidence and capability-tool review

These lessons were reproduced through source review and compiled counterexamples against an unexecuted Frame Debugger draft. They are **not** a tested Unity automation implementation or proof that the target Editor supports the proposed programmatic interface. Recheck the pinned version, actual available API and native behaviour before using any helper.

## Resolved colour transitions are not pixel history

A replay step whose resolved pixel colour changes is evidence of that colour transition. It is not necessarily the last GPU writer. A later draw can write exactly the same colour; blending and multisample resolution can combine multiple contributions. No colour change does not mean no write, and the last visible change does not identify a unique sample owner.

Use the term **resolved-colour replay transition** unless a tool supplies actual validated pixel/sample history. Keep batching, blending, depth, multisample, resolve and unobserved-input hypotheses conditional. Do not propose a product repair solely from a last-change label.

## Dimensions do not identify a render target

Several camera targets or attachments can have the same width and height. Bind the actual capture generation, camera, render target, attachment/subresource and relevant descriptor, plus the event table used for the replay. Refresh event data after changing the replay limit instead of assuming a cached target still describes the new output.

Verify full-colour replay endpoints against the intended baseline/candidate images and check repeat stability. A different endpoint hash caused by pixels outside the selected anchors does not establish that the anchors exercised the required transitions. Unknown camera/target mapping or an incomplete resolve path is a HOLD for that inference.

## Require positive controls

A capability fixture needs a known, observed colour-changing draw at its intended anchors, a same-colour write control and sufficiently identified event/target association. A report that sees zero anchor transitions, zero demonstrated draws or only unrelated full-image changes has not proved the capability. Fail closed or describe a genuinely demonstrated subset; do not mark missing controls as an informational warning under an overall success verdict.

Start with a tiny synthetic fixture before using private product images or executing thousands of replay steps. Programmatic and manual fallback paths are distinct experiments; neither should run automatically after a capability failure.

## Missing object association is not a non-draw event

A batched draw can lack a unique object association. Classify known draw/batch semantics before treating a null object as meaningful. Positively identify clears, blits and resolves using the pinned interface. Unknown event kinds remain unknown. A record with a null object and a batch type must not silently become 'non-draw', bypassing target-association checks.

If the protocol promises an unchanged event table, compare the stable facts it actually relies on: type, association, target/attachments, counts and relevant pass/shader/depth/blend metadata. A hash of only type and object does not establish all those invariants. Do not assume fields are stable across different replay limits before testing that premise.

## Cleanup must cover partial side effects and iterator failure

A setter may enable the debugger and then throw. Marking ownership only after the call returns can leave the debugger on with no cleanup owner. With an OFF precondition, track an enable attempt before invocation, inspect actual state on failure and verify final OFF. If the debugger was already owned by another session, abort instead of claiming or disabling it.

Put restoration, debugger shutdown, owned-object destruction, scene unloading and failure-receipt handling inside exception-safe cleanup paths. Code after a `finally` block is skipped if an exception propagates. Include nested enumerator exceptions and disposal/cancellation, not only happy-return tests. Report cleanup failures rather than swallowing them. The synthetic Python examples demonstrate the partial-side-effect problem; they do not test Unity's debugger.
