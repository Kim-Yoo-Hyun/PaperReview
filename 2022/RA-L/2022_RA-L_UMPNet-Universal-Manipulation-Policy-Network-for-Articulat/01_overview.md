# Universal Manipulation Policy Network for Articulated Objects

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2109.05668.
> PDF retrieval source: https://arxiv.org/pdf/2109.05668. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / RA-L
- Authors: Zhenjia Xu, Zhanpeng He, Shuran Song
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, 3D Vision, active perception, articulated objects, manipulation policy
- Official paper: https://arxiv.org/abs/2109.05668
- Full-text retrieval: https://arxiv.org/pdf/2109.05668
- Code/Project: https://ump-net.cs.columbia.edu/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

RGB-D로 관절 물체의 작용점과 이동 방향을 예측해 닫힌루프에서 조작한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce the Universal Manipulation Policy Network (UMPNet) - a single image-based policy network that infers closed-loop action sequences for manipulating articulated objects.
- **p. 1 / Abstract - extractive body cue:** To infer a wide range of action trajectories, the policy supports 6DoF action representation and varying trajectory length.
- **p. 1 / Abstract - extractive body cue:** To handle a diverse set of objects, the policy learns from objects with different articulation structures and generalizes to unseen objects or categories.
- **p. 1 / Abstract - extractive body cue:** The policy is trained with selfguided exploration without any human demonstrations, scripted policy, or pre-defined goal conditions.
- **p. 1 / Abstract - extractive body cue:** To support effective multistep interaction, we introduce a novel Arrow-of-Time action attribute that indicates whether an action will change the object state back to the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, such policies are often time-consuming to design and fail to generalize across objects with different articulation structures.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Extensive prior works have studied how to manually design or learn an object-specific policy for each type of interaction (e.g., opening doors).

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, we present a unified framework that discovers possible manipulation policies for an articulated object from visual observations.
- **p. 3 / III. APPROACH - extractive body cue:** To address this issue, we proposes an "Arrow-of-Time" (AoT) action attribute that indicates
- **p. 2 / I. INTRODUCTION - extractive body cue:** We validate our approach on two manipulation tasks (1) open-ended state exploration and (2) goal-conditioned manipulation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To achieve this goal, we formulate an action trajectory by its initial 3D position and a sequence of action directions, which allows the network to ...
- **p. 3 / III. APPROACH - extractive body cue:** For single-step interaction, any action that changes the object's state would result in a novel state.
- **p. 3 / III. APPROACH - extractive body cue:** We use a U-Net architecture for this task, the network is supervised by the outcome of the executed action (one out of W ×H pixels).
- **p. 3 / III. APPROACH - extractive body cue:** DistDecoder is a fully-connected neural network trained using MSE loss Ldist for the executed action at.
- **p. 4 / III. APPROACH - extractive body cue:** In the first half of each sequence, we select action with positive AoT prediction for execution to move the object away from its initial state.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Problem formulation The task is defined as follows: given a visual observation of an articulated object in the form of an RGB-D image at the initial and current state o0,ot ∈RW×H×4, the ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (III. APPROACH), p. 4 (III. APPROACH) |
| State/latent | Problem, formulation, task, defined, follows, given, visual, observation, articulated, object, form, RGB-D | geometry, map, object/relationship state | p. 3 (III. APPROACH), p. 4 (III. APPROACH), p. 2 (III. APPROACH) |
| Output/action | The key idea for performing the goal-conditioned task is to swap out the initial observation with the goal state observation as the input to the policy. | point map, pose, scene graph, affordance 또는 query result | p. 4 (III. APPROACH), p. 2 (III. APPROACH), p. 4 (III. APPROACH) |
| Objective/outcome | The network is trained with Binary Cross-Entropy loss. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (III. APPROACH), p. 4 (III. APPROACH), p. 3 (III. APPROACH) |

## Main Claims and Actual Contribution

- 자기주도 탐색으로 사람 시연 없이 상호작용 정책을 학습한다.
- Arrow-of-Time으로 과거 상태를 향하는 행동과 새로운 상태를 향하는 행동을 구분한다.

[검증한 원문](https://arxiv.org/abs/2109.05668)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (IV. EVALUATION), p. 5 (IV. EVALUATION) |
| Embodiment/environment | Being able to effectively explore the possible states of an object without a specific goal is a critical first step for many robot learning algorithms since it is often used to collect ... | hardware/simulator version and reset protocol | p. 5 (IV. EVALUATION), p. 7 (IV. EVALUATION) |
| Dataset/benchmark | In addition, our policy doesn't consider real robot situation, for example, whether the grasping position can be reached by a real robot, the moving trajectory is safe, the grasping surface is flat ... | role, split, size and leakage | p. 5 (IV. EVALUATION), p. 7 (IV. EVALUATION), p. 7 (IV. EVALUATION), p. 4 (IV. EVALUATION) |
| Metric | (2) success rate, where a successful case is defined as the normalized distance to the goal state is smaller than 0.1. | definition, denominator, direction and uncertainty | p. 6 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 7 (IV. EVALUATION) |
| Baseline/ablation | Compared to [ AoTOnly ], we can observe that by explicitly predicting the distance value for each action candidate, [ UMPNet ] can better differentiate | fair input/data/compute/action matching | p. 5 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 5 (IV. EVALUATION) |

## Explicit Limitations and Failure Boundary

- **p. 7 / IV. EVALUATION - extractive body cue:** Limitations and failure cases Assumptions: To allow goal-conditioned manipulation with reversed AoT actions, we assume the action trajectories are bi-directional in time (i.e., they are ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Typical failure cases. UR5 robot, and a suction gripper. Fig. 8 (a) shows the real- world setup. In this experiment, we directly tested ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Open-ended state exploration. Arrow length indicates the inferred distance value, color indicates the inferred AoT label. We visualized the uniform samples to better ...
- **p. 5 / IV. EVALUATION - extractive body cue:** I we can see that [ Where2Act ] is able to achieve similar performance in "single action effects", however, both [ Where2Act ] and [ ...
- **p. 5 / IV. EVALUATION - extractive body cue:** This heuristic helps to avoid back-and-forth actions, however cannot be applied for goal-conditioned manipulation. • SingleStep: Single-step version of our method that only takes the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Real-world experiment. We test the model trained in simulation on a real-world platform. (a) We an RGB-D camera to capture visual observation and ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. APPROACH)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, such policies are often time-consuming to design and fail to generalize across objects with different articulation structures. (p. 1, I. INTRODUCTION).
- **Actual contribution:** In this paper, we introduce the Universal Manipulation Policy Network (UMPNet) - a single policy network that discovers possible manipulation policies for an articulated object from visual observations (i.e., RGB-D ... (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** When combined with the heuristic the algorithm [ Where2Act+HP ] can avoid back-and-forth action, however, it is sensitive to error propagation, where one sub-optimal action would affect all following steps ... (p. 5, IV. EVALUATION).
- **Explicit failure boundary:** Limitations and failure cases Assumptions: To allow goal-conditioned manipulation with reversed AoT actions, we assume the action trajectories are bi-directional in time (i.e., they are valid in either direction). (p. 7, IV. EVALUATION).
