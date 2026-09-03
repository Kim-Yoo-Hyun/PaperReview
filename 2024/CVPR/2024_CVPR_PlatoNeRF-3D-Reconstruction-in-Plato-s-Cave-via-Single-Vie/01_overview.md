# PlatoNeRF: 3D Reconstruction in Plato's Cave via Single-View Two-Bounce Lidar

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Klinghoffer_PlatoNeRF_3D_Reconstruction_in_Platos_Cave_via_Single-View_Two-Bounce_Lidar_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Klinghoffer_PlatoNeRF_3D_Reconstruction_in_Platos_Cave_via_Single-View_Two-Bounce_Lidar_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: NeRF, 3D reconstruction, sensor fusion, LiDAR, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Klinghoffer_PlatoNeRF_3D_Reconstruction_in_Platos_Cave_via_Single-View_Two-Bounce_Lidar_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Klinghoffer_PlatoNeRF_3D_Reconstruction_in_Platos_Cave_via_Single-View_Two-Bounce_Lidar_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 While promising, a limitation of existing methods is generalization to the lower spatial- and temporal-resolutions of lidars found on consumer devices.를 문제로 두고, Our method consists of three steps.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D reconstruction from a single-view is challenging because of the ambiguity from monocular cues and lack of information about occluded regions.
- **p. 1 / Abstract - extractive body cue:** Neural radiance fields (NeRF), while popular for view synthesis and 3D reconstruction, are typically reliant on multi-view images.
- **p. 1 / Abstract - extractive body cue:** Existing methods for single-view 3D reconstruction with NeRF rely on either data priors to hallucinate views of occluded regions, which may not be physically accurate, ...
- **p. 1 / Abstract - extractive body cue:** We propose using time-offlight data captured by a single-photon avalanche diode to overcome these limitations.
- **p. 1 / Abstract - extractive body cue:** Our method models two-bounce optical paths with NeRF, using lidar transient data for supervision.
- **p. 2 / 1. Introduction - extractive body cue:** While promising, a limitation of existing methods is generalization to the lower spatial- and temporal-resolutions of lidars found on consumer devices.
- **p. 1 / 1. Introduction - extractive body cue:** However, these methods struggle when the shadow is difficult to detect, such as in ambient light or low albedo backgrounds.

## Core Idea

- **p. 4 / 3.1. Notations and Problem Definition - extractive body cue:** Our method consists of three steps.
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, using lidar allows our method to operate with higher ambient light and lower scene albedo than RGB methods that exploit shadows.
- **p. 2 / 1. Introduction - extractive body cue:** We use this data to evaluate our method and our baselines.
- **p. 3 / 3.1. Notations and Problem Definition - extractive body cue:** The lidar system consists of a SPAD sensor and pulsed laser at known positions xs and xl respectively.
- **p. 5 / 3.3. Implementation Details - extractive body cue:** Our method requires five inputs per pixel: (1) sensor location op = xs and ray direction dp, (2) laser location xl, (3) distance from the ...
- **p. 5 / 3.3. Implementation Details - extractive body cue:** As in NeRF, we use the Adam optimizer [15] and set an initial learning rate of 5 × 10-4, which decays exponentially over training.
- **p. 5 / 3.3. Implementation Details - extractive body cue:** For the first 25,000 iterations of training, β is set to 0.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Because l is modeled as a point light source, we neglect any diffraction effects and soft shadows that are common with area sources. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.1. Notations and Problem Definition), p. 5 (3.3. Implementation Details) |
| State/latent | Because, modeled, point, light, source, neglect, diffraction, effects, soft, shadows, common, area | geometry, map, object/relationship state | p. 3 (3.1. Notations and Problem Definition), p. 5 (3.3. Implementation Details), p. 1 (1. Introduction) |
| Output/action | Our method requires five inputs per pixel: (1) sensor location op = xs and ray direction dp, (2) laser location xl, (3) distance from the laser to the virtual source ∥l -xl∥, ... | point map, pose, scene graph, affordance 또는 query result | p. 5 (3.3. Implementation Details), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | After 25,000 iterations, when an accurate initial estimate of the virtual detector xp is obtained, we set β to 1/6,000 in most experiments to encourage Lprimary to continue to improve after activating ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.3. Implementation Details), p. 5 (3.3. Implementation Details) |

