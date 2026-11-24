# CityGaussianV2: Efficient and Geometrically Accurate Reconstruction for Large-Scale Scenes

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/d218ec74edbfc494fa7d7a253951c603-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114864. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Yang Liu, Chuanchen Luo, Zhongkai Mao, Junran Peng, Zhaoxiang Zhang
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/d218ec74edbfc494fa7d7a253951c603-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2025/file/d218ec74edbfc494fa7d7a253951c603-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://proceedings.iclr.cc/paper_files/paper/2025/file/d218ec74edbfc494fa7d7a253951c603-Paper-Conference.pdf)

## Why This Paper Is Here

CityGaussianV2는 도시 규모 장면에서 2D 가우시안의 기하와 렌더링을 함께 복원하면서 훈련·저장 비용을 줄인다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/d218ec74edbfc494fa7d7a253951c603-Paper-Conference.pdf#page=1) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/d218ec74edbfc494fa7d7a253951c603-Paper-Conference.pdf#page=5)

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

- 분리한 기울기와 깊이 회귀로 가우시안 증식을 제어하고, 지나치게 길어진 가우시안을 걸러 개수 폭증을 억제한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/d218ec74edbfc494fa7d7a253951c603-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/d218ec74edbfc494fa7d7a253951c603-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/d218ec74edbfc494fa7d7a253951c603-Paper-Conference.pdf#page=6)
- 대규모 장면에서 정답 점군에 대한 표면 오차와 렌더링 품질을 평가하고 블록별 학습의 시간·메모리·저장 비용을 비교했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/d218ec74edbfc494fa7d7a253951c603-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/d218ec74edbfc494fa7d7a253951c603-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/d218ec74edbfc494fa7d7a253951c603-Paper-Conference.pdf#page=9)

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

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 4 (3 METHOD)이다.
