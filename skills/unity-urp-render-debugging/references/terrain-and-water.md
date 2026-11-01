# Terrain geometry, water and visual quality

## Reject an impossible skirt before generating it

Let a forward ray be `p(t) = eye + t * direction`, with `t >= 0`. If `eye.y < floor` and `direction.y <= 0`, it cannot hit any triangle all of whose vertices have `y >= floor`. Every point of such a triangle is a convex combination of its vertices. No amount of added triangles above that floor repairs this ray.

This is conditional elementary geometry, not a complete scene certificate. The synthetic script demonstrates it. The source project had gap rays of this kind in every remaining gap column. Raising triangle density was therefore the wrong next experiment.

Likewise, a backing face can close a visible hole while intersecting a protected water sightline. Test final transformed triangles against the relevant water/viewer domain, not just vertex heights, a mesh AABB or a handful of old gap-centre rays. Check newly created gaps in the raster result too.

## Work in the actual domain

Inventory all potentially co-visible water and viewers, including entrance basins/horizons, rather than assuming the main lake is the whole domain. Verify transforms, animation bounds, sidedness and whether the water is actually filled and opaque. A nominal disk radius does not establish coverage by a polygon: the inner radius of a regular n-gon of circumradius R is `R*cos(pi/n)`. The synthetic script shows a point inside the disk but outside the polygon.

Use horizontal and vertical numerical-error bounds for their respective quantities. Reject degenerate viewer axes. Propagate unsupported/deformed materials and geometry as unresolved instead of silently dropping them. Final float32 geometry, winding, every transformed triangle and raster controls still need validation; a scalar feasibility calculation only selects a plausible design envelope.

Front/back winding changes visible coverage. Adding reverse faces only where needed can be more economical than duplicating everything, but assess all relevant viewer directions, boundary views and the real vertex/triangle budget. A CPU ray with two-sided intersections can falsely promise closure for a backface-culled GPU draw.

## Geometric separation and visibility are different contracts

A far terrain proposal intersected the source project's entrance sky dome. The dome and terrain were normally visible in different zones, but normal correlation is not a live guarantee. At the initial 02:55 UTC snapshot, preventing simultaneous drawing was still a proposal. Later integration checks exercised the conditional visibility guard and manual render paths on reviewed V2 stand-in geometry; they did not establish final V3 pixel acceptance or geometric separation.

If your project accepts a conditional visibility contract, bind the exact objects and scene identities, check relevant duplicates/LOD/probe conditions, and enforce the condition before every covered draw path. Include normal cameras, additional cameras, reflection/VR paths and explicit captures where applicable. A pre-camera callback can be followed by other writers: audit the actual order, limit the guarantee to verified paths and hold uncovered paths. Do not generalise this into 'ignore inactive geometry'.

## Budget compliance is not convincing terrain

Review macro silhouette first: broad asymmetrical masses, overlapping shoulders, natural endings and a grounded horizon. Then branching erosion/gullies and slope-following rock/dry-grass variation. Finally inspect near/far value, colour and atmospheric depth from the intended viewpoints. These are art-direction criteria, not a validated procedural recipe.

Regular horizontal terraces, pale smooth surfaces and an impressive unseen texture atlas did not achieve the source project's brief. Check how much authored terrain is actually visible through the architecture. More texture detail cannot fix a flat dominant silhouette or surfaces hidden behind accepted scenery.

Use representative crops for quick rejection and the full fixed-view set for acceptance. Keep a visible quality rubric alongside water, foreground, text and geometry gates. Desktop results do not replace headset checks.
