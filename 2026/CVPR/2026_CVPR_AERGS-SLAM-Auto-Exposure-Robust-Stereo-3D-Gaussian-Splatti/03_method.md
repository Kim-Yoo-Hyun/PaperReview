# Method - AERGS-SLAM: Auto-Exposure-Robust Stereo 3D Gaussian Splatting SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_AERGS-SLAM_Auto-Exposure-Robust_Stereo_3D_Gaussian_Splatting_SLAM_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhou_AERGS-SLAM_Auto-Exposure-Robust_Stereo_3D_Gaussian_Splatting_SLAM_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (Method), p. 6 (Method), p. 5 (3.3.2. Coarse-To-Fine Optimization), p. 5 (3.3.2. Coarse-To-Fine Optimization)): For localization, we report the root mean square error (RMSE) of the absolute trajectory error for all frames.

## Method Body Digest

- **p. 6 / Method - extractive PDF cue:** For localization, we report the root mean square error (RMSE) of the absolute trajectory error for all frames.
- **p. 6 / Method - extractive PDF cue:** For quantitative evaluation, we adopt the trajectory from the SOTA learning-based stereo SLAM system DROID-SLAM [34] as the reference.
- **p. 5 / 3.3.2. Coarse-To-Fine Optimization - extractive PDF cue:** Methods [14, 37] adopt multi-scale frequency representations to accelerate training.
- **p. 5 / 3.3.2. Coarse-To-Fine Optimization - extractive PDF cue:** Coarse-to-fine optimization strategy is effective in many SLAM methods.
- **p. 5 / 3.3.2. Coarse-To-Fine Optimization - extractive PDF cue:** However, these methods use a fixed low-to-high frequency progression for the entire scene and overlook the temporal dynamics of SLAM keyframes, where new and old ...
- **p. 6 / Method - extractive PDF cue:** Brightness adjustment is modeled as Vout = AVint, where Vint and Vout are the input and output brightness of a pixel, respectively, and A is ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Most 3DGS-based visual SLAM methods assume that input images strictly satisfy photometric consistency.
- **p. 1 / 1. Introduction - extractive PDF cue:** However, to capture high-quality images, cameras automatically regulate light input via auto-exposure (AE) algorithms, which induces appearance variations in images and leads to photometric inconsistency.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** To summarize, the main contributions of this work are as follows: • We propose a camera exposure network that recovers the camera's CRF to map ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To address these problems, we propose a stereo decoupled auto-exposure-robust Gaussian splatting SLAM (AERGS-SLAM).
- **p. 6 / Method - extractive PDF cue:** Then, we evaluate on our self-collected dataset, which consists of six sequences captured using a ZED 2i stereo camera.

## Source Evidence Cues

