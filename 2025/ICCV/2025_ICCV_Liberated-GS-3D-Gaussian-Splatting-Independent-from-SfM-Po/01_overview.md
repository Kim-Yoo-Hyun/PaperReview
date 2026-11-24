# Liberated-GS: 3D Gaussian Splatting Independent from SfM Point Clouds

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Pan_Liberated-GS_3D_Gaussian_Splatting_Independent_from_SfM_Point_Clouds_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_Liberated-GS_3D_Gaussian_Splatting_Independent_from_SfM_Point_Clouds_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Weihong Pan, Xiaoyu Zhang, Hongjia Zhai, Xiaojun Xiang, Hanqing Jiang, Guofeng Zhang
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, geometry, point cloud, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Pan_Liberated-GS_3D_Gaussian_Splatting_Independent_from_SfM_Point_Clouds_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_Liberated-GS_3D_Gaussian_Splatting_Independent_from_SfM_Point_Clouds_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_Liberated-GS_3D_Gaussian_Splatting_Independent_from_SfM_Point_Clouds_ICCV_2025_paper.pdf)

## Why This Paper Is Here

Liberated-GS는 조밀한 영상 시퀀스에서 단안 깊이와 초기 가우시안의 렌더링 깊이를 결합해 SfM 점군 없이 3D 가우시안을 초기화한다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_Liberated-GS_3D_Gaussian_Splatting_Independent_from_SfM_Point_Clouds_ICCV_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_Liberated-GS_3D_Gaussian_Splatting_Independent_from_SfM_Point_Clouds_ICCV_2025_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian Splatting (3DGS) has demonstrated impressive performance in novel view synthesis and real-time rendering.
- **p. 1 / Abstract - extractive body cue:** However, it heavily relies on high-quality initial sparse points from Structure-from-Motion (SfM), which often struggles in textureless regions, degrading the geometry and visual quality of ...
- **p. 1 / Abstract - extractive body cue:** To address this limitation, we propose a novel initialization pipeline, achieving highfidelity reconstruction from dense image sequences without relying on SfM-derived point clouds.
- **p. 1 / Abstract - extractive body cue:** Specifically, we first propose an effective depth alignment method to align the estimated monocular depth with depth rendered from an under-optimized coarse Gaussian model using ...
- **p. 1 / Abstract - extractive body cue:** After that, to efficiently process dense image sequences, we incorporate a progressive segmented initialization process to generate the initial points.
- **p. 2 / 1. Introduction - extractive body cue:** However, the rendering performance of this method is also not competitive, suffering from poor detail recovery and floaters due to the lack of prior geometric ...
- **p. 2 / 1. Introduction - extractive body cue:** This significantly degrades the rendering performance of 3DGS, as it cannot transport Gaussians far away from their initialized positions [18], leading to a lack of ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** The contributions of our method are as follows. • We propose Librated-GS, a novel initialization approach to eliminate the reliance on SfM points of 3D ...
- **p. 2 / 3. Method - extractive body cue:** 3.3, we present a progressive segmented initialization with importance resampling.
- **p. 3 / 3. Method - extractive body cue:** To address this, we propose an unbiased depth rendering method detailed in Sec.
- **p. 3 / 3. Method - extractive body cue:** First, we propose an effective depth alignment method to establish high-quality geometry priors, as described in Sec.
- **p. 4 / 3.2. Effective Depth Alignment - extractive body cue:** Maximum Alpha Current Ray i-th Gaussian depth in alpha-blending i-th Gaussian depth in our method Figure 4.
- **p. 3 / 3. Method - extractive body cue:** … …… Importance Resampling Progressive Segmented Initialization RGB Images Random Init Monocular Depth Estimator Coarse Gaussian Model Estimate Render Rendered Depth Estimated Depth Align Ensembled ...
- **p. 2 / 3. Method - extractive body cue:** The optimization stage remains unchanged.
- **p. 3 / 3.2. Effective Depth Alignment - extractive body cue:** As the coarse model is not fully optimized, direct alpha-blending introduces noise.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We propose a pipeline to reconstruct photo-realistic scenes from posed image sequences without requiring an input point cloud. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (3. Method), p. 5 (3.2. Effective Depth Alignment) |
| State/latent | pipeline, reconstruct, photo-realistic, scenes, posed, image, sequences, without, requiring, input, point, cloud | geometry, map, object/relationship state | p. 2 (3. Method), p. 5 (3.2. Effective Depth Alignment), p. 5 (3.3. Progressive Segmented Initialization) |
| Output/action | Specifically, taking the current view I along with its rendered image Irender and depth map Drender from Eq. | point map, pose, scene graph, affordance 또는 query result | p. 5 (3.2. Effective Depth Alignment), p. 5 (3.3. Progressive Segmented Initialization), p. 2 (1. Introduction) |
| Objective/outcome | we optimize the photometric loss to refine the ensembled depths {D1, D2, . . . , Dki} for all previous views. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3.3. Progressive Segmented Initialization), p. 3 (3. Method), p. 4 (3.2. Effective Depth Alignment) |

