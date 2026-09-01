# Method - LiV-GS: LiDAR-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2411.12185; PDF retrieval source: https://arxiv.org/pdf/2411.12185. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 2 (III. METHODOLOGY)): Since the length of the Gaussian normal is difficult to restrict during the optimization, we introduced the normal length normalization for both point clouds and Gaussians, so that the robustness ...

## Method Body Digest

- **p. 4 / III. METHODOLOGY - extractive PDF cue:** Since the length of the Gaussian normal is difficult to restrict during the optimization, we introduced the normal length normalization for both point clouds and ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** We introduce a Conditional Gaussian Constraint (CGC) to adjust the positions of color-supervised Gaussians through the loss function (10).
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** The Gaussian map incorporating keyframe parameters is then processed in the back-end for pose optimization and map updates.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** The multi-modal measurements from LiDAR and visual sensors are integrated in Data Preporessing and then fed into the front-end Tracking module.
- **p. 2 / III. METHODOLOGY - extractive PDF cue:** Our LiV-GS is an outdoor visual-LiDAR SLAM system that employs 3D gaussian for environmental representation.
- **p. 2 / III. METHODOLOGY - extractive PDF cue:** In our model, each Gaussian is defined by gi = {α, c, µ, Σ}, where α signifies opacity, and c the color, directly derived from ...
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** 4, the newly-split points will strictly adhere to the distribution patterns of existing reliable points, especially in areas with complex shapes or distinctive surface features.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** By minimizing the loss function, the Gaussian map updates the parameters of Gaussians continuously together with splitting and pruning operations of Gaussians.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** To the end, we introduce LiV-GS, a SLAM framework that uses 3D Gaussian spatial representations to seamlessly integrate LiDAR and camera images.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Our method estimates robot pose by aligning Gaussian covariance from rendering with the current observations, with the back-end correcting drift and updating the Gaussian map.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Our method effectively prevents these issues. by LiDAR depth in the error calculation of point clouds and Gaussian match.

## Source Evidence Cues

