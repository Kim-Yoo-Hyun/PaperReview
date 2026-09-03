# PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1706.02413.
> PDF retrieval source: https://arxiv.org/pdf/1706.02413. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2017 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D geometry, point cloud, representation
- Official paper: https://arxiv.org/abs/1706.02413
- Full-text retrieval: https://arxiv.org/pdf/1706.02413
- Code/Project: https://github.com/charlesq34/pointnet2
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Deciding the appropriate scale of local neighborhood balls, however, is a more challenging yet intriguing problem, due to the entanglement of feature scale and non-uniformity of input point set.를 문제로 두고, We introduce a hierarchical neural network, named as PointNet++, to process a set of points sampled in a metric space in a hierarchical fashion.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Few prior works study deep learning on point sets.
- **p. 1 / Abstract - extractive body cue:** PointNet [20] is a pioneer in this direction.
- **p. 1 / Abstract - extractive body cue:** However, by design PointNet does not capture local structures induced by the metric space points live in, limiting its ability to recognize fine-grained patterns and ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce a hierarchical neural network that applies PointNet recursively on a nested partitioning of the input point set.
- **p. 1 / Abstract - extractive body cue:** By exploiting metric space distances, our network is able to learn local features with increasing contextual scales.
- **p. 2 / 1 Introduction - extractive body cue:** Deciding the appropriate scale of local neighborhood balls, however, is a more challenging yet intriguing problem, due to the entanglement of feature scale and non-uniformity ...
- **p. 2 / 1 Introduction - extractive body cue:** 2 Problem Statement Suppose that X = (M, d) is a discrete metric space whose metric is inherited from a Euclidean space Rn, where M ...

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** We introduce a hierarchical neural network, named as PointNet++, to process a set of points sampled in a metric space in a hierarchical fashion.
- **p. 2 / 3 Method - extractive body cue:** Finally, we propose our PointNet++ that is able to robustly learn features even in non-uniformly sampled point sets (Sec.
- **p. 3 / 3 Method - extractive body cue:** We introduce the layers of a set abstraction level in the following paragraphs.
- **p. 3 / 3 Method - extractive body cue:** In convolutional neural networks, a local region of a pixel consists of pixels with array indices within certain Manhattan distance (kernel size) of the pixel.
- **p. 4 / 3 Method - extractive body cue:** To achieve this goal we propose density adaptive PointNet layers (Fig.
- **p. 7 / Method - extractive body cue:** We use these features as input and then sample and group points according to the underlying metric space.
- **p. 5 / 3 Method - extractive body cue:** The interpolated features on Nl-1 points are then concatenated with skip linked point features from the set abstraction level.
- **p. 3 / 3 Method - extractive body cue:** Our hierarchical structure is composed by a number of set abstraction levels (Fig.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In a feature propagation level, we propagate point features from Nl × (d + C) points to Nl-1 points where Nl-1 and Nl (with Nl ≤Nl-1) are point set size of input ... | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3 Method), p. 3 (3 Method) |
| State/latent | feature, propagation, level, propagate, point, features, points, Nl-1, where, size, input, output | geometry, map, object/relationship state | p. 5 (3 Method), p. 3 (3 Method), p. 3 (3 Method) |
| Output/action | A set abstraction level takes an N × (d + C) matrix as input that is from N points with d-dim coordinates and C-dim point feature. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3 Method), p. 3 (3 Method), p. 2 (1 Introduction) |
| Objective/outcome | In particular, since the number of centroid points is usually quite large at the lowest level, the time cost is significant. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3 Method), p. 5 (3 Method), p. 6 (Method) |

## Main Claims and Actual Contribution

- **p. 1 / 1 Introduction - extractive body cue:** We introduce a hierarchical neural network, named as PointNet++, to process a set of points sampled in a metric space in a hierarchical fashion.
- **p. 2 / 3 Method - extractive body cue:** Finally, we propose our PointNet++ that is able to robustly learn features even in non-uniformly sampled point sets (Sec.
- **p. 3 / 3 Method - extractive body cue:** We introduce the layers of a set abstraction level in the following paragraphs.
- **p. 3 / 3 Method - extractive body cue:** In convolutional neural networks, a local region of a pixel consists of pixels with array indices within certain Manhattan distance (kernel size) of the pixel.
- **p. 4 / 3 Method - extractive body cue:** To achieve this goal we propose density adaptive PointNet layers (Fig.
- **p. 5 / 4 Experiments - extractive body cue:** Firstly, our hierarchical learning architecture achieves significantly better performance than the non-hierarchical PointNet [20].
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Left: Point cloud with random point dropout. Right: Curve showing advantage of our density adaptive strategy in dealing with non-uniform density. DP means ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Illustration of our hierarchical feature learning architecture and its application for set segmentation and classification using points in 2D Euclidean space as an ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (4 Experiments), p. 6 (Figure/Table caption) |
| Embodiment/environment | We use five fold cross validation to acquire classification accuracy on this dataset. • ScanNet: 1513 scanned and reconstructed indoor scenes. | hardware/simulator version and reset protocol | p. 5 (4 Experiments), p. 5 (4 Experiments) |
| Dataset/benchmark | We use five fold cross validation to acquire classification accuracy on this dataset. • ScanNet: 1513 scanned and reconstructed indoor scenes. | role, split, size and leakage | p. 5 (4 Experiments), p. 5 (4 Experiments) |
| Metric | In MNIST, we see a relative 60.8% and 34.6% error rate reduction 1See supplementary for more details on network architecture and experiment preparation. | definition, denominator, direction and uncertainty | p. 5 (4 Experiments), p. 6 (Figure/Table caption), p. 5 (4 Experiments) |
| Baseline/ablation | Figure 5: Scannet labeling accuracy. To validate that our approach is suitable for large scale point cloud analysis, we also evaluate on semantic scene labeling task. The goal is to pre- dict ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 14 (Figure/Table caption), p. 13 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Scannet labeling results. [20] cap- tures the overall layout of the room correctly but fails to discover the furniture. Our ap- proach, in ...
- **p. 5 / 4 Experiments - extractive body cue:** Note that PointNet (vanilla) in Table 2 is the the version in [20] that does not use transformation networks, which is equivalent to our hierarchical ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Deciding the appropriate scale of local neighborhood balls, however, is a more challenging yet intriguing problem, due to the entanglement of feature scale and non-uniformity of input point set.를 문제로 두고, We introduce a hierarchical neural network, named as PointNet++, to process a set of points sampled in a metric space in a hierarchical fashion.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 7 (Method), p. 5 (3 Method), p. 2 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
