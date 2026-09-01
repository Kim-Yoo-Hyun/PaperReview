# Method - CG-SLAM: Efficient Dense RGB-D SLAM in a Consistent Uncertainty-aware 3D Gaussian Field

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3580_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03580.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (3 Method), p. 7 (3 Method), p. 9 (3 Method), p. 9 (3 Method), p. 5 (3 Method), p. 5 (3 Method)): To mitigate drastic changes in positions of Gaussian primitives during optimization, we proposed a geometry variance loss term (Eq.

## Method Body Digest

- **p. 7 / 3 Method - extractive PDF cue:** To mitigate drastic changes in positions of Gaussian primitives during optimization, we proposed a geometry variance loss term (Eq.
- **p. 7 / 3 Method - extractive PDF cue:** Hence, we propose an uncertainty model suitable for RGB-D observations from two perspectives: rendering images and Gaussian primitives.
- **p. 9 / 3 Method - extractive PDF cue:** Given the fixed scene representation, the camera pose is initially guessed via the constant speed assumption where the last pose is transformed by the last ...
- **p. 9 / 3 Method - extractive PDF cue:** In initialization, we densely project Gaussian primitives into 3D space based on depth observations of the first frame.
- **p. 5 / 3 Method - extractive PDF cue:** Finally, by minimizing the re-rendering loss from low-uncertainty primitives, we can build a real-time and accurate tracking module (Sec.
- **p. 5 / 3 Method - extractive PDF cue:** 3.1 Preliminary Scene Representation.
- **p. 6 / 3 Method - extractive PDF cue:** (9) 3.2 Uncertainty Modeling Uncertainty model remains a trending topic in multi-view 3D reconstruction in recent decades.
- **p. 8 / 3 Method - extractive PDF cue:** 3.3 Mapping We employ various loss functions to update Gaussian properties, aiming for a consistent and stable Gaussian field.

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** Overall, our contributions can be summarized as follows: - We present a new GPU-accelerated framework for real-time dense RGB-D SLAM based on a thorough theoretical ...
- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we introduce a real-time Gaussian splatting SLAM system, i.e., CG-SLAM, based on a novel uncertainty-aware 3D Gaussian field with high consistency and ...
- **p. 7 / 3 Method - extractive PDF cue:** To mitigate drastic changes in positions of Gaussian primitives during optimization, we proposed a geometry variance loss term (Eq.

## Source Evidence Cues

- **p. 7 / 3 Method - extractive PDF cue:** To mitigate drastic changes in positions of Gaussian primitives during optimization, we proposed a geometry variance loss term (Eq.
- **p. 7 / 3 Method - extractive PDF cue:** Hence, we propose an uncertainty model suitable for RGB-D observations from two perspectives: rendering images and Gaussian primitives.
- **p. 9 / 3 Method - extractive PDF cue:** Given the fixed scene representation, the camera pose is initially guessed via the constant speed assumption where the last pose is transformed by the last ...
- **p. 9 / 3 Method - extractive PDF cue:** In initialization, we densely project Gaussian primitives into 3D space based on depth observations of the first frame.
- **p. 5 / 3 Method - extractive PDF cue:** Finally, by minimizing the re-rendering loss from low-uncertainty primitives, we can build a real-time and accurate tracking module (Sec.
- **p. 5 / 3 Method - extractive PDF cue:** 3.1 Preliminary Scene Representation.
- **p. 6 / 3 Method - extractive PDF cue:** (9) 3.2 Uncertainty Modeling Uncertainty model remains a trending topic in multi-view 3D reconstruction in recent decades.
- **Detected method headings:** 3 Method (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | To mitigate drastic changes in positions of Gaussian primitives during optimization, we proposed a geometry variance loss term (Eq. | p. 7 (3 Method), p. 7 (3 Method) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Hence, we propose an uncertainty model suitable for RGB-D observations from two perspectives: rendering images and Gaussian primitives. | p. 7 (3 Method), p. 9 (3 Method) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Given the fixed scene representation, the camera pose is initially guessed via the constant speed assumption where the last pose is transformed ... | p. 9 (3 Method), p. 9 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 Method - extractive PDF cue:** Finally, by minimizing the re-rendering loss from low-uncertainty primitives, we can build a real-time and accurate tracking module (Sec.
- **p. 7 / 3 Method - extractive PDF cue:** To mitigate drastic changes in positions of Gaussian primitives during optimization, we proposed a geometry variance loss term (Eq.
- **p. 8 / 3 Method - extractive PDF cue:** 3.3 Mapping We employ various loss functions to update Gaussian properties, aiming for a consistent and stable Gaussian field.
- **p. 8 / 3 Method - extractive PDF cue:** To overcome anisotropic interference (Arrow-shaped Gaussian primitives), we add a soft scale regularization loss in the mapping process.
- **p. 5 / 3 Method - extractive PDF cue:** 3.3, we detail the Gaussian primitive management strategy and some innovative loss terms that ensure geometry stability and accuracy.
- **p. 6 / 3 Method - extractive PDF cue:** In terms of depth rendering, considering the loss term designed for geometry consistency, our rasterizer provides not only α-blending depth ˆDalpha but also the median ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 9 (3 Method), p. 8 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 7 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Hence, uncertainty, model, suitable, RGB-D, observations, perspectives, rendering, images, Gaussian, primitives, alpha, T_i, where | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Hence, uncertainty, model, suitable, RGB-D, observations, perspectives, rendering, images, Gaussian | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | Overall, contributions, summarized, follows, present, GPU-accelerated, framework, real-time, dense, RGB-D | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Finally, minimizing, re-rendering, loss, low-uncertainty, primitives, build, real-time, accurate, tracking | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 7 / 3 Method - extractive PDF cue:** Hence, we propose an uncertainty model suitable for RGB-D observations from two perspectives: rendering images and Gaussian primitives.
- **p. 7 / 3 Method - extractive PDF cue:** \ l abe l {eq -1 0 } U = \sum _{i=1}^N \alpha _i T_i (~d_i - D~)^2~, (10) where D represents depth observations from ...
- **p. 8 / 3 Method - extractive PDF cue:** 8 Jiarui Hu and Xianhao Chen et al. is determined by the difference between its depth and depth observations from all its dominated pixels within ...
- **p. 8 / 3 Method - extractive PDF cue:** Dk p represents the depth observation on a pixel p in fk. dk i is the depth value of the i-th Gaussian primitive at fk. ...
- **p. 9 / 3 Method - extractive PDF cue:** In initialization, we densely project Gaussian primitives into 3D space based on depth observations of the first frame.
- **p. 2 / 1 Introduction - extractive PDF cue:** As a photorealistic view synthesis technique, the 3D Gaussian field is prone to overfitting the input images due to strong anisotropy and the lack of ...
- **p. 2 / 1 Introduction - extractive PDF cue:** 1: CG-SLAM, which adopts a well-designed 3D Gaussian field, can simultaneously achieve state-of-the-art performance in localization, reconstruction and rendering.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | In addition to keyframes from NetVLAD [2], we also added the current frame and the most recent keyframes in the sliding window ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | FPS ≈15 Hz Mean PSNR: 33.27 dB Mean PSNR: 34.60 dB Acc: 1.10 cm RMSE: 0.29 cm Acc: 1.28 cm RMSE: 0.31 ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | FPS ≈15 Hz Mean PSNR: 33.27 dB Mean PSNR: 34.60 dB Acc: 1.10 cm RMSE: 0.29 cm Acc: 1.28 cm RMSE: 0.31 ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** mitigate, drastic, changes, positions, Gaussian, primitives, during, optimization, geometry, variance, loss, term, Hence, uncertainty, model, suitable, RGB-D, observations, perspectives, rendering.
- **Relevant PDF headings:** 3 Method (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | We examined the generalization of our method on real-world TUM [44] and ScanNet [10] datasets, which contain 5 and 6 challenging scenes ... | p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Global / local decision | We primarily consider state-of-the-art NeRF-SLAM works, including NICE-SLAM [61], Co-SLAM [50], Point-SLAM [37], and Vox-Fusion [56], as baselines. | p. 10 (4 Experiments), p. 11 (4 Experiments) |
| Motion execution / recovery | In this section, we describe our experimental setup and validate that the proposed system can achieve improvement in both accuracy (Sec. | p. 9 (4 Experiments), p. 11 (4 Experiments) |

## Failure and Ablation Link

- **p. 13 / 56.50 MB - extractive PDF cue:** 4.4 Ablation Study To verify the rationality of our designs, we investigate the effectiveness of the anisotropy regularization, alignment and variance losses, and uncertainty model.
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 6: Isotropy Loss Ablation Results(ATE RMSE [cm] ↓). The experimental results demonstrate the effectiveness of our anisotropy regularization term. "-" indicates a failure situation. ...
- **p. 13 / 56.50 MB - extractive PDF cue:** To more intuitively illustrate this phenomenon, we display opacity maps with and without anisotropy regularization in Fig.
- **p. 14 / 56.50 MB - extractive PDF cue:** For further quantitative ablation results, refer to the supplementary material.
- **p. 14 / 5 Conclusion - extractive PDF cue:** Considerable memory usage is one limitation of the Gaussianbased system.
- **p. 11 / 4 Experiments - extractive PDF cue:** Our method achieves state-of-the-art tracking results in 6 scenes and exceeds other methods on average. "-" indicates failure results in Vox-Fusion [56].
- **p. 14 / 56.50 MB - extractive PDF cue:** The experimental results demonstrate the effectiveness of our anisotropy regularization term. "-" indicates a failure situation.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (3 Method), p. 7 (3 Method), p. 9 (3 Method), p. 9 (3 Method), p. 5 (3 Method), p. 5 (3 Method), objective p. 5 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method), p. 5 (3 Method), p. 6 (3 Method), temporal p. 9 (3 Method), p. 2 (1 Introduction), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
