# PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1706.02413.
> PDF retrieval source: https://arxiv.org/pdf/1706.02413. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2017 / NeurIPS
- Authors: Charles Ruizhongtai Qi, Li Yi, Hao Su, Leonidas Guibas
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D geometry, point cloud, representation, 3D segmentation
- Official paper: https://arxiv.org/abs/1706.02413
- Full-text retrieval: https://arxiv.org/pdf/1706.02413
- Code/Project: https://github.com/charlesq34/pointnet2
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

PointNet++는 점군을 국소 이웃으로 묶고 여러 공간 규모의 특징을 계층적으로 집계한다.

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

| 항목 | 원문에서 확인한 범위 |
|---|---|
| 입력 | 좌표와 선택적 점 속성으로 구성한 점 집합 |
| 표현 | 국소 이웃에서 묶은 여러 해상도의 점 특징 |
| 출력 | 형상 범주 또는 점별 의미 라벨 |
| 평가 | ModelNet40 분류와 ScanNet 점 분할 정확도 |

[방법 3쪽](https://proceedings.neurips.cc/paper_files/paper/2017/file/d8bf84be3800d12f74d8b05e9b89836f-Paper.pdf#page=3) · [평가 7쪽](https://proceedings.neurips.cc/paper_files/paper/2017/file/d8bf84be3800d12f74d8b05e9b89836f-Paper.pdf#page=7)

## Main Claims and Actual Contribution

- 거리 공간에서 점을 표집하고 이웃마다 PointNet을 적용한다.
- 점 밀도가 일정하지 않은 조건에서 다중 규모 특징의 효과를 비교한다.

[저자 원문](https://proceedings.neurips.cc/paper_files/paper/2017/hash/d8bf84be3800d12f74d8b05e9b89836f-Abstract.html)

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

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 1 (1 Introduction), p. 7 (Method), p. 5 (3 Method), p. 2 (3 Method)이다.

## 검색 태그 근거

점 좌표의 국소 이웃을 계층적으로 묶고 밀도 차이에 대처하기 위해 여러 스케일의 특징을 합친다. ModelNet40 분류와 ScanNet 점 분할로 평가했다. [원문 3쪽](https://proceedings.neurips.cc/paper_files/paper/2017/file/d8bf84be3800d12f74d8b05e9b89836f-Paper.pdf#page=3) · [원문 7쪽](https://proceedings.neurips.cc/paper_files/paper/2017/file/d8bf84be3800d12f74d8b05e9b89836f-Paper.pdf#page=7)
