# Method - SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.3. Lidar rendering), p. 3 (3.2. Camera rendering), p. 3 (3.1. Scene representation), p. 4 (3.3. Lidar rendering), p. 4 (3.2. Camera rendering), p. 5 (3.4. Optimization and implementation)): While we use the expected range for training, the median range is used during inference as it, in contrast to the expected range, does not yield depths between Gaussians.

## Method Body Digest

- **p. 5 / 3.3. Lidar rendering - extractive PDF cue:** While we use the expected range for training, the median range is used during inference as it, in contrast to the expected range, does not ...
- **p. 3 / 3.2. Camera rendering - extractive PDF cue:** While we retain 3DGS's high-level steps-projection and view frustum culling, tile-assignment, depth sorting, and tilebased rasterization-we introduce key adaptations to better model the unique characteristics ...
- **p. 3 / 3.1. Scene representation - extractive PDF cue:** Last, our representation contains a learnable embedding per sensor to model their specific appearance characteristics.
- **p. 4 / 3.3. Lidar rendering - extractive PDF cue:** However, we note that modeling other types of lidars, such as solid-state lidars [21], can be easily 11985
- **p. 4 / 3.2. Camera rendering - extractive PDF cue:** View-dependent effects are modeled using a small CNN; given the feature map F ∈RH×W ×Df , the corresponding ray directions d ∈RH×W ×3, and a ...
- **p. 5 / 3.4. Optimization and implementation - extractive PDF cue:** All model components are optimized jointly using the loss { eq:l o ss _ fn} \mat h cal {L} = \l a mbda _r\m athcal ...
- **p. 2 / 3. Method - extractive PDF cue:** Our aim is to learn a scene representation from collected vehicle logs that enables rendering of realistic camera and lidar 11983
- **p. 5 / 3.4. Optimization and implementation - extractive PDF cue:** LBCE is a binary cross-entropy loss on the predicted ray drop probability, where ground-truth is generated in the same way as for NeuRAD.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** To summarize, our contributions are as follows: • We propose the first method for efficient lidar rendering using 3D Gaussians, introducing custom CUDA-accelerated algorithms for ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To overcome these challenges, we introduce SplatAD, a novel view synthesis method that unifies camera and lidar rendering and is designed for real-time rendering of ...
- **p. 3 / 3. Method - extractive PDF cue:** Our method projects 3D Gaussians with associated feature vectors onto the corresponding sensor modalities (camera and lidar) and employs sensor-specific tiling to match their distinct ...

## Source Evidence Cues

