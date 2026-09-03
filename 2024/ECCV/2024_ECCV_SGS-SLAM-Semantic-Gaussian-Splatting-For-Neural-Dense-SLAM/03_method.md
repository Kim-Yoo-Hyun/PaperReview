# Method - SGS-SLAM: Semantic Gaussian Splatting For Neural Dense SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4516_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04516.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 8 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 6 (3 Method)): Compared to existing NeRF-based approaches [16,20,47,48] that necessitate complex model architectures and feature fusion strategies, SGS-SLAM adopts explicit Gaussian representation for mapping, resulting in high rendering speeds and op ...

## Method Body Digest

- **p. 8 / 3 Method - extractive body cue:** Compared to existing NeRF-based approaches [16,20,47,48] that necessitate complex model architectures and feature fusion strategies, SGS-SLAM adopts explicit Gaussian representation for mapping, resulting in high ...
- **p. 4 / 3 Method - extractive body cue:** 3.1 introduces its multi-channel Gaussian representation for joint parameter optimization.
- **p. 6 / 3 Method - extractive body cue:** Furthermore, the integration of semantic features within our method significantly advances optimal scene interpretation and precise object-level geometry, effectively mitigating the oversmoothing issues prevalent in ...
- **p. 4 / 3 Method - extractive body cue:** Mapping optimizes the scene representations based on the estimated camera pose.
- **p. 5 / 3 Method - extractive body cue:** SGS-SLAM: Semantic Gaussian Splatting For Neural Dense SLAM 5 3.1 Multi-Channel Gaussian Representation The scene is represented using a Gaussian influence function f(·) on the ...
- **p. 6 / 3 Method - extractive body cue:** The Gaussian representations employed in SGS-SLAM facilitate high-quality reconstructions at high rendering speed, offering exceptional accuracy in capturing complex textures and geometry with remarkable detail ...
- **p. 7 / 3 Method - extractive body cue:** This uncertainty score is used to weight the mapping loss Lmapping.
- **p. 7 / 3 Method - extractive body cue:** After densification, the parameters of the map are optimized by minimizing the mapping loss: \mathc a l { L}_ {\rm m app i ng} = ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** Overall, our work presents several key contributions, summarized as follows: - We introduce SGS-SLAM, the first semantic RGB-D SLAM system grounded in 3D Gaussians.
- **p. 3 / 1 Introduction - extractive body cue:** Leveraging these benefits, our method enables precise editing and manipulation of specific scene elements while preserving the high fidelity of the overall rendering.
- **p. 4 / 3 Method - extractive body cue:** Like previous SLAM techniques, our method can be split into two processes: tracking and mapping.

## Source Evidence Cues

