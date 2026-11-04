# Preservation-first architecture and visible surface detail

Use this when a replacement repeatedly disturbs protected visuals, or new terrain passes geometry checks but contributes little to the image. These are bounded case lessons, not a universal instruction to retain every original mountain.

## Separate replacing from adding

Retiring an original renderer and drawing a replacement changes two things: the new draw contribution and the original depth/occlusion context. Turning off only the new draw does not recreate the original baseline. Material copies and installation state can introduce further differences.

If replacement repair stalls, test whether keeping the original drawing and adding separated distant terrain can satisfy the actual brief. This trades freedom to change the original silhouette for stable original draw context. Validate the original's live geometry and actual new triangles against the project's separation, water and domain rules. Identity bindings or a name-based exemption are not geometry evidence.

In the source case, the original overlapped a proposed separation cylinder and some initial far rows. Binding it as a foreign renderer did not justify labelling it separated. The revised prototype needed a live content-bound boundary and terrain proved outside it. Its own two-view ON captures then had zero foreground, water and Entrance differences; cleanup passed. The complete capture still failed its separate first-frame assertion, and the images were rejected because the original flat faces hid much of the new landscape.

Choose this approach only if a visible additive result can meet the brief. Preservation with hidden terrain is not a product win. A failed replacement does not prove the original's retirement was its unique cause.

## Diagnose which visual dimension is missing

Inspect the actual representative images and distinguish:

- **Visibility:** does the new mass clear the existing horizon at useful views?
- **Silhouette and form:** do broad shapes, shoulders, gullies and scale read convincingly?
- **Surface detail:** do the visible faces need rock, scree, grass or erosion variation?
- **Depth:** do contrast, atmospheric colour and overlap communicate distance?

A height increase can expose more of a plain surface without repairing its form or detail. In the tested source candidate it also introduced one protected-pixel difference despite passing geometry budgets. Reject the candidate on its own preservation and visual evidence; do not keep sweeping height merely because the mesh fits the cap.

If surface detail is the main issue, consider a material change or surface treatment only within the target project's permissions. Such a treatment cannot repair a silhouette the brief requires to change.

## Verify the surface you intend to treat

A baked base strip may contain only a selected subset of a static-batched renderer. Compare selection rules, triangle counts and the actual drawn submesh slice before planning a full-surface operation. The source case had 636 selected foot-strip triangles versus 2,862 triangles in the full drawn slice. A successful subset comparison did not extend that subset resource to the full mountain.

Distinguish build-time verification from live freshness. Mesh identities, counts and source hashes alone do not show that uploaded vertex/index bytes remain unchanged. Bind the attributes and matrices the operation depends on; report which are actually re-read and when. A live positions proof does not also prove normals, UVs, material state or owned GPU bytes.

## Treat co-depth overlays as a hypothesis

Bit-identical decoded positions do not guarantee identical clip-space depth or sample coverage after different shader paths. A depth-equality overlay can miss intended samples or pass at an equal stored depth from another surface. CPU geometry separation does not itself bound GPU interpolation/rounding.

A useful feasibility test can compare an original key-colour render, an exact repeat, the ordinary original, and full/subset overlays at fixed views and actual allocated AA/depth formats. Verify uploaded buffer contents and restore original material state. Record missing coverage, extra coverage, water-region changes and cleanup separately. This is a possible test design, not a validated implementation supplied here.

Interpret a resolved 8-bit RGB match only at its tested poses, sample counts and backend. It cannot identify which MSAA samples matched, certify all views, exclude leaks elsewhere or establish stereo safety. Geometry that cannot intersect a direct eye-to-water ray may still change reflections, refraction or sampled opaque colour. Keep the water and full product captures decisive.

The early 4 November snapshot contained only the source draft. Later actual tests changed the conclusion: source-slice and owned-upload readback feasibility passed, but stable 4-sample reference arms had 54 and 59 full-overlay differences. One single-sample north arm matched exactly; another single-sample arm was INVALID due to its repeat. The equal-depth overlay route was rejected under the unchanged exact criteria. North's full-overlay arm had four water-key extra pixels; the subset arm did not. These results do not identify a unique rounding mechanism or establish subset leak-freedom.

Keep each arm's validity separate from overall test status. A valid rejecting arm can stop a hypothesis even when another arm makes the overall result INVALID. A passing single-sample arm cannot override a valid multisample rejection. Desktop readback feasibility still says nothing about acceptable headset frame time.
