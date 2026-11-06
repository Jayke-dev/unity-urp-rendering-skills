# Actual draw geometry and ownership

## The imported mesh may not be what is drawn

Before reproducing an existing surface, establish the actual vertex/index buffers, renderer slice/submeshes, material slots, vertex attributes/streams/strides/offsets and coordinate frame. Static batching and nonuniform transforms can invalidate an export based only on prefab CPU vertices. Avoid changing batching merely to make a preservation test easier.

The source case verified the live statically batched draw slice through read-only GPU acquisition on Metal and compared 8,586 position/normal/UV corners bit for bit. That establishes one concrete acquisition route in that environment. It is not proof that all meshes are readable on all platforms or that matching geometry reproduces every shading result.

Later exact-order copy controls still changed 32 protected pixels; partitioning changed the same residual set plus other allowed pixels. Retire a non-neutral route rather than treating another byte proof as a repair. A separate lit-redraw experiment exposed missing draw context, then reached exact native controls only in an isolated synthetic fixture. Read [lit redraw and fixture isolation](lit-redraw-and-fixture-isolation.md) when lighting, culling and attachments are the relevant next decision.

Use the public buffer APIs and exact observed layout. If your contract forbids changing foreign buffer targets, do not silently add Raw/CopySource flags. Hold unsupported access. Snapshot count/stride/target/byte metadata while handles are valid; one source bug tried to read metadata after disposal. When verifying drift, identities and counts alone cannot establish unchanged contents. Recompute the needed content proof at the lifecycle point where it is used.

## Asynchronous requests need an owner

Tie each request to a generation/installation ticket. Cancelling invalidates that generation before cleanup, so a late callback cannot commit stale geometry, revive a hidden replacement or restore an obsolete owner. Settle/cancel paths should be idempotent and preserve pending recovery when restoration genuinely fails.

Release owned resources exactly through their designated owner. Distinguish borrowed mesh resources from owned wrappers/readback storage. Do not dispose a resource still needed by an outstanding operation. Preserve errors and bounded completion/timeout outcomes instead of retrying indefinitely.

Request completion is not proof that request storage has retired. Budget overlapping CPU/GPU staging explicitly, including cancellation/error paths; retain a source when settlement cannot be established and make cleanup faults invalidate success. A later native fixture issued, consumed and retired twenty requests with maximum one live. Its ten unknown memory rows still prevented overall acceptance; successful sequencing did not measure every engine allocation.

Useful integration tests: successful completion, cancellation during acquisition, late callback after cancellation, readback failure/timeout, material/geometry drift before commit, explicit disable, re-enable and real scene exit. Assert no remaining owned nodes, wrappers, tickets or leases after valid cleanup. A shared state object's failure to restore is a visible recovery condition, not a false success.

## Scene unload has more than one observed order

In real scene-unload tests the original object was sometimes already destroyed at the replacement's callback and sometimes still alive. A rule that recognises valid exit only when the original is dead rejected the second order.

For an owned replacement, retain the original assignment and owning-scene facts independently of Unity's destroyed-object equality. Distinguish a genuine owner-scene unload from destruction in a loaded scene or loss of an unrelated object. The correct predicate depends on your actual ownership model; do not universally suppress null-object errors. Restore a living borrowed original or end its ownership record if already destroyed. Keep genuine loaded-scene faults visible.

Test actual scene unload without a pre-test teardown that hides the bug. Record alive/dead order; require cleanup rather than one guessed order. Source predicate tests and observed native callback orders are different evidence.

## Ordinary logs are not functional failures

The source project's new tests passed cleanup assertions but failed an explicit 'no unexpected logs' assertion on ordinary informational messages. Scope additional log checks to the severities and exact errors required by the contract while retaining the test runner's normal unexpected-error handling. Never mute genuine Error/Assert/Exception logs or remove cleanup assertions to get green tests.
