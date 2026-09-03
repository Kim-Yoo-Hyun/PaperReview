# Method - UrbanGS: Efficient and Scalable Architecture for Geometrically Accurate Large-Scene Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=L3utaw6SD9; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/248058. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 7 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 15 (A IMPLEMENTATION DETAILS), p. 5 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES)): First, when obtaining the global coarse 3DGS model, we first eliminate redundant Gaussians through SAGP pruning to prevent these redundant Gaussians from attracting non-contributing views and amplifying the computational load ...

## Method Body Digest

- **p. 7 / 3.1 PRELIMINARIES - extractive body cue:** First, when obtaining the global coarse 3DGS model, we first eliminate redundant Gaussians through SAGP pruning to prevent these redundant Gaussians from attracting non-contributing views ...
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** To reconstruct scene surfaces, we enforce normal priors N predicted by a pretrained monocular deep neural network (Bae & Davison, 2024) to supervise the rendered ...
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** The surface is then extracted using the Marching Cubes algorithm at the zero-level isosurface, enabling direct reconstruction of 3D geometry without relying on intermediate point ...
- **p. 5 / 3.1 PRELIMINARIES - extractive body cue:** (b) Depth-Consistent D-Normal Regularization: 3D Gaussians are rendered to depth and normal maps, depth is converted to D-normals and jointly supervised with pseudo-depth and pseudonormal ...
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** The total optimization objective is consequently augmented to: Ltotal = LRGB + λ1Ln + λ2Ldn + λ3(wd · Lid), (12) where λi(i = 1, 2, ...
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** This process brings the relative depth estimates into alignment with the scale of the multi-view geometry.We define an inverse depth loss Lid that operates on ...
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** 3D Gaussian Splatting models a scene using a collection of anisotropic 3D Gaussians G = {Gi / i ∈N}.
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** This formulation minimizes relative depth errors per pixel while enhancing distant surface accuracy where linear depth gradients diminish.

## Design Rationale

- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our main contributions are summarized below: • We propose a Depth-Consistent D-Normal Regularizer that enables holistic optimization of all Gaussian parameters (position, rotation), addressing the ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To overcome this limitation, we introduce a Depth-Consistent D-Normal Regularization framework.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We propose UrbanGS, a strategy that achieves high geometric accuracy, fidelity, and efficiency in large-scale scene reconstruction.

## Source Evidence Cues

- **p. 7 / 3.1 PRELIMINARIES - extractive body cue:** First, when obtaining the global coarse 3DGS model, we first eliminate redundant Gaussians through SAGP pruning to prevent these redundant Gaussians from attracting non-contributing views ...
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** To reconstruct scene surfaces, we enforce normal priors N predicted by a pretrained monocular deep neural network (Bae & Davison, 2024) to supervise the rendered ...
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** The surface is then extracted using the Marching Cubes algorithm at the zero-level isosurface, enabling direct reconstruction of 3D geometry without relying on intermediate point ...
- **p. 5 / 3.1 PRELIMINARIES - extractive body cue:** (b) Depth-Consistent D-Normal Regularization: 3D Gaussians are rendered to depth and normal maps, depth is converted to D-normals and jointly supervised with pseudo-depth and pseudonormal ...
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** The total optimization objective is consequently augmented to: Ltotal = LRGB + λ1Ln + λ2Ldn + λ3(wd · Lid), (12) where λi(i = 1, 2, ...
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** This process brings the relative depth estimates into alignment with the scale of the multi-view geometry.We define an inverse depth loss Lid that operates on ...
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** 3D Gaussian Splatting models a scene using a collection of anisotropic 3D Gaussians G = {Gi / i ∈N}.
- **Detected method headings:** 3 METHODOLOGY (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | First, when obtaining the global coarse 3DGS model, we first eliminate redundant Gaussians through SAGP pruning to prevent these redundant Gaussians from ... | p. 7 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To reconstruct scene surfaces, we enforce normal priors N predicted by a pretrained monocular deep neural network (Bae & Davison, 2024) to ... | p. 4 (3.1 PRELIMINARIES), p. 15 (A IMPLEMENTATION DETAILS) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The surface is then extracted using the Marching Cubes algorithm at the zero-level isosurface, enabling direct reconstruction of 3D geometry without relying ... | p. 15 (A IMPLEMENTATION DETAILS), p. 5 (3.1 PRELIMINARIES) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** This formulation minimizes relative depth errors per pixel while enhancing distant surface accuracy where linear depth gradients diminish.
- **p. 5 / 3.1 PRELIMINARIES - extractive body cue:** In urban-scale scenes, D-Normal regularization optimizes geometry through normal-depth associations but lacks explicit cross-view depth constraints, frequently causing building misalignment and street distortion-especially in distant/co ...
- **p. 5 / 3.1 PRELIMINARIES - extractive body cue:** (b) Depth-Consistent D-Normal Regularization: 3D Gaussians are rendered to depth and normal maps, depth is converted to D-normals and jointly supervised with pseudo-depth and pseudonormal ...
- **p. 6 / 3.1 PRELIMINARIES - extractive body cue:** The total optimization objective is consequently augmented to: Ltotal = LRGB + λ1Ln + λ2Ldn + λ3(wd · Lid), (12) where λi(i = 1, 2, ...
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** To reconstruct scene surfaces, we enforce normal priors N predicted by a pretrained monocular deep neural network (Bae & Davison, 2024) to supervise the rendered ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | First, rendered, depth, back-projected, point, clouds, camera, intrinsic, matrix, ensures, Gaussian, retained, only, when | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | First, rendered, depth, back-projected, point, clouds, camera, intrinsic, matrix, ensures | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contributions, summarized, below, Depth-Consistent, D-Normal, Regularizer, enables, holistic, optimization | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | formulation, minimizes, relative, depth, errors, pixel, while, enhancing, distant, surface | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.1 PRELIMINARIES - extractive body cue:** First, the rendered depth map is back-projected into point clouds{dk(n, p)}, using the camera intrinsic matrix.
- **p. 7 / 3.1 PRELIMINARIES - extractive body cue:** D.5) and ensures that a Gaussian is retained only when it simultaneously exhibits high visibility, frequent observation across views, and appropriate geometric scale.
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** To reconstruct scene surfaces, we enforce normal priors N predicted by a pretrained monocular deep neural network (Bae & Davison, 2024) to supervise the rendered ...
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** (4) In our method, the depth map is rendered by performing a weighted sum of depths (Bae & Davison, 2024; Chen et al., 2024b; Yu ...
- **p. 5 / 3.1 PRELIMINARIES - extractive body cue:** N d(n, p) = ∇vd(n, p) × ∇hd(n, p) /∇vd × ∇hd/ , (6) where d represents the 3D coordinates of a pixel obtained via ...
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** Since the Mill-19 (Yu et al., 2022), UrbanScene3D (Lin et al., 2022), and GauU-Scene (Xiong et al., 2024) datasets contain thousands of high-resolution images, we ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To ensure the reliability of depth alignment across multiple views, we propose an adaptive confidence weighting strategy that dynamically ad2
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | While 3D Gaussian Splatting (3DGS) enables high-quality, real-time rendering for bounded scenes, its extension to large-scale urban environments gives rise to critical ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | These limitations underscore the urgent need for a unified framework that balances geometric precision, memory efficiency, and seamless scalability. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | While 3D Gaussian Splatting (3DGS) enables high-quality, real-time rendering for bounded scenes, its extension to large-scale urban environments gives rise to critical ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / 3.1 PRELIMINARIES - extractive body cue:** First, when obtaining the global coarse 3DGS model, we first eliminate redundant Gaussians through SAGP pruning to prevent these redundant Gaussians from attracting non-contributing views ...
- **p. 4 / 3.1 PRELIMINARIES - extractive body cue:** To reconstruct scene surfaces, we enforce normal priors N predicted by a pretrained monocular deep neural network (Bae & Davison, 2024) to supervise the rendered ...
- **p. 5 / 3.1 PRELIMINARIES - extractive body cue:** (b) Depth-Consistent D-Normal Regularization: 3D Gaussians are rendered to depth and normal maps, depth is converted to D-normals and jointly supervised with pseudo-depth and pseudonormal ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** We compare the training time of our method with that of existing methods.
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** The results demonstrate that our SAGP is more effective at preserving the original geometric quality (higher F1 score) while significantly reducing the number of Gaussians, ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** First, when, obtaining, global, coarse, DGS, model, eliminate, redundant, Gaussians, through, SAGP, pruning, prevent, attracting, non-contributing, views, amplifying, computational, load.
- **Relevant PDF headings:** 3 METHODOLOGY (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We compare our method with existing surface reconstruction approaches on the GauU-Scene datasets (Xiong et al., 2024). | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Semantic / temporal fusion | Figure 4: Qualitative mesh and texture comparison between SOTA and our method on GauU-Scene dataset (Xiong et al., 2024). 4.2 MAIN RESULTS ... | p. 8 (Figure/Table caption), p. 10 (4 EXPERIMENTS) |
| Robot query / planning handoff | Quantitative results reveal consistent improvements across all evaluation metrics, with notable gains in F1-score (from 0.453 to 0.503) and PSNR (from 24.59 ... | p. 10 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Method PSNR↑ SSIM↑ LPIPS↓ F1↑ w/o D-Normal 25.02 0.743 0.215 0.463 w/o Depth Consistency 24.59 0.792 0.201 0.453 w/o Geometry-Aware Confidence 26.02 0.795 0.163 0.493 ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Method Rendering Quality Geometric Quality Training Statistics PSNR↑ SSIM↑ LPIPS↓ P↑ R↑ F1↑ GS (M)↓ Time↓ Size↓ Mem↓ Baseline 22.54 0.778 0.231 0.532 0.501 0.516 ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** The top three results are highlighted with red, orange, and yellow backgrounds, respectively. † denotes results obtained without the decoupled appearance encoding.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** 3, we present quantitative and qualitative evaluations of large-scale scene reconstruction methods with and without geometric optimization.
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** The surface is then extracted using the Marching Cubes algorithm at the zero-level isosurface, enabling direct reconstruction of 3D geometry without relying on intermediate point ...
- **p. 15 / A IMPLEMENTATION DETAILS - extractive body cue:** When constructing the coarse global Gaussian model, we apply an initial, simple pruning rule to remove obviously redundant Gaussians, reduce memory, and obtain a compact ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: UrbanGS training pipeline and core components. (a) Training Pipeline: Starting from coarse global Gaussians, we apply spatially adaptive Gaussian pruning to obtain compact ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 7 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 15 (A IMPLEMENTATION DETAILS), p. 5 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), objective p. 6 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), temporal p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 5 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
