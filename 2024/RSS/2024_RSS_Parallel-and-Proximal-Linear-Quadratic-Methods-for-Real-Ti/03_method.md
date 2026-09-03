# Method - Parallel and Proximal Linear-Quadratic Methods for Real-Time Constrained Model-Predictive Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p002.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p002.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY), p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY)): OPTIMIZER We now consider a nonlinear discrete-time trajectory optimization problem with implicit system dynamics: min x,u J(x,u) = N-1 ∑ t=0 ℓt(xt,ut)+ℓN(xN) (48a) s.t. x0 = x0 (48b) φt(xt,ut,xt+1) = ...

## Method Body Digest

- **p. 8 / VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY - extractive body cue:** OPTIMIZER We now consider a nonlinear discrete-time trajectory optimization problem with implicit system dynamics: min x,u J(x,u) = N-1 ∑ t=0 ℓt(xt,ut)+ℓN(xN) (48a) s.t. x0 ...
- **p. 8 / VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY - extractive body cue:** The coefficients of the problem are obtained from the derivatives of (48) with the following equivalences: At = φx,t Bt = φu,t Et = φy,t ...
- **p. 4 / III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM - extractive body cue:** Algorithm 1: Generalized Riccati equations for proximal, constrained LQ problem Data: Cost and constraint matrices Qt,St,Rt,qt,rt,At,Bt,Ct,Et,Dt, ft,ht 1 PN ←QN + 1 µC⊤ NCN; 2 ...
- **p. 3 / III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM - extractive body cue:** We introduce the primal-dual feedforward (resp. feedback) gains (k1,ζ1,ω2,a1) (resp.
- **p. 3 / III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM - extractive body cue:** (K1,Z1,Ω2,M1)) for the control, constraint multiplier, co-state and next state, so that the parametric solution in (u1,ν1,λ2,x2) is: u1 = k1 +K1x1, ν1 = ζ1 ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** More recently, Nielsen and Axehill [38] subdivide the LQR problem into subproblems with state-control linkage constraints; this approach involves computing nullspace matrices to handle infeasible ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Laine and Tomlin [34] suggest subdivision of the LQR problem into a set of subproblems with state linkage constraints at the endpoints; the linkage constraints' ...
- **p. 4 / III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM - extractive body cue:** Although obtained differently, it is the same as proposed in [28].

## Design Rationale

- **p. 4 / III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM - extractive body cue:** We present this as a secondary contribution of this paper, which we have implemented and evaluated in the experimental section.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we introduce a parallel algorithm to enhance the efficiency of model-predictive control (MPC) solvers [49, 16].
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a general direct solver for LQ problems with implicit dynamics and additional equality constraints, leveraging parameterization to formulate a parallel ...

## Source Evidence Cues