- **p. 5 / 3.3. Lidar rendering - extractive PDF cue:** While we use the expected range for training, the median range is used during inference as it, in contrast to the expected range, does not ...
- **p. 3 / 3.2. Camera rendering - extractive PDF cue:** While we retain 3DGS's high-level steps-projection and view frustum culling, tile-assignment, depth sorting, and tilebased rasterization-we introduce key adaptations to better model the unique characteristics ...
- **p. 3 / 3.1. Scene representation - extractive PDF cue:** Last, our representation contains a learnable embedding per sensor to model their specific appearance characteristics.
- **p. 4 / 3.3. Lidar rendering - extractive PDF cue:** However, we note that modeling other types of lidars, such as solid-state lidars [21], can be easily 11985
- **p. 4 / 3.2. Camera rendering - extractive PDF cue:** View-dependent effects are modeled using a small CNN; given the feature map F ∈RH×W ×Df , the corresponding ray directions d ∈RH×W ×3, and a ...
- **p. 5 / 3.4. Optimization and implementation - extractive PDF cue:** All model components are optimized jointly using the loss { eq:l o ss _ fn} \mat h cal {L} = \l a mbda _r\m athcal ...
- **p. 2 / 3. Method - extractive PDF cue:** Our aim is to learn a scene representation from collected vehicle logs that enables rendering of realistic camera and lidar 11983
- **Detected method headings:** 3. Method (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | While we use the expected range for training, the median range is used during inference as it, in contrast to the expected ... | p. 5 (3.3. Lidar rendering), p. 3 (3.2. Camera rendering) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | While we retain 3DGS's high-level steps-projection and view frustum culling, tile-assignment, depth sorting, and tilebased rasterization-we introduce key adaptations to better model ... | p. 3 (3.2. Camera rendering), p. 3 (3.1. Scene representation) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Last, our representation contains a learnable embedding per sensor to model their specific appearance characteristics. | p. 3 (3.1. Scene representation), p. 4 (3.3. Lidar rendering) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.4. Optimization and implementation - extractive PDF cue:** LBCE is a binary cross-entropy loss on the predicted ray drop probability, where ground-truth is generated in the same way as for NeuRAD.
- **p. 5 / 3.4. Optimization and implementation - extractive PDF cue:** All model components are optimized jointly using the loss { eq:l o ss _ fn} \mat h cal {L} = \l a mbda _r\m athcal ...
- **p. 3 / 3. Method - extractive PDF cue:** 3.2 and 3.3), and implementation and optimization strategy (Sec.
- **p. 4 / 3.3. Lidar rendering - extractive PDF cue:** They do so by emitting laser beam pulses and measuring the time of flight to determine distance and returning power for reflectivity.
- **p. 6 / 3.4. Optimization and implementation - extractive PDF cue:** We train SplatAD for 30,000 iterations using the Adam optimizer, which takes an hour on a single NVIDIA A100.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.4. Optimization and implementation), p. 5 (3.4. Optimization and implementation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | summarize, contributions, follows, first, efficient, lidar, rendering, Gaussians, introducing, custom, CUDA-accelerated, algorithms, rasterizing, sparse | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | summarize, contributions, follows, first, efficient, lidar, rendering, Gaussians, introducing, custom | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summarize, contributions, follows, first, efficient, lidar, rendering, Gaussians, introducing, custom | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | LBCE, binary, cross-entropy, loss, predicted, drop, probability, where, ground-truth, generated | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** To summarize, our contributions are as follows: • We propose the first method for efficient lidar rendering using 3D Gaussians, introducing custom CUDA-accelerated algorithms for ...
- **p. 3 / 3. Method - extractive PDF cue:** Our proposed lidar rendering matches the image rendering on a high level, but modifies each component to accurately model sensor characteristics.
- **p. 6 / 3.4. Optimization and implementation - extractive PDF cue:** Projecting lidar points into images for depth supervision, as used by previous 3DGS methods, causes line-of-sight errors and incorrect volume carving due to the pose ...
- **p. 4 / 3.3. Lidar rendering - extractive PDF cue:** However, we note that modeling other types of lidars, such as solid-state lidars [21], can be easily 11985
- **p. 3 / 3. Method - extractive PDF cue:** Finally, the rasterized features are decoded into the respective image and lidar point cloud representations. data, with the ability to alter the locations of both ...
- **p. 4 / 3.2. Camera rendering - extractive PDF cue:** Specifically, each Gaussian's velocity relative to the camera is projected to image space, and their pixel mean µI is adjusted during rasterization based on the ...
- **p. 5 / 3.3. Lidar rendering - extractive PDF cue:** Comparing our strategy to using tiles of equal size, similar to the depth image-based rendering in [7], we avoid many unnecessary computations.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We use the models trained on every other frame and follow the three settings in [35]: shift the ego-vehicle horizontally, shift the ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Each dynamic actor is described by a 3D bounding box and a sequence of SE(3) poses, obtained either from an off-the-shelf object ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. Lidar rendering - extractive PDF cue:** While we use the expected range for training, the median range is used during inference as it, in contrast to the expected range, does not ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** While, expected, range, training, median, during, inference, contrast, does, yield, depths, between, Gaussians, retain, DGS, high-level, steps-projection, view, frustum, culling.
- **Relevant PDF headings:** 3. Method (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Datasets: We perform experiments on PandaSet [41], Argoverse2 [38] and nuScenes [5]. | p. 6 (4. Experiments), p. 7 (4. Experiments) |
| Semantic / temporal fusion | Compared to the baselines, SplatAD produces sharp images with a high level of detail. | p. 6 (3.4. Optimization and implementation), p. 7 (4. Experiments) |
| Robot query / planning handoff | Figure 4. Removing our rolling shutter modeling compensation leads to inaccurate geometries and inconsistencies in the learning. We measure speed using resolution-agnostic ... | p. 7 (Figure/Table caption), p. 7 (4.1. Image rendering) |

## Failure and Ablation Link

- **p. 6 / 4. Experiments - extractive PDF cue:** Further, some cameras are cropped slightly to remove views of the ego-vehicle, such as the hood and the trunk.
- **p. 7 / 4. Experiments - extractive PDF cue:** NVS results for lidar, over three datasets. §without missing points.
- **p. 8 / 4.2. Lidar rendering - extractive PDF cue:** Reconstruction results for image and lidar point clouds on PandaSet. §without missing points.
- **p. 8 / 4.3. Ablations - extractive PDF cue:** We validate the effectiveness of key components of our method by measuring their impact on NVS metrics in Tab.
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of our proposed method. Given the composition of static and dynamic 3D Gaussians, SplatAD is capable of differentiable rendering of both lidar ...
- **p. 6 / 3.4. Optimization and implementation - extractive PDF cue:** We use [16] as is, without any special treatment of Gaussians assigned to dynamic actors.
- **p. 7 / 4.1. Image rendering - extractive PDF cue:** Removing our rolling shutter modeling compensation leads to inaccurate geometries and inconsistencies in the learning.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.3. Lidar rendering), p. 3 (3.2. Camera rendering), p. 3 (3.1. Scene representation), p. 4 (3.3. Lidar rendering), p. 4 (3.2. Camera rendering), p. 5 (3.4. Optimization and implementation), objective p. 5 (3.4. Optimization and implementation), p. 5 (3.4. Optimization and implementation), p. 3 (3. Method), p. 4 (3.3. Lidar rendering), p. 6 (3.4. Optimization and implementation), temporal p. 7 (4.1. Image rendering), p. 3 (3.1. Scene representation), p. 3 (3.2. Camera rendering), p. 4 (3.2. Camera rendering), p. 5 (3.3. Lidar rendering), p. 5 (3.3. Lidar rendering).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
