# Synthesis of Whole-Body Behaviors through Hierarchical Control of Behavioral Primitives

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://ai.stanford.edu/~lsentis/files/publications.html.
> PDF retrieval source: https://ai.stanford.edu/manips/publications/pdfs/Sentis_2005_IJHR.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2005 / IJHR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, humanoid, whole-body control, task hierarchy, operational space
- Official paper: https://ai.stanford.edu/~lsentis/files/publications.html
- Full-text retrieval: https://ai.stanford.edu/manips/publications/pdfs/Sentis_2005_IJHR.pdf
- Code/Project: https://ai.stanford.edu/~lsentis/files/publications.html
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Controlling humanoids in these environments requires us to synthesize and change complex whole-body behaviors on-demand in the presence of high uncertainty.를 문제로 두고, In contrast, our methodology integrates constraints in the control formulation as primary controls and projects the operational tasks and the posture primitives into the constraint motion null-space, thus eliminating the motion componen ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1. Introduction - extractive body cue:** Emerging applications of humanoids demand higher and higher degrees of autonomy for efficient interactions in human-populated environments.
- **p. 1 / 1. Introduction - extractive body cue:** Controlling humanoids in these environments requires us to synthesize and change complex whole-body behaviors on-demand in the presence of high uncertainty.
- **p. 1 / 1. Introduction - extractive body cue:** To synthesize whole-body behaviors on-demand we have developed a behavior-oriented methodology where multiple behavioral primitives are controlled simultaneously.
- **p. 1 / 1. Introduction - extractive body cue:** New behaviors are created by adding or removing individual, or collections of, pre-designed behavioral primitives, without the need to interrupt the movement.
- **p. 1 / 1. Introduction - extractive body cue:** To guarantee the safety of the robot and its environment we have designed a control hierarchy among primitives, where the control of the most critical ...
- **p. 2 / 1. Introduction - extractive body cue:** Section 4 presents a multi-level prioritized framework that allows us to establish multiple priority levels among categories.
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we will describe in detail this hierarchy based on projecting the control of lower priority primitives into the motion null-space of higher ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In contrast, our methodology integrates constraints in the control formulation as primary controls and projects the operational tasks and the posture primitives into the constraint ...
- **p. 2 / 1. Introduction - extractive body cue:** In Section 2 we describe previous related work, and also lay the mathematical foundations for this research based on our previous work.9 In Section 3 ...
- **p. 5 / 3. Integration of constraints - extractive body cue:** Based on the operational space formulation for redundant robots, further represented by the torque decomposition Γ = J T F + N T Γnull, (9) ...
- **p. 6 / 4. Multi-level hierarchy - extractive body cue:** We propose a multi-level control hierarchy that extends the task and posture decomposition previously described.
- **p. 1 / 1. Introduction - extractive body cue:** New behaviors are created by adding or removing individual, or collections of, pre-designed behavioral primitives, without the need to interrupt the movement.
- **p. 1 / Body text (section not recovered) - extractive body cue:** In this paper we will present a multi-level hierarchical control structure that allows the establishment of general priorities among behavioral primitives, and we will describe ...
- **p. 4 / 3. Integration of constraints - extractive body cue:** In this context, redundancy has received much attention, with most algorithms
- **p. 1 / 1. Introduction - extractive body cue:** Emerging applications of humanoids demand higher and higher degrees of autonomy for efficient interactions in human-populated environments.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Emerging applications of humanoids demand higher and higher degrees of autonomy for efficient interactions in human-populated environments. | proprioception, reference pose/motion, visual or language command | p. 1 (1. Introduction), p. 1 (Body text (section not recovered)) |
| State/latent | Emerging, applications, humanoids, demand, higher, degrees, autonomy, efficient, interactions, human-populated, environments, will | whole-body pose, balance/contact state와 skill/mode | p. 1 (1. Introduction), p. 1 (Body text (section not recovered)), p. 2 (1. Introduction) |
| Output/action | In this paper we will present a multi-level hierarchical control structure that allows the establishment of general priorities among behavioral primitives, and we will describe compliant control strategies for efficient control under ... | joint/whole-body action, motion target 또는 task trajectory | p. 1 (Body text (section not recovered)), p. 2 (1. Introduction), p. 5 (3. Integration of constraints) |
| Objective/outcome | To accomplish the task and handle the constraint efficiently, we apply the control described in Equation (10). | tracking, balance, skill/task success와 recovery | p. 6 (3. Integration of constraints), p. 7 (4. Multi-level hierarchy), p. 7 (4. Multi-level hierarchy) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In contrast, our methodology integrates constraints in the control formulation as primary controls and projects the operational tasks and the posture primitives into the constraint ...
- **p. 2 / 1. Introduction - extractive body cue:** In Section 2 we describe previous related work, and also lay the mathematical foundations for this research based on our previous work.9 In Section 3 ...
- **p. 5 / 3. Integration of constraints - extractive body cue:** Based on the operational space formulation for redundant robots, further represented by the torque decomposition Γ = J T F + N T Γnull, (9) ...
- **p. 6 / 4. Multi-level hierarchy - extractive body cue:** We propose a multi-level control hierarchy that extends the task and posture decomposition previously described.
- **p. 1 / 1. Introduction - extractive body cue:** New behaviors are created by adding or removing individual, or collections of, pre-designed behavioral primitives, without the need to interrupt the movement.
- **p. 10 / 4.3. Movement feasibility - extractive body cue:** But first, to evaluate the performance and determine the optimal ordering we examine a scenario where the center of gravity control shares control priority with ...
- **p. 12 / X Direction - extractive body cue:** The results of this control are shown in Figure 4.
- **p. 13 / 6. Summary and discussion - extractive body cue:** Our major contribution is in presenting a novel and unified framework that is based on robust theoretical results.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 10 (4.3. Movement feasibility), p. 12 (X Direction) |
| Embodiment/environment | Collision avoidance and control of multiple task primitives: This sequence depicts a robot avoiding an obstacle that is moved interactively towards several points near the robot's body. | hardware/simulator version and reset protocol | p. 5 (3. Integration of constraints), p. 5 (3. Integration of constraints) |
| Dataset/benchmark | A humanoid robot must accomplish a collection of operational tasks while satisfying several constraints acting on the robot's body. | role, split, size and leakage | p. 5 (3. Integration of constraints), p. 5 (3. Integration of constraints), p. 6 (4. Multi-level hierarchy), p. 6 (4. Multi-level hierarchy) |
| Metric | December 19, 2005 17:13 WSPC/INSTRUCTION FILE ijhr-II-v4 11 0 1 2 3 -2 0 2 time [s] error [cm] Balancing Error | definition, denominator, direction and uncertainty | p. 11 (4.3. Movement feasibility), p. 12 (X Direction), p. 12 (X Direction) |
| Baseline/ablation | We can then modify the task trajectory or remove its control while the control of other higher priority tasks such as balancing or control of the contact points is maintained. | fair input/data/compute/action matching | p. 9 (4.3. Movement feasibility), p. 5 (3. Integration of constraints), p. 6 (3. Integration of constraints) |

