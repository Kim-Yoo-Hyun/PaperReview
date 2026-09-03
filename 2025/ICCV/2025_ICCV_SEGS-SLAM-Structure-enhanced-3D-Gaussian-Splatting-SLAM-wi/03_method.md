# Method - SEGS-SLAM: Structure-enhanced 3D Gaussian Splatting SLAM with Appearance Embedding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wen_SEGS-SLAM_Structure-enhanced_3D_Gaussian_Splatting_SLAM_with_Appearance_Embedding_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wen_SEGS-SLAM_Structure-enhanced_3D_Gaussian_Splatting_SLAM_with_Appearance_Embedding_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 2 (1. Introduction), p. 4 (4.2. Appearance-from-Motion Embedding), p. 4 (4.1. Structure-Enhanced Photorealistic Mapping), p. 1 (1. Introduction), p. 2 (2. We)): Second, we propose Appearance-from-Motion embedding (AfME), enabling 3D Gaussians to better model image appearance variations across different camera poses.

## Method Body Digest

- **p. 1 / Abstract - extractive body cue:** Second, we propose Appearance-from-Motion embedding (AfME), enabling 3D Gaussians to better model image appearance variations across different camera poses.
- **p. 2 / 1. Introduction - extractive body cue:** Second, we propose Appearancefrom-Motion embedding (AfME), which takes poses as input and eliminates the need for training on the left half of each ground-truth image ...
- **p. 4 / 4.2. Appearance-from-Motion Embedding - extractive body cue:** To address this issue, we propose Appearance-from-Motion embedding (AfME), which employs a lightweight Multilayer Perceptron (MLP) Mθa to learn a shared appearance representation.
- **p. 4 / 4.1. Structure-Enhanced Photorealistic Mapping - extractive body cue:** Based on this observation, we propose incrementally voxelizing the point cloud Pk of each keyframe to construct anchor points, as follows: Vk = {⌊Pk ϵ ...
- **p. 1 / 1. Introduction - extractive body cue:** However, most SLAM algorithms based on 3D-GS have neglected the latent structure in the scene, which constrains their rendering quality.
- **p. 2 / 2. We - extractive body cue:** propose Appearance-from-Motion embedding (AfME), which models per-image appearance variations into a latent space extracted from camera pose.
- **p. 5 / 4.4. Losses Design - extractive body cue:** The optimization of the learnable parameters, the MLP Mα, Mc, Mq, Ms, and Mθa, are achieved by minimizing the L1 loss L1, SSIM term [40] ...
- **p. 3 / 3.2. Localization and Geometry Mapping - extractive body cue:** The camera poses (R, t) and the point cloud {P0, . . . , Pη} ∈Rη×3 of the scene can be solved through local or ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Second, we propose Appearancefrom-Motion embedding (AfME), which takes poses as input and eliminates the need for training on the left half of each ground-truth image ...
- **p. 2 / 1. Introduction - extractive body cue:** Motivated by this, we propose a structure-enhanced photorealistic mapping (SEPM) framework, which initializes anchor points using ORB-SLAM3 [3] point cloud, significantly enhancing the utilization of ...
- **p. 1 / Abstract - extractive body cue:** To address these problems, we propose SEGS-SLAM, a structure-enhanced 3D Gaussian Splatting SLAM, which achieves high-quality photorealistic mapping.

## Source Evidence Cues

- **p. 1 / Abstract - extractive body cue:** Second, we propose Appearance-from-Motion embedding (AfME), enabling 3D Gaussians to better model image appearance variations across different camera poses.
- **p. 2 / 1. Introduction - extractive body cue:** Second, we propose Appearancefrom-Motion embedding (AfME), which takes poses as input and eliminates the need for training on the left half of each ground-truth image ...
- **p. 4 / 4.2. Appearance-from-Motion Embedding - extractive body cue:** To address this issue, we propose Appearance-from-Motion embedding (AfME), which employs a lightweight Multilayer Perceptron (MLP) Mθa to learn a shared appearance representation.
- **p. 4 / 4.1. Structure-Enhanced Photorealistic Mapping - extractive body cue:** Based on this observation, we propose incrementally voxelizing the point cloud Pk of each keyframe to construct anchor points, as follows: Vk = {⌊Pk ϵ ...
- **p. 1 / 1. Introduction - extractive body cue:** However, most SLAM algorithms based on 3D-GS have neglected the latent structure in the scene, which constrains their rendering quality.
- **p. 2 / 2. We - extractive body cue:** propose Appearance-from-Motion embedding (AfME), which models per-image appearance variations into a latent space extracted from camera pose.
- **p. 5 / 4.4. Losses Design - extractive body cue:** The optimization of the learnable parameters, the MLP Mα, Mc, Mq, Ms, and Mθa, are achieved by minimizing the L1 loss L1, SSIM term [40] ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Second, we propose Appearance-from-Motion embedding (AfME), enabling 3D Gaussians to better model image appearance variations across different camera poses. | p. 1 (Abstract), p. 2 (1. Introduction) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Second, we propose Appearancefrom-Motion embedding (AfME), which takes poses as input and eliminates the need for training on the left half of ... | p. 2 (1. Introduction), p. 4 (4.2. Appearance-from-Motion Embedding) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | To address this issue, we propose Appearance-from-Motion embedding (AfME), which employs a lightweight Multilayer Perceptron (MLP) Mθa to learn a shared appearance ... | p. 4 (4.2. Appearance-from-Motion Embedding), p. 4 (4.1. Structure-Enhanced Photorealistic Mapping) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.4. Losses Design - extractive body cue:** The optimization of the learnable parameters, the MLP Mα, Mc, Mq, Ms, and Mθa, are achieved by minimizing the L1 loss L1, SSIM term [40] ...
- **p. 3 / 3.2. Localization and Geometry Mapping - extractive body cue:** The camera poses (R, t) and the point cloud {P0, . . . , Pη} ∈Rη×3 of the scene can be solved through local or ...
- **p. 4 / 4. SEGS-SLAM - extractive body cue:** SEPM enhances the underlying structure of the 3D representation. loss and FPR.
- **p. 5 / 4.3. Frequency Pyramid Regularization - extractive body cue:** The loss Lhf is computed as Lhf =  s∈S 1 N λs  u,v F s hf,r(u, v) -F s hf,g(u, v)  , ...
- **p. 2 / 1. Introduction - extractive body cue:** We further introduce a frequency pyramid regularization (FPR) technique to better capture high-frequency details in the scene.
- **p. 2 / 1. Introduction - extractive body cue:** FreGS [47] combines frequency regularization to model the local details, but its effectiveness is constrained by the use of a single-scale frequency spectrum.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (3.2. Localization and Geometry Mapping), p. 4 (4. SEGS-SLAM), p. 5 (4.4. Losses Design), p. 5 (4.3. Frequency Pyramid Regularization).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | observation, incrementally, voxelizing, point, cloud, keyframe, construct, anchor, points, follows, where, denotes, voxel, centers | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | observation, incrementally, voxelizing, point, cloud, keyframe, construct, anchor, points, follows | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | Second, Appearancefrom-Motion, embedding, AfME, takes, poses, input, eliminates, need, training | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | optimization, learnable, parameters, MLP, achieved, minimizing, loss, SSIM, term, LSSIM | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4.1. Structure-Enhanced Photorealistic Mapping - extractive body cue:** Based on this observation, we propose incrementally voxelizing the point cloud Pk of each keyframe to construct anchor points, as follows: Vk = {⌊Pk ϵ ...
- **p. 2 / 1. Introduction - extractive body cue:** Second, we propose Appearancefrom-Motion embedding (AfME), which takes poses as input and eliminates the need for training on the left half of each ground-truth image ...
- **p. 4 / 2.1 Test on the right half of each - extractive body cue:** The differences between them are: (1) AE uses image indexes as input, whereas AfME leverages camera poses.
- **p. 5 / 4.2. Appearance-from-Motion Embedding - extractive body cue:** The input poses of the AfME in the top-row images correspond to those in the bottomrow images.
- **p. 5 / 4.2. Appearance-from-Motion Embedding - extractive body cue:** We choose camera poses as inputs for several reasons: 1) Similar to image indices, camera poses are unique for each view.
- **p. 3 / 3.2. Localization and Geometry Mapping - extractive body cue:** ORB-SLAM3 [3] can track camera poses and generate point cloud accurately.
- **p. 3 / 3.2. Localization and Geometry Mapping - extractive body cue:** The camera poses (R, t) and the point cloud {P0, . . . , Pη} ∈Rη×3 of the scene can be solved through local or ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Additionally, while our method achieves real-time tracking and rendering at 17 and 400 FPS, respectively, it exhibits reduced rendering speed due to ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Our SEGS-SLAM is fully implemented using the LibTorch framework with C++ and CUDA. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Additionally, while our method achieves real-time tracking and rendering at 17 and 400 FPS, respectively, it exhibits reduced rendering speed due to ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1. Introduction - extractive body cue:** Second, we propose Appearancefrom-Motion embedding (AfME), which takes poses as input and eliminates the need for training on the left half of each ground-truth image ...
- **p. 1 / 1. Introduction - extractive body cue:** However, most SLAM algorithms based on 3D-GS have neglected the latent structure in the scene, which constrains their rendering quality.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Second, Appearance-from-Motion, embedding, AfME, enabling, Gaussians, better, model, image, appearance, variations, across, different, camera, poses, Appearancefrom-Motion, takes, input, eliminates, need.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | The top scene is office2 from the Replica datasets, and the bottom is fr3/office from TUM RGB-D datasets. | p. 6 (5.1. Experiment Setup), p. 6 (5.2. Results Analysis) |
| Global / local decision | Quantitative evaluation of our method compared to SOTA methods for RGB-D camera on Replica and TUM RGB-D datasets. | p. 6 (5.1. Experiment Setup), p. 6 (5.2. Results Analysis) |
| Motion execution / recovery | The best results are marked as best score , second best score and third best score . '-' denotes that the system ... | p. 7 (5.2. Results Analysis), p. 6 (5.2. Results Analysis) |

## Failure and Ablation Link

- **p. 8 / 5.3. Ablation Studies - extractive body cue:** To evaluate the effect of the proposed FPR on photorealistic mapping metrics, we train an additional model for our method without FPR.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 9. Ablation of AfME (Top) and FPR (Bottom). It is evident that with the introduction of AfME, the lighting conditions at novel views are ...
- **p. 7 / 5.3. Ablation Studies - extractive body cue:** The variant without SEPM, AfME, and FPR directly uses the original 3D-GS [17].
- **p. 7 / 5.3. Ablation Studies - extractive body cue:** To evaluate the impact of SEPM on photorealistic mapping metrics, we additionally train two variants of our method: one without SEPM, AfME, and FPR, and ...
- **p. 8 / 5.4. Limitations - extractive body cue:** One limitation of our method is that a poorly structured point cloud leads to a decline in photorealistic mapping quality.
- **p. 6 / 5.1. Experiment Setup - extractive body cue:** GS-SLAM∗denotes the result of GS-SLAM is taken from [42], all others are obtained in our experiments. '-' denotes the system does not provide valid results.
- **p. 7 / 5.2. Results Analysis - extractive body cue:** The best results are marked as best score , second best score and third best score . '-' denotes that the system does not provide ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Abstract), p. 2 (1. Introduction), p. 4 (4.2. Appearance-from-Motion Embedding), p. 4 (4.1. Structure-Enhanced Photorealistic Mapping), p. 1 (1. Introduction), p. 2 (2. We), objective p. 5 (4.4. Losses Design), p. 3 (3.2. Localization and Geometry Mapping), p. 4 (4. SEGS-SLAM), p. 5 (4.3. Frequency Pyramid Regularization), p. 2 (1. Introduction), p. 2 (1. Introduction), temporal p. 8 (5.4. Limitations), p. 5 (5.1. Experiment Setup), p. 5 (5.1. Experiment Setup), p. 6 (5.1. Experiment Setup), p. 6 (5.1. Experiment Setup), p. 7 (5.2. Results Analysis).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
