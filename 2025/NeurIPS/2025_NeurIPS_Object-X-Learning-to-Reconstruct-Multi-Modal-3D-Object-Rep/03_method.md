# Method - Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=nI7wKr4eop; PDF retrieval source: https://arxiv.org/pdf/2506.04789. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 9 (Method), p. 9 (Method), p. 10 (Method), p. 10 (Method)): Object-X is then applied to obtain the object embedding from this input which is then fed directly into our decoder.

## Method Body Digest

- **p. 9 / Method - extractive body cue:** Object-X is then applied to obtain the object embedding from this input which is then fed directly into our decoder.
- **p. 9 / Method - extractive body cue:** In contrast, Object-X focuses on reconstruction rather than generation, leveraging voxel-grounded latent representations to maintain geometric consistency even under large appearance or domain shifts.
- **p. 10 / Method - extractive body cue:** In constrast to the baselines, Object-X is used without training on this task.
- **p. 10 / Method - extractive body cue:** We compare Object-X to 3DGS [28] optimized on all unmasked images, and two 12-view baselines: 3DGS (12V) and 2DGS (12V), which optimize scenes using a ...
- **p. 10 / Method - extractive body cue:** Unlike SGAligner, explicitly trained for this task using point cloud and object-level modalities, our method relies solely on the proposed Object-X embedding trained with reconstruction ...
- **p. 9 / Method - extractive body cue:** We compare our approach to 3DGS [28] which optimizes 3D Gaussian splats based on a single masked image.
- **p. 9 / Method - extractive body cue:** Runtime remains comparable to the 12-view baselines, and significantly faster than full-scene 3DGS optimization.
- **p. 4 / 1 Introduction - extractive body cue:** 3 Learning Versatile Object Embeddings We propose Object-X, taking a reconstructed scene with a 3D object segmentation as input and learning a compact and descriptive ...

## Design Rationale

- **p. 4 / 1 Introduction - extractive body cue:** 3 Learning Versatile Object Embeddings We propose Object-X, taking a reconstructed scene with a 3D object segmentation as input and learning a compact and descriptive ...
- **p. 5 / 1 Introduction - extractive body cue:** Specifically, we introduce a decompression function fdecomp that maps w back to a predicted ˆz = {ˆzi, pi}L i=1.
- **p. 10 / Method - extractive body cue:** Our method, along with SceneGraphLoc and the recent CrossOver [23], uses a ViT to extract per-patch object embeddings from the query image.

## Source Evidence Cues

