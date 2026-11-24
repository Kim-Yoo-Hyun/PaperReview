# GeoGaussian: Geometry-aware Gaussian Splatting for Scene Rendering

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5218_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05218.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: Yanyan Li, Chenyu Lyu, Yan Di, Guangyao Zhai, Gim Hee Lee, Federico Tombari
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D Vision
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5218_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05218.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05218.pdf)

## Why This Paper Is Here

GeoGaussian은 점군에서 매끄럽게 이어지는 표면을 찾아 얇은 가우시안을 표면에 정렬하고 그 방향을 최적화 중에도 유지한다. [PDF 1쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05218.pdf#page=1) · [PDF 5쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05218.pdf#page=5)

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Due to the impressive rendering quality of Neural Radiance Fields (NeRF) [25], the area of photo-realistic novel view synthesis (NVS) has become a popular research ...
- **p. 1 / 1 Introduction - extractive body cue:** While NeRFs offer high-quality rendering, 3D Gaussian Splatting ( [8,18]) shows better performance in terms of training speed and rendering quality.
- **p. 1 / 1 Introduction - extractive body cue:** 3D Gaussian Splatting is explicitly represented by a set of Gaussian points parameterized by its position, orientation, and spherical harmonics parameters.
- **p. 1 / 1 Introduction - extractive body cue:** An additional rasterization step re-projects these 3D Gaussians back to training images to capture ⋆Equal senior author
- **p. 2 / 1 Introduction - extractive body cue:** GeoGaussian (ours) Reference 3DGS [18] Fig.
- **p. 2 / 1 Introduction - extractive body cue:** However, in the Gaussian Splatting optimization process, the geometry of 3D Gaussian models lacks sufficient constraints especially in low-textured regions, leading to significant degradation in ...
- **p. 2 / 1 Introduction - extractive body cue:** Since the impressive achievements of convolutional neural networks are made on many tasks, such as point detection [6] and scene completion [40], deep learningbased mesh ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** The contributions of the paper are summarized as: - A parameterization with explicit geometry meaning for thin 3D Gaussians is employed in our carefully designed ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** To mitigate this issue, we propose a novel approach called GeoGaussian.
- **p. 3 / 1 Introduction - extractive body cue:** In this paper, we propose a geometry-aware Gaussian Splatting method emphasizing rendering fidelity and geometry structure simultaneously.
- **p. 1 / 1 Introduction - extractive body cue:** Due to the impressive rendering quality of Neural Radiance Fields (NeRF) [25], the area of photo-realistic novel view synthesis (NVS) has become a popular research ...
- **p. 2 / 1 Introduction - extractive body cue:** 1: Comparisons of novel view rendering and 3D Gaussian model on the Replica Datasets.
- **p. 3 / 1 Introduction - extractive body cue:** In the optimization module, we propose a new geometrically consistent constraint for thin ellipsoids lying on the smooth areas by encouraging the nearest neighbors to ...
- **p. 2 / 1 Introduction - extractive body cue:** However, in the Gaussian Splatting optimization process, the geometry of 3D Gaussian models lacks sufficient constraints especially in low-textured regions, leading to significant degradation in ...
- **p. 2 / 1 Introduction - extractive body cue:** Since the impressive achievements of convolutional neural networks are made on many tasks, such as point detection [6] and scene completion [40], deep learningbased mesh ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Initially, normal vectors are extracted from input point clouds, and then smoothly connected areas are detected based on normals. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (1 Introduction), p. 1 (Body text (section not recovered)) |
| State/latent | Initially, normal, vectors, extracted, input, point, clouds, then, smoothly, connected, areas, detected | geometry, map, object/relationship state | p. 3 (1 Introduction), p. 1 (Body text (section not recovered)), p. 4 (1 Introduction) |
| Output/action | Our proposed pipeline achieves state-of-the-art performance in novel view synthesis and geometric reconstruction, as evaluated qualitatively and quantitatively on public datasets. | point map, pose, scene graph, affordance 또는 query result | p. 1 (Body text (section not recovered)), p. 4 (1 Introduction), p. 1 (Body text (section not recovered)) |
| Objective/outcome | Finally, the pipeline ensures that the scene geometry and texture are maintained through constrained optimization processes with explicit geometry constraints. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 1 (Body text (section not recovered)), p. 2 (1 Introduction), p. 3 (1 Introduction) |

## Main Claims and Actual Contribution

- 국소 표면의 기하로 가우시안을 초기화하고 밀도를 늘릴 때 새 가우시안에도 표면 정렬 정보를 전달한다. [PDF 5쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05218.pdf#page=5) · [PDF 6쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05218.pdf#page=6) · [PDF 7쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05218.pdf#page=7)
- 실내 장면 등에서 새 시점 렌더링과 기하 복원을 비교하고 입력 뷰가 적을 때 구조가 보존되는지를 검토했다. [PDF 9쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05218.pdf#page=9) · [PDF 10쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05218.pdf#page=10) · [PDF 13쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05218.pdf#page=13)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 13 (Figure/Table caption), p. 1 (Body text (section not recovered)) |
| Embodiment/environment | Our proposed pipeline achieves state-of-the-art performance in novel view synthesis and geometric reconstruction, as evaluated qualitatively and quantitatively on public datasets. | hardware/simulator version and reset protocol | p. 1 (Body text (section not recovered)), p. 1 (1 Introduction) |
| Dataset/benchmark | 1: Comparisons of novel view rendering and 3D Gaussian model on the Replica Datasets. | role, split, size and leakage | p. 1 (Body text (section not recovered)), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Metric | Table 4: Sparse view rendering on the R1 sequence of Replica dataset. The position and orientation of viewpoints used in training and evaluation are given in Appendix. Training and Evaluation. Figure 5 ... | definition, denominator, direction and uncertainty | p. 13 (Figure/Table caption), p. 2 (1 Introduction), p. 2 (Figure/Table caption) |
| Baseline/ablation | Li et al. - Evaluations on the public datasets demonstrate that the proposed method improves rendering quality compared to state-of-the-art Gaussian Splatting methods. | fair input/data/compute/action matching | p. 4 (1 Introduction), p. 9 (Figure/Table caption), p. 11 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Body text (section not recovered) - extractive body cue:** This degradation significantly affects the rendering quality of novel views that deviate significantly from the viewpoints in the training data.
- **p. 2 / 1 Introduction - extractive body cue:** However, in the Gaussian Splatting optimization process, the geometry of 3D Gaussian models lacks sufficient constraints especially in low-textured regions, leading to significant degradation in ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 4: Statistics of the number of Gaussians in sequences of Replica. To make the comparison compact, more values are illustrated in Appendix. evident in ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (Body text (section not recovered))이다.
