# SSCNet: Semantic Scene Completion from a Single Depth Image

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1611.08974.
> PDF retrieval source: https://arxiv.org/pdf/1611.08974. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2017 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, semantic, occupancy, geometry
- Official paper: https://arxiv.org/abs/1611.08974
- Full-text retrieval: https://arxiv.org/pdf/1611.08974
- Code/Project: https://github.com/shurans/sscnet
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, if we consider the context due to surrounding objects, such as the table and floor, the problem is much easier.를 문제로 두고, To provide the training data for our network, we introduce SUNCG, a manually created large-scale dataset of synthetic 3D scenes with dense occupancy and semantic annotations.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This paper focuses on semantic scene completion, a task for producing a complete 3D voxel representation of volumetric occupancy and semantic labels for a scene ...
- **p. 1 / Abstract - extractive body cue:** Previous work has considered scene completion and semantic labeling of depth maps separately.
- **p. 1 / Abstract - extractive body cue:** However, we observe that these two problems are tightly intertwined.
- **p. 1 / Abstract - extractive body cue:** To leverage the coupled nature of these two tasks, we introduce the semantic scene completion network (SSCNet), an end-to-end 3D convolutional network that takes a ...
- **p. 1 / Abstract - extractive body cue:** Our network uses a dilation-based 3D context module to efficiently expand the receptive field and enable 3D context learning.
- **p. 2 / 1. Introduction - extractive body cue:** However, if we consider the context due to surrounding objects, such as the table and floor, the problem is much easier.
- **p. 2 / 1. Introduction - extractive body cue:** First, how do we effectively capture contextual information from 3D volumetric data, where the signal is sparse and lacks high frequency detail?

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To provide the training data for our network, we introduce SUNCG, a manually created large-scale dataset of synthetic 3D scenes with dense occupancy and semantic ...
- **p. 1 / 1. Introduction - extractive body cue:** Similarly, for a robot, the ability to infer complete 3D shape from partial observations is necessary for low-level tasks such as grasping and obstacle avoidance ...
- **p. 2 / 1. Introduction - extractive body cue:** In support of that goal, we design a dilation-based 3D context module that enables efficient context learning with large receptive fields.
- **p. 5 / 4. Synthesizing training data - extractive body cue:** In this paper, we present a new large-scale synthetic 3D scene dataset, from which we obtain a large amount of training data with synthetically rendered ...
- **p. 5 / 4. Synthesizing training data - extractive body cue:** During the task, we show a set of top view renderings of each floor and ask turkers to vote whether this is a valid apartment ...
- **p. 4 / 3.2. Network architecture - extractive body cue:** Then, we use a dilation-based 3D context module to capture higher-level inter-object contextual information.
- **p. 4 / 3.2. Network architecture - extractive body cue:** Taking a high-resolution 3D volume as input, the network first uses several 3D convolution layers to learn a local geometry representation.
- **p. 5 / 3.2. Network architecture - extractive body cue:** We implement our network architecture in Caffe [10].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (a) Input single-view depth map (b) Visible surface from the depth map; color is for visualization only. | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (1. Introduction), p. 1 (1. Introduction) |
| State/latent | Input, single-view, depth, Visible, surface, color, visualization, only, motivation, goal, have, model | geometry, map, object/relationship state | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 5 (4.2. Synthetic depth map generation) |
| Output/action | With this motivation, our goal is to have a model that predicts both volumetric occupancy (i.e., scene completion) and object category (i.e., scene labeling) from a single depth image of a 3D ... | point map, pose, scene graph, affordance 또는 query result | p. 1 (1. Introduction), p. 5 (4.2. Synthetic depth map generation), p. 4 (3.2. Network architecture) |
| Objective/outcome | The loss function of the network is the sum of voxel-wise softmax loss L(p, y) = P i,j,k wijkLsm(pijk, yijk), where Lsm is softmax loss, yijk is the ground truth label, pijk ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.2. Network architecture), p. 5 (3.2. Network architecture), p. 4 (3.2. Network architecture) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To provide the training data for our network, we introduce SUNCG, a manually created large-scale dataset of synthetic 3D scenes with dense occupancy and semantic ...
- **p. 1 / 1. Introduction - extractive body cue:** Similarly, for a robot, the ability to infer complete 3D shape from partial observations is necessary for low-level tasks such as grasping and obstacle avoidance ...
- **p. 2 / 1. Introduction - extractive body cue:** In support of that goal, we design a dilation-based 3D context module that enables efficient context learning with large receptive fields.
- **p. 5 / 4. Synthesizing training data - extractive body cue:** In this paper, we present a new large-scale synthetic 3D scene dataset, from which we obtain a large amount of training data with synthetically rendered ...
- **p. 5 / 4. Synthesizing training data - extractive body cue:** During the task, we show a set of top view renderings of each floor and ask turkers to vote whether this is a valid apartment ...
- **p. 8 / 5.1. Experimental results - extractive body cue:** Increasing the receptive field gives the network a opportunity to capture richer contextual information and significantly improve the network performance from 38.0% to 44.3%.
- **p. 8 / 5.1. Experimental results - extractive body cue:** We see a performance gain by using additional synthetic data especially for the semantic scene completion task having an 10.3% improvement in IoU.
- **p. 6 / 5.1. Experimental results - extractive body cue:** Therefore, they can achieve perfect alignments by finding the exact mesh model in a small database.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (5.1. Experimental results), p. 8 (5.1. Experimental results) |
| Embodiment/environment | The SUNCG test set consists of 500 depth images rendered from 184 scenes that are not in the training set. | hardware/simulator version and reset protocol | p. 6 (5. Evaluation), p. 6 (5. Evaluation) |
| Dataset/benchmark | We examine to what extent the supervision of object semantics benefits the scene completion task. | role, split, size and leakage | p. 6 (5. Evaluation), p. 6 (5. Evaluation), p. 7 (5.1. Experimental results), p. 7 (5.1. Experimental results) |
| Metric | We see a performance gain by using additional synthetic data especially for the semantic scene completion task having an 10.3% improvement in IoU. | definition, denominator, direction and uncertainty | p. 8 (5.1. Experimental results), p. 6 (5. Evaluation), p. 6 (5. Evaluation) |
| Baseline/ablation | Figure 4. Comparison of receptive fields and voxel sizes between SSCNet and prior work. (a) Object centric networks such as [34] and [20] scale objects into the same 3D voxel grid thus ... | fair input/data/compute/action matching | p. 4 (Figure/Table caption), p. 6 (5. Evaluation), p. 6 (5.1. Experimental results) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5.1. Experimental results - extractive body cue:** While Firman et al. produces good results for many cases, their approach fails when the scene becomes complex.
- **p. 7 / 5.1. Experimental results - extractive body cue:** For instance, their algorithm fails to complete half of the bed in the first row of Figure 7, and also fails to complete the chairs ...
- **p. 6 / 5.1. Experimental results - extractive body cue:** In contrast, our algorithm is based on only depth and does not use additional mesh model at test time.
- **p. 6 / 5.1. Experimental results - extractive body cue:** Moreover, since our method does not require the model fitting step it is much faster at 7s compared to 127s per image [4].
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 5. Different encodings for surface (a). The projective TSDF (b) is computed with respect to the camera and is therefore view-dependent. The accurate TSDF ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, if we consider the context due to surrounding objects, such as the table and floor, the problem is much easier.를 문제로 두고, To provide the training data for our network, we introduce SUNCG, a manually created large-scale dataset of synthetic 3D scenes with dense occupancy and semantic annotations.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.2. Network architecture), p. 4 (3.2. Network architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
