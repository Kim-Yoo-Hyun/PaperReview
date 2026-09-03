# Method - Push Anything: Single- and Multi-Object Pushing From First Sight with Contact-Implicit MPC

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2510.19974; PDF retrieval source: https://arxiv.org/pdf/2510.19974. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (A. Hybrid Models for Contact Dynamics), p. 3 (A. Hybrid Models for Contact Dynamics), p. 4 (IV. METHODS), p. 4 (IV. METHODS), p. 6 (IV. METHODS), p. 5 (IV. METHODS)): A compact representation for contact dynamics uses complementarity constraints: xk+1 = f(xk, uk, λk), (1a) 0 ≤λk ⊥Φ(xk, uk, λk) ≥0, (1b) where xk ∈Rnx is the state, uk ∈Rnu ...

## Method Body Digest

- **p. 3 / A. Hybrid Models for Contact Dynamics - extractive body cue:** A compact representation for contact dynamics uses complementarity constraints: xk+1 = f(xk, uk, λk), (1a) 0 ≤λk ⊥Φ(xk, uk, λk) ≥0, (1b) where xk ∈Rnx ...
- **p. 3 / A. Hybrid Models for Contact Dynamics - extractive body cue:** Hybrid models capture these behaviors by switching dynamics depending on the active contact mode.
- **p. 4 / IV. METHODS - extractive body cue:** While using linearized terms, this model preserves the multi-modal nature of contact dynamics through the complementarity constraint (3b).
- **p. 4 / IV. METHODS - extractive body cue:** The set D comprises all feasible z satisfying the coupled constraints across time: the linear dynamics (5b), the slack-variable equality (5c), and initial and state/input ...
- **p. 6 / IV. METHODS - extractive body cue:** We note that the concurrent work [15] independently developed an approach similar to C3+, though in the context of an inverse dynamics controller.
- **p. 5 / IV. METHODS - extractive body cue:** While this could theoretically be applied to all contacts, in
- **p. 5 / IV. METHODS - extractive body cue:** Visualization of the selected contact pairs in planar pushing task. yielding a significant overall speedup.
- **p. 4 / IV. METHODS - extractive body cue:** Combining this LCS model with a standard quadratic cost function yields a Quadratic Program with Complementarity Constraints (QPCC), a well-known class of non-convex optimization problems ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** We introduce Push Anything, a manipulation pipeline for real-time planar pushing of a wide variety of objects, including multi-object scenes.
- **p. 3 / IV. METHODS - extractive body cue:** Our framework operates in two phases.
- **p. 3 / IV. METHODS - extractive body cue:** We present the Push Anything framework (Fig.

## Source Evidence Cues

- **p. 3 / A. Hybrid Models for Contact Dynamics - extractive body cue:** A compact representation for contact dynamics uses complementarity constraints: xk+1 = f(xk, uk, λk), (1a) 0 ≤λk ⊥Φ(xk, uk, λk) ≥0, (1b) where xk ∈Rnx ...
- **p. 3 / A. Hybrid Models for Contact Dynamics - extractive body cue:** Hybrid models capture these behaviors by switching dynamics depending on the active contact mode.
- **p. 4 / IV. METHODS - extractive body cue:** While using linearized terms, this model preserves the multi-modal nature of contact dynamics through the complementarity constraint (3b).
- **p. 4 / IV. METHODS - extractive body cue:** The set D comprises all feasible z satisfying the coupled constraints across time: the linear dynamics (5b), the slack-variable equality (5c), and initial and state/input ...
- **p. 6 / IV. METHODS - extractive body cue:** We note that the concurrent work [15] independently developed an approach similar to C3+, though in the context of an inverse dynamics controller.
- **p. 5 / IV. METHODS - extractive body cue:** While this could theoretically be applied to all contacts, in
- **p. 5 / IV. METHODS - extractive body cue:** Visualization of the selected contact pairs in planar pushing task. yielding a significant overall speedup.
- **Detected method headings:** A. Hybrid Models for Contact Dynamics (p. 3); IV. METHODS (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / error representation | motion·force 목표를 제어 error로 바꾼다 | joint/task state, reference, wrench | task frame, Jacobian, impedance, selection 또는 error coordinates를 구성 | desired task command | A compact representation for contact dynamics uses complementarity constraints: xk+1 = f(xk, uk, λk), (1a) 0 ≤λk ⊥Φ(xk, uk, λk) ≥0, (1b) ... | p. 3 (A. Hybrid Models for Contact Dynamics), p. 3 (A. Hybrid Models for Contact Dynamics) |
| Dynamics / constraint solve | 목표를 feasible actuator command로 바꾼다 | error, model, constraints | inverse dynamics, QP, MPC, operational mapping 또는 feedback law를 계산 | torque, force, velocity 또는 position command | Hybrid models capture these behaviors by switching dynamics depending on the active contact mode. | p. 3 (A. Hybrid Models for Contact Dynamics), p. 4 (IV. METHODS) |
| Feedback / actuation | 실제 state와 disturbance에 따라 command를 닫힌 loop로 보정한다 | sensor feedback과 nominal command | tracking correction, saturation, null-space, fallback 또는 replan을 수행 | next actuation과 response | While using linearized terms, this model preserves the multi-modal nature of contact dynamics through the complementarity constraint (3b). | p. 4 (IV. METHODS), p. 4 (IV. METHODS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / IV. METHODS - extractive body cue:** Combining this LCS model with a standard quadratic cost function yields a Quadratic Program with Complementarity Constraints (QPCC), a well-known class of non-convex optimization problems ...
- **p. 4 / IV. METHODS - extractive body cue:** (6) Here, zT = [zT 0 , zT 1 , ..., zT N-1], δT = [δT 0 , δT 1 , ..., δT N-1], c(z) ...
- **p. 3 / A. Hybrid Models for Contact Dynamics - extractive body cue:** This increases the number of variables and constraints, but often leads to better-conditioned problems. min x0:N,u0:N-1,λ0:N-1 N-1 X k=0 ℓ(xk, uk) + ℓf(xN) (2a) s.t. ...
- **p. 5 / IV. METHODS - extractive body cue:** (10) Unlike C3, C3+ augments the set D with an additional linear equality constraint on ηk as given in (5c).
- **p. 5 / IV. METHODS - extractive body cue:** The introduction of a slack variable means that the non-convex component, the complementarity constraint, becomes decoupled across contacts.
- **p. 3 / A. Hybrid Models for Contact Dynamics - extractive body cue:** Different end effector positions are shown with their associated MPC costs.
- **Formal bridge:** q, q̇, x, wrench -> u/τ subject to dynamics and actuator/contact constraints -> tracking or interaction error -> stability, tracking and constraint satisfaction.
- **Equation/algorithm anchors:** p. 3 (A. Hybrid Models for Contact Dynamics), p. 4 (IV. METHODS), p. 4 (IV. METHODS), p. 5 (IV. METHODS), p. 3 (A. Hybrid Models for Contact Dynamics), p. 5 (IV. METHODS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | comprises, feasible, satisfying, coupled, constraints, across, time, linear, dynamics, slack-variable, equality, initial, state/input, bounds | joint/task state, reference와 sensor feedback | body cue; exact tensor/frame verify |
| State/latent | comprises, feasible, satisfying, coupled, constraints, across, time, linear, dynamics, slack-variable | state estimate, task-space error와 control decision | body cue; notation verify |
| Action/output | introduce, Push, Anything, manipulation, pipeline, real-time, planar, pushing, wide, variety | torque, force, velocity 또는 position command | body cue; unit/decoder verify |
| Objective/constraint | Combining, LCS, model, standard, quadratic, cost, function, yields, Program, Complementarity | tracking or interaction error | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / IV. METHODS - extractive body cue:** The set D comprises all feasible z satisfying the coupled constraints across time: the linear dynamics (5b), the slack-variable equality (5c), and initial and state/input ...
- **p. 3 / A. Hybrid Models for Contact Dynamics - extractive body cue:** A compact representation for contact dynamics uses complementarity constraints: xk+1 = f(xk, uk, λk), (1a) 0 ≤λk ⊥Φ(xk, uk, λk) ≥0, (1b) where xk ∈Rnx ...
- **p. 3 / A. Hybrid Models for Contact Dynamics - extractive body cue:** This increases the number of variables and constraints, but often leads to better-conditioned problems. min x0:N,u0:N-1,λ0:N-1 N-1 X k=0 ℓ(xk, uk) + ℓf(xN) (2a) s.t. ...
- **p. 4 / IV. METHODS - extractive body cue:** To do so efficiently, we approximate (1) by linearizing f and Φ with respect to x, u, and λ, where x comprises of the current ...
- **p. 5 / IV. METHODS - extractive body cue:** Additionally, we terminate after the quadratic step, as empirical observations indicate this yields better performance.
- **p. 5 / IV. METHODS - extractive body cue:** For each timestep, the task is to project the output from the first step onto the simple complementarity set Hk: min δk ∥δk -(zi+1 k ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Moreover, tasks involving complex multi-object interactions, such as resolving cluttered scenes, remain intractable for prior CIMPC methods as problem complexity grows exponentially with the number ...
- **Normalized interface:** observation=joint/task state, reference와 sensor feedback; state=state estimate, task-space error와 control decision; output/action=torque, force, velocity 또는 position command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instantaneous or receding-horizon reference tracking; exact prediction horizon은 exact value not recovered from the selected body cues. | Results For Multi-Object Pushing In the 3- and 4-object tasks, we shorten the planning horizon to maintain a real-time control rate, as ... | episode/sequence/action-chunk boundary |
| Rate / latency | sensor/actuator control tick마다 feedback solve; numeric rate는 paper-specific. | To resolve this, we detect and correct sudden, implausibly large changes in orientation between consecutive timesteps by selecting the pose that maintains ... | Hz/fps, inference time and control rate |
| Memory | 현재 joint/task state, reference, contact/wrench feedback; long history 여부 확인 필요. | 2) Multi-Object Tracking: To track multiple objects, we run multiple instances of FoundationPose [31] in parallel, directly sharing memory access to the ... | window and reset |
| Compute | dynamics/Jacobian evaluation, QP/MPC/inverse-dynamics solve와 actuator latency가 결정한다. | System diagram of the Push Anything framework. ject-environment contacts (demonstrated with up to 19 contact pairs), while planning over a multi-step horizon ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / A. Hybrid Models for Contact Dynamics - extractive body cue:** A compact representation for contact dynamics uses complementarity constraints: xk+1 = f(xk, uk, λk), (1a) 0 ≤λk ⊥Φ(xk, uk, λk) ≥0, (1b) where xk ∈Rnx ...
- **p. 4 / IV. METHODS - extractive body cue:** While using linearized terms, this model preserves the multi-modal nature of contact dynamics through the complementarity constraint (3b).
- **p. 4 / IV. METHODS - extractive body cue:** The set D comprises all feasible z satisfying the coupled constraints across time: the linear dynamics (5b), the slack-variable equality (5c), and initial and state/input ...
- **p. 3 / IV. METHODS - extractive body cue:** In the online phase, our controller uses robot and object state estimates to compute end effector trajectories.
- **p. 4 / IV. METHODS - extractive body cue:** (6) Here, zT = [zT 0 , zT 1 , ..., zT N-1], δT = [δT 0 , δT 1 , ..., δT N-1], c(z) ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** compact, representation, contact, dynamics, uses, complementarity, constraints, where, Rnx, state, Rnu, control, input, forces, signed, distance, function, between, potential, pairs.
- **Relevant PDF headings:** A. Hybrid Models for Contact Dynamics (p. 3); IV. METHODS (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / error representation | 8, we evaluated our method in 701 hardware trials, testing 25 objects, with each object run until 28 successful trials were obtained. | p. 6 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS) |
| Dynamics / constraint solve | For the Push T task, our framework achieves a mean time-to-goal of 26.9 s, improving upon prior work [4] at 30.5 s ... | p. 7 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS) |
| Feedback / actuation | The system achieved a 99.9% success rate (700/701), with the only failure occurring when the large egg carton was pushed out of ... | p. 6 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS) |

## Failure and Ablation Link

- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 7. Visualization of the selected contact pairs in planar pushing task. yielding a significant overall speedup. As defined below and illustrated in Fig. 5, ...
- **p. 7 / VI. LIMITATIONS AND FUTURE WORK - extractive body cue:** Another limitation is we model all objects with identical mass and inertia.
- **p. 6 / V. HARDWARE EXPERIMENTS - extractive body cue:** The system achieved a 99.9% success rate (700/701), with the only failure occurring when the large egg carton was pushed out of the robot's
- **p. 7 / V. HARDWARE EXPERIMENTS - extractive body cue:** All failures occurred when an object moved beyond the robot's reach.
- **p. 6 / V. HARDWARE EXPERIMENTS - extractive body cue:** We predefine contact geometries, but contact point pairs and their corresponding normals are determined dynamically via collision detection at each control loop.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (A. Hybrid Models for Contact Dynamics), p. 3 (A. Hybrid Models for Contact Dynamics), p. 4 (IV. METHODS), p. 4 (IV. METHODS), p. 6 (IV. METHODS), p. 5 (IV. METHODS), objective p. 4 (IV. METHODS), p. 4 (IV. METHODS), p. 3 (A. Hybrid Models for Contact Dynamics), p. 5 (IV. METHODS), p. 5 (IV. METHODS), p. 3 (A. Hybrid Models for Contact Dynamics), temporal p. 7 (V. HARDWARE EXPERIMENTS), p. 4 (IV. METHODS), p. 6 (V. HARDWARE EXPERIMENTS), p. 5 (IV. METHODS), p. 2 (I. INTRODUCTION), p. 3 (IV. METHODS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