## Main Claims and Actual Contribution

- 초기 가우시안 모델의 깊이에 단안 추정치를 정렬해 융합하고, 긴 시퀀스는 구간을 나누어 초기 점을 순차적으로 만든다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_Liberated-GS_3D_Gaussian_Splatting_Independent_from_SfM_Point_Clouds_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_Liberated-GS_3D_Gaussian_Splatting_Independent_from_SfM_Point_Clouds_ICCV_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_Liberated-GS_3D_Gaussian_Splatting_Independent_from_SfM_Point_Clouds_ICCV_2025_paper.pdf#page=5)
- Mip-NeRF360과 Tanks and Temples 등에서 SfM 점을 쓴 초기화와 새 시점 화질을 비교하고 깊이 정렬의 효과를 평가했다. [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_Liberated-GS_3D_Gaussian_Splatting_Independent_from_SfM_Point_Clouds_ICCV_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_Liberated-GS_3D_Gaussian_Splatting_Independent_from_SfM_Point_Clouds_ICCV_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_Liberated-GS_3D_Gaussian_Splatting_Independent_from_SfM_Point_Clouds_ICCV_2025_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 6 (4.2. Comparison), p. 7 (4.2. Comparison) |
| Embodiment/environment | To validate the effectiveness of our method, extensive qualitative and quantitative comparison experiments are conducted on three real-world datasets, including two benchmark datasets (Mip-NeRF360 [5] and Tanks and Temples [22]) and an ... | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Dataset/benchmark | Comparison of runtime between our pipeline and COLMAP on Scene03 (300 images, 1237×658 resolution) from OMMO [25] dataset. | role, split, size and leakage | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 8 (4.3. Ablation Study), p. 7 (4.2. Comparison) |
| Metric | Similarly, RAIN-GS [18], despite its new initialization strategy, struggles to address detail loss from insufficient initial points and produces lower geometric quality compared to SfM-initialized 3DGS (e.g., the lower part of the ... | definition, denominator, direction and uncertainty | p. 6 (4.2. Comparison), p. 8 (4.2. Comparison), p. 6 (4.2. Comparison) |
| Baseline/ablation | Our method demonstrates substantial improvements across all three metrics compared to all other methods, even outperforming 3DGS initialized with SfM point clouds. | fair input/data/compute/action matching | p. 6 (4.2. Comparison), p. 6 (4.2. Comparison), p. 7 (4.2. Comparison) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.2. Comparison - extractive body cue:** Additionally, since [14] does not account for scale when utilizing monocular depth to estimate camera poses and generate 3D points, directly using the ground-truth poses ...
- **p. 8 / 4.2. Comparison - extractive body cue:** Depth PSNR↑ SSIM↑ LPIPS↓ Ensembled Depth 27.588 0.822 0.187 Aligned Depth 27.524 0.818 0.189 Estimated Depth 27.390 0.816 0.191 Rendered Depth 26.596 0.708 0.201 segmented ...
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Our initialization does not interfere with subsequent optimization.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Novel View Synthesis Comparison. We propose a novel Gaussian Splatting initialization pipeline to address the degradation in novel view rendering quality caused by ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Point Cloud from different depths. We compare the point cloud from different depths for single view and multiple views. (a) Rendered Depth from ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Method), p. 2 (3. Method), p. 3 (3.2. Effective Depth Alignment)이다.
