# Optimization-Based Locomotion Planning, Estimation, and Control Design for the Atlas Humanoid Robot

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.research.ed.ac.uk/en/publications/optimization-based-locomotion-planning-estimation-and-controldesi/.
> PDF retrieval source: https://www.cs.cmu.edu/~cga/z/Kuindersma_AURO_2016.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2016 / Autonomous Robots
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, humanoid, locomotion planning, optimization, state estimation
- Official paper: https://www.research.ed.ac.uk/en/publications/optimization-based-locomotion-planning-estimation-and-controldesi/
- Full-text retrieval: https://www.cs.cmu.edu/~cga/z/Kuindersma_AURO_2016.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Several practical challenges arise in the design of these systems, such as how to manage the complexity of the robot and environment model to efficiently do online planning and feedback control and ...를 문제로 두고, Unfortunately, the set of safe terrain is unlikely to be convex or even connected: in an environment as simple as a staircase, the safe terrain consists of the top surface of every ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This paper describes a collection of optimization algorithmsforachievingdynamicplanning,control,andstate estimation for a bipedal robot designed to operate reliably in complex environments.
- **p. 1 / Abstract - extractive body cue:** To make challenging locomotion tasks tractable, we describe several novel applications of convex, mixed-integer, and sparse nonlinear optimization to problems ranging from footstep placement to ...
- **p. 1 / Abstract - extractive body cue:** We also present a state estimator formulation that, when combined with our walking controller, permits highly precise execution of extended walking plans over non-flat terrain.
- **p. 1 / Abstract - extractive body cue:** We describe our complete system integration and experiments carried out on Atlas, a full-size hydraulic humanoid robot built by Boston Dynamics, Inc.
- **p. 1 / 1 Introduction - extractive body cue:** The dream of legged robotics is to achieve reliable, versatile, and dynamic locomotion for a robot capable of doing useful work in a variety of ...
- **p. 1 / 1 Introduction - extractive body cue:** Several practical challenges arise in the design of these systems, such as how to manage the complexity of the robot and environment model to efficiently ...
- **p. 1 / 1 Introduction - extractive body cue:** As participants in the DARPA Robotics Challenge (DRC), we are particularly interested in tasks related to disaster relief, such as walking outdoors over irregular terrain ...

## Core Idea

- **p. 4 / 3.1 Footstep planning as a mixed-integer convex - extractive body cue:** Unfortunately, the set of safe terrain is unlikely to be convex or even connected: in an environment as simple as a staircase, the safe terrain ...
- **p. 1 / 1 Introduction - extractive body cue:** In this paper we describe our approach to addressing these problems with Atlas.
- **p. 1 / 1 Introduction - extractive body cue:** Our approach to walking combines an efficient footstep planner with a simple dynamic model of the robot to efficiently compute desired walking trajectories.
- **p. 2 / 1 Introduction - extractive body cue:** We show that the robot is capable of walking over nontrivial terrain while maintaining extremely low drift from the desired footstep trajectory-a critically important capability ...
- **p. 2 / 1 Introduction - extractive body cue:** 6 we describe several experiments performed on the physical robot evaluatingthestateestimationandcontrolalgorithmsinpractice.We also describe recent simulation results of controlled highly dynamic motions that are currently being ...
- **p. 5 / 3.1.1 Convex decomposition - extractive body cue:** We use the polytope representation in our planner, since it is always of larger volume than the (inscribed) ellipsoid and can be represented as a ...
- **p. 8 / 3.2 Dynamic motion planning - extractive body cue:** As will be discussed below, we use a redundant multiple-force description of the total wrench acting on a rigid body because it permits the use ...
- **p. 11 / 4.4 Additional costs and constraints - extractive body cue:** For this we used a simple logic to determine what contact force variables should be included in the 123

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Note that inputs computed by solving this QP are, in general, not equal to those computed by thresholding the output of the closed-form LQR policy. | proprioception, reference pose/motion, visual or language command | p. 10 (4.1 General formulation), p. 11 (4.4 Additional costs and constraints) |
| State/latent | Note, inputs, computed, solving, general, equal, thresholding, output, closed-form, LQR, policy, Given | whole-body pose, balance/contact state와 skill/mode | p. 10 (4.1 General formulation), p. 11 (4.4 Additional costs and constraints), p. 14 (5.1 Requirements and approach) |
| Output/action | Given the current robot state, q, v, we can compute the equations of motion, H(q)˙v + C(q, v) = Bτ + JT λ, (25) H f Ha  ˙v + C f ... | joint/whole-body action, motion target 또는 task trajectory | p. 11 (4.4 Additional costs and constraints), p. 14 (5.1 Requirements and approach), p. 2 (1 Introduction) |
| Objective/outcome | Then we solve an optimization problem that assigns contacts to these regions in a way that minimizes cost while respecting kinematic and dynamic constraints. | tracking, balance, skill/task success와 recovery | p. 3 (3 Motion planning), p. 6 (3.1.3 Determining the number of footsteps), p. 10 (4.1 General formulation) |