- **p. 8 / VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY - extractive body cue:** OPTIMIZER We now consider a nonlinear discrete-time trajectory optimization problem with implicit system dynamics: min x,u J(x,u) = N-1 ∑ t=0 ℓt(xt,ut)+ℓN(xN) (48a) s.t. x0 ...
- **p. 8 / VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY - extractive body cue:** The coefficients of the problem are obtained from the derivatives of (48) with the following equivalences: At = φx,t Bt = φu,t Et = φy,t ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | OPTIMIZER We now consider a nonlinear discrete-time trajectory optimization problem with implicit system dynamics: min x,u J(x,u) = N-1 ∑ t=0 ℓt(xt,ut)+ℓN(xN) ... | p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY), p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | The coefficients of the problem are obtained from the derivatives of (48) with the following equivalences: At = φx,t Bt = φu,t ... | p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | OPTIMIZER We now consider a nonlinear discrete-time trajectory optimization problem with implicit system dynamics: min x,u J(x,u) = N-1 ∑ t=0 ℓt(xt,ut)+ℓN(xN) ... | p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 8 / VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY - extractive body cue:** OPTIMIZER We now consider a nonlinear discrete-time trajectory optimization problem with implicit system dynamics: min x,u J(x,u) = N-1 ∑ t=0 ℓt(xt,ut)+ℓN(xN) (48a) s.t. x0 ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Algorithm, Generalized, Riccati, equations, proximal, constrained, problem, Data, Cost, constraint, matrices, NCN, Backward, pass | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | Algorithm, Generalized, Riccati, equations, proximal, constrained, problem, Data, Cost, constraint | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | present, secondary, contribution, have, implemented, evaluated, experimental, section, introduce, parallel | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | OPTIMIZER, consider, nonlinear, discrete-time, trajectory, optimization, problem, implicit, system, dynamics | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM - extractive body cue:** Algorithm 1: Generalized Riccati equations for proximal, constrained LQ problem Data: Cost and constraint matrices Qt,St,Rt,qt,rt,At,Bt,Ct,Et,Dt, ft,ht 1 PN ←QN + 1 µC⊤ NCN; 2 ...
- **p. 3 / III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM - extractive body cue:** We introduce the primal-dual feedforward (resp. feedback) gains (k1,ζ1,ω2,a1) (resp.
- **p. 3 / III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM - extractive body cue:** (K1,Z1,Ω2,M1)) for the control, constraint multiplier, co-state and next state, so that the parametric solution in (u1,ν1,λ2,x2) is: u1 = k1 +K1x1, ν1 = ζ1 ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** More recently, Nielsen and Axehill [38] subdivide the LQR problem into subproblems with state-control linkage constraints; this approach involves computing nullspace matrices to handle infeasible ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Laine and Tomlin [34] suggest subdivision of the LQR problem into a set of subproblems with state linkage constraints at the endpoints; the linkage constraints' ...
- **p. 4 / III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM - extractive body cue:** Although obtained differently, it is the same as proposed in [28].
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | Horizon window is set to 0.5 s with a timestep of 10 ms for a total of N = 50 steps. | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | The horizon is set to 0.96 s, with a 12 ms timestep, resulting in a discrete-time horizon of N = 80. | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | Horizon window is set to 0.5 s with a timestep of 10 ms for a total of N = 50 steps. | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY - extractive body cue:** OPTIMIZER We now consider a nonlinear discrete-time trajectory optimization problem with implicit system dynamics: min x,u J(x,u) = N-1 ∑ t=0 ℓt(xt,ut)+ℓN(xN) (48a) s.t. x0 ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** OPTIMIZER, consider, nonlinear, discrete-time, trajectory, optimization, problem, implicit, system, dynamics, N-1, coefficients, obtained, derivatives, following, equivalences, quantities, directly, applying, semismooth.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | 1) TALOS locomotion benchmarks: We consider a wholebody trajectory optimization problem on a TALOS [47] humanoid robot with constrained 6D contacts. | p. 9 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS) |
| Balance-aware whole-body execution | 4, our proximal solver with various parallelization settings is compared against the feasibility-prone DDP from the CROCODDYL library [36]. | p. 9 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS) |
| Recovery / adaptation | It is the authors' aim to improve its efficiency in the future. | p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 9 / VII. DISCUSSION - extractive body cue:** In our setting, the linear subproblem (47) does not have that same structure (such that our construction from section V cannot be iterated), however, it ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY), p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY), objective p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY), temporal p. 10 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 8 (VII. DISCUSSION), p. 4 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** OPTIMIZER We now consider a nonlinear discrete-time trajectory optimization problem with implicit system dynamics: min x,u J(x,u) = N-1 ∑ t=0 ℓt(xt,ut)+ℓN(xN) (48a) s.t. x0 = x0 (48b) φt(xt,ut,xt+1) = ... (p. 8, VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY).
- **Objective/update evidence:** OPTIMIZER We now consider a nonlinear discrete-time trajectory optimization problem with implicit system dynamics: min x,u J(x,u) = N-1 ∑ t=0 ℓt(xt,ut)+ℓN(xN) (48a) s.t. x0 = x0 (48b) φt(xt,ut,xt+1) = ... (p. 8, VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY).
- **Temporal/runtime evidence:** We consider three instances of the problem with different time horizons, encompassing two full steps of the robot. (p. 9, VIII. EXPERIMENTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
