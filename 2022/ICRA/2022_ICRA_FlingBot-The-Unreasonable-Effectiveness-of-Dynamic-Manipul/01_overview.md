# FlingBot: The Unreasonable Effectiveness of Dynamic Manipulation for Cloth Unfolding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2105.03655.
> PDF retrieval source: https://arxiv.org/pdf/2105.03655. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, deformable object, cloth manipulation, dynamic manipulation, vision-based control
- Official paper: https://arxiv.org/abs/2105.03655
- Full-text retrieval: https://arxiv.org/pdf/2105.03655
- Code/Project: https://flingbot.cs.columbia.edu/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 Additionally, since the robot arm cannot manipulate the cloth at locations it can't reach, the maximum cloth size is greatly limited by the robot arm's reach range.를 문제로 두고, In summary: • Our main contribution is in demonstrating the effectiveness of dynamic manipulation for cloth unfolding through our self-supervised learning framework, FlingBot. • We propose a parameterization for the dual-arm grasp ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** High-velocity dynamic actions (e.g., fling or throw) play a crucial role in our everyday interaction with deformable objects by improving our efficiency and effectively expanding ...
- **p. 1 / Abstract - extractive body cue:** Yet, most prior works have tackled cloth manipulation using exclusively single-arm quasi-static actions, which requires a large number of interactions for challenging initial cloth configurations ...
- **p. 1 / Abstract - extractive body cue:** In this work, we demonstrate the effectiveness of dynamic flinging actions for cloth unfolding with our proposed self-supervised learning framework, FlingBot.
- **p. 1 / Abstract - extractive body cue:** Our approach learns how to unfold a piece of fabric from arbitrary initial configurations using a pick, stretch, and fling primitive for a dual-arm setup ...
- **p. 1 / Abstract - extractive body cue:** The final system achieves over 80% coverage within 3 actions on novel cloths, can unfold cloths larger than the system's reach range, and generalizes to ...
- **p. 1 / 1 Introduction - extractive body cue:** Additionally, since the robot arm cannot manipulate the cloth at locations it can't reach, the maximum cloth size is greatly limited by the robot arm's ...
- **p. 1 / 1 Introduction - extractive body cue:** From goal-conditioned folding [2] to fabric smoothing [3, 4], prior works have achieved success using exclusively single-arm quasistatic interactions (e.g., pick & place) for cloth ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In summary: • Our main contribution is in demonstrating the effectiveness of dynamic manipulation for cloth unfolding through our self-supervised learning framework, FlingBot. • We ...
- **p. 4 / 3 Method - extractive body cue:** To make these constraints linear and independent, we propose an alternative 4-scalar parameterization, which consists of pixel position of the point C ∈R2 at the ...
- **p. 2 / 1 Introduction - extractive body cue:** To achieve this goal, we present FlingBot, a self-supervised algorithm that learns how to unfold cloths from arbitrary initial configurations using a pick, stretch, and ...
- **p. 5 / 3 Method - extractive body cue:** To this end, we propose to use spatial action maps [5, 6, 7].
- **p. 6 / 3 Method - extractive body cue:** Our real-world experiment setup consists of two UR5s, where one is equipped with a Schunk WSG50 and the other with an OnRobot RG2, facing each ...
- **p. 5 / 3 Method - extractive body cue:** Our value network is a fully convolutional neural network with nine residual blocks [21] and two convolutional layers in the first and last layer, and ...
- **p. 5 / 3 Method - extractive body cue:** From a top-down RGB image a), our policy evaluates a batch of different action rotations and scales by transforming the observation b) then predicting the ...
- **p. 3 / 3 Method - extractive body cue:** It predicts the value of each action with a value network (Sec.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | From a top-down RGB image a), our policy evaluates a batch of different action rotations and scales by transforming the observation b) then predicting the corresponding batch of value maps c). | RGB-D/point cloud, object state와 contact/task observation | p. 5 (3 Method), p. 2 (1 Introduction) |
| State/latent | top-down, RGB, image, policy, evaluates, batch, different, action, rotations, scales, transforming, observation | object geometry, affordance, contact mode 또는 end-effector state | p. 5 (3 Method), p. 2 (1 Introduction), p. 3 (3 Method) |
| Output/action | At each time step, the policy predicts value maps from its visual observation and picks actions greedily with respect to its value maps. | grasp, pose, force 또는 end-effector trajectory | p. 2 (1 Introduction), p. 3 (3 Method), p. 5 (3 Method) |
| Objective/outcome | However, to minimize collisions between two arms, we wish to impose a constraint that L is always left of R, and vice versa (Fig 9a). | task completion, contact success, pose/force error와 generalization | p. 4 (3 Method), p. 3 (3 Method), p. 3 (3 Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In summary: • Our main contribution is in demonstrating the effectiveness of dynamic manipulation for cloth unfolding through our self-supervised learning framework, FlingBot. • We ...
- **p. 4 / 3 Method - extractive body cue:** To make these constraints linear and independent, we propose an alternative 4-scalar parameterization, which consists of pixel position of the point C ∈R2 at the ...
- **p. 2 / 1 Introduction - extractive body cue:** To achieve this goal, we present FlingBot, a self-supervised algorithm that learns how to unfold cloths from arbitrary initial configurations using a pick, stretch, and ...
- **p. 5 / 3 Method - extractive body cue:** To this end, we propose to use spatial action maps [5, 6, 7].
- **p. 6 / 3 Method - extractive body cue:** Our real-world experiment setup consists of two UR5s, where one is equipped with a Schunk WSG50 and the other with an OnRobot RG2, facing each ...
- **p. 7 / 4 Evaluation - extractive body cue:** While the pick & place baseline discovered a similar strategy, its performance is inherently limited by quasi-static actions, requiring significantly more steps to achieve a ...
- **p. 9 / 4.4 Results - extractive body cue:** 2, we report that our policy achieves over 80% on all cloth types, which outperforms the quasi-static pick & place baseline by over 40%.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Coverage v.s. Steps. With 95% confidence interval shaded. FlingBot can achieve high coverage within a few interaction steps, while the quasi-static baselines never ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4 Evaluation), p. 9 (4.4 Results) |
| Embodiment/environment | The performance is reported averaged over 10 test episodes, where real-world grasp errors are filtered out (see "Real World Failure Cases" below). | hardware/simulator version and reset protocol | p. 9 (4.4 Results), p. 7 (4 Evaluation) |
| Dataset/benchmark | 4.2 Task Dataset Generation Each task is specified by a cloth mesh, mass, stiffness, and initial configuration. | role, split, size and leakage | p. 9 (4.4 Results), p. 7 (4 Evaluation), p. 6 (4 Evaluation), p. 6 (4 Evaluation) |
| Metric | The average grasp success rate is 78.0%, 45.0%, and 75.8% for normal rectangular, large rectangular, and shirts respectively. | definition, denominator, direction and uncertainty | p. 9 (4.4 Results), p. 7 (4 Evaluation), p. 9 (4.4 Results) |
| Baseline/ablation | Compared to the quasi-static baselines, [FlingBot] increases the coverage by +52.0%, which is roughly twice that of the quasi-static baselines ( +27.1%, +24.8%, +23.1%). | fair input/data/compute/action matching | p. 8 (4.4 Results), p. 9 (4.4 Results), p. 8 (4 Evaluation) |

