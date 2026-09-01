# Problem - Optimization-Based Locomotion Planning, Estimation, and Control Design for the Atlas Humanoid Robot

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.research.ed.ac.uk/en/publications/optimization-based-locomotion-planning-estimation-and-controldesi/; PDF retrieval source: https://www.cs.cmu.edu/~cga/z/Kuindersma_AURO_2016.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): Several practical challenges arise in the design of these systems, such as how to manage the complexity of the robot and environment model to efficiently do online planning and feedback ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** This paper describes a collection of optimization algorithmsforachievingdynamicplanning,control,andstate estimation for a bipedal robot designed to operate reliably in complex environments.
- **p. 1 / Abstract - extractive PDF cue:** To make challenging locomotion tasks tractable, we describe several novel applications of convex, mixed-integer, and sparse nonlinear optimization to problems ranging from footstep placement to ...
- **p. 1 / Abstract - extractive PDF cue:** We also present a state estimator formulation that, when combined with our walking controller, permits highly precise execution of extended walking plans over non-flat terrain.
- **p. 1 / Abstract - extractive PDF cue:** We describe our complete system integration and experiments carried out on Atlas, a full-size hydraulic humanoid robot built by Boston Dynamics, Inc.
- **p. 1 / 1 Introduction - extractive PDF cue:** The dream of legged robotics is to achieve reliable, versatile, and dynamic locomotion for a robot capable of doing useful work in a variety of ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Several practical challenges arise in the design of these systems, such as how to manage the complexity of the robot and environment model to efficiently ...
- **p. 1 / 1 Introduction - extractive PDF cue:** As participants in the DARPA Robotics Challenge (DRC), we are particularly interested in tasks related to disaster relief, such as walking outdoors over irregular terrain ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Several practical challenges arise in the design of these systems, such as how to manage the complexity of the robot and environment ... | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | Note that inputs computed by solving this QP are, in general, not equal to those computed by thresholding the output of the ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF |
| State / latent | Note, inputs, computed, solving, general, equal, thresholding, output, closed-form, LQR | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | LQR, solutions, recomputed, online, typically, separate, thread, current | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: Note, inputs, computed, solving, general, equal, thresholding, output, closed-form, LQR | p. 10 (4.1 General formulation), p. 11 (4.4 Additional costs and constraints), p. 14 (5.1 Requirements and approach) |
| Decision / output variable | joint/whole-body action; body terms: Unfortunately, safe, terrain, unlikely, convex, even, connected, environment | p. 4 (3.1 Footstep planning as a mixed-integer convex), p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: Then, solve, optimization, problem, assigns, contacts, regions, minimizes | p. 3 (3.1 Footstep planning as a mixed-integer convex), p. 7 (3.1.3 Determining the number of footsteps), p. 8 (3.2 Dynamic motion planning), p. 9 (3.2 Dynamic motion planning), p. 12 (4.4 Additional costs and constraints), p. 10 (4.1 General formulation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 10 (4.1 General formulation), p. 13 (4.5 Efficient QP solver), p. 3 (3.1 Footstep planning as a mixed-integer convex) |
| Success / guarantee | motion/task success and recovery | p. 19 (6.1 State estimation evaluation), p. 19 (6.1 State estimation evaluation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive PDF cue:** As participants in the DARPA Robotics Challenge (DRC), we are particularly interested in tasks related to disaster relief, such as walking outdoors over irregular terrain ...
- **p. 2 / 1 Introduction - extractive PDF cue:** However, for complex humanoid systems like Atlas, solving trajectory optimization problems using the full dynamics can be computationally prohibitive.
- **p. 2 / 1 Introduction - extractive PDF cue:** Despite significant kinematic sensor limitations due to backlash and actuator deflection, our experiments demonstrate a measurable improvement in our ability to estimate the robot's state ...

## What the Paper Changes

PDF contribution framing (p. 4 (3.1 Footstep planning as a mixed-integer convex), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): Unfortunately, the set of safe terrain is unlikely to be convex or even connected: in an environment as simple as a staircase, the safe terrain consists of the top surface ...

- **p. 1 / 1 Introduction - extractive PDF cue:** In this paper we describe our approach to addressing these problems with Atlas.
- **p. 1 / 1 Introduction - extractive PDF cue:** Our approach to walking combines an efficient footstep planner with a simple dynamic model of the robot to efficiently compute desired walking trajectories.
- **p. 2 / 1 Introduction - extractive PDF cue:** We show that the robot is capable of walking over nontrivial terrain while maintaining extremely low drift from the desired footstep trajectory-a critically important capability ...
- **p. 2 / 1 Introduction - extractive PDF cue:** 6 we describe several experiments performed on the physical robot evaluatingthestateestimationandcontrolalgorithmsinpractice.We also describe recent simulation results of controlled highly dynamic motions that are currently being ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 20 | The robot's trailing foot eventually collided with the front of the step resulting in a fall. | reported limitation/failure wording; scope must be verified |
| body cue at p. 20 | This scenario requires great precision, if the state estimator drifts by even a few centimeters, the robot will ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 22 | 13), require at least 3cm of clearance between links to avoid self-collisions, and constrain the gaze of the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 19 | In the manipulation experiment, the LIDAR contribution actually degrades performance slightly due to occlusions caused by arm motions. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 10 (4.1 General formulation), p. 11 (4.4 Additional costs and constraints), p. 14 (5.1 Requirements and approach), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 10 (4.1 General formulation), p. 11 (4.4 Additional costs and constraints), p. 14 (5.1 Requirements and approach), p. 2 (1 Introduction), objective p. 3 (3.1 Footstep planning as a mixed-integer convex), p. 7 (3.1.3 Determining the number of footsteps), p. 8 (3.2 Dynamic motion planning), p. 9 (3.2 Dynamic motion planning), p. 12 (4.4 Additional costs and constraints), p. 10 (4.1 General formulation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
