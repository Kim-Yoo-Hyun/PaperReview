# Method - Information Theoretic MPC for Model-Based Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ieeexplore.ieee.org/document/7989202/; PDF retrieval source: https://ieeexplore.ieee.org/document/7989202/. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (II. MODEL PREDICTIVE CONTROL), p. 2 (II. MODEL PREDICTIVE CONTROL)): The key difference between classical MPC and MPC for reinforcement learning is that RL tasks have complicated objectives beyond stabilization or tracking.

## Method Body Digest

- **p. 2 / II. MODEL PREDICTIVE CONTROL - extractive body cue:** The key difference between classical MPC and MPC for reinforcement learning is that RL tasks have complicated objectives beyond stabilization or tracking.
- **p. 2 / II. MODEL PREDICTIVE CONTROL - extractive body cue:** The complexity of the objectives in RL tasks increases the computational cost of the optimization, a major problem since optimization must occur in real time.
- **p. 2 / II. MODEL PREDICTIVE CONTROL - extractive body cue:** The resulting derivation and update law are closely related to the cross-entropy method for stochastic diffusion processes [19], as well as reward weighted regression [20].
- **p. 1 / I. INTRODUCTION - extractive body cue:** The types of reinforcement learning problems encountered in robotic tasks are frequently in the continuous state-action space and high dimensional [1].
- **p. 1 / I. INTRODUCTION - extractive body cue:** In the second paradigm, model-based RL approaches first learn a model of the system and then train a feedback control policy using the learned model ...
- **p. 2 / II. MODEL PREDICTIVE CONTROL - extractive body cue:** However, those prior works are geared towards updating the parameters of a feedback control policy, whereas we focus on optimizing an open-loop control plan for ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** This is a significant step forward because it enables a purely data-driven approach to model learning within the MPPI framework.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This limits the method's ability to discover novel optimal control behaviors.
- **p. 2 / II. MODEL PREDICTIVE CONTROL - extractive body cue:** The information theoretic MPC algorithm that we develop is originally based on path integral control theory.

## Source Evidence Cues

