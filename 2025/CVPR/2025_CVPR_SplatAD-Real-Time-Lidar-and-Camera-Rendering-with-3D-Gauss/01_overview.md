# SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: Georg Hess, Carl Lindström, Maryam Fatemi, Christoffer Petersson, Lennart Svensson
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Gaussian Splatting, sensor fusion, LiDAR, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

SplatAD는 실제 주행 기록으로 만든 동적 3차원 장면에서 카메라 관측과 LiDAR 관측을 함께 렌더링한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Ensuring the safety of autonomous robots, such as selfdriving vehicles, requires extensive testing across diverse driving scenarios.
- **p. 1 / Abstract - extractive body cue:** Simulation is a key ingredient for conducting such testing in a cost-effective and scalable way.
- **p. 1 / Abstract - extractive body cue:** Neural rendering methods have gained popularity, as they can build simulation environments from collected logs in a data-driven manner.
- **p. 1 / Abstract - extractive body cue:** However, existing neural radiance field (NeRF) methods for sensor-realistic rendering of camera and lidar data suffer from low rendering speeds, limiting their applicability for large-scale ...
- **p. 1 / Abstract - extractive body cue:** While 3D Gaussian Splatting (3DGS) enables real-time rendering, current methods are limited to camera data and are unable to render lidar data essential for autonomous ...
- **p. 1 / 1. Introduction - extractive body cue:** Nevertheless, 3DGS-based methods for the AD setting [7, 43, 51] inherit the limitation of only being able to render camera data, overlooking the lidar modality.
- **p. 2 / 1. Introduction - extractive body cue:** Applying 3DGS to lidar sensors presents unique challenges due to their distinct characteristics.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are as follows: • We propose the first method for efficient lidar rendering using 3D Gaussians, introducing custom CUDA-accelerated algorithms for ...
- **p. 2 / 1. Introduction - extractive body cue:** To overcome these challenges, we introduce SplatAD, a novel view synthesis method that unifies camera and lidar rendering and is designed for real-time rendering of ...
- **p. 3 / 3. Method - extractive body cue:** Our method projects 3D Gaussians with associated feature vectors onto the corresponding sensor modalities (camera and lidar) and employs sensor-specific tiling to match their distinct ...
- **p. 3 / 3.2. Camera rendering - extractive body cue:** While we retain 3DGS's high-level steps-projection and view frustum culling, tile-assignment, depth sorting, and tilebased rasterization-we introduce key adaptations to better model the unique characteristics ...
- **p. 5 / 3.3. Lidar rendering - extractive body cue:** done in our method by modifying the projection accordingly.
- **p. 5 / 3.3. Lidar rendering - extractive body cue:** While we use the expected range for training, the median range is used during inference as it, in contrast to the expected range, does not ...
- **p. 3 / 3.1. Scene representation - extractive body cue:** Last, our representation contains a learnable embedding per sensor to model their specific appearance characteristics.
- **p. 4 / 3.3. Lidar rendering - extractive body cue:** However, we note that modeling other types of lidars, such as solid-state lidars [21], can be easily 11985

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To summarize, our contributions are as follows: • We propose the first method for efficient lidar rendering using 3D Gaussians, introducing custom CUDA-accelerated algorithms for rasterizing sparse point clouds in spherical coordinates. ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 3 (3. Method) |
| State/latent | summarize, contributions, follows, first, efficient, lidar, rendering, Gaussians, introducing, custom, CUDA-accelerated, algorithms | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 3 (3. Method), p. 6 (3.4. Optimization and implementation) |
| Output/action | Our proposed lidar rendering matches the image rendering on a high level, but modifies each component to accurately model sensor characteristics. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3. Method), p. 6 (3.4. Optimization and implementation), p. 4 (3.3. Lidar rendering) |
| Objective/outcome | LBCE is a binary cross-entropy loss on the predicted ray drop probability, where ground-truth is generated in the same way as for NeuRAD. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.4. Optimization and implementation), p. 5 (3.4. Optimization and implementation), p. 3 (3. Method) |

## Main Claims and Actual Contribution

- 카메라의 롤링 셔터와 LiDAR의 반사 강도·누락 광선을 센서별 렌더링 과정에 반영했다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.pdf#page=5)
- 주행 데이터에서 새로운 시점과 재구성된 시점의 RGB·LiDAR 품질 및 렌더링 속도를 구분해 평가했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 7 (4.1. Image rendering) |
| Embodiment/environment | Datasets: We perform experiments on PandaSet [41], Argoverse2 [38] and nuScenes [5]. | hardware/simulator version and reset protocol | p. 6 (4. Experiments), p. 7 (4. Experiments) |
| Dataset/benchmark | NVS results for image, over three datasets. | role, split, size and leakage | p. 6 (4. Experiments), p. 7 (4. Experiments), p. 6 (4. Experiments), p. 7 (4. Experiments) |
| Metric | We measure the quality of our lidar point clouds using the same metrics as in [35], i.e., median squared depth error, RMSE intensity error, ray drop accuracy, and chamfer distance, see Tab. | definition, denominator, direction and uncertainty | p. 7 (4.2. Lidar rendering), p. 8 (4.2. Lidar rendering), p. 8 (4.3. Ablations) |
| Baseline/ablation | Compared to the baselines, SplatAD produces sharp images with a high level of detail. | fair input/data/compute/action matching | p. 6 (3.4. Optimization and implementation), p. 7 (4. Experiments), p. 7 (4.1. Image rendering) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Limitations and future work: SplatAD is currently limited to modeling all dynamic actors as rigid.
- **p. 8 / 5. Conclusion - extractive body cue:** Drawing inspiration from recent advances in human reconstruction [18, 20, 26] can provide inspiration how to overcome this limitation in future research.
- **p. 7 / 4.1. Image rendering - extractive body cue:** However, we note that using Inception-v3 features instead does not change the model ranking or our conclusions.
- **p. 6 / 4. Experiments - extractive body cue:** To validate the robustness of our method, we evaluate it across multiple popular AD datasets, using the same set of hyperparameters.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.3. Lidar rendering), p. 3 (3.2. Camera rendering), p. 3 (3.1. Scene representation)이다.
