# Momentum Control with Hierarchical Inverse Dynamics on a Torque-Controlled Humanoid

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1410.7284.
> PDF retrieval source: https://arxiv.org/pdf/1410.7284. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2016 / Autonomous Robots
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, humanoid, whole-body control, momentum control, inverse dynamics
- Official paper: https://arxiv.org/abs/1410.7284
- Full-text retrieval: https://arxiv.org/pdf/1410.7284
- Code/Project: https://is.mpg.de/am/publications/herzog_momentum_2016
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, the quasi-static assumption can be a limitation for dynamic motions.를 문제로 두고, This leads us to the main contribution of this paper, where we show experiments with extensive quantitative analysis for various tasks (Sections 4 and 5).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** 1We expect autonomous legged robots to perform complex tasks in persistent interaction with an uncertain and changing environment (e.g. in a disaster relief scenario).
- **p. 1 / 1 Introduction - extractive body cue:** Therefore, we need to design algorithms that can generate precise but compliant motions while optimizing the interactions with the environment.
- **p. 1 / 1 Introduction - extractive body cue:** In this context, the choice of a control strategy for legged robots is of primary importance as it can drastically improve performance in the face ...
- **p. 1 / 1 Introduction - extractive body cue:** Robots with torque control capabilities [4,12], including humanoids [5,25,28], are becoming increasingly available and torque control algorithms are therefore necessary to fully exploit their capabilities.
- **p. 1 / 1 Introduction - extractive body cue:** Indeed, such algorithms often offer high performance for motion control while guaranteeing a certain level of compliance [4, 16,33,34].
- **p. 2 / 1 Introduction - extractive body cue:** However, the quasi-static assumption can be a limitation for dynamic motions.
- **p. 2 / 1 Introduction - extractive body cue:** However, pseudo-inverse-based controllers are limited as they cannot properly handle inequality constraints such as torque limits or friction cone constraints.

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** This leads us to the main contribution of this paper, where we show experiments with extensive quantitative analysis for various tasks (Sections 4 and 5).
- **p. 1 / 1 Introduction - extractive body cue:** Recent contributions have also demonstrated the relevance of torque control approaches for humanoid robots [13,28,36].
- **p. 2 / 1 Introduction - extractive body cue:** It has been shown in several contributions [39,21] that the regulation of momentum could be very powerful for control on humanoids.
- **p. 2 / 1 Introduction - extractive body cue:** In a recent contribution [11], we have demonstrated that hierarchical inverse dynamics controllers could be efficiently used on a torquecontrolled humanoid robot.
- **p. 3 / 1 Introduction - extractive body cue:** Contribution In this contribution, we extend our preliminary work and present extensive experimental evaluations.
- **p. 17 / 6.2 Relation to other balancing approaches - extractive body cue:** However, with the optimization problem being complicated, they actually solve a simpler problem where the contact forces are first determined and then desired accelerations and ...
- **p. 17 / 6.2 Relation to other balancing approaches - extractive body cue:** In [36], the authors write the whole optimization procedure using Equation (1) with constraints similar to the ones we use.
- **p. 3 / 2.1 Modelling Assumptions and Problem Formulation - extractive body cue:** This can be expressed as a linear inequality by expressing the ground reaction force at the zero moment point.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Therefore it is not possible to directly control interaction forces during multi-contact tasks or to close a feedback loop directly around the tasks of interests, for example the center of gravity (CoG), ... | proprioception, reference pose/motion, visual or language command | p. 2 (1 Introduction), p. 3 (2.1 Modelling Assumptions and Problem Formulation) |
| State/latent | Therefore, possible, directly, control, interaction, forces, during, multi-contact, tasks, close, feedback, loop | whole-body pose, balance/contact state와 skill/mode | p. 2 (1 Introduction), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 3 (2.1 Modelling Assumptions and Problem Formulation) |
| Output/action | This can be expressed as a linear inequality by expressing the ground reaction force at the zero moment point. | joint/whole-body action, motion target 또는 task trajectory | p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 2 (1 Introduction) |
| Objective/outcome | At every control cycle, the equations of motion (Equation (1)), the constraints for physical consistency (torque saturation, CoP constraints, etc.) and our control objectives are all expressed as affine equations of the ... | tracking, balance, skill/task success와 recovery | p. 4 (2.1 Modelling Assumptions and Problem Formulation), p. 17 (6.2 Relation to other balancing approaches), p. 4 (2.1 Modelling Assumptions and Problem Formulation) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** This leads us to the main contribution of this paper, where we show experiments with extensive quantitative analysis for various tasks (Sections 4 and 5).
- **p. 1 / 1 Introduction - extractive body cue:** Recent contributions have also demonstrated the relevance of torque control approaches for humanoid robots [13,28,36].
- **p. 2 / 1 Introduction - extractive body cue:** It has been shown in several contributions [39,21] that the regulation of momentum could be very powerful for control on humanoids.
- **p. 2 / 1 Introduction - extractive body cue:** In a recent contribution [11], we have demonstrated that hierarchical inverse dynamics controllers could be efficiently used on a torquecontrolled humanoid robot.
- **p. 3 / 1 Introduction - extractive body cue:** Contribution In this contribution, we extend our preliminary work and present extensive experimental evaluations.
- **p. 8 / 4.2 Low-level torque control - extractive body cue:** This controller design allowed us to achieve good torque tracking performance.
- **p. 8 / 4.2 Low-level torque control - extractive body cue:** It is important to note that such performance was necessary to achieve good performance in the hierarchical inverse dynamics controller.
- **p. 13 / 5.3 Tracking Experiments in Double Support - extractive body cue:** As a consequence, the tracking of the CoG, which is in a lower priority, is not ideal but still achieves a reasonable performance.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.2 Low-level torque control), p. 8 (4.2 Low-level torque control) |
| Embodiment/environment | In the following, however, we construct a more complex stepping task in simulation for the full 25 DoF robot. | hardware/simulator version and reset protocol | p. 9 (5.1 Processing Time), p. 15 (5.4 Single Support Experiments) |
| Dataset/benchmark | Going from a 14 DoF robot to a 25 DoF robot with similar task setup makes the peak computation time rise from 1ms to 3ms. | role, split, size and leakage | p. 9 (5.1 Processing Time), p. 15 (5.4 Single Support Experiments), p. 9 (5.1 Processing Time), p. 11 (5.2.2 Comparison of momentum controllers) |
| Metric | It can be seen that overall the CoG error remains lower with the LQR controller, while the angular momentum behaves similarly. disturbance. | definition, denominator, direction and uncertainty | p. 11 (5.2.2 Comparison of momentum controllers), p. 11 (5.2.2 Comparison of momentum controllers), p. 8 (4.3 State estimation) |
| Baseline/ablation | It is worth mentioning again that the foot size of the robot is rather small compared to other humanoids. | fair input/data/compute/action matching | p. 16 (5.4 Single Support Experiments), p. 8 (4.4 Dynamic model), p. 9 (5.1 Processing Time) |

