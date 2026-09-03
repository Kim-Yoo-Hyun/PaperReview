# Method - Control-Limited Differential Dynamic Programming

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ICRA.2014.6907001; PDF retrieval source: https://roboti.us/lab/papers/TassaICRA14.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 3 (III. CONTROL LIMITS), p. 3 (C. Line Search), p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING)): Trajectory optimization is the process of finding a statecontrol sequence which locally minimizes a given cost function.

## Method Body Digest

- **p. 1 / I. INTRODUCTION - extractive body cue:** Trajectory optimization is the process of finding a statecontrol sequence which locally minimizes a given cost function.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Because the dynamics are folded into the optimization, state-control trajectories are always strictly feasible and "dynamic constraints" are unnecessary.
- **p. 2 / II. DIFFERENTIAL DYNAMIC PROGRAMMING - extractive body cue:** The dynamics is modeled by the generic function f xi+1 = f(xi,ui), (1) which describes the evolution from time i to i+1 of the state ...
- **p. 3 / III. CONTROL LIMITS - extractive body cue:** Na¨ıve Clamping A first attempt to enforce box constraints is to clamp the controls in the forward-pass.
- **p. 3 / C. Line Search - extractive body cue:** Once the backward pass is completed, the proposed locally-linear policy is evaluated with a forward pass: ˆx0 = x0 (7a) ˆui = ui + αki ...
- **p. 2 / II. DIFFERENTIAL DYNAMIC PROGRAMMING - extractive body cue:** Plugging this policy back into the expansion of Q, a quadratic model of V is obtained.
- **p. 4 / III. CONTROL LIMITS - extractive body cue:** The warm-start requirement rules out some classes of algorithms, for example interior-point methods.
- **p. 4 / III. CONTROL LIMITS - extractive body cue:** while minimizing the quadratic model of Q, which amounts to solving a quadratic program (QP) subject to the box constraints (8) at each timestep.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** Finally, Section IV describes the results, illustrating the usefulness of our approach.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show experimentally in simulation that simplistic ways of handling them are inefficient and detrimental to convergence.

## Source Evidence Cues

