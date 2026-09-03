# CenterPoint: Center-based 3D Object Detection and Tracking

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2006.11275.
> PDF retrieval source: https://arxiv.org/pdf/2006.11275. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: point cloud, 3D Vision
- Official paper: https://arxiv.org/abs/2006.11275
- Full-text retrieval: https://arxiv.org/pdf/2006.11275
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, during a safety-critical left turn (bottom), anchor-based methods have difficulty fitting axisaligned bounding boxes to rotated objects.를 문제로 두고, These marked differences between 2D and 3D detection made a transfer of ideas bea) Anchor-based t=1 c) Anchor-based t=2 b) Center-based t=1 d) Center-based t=2 Figure 1: We present a center-based framework ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Three-dimensional objects are commonly represented as 3D boxes in a point-cloud.
- **p. 1 / Abstract - extractive body cue:** This representation mimics the well-studied image-based 2D bounding-box detection but comes with additional challenges.
- **p. 1 / Abstract - extractive body cue:** Objects in a 3D world do not follow any particular orientation, and box-based detectors have difficulties enumerating all orientations or fitting an axis-aligned bounding box ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we instead propose to represent, detect, and track 3D objects as points.
- **p. 1 / Abstract - extractive body cue:** Our framework, CenterPoint, first detects centers of objects using a keypoint detector and regresses to other attributes, including 3D size, 3D orientation, and velocity.
- **p. 1 / 1. Introduction - extractive body cue:** However, during a safety-critical left turn (bottom), anchor-based methods have difficulty fitting axisaligned bounding boxes to rotated objects.
- **p. 1 / 1. Introduction - extractive body cue:** Compared to the wellstudied 2D detection problem, 3D detection on point-clouds offers a series of interesting challenges: First, point-clouds are sparse, and most regions of ...

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** These marked differences between 2D and 3D detection made a transfer of ideas bea) Anchor-based t=1 c) Anchor-based t=2 b) Center-based t=1 d) Center-based t=2 ...
- **p. 3 / 3. Preliminaries - extractive body cue:** We introduce a novel center-based detection head but rely on existing 3D backbones (VoxelNet or PointPillars).
- **p. 2 / 1. Introduction - extractive body cue:** Thirdly, point-based feature extraction enables us to design an effective two-stage refinement module that is much faster than previous approaches [44-46].
- **p. 1 / Abstract - extractive body cue:** Our framework, CenterPoint, first detects centers of objects using a keypoint detector and regresses to other attributes, including 3D size, 3D orientation, and velocity.
- **p. 3 / 3. Preliminaries - extractive body cue:** Each bounding box b = (u, v, d, w, l, h, α) consists of a center location (u, v, d), relative to the objects ground ...
- **p. 3 / 3. Preliminaries - extractive body cue:** The 3D encoder then pools these features into its primary feature representation.
- **p. 3 / 3. Preliminaries - extractive body cue:** A point-based network [40] then extracts features for all points inside a bin.
- **p. 4 / 4. CenterPoint - extractive body cue:** Then, a 2D CNN architecture detection head finds object centers and regress to full 3D bounding boxes using center features.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It takes an input image and predicts a w × h heatmap ˆY ∈[0, 1]w×h×K for each of K classes. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3. Preliminaries), p. 3 (3. Preliminaries) |
| State/latent | takes, input, image, predicts, heatmap, classes, output, backbone, network, map-view, feature-map, width | geometry, map, object/relationship state | p. 3 (3. Preliminaries), p. 3 (3. Preliminaries), p. 4 (4. CenterPoint) |
| Output/action | The output of a backbone network is a map-view feature-map M ∈RW ×L×F of width W and length L with F channels in a map-view reference frame. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3. Preliminaries), p. 4 (4. CenterPoint), p. 4 (4.1. Two-Stage CenterPoint) |
| Objective/outcome | CenterPoint combines all heatmap and regression losses in one common objective and jointly optimizes them. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (4. CenterPoint), p. 4 (4.1. Two-Stage CenterPoint), p. 2 (1. Introduction) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** These marked differences between 2D and 3D detection made a transfer of ideas bea) Anchor-based t=1 c) Anchor-based t=2 b) Center-based t=1 d) Center-based t=2 ...
- **p. 3 / 3. Preliminaries - extractive body cue:** We introduce a novel center-based detection head but rely on existing 3D backbones (VoxelNet or PointPillars).
- **p. 2 / 1. Introduction - extractive body cue:** Thirdly, point-based feature extraction enables us to design an effective two-stage refinement module that is much faster than previous approaches [44-46].
- **p. 1 / Abstract - extractive body cue:** Our framework, CenterPoint, first detects centers of objects using a keypoint detector and regresses to other attributes, including 3D size, 3D orientation, and velocity.
- **p. 3 / 3. Preliminaries - extractive body cue:** Each bounding box b = (u, v, d, w, l, h, α) consists of a center location (u, v, d), relative to the objects ground ...
- **p. 6 / 5.1. Main Results - extractive body cue:** More importantly, our model significantly outperforms all other submissions under the neural planar metric (PKL), a hidden metric evaluated by the organizers after our leaderboard ...
- **p. 6 / 5.1. Main Results - extractive body cue:** Our velocity-based closest distance matching described in Section 4 significantly outperforms the official tracking baseline in the Waymo paper [48], which uses a Kalman-filter based ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 14: Ablation studies for 3D detection on nuScenes validation. entries in the NeurIPS 2020 nuScenes detection challenge. In this section, we describe the details ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (5.1. Main Results), p. 6 (5.1. Main Results) |
| Embodiment/environment | CenterPoint-Voxel uses a (0.1m, 0.1m, 0.15m) voxel size following PV-RCNN [44] while CenterPoint-Pillar uses a grid size of (0.32m, 0.32m). nuScenes Dataset. nuScenes [6] contains 1000 driving sequences, with 700, 150, 150 ... | hardware/simulator version and reset protocol | p. 5 (5. Experiments), p. 5 (5. Experiments) |
| Dataset/benchmark | We think the reason is that the nuScenes dataset uses 32 lanes Lidar, which produces about 30k Lidar points per frame, about 1 6 of the number of points in the Waymo ... | role, split, size and leakage | p. 5 (5. Experiments), p. 5 (5. Experiments), p. 7 (5.2. Ablation studies), p. 7 (5.2. Ablation studies) |
| Metric | Figure 2: Overview of our CenterPoint framework. We rely on a standard 3D backbone that extracts map-view feature representation from Lidar point-clouds. Then, a 2D CNN architecture detection head finds object centers ... | definition, denominator, direction and uncertainty | p. 4 (Figure/Table caption), p. 5 (5. Experiments), p. 5 (5. Experiments) |
| Baseline/ablation | Our velocity-based closest distance matching described in Section 4 significantly outperforms the official tracking baseline in the Waymo paper [48], which uses a Kalman-filter based tracker [53]. | fair input/data/compute/action matching | p. 6 (5.1. Main Results), p. 6 (5.1. Main Results), p. 8 (5.2. Ablation studies) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 5.1. Main Results - extractive body cue:** Notably, our tracking does not require a separate motion model and runs in a negligible time, 1ms on top of detection.
- **p. 7 / 5.2. Ablation studies - extractive body cue:** Two-stage refinement does not bring an improvement over the single-stage CenterPoint model on nuScenes in our experiments.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, during a safety-critical left turn (bottom), anchor-based methods have difficulty fitting axisaligned bounding boxes to rotated objects.를 문제로 두고, These marked differences between 2D and 3D detection made a transfer of ideas bea) Anchor-based t=1 c) Anchor-based t=2 b) Center-based t=1 d) Center-based t=2 Figure 1: We present a center-based framework ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries), p. 2 (1. Introduction), p. 3 (3. Preliminaries) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