## Explicit Limitations and Failure Boundary

- **p. 17 / 6.2 Relation to other balancing approaches - extractive body cue:** Also, separating the EoM from kinematic contact constraints allows to keep solutions consistent with the dynamics even in postures where the feet cannot be kept ...
- **p. 17 / 6.3 Relations to other hierarchical inverse dynamics - extractive body cue:** On the other hand, it allows for prioritization of inequality constraints, which we exploit e.g. to give more importance to hardware limitations than to contact ...
- **p. 16 / 6.1 Task design and hierarchies - extractive body cue:** The bottom plot shows the CoP of the stance foot, which saturates close to the heel during the push, such that the foot does not ...
- **p. 7 / 4.1 Sarcos Humanoid Robot - extractive body cue:** Moving the CoP across this link makes the foot bend and causes the robot to fall.
- **p. 7 / 4 Experimental Setup - extractive body cue:** These details are important in order to understand the strengths and limitations of the presented experiments.
- **p. 9 / 5.1 Processing Time - extractive body cue:** The highest two priorities satisfy hardware limitations and dynamic constraints, the third priority task tracks a predefined center of gravity and swing foot motion and ...
- **p. 11 / 5.2.2 Comparison of momentum controllers - extractive body cue:** For both momentum control tasks, the robot was able to withstand impacts with high peak forces and strong impulses without falling.

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, the quasi-static assumption can be a limitation for dynamic motions.를 문제로 두고, This leads us to the main contribution of this paper, where we show experiments with extensive quantitative analysis for various tasks (Sections 4 and 5).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (2.1 Modelling Assumptions and Problem Formulation), p. 17 (6.2 Relation to other balancing approaches) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
