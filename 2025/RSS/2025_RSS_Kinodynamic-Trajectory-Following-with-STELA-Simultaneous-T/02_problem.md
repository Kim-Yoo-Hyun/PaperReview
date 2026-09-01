# Problem - Kinodynamic Trajectory Following with STELA: Simultaneous Trajectory Estimation & Local Adaptation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p008.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p008.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 4 (1. INTRODUCTION)): They can sinnultaneously solve trajectory estimation and control or planning challenges as a unified problem [22, 29]. ‘These solutions

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** State estimation and control are often addressed separately, leading to unsafe execution due to sensing noise, execution errors, and diserepancies between the planning model ‘and ...
- **p. 1 / Abstract - extractive body cue:** Simultaneous control and trajectory estimation using probabilistic graphical models has been proposed as a tuned solution 10 these challenges.
- **p. 1 / Abstract - extractive body cue:** Previous work, however, iors and is Timited to
- **p. 1 / Abstract - extractive body cue:** The current methods to vehicles ullaneous ‘Trajectory
- **p. 1 / Abstract - extractive body cue:** past trajectory based on noisy observations, and (ii) adapts the controls to be executed to mi deviations from the planned, feasible trajectory, while avoiding collisions.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** They can sinnultaneously solve trajectory estimation and control or planning challenges as a unified problem [22, 29]. ‘These solutions
- **p. 2 / 1. INTRODUCTION - extractive body cue:** While system identification [16, 3, 44] can reduce the model gap. it does not fully address it.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | They can sinnultaneously solve trajectory estimation and control or planning challenges as a unified problem [22, 29]. ‘These solutions | robot mechanism의 state와 task-space dynamics | body wording is the source claim |
| Observation / input | However, observation and actuation noise ‘can lead to errors in state estimation, where the focus is often filtering, i.e., estimating the latest ... | joint/task state, reference와 sensor feedback | exact sensor/frame/preprocessing from PDF |
| State / latent | However, observation, actuation, noise, lead, errors, state, estimation, where, focus | state estimate, task-space error와 control decision | notation and tensor shape require body check |
| Output / action | wypical, unjectory, estimation, time, uses, state, observations, robot | torque, force, velocity 또는 position command | exact unit/frame/decoder require body check |
| Target outcome | stability, tracking and constraint satisfaction | tracking, stability, constraint satisfaction과 contact behavior | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | q, q̇, x, wrench; body terms: However, observation, actuation, noise, lead, errors, state, estimation, where, focus | p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 4 (1. INTRODUCTION) |
| Decision / output variable | u/τ subject to dynamics and actuator/contact constraints; body terms: sliding, window, mechanism, allows, factor, graph, dynamically, updated | p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |
| Objective / loss / cost | tracking or interaction error; cue terms: Motion, planning, seen, optimization, problem, where, cost, trajectory | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (B. Trajectory Optimization as a Motion Planner), p. 5 (B. Trajectory Optimization as a Motion Planner) |
| Success / guarantee | stability, tracking and constraint satisfaction | p. 11 (Figure/Table caption), p. 11 (A. Experimemal setup), p. 12 (A. Experimemal setup) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. INTRODUCTION - extractive body cue:** While system identification [16, 3, 44] can reduce the model gap. it does not fully address it.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** challenge convergence and may require careful definition of parameters, such as obstacle potentials [36].
- **p. 3 / 1. INTRODUCTION - extractive body cue:** An interleaving approach uses a graph to generate suggestions used by an optimizer [31] ‘Simultaneous localization and planning (SLAP) [1] models the challenge as a ...
- **p. 4 / 1. INTRODUCTION - extractive body cue:** Due to the gap between the true dynamics J and the planning model ,, the executed robot trajectory 77(rj,pr) does not match the planned trajectory ...

## What the Paper Changes

PDF contribution framing (p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION)): The sliding, window mechanism allows the factor graph to be dynamically updated at high frequency by operating over a limited past history and forward horizon of the planned trajectory. ‘The ...

- **p. 3 / 1. INTRODUCTION - extractive body cue:** Motion planning consists of finding a plan for a robot to ‘move in an environment from a stating state to a desired goal region without ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Proposed Method and Contribution: ‘The proposed 'STELA framework first calls an asymptotically optimal SEXP for kinodynamic systems (23, 27] in order to acquire a feasible, ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** This allows the optimizer to stretch or contract edges depending oon the estimated state of the system.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 12 | The "multiple obstacles" environment is similar to the setups from simulated experiments, where collisions with obstacles are considered ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | The second environment considers a set of movable boxes that are not present during planning, and the robot ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | While the SEMP trajectory initialization is collision-free, a robot may move dangerously close to obstacles due to the ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

control writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 4 (1. INTRODUCTION), p. 4 (1. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 4 (1. INTRODUCTION), interface p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 4 (1. INTRODUCTION), p. 4 (1. INTRODUCTION), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
