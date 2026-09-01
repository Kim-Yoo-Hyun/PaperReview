# Problem - Information Theoretic MPC for Model-Based Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ieeexplore.ieee.org/document/7989202/; PDF retrieval source: https://ieeexplore.ieee.org/document/7989202/. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): Despite all of the progress on both model-based and model-free RL methods, generalization remains a primary challenge.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We introduce an information theoretic model predictive control (MPC) algorithm capable of handling complex cost criteria and general nonlinear dynamics.
- **p. 1 / Abstract - extractive body cue:** The generality of the approach makes it possible to use multi-layer neural networks as dynamics models, which we incorporate into our MPC algorithm in order ...
- **p. 1 / Abstract - extractive body cue:** We test the algorithm in simulation on a cartpole swing up and quadrotor navigation task, as well as on actual hardware in an aggressive driving ...
- **p. 1 / Abstract - extractive body cue:** Empirical results demonstrate that the algorithm is capable of achieving a high level of performance and does so only utilizing data collected from the system.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Many robotic tasks can be framed as reinforcement learning (RL) problems, where a robot seeks to optimize a cost function encoding a task by utilizing ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Despite all of the progress on both model-based and model-free RL methods, generalization remains a primary challenge.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, in prior work, MPPI could only be applied to systems with control affine dynamics.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Despite all of the progress on both model-based and model-free RL methods, generalization remains a primary challenge. | robot mechanism의 state와 task-space dynamics | body wording is the source claim |
| Observation / input | The types of reinforcement learning problems encountered in robotic tasks are frequently in the continuous state-action space and high dimensional [1]. | joint/task state, reference와 sensor feedback | exact sensor/frame/preprocessing from PDF |
| State / latent | types, reinforcement, learning, problems, encountered, robotic, tasks, frequently, continuous, state-action | state estimate, task-space error와 control decision | notation and tensor shape require body check |
| Output / action | However, prior, works, geared, towards, updating, parameters, feedback | torque, force, velocity 또는 position command | exact unit/frame/decoder require body check |
| Target outcome | stability, tracking and constraint satisfaction | tracking, stability, constraint satisfaction과 contact behavior | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | q, q̇, x, wrench; body terms: types, reinforcement, learning, problems, encountered, robotic, tasks, frequently, continuous, state-action | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. MODEL PREDICTIVE CONTROL) |
| Decision / output variable | u/τ subject to dynamics and actuator/contact constraints; body terms: significant, step, forward, because, enables, purely, data-driven, model | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. MODEL PREDICTIVE CONTROL) |
| Objective / loss / cost | tracking or interaction error; cue terms: complexity, objectives, tasks, increases, computational, cost, optimization, major | p. 2 (II. MODEL PREDICTIVE CONTROL), p. 2 (II. MODEL PREDICTIVE CONTROL) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (II. MODEL PREDICTIVE CONTROL), p. 2 (II. MODEL PREDICTIVE CONTROL) |
| Success / guarantee | stability, tracking and constraint satisfaction | p. 6 (V. SIMULATED RESULTS), p. 6 (V. SIMULATED RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, in prior work, MPPI could only be applied to systems with control affine dynamics.

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. MODEL PREDICTIVE CONTROL)): This is a significant step forward because it enables a purely data-driven approach to model learning within the MPPI framework.

- **p. 1 / I. INTRODUCTION - extractive body cue:** This limits the method's ability to discover novel optimal control behaviors.
- **p. 2 / II. MODEL PREDICTIVE CONTROL - extractive body cue:** The information theoretic MPC algorithm that we develop is originally based on path integral control theory.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | Running the algorithm without a bootstrapped neural network results in repeated failures. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The slip angle is defined as -arctan( vy /vx/), where vx and vy are the longitudinal and lateral ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | M(x, y) is the cost-map value at the position (x, y), and Sc is an indicator variable which ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | During training, we set the slip angle threshold to 15.76 degrees (0.275 radians), and for the final testing ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

control writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. MODEL PREDICTIVE CONTROL), p. 2 (II. MODEL PREDICTIVE CONTROL). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. MODEL PREDICTIVE CONTROL), p. 2 (II. MODEL PREDICTIVE CONTROL), objective p. 2 (II. MODEL PREDICTIVE CONTROL), p. 2 (II. MODEL PREDICTIVE CONTROL).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
