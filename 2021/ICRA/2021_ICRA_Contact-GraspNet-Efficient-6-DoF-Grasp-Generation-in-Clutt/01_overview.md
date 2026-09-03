# Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2103.14127.
> PDF retrieval source: https://arxiv.org/pdf/2103.14127. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: CORE
- Tags: Robotics, grasping, contact prediction, 6-DoF grasp
- Official paper: https://arxiv.org/abs/2103.14127
- Full-text retrieval: https://arxiv.org/pdf/2103.14127
- Code/Project: https://github.com/NVlabs/contact_graspnet
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 To address the limitations of planar grasping, there has been a recent interest in tackling the problem of 6-DoF grasping of unknown objects [10, 11, 12, 13, 14].를 문제로 두고, Our method is closely related to the work of Murali et al.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Grasping unseen objects in unconstrained, cluttered environments is an essential skill for autonomous robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** Despite recent progress in full 6-DoF grasp learning, existing approaches often consist of complex sequential pipelines that possess several potential failure points and run-times unsuitable ...
- **p. 1 / Abstract - extractive body cue:** Therefore, we propose an end-to-end network that efficiently generates a distribution of 6-DoF parallel-jaw grasps directly from a depth recording of a scene.
- **p. 1 / Abstract - extractive body cue:** Our novel grasp representation treats 3D points of the recorded point cloud as potential grasp contacts.
- **p. 1 / Abstract - extractive body cue:** By rooting the full 6-DoF grasp pose and width in the observed point cloud, we can reduce the dimensionality of our grasp representation to 4-DoF ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address the limitations of planar grasping, there has been a recent interest in tackling the problem of 6-DoF grasping of unknown objects [10, 11, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Grasping objects from cluttered scenes with structure introduces extra challenges.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method is closely related to the work of Murali et al.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address these issues, our method instead directly processes a full scene point cloud or a local region around a target object.
- **p. 3 / III. METHOD - extractive body cue:** We used the ACRONYM dataset [32], which consists of 8872 meshes from the Shapenet dataset [35] and 17.7 million
- **p. 4 / III. METHOD - extractive body cue:** Instead of supervising all network heads in isolation, we propose to combine the predictions to the 6-DoF grasp pose ˆg ∈G given in Eq.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Thus, our main contributions are the following: • A new end-to-end method for 6-DoF grasping of unknown objects in cluttered real world scenes where we ...
- **p. 4 / III. METHOD - extractive body cue:** The network has four heads with two 1DConv layers each and per-point outputs s ∈R, z1 ∈R3, z2 ∈ R3, o ∈R10, from which we ...
- **p. 3 / III. METHOD - extractive body cue:** In pink we show the five gripper points v that we used in the ladd-s loss. been shown to be difficult in grasping [11] and ...
- **p. 3 / III. METHOD - extractive body cue:** Point Set Networks such as PointNet++ [34] effectively process point clouds and hierarchically aggregate points and their feature representations in local 3D neighborhoods.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Their predictions can be directly associated to 3D points in the input point cloud and our proposed grasp representation exploits this ability. | RGB-D/point cloud, object state와 contact/task observation | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| State/latent | predictions, directly, associated, points, input, point, cloud, grasp, representation, exploits, ability, Network | object geometry, affordance, contact mode 또는 end-effector state | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD) |
| Output/action | Network We employ the set abstraction and feature propagation layers proposed in PointNet++ [34] to build an asymmetric Ushaped network. | grasp, pose, force 또는 end-effector trajectory | p. 4 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Objective/outcome | On the grasp width bin predictions, we optimize a weighted, multi-label binary cross entropy loss lwidth. | task completion, contact success, pose/force error와 generalization | p. 4 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method is closely related to the work of Murali et al.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address these issues, our method instead directly processes a full scene point cloud or a local region around a target object.
- **p. 3 / III. METHOD - extractive body cue:** We used the ACRONYM dataset [32], which consists of 8872 meshes from the Shapenet dataset [35] and 17.7 million
- **p. 4 / III. METHOD - extractive body cue:** Instead of supervising all network heads in isolation, we propose to combine the predictions to the 6-DoF grasp pose ˆg ∈G given in Eq.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Thus, our main contributions are the following: • A new end-to-end method for 6-DoF grasping of unknown objects in cluttered real world scenes where we ...
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** We observe a significantly higher grasp success rate of our method compared to [11] and [12] which themselves outperform other learning-based methods and analytic/heuristic baselines.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** The average distance loss ladd-s improves the success rate of high confidence contacts which is important because most grasps that we execute lie in the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6. Data Ablations: Training with Gaussian noise has similar perfor- mance in simulation but helps generalization to noisy sensor data. Predicting grasps directly on ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Embodiment/environment | We evaluate our method in a grasping study with a Franka robot where we pick unknown objects in cluttered scenes. | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Dataset/benchmark | In the end we execute the most confident grasp that is kinematically reachable and where the robot does not collide with the scene [38]. | role, split, size and leakage | p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Metric | The average distance loss ladd-s improves the success rate of high confidence contacts which is important because most grasps that we execute lie in the first decimal of coverage. | definition, denominator, direction and uncertainty | p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (Figure/Table caption), p. 6 (IV. EXPERIMENTAL EVALUATION) |
| Baseline/ablation | We observe a significantly higher grasp success rate of our method compared to [11] and [12] which themselves outperform other learning-based methods and analytic/heuristic baselines. | fair input/data/compute/action matching | p. 6 (IV. EXPERIMENTAL EVALUATION), p. 5 (IV. EXPERIMENTAL EVALUATION), p. 3 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / V. CONCLUSIONS - extractive body cue:** Gripper collisions are effectively avoided by considering them during training and by predicting grasps directly in scenes.
- **p. 6 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** Failure Cases: We observe some failure cases for thick objects that only allow grasps almost at maximum grasp width.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Contact-GraspNet efficiently predicts diverse and stable grasps in cluttered scenes while avoiding collisions. space of possible grasps to planar grasping, where grasps are ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Training Data Pipeline. We place object meshes with dense grasp annotations from the ACRONYM dataset [32] at random stable poses in scenes. Grasp ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** However, grasping in only one or two trials is crucial in cluttered scenes (e.g. in households) with large, densely packed objects where collisions should be ...
- **p. 5 / IV. EXPERIMENTAL EVALUATION - extractive body cue:** In the end we execute the most confident grasp that is kinematically reachable and where the robot does not collide with the scene [38].

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 To address the limitations of planar grasping, there has been a recent interest in tackling the problem of 6-DoF grasping of unknown objects [10, 11, 12, 13, 14].를 문제로 두고, Our method is closely related to the work of Murali et al.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** To address the limitations of planar grasping, there has been a recent interest in tackling the problem of 6-DoF grasping of unknown objects [10, 11, 12, 13, 14]. (p. 1, I. INTRODUCTION).
- **Actual contribution:** Thus, our main contributions are the following: • A new end-to-end method for 6-DoF grasping of unknown objects in cluttered real world scenes where we achieve 90% grasp success rate. (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** We observe a significantly higher grasp success rate of our method compared to [11] and [12] which themselves outperform other learning-based methods and analytic/heuristic baselines. (p. 6, IV. EXPERIMENTAL EVALUATION).
- **Explicit failure boundary:** Failure Cases: We observe some failure cases for thick objects that only allow grasps almost at maximum grasp width. (p. 6, IV. EXPERIMENTAL EVALUATION).