## Explicit Limitations and Failure Boundary

- **p. 13 / Figure/Table caption - extractive body cue:** Figure 8: Failure Cases in Simulation Experiments. 6.3 Real world fling parameter robustness In designing our motion primitive, we optimized fling parameters (waypoints, velocities, accelera- ...
- **p. 9 / 4.4 Results - extractive body cue:** We discuss more of real world grasp failures in Sec.
- **p. 9 / 4.4 Results - extractive body cue:** The performance is reported averaged over 10 test episodes, where real-world grasp errors are filtered out (see "Real World Failure Cases" below).
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 6: Qualitative Results in Simulation Experiments. 6.2 Failure cases 1.0 1.2 1.4 1.6 Fling speed
- **p. 8 / 4 Evaluation - extractive body cue:** 1, [Fling-Reg] completely fails to perform the task, demonstrating the advantage of encoding inductive biases which leverage equivariances in the problem structure.
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 9: To minimize collisions, arms should grasp points closer to their side (a) and be a reasonable distance away from each other (b). 6.6 ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 7: Real world fling speed robust- ness. By flinging at speeds in the range [1.0m s-1, 1.7m s-1] at 0.1m s-1 intervals, we observed ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 Additionally, since the robot arm cannot manipulate the cloth at locations it can't reach, the maximum cloth size is greatly limited by the robot arm's reach range.를 문제로 두고, In summary: • Our main contribution is in demonstrating the effectiveness of dynamic manipulation for cloth unfolding through our self-supervised learning framework, FlingBot. • We propose a parameterization for the dual-arm grasp ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Method), p. 5 (3 Method), p. 3 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