## Main Claims and Actual Contribution

- **p. 4 / 3.1 Footstep planning as a mixed-integer convex - extractive body cue:** Unfortunately, the set of safe terrain is unlikely to be convex or even connected: in an environment as simple as a staircase, the safe terrain ...
- **p. 1 / 1 Introduction - extractive body cue:** In this paper we describe our approach to addressing these problems with Atlas.
- **p. 1 / 1 Introduction - extractive body cue:** Our approach to walking combines an efficient footstep planner with a simple dynamic model of the robot to efficiently compute desired walking trajectories.
- **p. 2 / 1 Introduction - extractive body cue:** We show that the robot is capable of walking over nontrivial terrain while maintaining extremely low drift from the desired footstep trajectory-a critically important capability ...
- **p. 2 / 1 Introduction - extractive body cue:** 6 we describe several experiments performed on the physical robot evaluatingthestateestimationandcontrolalgorithmsinpractice.We also describe recent simulation results of controlled highly dynamic motions that are currently being ...
- **p. 19 / 6.1 State estimation evaluation - extractive body cue:** To characterize the state estimator we evaluate its performance in a variety of experiments.
- **p. 19 / 6.1 State estimation evaluation - extractive body cue:** In the manipulation experiment, the LIDAR contribution actually degrades performance slightly due to occlusions caused by arm motions.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 19 (6.1 State estimation evaluation), p. 19 (6.1 State estimation evaluation) |
| Embodiment/environment | We describe several experiments performed on the robot and in simulation. | hardware/simulator version and reset protocol | p. 19 (6 Experiments), p. 19 (6.1 State estimation evaluation) |
| Dataset/benchmark | We describe several experiments performed on the robot and in simulation. | role, split, size and leakage | p. 19 (6 Experiments), p. 19 (6.1 State estimation evaluation) |
| Metric | Orientation estimation performance is comparable between different estimators.Notethattheprecisionofthegroundtruthorientation determined using VICON measurements is on the order of 1◦, so we were unable to differentiate yaw drift on a f ... | definition, denominator, direction and uncertainty | p. 19 (6.1 State estimation evaluation), p. 19 (6.1 State estimation evaluation) |
| Baseline/ablation | not recovered | fair input/data/compute/action matching | 본문 anchor 없음 |

## Explicit Limitations and Failure Boundary

- **p. 20 / 6.3 Closed-loop walking with LIDAR feedback - extractive body cue:** The robot's trailing foot eventually collided with the front of the step resulting in a fall.
- **p. 20 / 6.3 Closed-loop walking with LIDAR feedback - extractive body cue:** This scenario requires great precision, if the state estimator drifts by even a few centimeters, the robot will hit a step edge and fall.
- **p. 22 / 6.4.1 Running - extractive body cue:** 13), require at least 3cm of clearance between links to avoid self-collisions, and constrain the gaze of the robot's head cameras to be no more ...
- **p. 19 / 6.1 State estimation evaluation - extractive body cue:** In the manipulation experiment, the LIDAR contribution actually degrades performance slightly due to occlusions caused by arm motions.

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 Several practical challenges arise in the design of these systems, such as how to manage the complexity of the robot and environment model to efficiently do online planning and feedback control and ...를 문제로 두고, Unfortunately, the set of safe terrain is unlikely to be convex or even connected: in an environment as simple as a staircase, the safe terrain consists of the top surface of every ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (3.1.1 Convex decomposition), p. 8 (3.2 Dynamic motion planning) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
