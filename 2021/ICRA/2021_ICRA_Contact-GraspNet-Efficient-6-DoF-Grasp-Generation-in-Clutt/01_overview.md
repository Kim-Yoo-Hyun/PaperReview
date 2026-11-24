# Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2103.14127.
> PDF retrieval source: https://arxiv.org/pdf/2103.14127. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ICRA
- Authors: Martin Sundermeyer, Arsalan Mousavian, Rudolph Triebel, Dieter Fox
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, grasping, contact prediction, 6-DoF grasp
- Official paper: https://arxiv.org/abs/2103.14127
- Full-text retrieval: https://arxiv.org/pdf/2103.14127
- Code/Project: https://github.com/NVlabs/contact_graspnet
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Contact-GraspNet은 복잡한 장면의 깊이 관측 하나에서 평행 그리퍼의 6자유도 파지 자세와 폭을 생성한다. [PDF 1쪽](https://arxiv.org/pdf/2103.14127#page=1)

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

- 관측된 점을 접촉 후보로 고정해 학습할 파지 변수의 차원을 줄이고 장면 점군에서 여러 후보를 한 번에 예측한다. [PDF 3쪽](https://arxiv.org/pdf/2103.14127#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2103.14127#page=4)
- 시뮬레이션 파지 기록으로 학습한 모델을 실제 깊이 센서에 적용해, 처음 보는 물체들이 섞인 장면에서 파지를 평가했다. [PDF 5쪽](https://arxiv.org/pdf/2103.14127#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2103.14127#page=6)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 3 (III. METHOD)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** To address the limitations of planar grasping, there has been a recent interest in tackling the problem of 6-DoF grasping of unknown objects [10, 11, 12, 13, 14]. (p. 1, I. INTRODUCTION).
- **Actual contribution:** Thus, our main contributions are the following: • A new end-to-end method for 6-DoF grasping of unknown objects in cluttered real world scenes where we achieve 90% grasp success rate. (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** We observe a significantly higher grasp success rate of our method compared to [11] and [12] which themselves outperform other learning-based methods and analytic/heuristic baselines. (p. 6, IV. EXPERIMENTAL EVALUATION).
- **Explicit failure boundary:** Failure Cases: We observe some failure cases for thick objects that only allow grasps almost at maximum grasp width. (p. 6, IV. EXPERIMENTAL EVALUATION).

## 배포 범위 대조

- 코드 — 저자 구현 파일 · contact_graspnet/contact_graspnet.py [배포 파일](https://raw.githubusercontent.com/NVlabs/contact_graspnet/721706067cc7f7889c32afe7b4f7955eb90bd866/contact_graspnet/contact_graspnet.py)
- 가중치 — Contact-GraspNet의 학습 체크포인트 자료 파일과 동일 폴더의 색인을 확인했다. [배포 파일](https://drive.google.com/file/d/1LIHVgwseBBTv0YxhgYMn7-pKjo8vptEk/view)
- 데이터 — 저자가 배포한 시험용 장면 관측 파일이다. [배포 파일](https://drive.google.com/file/d/1lMCkzIPYvTGYbjLaTEPpRL4qXN5Xz0TF/view)