## Main Claims and Actual Contribution

- **p. 4 / 3.1. Notations and Problem Definition - extractive body cue:** Our method consists of three steps.
- **p. 2 / 1. Introduction - extractive body cue:** Furthermore, using lidar allows our method to operate with higher ambient light and lower scene albedo than RGB methods that exploit shadows.
- **p. 2 / 1. Introduction - extractive body cue:** We use this data to evaluate our method and our baselines.
- **p. 3 / 3.1. Notations and Problem Definition - extractive body cue:** The lidar system consists of a SPAD sensor and pulsed laser at known positions xs and xl respectively.
- **p. 5 / 3.3. Implementation Details - extractive body cue:** Our method requires five inputs per pixel: (1) sensor location op = xs and ray direction dp, (2) laser location xl, (3) distance from the ...
- **p. 7 / 4.2. Results - extractive body cue:** PlatoNeRF method achieves competitive performance.
- **p. 7 / 4.2. Results - extractive body cue:** Due to our use of an implicit representation, we achieve much smoother results than BF Lidar.
- **p. 5 / 3.3. Implementation Details - extractive body cue:** After 25,000 iterations, when an accurate initial estimate of the virtual detector xp is obtained, we set β to 1/6,000 in most experiments to encourage ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.2. Results), p. 7 (4.2. Results) |
| Embodiment/environment | We create datasets of four scenes of a room with either a chair, bunny, dragon, or occluded bunny in a chair, shown in Fig. | hardware/simulator version and reset protocol | p. 5 (4.1. Datasets), p. 5 (4. Experiments) |
| Dataset/benchmark | The dataset captures a simple indoor scene, shown in Fig. | role, split, size and leakage | p. 5 (4.1. Datasets), p. 5 (4. Experiments), p. 6 (4.1. Datasets), p. 8 (4.3. Ablations) |
| Metric | We use L1 depth error to evaluate our method for 3D reconstruction, as done in past work [14, 19, 44]. | definition, denominator, direction and uncertainty | p. 6 (4.2. Results), p. 7 (4.3. Ablations), p. 8 (4.3. Ablations) |
| Baseline/ablation | Figure 5. Real-World Results. (a) Captured scene (stars are illumi- nation spots), (b) BF Lidar result, (c) PlatoNeRF result. Our method yields similar results as BF Lidar, with much fewer artifacts/holes. results ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 7 (4.3. Ablations), p. 5 (4. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Our method has a couple limitations.
- **p. 8 / 4.3. Ablations - extractive body cue:** In contrast, lidar-based methods, such as PlatoNeRF, are fundamentally more robust to these low signal-to-noise (SNR) and signal-to-background (SBR) scenarios.
- **p. 5 / 4. Experiments - extractive body cue:** First, we introduce the simulated datasets that we make available to accelerate future work in learning-based methods for single-photon lidars.
- **p. 7 / 4.2. Results - extractive body cue:** In general, PlatoNeRF produces smoother depth, but small floaters are noticeable, especially in the nearby floor region, which is an area for future work.
- **p. 7 / 4.2. Results - extractive body cue:** We also note that, as in the original work, we train S3-NeRF with RGB images rendered with only one bounce, as we found it does ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Depth evaluation. We compare PlatoNeRF to both lidar- and RGB-based single-view 3D reconstruction methods, BF Lidar [7] and S3-NeRF [44], respectively. Depth metrics ...
- **p. 6 / 4.1. Datasets - extractive body cue:** Chair Scene Dragon Scene Bunny Scene Occlusion Scene Train View Test Views Train View Test Views Train View Test Views Train View Test Views Approach ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 While promising, a limitation of existing methods is generalization to the lower spatial- and temporal-resolutions of lidars found on consumer devices.를 문제로 두고, Our method consists of three steps.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Notations and Problem Definition), p. 5 (3.3. Implementation Details) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
