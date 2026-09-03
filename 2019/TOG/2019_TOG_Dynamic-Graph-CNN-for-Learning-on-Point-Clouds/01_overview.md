# Dynamic Graph CNN for Learning on Point Clouds

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1801.07829.
> PDF retrieval source: https://arxiv.org/pdf/1801.07829. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / TOG
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: point cloud, 3D Vision
- Official paper: https://arxiv.org/abs/1801.07829
- Full-text retrieval: https://arxiv.org/pdf/1801.07829
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This independence, however, neglects the geometric relationships among points, presenting a fundamental limitation that cannot capture local features.를 문제로 두고, We summarize the key contributions of our work as follows: • We present a novel operation for learning from point clouds, EdgeConv, to better capture local geometric features of point clouds while ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Point clouds, or scattered collections of points in 2D or 3D, are arguably the simplest shape representation; they also comprise the output of 3D sensing ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** With the advent of fast 3D point cloud acquisition, recent pipelines for graphics and vision often process point clouds directly, bypassing expensive mesh reconstruction or ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** A few of the many recent applications of point cloud processing and analysis include indoor navigation [Zhu et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 2017], self-driving vehicles [Liang et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 2008b], and shape synthesis and modeling [Golovinskiy et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This independence, however, neglects the geometric relationships among points, presenting a fundamental limitation that cannot capture local features.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This approach, however, usually introduces quantization artifacts and excessive memory usage, making it difficult to go to capture high-resolution or fine-grained features.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We summarize the key contributions of our work as follows: • We present a novel operation for learning from point clouds, EdgeConv, to better capture ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these drawbacks, we propose a novel simple operation, called EdgeConv, which captures local geometric structure while maintaining permutation invariance.
- **p. 1 / Body text (section not recovered) - extractive body cue:** To this end, we propose a new neural network module dubbed EdgeConv suitable for CNN-based high-level tasks on point clouds including classification and segmentation.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We show the performance of our model on standard benchmarks including ModelNet40, ShapeNetPart, and S3DIS.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** One common approach to process point cloud data using deep learning models is to first convert raw point cloud data into a volumetric representation, namely ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 2017]; these allow the network to exploit local features, improving upon performance of the basic model.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Bottom: schematic neural network architecture.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Point clouds provide a flexible geometric representation suitable for countless applications in computer graphics; they also comprise the raw output of most 3D data acquisition devices. | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (Body text (section not recovered)), p. 2 (1 INTRODUCTION) |
| State/latent | Point, clouds, provide, flexible, geometric, representation, suitable, countless, applications, computer, graphics, they | geometry, map, object/relationship state | p. 1 (Body text (section not recovered)), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/action | State-of-the-art deep neural networks are designed specifically to handle the irregularity of point clouds, directly manipulating raw point cloud data rather than passing to an intermediate regular representation. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (Body text (section not recovered)) |
| Objective/outcome | Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 1 (Body text (section not recovered)) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** We summarize the key contributions of our work as follows: • We present a novel operation for learning from point clouds, EdgeConv, to better capture ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these drawbacks, we propose a novel simple operation, called EdgeConv, which captures local geometric structure while maintaining permutation invariance.
- **p. 1 / Body text (section not recovered) - extractive body cue:** To this end, we propose a new neural network module dubbed EdgeConv suitable for CNN-based high-level tasks on point clouds including classification and segmentation.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We show the performance of our model on standard benchmarks including ModelNet40, ShapeNetPart, and S3DIS.
- **p. 7 / 4 EVALUATION - extractive body cue:** Our model achieves the best results on this dataset.
- **p. 7 / 4 EVALUATION - extractive body cue:** Our baseline model using the fixed k-NN graph outperforms the previous state-of-the-art PointNet++ by 1.0% accuracy, at the same time being 7 times faster.
- **p. 8 / 4 EVALUATION - extractive body cue:** Using more points further improves the overall accuracy by 0.6%.
- **p. 8 / 4 EVALUATION - extractive body cue:** Explicitly centralizing each patch by using the concatenation of xi and xi -xj leads to about 0.5% improvement for overall accuracy.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4 EVALUATION), p. 7 (4 EVALUATION) |
| Embodiment/environment | The dataset contains 16,881 3D shapes from 16 object categories, annotated with 50 parts in total. | hardware/simulator version and reset protocol | p. 8 (4 EVALUATION), p. 8 (4 EVALUATION) |
| Dataset/benchmark | Our model achieves the best results on this dataset. | role, split, size and leakage | p. 8 (4 EVALUATION), p. 8 (4 EVALUATION), p. 7 (4 EVALUATION), p. 7 (4 EVALUATION) |
| Metric | Mean overall IoU accuracy PointNet (baseline) [Qi et al. | definition, denominator, direction and uncertainty | p. 10 (4 EVALUATION), p. 7 (4 EVALUATION), p. 7 (4 EVALUATION) |
| Baseline/ablation | Our baseline model using the fixed k-NN graph outperforms the previous state-of-the-art PointNet++ by 1.0% accuracy, at the same time being 7 times faster. | fair input/data/compute/action matching | p. 7 (4 EVALUATION), p. 7 (4 EVALUATION), p. 8 (4 EVALUATION) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4 EVALUATION - extractive body cue:** This confirms our hypothesis that for certain density, with large k the Euclidean distance fails to approximate geodesic distance, destroying the geometry of each patch.
- **p. 8 / 4 EVALUATION - extractive body cue:** We further evaluate the robustness of our model (trained on 1,024 points with k = 20) to point cloud density.
- **p. 9 / 4 EVALUATION - extractive body cue:** Our model is robust to partial data.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This independence, however, neglects the geometric relationships among points, presenting a fundamental limitation that cannot capture local features.를 문제로 두고, We summarize the key contributions of our work as follows: • We present a novel operation for learning from point clouds, EdgeConv, to better capture local geometric features of point clouds while ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (Body text (section not recovered)), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (Body text (section not recovered)) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
