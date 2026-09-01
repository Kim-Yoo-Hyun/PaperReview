# UMPNet: Universal Manipulation Policy Network for Articulated Objects

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2109.05668.
> PDF retrieval source: https://arxiv.org/pdf/2109.05668. Reading tracker status/evidence was not changed.

- Year/Venue: 2022 / RA-L
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, 3D Vision, active perception, articulated objects, manipulation policy
- Official paper: https://arxiv.org/abs/2109.05668
- Full-text retrieval: https://arxiv.org/pdf/2109.05668
- Code/Project: https://ump-net.cs.columbia.edu/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, such policies are often time-consuming to design and fail to generalize across objects with different articulation structures.를 문제로 두고, In summary, we present a unified framework that discovers possible manipulation policies for an articulated object from visual observations.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, we present a unified framework that discovers possible manipulation policies for an articulated object from visual observations.
- **p. 3 / III. APPROACH - extractive body cue:** To address this issue, we proposes an "Arrow-of-Time" (AoT) action attribute that indicates
- **p. 2 / I. INTRODUCTION - extractive body cue:** We validate our approach on two manipulation tasks (1) open-ended state exploration and (2) goal-conditioned manipulation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** To achieve this goal, we formulate an action trajectory by its initial 3D position and a sequence of action directions, which allows the network to ...
- **p. 3 / III. APPROACH - extractive body cue:** For single-step interaction, any action that changes the object's state would result in a novel state.
- **p. 5 / IV. EVALUATION - extractive body cue:** When combined with heuristic filter, the performance improves slightly.
- **p. 5 / IV. EVALUATION - extractive body cue:** I we can see that [ Where2Act ] is able to achieve similar performance in "single action effects", however, both [ Where2Act ] and [ ...
- **p. 6 / IV. EVALUATION - extractive body cue:** As a result, [ UMPNet ] can achieve better performance in both metrics.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Manipulation, contact, tactile, and dexterity의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, such policies are often time-consuming to design and fail to generalize across objects with different articulation structures.를 문제로 두고, In summary, we present a unified framework that discovers possible manipulation policies for an articulated object from visual observations.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. APPROACH), p. 3 (III. APPROACH) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
