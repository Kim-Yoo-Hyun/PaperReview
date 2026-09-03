# CityGaussianV2: Efficient and Geometrically Accurate Reconstruction for Large-Scale Scenes

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=a3ptUbuzbW.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114864. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openreview.net/forum?id=a3ptUbuzbW
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/114864
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 On the one hand, existing methods face significant challenges related to scalability and generalization ability.를 문제로 두고, In summary, our contributions are four-fold: • A novel optimization strategy for 2DGS, that accelerates its convergence under large-scale scenes and enables it to be scaled up to high capacity (Sec.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Recently, 3D Gaussian Splatting (3DGS) has revolutionized radiance field reconstruction, manifesting efficient and high-fidelity novel view synthesis.
- **p. 1 / ABSTRACT - extractive body cue:** However, accurately representing surfaces, especially in large and complex scenarios, remains a significant challenge due to the unstructured nature of 3DGS.
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we present CityGaussianV2, a novel approach for large-scale scene reconstruction that addresses critical challenges related to geometric accuracy and efficiency.
- **p. 1 / ABSTRACT - extractive body cue:** Building on the favorable generalization capabilities of 2D Gaussian Splatting (2DGS), we address its convergence and scalability issues.
- **p. 1 / ABSTRACT - extractive body cue:** Specifically, we implement a decomposed-gradient-based densification and depth regression technique to eliminate blurry artifacts and accelerate convergence.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** On the one hand, existing methods face significant challenges related to scalability and generalization ability.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In response to these challenges, we introduce CityGaussianV2, a geometrically accurate yet efficient strategy for large-scale scene reconstruction.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are four-fold: • A novel optimization strategy for 2DGS, that accelerates its convergence under large-scale scenes and enables it to be ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, our contribution-based vectree quantization enables a tenfold reduction in storage requirements for large-scale 2DGS.
- **p. 6 / 3 METHOD - extractive body cue:** To resolve these issues, we propose a novel pipeline, as shown in Fig.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** TrimGS (Fan et al., 2024) further provides a novel per-Gaussian contribution definition to remove inaccurate geometry.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** One of the most seminal contributions to this field is Neural Radiance Fields (NeRF) (Mildenhall et al., 2021), which implicitly models target scenes using multi-layer ...
- **p. 4 / 3 METHOD - extractive body cue:** 4, it first pre-trains a coarse model on full training data with the schedule of 3DGS.
- **p. 6 / 3 METHOD - extractive body cue:** To bypass the distillation step, we use an SH degree of 2 from the start, reducing the SH feature dimension from 48 to 27.
- **p. 5 / 3 METHOD - extractive body cue:** The derived outputs are used for loss calculation.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 5, we begin by initializing a 3DGS field with the ground-truth point cloud, then traverse all training views to rasterize and count visible frequency through the output visible mask. | RGB-D, image set, point cloud, depth와 camera pose | p. 7 (3 METHOD), p. 17 (C MORE IMPLEMENTATION DETAILS) |
| State/latent | begin, initializing, DGS, field, ground-truth, point, cloud, then, traverse, training, views, rasterize | geometry, map, object/relationship state | p. 7 (3 METHOD), p. 17 (C MORE IMPLEMENTATION DETAILS), p. 5 (3 METHOD) |
| Output/action | Secondly, for mesh extraction, occlusion and lack of observation hinder reconstruction of some road surfaces and building facades. | point map, pose, scene graph, affordance 또는 query result | p. 17 (C MORE IMPLEMENTATION DETAILS), p. 5 (3 METHOD), p. 5 (3 METHOD) |
| Objective/outcome | To alleviate this problem, we prioritize the gradient from SSIM loss and introduce a Decomposed-Gradient-based Densification (DGD) strategy. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our contributions are four-fold: • A novel optimization strategy for 2DGS, that accelerates its convergence under large-scale scenes and enables it to be ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, our contribution-based vectree quantization enables a tenfold reduction in storage requirements for large-scale 2DGS.
- **p. 6 / 3 METHOD - extractive body cue:** To resolve these issues, we propose a novel pipeline, as shown in Fig.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** TrimGS (Fan et al., 2024) further provides a novel per-Gaussian contribution definition to remove inaccurate geometry.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** One of the most seminal contributions to this field is Neural Radiance Fields (NeRF) (Mildenhall et al., 2021), which implicitly models target scenes using multi-layer ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** For MatrixCity-Aerial, our method achieves the best surface quality among all algorithms, with the F1 score being twice that of 2DGS and outperforming CityGaussian by ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** For GauU-Scene, our model significantly outperforms existing geometry-specialized methods in rendering quality.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** 1 shows that even without parallel tuning, our proposed optimization strategy enables our model to achieve significantly better 8

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Embodiment/environment | Therefore, we utilize the realistic dataset GauU-Scene (Xiong et al., 2024) and the synthetic dataset MatrixCity (Li et al., 2023a). | hardware/simulator version and reset protocol | p. 7 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Dataset/benchmark | We require datasets with accurate ground-truth point clouds. | role, split, size and leakage | p. 7 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Metric | Figure 1: Illustration of the superiority of CityGaussianV2. (a) Our method reconstructs large-scale complex scenes with accurate geometry from multi-view RGB images, restoring intricate structures of woods, buildings, and roads. (b) "O ... | definition, denominator, direction and uncertainty | p. 1 (Figure/Table caption), p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Baseline/ablation | 5.2 COMPARISON WITH SOTA METHODS In this section, we compare CityGaussianV2 with state-of-the-art (SOTA) methods both quantitatively and qualitatively. | fair input/data/compute/action matching | p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5 EXPERIMENTS - extractive body cue:** As shown, NeRF-based methods are more prone to failure due to the NaN outputs of the MLP or poor convergence under sparse supervision in large-scale ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Due to page limitations, detailed parameters for block partition and quantization are provided in the Appendix.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** Furthermore, GOF fails to complete training or extract meaningful meshes.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 1: Comparison with SOTA reconstruction methods. "NaN" means no results due to NaN error. "FAIL" means the method fails to extract meaningful mesh due ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** LightGaussian's (Fan et al., 2023) pruning strategy, however, falls short in preserving rendering quality.
- **p. 16 / Figure/Table caption - extractive body cue:** Table 5: Detailed geometry metrics on GauU-Scene datasets ((Xiong et al., 2024)). * means that the method fails to finish 60,000 iterations training and therefore ...
- **p. 17 / C MORE IMPLEMENTATION DETAILS - extractive body cue:** D DISCUSSION While our method successfully delivers favorable efficiency and accurate geometry reconstruction for large-scale scenes, we also want to discuss its limitations: Firstly, this ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 On the one hand, existing methods face significant challenges related to scalability and generalization ability.를 문제로 두고, In summary, our contributions are four-fold: • A novel optimization strategy for 2DGS, that accelerates its convergence under large-scale scenes and enables it to be scaled up to high capacity (Sec.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 4 (3 METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
