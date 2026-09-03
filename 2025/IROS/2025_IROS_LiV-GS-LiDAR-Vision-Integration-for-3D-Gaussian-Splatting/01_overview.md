# LiV-GS: LiDAR-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2411.12185.
> PDF retrieval source: https://arxiv.org/pdf/2411.12185. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Gaussian Splatting
- Official paper: https://arxiv.org/abs/2411.12185
- Full-text retrieval: https://arxiv.org/pdf/2411.12185
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Outdoor SLAM and scene reconstruction face unique challenges, such as lighting variations and unbounded depth scales, which make indoor RGBD-based solutions inadequate [4]-[8].를 문제로 두고, To the end, we introduce LiV-GS, a SLAM framework that uses 3D Gaussian spatial representations to seamlessly integrate LiDAR and camera images.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present LiV-GS, a LiDAR-visual SLAM system in outdoor environments that leverages 3D Gaussian as a differentiable spatial representation.
- **p. 1 / Abstract - extractive body cue:** Notably, LiV-GS is the first method that directly aligns discrete and sparse LiDAR data with continuous differentiable Gaussian maps in large-scale outdoor scenes, overcoming the ...
- **p. 1 / Abstract - extractive body cue:** The system aligns point clouds with Gaussian maps using shared covariance attributes for front-end tracking and integrates the normal orientation into the loss function to ...
- **p. 1 / Abstract - extractive body cue:** To reliably and stably update Gaussians outside the LiDAR field of view, we introduce a novel conditional Gaussian constraint that aligns these Gaussians closely with ...
- **p. 1 / Abstract - extractive body cue:** The targeted adjustment enables LiV-GS to achieve fast and accurate mapping with novel view synthesis at a rate of 7.98 FPS.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Outdoor SLAM and scene reconstruction face unique challenges, such as lighting variations and unbounded depth scales, which make indoor RGBD-based solutions inadequate [4]-[8].
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method estimates robot pose by aligning Gaussian covariance from rendering with the current observations, with the back-end correcting drift and updating the Gaussian map.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** To the end, we introduce LiV-GS, a SLAM framework that uses 3D Gaussian spatial representations to seamlessly integrate LiDAR and camera images.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method estimates robot pose by aligning Gaussian covariance from rendering with the current observations, with the back-end correcting drift and updating the Gaussian map.
- **p. 3 / III. METHODOLOGY - extractive body cue:** Our method effectively prevents these issues. by LiDAR depth in the error calculation of point clouds and Gaussian match.
- **p. 3 / III. METHODOLOGY - extractive body cue:** To further facilitate stable tracking, we introduce a weighting function for Gaussians that distinguishes Gaussians generated solely by color supervision and those also Fig.
- **p. 4 / III. METHODOLOGY - extractive body cue:** We introduce a Conditional Gaussian Constraint (CGC) to adjust the positions of color-supervised Gaussians through the loss function (10).
- **p. 4 / III. METHODOLOGY - extractive body cue:** Since the length of the Gaussian normal is difficult to restrict during the optimization, we introduced the normal length normalization for both point clouds and ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** The Gaussian map incorporating keyframe parameters is then processed in the back-end for pose optimization and map updates.
- **p. 3 / III. METHODOLOGY - extractive body cue:** The multi-modal measurements from LiDAR and visual sensors are integrated in Data Preporessing and then fed into the front-end Tracking module.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In the proposed system, data inputs consist of imagery from a camera and point clouds from a LiDAR sensor. | camera/depth stream, pose, map와 language goal | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| State/latent | system, data, inputs, consist, imagery, camera, point, clouds, LiDAR, sensor, integrated, calibrated | robot pose, free-space/semantic map와 local goal | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Output/action | These inputs are integrated using calibrated extrinsic to transform the time-aligned LiDAR point clouds into depth images. | collision-free trajectory 또는 velocity command | p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Objective/outcome | By minimizing the loss function, the Gaussian map updates the parameters of Gaussians continuously together with splitting and pruning operations of Gaussians. | goal reach, safety, localization error와 replanning latency | p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** To the end, we introduce LiV-GS, a SLAM framework that uses 3D Gaussian spatial representations to seamlessly integrate LiDAR and camera images.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method estimates robot pose by aligning Gaussian covariance from rendering with the current observations, with the back-end correcting drift and updating the Gaussian map.
- **p. 3 / III. METHODOLOGY - extractive body cue:** Our method effectively prevents these issues. by LiDAR depth in the error calculation of point clouds and Gaussian match.
- **p. 3 / III. METHODOLOGY - extractive body cue:** To further facilitate stable tracking, we introduce a weighting function for Gaussians that distinguishes Gaussians generated solely by color supervision and those also Fig.
- **p. 4 / III. METHODOLOGY - extractive body cue:** We introduce a Conditional Gaussian Constraint (CGC) to adjust the positions of color-supervised Gaussians through the loss function (10).
- **p. 7 / IV. EXPERIMENT - extractive body cue:** 8 highlights that even with cross-modal radar data, accurate localization is consistently achieved using Gaussian maps.
- **p. 7 / IV. EXPERIMENT - extractive body cue:** The ATE RMSE is directly used to measure localization accuracy and the image quality of each algorithm is calculated by normalizing the composite score: Image ...
- **p. 5 / IV. EXPERIMENT - extractive body cue:** In the experiments, we evaluate LiV-GS and compare it against other SOTA algorithms from three aspects: localization accuracy, rendering quality, and the reliability of spatial ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |
| Embodiment/environment | MonoGS, SplaTAM, GS-ICP-SLAM, and GaussianSLAM are all tailored for indoor environments with welltextured images and dense depth information, and they suffer performance degradation or even fail in some outdoor sequences due to ... | hardware/simulator version and reset protocol | p. 6 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT) |
| Dataset/benchmark | Due to the challenge of maintaining photometric consistency in long-distance outdoor scenes, we segmented the low-speed, kilometers-long scenarios as several shorter sequences. | role, split, size and leakage | p. 6 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |
| Metric | The ATE RMSE is directly used to measure localization accuracy and the image quality of each algorithm is calculated by normalizing the composite score: Image Quality = SSIM + PSNR/30 + (1 ... | definition, denominator, direction and uncertainty | p. 7 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |
| Baseline/ablation | For rendering evaluation, the optimized viewpoints from each algorithm were extracted and compared against the actual images using metrics of SSIM, PSNR[dB], and LPIPS. | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |

## Explicit Limitations and Failure Boundary

- **p. 7 / IV. EXPERIMENT - extractive body cue:** In this looped sequence, our LiV-GS still performs well but its performance falls behind some other algorithms occasionally.
- **p. 6 / IV. EXPERIMENT - extractive body cue:** MonoGS, SplaTAM, GS-ICP-SLAM, and GaussianSLAM are all tailored for indoor environments with welltextured images and dense depth information, and they suffer performance degradation or even ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 8: Visualization of cross-modal mmWave radar lo- calization trajectory. mmWave radar localization on the Gaussian map. Unlike LiDAR, the point clouds of mm-Wave radar ...
- **p. 6 / IV. EXPERIMENT - extractive body cue:** Our method does not use the IMU data.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Outdoor SLAM and scene reconstruction face unique challenges, such as lighting variations and unbounded depth scales, which make indoor RGBD-based solutions inadequate [4]-[8].를 문제로 두고, To the end, we introduce LiV-GS, a SLAM framework that uses 3D Gaussian spatial representations to seamlessly integrate LiDAR and camera images.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
