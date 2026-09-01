# Method - VarSplat: Uncertainty-aware 3D Gaussian Splatting for Robust RGB-D SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Tran_VarSplat_Uncertainty-aware_3D_Gaussian_Splatting_for_Robust_RGB-D_SLAM_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Tran_VarSplat_Uncertainty-aware_3D_Gaussian_Splatting_for_Robust_RGB-D_SLAM_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Mapping), p. 4 (3.2. Mapping), p. 5 (3.3. Downstream Pose Estimation), p. 5 (3.3. Downstream Pose Estimation), p. 3 (3.1. Per-pixel uncertainty rendering), p. 3 (3. Method)): To stay consistent with the Gaussian view, we use square L2 (MSE) for variance loss Lvar.

## Method Body Digest

- **p. 4 / 3.2. Mapping - extractive PDF cue:** To stay consistent with the Gaussian view, we use square L2 (MSE) for variance loss Lvar.
- **p. 4 / 3.2. Mapping - extractive PDF cue:** For color supervision, we use a weighted combination of L1 and SSIM [16], while depth loss is L1 between rendered and ground-truth depth.
- **p. 5 / 3.3. Downstream Pose Estimation - extractive PDF cue:** Thanks to the explicit representation and the parallel optimization of poses and Gaussian parameters, we can simultaneously freeze the variance during tracking and registration, while ...
- **p. 5 / 3.3. Downstream Pose Estimation - extractive PDF cue:** The merged geometry is then used to initialize Gaussian centers in the global map, which are subsequently refined using the color reconstruction loss Lcolor as ...
- **p. 3 / 3.1. Per-pixel uncertainty rendering - extractive PDF cue:** Even when the SH color correctly models the mean, view-dependent appearance, the actual color observations at a splat can vary across viewpoints.
- **p. 3 / 3. Method - extractive PDF cue:** However, pose estimation through photometric optimization can suffer from unreliable observations in low-texture regions, reflective surfaces, and areas near depth discontinuities, which can destabilize this ...
- **p. 5 / 3.3. Downstream Pose Estimation - extractive PDF cue:** Therefore, optimizing a pure photometric loss for pose refinement can lead to unstable gradients.
- **p. 5 / 3.2. Mapping - extractive PDF cue:** Gradients from both color and depth residuals update per-splat variance, so the predicted variance reflects measurement reliability and avoids overconfidence in reflective, transparent, or glossy ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, our contributions can be shown as follows: • We introduce VarSplat, an RGB-D 3DGS-SLAM system that learns per-splat appearance variance σ2 to render ...
- **p. 3 / 3. Method - extractive PDF cue:** To address these issues, we introduce a novel uncertainty quantification pipeline based on per-pixel uncertainty map rendering.
- **p. 2 / 1. Introduction - extractive PDF cue:** To address these challenges, we introduce VarSplat, an uncertainty-aware RGB-D SLAM system leveraging 3D Gaussian Splatting.

## Source Evidence Cues

