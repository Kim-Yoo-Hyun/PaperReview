# SMORE: Simultaneous Map and Object REconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/.
> PDF retrieval source: https://openreview.net/attachment?id=1NhnG9BvQB&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, 3D Vision
- Official paper: https://3dvconf.github.io/2025/accepted-papers/
- Full-text retrieval: https://openreview.net/attachment?id=1NhnG9BvQB&name=pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, investment in autonomous driving has created a new mode of depth capture - spinning LiDAR sensors atop moving vehicles - which is largely unaddressed by the existing research.를 문제로 두고, An example of the depth maps produced by our method is shown in Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present a method for dynamic surface reconstruction of large-scale urban scenes from LiDAR.
- **p. 1 / Abstract - extractive body cue:** Depth-based reconstructions tend to focus on small-scale objects or largescale SLAM reconstructions that treat moving objects as outliers.
- **p. 1 / Abstract - extractive body cue:** We take a holistic perspective and optimize a compositional model of a dynamic scene that decomposes the world into rigidly-moving objects and the background.
- **p. 1 / Abstract - extractive body cue:** To achieve this, we take inspiration from recent novel view synthesis methods and frame the reconstruction problem as a global optimization over neural surfaces, ego ...
- **p. 1 / Abstract - extractive body cue:** In contrast to view synthesis methods, which typically minimize 2D errors with gradient descent, we minimize a 3D point-to-surface error by coordinate descent, which we ...
- **p. 1 / 1. Introduction - extractive body cue:** However, investment in autonomous driving has created a new mode of depth capture - spinning LiDAR sensors atop moving vehicles - which is largely unaddressed ...
- **p. 1 / 1. Introduction - extractive body cue:** This problem has been widely studied in the context of handheld RGB-D sensors capturing humanscale scenes [23, 29, 44, 48].

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** An example of the depth maps produced by our method is shown in Fig.
- **p. 2 / 1. Introduction - extractive body cue:** We introduce a global optimization that refines both ego and object poses so as to minimize a scan-to-surface reconstruction error, dramatically improving results (right).
- **p. 4 / 4.1. Decomposition - extractive body cue:** Our approach consists of applying coordinate descent to Equation (2): alternating between fixing the poses to optimize surfaces and then fixing the surfaces to optimize ...
- **p. 4 / 4. Objective - extractive body cue:** Our method aims to find the surfaces and object motions that best explain the LiDAR measurements.
- **p. 1 / 1. Introduction - extractive body cue:** In contrast, recent novel view synthesis methods have modeled AV scenes with a composition of rigid models [24, 33, 34, 43].
- **p. 4 / 4.1. Decomposition - extractive body cue:** The first step of both derivations decomposes the objective across objects.
- **p. 4 / 4.1. Decomposition - extractive body cue:** In the following sections we derive the appropriate surface and pose optimization steps from the global objective.
- **p. 5 / 4.4. What is a LiDAR sweep? - extractive body cue:** However, our spacetime optimization can correctly model moving objects by applying the same insight; just as we assumed that the ego-vehicle obeys a constant velocity ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We assume as input a sequence of LiDAR sweeps measured at timestamps t ∈T , and coarse tracks of K objects. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3. Problem Statement), p. 3 (3. Problem Statement) |
| State/latent | assume, input, sequence, LiDAR, sweeps, measured, timestamps, coarse, tracks, objects, Since, compositional | geometry, map, object/relationship state | p. 3 (3. Problem Statement), p. 3 (3. Problem Statement), p. 5 (4.4. What is a LiDAR sweep?) |
| Output/action | Since we are using a compositional model of the scene, we will need a coordinate frame for each component. • Ego coordinates: This is the moving ego-vehicle coordinate frame used to measure ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3. Problem Statement), p. 5 (4.4. What is a LiDAR sweep?), p. 4 (3. Problem Statement) |
| Objective/outcome | In the following sections we derive the appropriate surface and pose optimization steps from the global objective. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (4.1. Decomposition), p. 4 (4.1. Decomposition), p. 5 (4.4. What is a LiDAR sweep?) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** An example of the depth maps produced by our method is shown in Fig.
- **p. 2 / 1. Introduction - extractive body cue:** We introduce a global optimization that refines both ego and object poses so as to minimize a scan-to-surface reconstruction error, dramatically improving results (right).
- **p. 4 / 4.1. Decomposition - extractive body cue:** Our approach consists of applying coordinate descent to Equation (2): alternating between fixing the poses to optimize surfaces and then fixing the surfaces to optimize ...
- **p. 4 / 4. Objective - extractive body cue:** Our method aims to find the surfaces and object motions that best explain the LiDAR measurements.
- **p. 1 / 1. Introduction - extractive body cue:** In contrast, recent novel view synthesis methods have modeled AV scenes with a composition of rigid models [24, 33, 34, 43].
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Dynamic object reconstructions using human-annotated bounding-box annotations (top left) tend to be noisy. Optimizing over object pose (top right) improves accuracy, while de-skewing ...
- **p. 8 / 6. Qualitative Results - extractive body cue:** 2, we show how accounting for this distortion can significantly improve the reconstructions.
- **p. 6 / 5.1. Lidar Novel View Synthesis - extractive body cue:** We follow [49] and let each method use the test pose that achieves the lowest error.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 2 (Figure/Table caption), p. 8 (6. Qualitative Results) |
| Embodiment/environment | Datasets: All of our experiments are conducted on nuScenes[3] and Argoverse 2.0[42]. | hardware/simulator version and reset protocol | p. 5 (5. Experiments), p. 6 (5. Experiments) |
| Dataset/benchmark | (Left) Each column shows nuScenes and Argoverse object reconstructions using ground truth poses compared to (right) ours. | role, split, size and leakage | p. 5 (5. Experiments), p. 6 (5. Experiments), p. 7 (5.2. Pose Estimation), p. 5 (5. Experiments) |
| Metric | We report the average distance and two accuracy metrics to characterize the distribution of errors. | definition, denominator, direction and uncertainty | p. 8 (6. Qualitative Results), p. 8 (Figure/Table caption), p. 6 (5.1. Lidar Novel View Synthesis) |
| Baseline/ablation | However, the comparison is with a state-of-the-art LiDAR odometry method instead of the ground truth since we find odometry is generally superior. | fair input/data/compute/action matching | p. 8 (6. Qualitative Results), p. 7 (5.1. Lidar Novel View Synthesis), p. 7 (5.2. Pose Estimation) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 5.1. Lidar Novel View Synthesis - extractive body cue:** Iterations are stopped if the mean registration error for an object falls below 1 centimeter for three consecutive iterations.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. NuScenes surface reconstruction produced by aggregating LiDAR scans using human-annotated ego-pose and dynamic object bounding boxes (left). We introduce a global optimization that ...
- **p. 6 / 5. Experiments - extractive body cue:** Interestingly, our approach is even more effective for recent AV datasets [30, 42] that employ multiple spinning lidars, which are often set to be out-of-phase ...
- **p. 7 / 5.1. Lidar Novel View Synthesis - extractive body cue:** For testing, however, the reference implementation does not support optimizing new poses that were not present at train time.
- **p. 5 / 5. Experiments - extractive body cue:** We focus primarily on nuScenes as its noisy annotations and sparse LiDAR present the greatest challenge to accurate geometry recovery.
- **p. 7 / 5.2. Pose Estimation - extractive body cue:** 1 further confirm the robustness of our method to input annotation errors.
- **p. 8 / 6. Qualitative Results - extractive body cue:** Evaluation of our method's robustness to actor annotation errors (subsampling or real tracks).

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, investment in autonomous driving has created a new mode of depth capture - spinning LiDAR sensors atop moving vehicles - which is largely unaddressed by the existing research.를 문제로 두고, An example of the depth maps produced by our method is shown in Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 4 (4.1. Decomposition) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
