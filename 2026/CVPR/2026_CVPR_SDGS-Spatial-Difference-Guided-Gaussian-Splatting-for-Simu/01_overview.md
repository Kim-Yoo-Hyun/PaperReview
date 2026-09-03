# SDGS: Spatial Difference Guided Gaussian Splatting for Simultaneous Localization and 3D Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Tian_SDGS_Spatial_Difference_Guided_Gaussian_Splatting_for_Simultaneous_Localization_and_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This is fundamentally due to the inherent limitations of traditional imaging mechanisms of vision sensors and their dense descriptors.를 문제로 두고, Our main contributions are summarized as follows: • We introduce a sparse edge descriptor using Gaussian ellipsoids as 3D representation, providing clear geometric cues while remaining computationally efficient. • We develop an ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian Splatting (3DGS) pioneers explicit scene representation, enabling photorealistic, real-time 3D reconstruction.
- **p. 1 / Abstract - extractive body cue:** Conventional pipelines require precomputed camera poses for Gaussian parameter optimization, which introduces latency between perception and reconstruction.
- **p. 1 / Abstract - extractive body cue:** Recent works have adapted 3DGS to online settings without pose priors.
- **p. 1 / Abstract - extractive body cue:** However, these approaches often suffer from high computational costs and are vulnerable to lowquality image inputs.
- **p. 1 / Abstract - extractive body cue:** We propose a sparse, edge-guided reconstruction strategy that simultaneously estimates 6-DoF camera poses by aligning rendered 3D edges with input 2D edges, achieving about 2× ...
- **p. 1 / 1. Introduction - extractive body cue:** This is fundamentally due to the inherent limitations of traditional imaging mechanisms of vision sensors and their dense descriptors.
- **p. 1 / 1. Introduction - extractive body cue:** This makes it challenging for the system to achieve both efficiency and robustness in real world, making it difficult to balance reconstruction accuracy and speed.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We introduce a sparse edge descriptor using Gaussian ellipsoids as 3D representation, providing clear geometric cues while ...
- **p. 2 / 1. Introduction - extractive body cue:** Moreover, our method substantially reduces the resource overhead required for representing key geometries relative to fully dense approaches.
- **p. 5 / 3.2.2. Tracking - extractive body cue:** A Gaussian is marked as visible in the current view if its center falls within the observed depth range and has a non-negligible opacity contribution.
- **p. 5 / 3.3.1. SD Keyframe - extractive body cue:** With a regular opacity reset strategy, Gaussians that have never been marked as active will receive no supervision after reset and are pruned from the ...
- **p. 4 / 3.1.2. Edge-aligned 3D Gaussian Representation - extractive body cue:** SDGS overview: our approach uses high-frame-rate SD inputs to optimize a sparse Gaussian map and performs camera pose estimation via edge alignment.
- **p. 5 / 3.3.2. SD Loss - extractive body cue:** For SD photometric mapping, we use the loss defined as follows: \ m at hcal {L} _ { \te xt {sd}}=\bigl \/\, I(\mathcal {G}_A,T_{CW})-I_{\text {SD}} ...
- **p. 5 / 3.2.2. Tracking - extractive body cue:** At each level, the SD observation is downsampled and its distance transform is computed once; we then directly render I(\mat hca l {G}_{\mathrm {SD}}, T_{CW} ...
- **p. 4 / 3.1.2. Edge-aligned 3D Gaussian Representation - extractive body cue:** With the estimated poses, we then promote keyframes for dense RGB reconstruction using SD-guided initialization and optimization.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We estimate camera poses by aligning the rendered sparse edge map with the input edge image using a distance transform. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 4 (3.1.2. Edge-aligned 3D Gaussian Representation) |
| State/latent | estimate, camera, poses, aligning, rendered, sparse, edge, input, image, distance, transform, SDGS | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 4 (3.1.2. Edge-aligned 3D Gaussian Representation), p. 2 (1. Introduction) |
| Output/action | SDGS overview: our approach uses high-frame-rate SD inputs to optimize a sparse Gaussian map and performs camera pose estimation via edge alignment. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.1.2. Edge-aligned 3D Gaussian Representation), p. 2 (1. Introduction), p. 5 (3.2.2. Tracking) |
| Objective/outcome | We minimize \mathca l { L}_{\t ext { trackin g} } = \big \/\, I(\mathcal {G}_{\mathrm {SD}}, T_{CW}) \odot DT(I_{\text {SD}}) \,\big \/_{1}, \label {eq:track-loss} (7) so that each rendered positive response ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.2.2. Tracking), p. 6 (3.4.2. SD-guided Mutually Exclusive RGB Supervision), p. 3 (3.1.1. Sparse Edge Descriptor) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We introduce a sparse edge descriptor using Gaussian ellipsoids as 3D representation, providing clear geometric cues while ...
- **p. 2 / 1. Introduction - extractive body cue:** Moreover, our method substantially reduces the resource overhead required for representing key geometries relative to fully dense approaches.
- **p. 5 / 3.2.2. Tracking - extractive body cue:** A Gaussian is marked as visible in the current view if its center falls within the observed depth range and has a non-negligible opacity contribution.
- **p. 5 / 3.3.1. SD Keyframe - extractive body cue:** With a regular opacity reset strategy, Gaussians that have never been marked as active will receive no supervision after reset and are pruned from the ...
- **p. 4 / 3.1.2. Edge-aligned 3D Gaussian Representation - extractive body cue:** SDGS overview: our approach uses high-frame-rate SD inputs to optimize a sparse Gaussian map and performs camera pose estimation via edge alignment.
- **p. 7 / 4.2.1. Tracking Accuracy - extractive body cue:** 2, across three complex scenarios, while our method exhibits marginally lower overall tracking accuracy compared to the baseline approaches, it achieves a substantial improvement in ...
- **p. 8 / 4.3. Ablation Study - extractive body cue:** We can see that a pyramid strategy can significantly improve system's tracking accuracy under long sequences like fr3/office.
- **p. 7 / 4.2.1. Tracking Accuracy - extractive body cue:** 1, under low-speed motion, our method achieves tracking accuracy comparable to the baselines.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 7 (4.2.1. Tracking Accuracy), p. 8 (4.3. Ablation Study) |
| Embodiment/environment | To analyze our method under controllable settings, we construct a SD-Replica dataset by simulating the hybrid pixel camera's sampling process on the Replica [15] scenes. | hardware/simulator version and reset protocol | p. 6 (4.1.2. Datasets), p. 6 (4.1.3. Evaluation Metrics) |
| Dataset/benchmark | And a semi-isotropic loss can help tracking accuracy for scenes with sharp edges like fr1/desk and fr2/xyz, however it slightly reduces tracking accuracy in fr3/office where spatially smooth spherical objects frequently appear, ... | role, split, size and leakage | p. 6 (4.1.2. Datasets), p. 6 (4.1.3. Evaluation Metrics), p. 8 (4.3. Ablation Study), p. 7 (4.2.2. Deblurring Metrics) |
| Metric | For tracking accuracy, we adopt the Root Mean Square Error (RMSE) of Absolute Trajectory Error (ATE), following standard camera 6-DoF pose estimation benchmarks. | definition, denominator, direction and uncertainty | p. 6 (4.1.3. Evaluation Metrics), p. 7 (4.2.1. Tracking Accuracy), p. 7 (4.2.1. Tracking Accuracy) |
| Baseline/ablation | 3, on SD-Replica room0, we consistently outperform the baseline MonoGS-RGBD in terms of PSNR, SSIM, and LPIPS. | fair input/data/compute/action matching | p. 7 (4.2.2. Deblurring Metrics), p. 7 (4.2.1. Tracking Accuracy), p. 8 (4.2.3. Performance Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** By combining emerging hybrid pixel cameras, we not only maintain robust tracking accuracy under extreme motions where other methods fail, but also reconstruct dense maps ...
- **p. 8 / 5. Conclusion - extractive body cue:** Our system balances tracking robustness, high-fidelity reconstruction, and system efficiency.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Our approach follows a "sketch-then-paint" paradigm. Similar to drawing the outline before adding colors, we first generate a discrete outline (skeleton) for efficient ...
- **p. 6 / 4.1.2. Datasets - extractive body cue:** We evaluate our method on three datasets to verify both the robustness and generalization ability: SD-Replica Datasets.
- **p. 7 / 4.2.1. Tracking Accuracy - extractive body cue:** We first evaluate our method against state-of-the-art approaches in terms of tracking 6-DoF pose accuracy and robustness under various motion conditions, based on the stereo ...
- **p. 7 / 4.2.2. Deblurring Metrics - extractive body cue:** Method Input tianmouc/slow tianmouc/fast tianmouc/extreme Average Gaussian-SLAM RGB 4.60 fail fail - SplaTAM 6.52 fail fail - MonoGS-RGBD 3.32 24.52 fail - WildGS-SLAM∗† 2.01 8.21 ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This is fundamentally due to the inherent limitations of traditional imaging mechanisms of vision sensors and their dense descriptors.를 문제로 두고, Our main contributions are summarized as follows: • We introduce a sparse edge descriptor using Gaussian ellipsoids as 3D representation, providing clear geometric cues while remaining computationally efficient. • We develop an ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3.2. SD Loss), p. 5 (3.2.2. Tracking) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
