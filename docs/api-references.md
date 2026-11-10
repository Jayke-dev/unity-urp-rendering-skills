# Official API references

Checked 2026-11-01. These explain APIs, not the private project's measured results. Recheck against the installed editor and pipeline package before implementation.

- [Mesh.GetVertexBuffer (6000.3)](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityengine/mesh/getvertexbuffer): direct GPU vertex-buffer access; query actual layout and reacquire after recreation. CPU and GPU data are distinct.
- [AsyncGPUReadback.Request (6000.3)](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityengine/rendering/asyncgpureadback/request): async acquisition and error reporting. Keep a temporary source texture alive until the request completes.
- [OpaqueSortMode (6000.3)](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityengine/rendering/opaquesortmode): sorting trades batching/state changes against GPU efficiency; default distance sorting depends on the GPU.
- [Material.GetShaderPassEnabled (6000.3)](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityengine/material/getshaderpassenabled): a pass not explicitly disabled can report enabled even if absent. This query alone does not establish active topology.
- [RenderPipelineManager.beginCameraRendering (6000.3)](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityengine/rendering/renderpipelinemanager/begincamerarendering): a per-camera callback used by URP/HDRP. It is not a guarantee against subsequent state writers.
- [Material.GetTag (6000.3)](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityengine/material/gettag): without fallback search, queries the currently used SubShader; it is not an immutable serialized-property snapshot.
- [Shader.FindSubshaderTagValue (6000.3)](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Shader.FindSubshaderTagValue.html): queries a named tag in a specified declared SubShader, useful as an independent diagnostic basis when selection is known.
- [Material.SetOverrideTag (6000.3)](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityengine/material/setoverridetag): material overrides can supersede shader tag values; shader declarations alone do not describe every effective material tag.
- [Frame Debugger introduction (6000.3)](https://docs.unity.com/en-us/engine/6000.3/manual/analysis/graphics-performance-profiling/profile-rendering/frame-debugger/frame-debugger): stepping rendering events and examining scene state. This link does not establish the reliability of a custom programmatic wrapper or sample-level pixel history.
- [Renderer.bounds (6000.3)](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityengine/renderer/bounds): world-space bounds and custom overrides. Clone comparisons must inspect their final state; do not assume equal mesh references imply equal bounds.

No Unity documentation or package source is vendored here. The application-specific shader transition, effective depth format, numerical counts and cleanup observations come from the [case study](../evidence/case-study.md); they are not asserted as universal API behaviour.


Additional reference checked 2026-11-04:

- [AssetDatabase.GetDependencies (6000.3)](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityeditor/assetdatabase/getdependencies): distinguishes direct and recursive asset references; recursive results contain the requested root. Root inclusion alone is not a positive-length cycle witness. The source case's actual graph evidence is in the afternoon addendum, not established by the API documentation.

Additional workflow reference checked 2026-11-05:

- [Claude Code Read tool](https://code.claude.com/docs/en/tools-reference#read-tool-behavior): supported image files are returned as visual content, with resizing/recompression possible. A successful image Read proves delivery of visual input; it does not certify exact pixels or the quality of the model's interpretation. The source case's verified read results are recorded in the 5 November addendum.

Additional references checked 2026-11-06:

- [CommandBuffer.DrawRenderer (6000.3)](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityengine/rendering/commandbuffer/drawrenderer): does not set up lighting-related shader inputs; reusing a lit material is not a complete draw-context setup. The case failure and later renderer-list result are separate observations, not promised API equivalence.
- [Camera.overrideSceneCullingMask (6000.3)](https://docs.unity.com/en-us/engine/6000.3/script-reference/unityengine/camera/overridescenecullingmask): camera scene-culling selection, with the related Editor scene-mask API. It does not prove isolation of every global lighting input; the native before/after controls and limitations are in the 6 November addendum.

Additional references checked 2026-11-10:

- [Blender 4.1 Python API release notes](https://developer.blender.org/docs/release_notes/4.1/python_api/): documents the read-only loop-normal change and custom-normal setter methods. Check the installed version and actual callable; it does not prove this case’s UV lifetime or storage repair.
- [Python math.fsum and math.hypot](https://docs.python.org/3/library/math.html): summation and norm APIs with documented numerical behavior. These explain available operations, not the correctness of the private QR implementation or a terrain-feasibility guarantee.
