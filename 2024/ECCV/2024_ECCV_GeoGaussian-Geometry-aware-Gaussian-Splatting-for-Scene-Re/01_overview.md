# GeoGaussian: Geometry-aware Gaussian Splatting for Scene Rendering

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5218_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05218.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D Vision
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5218_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05218.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, in the Gaussian Splatting optimization process, the geometry of 3D Gaussian models lacks sufficient constraints especially in low-textured regions, leading to significant degradation in rendering performance for novel views tha ...를 문제로 두고, The contributions of the paper are summarized as: - A parameterization with explicit geometry meaning for thin 3D Gaussians is employed in our carefully designed initialization and densification strategies to establish reasonable ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 3 / 1 Introduction - extractive body cue:** The contributions of the paper are summarized as: - A parameterization with explicit geometry meaning for thin 3D Gaussians is employed in our carefully designed ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** To mitigate this issue, we propose a novel approach called GeoGaussian.
- **p. 3 / 1 Introduction - extractive body cue:** In this paper, we propose a geometry-aware Gaussian Splatting method emphasizing rendering fidelity and geometry structure simultaneously.
- **p. 1 / 1 Introduction - extractive body cue:** Due to the impressive rendering quality of Neural Radiance Fields (NeRF) [25], the area of photo-realistic novel view synthesis (NVS) has become a popular research ...
- **p. 2 / 1 Introduction - extractive body cue:** 1: Comparisons of novel view rendering and 3D Gaussian model on the Replica Datasets.
- **p. 13 / Figure/Table caption - extractive body cue:** Table 4: Sparse view rendering on the R1 sequence of Replica dataset. The position and orientation of viewpoints used in training and evaluation are given ...
- **p. 1 / Body text (section not recovered) - extractive body cue:** Our proposed pipeline achieves state-of-the-art performance in novel view synthesis and geometric reconstruction, as evaluated qualitatively and quantitatively on public datasets.
- **p. 11 / Figure/Table caption - extractive body cue:** Table 2: Comparison of rendering on the Replica dataset. The position and orientation of viewpoints used in training and evaluation are illustrated in Appendix. Evaluation ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 13 (Figure/Table caption), p. 1 (Body text (section not recovered)) |
| Embodiment/environment | Our proposed pipeline achieves state-of-the-art performance in novel view synthesis and geometric reconstruction, as evaluated qualitatively and quantitatively on public datasets. | hardware/simulator version and reset protocol | p. 1 (Body text (section not recovered)), p. 1 (1 Introduction) |
| Dataset/benchmark | 1: Comparisons of novel view rendering and 3D Gaussian model on the Replica Datasets. | role, split, size and leakage | p. 1 (Body text (section not recovered)), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Metric | Table 4: Sparse view rendering on the R1 sequence of Replica dataset. The position and orientation of viewpoints used in training and evaluation are given in Appendix. Training and Evaluation. Figure 5 ... | definition, denominator, direction and uncertainty | p. 13 (Figure/Table caption), p. 2 (1 Introduction), p. 2 (Figure/Table caption) |
| Baseline/ablation | Li et al. - Evaluations on the public datasets demonstrate that the proposed method improves rendering quality compared to state-of-the-art Gaussian Splatting methods. | fair input/data/compute/action matching | p. 4 (1 Introduction), p. 9 (Figure/Table caption), p. 11 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Body text (section not recovered) - extractive body cue:** This degradation significantly affects the rendering quality of novel views that deviate significantly from the viewpoints in the training data.
- **p. 2 / 1 Introduction - extractive body cue:** However, in the Gaussian Splatting optimization process, the geometry of 3D Gaussian models lacks sufficient constraints especially in low-textured regions, leading to significant degradation in ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 4: Statistics of the number of Gaussians in sequences of Replica. To make the comparison compact, more values are illustrated in Appendix. evident in ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, in the Gaussian Splatting optimization process, the geometry of 3D Gaussian models lacks sufficient constraints especially in low-textured regions, leading to significant degradation in rendering performance for novel views tha ...를 문제로 두고, The contributions of the paper are summarized as: - A parameterization with explicit geometry meaning for thin 3D Gaussians is employed in our carefully designed initialization and densification strategies to establish reasonable ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (Body text (section not recovered)) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
