# V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Huang_V2X-R_Cooperative_LiDAR-4D_Radar_Fusion_with_Denoising_Diffusion_for_3D_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_V2X-R_Cooperative_LiDAR-4D_Radar_Fusion_with_Denoising_Diffusion_for_3D_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: sensor fusion, LiDAR, Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Huang_V2X-R_Cooperative_LiDAR-4D_Radar_Fusion_with_Denoising_Diffusion_for_3D_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_V2X-R_Cooperative_LiDAR-4D_Radar_Fusion_with_Denoising_Diffusion_for_3D_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, there is a lack of 4D radar data in the current cooperative perception dataset.를 문제로 두고, Our contributions can be summarized in three key points: • We present V2X-R, the first simulated V2X dataset that not only includes LiDAR, cameras, but also 4D radar data.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Current Vehicle-to-Everything (V2X) systems have significantly enhanced 3D object detection using LiDAR and camera data.
- **p. 1 / Abstract - extractive body cue:** However, they face performance degradation in adverse weather.
- **p. 1 / Abstract - extractive body cue:** Weather-robust 4D radar, with Doppler velocity and additional geometric information, offers a promising solution to this challenge.
- **p. 1 / Abstract - extractive body cue:** To this end, we present V2X-R, the first simulated V2X dataset incorporating LiDAR, camera, and 4D radar modalities.
- **p. 1 / Abstract - extractive body cue:** V2XR contains 12,079 scenarios with 37,727 frames of LiDAR and 4D radar point clouds, 150,908 images, and 170,859 annotated 3D vehicle bounding boxes.
- **p. 2 / 1. Introduction - extractive body cue:** However, there is a lack of 4D radar data in the current cooperative perception dataset.
- **p. 2 / 1. Introduction - extractive body cue:** MDD transforms the noise feature distribution into the easy-to-fit Gaussian distribution by reparameterization, which solves the challenge of complex and variable weather noise features that ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions can be summarized in three key points: • We present V2X-R, the first simulated V2X dataset that not only includes LiDAR, cameras, but ...
- **p. 2 / 1. Introduction - extractive body cue:** To address the challenge of agent-fused LiDAR features becoming noisy in adverse weather, we propose a novel Multi-modal Diffusion Denoising (MDD) module in the modal ...
- **p. 1 / Abstract - extractive body cue:** Subsequently, we propose a novel cooperative LiDAR-4D radar fusion pipeline for 3D object detection and implement it with multiple fusion strategies.
- **p. 1 / Abstract - extractive body cue:** To this end, we present V2X-R, the first simulated V2X dataset incorporating LiDAR, camera, and 4D radar modalities.
- **p. 4 / 3.4. Adverse Weather Simulation - extractive body cue:** Subsequent fusion consists of four stages: 1) Encode by each agent.
- **p. 5 / 3) Modal fusion. The weather-induced noisy LiDAR fea - extractive body cue:** Specifically, we first extract multi-agent features from LiDAR and 4D radar point clouds individually and then concatenate BEV features in multi-modal fusion (3rd stage).
- **p. 5 / 4.3. Multi-modal Denoising Diffusion (MDD) - extractive body cue:** Specifically, drawing inspiration from DDPM [11] and Algorithm 1 Multi-modal Denoising Diffusion process Input: Training ∈{True, False}; Noisy LiDAR BEV feature FL A; Noise-masked LiDAR ...
- **p. 4 / 3) Modal fusion. The weather-induced noisy LiDAR fea - extractive body cue:** ture FL A will first be denoised to clear LiDAR feature ˜ FL A by MDD module (will be described in the next section).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Specifically, drawing inspiration from DDPM [11] and Algorithm 1 Multi-modal Denoising Diffusion process Input: Training ∈{True, False}; Noisy LiDAR BEV feature FL A; Noise-masked LiDAR BEV feature FL l ; 4D radar ... | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (4.3. Multi-modal Denoising Diffusion (MDD)), p. 4 (4.2. Fusion Pipeline) |
| State/latent | Specifically, drawing, inspiration, DDPM, Algorithm, Multi-modal, Denoising, Diffusion, process, Input, Training, True | geometry, map, object/relationship state | p. 5 (4.3. Multi-modal Denoising Diffusion (MDD)), p. 4 (4.2. Fusion Pipeline), p. 1 (1. Introduction) |
| Output/action | Each agent collects LiDAR and 4D radar point cloud data, forming the multi-agent multi-modal input X = {XL C, XL E, XL I , XR C , XR E, XR I }. | point map, pose, scene graph, affordance 또는 query result | p. 4 (4.2. Fusion Pipeline), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | We trained models with our MDD by the following losses: \l a bel {eq_ a ll} \mat h cal {L}_{all} = \beta _{cls}\mathcal {L}_{cls}+\beta _{loc} \mathcal {L}_{loc}+ \mathcal {L}_{MDD}, (10) where βcls, ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (4.4. Loss Function), p. 5 (A Finit ←FL), p. 5 (A Finit ←FL) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions can be summarized in three key points: • We present V2X-R, the first simulated V2X dataset that not only includes LiDAR, cameras, but ...
- **p. 2 / 1. Introduction - extractive body cue:** To address the challenge of agent-fused LiDAR features becoming noisy in adverse weather, we propose a novel Multi-modal Diffusion Denoising (MDD) module in the modal ...
- **p. 1 / Abstract - extractive body cue:** Subsequently, we propose a novel cooperative LiDAR-4D radar fusion pipeline for 3D object detection and implement it with multiple fusion strategies.
- **p. 1 / Abstract - extractive body cue:** To this end, we present V2X-R, the first simulated V2X dataset incorporating LiDAR, camera, and 4D radar modalities.
- **p. 4 / 3.4. Adverse Weather Simulation - extractive body cue:** Subsequent fusion consists of four stages: 1) Encode by each agent.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 7. Effect of each component in MDD module, tested by AttFuse [55] on V2X-R testing with fog-simulation. SM2MM fusion strategies, to evaluate the performance ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. The performance of different methods in our V2X-R dataset. (a) Performance comparison of different modalities (L and 4DR represent LiDAR and 4D radar ...
- **p. 8 / 5.4. Multi-modal Diffusion Denoising Analysis - extractive body cue:** Although MDD inevitably introduces an additional inference time of 32 ms, it significantly improves weather robustness and still maintains real-time (about 20 FPS).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 2 (Figure/Table caption) |
| Embodiment/environment | Performance comparison under different real-world weather on K-Radar dataset. | hardware/simulator version and reset protocol | p. 8 (5.4. Multi-modal Diffusion Denoising Analysis), p. 8 (5.4. Multi-modal Diffusion Denoising Analysis) |
| Dataset/benchmark | Experimental 3D object detection results of various cooperative LiDAR-based methods on the validation and testing of our V2X-R dataset in different IoU (0.3,0.5,0.7). | role, split, size and leakage | p. 8 (5.4. Multi-modal Diffusion Denoising Analysis), p. 8 (5.4. Multi-modal Diffusion Denoising Analysis), p. 6 (5.2. Benchmark Models), p. 3 (3.4. Adverse Weather Simulation) |
| Metric | Table 7. Effect of each component in MDD module, tested by AttFuse [55] on V2X-R testing with fog-simulation. SM2MM fusion strategies, to evaluate the performance un- der different weather conditions. As shown ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 8 (5.4. Multi-modal Diffusion Denoising Analysis), p. 6 (5.2. Benchmark Models) |
| Baseline/ablation | We implement various state-of-the-art 3D object detectors on the V2X-R dataset, including different numbers of agents and different modalities. | fair input/data/compute/action matching | p. 6 (5.2. Benchmark Models), p. 7 (5.3. Benchmark Analysis), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5.3. Benchmark Analysis - extractive body cue:** This can be attributed to the significantly lower resolution of 4D radar than LiDAR, which is a limitation hindering the independent use of 4D radar ...
- **p. 7 / 5.3. Benchmark Analysis - extractive body cue:** The 3D mAP performance comparison under different weather conditions on the V2X-R dataset. 'L' and '4DR' represent LiDAR and 4D radar, respectively. '-' indicates that ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The advantages of the dense 4D radar point cloud in multi-agent view. Including weather robustness, fewer spatial er- rors, Doppler information, and geometric ...
- **p. 8 / 6. Conclusion and Discussion - extractive body cue:** Moreover, we propose the MDD module to tackle dense noise in collaborative conditions.
- **p. 8 / 6. Conclusion and Discussion - extractive body cue:** A compelling research direction is the full utilization of multi-agent and multi-modal information for robust 3D object detection.
- **p. 4 / 3.4. Adverse Weather Simulation - extractive body cue:** The input noisy LiDAR features are first subjected to a diffusion process, followed by T step denoising process with weather-robust 4D radar features as conditions ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. The performance of different methods in our V2X-R dataset. (a) Performance comparison of different modalities (L and 4DR represent LiDAR and 4D radar ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, there is a lack of 4D radar data in the current cooperative perception dataset.를 문제로 두고, Our contributions can be summarized in three key points: • We present V2X-R, the first simulated V2X dataset that not only includes LiDAR, cameras, but also 4D radar data.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3) Modal fusion. The weather-induced noisy LiDAR fea) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
