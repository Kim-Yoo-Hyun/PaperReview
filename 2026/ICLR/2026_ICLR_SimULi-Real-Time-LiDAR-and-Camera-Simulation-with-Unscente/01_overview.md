# SimULi: Real-Time LiDAR and Camera Simulation with Unscented Transforms

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=osxP6FafPZ.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/247739. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: sensor fusion, LiDAR, 3D Vision
- Official paper: https://openreview.net/forum?id=osxP6FafPZ
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/247739
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, this comes at the cost of limitations inherent to the rasterization paradigm.를 문제로 두고, In this work, we propose a high-fidelity and efficient reconstruction pipeline that enables joint camera and LiDAR simulation for AV scenarios.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Rigorous testing of autonomous robots, such as self-driving vehicles, is essential to ensure their safety in real-world deployments.
- **p. 1 / ABSTRACT - extractive body cue:** This requires building highfidelity simulators to test scenarios beyond those that can be safely or exhaustively collected in the real-world.
- **p. 1 / ABSTRACT - extractive body cue:** Existing neural rendering methods based on NeRF and 3DGS hold promise but suffer from low rendering speeds or can only render pinhole camera models, hindering ...
- **p. 1 / ABSTRACT - extractive body cue:** Multi-sensor simulation poses additional challenges as existing methods handle cross-sensor inconsistencies by favoring the quality of one modality at the expense of others.
- **p. 1 / ABSTRACT - extractive body cue:** To overcome these limitations, we propose SimULi, the first method capable of rendering arbitrary camera models and LiDAR data in real-time.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, this comes at the cost of limitations inherent to the rasterization paradigm.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** As they are optimized to match real-world observations, they also exhibit a smaller domain gap compared to traditional artist-generated simulators.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this work, we propose a high-fidelity and efficient reconstruction pipeline that enables joint camera and LiDAR simulation for AV scenarios.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We make the following contributions: (1) we extend 3DGUT with LiDAR support and introduce an automated tiling scheme from which we derive optimal tiling parameters ...
- **p. 5 / 3 METHOD - extractive body cue:** Particle Contributions and Response.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** With the rise of end-to-end policy models, accurate sensor simulation has become a critical component in the development and evaluation of autonomous vehicle (AV) systems.
- **p. 4 / 3 METHOD - extractive body cue:** Our goal is to learn a controllable scene representation that simulates camera and LiDAR renderings from novel viewpoints in real-time (Fig.
- **p. 7 / 3 METHOD - extractive body cue:** As crosssensor data contains inconsistencies that are impossible to eliminate, this forces the representation to prioritize the reconstruction quality of one modality over the other ...
- **p. 6 / 3 METHOD - extractive body cue:** Prior work encodes camera and LiDAR into the same representation constrained with a LiDAR-supervised depth loss.
- **p. 6 / 3 METHOD - extractive body cue:** As cross-sensor data is not fully consistent, this forces the representation to prioritize camera instead of LiDAR quality (left) or the inverse (middle), as shown ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3.4 OPTIMIZATION We jointly optimize the camera particles Gc, LiDAR particles Gl, bilateral grids A, and the environment map by sampling a random input image and LiDAR scan at each training step. | RGB-D, image set, point cloud, depth와 camera pose | p. 6 (3 METHOD), p. 2 (1 INTRODUCTION) |
| State/latent | OPTIMIZATION, jointly, optimize, camera, particles, LiDAR, bilateral, grids, environment, sampling, random, input | geometry, map, object/relationship state | p. 6 (3 METHOD), p. 2 (1 INTRODUCTION), p. 6 (3 METHOD) |
| Output/action | With the rise of end-to-end policy models, accurate sensor simulation has become a critical component in the development and evaluation of autonomous vehicle (AV) systems. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1 INTRODUCTION), p. 6 (3 METHOD), p. 7 (3 METHOD) |
| Objective/outcome | We minimize a reconstruction loss, an anchoring loss that encourages camera Gaussians in Gc to lie near the LiDAR-supervised scene geometry distilled into Gl, and lower-level regularization terms such that the final ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this work, we propose a high-fidelity and efficient reconstruction pipeline that enables joint camera and LiDAR simulation for AV scenarios.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We make the following contributions: (1) we extend 3DGUT with LiDAR support and introduce an automated tiling scheme from which we derive optimal tiling parameters ...
- **p. 5 / 3 METHOD - extractive body cue:** Particle Contributions and Response.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** With the rise of end-to-end policy models, accurate sensor simulation has become a critical component in the development and evaluation of autonomous vehicle (AV) systems.
- **p. 4 / 3 METHOD - extractive body cue:** Our goal is to learn a controllable scene representation that simulates camera and LiDAR renderings from novel viewpoints in real-time (Fig.
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** Not only does anchoring improve NVS compared to camera-only reconstruction (⇀d = 0), but it outperforms the unified strategy across all metrics for all values ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** It outperforms LiDAR-RT (Zhou et al., 2025), which solely targets LiDAR reconstruction, on all metrics except ray drop accuracy (for which LiDAR-RT uses a U-Net ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Visually, SimULi outperforms all methods by >2dB PSNR, and is best or nearly-best across all other metrics.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Embodiment/environment | We perform experiments on all four scenes of the Waymo Interp. benchmark (Huang et al., 2023) and follow the suggested protocol of holding out every 5th frame for validation. | hardware/simulator version and reset protocol | p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS) |
| Dataset/benchmark | RMSE↑ RayDrop→ CD ↑ MP/s→ MR/s→ OmniRe (Chen et al., 2025) 25.13 0.757 0.351 0.425 0.113 - - 1.126 53.19 - StreetGS (Yan et al., 2024) 25.09 0.756 0.352 0.378 0.102 - ... | role, split, size and leakage | p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Metric | We list the median absolute depth error, mean relative depth accuracy, and chamfer distance of LiDAR predictions in meters, and intensity and ray drop accuracy for methods that support it. | definition, denominator, direction and uncertainty | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 6 (Figure/Table caption) |
| Baseline/ablation | Table 5. Not only does anchoring improve NVS compared to camera-only reconstruction (⇀d = 0), but it outperforms the unified strategy across all metrics for all values of ⇀d, and renders LiDAR ... | fair input/data/compute/action matching | p. 10 (Figure/Table caption), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Static NVS. Projecting LiDAR as a sparse depth map causes inaccuracies that degrade 3DGUT's rendering of the pole (above), which we avoid by ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6: Dynamic Scenes. FPS numbers are averaged across Waymo Dynamic and PandaSet. Approaches that use CNNs for upsampling (Yang et al., 2023b; Tonderski et ...
- **p. 10 / 4 EXPERIMENTS - extractive body cue:** The choice M = 32, Nε = 16 gives the best LiDAR rendering speed (note that does not affect quality).

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, this comes at the cost of limitations inherent to the rasterization paradigm.를 문제로 두고, In this work, we propose a high-fidelity and efficient reconstruction pipeline that enables joint camera and LiDAR simulation for AV scenarios.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 7 (3 METHOD), p. 6 (3 METHOD), p. 6 (3 METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