- **p. 2 / II. MODEL PREDICTIVE CONTROL - extractive body cue:** The key difference between classical MPC and MPC for reinforcement learning is that RL tasks have complicated objectives beyond stabilization or tracking.
- **p. 2 / II. MODEL PREDICTIVE CONTROL - extractive body cue:** The complexity of the objectives in RL tasks increases the computational cost of the optimization, a major problem since optimization must occur in real time.
- **Detected method headings:** II. MODEL PREDICTIVE CONTROL (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / error representation | motion·force 목표를 제어 error로 바꾼다 | joint/task state, reference, wrench | task frame, Jacobian, impedance, selection 또는 error coordinates를 구성 | desired task command | The key difference between classical MPC and MPC for reinforcement learning is that RL tasks have complicated objectives beyond stabilization or tracking. | p. 2 (II. MODEL PREDICTIVE CONTROL), p. 2 (II. MODEL PREDICTIVE CONTROL) |
| Dynamics / constraint solve | 목표를 feasible actuator command로 바꾼다 | error, model, constraints | inverse dynamics, QP, MPC, operational mapping 또는 feedback law를 계산 | torque, force, velocity 또는 position command | The complexity of the objectives in RL tasks increases the computational cost of the optimization, a major problem since optimization must occur ... | p. 2 (II. MODEL PREDICTIVE CONTROL) |
| Feedback / actuation | 실제 state와 disturbance에 따라 command를 닫힌 loop로 보정한다 | sensor feedback과 nominal command | tracking correction, saturation, null-space, fallback 또는 replan을 수행 | next actuation과 response | The key difference between classical MPC and MPC for reinforcement learning is that RL tasks have complicated objectives beyond stabilization or tracking. | p. 2 (II. MODEL PREDICTIVE CONTROL) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / II. MODEL PREDICTIVE CONTROL - extractive body cue:** The complexity of the objectives in RL tasks increases the computational cost of the optimization, a major problem since optimization must occur in real time.
- **p. 2 / II. MODEL PREDICTIVE CONTROL - extractive body cue:** The resulting derivation and update law are closely related to the cross-entropy method for stochastic diffusion processes [19], as well as reward weighted regression [20].
- **Formal bridge:** q, q̇, x, wrench -> u/τ subject to dynamics and actuator/contact constraints -> tracking or interaction error -> stability, tracking and constraint satisfaction.
- **Equation/algorithm anchors:** p. 2 (II. MODEL PREDICTIVE CONTROL), p. 2 (II. MODEL PREDICTIVE CONTROL).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | types, reinforcement, learning, problems, encountered, robotic, tasks, frequently, continuous, state-action, space, high, dimensional, second | joint/task state, reference와 sensor feedback | body cue; exact tensor/frame verify |
| State/latent | types, reinforcement, learning, problems, encountered, robotic, tasks, frequently, continuous, state-action | state estimate, task-space error와 control decision | body cue; notation verify |
| Action/output | significant, step, forward, because, enables, purely, data-driven, model, learning, within | torque, force, velocity 또는 position command | body cue; unit/decoder verify |
| Objective/constraint | complexity, objectives, tasks, increases, computational, cost, optimization, major, problem, since | tracking or interaction error | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive body cue:** The types of reinforcement learning problems encountered in robotic tasks are frequently in the continuous state-action space and high dimensional [1].
- **p. 1 / I. INTRODUCTION - extractive body cue:** In the second paradigm, model-based RL approaches first learn a model of the system and then train a feedback control policy using the learned model ...
- **p. 2 / II. MODEL PREDICTIVE CONTROL - extractive body cue:** However, those prior works are geared towards updating the parameters of a feedback control policy, whereas we focus on optimizing an open-loop control plan for ...
- **p. 2 / II. MODEL PREDICTIVE CONTROL - extractive body cue:** The key difference between classical MPC and MPC for reinforcement learning is that RL tasks have complicated objectives beyond stabilization or tracking.
- **Normalized interface:** observation=joint/task state, reference와 sensor feedback; state=state estimate, task-space error와 control decision; output/action=torque, force, velocity 또는 position command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instantaneous or receding-horizon reference tracking; exact prediction horizon은 exact value not recovered from the selected body cues. | The MPPI controller uses a time horizon of 2.5 seconds, a control frequency of 40 Hz, and performs 1200 samples every time-step. | episode/sequence/action-chunk boundary |
| Rate / latency | sensor/actuator control tick마다 feedback solve; numeric rate는 paper-specific. | Model predictive control (MPC) or receding horizon control tackles this problem by relying on online optimization of the cost function and is ... | Hz/fps, inference time and control rate |
| Memory | 현재 joint/task state, reference, contact/wrench feedback; long history 여부 확인 필요. | not recovered | window and reset |
| Compute | dynamics/Jacobian evaluation, QP/MPC/inverse-dynamics solve와 actuator latency가 결정한다. | The MPPI controller uses a time horizon of 2.5 seconds, a control frequency of 40 Hz, and performs 1200 samples every time-step. | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** Each training/test iteration consisted of three separate trial runs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** difference, between, classical, MPC, reinforcement, learning, tasks, have, complicated, objectives, beyond, stabilization, tracking, complexity, increases, computational, cost, optimization, major, problem.
- **Relevant PDF headings:** II. MODEL PREDICTIVE CONTROL (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / error representation | The bootstrapping dataset for the cart-pole comes from 5 minutes of multiple MPPI demonstrations using known dynamics but a different cost function ... | p. 5 (V. SIMULATED RESULTS), p. 6 (VI. EXPERIMENTAL RESULTS) |
| Dynamics / constraint solve | In our prior work, MPPI was successfully applied to this task using a physics-inspired model. | p. 6 (VI. EXPERIMENTAL RESULTS), p. 5 (V. SIMULATED RESULTS) |
| Feedback / actuation | After one iteration, the algorithm achieves the same level of performance regardless of which network is being used. | p. 5 (V. SIMULATED RESULTS), p. 6 (V. SIMULATED RESULTS) |

## Failure and Ablation Link

- **p. 5 / V. SIMULATED RESULTS - extractive body cue:** Running the algorithm without a bootstrapped neural network results in repeated failures.
- **p. 5 / V. SIMULATED RESULTS - extractive body cue:** Running the algorithm without a bootstrapped neural network results in repeated failures.
- **p. 6 / VI. EXPERIMENTAL RESULTS - extractive body cue:** The slip angle is defined as -arctan( vy /vx/), where vx and vy are the longitudinal and lateral velocities, respectively.
- **p. 6 / VI. EXPERIMENTAL RESULTS - extractive body cue:** M(x, y) is the cost-map value at the position (x, y), and Sc is an indicator variable which activates if the magnitude of the slip ...
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** During training, we set the slip angle threshold to 15.76 degrees (0.275 radians), and for the final testing runs we raised it to 21.5 degrees ...
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** Slip 10 m/s 10.34 9.93 8.05 38.68 11 m/s 9.97 9.43 8.71 34.65 12 m/s 9.88 9.47 8.63 43.72 13 m/s 9.74 9.36 8.44 48.70 ...
- **p. 5 / V. SIMULATED RESULTS - extractive body cue:** The temperature was set as λ = 1 and the system noise to (2.5, .25, .25, .25), where the 2.5 value corresponds to the thrust ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (II. MODEL PREDICTIVE CONTROL), p. 2 (II. MODEL PREDICTIVE CONTROL), objective p. 2 (II. MODEL PREDICTIVE CONTROL), p. 2 (II. MODEL PREDICTIVE CONTROL), temporal p. 6 (VI. EXPERIMENTAL RESULTS), p. 1 (I. INTRODUCTION), p. 2 (III. INFORMATION THEORETIC CONTROL), p. 5 (IV. MPC WITH NEURAL NETWORK DYNAMICS), p. 1 (I. INTRODUCTION), p. 2 (II. MODEL PREDICTIVE CONTROL).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
