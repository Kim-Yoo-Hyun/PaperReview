# VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1711.06396.
> PDF retrieval source: https://arxiv.org/pdf/1711.06396. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2018 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, LiDAR, 3D detection, sensor fusion
- Official paper: https://arxiv.org/abs/1711.06396
- Full-text retrieval: https://arxiv.org/pdf/1711.06396
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these manual design choices introduce an information bottleneck that prevents these approaches from effectively exploiting 3D shape information and the required invariances for the detection task.를 문제로 두고, • We propose a novel end-to-end trainable deep architecture for point-cloud-based 3D detection, VoxelNet, that directly operates on sparse 3D points and avoids information bottlenecks introduced by manual feature engineering. • We ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Accurate detection of objects in 3D point clouds is a central problem in many applications, such as autonomous navigation, housekeeping robots, and augmented/virtual reality.
- **p. 1 / Abstract - extractive body cue:** To interface a highly sparse LiDAR point cloud with a region proposal network (RPN), most existing efforts have focused on hand-crafted feature representations, for example, ...
- **p. 1 / Abstract - extractive body cue:** In this work, we remove the need of manual feature engineering for 3D point clouds and propose VoxelNet, a generic 3D detection network that unifies ...
- **p. 1 / Abstract - extractive body cue:** Specifically, VoxelNet divides a point cloud into equally spaced 3D voxels and transforms a group of points within each voxel into a unified feature representation ...
- **p. 1 / Abstract - extractive body cue:** In this way, the point cloud is encoded as a descriptive volumetric representation, which is then connected to a RPN to generate detections.
- **p. 1 / 1. Introduction - extractive body cue:** However, these manual design choices introduce an information bottleneck that prevents these approaches from effectively exploiting 3D shape information and the required invariances for the ...
- **p. 1 / 1. Introduction - extractive body cue:** To handle these challenges, many approaches manually crafted feature represenFigure 1.

## Core Idea

- **p. 3 / 1.2. Contributions - extractive body cue:** • We propose a novel end-to-end trainable deep architecture for point-cloud-based 3D detection, VoxelNet, that directly operates on sparse 3D points and avoids information bottlenecks ...
- **p. 2 / 1. Introduction - extractive body cue:** We design a novel voxel feature encoding (VFE) layer, which enables inter-point interaction within a voxel, by combining point-wise features with a locally aggregated feature.
- **p. 2 / 1. Introduction - extractive body cue:** We present VoxelNet, a generic 3D detection framework that simultaneously learns a discriminative feature representation from point clouds and predicts accurate 3D bounding boxes, in ...
- **p. 3 / 2.1. VoxelNet Architecture - extractive body cue:** The proposed VoxelNet consists of three functional blocks: (1) Feature learning network, (2) Convolutional middle layers, and (3) Region proposal network [32], as illustrated in ...
- **p. 4 / 2.1. VoxelNet Architecture - extractive body cue:** Because the output feature combines both point-wise features and locally aggregated feature, stacking VFE layers encodes point interactions within a voxel and enables the final ...
- **p. 3 / 2.1. VoxelNet Architecture - extractive body cue:** After obtaining point-wise feature representations, we use element-wise MaxPooling across all fi associated to V to get the locally aggregated feature ˜f ∈Rm for V.
- **p. 6 / 3.1. Network Details - extractive body cue:** During training, we use stochastic gradient descent (SGD) with learning rate 0.01 for the first 150 epochs and decrease the learning rate to 0.001 for ...
- **p. 4 / 2.1. VoxelNet Architecture - extractive body cue:** We use VFE-i(cin, cout) to represent the i-th VFE layer that transforms input features of dimension cin into output features of dimension cout.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Several methods project point clouds into a perspective view and apply image-based feature extraction techniques [28, 15, 22]. | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (1. Introduction), p. 4 (2.1. VoxelNet Architecture) |
| State/latent | Several, methods, project, point, clouds, perspective, view, apply, image-based, feature, extraction, techniques | geometry, map, object/relationship state | p. 1 (1. Introduction), p. 4 (2.1. VoxelNet Architecture), p. 4 (2.1. VoxelNet Architecture) |
| Output/action | We use VFE-i(cin, cout) to represent the i-th VFE layer that transforms input features of dimension cin into output features of dimension cout. | point map, pose, scene graph, affordance 또는 query result | p. 4 (2.1. VoxelNet Architecture), p. 4 (2.1. VoxelNet Architecture), p. 1 (1. Introduction) |
| Objective/outcome | The first two terms are the normalized classification loss for {apos i }i=1...Npos and {aneg j }j=1...Nneg, where the Lcls stands for binary cross entropy loss and α, β are postive constants ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (2.2. Loss Function), p. 5 (2.2. Loss Function), p. 6 (3.1. Network Details) |

