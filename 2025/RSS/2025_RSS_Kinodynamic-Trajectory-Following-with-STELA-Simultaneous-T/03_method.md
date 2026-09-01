# Method - Kinodynamic Trajectory Following with STELA: Simultaneous Trajectory Estimation & Local Adaptation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p008.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p008.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (B. Trajectory Optimization as a Motion Planner), p. 5 (B. Trajectory Optimization as a Motion Planner)): 3: An 6 for robot planning employs the robot's model dy = Folds.) on a dynamics factor to compute a trajectory of T states, Sarting in % and ending in ...

## Method Body Digest

- **p. 5 / B. Trajectory Optimization as a Motion Planner - extractive body cue:** 3: An 6 for robot planning employs the robot's model dy = Folds.) on a dynamics factor to compute a trajectory of T states, Sarting ...
- **p. 5 / B. Trajectory Optimization as a Motion Planner - extractive body cue:** Beyond the ternary dynamics factor, there are costs imposed for the optimization by unary factors for obstacle avoidance (e(X.x)) over the intermediate state variables (X ...
- **p. 5 / B. Trajectory Optimization as a Motion Planner - extractive body cue:** Motion planning can be seen as an optimization problem where the cost of the trajectory eost(r) produced by the plan Pr is minimized subject to ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** However, observation and actuation noise ‘can lead to errors in state estimation, where the focus is often filtering, i.e., estimating the latest robot pose incrementally.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** ‘An approach to deal with the model gap is to use feedback controllers for trajectory following, given the latest state estimate [12, 33].
- **p. 4 / 1. INTRODUCTION - extractive body cue:** 2: A wypical unjectory estimation £6 at time T uses state observations 2*(0 : 7) and the robot model s+ = fg(ar, ue) to fenerate ...
- **p. 4 / 1. INTRODUCTION - extractive body cue:** ‘The robot has access to noisy sensing that provides discrete ‘measurements =(0), which partially inform about the robot's state 2(t), such as sensing the robot's ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** Motion planning consists of finding a plan for a robot to ‘move in an environment from a stating state to a desired goal region without ...

## Design Rationale

- **p. 3 / 1. INTRODUCTION - extractive body cue:** The sliding, window mechanism allows the factor graph to be dynamically updated at high frequency by operating over a limited past history and forward horizon ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** Motion planning consists of finding a plan for a robot to ‘move in an environment from a stating state to a desired goal region without ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Proposed Method and Contribution: ‘The proposed 'STELA framework first calls an asymptotically optimal SEXP for kinodynamic systems (23, 27] in order to acquire a feasible, ...

## Source Evidence Cues

- **p. 5 / B. Trajectory Optimization as a Motion Planner - extractive body cue:** 3: An 6 for robot planning employs the robot's model dy = Folds.) on a dynamics factor to compute a trajectory of T states, Sarting ...
- **p. 5 / B. Trajectory Optimization as a Motion Planner - extractive body cue:** Beyond the ternary dynamics factor, there are costs imposed for the optimization by unary factors for obstacle avoidance (e(X.x)) over the intermediate state variables (X ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / error representation | motion·force 목표를 제어 error로 바꾼다 | joint/task state, reference, wrench | task frame, Jacobian, impedance, selection 또는 error coordinates를 구성 | desired task command | 3: An 6 for robot planning employs the robot's model dy = Folds.) on a dynamics factor to compute a trajectory of ... | p. 5 (B. Trajectory Optimization as a Motion Planner), p. 5 (B. Trajectory Optimization as a Motion Planner) |
| Dynamics / constraint solve | 목표를 feasible actuator command로 바꾼다 | error, model, constraints | inverse dynamics, QP, MPC, operational mapping 또는 feedback law를 계산 | torque, force, velocity 또는 position command | Beyond the ternary dynamics factor, there are costs imposed for the optimization by unary factors for obstacle avoidance (e(X.x)) over the intermediate ... | p. 5 (B. Trajectory Optimization as a Motion Planner) |
| Feedback / actuation | 실제 state와 disturbance에 따라 command를 닫힌 loop로 보정한다 | sensor feedback과 nominal command | tracking correction, saturation, null-space, fallback 또는 replan을 수행 | next actuation과 response | 3: An 6 for robot planning employs the robot's model dy = Folds.) on a dynamics factor to compute a trajectory of ... | p. 5 (B. Trajectory Optimization as a Motion Planner) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / B. Trajectory Optimization as a Motion Planner - extractive body cue:** Motion planning can be seen as an optimization problem where the cost of the trajectory eost(r) produced by the plan Pr is minimized subject to ...
- **p. 5 / B. Trajectory Optimization as a Motion Planner - extractive body cue:** Beyond the ternary dynamics factor, there are costs imposed for the optimization by unary factors for obstacle avoidance (e(X.x)) over the intermediate state variables (X ...
- **Formal bridge:** q, q̇, x, wrench -> u/τ subject to dynamics and actuator/contact constraints -> tracking or interaction error -> stability, tracking and constraint satisfaction.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | However, observation, actuation, noise, lead, errors, state, estimation, where, focus, often, filtering, estimating, latest | joint/task state, reference와 sensor feedback | body cue; exact tensor/frame verify |
| State/latent | However, observation, actuation, noise, lead, errors, state, estimation, where, focus | state estimate, task-space error와 control decision | body cue; notation verify |
| Action/output | sliding, window, mechanism, allows, factor, graph, dynamically, updated, high, frequency | torque, force, velocity 또는 position command | body cue; unit/decoder verify |
| Objective/constraint | Motion, planning, seen, optimization, problem, where, cost, trajectory, eost, produced | tracking or interaction error | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. INTRODUCTION - extractive body cue:** However, observation and actuation noise ‘can lead to errors in state estimation, where the focus is often filtering, i.e., estimating the latest robot pose incrementally.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** ‘An approach to deal with the model gap is to use feedback controllers for trajectory following, given the latest state estimate [12, 33].
- **p. 4 / 1. INTRODUCTION - extractive body cue:** 2: A wypical unjectory estimation £6 at time T uses state observations 2*(0 : 7) and the robot model s+ = fg(ar, ue) to fenerate ...
- **p. 4 / 1. INTRODUCTION - extractive body cue:** ‘The robot has access to noisy sensing that provides discrete ‘measurements =(0), which partially inform about the robot's state 2(t), such as sensing the robot's ...
- **p. 5 / B. Trajectory Optimization as a Motion Planner - extractive body cue:** Beyond the ternary dynamics factor, there are costs imposed for the optimization by unary factors for obstacle avoidance (e(X.x)) over the intermediate state variables (X ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** Motion planning consists of finding a plan for a robot to ‘move in an environment from a stating state to a desired goal region without ...
- **p. 5 / B. Trajectory Optimization as a Motion Planner - extractive body cue:** 3: An 6 for robot planning employs the robot's model dy = Folds.) on a dynamics factor to compute a trajectory of T states, Sarting ...
- **Normalized interface:** observation=joint/task state, reference와 sensor feedback; state=state estimate, task-space error와 control decision; output/action=torque, force, velocity 또는 position command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instantaneous or receding-horizon reference tracking; exact prediction horizon은 exact value not recovered from the selected body cues. | The sliding, window mechanism allows the factor graph to be dynamically updated at high frequency by operating over a limited past history ... | episode/sequence/action-chunk boundary |
| Rate / latency | sensor/actuator control tick마다 feedback solve; numeric rate는 paper-specific. | ‘A plan pr is a sequence of T' piece-wise constant controls {uo,-++,ur-1)}s where each control uj is executed for a timestep At, ... | Hz/fps, inference time and control rate |
| Memory | 현재 joint/task state, reference, contact/wrench feedback; long history 여부 확인 필요. | The sliding, window mechanism allows the factor graph to be dynamically updated at high frequency by operating over a limited past history ... | window and reset |
| Compute | dynamics/Jacobian evaluation, QP/MPC/inverse-dynamics solve와 actuator latency가 결정한다. | The sliding, window mechanism allows the factor graph to be dynamically updated at high frequency by operating over a limited past history ... | hardware, batch and throughput |

## Training vs Inference

- **p. 12 / A. Experimemal setup - extractive body cue:** The low= cost trajectories returned from the SBMP are likely, however, to be in close proximity to obstacles, which makes following them susceptible to collisions ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** robot, planning, employs, model, Folds, dynamics, factor, compute, trajectory, states, Sarting, ending, goal, region, Nir, Beyond, ternary, there, costs, imposed.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / error representation | Given the identified robot model /, (1, us). an environment ‘map that identifies obstacle regions %, and a motion planning query specifying ... | p. 5 (V. SIMULTANEOUS TRAIECTORY ESTIMATION), p. 9 (A. Experimemal setup) |
| Dynamics / constraint solve | The baseline comparison point is open-loop execution of the desired trajectory. | p. 10 (A. Experimemal setup), p. 11 (A. Experimemal setup) |
| Feedback / actuation | Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a trajectory traversed before a ... | p. 11 (Figure/Table caption), p. 12 (A. Experimemal setup) |

## Failure and Ablation Link

- **p. 12 / A. Experimemal setup - extractive body cue:** The ablation evaluation of the effect of the sliding window size, the use of the duration AT' as a factor variable, the impact of the ...
- **p. 12 / A. Experimemal setup - extractive body cue:** The low= cost trajectories returned from the SBMP are likely, however, to be in close proximity to obstacles, which makes following them susceptible to collisions ...
- **p. 9 / A. Experimemal setup - extractive body cue:** (Bottom) The robot follows & desied trajectory planned without obstacles, During execution, the envionment has movable obstacles.
- **p. 10 / A. Experimemal setup - extractive body cue:** goal without collisions; the most critical metric for safety.
- **p. 10 / A. Experimemal setup - extractive body cue:** The second variant is initialized with the same desired plan from the SeMP as the proposed STELA approach.
- **p. 7 / C. Inference over a Sliding Window - extractive body cue:** 4le) ‘observation factors are fot used for the ‘local "adaptation ‘component of the optimization,
- **p. 7 / C. Inference over a Sliding Window - extractive body cue:** The prior, limit, and obstacle factors are not used for the trajectory estimation component of the optimization.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (B. Trajectory Optimization as a Motion Planner), p. 5 (B. Trajectory Optimization as a Motion Planner), objective p. 5 (B. Trajectory Optimization as a Motion Planner), p. 5 (B. Trajectory Optimization as a Motion Planner), temporal p. 3 (1. INTRODUCTION), p. 4 (1. INTRODUCTION), p. 5 (A. Trajectory Estimation), p. 1 (Front matter), p. 6 (B. The STELA Factor Graph), p. 6 (V. SIMULTANEOUS TRAIECTORY ESTIMATION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
