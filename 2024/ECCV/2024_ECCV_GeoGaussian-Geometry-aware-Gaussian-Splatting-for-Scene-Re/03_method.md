# Method - GeoGaussian: Geometry-aware Gaussian Splatting for Scene Rendering

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5218_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05218.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (1 Introduction), p. 7 (2) Splitting), p. 2 (1 Introduction), p. 7 (2) Splitting), p. 2 (1 Introduction), p. 1 (1 Introduction)): In the optimization module, we propose a new geometrically consistent constraint for thin ellipsoids lying on the smooth areas by encouraging the nearest neighbors to be co-planar, which are jointly ...

## Method Body Digest

- **p. 3 / 1 Introduction - extractive PDF cue:** In the optimization module, we propose a new geometrically consistent constraint for thin ellipsoids lying on the smooth areas by encouraging the nearest neighbors to ...
- **p. 7 / 2) Splitting - extractive PDF cue:** After selecting view-dependent thin Gaussians G which are encouraged to preserve smooth connections with their nearest neighbors, we propose a smoothness loss function to further ...
- **p. 2 / 1 Introduction - extractive PDF cue:** However, in the Gaussian Splatting optimization process, the geometry of 3D Gaussian models lacks sufficient constraints especially in low-textured regions, leading to significant degradation in ...
- **p. 7 / 2) Splitting - extractive PDF cue:** We then utilize the K-NN algorithm to detect the eight nearest neighbors around G , which are passed through a lter to remove outliers that ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Since the impressive achievements of convolutional neural networks are made on many tasks, such as point detection [6] and scene completion [40], deep learningbased mesh ...
- **p. 1 / 1 Introduction - extractive PDF cue:** An additional rasterization step re-projects these 3D Gaussians back to training images to capture ⋆Equal senior author
- **p. 1 / 1 Introduction - extractive PDF cue:** While NeRFs offer high-quality rendering, 3D Gaussian Splatting ( [8,18]) shows better performance in terms of training speed and rendering quality.
- **p. 3 / 1 Introduction - extractive PDF cue:** The step is supported by accumulating the gradient descent direction of the origin's position , and then the component of the direction that is perpendicular ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** The contributions of the paper are summarized as: - A parameterization with explicit geometry meaning for thin 3D Gaussians is employed in our carefully designed ...
- **p. 3 / 1 Introduction - extractive PDF cue:** In this paper, we propose a geometry-aware Gaussian Splatting method emphasizing rendering fidelity and geometry structure simultaneously.
- **p. 7 / 2) Splitting - extractive PDF cue:** After selecting view-dependent thin Gaussians G which are encouraged to preserve smooth connections with their nearest neighbors, we propose a smoothness loss function to further ...

## Source Evidence Cues