- **p. 6 / Method - extractive PDF cue:** For localization, we report the root mean square error (RMSE) of the absolute trajectory error for all frames.
- **p. 6 / Method - extractive PDF cue:** For quantitative evaluation, we adopt the trajectory from the SOTA learning-based stereo SLAM system DROID-SLAM [34] as the reference.
- **p. 5 / 3.3.2. Coarse-To-Fine Optimization - extractive PDF cue:** Methods [14, 37] adopt multi-scale frequency representations to accelerate training.
- **p. 5 / 3.3.2. Coarse-To-Fine Optimization - extractive PDF cue:** Coarse-to-fine optimization strategy is effective in many SLAM methods.
- **Detected method headings:** Method (p. 6); Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | For localization, we report the root mean square error (RMSE) of the absolute trajectory error for all frames. | p. 6 (Method), p. 6 (Method) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | For quantitative evaluation, we adopt the trajectory from the SOTA learning-based stereo SLAM system DROID-SLAM [34] as the reference. | p. 6 (Method), p. 5 (3.3.2. Coarse-To-Fine Optimization) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Methods [14, 37] adopt multi-scale frequency representations to accelerate training. | p. 5 (3.3.2. Coarse-To-Fine Optimization), p. 5 (3.3.2. Coarse-To-Fine Optimization) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3.2. Coarse-To-Fine Optimization - extractive PDF cue:** Coarse-to-fine optimization strategy is effective in many SLAM methods.
- **p. 5 / 3.3.2. Coarse-To-Fine Optimization - extractive PDF cue:** However, these methods use a fixed low-to-high frequency progression for the entire scene and overlook the temporal dynamics of SLAM keyframes, where new and old ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (3.3.2. Coarse-To-Fine Optimization).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Brightness, adjustment, modeled, Vout, AVint, where, Vint, input, output, pixel, respectively, scaling, factor, randomly | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Brightness, adjustment, modeled, Vout, AVint, where, Vint, input, output, pixel | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | summarize, main, contributions, follows, camera, exposure, network, recovers, CRF, per-image | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Coarse-to-fine, optimization, strategy, effective, many, SLAM, methods, However, fixed, low-to-high | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / Method - extractive PDF cue:** Brightness adjustment is modeled as Vout = AVint, where Vint and Vout are the input and output brightness of a pixel, respectively, and A is ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Most 3DGS-based visual SLAM methods assume that input images strictly satisfy photometric consistency.
- **p. 1 / 1. Introduction - extractive PDF cue:** However, to capture high-quality images, cameras automatically regulate light input via auto-exposure (AE) algorithms, which induces appearance variations in images and leads to photometric inconsistency.
- **p. 2 / 1. Introduction - extractive PDF cue:** Motivated by the physical image formation process [8], we propose a camera exposure network that models the CRF to map perimage radiance maps to red-green-blue ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To summarize, the main contributions of this work are as follows: • We propose a camera exposure network that recovers the camera's CRF to map ...
- **p. 6 / Method - extractive PDF cue:** Inspired by [38], we process the EuRoC MAV dataset [1] by adjusting image brightness to simulate AE-induced exposure variations.
- **p. 5 / 3.3.2. Coarse-To-Fine Optimization - extractive PDF cue:** To implement this, we design a novel image sampling strategy within the sliding window.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Additionally, these methods only adopt multi-scale frequency representations to accelerate training, failing to account for the temporal dynamics of consecutive frames. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | However, these methods use a fixed low-to-high frequency progression for the entire scene and overlook the temporal dynamics of SLAM keyframes, where ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3.2. Coarse-To-Fine Optimization - extractive PDF cue:** Methods [14, 37] adopt multi-scale frequency representations to accelerate training.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** localization, report, root, mean, square, error, RMSE, absolute, trajectory, frames, quantitative, evaluation, adopt, SOTA, learning-based, stereo, SLAM, system, DROID-SLAM, reference.
- **Relevant PDF headings:** Method (p. 6); Method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Secondly, on the self-collected dataset, AERGS-SLAM achieves significantly higher localization accuracy than all baselines, confirming its generalization to real-world scenarios. | p. 7 (4.3. Results and Evaluation), p. 7 (4.3. Results and Evaluation) |
| Global / local decision | We compare AERGS-SLAM with seven baselines: 1) MonoGS [26], a state-of-the-art (SOTA) coupled 3DGS-based SLAM method; 2) Photo-SLAM [14] and SEGS-SLAM [37], ... | p. 5 (4.2. Experiment Setup), p. 7 (4.3. Results and Evaluation) |
| Motion execution / recovery | Secondly, on the self-collected dataset, AERGS-SLAM achieves significantly higher localization accuracy than all baselines, confirming its generalization to real-world scenarios. | p. 7 (4.3. Results and Evaluation), p. 7 (4.3. Results and Evaluation) |

## Failure and Ablation Link

- **p. 8 / 4.4. Ablation Studies - extractive PDF cue:** The ablation results are reported in Table 3 within Row (1) (i.e., without CTFO, CEN and IRL) corresponds to the original Photo-SLAM [14].
- **p. 8 / 4.4. Ablation Studies - extractive PDF cue:** These ablation results consistently demonstrate that the proposed time-aware coarse-to-fine optimization strategy can effectively improve the quality of photorealistic mapping.
- **p. 5 / 4.2. Experiment Setup - extractive PDF cue:** We compare AERGS-SLAM with seven baselines: 1) MonoGS [26], a state-of-the-art (SOTA) coupled 3DGS-based SLAM method; 2) Photo-SLAM [14] and SEGS-SLAM [37], representative decoupled 3DGS-based ...
- **p. 5 / 4. Experiments - extractive PDF cue:** Section 4.4 reports ablation studies.
- **p. 7 / 4.3. Results and Evaluation - extractive PDF cue:** For the EuRoC dataset [1], AERGS-SLAM outperforms Photo-SLAM [14] without using any exposure mechanism, SEGS-SLAM utilizing appearance embedding, and MonoGS utilizing learnable exposure parameters.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative results of localization (RMSE ↓). We color code eac column as best and second best. 'X' denotes running failure in our experiments. ...
- **p. 8 / 5. Conclusion - extractive PDF cue:** Extensive experiments show the IRL module significantly improves localization accuracy and robustness.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (Method), p. 6 (Method), p. 5 (3.3.2. Coarse-To-Fine Optimization), p. 5 (3.3.2. Coarse-To-Fine Optimization), objective p. 5 (3.3.2. Coarse-To-Fine Optimization), p. 5 (3.3.2. Coarse-To-Fine Optimization), temporal p. 2 (1. Introduction), p. 5 (3.3.2. Coarse-To-Fine Optimization), p. 2 (2. Related Work), p. 5 (4.1. Implementation Details), p. 6 (Method), p. 6 (Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
