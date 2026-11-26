# C-GenReg: Training-Free 3D Point Cloud Registration by Multi-View-Consistent Geometry-to-Image Generation with Probabilistic Modalities Fusion

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Yuval Haitman, Amit Efraim, Joseph M. Francos
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Registration, LiDAR, Diffusion, Generation, point cloud, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

C-GenReg는 점군에서 합성한 다중 시점 영상의 대응과 원래 점군의 기하 대응을 결합해 추가 학습 없이 두 점군을 정합한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce C-GenReg, a training-free framework for 3D point cloud registration that leverages the complementary strengths of world-scale generative priors and registration-oriented Vision Foundation Models ...
- **p. 1 / Abstract - extractive body cue:** Current learning-based 3D point cloud registration methods struggle to generalize across sensing modalities, sampling differences, and environments.
- **p. 1 / Abstract - extractive body cue:** Hence, CGenReg augments the geometric point cloud registration branch by transferring the matching problem into an auxiliary image domain, where VFMs excel, using a World ...
- **p. 1 / Abstract - extractive body cue:** This generative transfer preserves spatial coherence across source and target views without any fine-tuning.
- **p. 1 / Abstract - extractive body cue:** From these generated views, a VFM pretrained for finding dense correspondences extracts matches.
- **p. 2 / 1. Introduction - extractive body cue:** However, these methods primarily rely on single-view generation and lack mechanisms for handling multiple geometrically related views.
- **p. 3 / 3.1. Problem Definition - extractive body cue:** However, C∗is unknown in practice, and the core challenge is to establish reliable correspondences between P and Q.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** Standard point cloud registration consists of feature extraction, feature matching, and robust pose estimation (e.g.
- **p. 2 / 1. Introduction - extractive body cue:** In contrast, our method, C-GenReg (stands for Consistent Generative Registration), leverages WFMs to generate multiview-consistent RGB views directly from geometry, eliminating the need for any ...
- **p. 2 / 1. Introduction - extractive body cue:** Instead, we introduce a "Matchthen-Fuse" scheme that combines two independent correspondence posteriors, one from the WFM + VFM branch and one from the geometric branch, ...
- **p. 5 / 3.5. Match-then-Fuse Probabilistic Fusion - extractive body cue:** To address this, we introduce the Disjunctive Posterior Fusion (Noisy-OR), which aggregates evidence 3008
- **p. 5 / 3.5. Match-then-Fuse Probabilistic Fusion - extractive body cue:** To meet these goals, we propose a "match-then-fuse" probabilistic strategy, where putative correspondences are first established independently for each modality by computing feature similarity matrices ...
- **p. 5 / 3.5. Match-then-Fuse Probabilistic Fusion - extractive body cue:** To approximate the modality-specific correspondence posterior Pr(Mij/Sm ij ), where m∈{geo,img}, we first compute the source-target feature similarity matrices for each modality and then apply ...
- **p. 4 / 3.3. Generated-RGB Branch - extractive body cue:** Specifically, we use MASt3R [14], a VFM trained to produce dense correspondence-aware features.
- **p. 4 / 3.3. Generated-RGB Branch - extractive body cue:** To ensure coherent and controllable generation, we use prompt-based text guidance with a fixed structure: a shared prefix that instructs the model to interpret the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | From each input point cloud, we render a depth map and use the Cosmos-Transfer WFM [18] to generate multi-view-consistent RGB images that preserve 3006 | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.2. C-GenReg - Overview), p. 4 (3.2. C-GenReg - Overview) |
| State/latent | input, point, cloud, render, depth, Cosmos-Transfer, WFM, generate, multi-view-consistent, RGB, images, preserve | geometry, map, object/relationship state | p. 3 (3.2. C-GenReg - Overview), p. 4 (3.2. C-GenReg - Overview), p. 4 (3.3. Generated-RGB Branch) |
| Output/action | Generated source and target images with a subset of matched points (color-coded correspondences), and the corresponding matches visualized on the input point clouds. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.2. C-GenReg - Overview), p. 4 (3.3. Generated-RGB Branch), p. 5 (3.3. Generated-RGB Branch) |
| Objective/outcome | The fusion module is designed with two main objectives: (1) to preserve the inductive biases of the pretrained feature extractors, which are optimized for point matching- each for its own domain, and ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.5. Match-then-Fuse Probabilistic Fusion), p. 4 (3.3. Generated-RGB Branch), p. 5 (3.3. Generated-RGB Branch) |

## Main Claims and Actual Contribution

- 기하에 일관된 RGB 영상을 합성하고 이미지에서 구한 대응점을 원래의 깊이로 3차원에 역투영한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.pdf#page=5)
- 두 대응 분포를 확률적으로 융합하고 실내 3DMatch·ScanNet 및 실외 Waymo에서 회전·이동 정합을 평가했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Haitman_C-GenReg_Training-Free_3D_Point_Cloud_Registration_by_Multi-View-Consistent_Geometry-to-Image_Generation_CVPR_2026_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.2. Method Evaluation), p. 7 (4.2. Method Evaluation) |
| Embodiment/environment | For outdoor evaluation, we employ the Waymo Open Dataset [24], which contains large-scale LiDAR scans, and serves as a generalization benchmark for outdoor registration tasks. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings) |
| Dataset/benchmark | To evaluate cross-dataset generalization, we benchmark all methods on the ScanNet indoor registration benchmarks (Tab. | role, split, size and leakage | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), p. 7 (4.2. Method Evaluation), p. 7 (4.2. Method Evaluation) |
| Metric | For each benchmark, we report both the mean and median values of these errors, as well as the registration accuracy - the percentage of registration problems with an error below a given ... | definition, denominator, direction and uncertainty | p. 6 (4.1. Experimental Settings), p. 7 (4.2. Method Evaluation), p. 8 (4.3. Ablation Studies) |
| Baseline/ablation | CGenReg is compared against both the hand-crafted descriptor FPFH [22] and several state-of-the-art (SOTA) learning-based baselines, including GeoTransformer [20], FCGF [4], Predator [11], RoITr [29], and GPCR [12]. | fair input/data/compute/action matching | p. 6 (4.2. Method Evaluation), p. 7 (4.2. Method Evaluation), p. 6 (4.2. Method Evaluation) |

## Explicit Limitations and Failure Boundary

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Prompt robustness on 3DMatch. Relative rotation (RRE,◦) and translation (RTE, cm) errors under different prompt types. geometric coherence across viewpoints. A task-specific VFM ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 3 (3.1. Problem Definition), p. 1 (1. Introduction), p. 5 (3.5. Match-then-Fuse Probabilistic Fusion)이다.