## Main Claims and Actual Contribution

- **p. 3 / 1.2. Contributions - extractive body cue:** • We propose a novel end-to-end trainable deep architecture for point-cloud-based 3D detection, VoxelNet, that directly operates on sparse 3D points and avoids information bottlenecks ...
- **p. 2 / 1. Introduction - extractive body cue:** We design a novel voxel feature encoding (VFE) layer, which enables inter-point interaction within a voxel, by combining point-wise features with a locally aggregated feature.
- **p. 2 / 1. Introduction - extractive body cue:** We present VoxelNet, a generic 3D detection framework that simultaneously learns a discriminative feature representation from point clouds and predicts accurate 3D bounding boxes, in ...
- **p. 3 / 2.1. VoxelNet Architecture - extractive body cue:** The proposed VoxelNet consists of three functional blocks: (1) Feature learning network, (2) Convolutional middle layers, and (3) Region proposal network [32], as illustrated in ...
- **p. 4 / 2.1. VoxelNet Architecture - extractive body cue:** Because the output feature combines both point-wise features and locally aggregated feature, stacking VFE layers encodes point interactions within a voxel and enables the final ...
- **p. 7 / 4.1. Evaluation on KITTI Validation Set - extractive body cue:** Specifically, using only LiDAR, VoxelNet significantly outperforms the
- **p. 7 / 4.1. Evaluation on KITTI Validation Set - extractive body cue:** For the class Car, VoxelNet significantly outperforms all other approaches in AP across all difficulty levels.
- **p. 8 / 4.2. Evaluation on KITTI Test Set - extractive body cue:** VoxelNet, significantly outperforms the previously published state-of-the-art [5] in all the tasks (bird's eye view and 3D detection) and all difficulties.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.1. Evaluation on KITTI Validation Set), p. 7 (4.1. Evaluation on KITTI Validation Set) |
| Embodiment/environment | We evaluate VoxelNet on the KITTI 3D object detection benchmark [11] which contains 7,481 training images/point clouds and 7,518 test images/point clouds, covering three categories: Car, Pedestrian, and Cyclist. | hardware/simulator version and reset protocol | p. 6 (4. Experiments), p. 6 (4. Experiments) |
| Dataset/benchmark | We would like to note that [21] reported 88.9%, 77.3%, and 72.7% for easy, moderate, and hard levels respectively, but these results are obtained based on a different split of 6,000 training ... | role, split, size and leakage | p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.1. Evaluation on KITTI Validation Set), p. 8 (4.2. Evaluation on KITTI Test Set) |
| Metric | The IoU threshold is the same for both bird's eye view and full 3D evaluation. | definition, denominator, direction and uncertainty | p. 7 (4.1. Evaluation on KITTI Validation Set), p. 7 (4.1. Evaluation on KITTI Validation Set), p. 8 (4.1. Evaluation on KITTI Validation Set) |
| Baseline/ablation | HC-baseline also achieves satisfactory performance compared to the state-of-the-art [5], which shows that our base region proposal network (RPN) is effective. | fair input/data/compute/action matching | p. 7 (4.1. Evaluation on KITTI Validation Set), p. 8 (4.2. Evaluation on KITTI Test Set), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** Future work includes extending VoxelNet for joint LiDAR and image based end-to-end 3D detection to further improve detection and localization accuracy.
- **p. 6 / 4. Experiments - extractive body cue:** For each class, detection outcomes are evaluated based on three difficulty levels: easy, moderate, and hard, which are determined according to the object size, occlusion ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these manual design choices introduce an information bottleneck that prevents these approaches from effectively exploiting 3D shape information and the required invariances for the detection task.를 문제로 두고, • We propose a novel end-to-end trainable deep architecture for point-cloud-based 3D detection, VoxelNet, that directly operates on sparse 3D points and avoids information bottlenecks introduced by manual feature engineering. • We ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1.2. Contributions), p. 3 (2.1. VoxelNet Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
