# AERGS-SLAM: Auto-Exposure-Robust Stereo 3D Gaussian Splatting SLAM

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_AERGS-SLAM_Auto-Exposure-Robust_Stereo_3D_Gaussian_Splatting_SLAM_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhou_AERGS-SLAM_Auto-Exposure-Robust_Stereo_3D_Gaussian_Splatting_SLAM_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, geometry, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_AERGS-SLAM_Auto-Exposure-Robust_Stereo_3D_Gaussian_Splatting_SLAM_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhou_AERGS-SLAM_Auto-Exposure-Robust_Stereo_3D_Gaussian_Splatting_SLAM_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, such methods suffer from a key limitation: This CVPR paper is the Open Access version, provided by the Computer Vision Foundation.를 문제로 두고, To summarize, the main contributions of this work are as follows: • We propose a camera exposure network that recovers the camera's CRF to map per-image radiance maps to RGB images, enabling ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian splatting (3DGS) has emerged as a revolutionary scene representation in simultaneous localization and mapping (SLAM) research.
- **p. 1 / Abstract - extractive body cue:** However, existing research on 3DGS-based SLAM fails to accurately address the appearance variations induced by camera auto-exposure in prevalent real-world scenarios, resulting in reduced localization ...
- **p. 1 / Abstract - extractive body cue:** To address this issue, we propose a stereo auto-exposure-robust Gaussian splatting SLAM (AERGS-SLAM), a framework robust to such variations and enables both reliable localization and ...
- **p. 1 / Abstract - extractive body cue:** Our key contributions are two fold.
- **p. 1 / Abstract - extractive body cue:** Firstly, we propose a camera exposure network to model the camera exposure process, which we integrate with Gaussian splatting to achieve exposure-controlled novel view synthesis.
- **p. 1 / 1. Introduction - extractive body cue:** However, such methods suffer from a key limitation: This CVPR paper is the Open Access version, provided by the Computer Vision Foundation.
- **p. 2 / 1. Introduction - extractive body cue:** However, such coupled methods suffer from key limitations in localization robustness and real-time performance.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, the main contributions of this work are as follows: • We propose a camera exposure network that recovers the camera's CRF to map ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these problems, we propose a stereo decoupled auto-exposure-robust Gaussian splatting SLAM (AERGS-SLAM).
- **p. 6 / Method - extractive body cue:** Then, we evaluate on our self-collected dataset, which consists of six sequences captured using a ZED 2i stereo camera.
- **p. 6 / Method - extractive body cue:** Given its demonstrated superior performance in handling complex real-world scenarios and stereo setups in recent literature [14, 37], DROID-SLAM provides a reliable benchmark for assessing ...
- **p. 5 / 3.3.2. Coarse-To-Fine Optimization - extractive body cue:** To mitigate this limitation, we propose a time-aware sliding window coarse-to-fine strategy.
- **p. 6 / Method - extractive body cue:** For localization, we report the root mean square error (RMSE) of the absolute trajectory error for all frames.
- **p. 6 / Method - extractive body cue:** For quantitative evaluation, we adopt the trajectory from the SOTA learning-based stereo SLAM system DROID-SLAM [34] as the reference.
- **p. 5 / 3.3.2. Coarse-To-Fine Optimization - extractive body cue:** Methods [14, 37] adopt multi-scale frequency representations to accelerate training.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Brightness adjustment is modeled as Vout = AVint, where Vint and Vout are the input and output brightness of a pixel, respectively, and A is the scaling factor which is randomly sampled ... | camera/depth stream, pose, map와 language goal | p. 6 (Method), p. 1 (1. Introduction) |
| State/latent | Brightness, adjustment, modeled, Vout, AVint, where, Vint, input, output, pixel, respectively, scaling | robot pose, free-space/semantic map와 local goal | p. 6 (Method), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Output/action | Most 3DGS-based visual SLAM methods assume that input images strictly satisfy photometric consistency. | collision-free trajectory 또는 velocity command | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | Coarse-to-fine optimization strategy is effective in many SLAM methods. | goal reach, safety, localization error와 replanning latency | p. 5 (3.3.2. Coarse-To-Fine Optimization), p. 5 (3.3.2. Coarse-To-Fine Optimization) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, the main contributions of this work are as follows: • We propose a camera exposure network that recovers the camera's CRF to map ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these problems, we propose a stereo decoupled auto-exposure-robust Gaussian splatting SLAM (AERGS-SLAM).
- **p. 6 / Method - extractive body cue:** Then, we evaluate on our self-collected dataset, which consists of six sequences captured using a ZED 2i stereo camera.
- **p. 6 / Method - extractive body cue:** Given its demonstrated superior performance in handling complex real-world scenarios and stereo setups in recent literature [14, 37], DROID-SLAM provides a reliable benchmark for assessing ...
- **p. 5 / 3.3.2. Coarse-To-Fine Optimization - extractive body cue:** To mitigate this limitation, we propose a time-aware sliding window coarse-to-fine strategy.
- **p. 7 / 4.3. Results and Evaluation - extractive body cue:** Secondly, on the self-collected dataset, AERGS-SLAM achieves significantly higher localization accuracy than all baselines, confirming its generalization to real-world scenarios.
- **p. 7 / 4.3. Results and Evaluation - extractive body cue:** On the processed EuRoC dataset [1], AERGS-SLAM achieves the best localization performance against 3DGS-based baselines.
- **p. 8 / 4.4. Ablation Studies - extractive body cue:** Firstly, as shown in the rows (3) and (5) of Table 3, the employment of the CEN module significantly enhances the quality of photometric mapping ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.3. Results and Evaluation), p. 7 (4.3. Results and Evaluation) |
| Embodiment/environment | Secondly, on the self-collected dataset, AERGS-SLAM achieves significantly higher localization accuracy than all baselines, confirming its generalization to real-world scenarios. | hardware/simulator version and reset protocol | p. 7 (4.3. Results and Evaluation), p. 7 (4.3. Results and Evaluation) |
| Dataset/benchmark | Experiments are conducted on the processed EuRoC and self-collected datasets. | role, split, size and leakage | p. 7 (4.3. Results and Evaluation), p. 7 (4.3. Results and Evaluation), p. 8 (4.4. Ablation Studies), p. 8 (4.4. Ablation Studies) |
| Metric | Additionally, compared with MonoGS [26], all decoupled pipelines achieve superior accuracy, highlighting the robustness of the decoupled framework. | definition, denominator, direction and uncertainty | p. 7 (4.3. Results and Evaluation), p. 7 (4.3. Results and Evaluation), p. 8 (4.4. Ablation Studies) |
| Baseline/ablation | We compare AERGS-SLAM with seven baselines: 1) MonoGS [26], a state-of-the-art (SOTA) coupled 3DGS-based SLAM method; 2) Photo-SLAM [14] and SEGS-SLAM [37], representative decoupled 3DGS-based methods; 3) Ours + HDR-GS, a variant ... | fair input/data/compute/action matching | p. 5 (4.2. Experiment Setup), p. 7 (4.3. Results and Evaluation), p. 7 (4.3. Results and Evaluation) |

