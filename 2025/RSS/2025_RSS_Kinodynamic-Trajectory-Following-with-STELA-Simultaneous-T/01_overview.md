# Kinodynamic Trajectory Following with STELA: Simultaneous Trajectory Estimation & Local Adaptation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss21/p008.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss21/p008.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: NEXT
- Tags: Robotics, trajectory following, state estimation, motion planning, online adaptation, mobile robot
- Official paper: https://www.roboticsproceedings.org/rss21/p008.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss21/p008.pdf
- Code/Project: https://go.rutgers.edu/46618xjt
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 control 문제를 이해하기 위해 읽는다. 본문은 They can sinnultaneously solve trajectory estimation and control or planning challenges as a unified problem [22, 29]. ‘These solutions를 문제로 두고, The sliding, window mechanism allows the factor graph to be dynamically updated at high frequency by operating over a limited past history and forward horizon of the planned trajectory. ‘The ‘combination of ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** State estimation and control are often addressed separately, leading to unsafe execution due to sensing noise, execution errors, and diserepancies between the planning model ‘and ...
- **p. 1 / Abstract - extractive body cue:** Simultaneous control and trajectory estimation using probabilistic graphical models has been proposed as a tuned solution 10 these challenges.
- **p. 1 / Abstract - extractive body cue:** Previous work, however, iors and is Timited to
- **p. 1 / Abstract - extractive body cue:** The current methods to vehicles ullaneous ‘Trajectory
- **p. 1 / Abstract - extractive body cue:** past trajectory based on noisy observations, and (ii) adapts the controls to be executed to mi deviations from the planned, feasible trajectory, while avoiding collisions.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** They can sinnultaneously solve trajectory estimation and control or planning challenges as a unified problem [22, 29]. ‘These solutions
- **p. 2 / 1. INTRODUCTION - extractive body cue:** While system identification [16, 3, 44] can reduce the model gap. it does not fully address it.

## Core Idea

- **p. 3 / 1. INTRODUCTION - extractive body cue:** The sliding, window mechanism allows the factor graph to be dynamically updated at high frequency by operating over a limited past history and forward horizon ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** Motion planning consists of finding a plan for a robot to ‘move in an environment from a stating state to a desired goal region without ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Proposed Method and Contribution: ‘The proposed 'STELA framework first calls an asymptotically optimal SEXP for kinodynamic systems (23, 27] in order to acquire a feasible, ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** This allows the optimizer to stretch or contract edges depending oon the estimated state of the system.
- **p. 5 / B. Trajectory Optimization as a Motion Planner - extractive body cue:** 3: An 6 for robot planning employs the robot's model dy = Folds.) on a dynamics factor to compute a trajectory of T states, Sarting ...
- **p. 5 / B. Trajectory Optimization as a Motion Planner - extractive body cue:** Beyond the ternary dynamics factor, there are costs imposed for the optimization by unary factors for obstacle avoidance (e(X.x)) over the intermediate state variables (X ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | However, observation and actuation noise ‘can lead to errors in state estimation, where the focus is often filtering, i.e., estimating the latest robot pose incrementally. | joint/task state, reference와 sensor feedback | p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |
| State/latent | However, observation, actuation, noise, lead, errors, state, estimation, where, focus, often, filtering | state estimate, task-space error와 control decision | p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 4 (1. INTRODUCTION) |
| Output/action | ‘An approach to deal with the model gap is to use feedback controllers for trajectory following, given the latest state estimate [12, 33]. | torque, force, velocity 또는 position command | p. 2 (1. INTRODUCTION), p. 4 (1. INTRODUCTION), p. 4 (1. INTRODUCTION) |
| Objective/outcome | Motion planning can be seen as an optimization problem where the cost of the trajectory eost(r) produced by the plan Pr is minimized subject to i) star state condition: 7(0) = tai) ... | tracking, stability, constraint satisfaction과 contact behavior | p. 5 (B. Trajectory Optimization as a Motion Planner), p. 5 (B. Trajectory Optimization as a Motion Planner) |

## Main Claims and Actual Contribution

