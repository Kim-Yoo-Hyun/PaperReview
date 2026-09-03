# PointCNN: Convolution On X-Transformed Points

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1801.07791.
> PDF retrieval source: https://arxiv.org/pdf/1801.07791. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2018 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, point cloud, geometry, representation
- Official paper: https://arxiv.org/abs/1801.07791
- Full-text retrieval: https://arxiv.org/pdf/1801.07791
- Code/Project: https://github.com/yangyanli/PointCNN
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 (1b) We illustrate the problems and challenges of applying convolutions on point clouds in Figure 1.를 문제로 두고, In this paper, we propose to learn a K × K X-transformation for the coordinates of K input points (p1, p2, ..., pK), with a multilayer perceptron [39], i.e., X = MLP(p1, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present a simple and general framework for feature learning from point clouds.
- **p. 1 / Abstract - extractive body cue:** The key to the success of CNNs is the convolution operator that is capable of leveraging spatially-local correlation in data represented densely in grids (e.g. ...
- **p. 1 / Abstract - extractive body cue:** However, point clouds are irregular and unordered, thus directly convolving kernels against features associated with the points will result in desertion of shape information and ...
- **p. 1 / Abstract - extractive body cue:** To address these problems, we propose to learn an X-transformation from the input points to simultaneously promote two causes: the first is the weighting of ...
- **p. 1 / Abstract - extractive body cue:** Element-wise product and sum operations of the typical convolution operator are subsequently applied on the X-transformed features.
- **p. 1 / 1 Introduction - extractive body cue:** (1b) We illustrate the problems and challenges of applying convolutions on point clouds in Figure 1.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose to learn a K × K X-transformation for the coordinates of K input points (p1, p2, ..., pK), with a ...
- **p. 1 / Abstract - extractive body cue:** We present a simple and general framework for feature learning from point clouds.
- **p. 1 / Abstract - extractive body cue:** To address these problems, we propose to learn an X-transformation from the input points to simultaneously promote two causes: the first is the weighting of ...
- **p. 2 / 1 Introduction - extractive body cue:** We show our results on multiple challenging benchmark datasets and tasks in Section 4, together with ablation experiments and visualizations for a better understanding of ...
- **p. 2 / 1 Introduction - extractive body cue:** Nevertheless, PointCNN built with X-Conv is still significantly better than a direct application of typical convolutions on point clouds, and on par or better than ...
- **p. 1 / 1 Introduction - extractive body cue:** In (i), each grid cell is associated with a feature.
- **p. 2 / 1 Introduction - extractive body cue:** Section 3 contains the details of X-Conv, as well as PointCNN architectures.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Nevertheless, PointCNN built with X-Conv is still significantly better than a direct application of typical convolutions on point clouds, and on par or better than state-of-the-art neural networks designed for point cloud ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| State/latent | Nevertheless, PointCNN, built, X-Conv, still, significantly, better, direct, application, typical, convolutions, point | geometry, map, object/relationship state | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Output/action | However, for data represented in point cloud form, which is irregular and unordered, the convoralution operator is ill-suited for leveraging spatially-local correlations in the data. 𝑓" 𝑓# 𝑓$ 𝑓% 1 𝑓" 2 ... | point map, pose, scene graph, affordance 또는 query result | p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| geometric accuracy, semantic consistency와 planning/manipulation utility | p. 1 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose to learn a K × K X-transformation for the coordinates of K input points (p1, p2, ..., pK), with a ...
- **p. 1 / Abstract - extractive body cue:** We present a simple and general framework for feature learning from point clouds.
- **p. 1 / Abstract - extractive body cue:** To address these problems, we propose to learn an X-transformation from the input points to simultaneously promote two causes: the first is the weighting of ...
- **p. 2 / 1 Introduction - extractive body cue:** We show our results on multiple challenging benchmark datasets and tasks in Section 4, together with ablation experiments and visualizations for a better understanding of ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 3: Segmentation result comparisons on the S3DIS [2] Area 5 in overall accuracy (OA, %), micro-averaged accuracy (mAcc, %), micro-averaged IoU (mIoU, %) and ...
- **p. 7 / 4 Experiments - extractive body cue:** PointCNN outperforms PointNet++ on both datasets, with a more prominent advantage on Quick Draw (25M data samples), which is significantly larger than TU-Berlin (0.02M data ...
- **p. 6 / 4 Experiments - extractive body cue:** Note that PointCNN achieved top performance on both ModelNet40 and ScanNet.
- **p. 7 / 4 Experiments - extractive body cue:** For MNIST data, PointCNN achieved comparable performance with other methods, indicating its effective learning of the digits' shape information.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 14 (Figure/Table caption), p. 7 (4 Experiments) |
| Embodiment/environment | Material Section 2, and the PointCNN architectures for the tasks on these datasets can be found in Supp. | hardware/simulator version and reset protocol | p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Dataset/benchmark | We evaluate PointCNN on the segmentation of ShapeNet Parts, S3DIS, and ScanNet datasets, and summarize the results in Table 2. | role, split, size and leakage | p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Metric | ShapeNet Parts S3DIS ScanNet pIoU mpIoU mIoU OA SyncSpecCNN [55] 84.74 82.0 - - Pd-Network [22] 85.49 82.7 - - SSCN [12] 85.98 83.3 - - SPLATNet [43] 85.4 83.7 - - ... | definition, denominator, direction and uncertainty | p. 7 (4 Experiments), p. 14 (Figure/Table caption), p. 7 (4 Experiments) |
| Baseline/ablation | We note that PointCNN outperforms all the compared methods, including SSCN [12], SPGraph [24] and SGPN [49], which are specialized segmentation networks with state-of-the-art performance. | fair input/data/compute/action matching | p. 7 (4 Experiments), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4 Experiments - extractive body cue:** Together with the lack of "shape" information, PointNet++ fails completely on this task.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 (1b) We illustrate the problems and challenges of applying convolutions on point clouds in Figure 1.를 문제로 두고, In this paper, we propose to learn a K × K X-transformation for the coordinates of K input points (p1, p2, ..., pK), with a multilayer perceptron [39], i.e., X = MLP(p1, ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 14 (Figure/Table caption) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