## Explicit Limitations and Failure Boundary

- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative results of localization (RMSE ↓). We color code eac column as best and second best. 'X' denotes running failure in our experiments. ...
- **p. 8 / 5. Conclusion - extractive body cue:** Extensive experiments show the IRL module significantly improves localization accuracy and robustness.
- **p. 8 / 5. Conclusion - extractive body cue:** It adopts a decoupled pipeline enabling illumination-robust localization and auto-exposurerobust photorealistic mapping.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the proposed AERGS-SLAM. Firstly, the localization thread performs illumination-robust localization using stereo images, generating posed keyframes and sparse point clouds to ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Feature detection in illumination-varying scene. handcrafted features [3] lack sufficient robustness to such appearance variations, reducing the reliability of residual E(k, j). As ...
- **p. 7 / 4.3. Results and Evaluation - extractive body cue:** Overall, these comprehensive evaluation results validate the effectiveness of our illumination-robust localization pipeline.
- **p. 7 / 4.3. Results and Evaluation - extractive body cue:** Additionally, compared with MonoGS [26], all decoupled pipelines achieve superior accuracy, highlighting the robustness of the decoupled framework.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, such methods suffer from a key limitation: This CVPR paper is the Open Access version, provided by the Computer Vision Foundation.를 문제로 두고, To summarize, the main contributions of this work are as follows: • We propose a camera exposure network that recovers the camera's CRF to map per-image radiance maps to RGB images, enabling ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 6 (Method), p. 6 (Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