- **p. 3 / 1. INTRODUCTION - extractive body cue:** The sliding, window mechanism allows the factor graph to be dynamically updated at high frequency by operating over a limited past history and forward horizon ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** Motion planning consists of finding a plan for a robot to ‘move in an environment from a stating state to a desired goal region without ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Proposed Method and Contribution: ‘The proposed 'STELA framework first calls an asymptotically optimal SEXP for kinodynamic systems (23, 27] in order to acquire a feasible, ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** This allows the optimizer to stretch or contract edges depending oon the estimated state of the system.
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a trajectory traversed before a collision (no data ...
- **p. 12 / A. Experimemal setup - extractive body cue:** The low= cost trajectories returned from the SBMP are likely, however, to be in close proximity to obstacles, which makes following them susceptible to collisions ...
- **p. 11 / A. Experimemal setup - extractive body cue:** Simulation Results , / eee ‘Tables Ill, and Ill show the success rate of each algoPed rithm per environment for the LTV-SDE system in simulation ...
- **p. 12 / A. Experimemal setup - extractive body cue:** It also significantly outperforms alternatives in simulated evaluations as noise increases, while achieving desirable high-frequency control update rates,

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 11 (Figure/Table caption), p. 12 (A. Experimemal setup) |
| Embodiment/environment | Given the identified robot model /, (1, us). an environment ‘map that identifies obstacle regions %, and a motion planning query specifying 9 and Xq. the approach ealls an asymptotically optimal kinodynamie ... | hardware/simulator version and reset protocol | p. 5 (V. SIMULTANEOUS TRAIECTORY ESTIMATION), p. 9 (A. Experimemal setup) |
| Dataset/benchmark | Real experiments are performed with a MuSHR [40] robot the scenes of Figures / and 8. | role, split, size and leakage | p. 5 (V. SIMULTANEOUS TRAIECTORY ESTIMATION), p. 9 (A. Experimemal setup), p. 12 (A. Experimemal setup), p. 8 (A. Experimemal setup) |
| Metric | Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a trajectory traversed before a collision (no data if the success rate is 100%). Trajectory ... | definition, denominator, direction and uncertainty | p. 11 (Figure/Table caption), p. 11 (A. Experimemal setup), p. 12 (A. Experimemal setup) |
| Baseline/ablation | The baseline comparison point is open-loop execution of the desired trajectory. | fair input/data/compute/action matching | p. 10 (A. Experimemal setup), p. 11 (A. Experimemal setup), p. 12 (A. Experimemal setup) |

## Explicit Limitations and Failure Boundary

- **p. 12 / A. Experimemal setup - extractive body cue:** The "multiple obstacles" environment is similar to the setups from simulated experiments, where collisions with obstacles are considered failures.
- **p. 12 / A. Experimemal setup - extractive body cue:** The second environment considers a set of movable boxes that are not present during planning, and the robot ‘can collide online without considering a failure, ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a trajectory traversed before a collision (no data ...
- **p. 6 / B. The STELA Factor Graph - extractive body cue:** While the SEMP trajectory initialization is collision-free, a robot may move dangerously close to obstacles due to the model gap and noise.
- **p. 11 / A. Experimemal setup - extractive body cue:** 13 for both STEZA and SCATE. e OPEN-LOOP showeases the effects of noise on the system's as/ 2? dynamics, resulting in collisions as soon as ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 14: The effects of state-space noise in collision on the Forest environment for the Open-loop baseline (left) and the proposed STELA (middle). The top ...
- **p. 5 / B. Trajectory Optimization as a Motion Planner - extractive body cue:** In previous factor graph approaches, these limitations are alleviated by using a holonomic robot modeled via a Gaussian Process and relying (on random re-initializations,

## Why Read It

Planning and control의 control 문제를 이해하기 위해 읽는다. 본문은 They can sinnultaneously solve trajectory estimation and control or planning challenges as a unified problem [22, 29]. ‘These solutions를 문제로 두고, The sliding, window mechanism allows the factor graph to be dynamically updated at high frequency by operating over a limited past history and forward horizon of the planned trajectory. ‘The ‘combination of ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 4 (1. INTRODUCTION), p. 5 (B. Trajectory Optimization as a Motion Planner) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** They can sinnultaneously solve trajectory estimation and control or planning challenges as a unified problem [22, 29]. ‘These solutions (p. 2, 1. INTRODUCTION).
- **Actual contribution:** Motion planning consists of finding a plan for a robot to ‘move in an environment from a stating state to a desired goal region without collisions. (p. 3, 1. INTRODUCTION).
- **Evaluation boundary:** Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a trajectory traversed before a collision (no data if the success rate is ... (p. 11, Figure/Table caption).
- **Explicit failure boundary:** The extreme noise level oj results mostly in failures, where 24% of failures arise from Indeterminant Linear System Exception, i. the accumulation of numerical errors, which does not occur for ... (p. 12, A. Experimemal setup).
