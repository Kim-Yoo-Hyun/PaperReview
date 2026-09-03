# GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Yan_GS-SLAM_Dense_Visual_SLAM_with_3D_Gaussian_Splatting_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Yan_GS-SLAM_Dense_Visual_SLAM_with_3D_Gaussian_Splatting_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: SLAM, Gaussian Splatting, geometry
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Yan_GS-SLAM_Dense_Visual_SLAM_with_3D_Gaussian_Splatting_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Yan_GS-SLAM_Dense_Visual_SLAM_with_3D_Gaussian_Splatting_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, these methods face serious challenges in obtaining fine-grained dense maps.를 문제로 두고, Overall, our contributions include: • We propose GS-SLAM, the first 3D Gaussian Splatting(3DGS)-based dense RGB-D SLAM approach, which takes advantage of the fast splatting rendering technique to boost the mapping optimizing and ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce GS-SLAM that first utilizes 3D Gaussian representation in the Simultaneous Localization and Mapping (SLAM) system.
- **p. 1 / Abstract - extractive body cue:** It facilitates a better balance between efficiency and accuracy.
- **p. 1 / Abstract - extractive body cue:** Compared to recent SLAM methods employing neural implicit representations, our method utilizes a real-time differentiable splatting rendering pipeline that offers significant speedup to map optimization ...
- **p. 1 / Abstract - extractive body cue:** Specifically, we propose an adaptive expansion strategy that adds new or deletes noisy 3D Gaussians in order to efficiently reconstruct new observed scene geometry and ...
- **p. 1 / Abstract - extractive body cue:** This strategy is essential to extend 3D Gaussian representation to reconstruct the whole scene rather than synthesize a static object in existing methods.
- **p. 1 / 1. Introduction - extractive body cue:** However, these methods face serious challenges in obtaining fine-grained dense maps.
- **p. 1 / 1. Introduction - extractive body cue:** In practical mapping and tracking steps, these methods only render a small set of pixels to reduce optimization time, which leads to the reconstructed dense ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Overall, our contributions include: • We propose GS-SLAM, the first 3D Gaussian Splatting(3DGS)-based dense RGB-D SLAM approach, which takes advantage of the fast splatting rendering ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose GS-SLAM, the first RGB-D dense SLAM system that first utilizes 3D Gaussian scene representation coupled with the splatting rendering technique ...
- **p. 3 / 3.1. 3D Gaussian Scene Representation - extractive body cue:** Our goal is to optimize a scene representation that captures the geometry and appearance of the scene, resulting in a detailed dense map and high-quality ...
- **p. 4 / 3.2. Adaptive 3D Gaussian Expanding Mapping - extractive body cue:** apply the proposed adaptive expansion strategy to add new or delete noisy 3D Gaussians from the whole scene representations to render RGB-D images with resolution ...
- **p. 5 / 3.3. Tracking and Bundle Adjustment - extractive body cue:** Further, we use this coarse camera pose and depth observation to select reliable 3D Gaussians, which guides GS-SLAM to render informative areas with clear geometric ...
- **p. 4 / 3.2. Adaptive 3D Gaussian Expanding Mapping - extractive body cue:** The 3D Gaussians are initialized and then optimized using the first RGB-D image with rendering loss.
- **p. 5 / 3.3. Tracking and Bundle Adjustment - extractive body cue:** For pose optimization stability, we only optimize the scene representation S in the first half of the iterations.
- **p. 3 / 3. Methodology - extractive body cue:** 3.1, we first introduce 3D Gaussian as the scene representation S and the RGBD render by differentiable splatting rasterization.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | apply the proposed adaptive expansion strategy to add new or delete noisy 3D Gaussians from the whole scene representations to render RGB-D images with resolution H ⇥W, and then the updated 3D ... | camera/depth stream, pose, map와 language goal | p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 3 (3. Methodology) |
| State/latent | apply, adaptive, expansion, strategy, delete, noisy, Gaussians, whole, scene, representations, render, RGB-D | robot pose, free-space/semantic map와 local goal | p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 3 (3. Methodology), p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping) |
| Output/action | We aim to estimate the camera poses {Pi}N i=1 of every frame and simultaneously reconstruct a dense scene map by giving an input sequential RGB-D stream {Ii, Di}M i=1 with known camera ... | collision-free trajectory 또는 velocity command | p. 3 (3. Methodology), p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 5 (3.3. Tracking and Bundle Adjustment) |
| Objective/outcome | apply the proposed adaptive expansion strategy to add new or delete noisy 3D Gaussians from the whole scene representations to render RGB-D images with resolution H ⇥W, and then the updated 3D ... | goal reach, safety, localization error와 replanning latency | p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 4 (3.3. Tracking and Bundle Adjustment), p. 3 (3. Methodology) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Overall, our contributions include: • We propose GS-SLAM, the first 3D Gaussian Splatting(3DGS)-based dense RGB-D SLAM approach, which takes advantage of the fast splatting rendering ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose GS-SLAM, the first RGB-D dense SLAM system that first utilizes 3D Gaussian scene representation coupled with the splatting rendering technique ...
- **p. 3 / 3.1. 3D Gaussian Scene Representation - extractive body cue:** Our goal is to optimize a scene representation that captures the geometry and appearance of the scene, resulting in a detailed dense map and high-quality ...
- **p. 6 / 4.2. Evaluation of Localization and Mapping - extractive body cue:** Our method achieves the best or second performance in 7 of 8 scenes and outperforms the second-best method Point-SLAM [27] by 0.4 cm on average ...
- **p. 7 / 4.5. Ablation Study - extractive body cue:** The results illustrate that the expansion strategy can significantly improve the tracking and mapping perTable 4.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 6. Rendering performance on Replica dataset. We outperform existing dense neural RGB-D methods on the commonly reported rendering metrics. Note that GS-SLAM achieves 386 ...
- **p. 6 / 4.3. Rendering Evaluation - extractive body cue:** The results show that GS-SLAM achieves the best performance Table 3.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The illustration of the proposed GS-SLAM. It first uti- lizes the 3D Gaussian representation and differentiable splatting rasterization pipeline in SLAM, achieving real-time ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.2. Evaluation of Localization and Mapping), p. 7 (4.5. Ablation Study) |
| Embodiment/environment | Following [11, 27, 41, 48, 55], we use 8 scenes from the Replica dataset for localization, mesh reconstruction, and rendering quality comparison. | hardware/simulator version and reset protocol | p. 5 (4.1. Experimental Setup), p. 6 (4.3. Rendering Evaluation) |
| Dataset/benchmark | The selected three subsets of TUM-RGBD datasets are used for localization. | role, split, size and leakage | p. 5 (4.1. Experimental Setup), p. 6 (4.3. Rendering Evaluation), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Evaluation of Localization and Mapping) |
| Metric | For localization, we use the absolute trajectory (ATE, cm) error [33] to measure the accuracy of the estimated camera poses. | definition, denominator, direction and uncertainty | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Evaluation of Localization and Mapping) |
| Baseline/ablation | 3 report the mapping evaluation results of our method with other current state-of-the-art visual SLAM methods. | fair input/data/compute/action matching | p. 6 (4.2. Evaluation of Localization and Mapping), p. 6 (4.2. Evaluation of Localization and Mapping), p. 7 (4.4. Runtime Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion and Limitations - extractive body cue:** We believe GS-SLAM has the potential to extend to larger scale with some improvements and will explore this in future work.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the proposed method. We aim to use 3D Gaussians to represent the scene and use the rendered RGB-D image for inverse ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We further evaluate the rendering performance using the peak signal-to-noise ratio (PSNR), SSIM [43], and LPIPS [52] by following [27].

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, these methods face serious challenges in obtaining fine-grained dense maps.를 문제로 두고, Overall, our contributions include: • We propose GS-SLAM, the first 3D Gaussian Splatting(3DGS)-based dense RGB-D SLAM approach, which takes advantage of the fast splatting rendering technique to boost the mapping optimizing and ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 5 (3.3. Tracking and Bundle Adjustment), p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
