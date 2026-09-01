# PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1612.00593.
> PDF retrieval source: https://arxiv.org/pdf/1612.00593. Reading tracker status/evidence was not changed.

- Year/Venue: 2017 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: CORE
- Tags: 3D geometry, point cloud, representation
- Official paper: https://arxiv.org/abs/1612.00593
- Full-text retrieval: https://arxiv.org/pdf/1612.00593
- Code/Project: https://github.com/charlesq34/pointnet
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The problem of processing unordered sets by neural nets is a very general and fundamental problem - we expect that our ideas can be transferred to other domains as well.를 문제로 두고, The key contributions of our work are as follows: • We design a novel deep net architecture suitable for consuming unordered point sets in 3D; • We show how such a net ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Point cloud is an important type of geometric data structure.
- **p. 1 / Abstract - extractive body cue:** Due to its irregular format, most researchers transform such data to regular 3D voxel grids or collections of images.
- **p. 1 / Abstract - extractive body cue:** This, however, renders data unnecessarily voluminous and causes issues.
- **p. 1 / Abstract - extractive body cue:** In this paper, we design a novel type of neural network that directly consumes point clouds, which well respects the permutation invariance of points in ...
- **p. 1 / Abstract - extractive body cue:** Our network, named PointNet, provides a unified architecture for applications ranging from object classification, part segmentation, to scene semantic parsing.
- **p. 2 / 1. Introduction - extractive body cue:** The problem of processing unordered sets by neural nets is a very general and fundamental problem - we expect that our ideas can be transferred ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** The key contributions of our work are as follows: • We design a novel deep net architecture suitable for consuming unordered point sets in 3D; ...
- **p. 1 / 1. Introduction - extractive body cue:** We propose a novel deep net architecture that consumes raw point cloud (set of points) without voxelization or rendering.
- **p. 1 / 1. Introduction - extractive body cue:** The PointNet, however, * indicates equal contributions. mug? table? car?
- **p. 2 / 1. Introduction - extractive body cue:** We show that our network can approximate any set function that is continuous.
- **p. 4 / 4.2. PointNet Architecture - extractive body cue:** Our input form of point clouds allows us to achieve this goal in a much simpler way compared with [9].
- **p. 4 / 4.2. PointNet Architecture - extractive body cue:** The mininetwork itself resembles the big network and is composed by basic modules of point independent feature extraction, max pooling and fully connected layers.
- **p. 3 / 4.2. PointNet Architecture - extractive body cue:** Our network has three key modules: the max pooling layer as a symmetric function to aggregate information from all the points, a local and global ...
- **p. 4 / 4.2. PointNet Architecture - extractive body cue:** Then we extract new per point features based on the combined point features - this time the per point feature is aware of both the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our PointNet is a unified architecture that directly takes point clouds as input and outputs either class labels for the entire input or per point segment/part labels for each point of the ... | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (1. Introduction), p. 3 (3. Problem Statement) |
| State/latent | PointNet, unified, architecture, directly, takes, point, clouds, input, outputs, either, class, labels | geometry, map, object/relationship state | p. 1 (1. Introduction), p. 3 (3. Problem Statement), p. 2 (3. Problem Statement) |
| Output/action | input points point features output scores max pool shared shared shared nx3 nx3 nx64 nx64 nx1024 1024 n x 1088 nx128 mlp (64,64) mlp (64,128,1024) input transform feature transform mlp (512,256,k) global ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3. Problem Statement), p. 2 (3. Problem Statement), p. 3 (4.2. PointNet Architecture) |
| Objective/outcome | We therefore add a regularization term to our softmax training loss. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (4.2. PointNet Architecture), p. 4 (4.2. PointNet Architecture) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** The key contributions of our work are as follows: • We design a novel deep net architecture suitable for consuming unordered point sets in 3D; ...
- **p. 1 / 1. Introduction - extractive body cue:** We propose a novel deep net architecture that consumes raw point cloud (set of points) without voxelization or rendering.
- **p. 1 / 1. Introduction - extractive body cue:** The PointNet, however, * indicates equal contributions. mug? table? car?
- **p. 2 / 1. Introduction - extractive body cue:** We show that our network can approximate any set function that is continuous.
- **p. 4 / 4.2. PointNet Architecture - extractive body cue:** Our input form of point clouds allows us to achieve this goal in a much simpler way compared with [9].
- **p. 7 / 5.1. Applications - extractive body cue:** Results are shown in Table 3, where our PointNet method significantly outperforms the baseline method.
- **p. 5 / 5.1. Applications - extractive body cue:** Even though we are working on a brand new data representation (point sets), we are able to achieve comparable or even better performance on benchmarks ...
- **p. 6 / 5.1. Applications - extractive body cue:** Our model achieved state-of-the-art performance among methods based on 3D input (volumetric and point cloud).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 7 (5.1. Applications), p. 5 (5.1. Applications) |
| Embodiment/environment | Even though we are working on a brand new data representation (point sets), we are able to achieve comparable or even better performance on benchmarks for several tasks. | hardware/simulator version and reset protocol | p. 5 (5.1. Applications), p. 6 (5.1. Applications) |
| Dataset/benchmark | Semantic Segmentation in Scenes Our network on part segmentation can be easily extended to semantic scene segmentation, where point labels become semantic object classes instead of object part labels. | role, split, size and leakage | p. 5 (5.1. Applications), p. 6 (5.1. Applications), p. 6 (5.1. Applications), p. 5 (5.1. Applications) |
| Metric | In Table 2, we report per-category and mean IoU(%) scores. | definition, denominator, direction and uncertainty | p. 6 (5.1. Applications), p. 6 (5.1. Applications), p. 12 (Figure/Table caption) |
| Baseline/ablation | Results are shown in Table 3, where our PointNet method significantly outperforms the baseline method. | fair input/data/compute/action matching | p. 7 (5.1. Applications), p. 7 (5.2. Architecture Design Analysis), p. 6 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 18 / Figure/Table caption - extractive body cue:** Figure 23. PointNet segmentation failure cases. In this figure, we summarize six types of common errors in our segmentation application. The prediction and the ground-truth ...
- **p. 8 / 5.3. Visualizing PointNet - extractive body cue:** While critical points jointly determine the global shape feature for a given shape, any point cloud that falls between the critical points set and the ...
- **p. 8 / 5.3. Visualizing PointNet - extractive body cue:** CS and NS reflect the robustness of PointNet, meaning that losing some non-critical points does not change the global shape signature f(S) at all.
- **p. 5 / 4.3. Theoretical Analysis - extractive body cue:** Combined with the continuity of h, this explains the robustness of our model w.r.t point perturbation, corruption and extra noise points.
- **p. 7 / 5.1. Applications - extractive body cue:** Our network is able to output smooth predictions and is robust to missing points and occlusions.
- **p. 5 / 4.3. Theoretical Analysis - extractive body cue:** The robustness is gained in analogy to the sparsity principle in machine learning models.
- **p. 6 / 5.1. Applications - extractive body cue:** We also perform experiments on simulated Kinect scans to test the robustness of these methods.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The problem of processing unordered sets by neural nets is a very general and fundamental problem - we expect that our ideas can be transferred to other domains as well.를 문제로 두고, The key contributions of our work are as follows: • We design a novel deep net architecture suitable for consuming unordered point sets in 3D; • We show how such a net ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 4 (4.2. PointNet Architecture), p. 3 (4.2. PointNet Architecture), p. 4 (4.2. PointNet Architecture), p. 3 (4.2. PointNet Architecture), p. 7 (5.1. Applications) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