- **p. 1 / I. INTRODUCTION - extractive body cue:** Trajectory optimization is the process of finding a statecontrol sequence which locally minimizes a given cost function.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Because the dynamics are folded into the optimization, state-control trajectories are always strictly feasible and "dynamic constraints" are unnecessary.
- **p. 2 / II. DIFFERENTIAL DYNAMIC PROGRAMMING - extractive body cue:** The dynamics is modeled by the generic function f xi+1 = f(xi,ui), (1) which describes the evolution from time i to i+1 of the state ...
- **p. 3 / III. CONTROL LIMITS - extractive body cue:** Na¨ıve Clamping A first attempt to enforce box constraints is to clamp the controls in the forward-pass.
- **p. 3 / C. Line Search - extractive body cue:** Once the backward pass is completed, the proposed locally-linear policy is evaluated with a forward pass: ˆx0 = x0 (7a) ˆui = ui + αki ...
- **p. 2 / II. DIFFERENTIAL DYNAMIC PROGRAMMING - extractive body cue:** Plugging this policy back into the expansion of Q, a quadratic model of V is obtained.
- **p. 4 / III. CONTROL LIMITS - extractive body cue:** The warm-start requirement rules out some classes of algorithms, for example interior-point methods.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / error representation | motion·force 목표를 제어 error로 바꾼다 | joint/task state, reference, wrench | task frame, Jacobian, impedance, selection 또는 error coordinates를 구성 | desired task command | Trajectory optimization is the process of finding a statecontrol sequence which locally minimizes a given cost function. | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Dynamics / constraint solve | 목표를 feasible actuator command로 바꾼다 | error, model, constraints | inverse dynamics, QP, MPC, operational mapping 또는 feedback law를 계산 | torque, force, velocity 또는 position command | Because the dynamics are folded into the optimization, state-control trajectories are always strictly feasible and "dynamic constraints" are unnecessary. | p. 1 (I. INTRODUCTION), p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING) |
| Feedback / actuation | 실제 state와 disturbance에 따라 command를 닫힌 loop로 보정한다 | sensor feedback과 nominal command | tracking correction, saturation, null-space, fallback 또는 replan을 수행 | next actuation과 response | The dynamics is modeled by the generic function f xi+1 = f(xi,ui), (1) which describes the evolution from time i to i+1 ... | p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 3 (III. CONTROL LIMITS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / I. INTRODUCTION - extractive body cue:** Trajectory optimization is the process of finding a statecontrol sequence which locally minimizes a given cost function.
- **p. 4 / III. CONTROL LIMITS - extractive body cue:** while minimizing the quadratic model of Q, which amounts to solving a quadratic program (QP) subject to the box constraints (8) at each timestep.
- **p. 1 / I. INTRODUCTION - extractive body cue:** It would be appealing to specify the behavior of a robot in terms of simple cost functions, and let an intelligent control algorithm handle the ...
- **p. 2 / II. DIFFERENTIAL DYNAMIC PROGRAMMING - extractive body cue:** (6c) The backward pass begins by initializing the Value function with the terminal cost and its derivatives VN = ℓf(xN), and then recursively computing (5) ...
- **p. 3 / III. CONTROL LIMITS - extractive body cue:** Due to the strict feasibility property of indirect methods, inequality constraints on the state are handled automatically under the condition that f maintains regularity, which ...
- **p. 4 / III. CONTROL LIMITS - extractive body cue:** The problem is written: minimize δu Q(δx,δu) (11) subject to ¯b ⩽u + δu ⩽¯b The QP is a well understood problem with many methods ...
- **Formal bridge:** q, q̇, x, wrench -> u/τ subject to dynamics and actuator/contact constraints -> tracking or interaction error -> stability, tracking and constraint satisfaction.
- **Equation/algorithm anchors:** p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 3 (III. CONTROL LIMITS), p. 3 (III. CONTROL LIMITS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | locally-linear, feedback, policy, Q-1, uuQu, uuQux, feed-forward, modification, gain, matrix, respectively, Although, indirect, methods | joint/task state, reference와 sensor feedback | body cue; exact tensor/frame verify |
| State/latent | locally-linear, feedback, policy, Q-1, uuQu, uuQux, feed-forward, modification, gain, matrix | state estimate, task-space error와 control decision | body cue; notation verify |
| Action/output | Finally, Section, describes, illustrating, usefulness, experimentally, simulation, simplistic, ways, handling | torque, force, velocity 또는 position command | body cue; unit/decoder verify |
| Objective/constraint | Trajectory, optimization, process, finding, statecontrol, sequence, locally, minimizes, given, cost | tracking or interaction error | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / II. DIFFERENTIAL DYNAMIC PROGRAMMING - extractive body cue:** (5a) This is a locally-linear feedback policy with k ≜-Q-1 uuQu and K ≜-Q-1 uuQux (5b) the feed-forward modification and feedback gain matrix, respectively.
- **p. 1 / Abstract - extractive body cue:** Although indirect methods automatically take into account state constraints, control limits pose a difficulty.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This is also the idea behind the task-function [1] or the operational-space [2] approaches: instead of working in the configuration space, the motion is specified ...
- **p. 3 / C. Line Search - extractive body cue:** Once the backward pass is completed, the proposed locally-linear policy is evaluated with a forward pass: ˆx0 = x0 (7a) ˆui = ui + αki ...
- **p. 2 / II. DIFFERENTIAL DYNAMIC PROGRAMMING - extractive body cue:** The states X are recovered by integration of (1) from the initial state x0.
- **p. 3 / III. CONTROL LIMITS - extractive body cue:** Clamping can also be introduced to the control modification k in (5): k ←⟦k + u⟧b -u, and it might also seem sensible that the ...
- **p. 4 / III. CONTROL LIMITS - extractive body cue:** This decomposition is used to compute the optimal feedback gain Kf = -Quu,fQux.
- **Normalized interface:** observation=joint/task state, reference와 sensor feedback; state=state estimate, task-space error와 control decision; output/action=torque, force, velocity 또는 position command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instantaneous or receding-horizon reference tracking; exact prediction horizon은 exact value was not selected from the PDF body. | The Dynamic Programming Principle then reduces the minimization over a sequence of controls Ui, to a sequence of minimizations over a single ... | episode/sequence/action-chunk boundary |
| Rate / latency | sensor/actuator control tick마다 feedback solve; numeric rate는 paper-specific. | The regularization parameter and the descent step length α are adapted online following a LevenbergMarquardt heuristic. | Hz/fps, inference time and control rate |
| Memory | 현재 joint/task state, reference, contact/wrench feedback; long history 여부 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | dynamics/Jacobian evaluation, QP/MPC/inverse-dynamics solve와 actuator latency가 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / I. INTRODUCTION - extractive body cue:** Because the dynamics are folded into the optimization, state-control trajectories are always strictly feasible and "dynamic constraints" are unnecessary.
- **p. 3 / III. CONTROL LIMITS - extractive body cue:** Na¨ıve Clamping A first attempt to enforce box constraints is to clamp the controls in the forward-pass.
- **p. 1 / Abstract - extractive body cue:** Differential Dynamic Programming (DDP) is an indirect method which optimizes only over the unconstrained control-space and is therefore fast enough to allow real-time control of ...
- **p. 2 / II. DIFFERENTIAL DYNAMIC PROGRAMMING - extractive body cue:** Quadratic Approximation DDP involves iterating a forward pass (or rollout) which integrates (1) for a given U, followed by a backward pass which compute a ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Trajectory, optimization, process, finding, statecontrol, sequence, locally, minimizes, given, cost, function, Because, dynamics, folded, state-control, trajectories, always, strictly, feasible, dynamic.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / error representation | Finally, we demonstrate box-DDP on a complex platform, the humanoid robot HRP-2. | p. 4 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Dynamics / constraint solve | The bottom row of Figure 2 shows a comparison between the clamping and squashing heuristics and the proposed algorithm. | p. 4 (IV. RESULTS), p. 4 (IV. RESULTS) |
| Feedback / actuation | However, despite some recent work in this direction [34], direct feed-forward current control is not yet a functional option, while the lack ... | p. 6 (IV. RESULTS), p. 5 (IV. RESULTS) |

## Failure and Ablation Link

- ablation/failure PDF body cue not selected; no claim inferred

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 3 (III. CONTROL LIMITS), p. 3 (C. Line Search), p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), objective p. 1 (I. INTRODUCTION), p. 4 (III. CONTROL LIMITS), p. 1 (I. INTRODUCTION), p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 3 (III. CONTROL LIMITS), p. 4 (III. CONTROL LIMITS), temporal p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 3 (C. Line Search), p. 4 (III. CONTROL LIMITS), p. 6 (IV. RESULTS), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Trajectory optimization is the process of finding a statecontrol sequence which locally minimizes a given cost function. (p. 1, I. INTRODUCTION).
- **Objective/update evidence:** Trajectory optimization is the process of finding a statecontrol sequence which locally minimizes a given cost function. (p. 1, I. INTRODUCTION).
- **Temporal/runtime evidence:** The Dynamic Programming Principle then reduces the minimization over a sequence of controls Ui, to a sequence of minimizations over a single control, proceeding backwards in time: V (x) = ... (p. 2, II. DIFFERENTIAL DYNAMIC PROGRAMMING).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
