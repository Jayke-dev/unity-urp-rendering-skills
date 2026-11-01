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

No Unity documentation or package source is vendored here. The application-specific shader transition, effective depth format, numerical counts and cleanup observations come from the [case study](../evidence/case-study.md); they are not asserted as universal API behaviour.