- **p. 8 / 3 Method - extractive body cue:** Compared to existing NeRF-based approaches [16,20,47,48] that necessitate complex model architectures and feature fusion strategies, SGS-SLAM adopts explicit Gaussian representation for mapping, resulting in high ...
- **p. 4 / 3 Method - extractive body cue:** 3.1 introduces its multi-channel Gaussian representation for joint parameter optimization.
- **p. 6 / 3 Method - extractive body cue:** Furthermore, the integration of semantic features within our method significantly advances optimal scene interpretation and precise object-level geometry, effectively mitigating the oversmoothing issues prevalent in ...
- **p. 4 / 3 Method - extractive body cue:** Mapping optimizes the scene representations based on the estimated camera pose.
- **p. 5 / 3 Method - extractive body cue:** SGS-SLAM: Semantic Gaussian Splatting For Neural Dense SLAM 5 3.1 Multi-Channel Gaussian Representation The scene is represented using a Gaussian influence function f(·) on the ...
- **p. 6 / 3 Method - extractive body cue:** The Gaussian representations employed in SGS-SLAM facilitate high-quality reconstructions at high rendering speed, offering exceptional accuracy in capturing complex textures and geometry with remarkable detail ...
- **p. 7 / 3 Method - extractive body cue:** This uncertainty score is used to weight the mapping loss Lmapping.
- **Detected method headings:** 3 Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Compared to existing NeRF-based approaches [16,20,47,48] that necessitate complex model architectures and feature fusion strategies, SGS-SLAM adopts explicit Gaussian representation for mapping, ... | p. 8 (3 Method), p. 4 (3 Method) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | 3.1 introduces its multi-channel Gaussian representation for joint parameter optimization. | p. 4 (3 Method), p. 6 (3 Method) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Furthermore, the integration of semantic features within our method significantly advances optimal scene interpretation and precise object-level geometry, effectively mitigating the oversmoothing ... | p. 6 (3 Method), p. 4 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / 3 Method - extractive body cue:** After densification, the parameters of the map are optimized by minimizing the mapping loss: \mathc a l { L}_ {\rm m app i ng} = ...
- **p. 6 / 3 Method - extractive body cue:** Following this, the current pose is iteratively refined by minimizing the tracking loss between the ground truth color (CGT pix ), depth images (DGT pix ...
- **p. 6 / 3 Method - extractive body cue:** Subsequently, keyframes associated with the current frame are chosen based on geometric and semantic constraints.
- **p. 7 / 3 Method - extractive body cue:** This uncertainty score is used to weight the mapping loss Lmapping.
- **p. 4 / 3 Method - extractive body cue:** Mapping optimizes the scene representations based on the estimated camera pose.
- **p. 4 / 3 Method - extractive body cue:** 3.1 introduces its multi-channel Gaussian representation for joint parameter optimization.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 7 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Following, current, pose, iteratively, refined, minimizing, tracking, loss, between, ground, truth, color, CGT, depth | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Following, current, pose, iteratively, refined, minimizing, tracking, loss, between, ground | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | Overall, presents, several, contributions, summarized, follows, introduce, SGS-SLAM, first, semantic | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | After, densification, parameters, optimized, minimizing, mapping, loss, mathc, lambda, mathcal | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 3 Method - extractive body cue:** Following this, the current pose is iteratively refined by minimizing the tracking loss between the ground truth color (CGT pix ), depth images (DGT pix ...
- **p. 5 / 3 Method - extractive body cue:** This aspect of visibility is essential for camera pose estimation, as it relies on the current reconstructed map.
- **p. 5 / 3 Method - extractive body cue:** It works by splatting 3D Gaussians into the image plane via approximating the integral projection of the influence function f(·) along the depth dimension in ...
- **p. 6 / 3 Method - extractive body cue:** While assessing the camera pose of an RGB-D view at a new timestep, the initial camera pose is determined by adding a displacement to the ...
- **p. 7 / 3 Method - extractive body cue:** After densification, the parameters of the map are optimized by minimizing the mapping loss: \mathc a l { L}_ {\rm m app i ng} = ...
- **p. 2 / 1 Introduction - extractive body cue:** It employs 2D inputs encompassing appearance, geometry, and semantic information, leveraging Gaussian Splatting and differentiable rendering for multi-channel parameter optimization.
- **p. 1 / 1 Introduction - extractive body cue:** It aims to reconstruct a dense 3D map in an unseen environment while simultaneously tracking the camera poses.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Our approach offers an unparalleled ability to identify 3D objects in decomposed representations, which can serve as 3D priors for tracking and ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | While assessing the camera pose of an RGB-D view at a new timestep, the initial camera pose is determined by adding a ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 11 / 4 Experiment - extractive body cue:** For each scene, we compute the average mIoU score by comparing the rendered and the ground-truth 2D semantic image in the training view.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Compared, existing, NeRF-based, approaches, necessitate, complex, model, architectures, feature, fusion, strategies, SGS-SLAM, adopts, explicit, Gaussian, representation, mapping, resulting, high, rendering.
- **Relevant PDF headings:** 3 Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | To compare with other neural implicit SLAM methods, we evaluate synthetic scenes from Replica dataset [35] and real-world scenes from ScanNet [4] ... | p. 8 (4 Experiment), p. 11 (4 Experiment) |
| Global / local decision | In comparison to these previous methods, SGS-SLAM demonstrates state-of-the-art performance, outperforming the initial baseline by more than 10%. | p. 11 (4 Experiment), p. 9 (4 Experiment) |
| Motion execution / recovery | The results reveal that our optimization strategy can significantly improve the localization and mapping performance. | p. 13 (4 Experiment), p. 11 (4 Experiment) |

## Failure and Ablation Link

- **p. 13 / 4 Experiment - extractive body cue:** Settings Depth L1 [cm]↓ ATE RMSE [cm]↓ PSNR [dB]↑ mIoU [%]↑ without color image (Cpix) 7.44 24.59 ✗ 68.19 without depth map (Dpix) 47.66 40.47 ...
- **p. 13 / 4 Experiment - extractive body cue:** 4.6 Ablation Study We perform the ablation of SGS-SLAM on the scene0000_00 of the ScanNet dataset [4] to evaluate the effectiveness of multi-channel feature supervision, ...
- **p. 14 / 4 Experiment - extractive body cue:** Without this threshold, the system shows a significant decline in the effectiveness of tracking and mapping.
- **p. 14 / Figure/Table caption - extractive body cue:** Table 5: Ablation study of keyframe optimization on the scene0000 of the ScanNet dataset [4]. The comparison involves settings where geometric, semantic, and uncer- tainty ...
- **p. 12 / 4 Experiment - extractive body cue:** Utilizing the decoupled scene representation, in contrast to NeRF-based approaches that demand fine-tuning of the entire network, SGS-SLAM can edit specific objects within the scene ...
- **p. 13 / 4 Experiment - extractive body cue:** Specifically, the system without appearance color cannot provide rendered views, whereas camera pose and depth can still be estimated by leveraging depth and
- **p. 14 / 4 Experiment - extractive body cue:** Addressing these limitations will be an objective for future research.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 8 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 6 (3 Method), objective p. 7 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 4 (3 Method), p. 4 (3 Method), temporal p. 11 (4 Experiment), p. 6 (3 Method), p. 7 (3 Method), p. 11 (4 Experiment), p. 4 (3 Method), p. 4 (3 Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
