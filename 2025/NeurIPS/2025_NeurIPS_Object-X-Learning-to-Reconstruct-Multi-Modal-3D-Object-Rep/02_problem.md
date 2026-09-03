# Problem - Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=nI7wKr4eop; PDF retrieval source: https://arxiv.org/pdf/2506.04789. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction)): However, a key limitation is that these embeddings typically lack a generative or reconstructive capability; they cannot be decoded back into explicit object geometry or appearance.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Learning effective multi-modal 3D representations of objects is essential for numerous applications, such as augmented reality and robotics.
- **p. 1 / Abstract - extractive body cue:** Existing methods often rely on task-specific embeddings that are tailored either for semantic understanding or geometric reconstruction.
- **p. 1 / Abstract - extractive body cue:** As a result, these embeddings typically cannot be decoded into explicit geometry and simultaneously reused across tasks.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose Object-X, a versatile multi-modal object representation framework capable of encoding rich object embeddings (e.g., images, point cloud, text) and decoding ...
- **p. 1 / Abstract - extractive body cue:** Object-X operates by geometrically grounding the captured modalities in a 3D voxel grid and learning an unstructured embedding fusing the information from the voxels with ...
- **p. 3 / 1 Introduction - extractive body cue:** However, a key limitation is that these embeddings typically lack a generative or reconstructive capability; they cannot be decoded back into explicit object geometry or ...
- **p. 2 / 1 Introduction - extractive body cue:** However, a critical limitation persists: existing object embeddings are generally learned for specific tasks and cannot be decoded to reconstruct the explicit, high-fidelity appearance and ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, a key limitation is that these embeddings typically lack a generative or reconstructive capability; they cannot be decoded back into explicit ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | 3 Learning Versatile Object Embeddings We propose Object-X, taking a reconstructed scene with a 3D object segmentation as input and learning a ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Learning, Versatile, Object, Embeddings, Object-X, taking, reconstructed, scene, segmentation, input | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | forces, systems, retain, original, high-bandwidth, source, data, images | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Learning, Versatile, Object, Embeddings, Object-X, taking, reconstructed, scene, segmentation, input | p. 4 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction) |
| Decision / output variable | geometry/map/query r; body terms: Learning, Versatile, Object, Embeddings, Object-X, taking, reconstructed, scene | p. 4 (1 Introduction), p. 5 (1 Introduction), p. 10 (Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Unlike, SGAligner, explicitly, trained, task, point, cloud, object-level | p. 10 (Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 9 (Method), p. 9 (Method), p. 10 (Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** However, a critical limitation persists: existing object embeddings are generally learned for specific tasks and cannot be decoded to reconstruct the explicit, high-fidelity appearance and ...
- **p. 2 / 1 Introduction - extractive body cue:** As a consequence, they inherently lack object-level modularity, making it difficult to reason about individual objects, efficiently incorporate other modalities (e.g., text, semantics), or easily ...
- **p. 3 / 1 Introduction - extractive body cue:** Object-X addresses this gap by learning rich, multi-modal object embeddings that are explicitly designed to be decodable into high-fidelity 3DGS representations.
- **p. 4 / 1 Introduction - extractive body cue:** More recent works explore structured latent spaces for improved scalability and control in generation.

## What the Paper Changes

PDF body contribution framing (p. 4 (1 Introduction), p. 5 (1 Introduction), p. 10 (Method), p. 10 (Method), p. 3 (1 Introduction)): 3 Learning Versatile Object Embeddings We propose Object-X, taking a reconstructed scene with a 3D object segmentation as input and learning a compact and descriptive embedding for each object from ...

- **p. 5 / 1 Introduction - extractive body cue:** Specifically, we introduce a decompression function fdecomp that maps w back to a predicted ˆz = {ˆzi, pi}L i=1.
- **p. 10 / Method - extractive body cue:** Our method, along with SceneGraphLoc and the recent CrossOver [23], uses a ViT to extract per-patch object embeddings from the query image.
- **p. 10 / Method - extractive body cue:** Unlike SGAligner, explicitly trained for this task using point cloud and object-level modalities, our method relies solely on the proposed Object-X embedding trained with reconstruction ...
- **p. 3 / 1 Introduction - extractive body cue:** The embedding is trained with a masked mean squared error loss to ensure accurate reconstruction of the SLat, which in turn enables decoding into 3D ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | Despite these advances, Object-X has limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Furthermore, while promising in zero-shot scenarios for tasks like single-image object reconstruction, performance does not yet consistently match ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Scenes, where SceneGraphFusion fails to generate annotations, are excluded. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Since ScanNet does not provide scene graph annotations, we apply SceneGraphFusion [30] on RGB-D sequences to generate 3D ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction), p. 9 (Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), interface p. 4 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction), p. 9 (Method), objective p. 10 (Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