- **p. 4 / III. METHODOLOGY - extractive PDF cue:** Since the length of the Gaussian normal is difficult to restrict during the optimization, we introduced the normal length normalization for both point clouds and ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** We introduce a Conditional Gaussian Constraint (CGC) to adjust the positions of color-supervised Gaussians through the loss function (10).
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** The Gaussian map incorporating keyframe parameters is then processed in the back-end for pose optimization and map updates.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** The multi-modal measurements from LiDAR and visual sensors are integrated in Data Preporessing and then fed into the front-end Tracking module.
- **p. 2 / III. METHODOLOGY - extractive PDF cue:** Our LiV-GS is an outdoor visual-LiDAR SLAM system that employs 3D gaussian for environmental representation.
- **p. 2 / III. METHODOLOGY - extractive PDF cue:** In our model, each Gaussian is defined by gi = {α, c, µ, Σ}, where α signifies opacity, and c the color, directly derived from ...
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** 4, the newly-split points will strictly adhere to the distribution patterns of existing reliable points, especially in areas with complex shapes or distinctive surface features.
- **Detected method headings:** III. METHODOLOGY (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Since the length of the Gaussian normal is difficult to restrict during the optimization, we introduced the normal length normalization for both ... | p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | We introduce a Conditional Gaussian Constraint (CGC) to adjust the positions of color-supervised Gaussians through the loss function (10). | p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | The Gaussian map incorporating keyframe parameters is then processed in the back-end for pose optimization and map updates. | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHODOLOGY - extractive PDF cue:** By minimizing the loss function, the Gaussian map updates the parameters of Gaussians continuously together with splitting and pruning operations of Gaussians.
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** We introduce a Conditional Gaussian Constraint (CGC) to adjust the positions of color-supervised Gaussians through the loss function (10).
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** To align Gaussians with object surfaces closely, we introduce the normal loss Enormal which is optimized for shorter and more stable normals.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** These Gaussian centers are determined by minimizing the distance from point x to each Gaussian center µgi.
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** The conditional Gaussian equation (11) adjusts the mean µx and covariance Σx of x, aligning them more closely with the nearest reliable Gaussian y.
- **p. 5 / III. METHODOLOGY - extractive PDF cue:** The new Gaussian split from the reliable Gaussian is regarded as reliable Gaussian after undergoing a round of back-end optimization, the process of which continue ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | system, data, inputs, consist, imagery, camera, point, clouds, LiDAR, sensor, integrated, calibrated, extrinsic, transform | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | system, data, inputs, consist, imagery, camera, point, clouds, LiDAR, sensor | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | introduce, LiV-GS, SLAM, framework, uses, Gaussian, spatial, representations, seamlessly, integrate | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | minimizing, loss, function, Gaussian, updates, parameters, Gaussians, continuously, together, splitting | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHODOLOGY - extractive PDF cue:** In the proposed system, data inputs consist of imagery from a camera and point clouds from a LiDAR sensor.
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** These inputs are integrated using calibrated extrinsic to transform the time-aligned LiDAR point clouds into depth images.
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** Our approach enhances the representation of Gaussians for objects in the images that lack LiDAR depth input via the introduced CGC. where di and ci ...
- **p. 4 / III. METHODOLOGY - extractive PDF cue:** The loss function used for optimizing the parameters of Gussians is designed as: L = (1 -λ1)Epho + λ1Egeo + λ2Enormal (10) where the first ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Our method estimates robot pose by aligning Gaussian covariance from rendering with the current observations, with the back-end correcting drift and updating the Gaussian map.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** To overcome depth continuity issues between vision and LiDAR in unbounded scenes, we propose a Gaussian splitting method based on LiDAR point clouds, ensuring proper ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | 7a and 7b, LiV-GS simultaneously reaches state-of-the-art performance in both accuracy and rendering quality with a running speed of 7.98 FPS, showing ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Back-End Optimization The back-end optimization process retrieves a sequence of keyframe identifiers along with their corresponding parameters and conducts two rounds of ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | 7a and 7b, LiV-GS simultaneously reaches state-of-the-art performance in both accuracy and rendering quality with a running speed of 7.98 FPS, showing ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / III. METHODOLOGY - extractive PDF cue:** We introduce a Conditional Gaussian Constraint (CGC) to adjust the positions of color-supervised Gaussians through the loss function (10).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Since, length, Gaussian, normal, difficult, restrict, during, optimization, introduced, normalization, point, clouds, Gaussians, robustness, tracking, algorithm, ensured, stable, orientation, introduce.
- **Relevant PDF headings:** III. METHODOLOGY (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | MonoGS, SplaTAM, GS-ICP-SLAM, and GaussianSLAM are all tailored for indoor environments with welltextured images and dense depth information, and they suffer performance ... | p. 6 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT) |
| Global / local decision | For rendering evaluation, the optimized viewpoints from each algorithm were extracted and compared against the actual images using metrics of SSIM, PSNR[dB], ... | p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT) |
| Motion execution / recovery | 8 highlights that even with cross-modal radar data, accurate localization is consistently achieved using Gaussian maps. | p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |

## Failure and Ablation Link

- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 3: Effect of Normal Restriction: Top: Ellipsoid vi- sualization. Middle: Render images. Bottom: Magnified details of the render. The left comparison (in red) illustrates ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 4: Effect of Splitting via conditional Gaussian con- straints (CGC). Our approach enhances the representation of Gaussians for objects in the images that lack ...
- **p. 7 / IV. EXPERIMENT - extractive PDF cue:** In this looped sequence, our LiV-GS still performs well but its performance falls behind some other algorithms occasionally.
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** MonoGS, SplaTAM, GS-ICP-SLAM, and GaussianSLAM are all tailored for indoor environments with welltextured images and dense depth information, and they suffer performance degradation or even ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 8: Visualization of cross-modal mmWave radar lo- calization trajectory. mmWave radar localization on the Gaussian map. Unlike LiDAR, the point clouds of mm-Wave radar ...
- **p. 6 / IV. EXPERIMENT - extractive PDF cue:** Our method does not use the IMU data.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), objective p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), temporal p. 7 (IV. EXPERIMENT), p. 4 (III. METHODOLOGY), p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 3 (III. METHODOLOGY).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