- **p. 4 / 3.2. Mapping - extractive PDF cue:** To stay consistent with the Gaussian view, we use square L2 (MSE) for variance loss Lvar.
- **p. 4 / 3.2. Mapping - extractive PDF cue:** For color supervision, we use a weighted combination of L1 and SSIM [16], while depth loss is L1 between rendered and ground-truth depth.
- **p. 5 / 3.3. Downstream Pose Estimation - extractive PDF cue:** Thanks to the explicit representation and the parallel optimization of poses and Gaussian parameters, we can simultaneously freeze the variance during tracking and registration, while ...
- **p. 5 / 3.3. Downstream Pose Estimation - extractive PDF cue:** The merged geometry is then used to initialize Gaussian centers in the global map, which are subsequently refined using the color reconstruction loss Lcolor as ...
- **p. 3 / 3.1. Per-pixel uncertainty rendering - extractive PDF cue:** Even when the SH color correctly models the mean, view-dependent appearance, the actual color observations at a splat can vary across viewpoints.
- **p. 3 / 3. Method - extractive PDF cue:** However, pose estimation through photometric optimization can suffer from unreliable observations in low-texture regions, reflective surfaces, and areas near depth discontinuities, which can destabilize this ...
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | To stay consistent with the Gaussian view, we use square L2 (MSE) for variance loss Lvar. | p. 4 (3.2. Mapping), p. 4 (3.2. Mapping) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | For color supervision, we use a weighted combination of L1 and SSIM [16], while depth loss is L1 between rendered and ground-truth ... | p. 4 (3.2. Mapping), p. 5 (3.3. Downstream Pose Estimation) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Thanks to the explicit representation and the parallel optimization of poses and Gaussian parameters, we can simultaneously freeze the variance during tracking ... | p. 5 (3.3. Downstream Pose Estimation), p. 5 (3.3. Downstream Pose Estimation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Downstream Pose Estimation - extractive PDF cue:** Therefore, optimizing a pure photometric loss for pose refinement can lead to unstable gradients.
- **p. 5 / 3.2. Mapping - extractive PDF cue:** Gradients from both color and depth residuals update per-splat variance, so the predicted variance reflects measurement reliability and avoids overconfidence in reflective, transparent, or glossy ...
- **p. 4 / 3.2. Mapping - extractive PDF cue:** Similar to [45], we also add regularization loss to control Gaussian scales: Lcolor = (1-λSSIM)∥ˆI-I∥1+λSSIM(1-SSIM(ˆI, I)) (11) Ldepth = ∥ˆD -D∥1, Lreg = ∥ˆs -s∥1 ...
- **p. 4 / 3.2. Mapping - extractive PDF cue:** To stay consistent with the Gaussian view, we use square L2 (MSE) for variance loss Lvar.
- **p. 3 / 3.1. Per-pixel uncertainty rendering - extractive PDF cue:** Using σ2 makes it clear that we optimize a true statistical variance rather than a free scale weight.
- **p. 3 / 3. Method - extractive PDF cue:** Unlike previous methods relying on pretrained predictors [19, 50], VarSplat learns this variance parameter from scratch, jointly optimizing them with appearance and geometry during mapping.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (3.2. Mapping), p. 5 (3.3. Downstream Pose Estimation), p. 4 (3.2. Mapping), p. 4 (3.2. Mapping), p. 3 (3. Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | VarSplat, RGB-D, SLAM, jointly, estimates, camera, poses, incrementally, updates, Gaussian, Splatting, DGS, input, frames | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | VarSplat, RGB-D, SLAM, jointly, estimates, camera, poses, incrementally, updates, Gaussian | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | summary, contributions, follows, introduce, VarSplat, RGB-D, DGS-SLAM, system, learns, per-splat | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Therefore, optimizing, pure, photometric, loss, pose, refinement, lead, unstable, gradients | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3. Method - extractive PDF cue:** VarSplat is an RGB-D SLAM approach that jointly estimates camera poses and incrementally updates 3D Gaussian Splatting (3DGS) map from input frames, following the general ...
- **p. 3 / 3. Method - extractive PDF cue:** However, pose estimation through photometric optimization can suffer from unreliable observations in low-texture regions, reflective surfaces, and areas near depth discontinuities, which can destabilize this ...
- **p. 4 / 3.2. Mapping - extractive PDF cue:** Given the current estimate Tj and keyframe color Ij, depth Dj images, we differentiably render the corresponding view from the current submap to obtain the ...
- **p. 4 / 3.2. Mapping - extractive PDF cue:** After sufficient observations, submap Gaussian parameters are jointly optimized to better align appearance and geometry with their associated keyframes.
- **p. 5 / 3.3. Downstream Pose Estimation - extractive PDF cue:** Unlike depth maps, RGB images are more susceptible to viewpoint changes, low texture, and occlusions.
- **p. 2 / 1. Introduction - extractive PDF cue:** The system is trained end-to-end online, jointly optimizing poses, Gaussian parameters, and σ2 as the map grows.
- **p. 2 / 1. Introduction - extractive PDF cue:** Uniform photometric weighting leaves pose estimation vulnerable in lowtexture regions, around depth discontinuities, and on reflective surfaces.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Perframe runtime is computed as total optimization time divided by the sequence length. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | In tracking, the per-pixel uncertainty map V provides short-horizon reliability measure within each submap, improving frame-to-frame pose updates. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. Downstream Pose Estimation - extractive PDF cue:** Thanks to the explicit representation and the parallel optimization of poses and Gaussian parameters, we can simultaneously freeze the variance during tracking and registration, while ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** stay, consistent, Gaussian, view, square, MSE, variance, loss, Lvar, color, supervision, weighted, combination, SSIM, while, depth, between, rendered, ground-truth, Thanks.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | In this section, we evaluate VarSplat against existing baselines on both synthetic and real-world datasets. | p. 6 (4. Experiments), p. 7 (4.2. Quantitative Evaluation) |
| Global / local decision | VarSplat outperforms both 3DGS and NeRF baselines. *Photo-SLAM [11] use ORB-SLAM3 features [2] for tracking and loop closure. | p. 6 (4.2. Quantitative Evaluation), p. 6 (4.1. Experimental Setup) |
| Motion execution / recovery | VarSplat achieves the highest accuracy with robustness on large motion camera. | p. 6 (4.2. Quantitative Evaluation), p. 6 (4.2. Quantitative Evaluation) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 3. Uncertainty ablation on ScanNet (scene0181). Without uncertainty, tracking jitters, loop detection has long-range drift, and registration ghosts submaps. With VarSplat enabled, the trajectory ...
- **p. 7 / 4.2. Quantitative Evaluation - extractive PDF cue:** Effect of uncertainty on pose estimation.
- **p. 6 / 4.2. Quantitative Evaluation - extractive PDF cue:** 90.4), indicating tighter alignment without surface inflation.
- **p. 6 / 4. Experiments - extractive PDF cue:** Moreover, we conduct ablation studies of the proposed uncertainty model, measuring its impact on tracking, registration, and loop detection.
- **p. 7 / 4.3. Ablation studies - extractive PDF cue:** We conduct all ablation studies on six ScanNet scenes.
- **p. 8 / 4.3. Ablation studies - extractive PDF cue:** Per-pixel uncertainty with vs. without depth on TUMRGBD (fr1/desk2).
- **p. 8 / 5. Conclusion - extractive PDF cue:** Limitations and future works are provided in Supplementary Material.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.2. Mapping), p. 4 (3.2. Mapping), p. 5 (3.3. Downstream Pose Estimation), p. 5 (3.3. Downstream Pose Estimation), p. 3 (3.1. Per-pixel uncertainty rendering), p. 3 (3. Method), objective p. 5 (3.3. Downstream Pose Estimation), p. 5 (3.2. Mapping), p. 4 (3.2. Mapping), p. 4 (3.2. Mapping), p. 3 (3.1. Per-pixel uncertainty rendering), p. 3 (3. Method), temporal p. 7 (4.2. Quantitative Evaluation), p. 2 (1. Introduction), p. 3 (3. Method), p. 4 (3.1. Per-pixel uncertainty rendering), p. 4 (3.2. Mapping), p. 5 (3.3. Downstream Pose Estimation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