- **p. 3 / 1 Introduction - extractive PDF cue:** In the optimization module, we propose a new geometrically consistent constraint for thin ellipsoids lying on the smooth areas by encouraging the nearest neighbors to ...
- **p. 7 / 2) Splitting - extractive PDF cue:** After selecting view-dependent thin Gaussians G which are encouraged to preserve smooth connections with their nearest neighbors, we propose a smoothness loss function to further ...
- **p. 2 / 1 Introduction - extractive PDF cue:** However, in the Gaussian Splatting optimization process, the geometry of 3D Gaussian models lacks sufficient constraints especially in low-textured regions, leading to significant degradation in ...
- **p. 7 / 2) Splitting - extractive PDF cue:** We then utilize the K-NN algorithm to detect the eight nearest neighbors around G , which are passed through a lter to remove outliers that ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Since the impressive achievements of convolutional neural networks are made on many tasks, such as point detection [6] and scene completion [40], deep learningbased mesh ...
- **p. 1 / 1 Introduction - extractive PDF cue:** An additional rasterization step re-projects these 3D Gaussians back to training images to capture ⋆Equal senior author
- **p. 1 / 1 Introduction - extractive PDF cue:** While NeRFs offer high-quality rendering, 3D Gaussian Splatting ( [8,18]) shows better performance in terms of training speed and rendering quality.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | In the optimization module, we propose a new geometrically consistent constraint for thin ellipsoids lying on the smooth areas by encouraging the ... | p. 3 (1 Introduction), p. 7 (2) Splitting) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | After selecting view-dependent thin Gaussians G which are encouraged to preserve smooth connections with their nearest neighbors, we propose a smoothness loss ... | p. 7 (2) Splitting), p. 2 (1 Introduction) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | However, in the Gaussian Splatting optimization process, the geometry of 3D Gaussian models lacks sufficient constraints especially in low-textured regions, leading to ... | p. 2 (1 Introduction), p. 7 (2) Splitting) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive PDF cue:** However, in the Gaussian Splatting optimization process, the geometry of 3D Gaussian models lacks sufficient constraints especially in low-textured regions, leading to significant degradation in ...
- **p. 3 / 1 Introduction - extractive PDF cue:** In the optimization module, we propose a new geometrically consistent constraint for thin ellipsoids lying on the smooth areas by encouraging the nearest neighbors to ...
- **p. 3 / 1 Introduction - extractive PDF cue:** The step is supported by accumulating the gradient descent direction of the origin's position , and then the component of the direction that is perpendicular ...
- **p. 7 / 2) Splitting - extractive PDF cue:** Following the strategy of 3DGS [18], the goal of our designed loss functions is to create correct geometry and adjust incorrectly positioned Gaussians.
- **p. 7 / 2) Splitting - extractive PDF cue:** After selecting view-dependent thin Gaussians G which are encouraged to preserve smooth connections with their nearest neighbors, we propose a smoothness loss function to further ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 7 (2) Splitting), p. 7 (2) Splitting).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Initially, normal, vectors, extracted, input, point, clouds, then, smoothly, connected, areas, detected, normals, Evaluations | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Initially, normal, vectors, extracted, input, point, clouds, then, smoothly, connected | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, parameterization, explicit, geometry, meaning, thin, Gaussians, employed, carefully | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | However, Gaussian, Splatting, optimization, process, geometry, models, lacks, sufficient, constraints | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1 Introduction - extractive PDF cue:** Initially, normal vectors are extracted from input point clouds, and then smoothly connected areas are detected based on normals.
- **p. 4 / 1 Introduction - extractive PDF cue:** Li et al. - Evaluations on the public datasets demonstrate that the proposed method improves rendering quality compared to state-of-the-art Gaussian Splatting methods.
- **p. 1 / 1 Introduction - extractive PDF cue:** An additional rasterization step re-projects these 3D Gaussians back to training images to capture ⋆Equal senior author
- **p. 2 / 1 Introduction - extractive PDF cue:** NVS methods typically represent 3D scenes implicitly [28, 42] or explicitly [4, 16] based on multiple 2D views and corresponding camera poses.
- **p. 2 / 1 Introduction - extractive PDF cue:** While these methods enable the rendering of new views in texture and depth based on 3D surface models, achieving photo-realistic rendering quality remains challenging.
- **p. 3 / 1 Introduction - extractive PDF cue:** Through the learning rate and direction, the Gaussian map undergoes densification for continuous training.
- **p. 7 / 2) Splitting - extractive PDF cue:** Following the strategy of 3DGS [18], the goal of our designed loss functions is to create correct geometry and adjust incorrectly positioned Gaussians.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | An additional rasterization step re-projects these 3D Gaussians back to training images to capture ⋆Equal senior author | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | To address the heavy computational burden and intensive memory consumption, recent improvements have been made using sparse volumes [21], hash tables [27], ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | To address the heavy computational burden and intensive memory consumption, recent improvements have been made using sparse volumes [21], hash tables [27], ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Recently, 3D Gaussian Splatting (3DGS) [18] has gained significant attention in the community, which shows that the rendering speed in high-quality NVS ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 1 Introduction - extractive PDF cue:** In the optimization module, we propose a new geometrically consistent constraint for thin ellipsoids lying on the smooth areas by encouraging the nearest neighbors to ...
- **p. 2 / 1 Introduction - extractive PDF cue:** However, in the Gaussian Splatting optimization process, the geometry of 3D Gaussian models lacks sufficient constraints especially in low-textured regions, leading to significant degradation in ...
- **p. 1 / 1 Introduction - extractive PDF cue:** An additional rasterization step re-projects these 3D Gaussians back to training images to capture ⋆Equal senior author
- **p. 1 / 1 Introduction - extractive PDF cue:** While NeRFs offer high-quality rendering, 3D Gaussian Splatting ( [8,18]) shows better performance in terms of training speed and rendering quality.
- **p. 3 / 1 Introduction - extractive PDF cue:** Through the learning rate and direction, the Gaussian map undergoes densification for continuous training.
- **p. 3 / 1 Introduction - extractive PDF cue:** GeoGaussian 3 spite a significant reduction in training time with these methods, improving rendering efficiency is still a pressing requirement for applications such as SLAM.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** optimization, module, geometrically, consistent, constraint, thin, ellipsoids, lying, smooth, areas, encouraging, nearest, neighbors, co-planar, jointly, optimized, widely, photometric, residuals, iterative.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | By jointly optimizing the normal alignment and depth consistency of the Gaussian point tangent space in the neighborhood, we can obtain Gaussian ... | p. 7 (2) Splitting), p. 2 (Figure/Table caption) |
| Semantic / temporal fusion | Fig. 1: Comparisons of novel view rendering and 3D Gaussian model on the Replica Datasets. As highlighted in the second row, the ... | p. 2 (Figure/Table caption), p. 7 (2) Splitting) |
| Robot query / planning handoff | After selecting view-dependent thin Gaussians G which are encouraged to preserve smooth connections with their nearest neighbors, we propose a smoothness loss ... | p. 7 (2) Splitting), p. 2 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / 2) Splitting - extractive PDF cue:** We then utilize the K-NN algorithm to detect the eight nearest neighbors around G , which are passed through a lter to remove outliers that ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: Comparisons of novel view rendering and 3D Gaussian model on the Replica Datasets. As highlighted in the second row, the proposed method shows ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (1 Introduction), p. 7 (2) Splitting), p. 2 (1 Introduction), p. 7 (2) Splitting), p. 2 (1 Introduction), p. 1 (1 Introduction), objective p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 7 (2) Splitting), p. 7 (2) Splitting), temporal p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (2 Related Work), p. 4 (2 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
