# GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3958_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03958.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: Yuanhui Huang, Wenzhao Zheng, Yunpeng Zhang, Jie Zhou, Jiwen Lu
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, Gaussian Splatting, semantic occupancy
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3958_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03958.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

GaussianFormer는 카메라 영상으로부터 3차원 의미 점유를 객체 중심 가우시안 집합으로 예측한다.

## Problem and Motivation

- **p. 2 / 1 Introduction - extractive body cue:** Whether to use LiDAR for 3D perception has long been the core debate among autonomous driving companies.
- **p. 2 / 1 Introduction - extractive body cue:** While vision-centric systems share an economical advantage, their inability to capture obstacles of arbitrary shapes hinders driving safety and robustness [14,18,26,27].
- **p. 2 / 1 Introduction - extractive body cue:** The emergence of 3D semantic occupancy prediction methods [4,17,19,36,51,58,64] remedies this issue by predicting the occupancy status of each voxel in the 3D space, which ...
- **p. 2 / 1 Introduction - extractive body cue:** Despite the promising applications, the dense output space of 3D occupancy prediction poses a great challenge in how to efficiently and effectively represent the 3D ...
- **p. 2 / 1 Introduction - extractive body cue:** Voxel-based methods [24,51] assign each voxel with a feature vector to obtain dense representations to describe the fine-grained structure of a 3D scene.
- **p. 2 / 1 Introduction - extractive body cue:** It is also more difficult to capture scene dynamics with grid-based representations since it is objects instead of grids that move in the 3D space ...
- **p. 3 / 1 Introduction - extractive body cue:** GaussianFormer achieves comparable performance with existing state-of-the-art methods with only 17.8% - 24.8% of their memory consumption.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We propose a GaussianFormer model to effectively obtain 3D semantic Gaussians from image inputs.
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose the first object-centric representation for 3D semantic occupancy prediction.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We propose a GaussianFormer model consisting of sparse convolution and cross-attention to efficiently transform 2D images into 3D Gaussian representations.
- **p. 1 / Body text (section not recovered) - extractive body cue:** To address this, we propose an object-centric representation to describe 3D scenes with sparse 3D semantic Gaussians where each Gaussian represents a flexible region of ...
- **p. 3 / 1 Introduction - extractive body cue:** The proposed 3D Gaussian representation uses a sparse and adaptive set of features to describe a 3D scene but can still model the fine-grained structure ...
- **p. 3 / 1 Introduction - extractive body cue:** We then decode the properties of 3D semantic Gaussians from the updated queries as the scene representation.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We propose a GaussianFormer model to effectively obtain 3D semantic Gaussians from image inputs. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | GaussianFormer, model, effectively, obtain, semantic, Gaussians, image, inputs, efficiently, incorporate, interactions, among | geometry, map, object/relationship state | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Output/action | To efficiently incorporate interactions among 3D Gaussians, we treat them as point clouds located at the Gaussian means and | point map, pose, scene graph, affordance 또는 query result | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (Body text (section not recovered)) |
| Objective/outcome | We iteratively refine the properties of the 3D Gaussians for smoother optimizations. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |

## Main Claims and Actual Contribution

- 각 가우시안에 공간과 의미 정보를 담는다.
- 예측한 집합으로 장면의 의미 점유를 복원해 평가한다.

[저자 원문](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3958_ECCV_2024_paper.php)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 10 (4 Experiments), p. 14 (Figure/Table caption) |
| Embodiment/environment | 4.1 Datasets NuScenes [3] consists of 1000 sequences of various driving scenes collected in Boston and Singapore, which are officially split into 700/150/150 sequences for training, validation and testing, respectively. | hardware/simulator version and reset protocol | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Dataset/benchmark | This is because the 3D Gaussian representation better exploits the sparse nature of the driving scenes and the diversity of object scales with flexible properties of position and covariance. | role, split, size and leakage | p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Metric | Table 5: Ablation on the number of Gaussians. The latency and memory are tested on an NVIDIA 4090 GPU with batch size one during inference. The performance improves consistently with more Gaussians ... | definition, denominator, direction and uncertainty | p. 13 (Figure/Table caption), p. 12 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Baseline/ablation | Even compared with dense grid representations, GaussianFormer performs on par with OccFormer [58] and SurroundOcc [51]. | fair input/data/compute/action matching | p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 12 / 26500 M - extractive body cue:** This is because the positions of Gaussians are sensitive to noise which quickly converge to a trivial solution without regularization for coherence during refinement.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (Body text (section not recovered))이다.