- **p. 9 / Method - extractive body cue:** Object-X is then applied to obtain the object embedding from this input which is then fed directly into our decoder.
- **p. 9 / Method - extractive body cue:** In contrast, Object-X focuses on reconstruction rather than generation, leveraging voxel-grounded latent representations to maintain geometric consistency even under large appearance or domain shifts.
- **p. 10 / Method - extractive body cue:** In constrast to the baselines, Object-X is used without training on this task.
- **p. 10 / Method - extractive body cue:** We compare Object-X to 3DGS [28] optimized on all unmasked images, and two 12-view baselines: 3DGS (12V) and 2DGS (12V), which optimize scenes using a ...
- **Detected method headings:** Method (p. 9)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Object-X is then applied to obtain the object embedding from this input which is then fed directly into our decoder. | p. 9 (Method), p. 9 (Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | In contrast, Object-X focuses on reconstruction rather than generation, leveraging voxel-grounded latent representations to maintain geometric consistency even under large appearance or ... | p. 9 (Method), p. 10 (Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | In constrast to the baselines, Object-X is used without training on this task. | p. 10 (Method), p. 10 (Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 10 / Method - extractive body cue:** Unlike SGAligner, explicitly trained for this task using point cloud and object-level modalities, our method relies solely on the proposed Object-X embedding trained with reconstruction ...
- **p. 9 / Method - extractive body cue:** We compare our approach to 3DGS [28] which optimizes 3D Gaussian splats based on a single masked image.
- **p. 9 / Method - extractive body cue:** Runtime remains comparable to the 12-view baselines, and significantly faster than full-scene 3DGS optimization.
- **p. 10 / Method - extractive body cue:** We compare Object-X to 3DGS [28] optimized on all unmasked images, and two 12-view baselines: 3DGS (12V) and 2DGS (12V), which optimize scenes using a ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 10 (Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Learning, Versatile, Object, Embeddings, Object-X, taking, reconstructed, scene, segmentation, input, compact, descriptive, embedding, associated | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Learning, Versatile, Object, Embeddings, Object-X, taking, reconstructed, scene, segmentation, input | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Learning, Versatile, Object, Embeddings, Object-X, taking, reconstructed, scene, segmentation, input | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Unlike, SGAligner, explicitly, trained, task, point, cloud, object-level, modalities, relies | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 1 Introduction - extractive body cue:** 3 Learning Versatile Object Embeddings We propose Object-X, taking a reconstructed scene with a 3D object segmentation as input and learning a compact and descriptive ...
- **p. 4 / 1 Introduction - extractive body cue:** 3.1 Structured Latents from Multi-View Images Let a set of object instances O be given, where each object o = (P, I, M, A, . ...
- **p. 2 / 1 Introduction - extractive body cue:** This forces systems to retain the original, high-bandwidth source data (images, point clouds, meshes) alongside the learned embeddings, undermining the goals of creating a compact, ...
- **p. 9 / Method - extractive body cue:** Using the object mask and depth map, we lift the object pixels in 3D, obtaining a point cloud.
- **p. 10 / Method - extractive body cue:** We indicate whether a method uses point cloud (P), image (I), other modalities like object attribute and relationship (O), or the proposed U-3DGS embedding.
- **p. 2 / 1 Introduction - extractive body cue:** More recently, implicit neural and Gaussian representations, notably Neural Radiance Fields (NeRF) [15] and 3D Gaussian Splatting (3DGS) [10], have achieved state-of-the-art results in synthesising ...
- **p. 9 / Method - extractive body cue:** Retrieval recall at various thresholds using various methods and input modalities.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Compared to 3RScan, ScanNet captures RGB-D sequences at a higher frame rate with minimal motion between consecutive frames. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | To ensure diverse viewpoints, we sample one image every 25 frames. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | To ensure diverse viewpoints, we sample one image every 25 frames. | hardware, batch and throughput |

## Training vs Inference

- **p. 10 / Method - extractive body cue:** In constrast to the baselines, Object-X is used without training on this task.
- **p. 10 / Method - extractive body cue:** We compare Object-X to 3DGS [28] optimized on all unmasked images, and two 12-view baselines: 3DGS (12V) and 2DGS (12V), which optimize scenes using a ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Object-X, then, applied, obtain, object, embedding, input, directly, decoder, contrast, focuses, reconstruction, rather, generation, leveraging, voxel-grounded, latent, representations, maintain, geometric.
- **Relevant PDF headings:** Method (p. 9).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Since the test set lacks such annotations, we reorganized the original validation split, allocating 34 scenes (17 rooms) for validation and 123 ... | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Semantic / temporal fusion | Even without training, we achieve the highest novel view synthesis scores compared to the baselines, being the closest to the reference 3DGS ... | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Robot query / planning handoff | While Object-X achieves lower SSIM and PSNR compared to 3DGS (12V), it significantly outperforms all methods in geometric accuracy. | p. 8 (4 Experiments), p. 8 (4 Experiments) |

## Failure and Ablation Link

- **p. 7 / 4 Experiments - extractive body cue:** Objects without available images were removed to ensure a consistent evaluation.
- **p. 26 / Figure/Table caption - extractive body cue:** Table 7: Ablation study on occlusion. Before encoding an object, we randomly select a point on its surface and remove all parts within a spherical ...
- **p. 26 / Figure/Table caption - extractive body cue:** Table 6: Ablation study on latent dimensions. Mean and median LPIPS and PSNR on a subset of scans from the test set. We compare the ...
- **p. 6 / 4 Experiments - extractive body cue:** Ablation studies, more visuals, and detailed descriptions of baselines are provided in the supplementary material.
- **p. 7 / 4 Experiments - extractive body cue:** As in 3RScan, objects without associated images are discarded.
- **p. 8 / 4 Experiments - extractive body cue:** Even without training, we achieve the highest novel view synthesis scores compared to the baselines, being the closest to the reference 3DGS reconstruction.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Object-X learns object-centric embeddings from an input object segmentation of a 3D scene reconstruction. The embeddings learned from multi-modal data (e.g., mesh, images, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 9 (Method), p. 9 (Method), p. 10 (Method), p. 10 (Method), objective p. 10 (Method), p. 9 (Method), p. 9 (Method), p. 10 (Method), temporal p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (Method), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