## Explicit Limitations and Failure Boundary

- **p. 13 / 6. Summary and discussion - extractive body cue:** Our research has addressed a wide set of constraints, such as joint-limits, collision avoidance, and self-collision avoidance, based on reactive techniques at the whole-body level.
- **p. 5 / 3. Integration of constraints - extractive body cue:** Collision avoidance and control of multiple task primitives: This sequence depicts a robot avoiding an obstacle that is moved interactively towards several points near the ...
- **p. 11 / X Direction - extractive body cue:** However, the center of gravity horizontal position cannot be maintained (a), because its control is directly affected by the hand control. i.e. Γ = ΓJLC ...
- **p. 12 / X Direction - extractive body cue:** Because the hierarchy assigns higher priority to the center of gravity task, it maintains its desired goal position (above the robot's feet) at all times, ...
- **p. 13 / X Direction - extractive body cue:** December 19, 2005 17:13 WSPC/INSTRUCTION FILE ijhr-II-v4 13 conflict in their control (cannot be simultaneously accomplished).
- **p. 6 / 3. Integration of constraints - extractive body cue:** This projection ensures that the operational task does not introduce acceleration components into the constrained directions.

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Controlling humanoids in these environments requires us to synthesize and change complex whole-body behaviors on-demand in the presence of high uncertainty.를 문제로 두고, In contrast, our methodology integrates constraints in the control formulation as primary controls and projects the operational tasks and the posture primitives into the constraint motion null-space, thus eliminating the motion componen ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (Body text (section not recovered)), p. 4 (3. Integration of constraints), p. 1 (1. Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
