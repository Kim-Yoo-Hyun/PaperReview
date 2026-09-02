# Method - Differentiable Robust Model Predictive Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p003.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p003.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC), p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC), p. 3 (II. MATHEMATICAL BACKGROUND), p. 4 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 7 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL)): However, we propose an alternative methodology enabled through differentiable optimization that allows the parameters to be learned and adapted online through minimization of an appropriately specified loss function describing the ...

## Method Body Digest

- **p. 5 / III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL - extractive body cue:** However, we propose an alternative methodology enabled through differentiable optimization that allows the parameters to be learned and adapted online through minimization of an appropriately ...
- **p. 8 / IV. DIFFERENTIABLE TUBE-BASED MPC - extractive body cue:** In order to optimize both the nominal and ancillary controller, we propose to use a loss function of the form L(τ ∗(θ), ¯τ(¯θ)) =
- **p. 8 / IV. DIFFERENTIABLE TUBE-BASED MPC - extractive body cue:** Next, we propose an algorithm that applies the DOC methodology presented in Section III to the real-time tuning of tube-based controllers of the form given ...
- **p. 3 / II. MATHEMATICAL BACKGROUND - extractive body cue:** To address this shortcoming, tube-based MPC augments the nominal controller with a feedback model predictive controller that drives the state of the true system towards ...
- **p. 4 / III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL - extractive body cue:** This prevents needing to store the entire trajectory of derivatives in memory at once, which is an important consideration for highly parameterized problems, e.g., when ...
- **p. 7 / III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL - extractive body cue:** Let the Jacobians of the dynamics fxk, fuk, fθk and the Hessians of the stateaction value function Q(k) uu , Q(k) ux , and Q(k) ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The first formulates the problem as a min-max optimization, finding a control policy that minimizes the cost under worst-case disturbances.
- **p. 6 / III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL - extractive body cue:** Algorithm 1: Differentiable Optimal Control (DOC) Input: Derivatives of L (equivalently f, ℓ, ϕ, and ξ) and L along the solution z∗ Output: Gradient of ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contribution of this work is the development of a novel differentiable tube-based MPC (DT-MPC) framework for safe, robust control.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the main contributions of this work include: 1) the derivation of a general differentiable optimal control framework enabled through a novel application of ...
- **p. 1 / Abstract - extractive body cue:** Drawing parallels with differential dynamic programming, the IFT enables the derivation of an efficient differentiable optimal control framework.

## Source Evidence Cues

- **p. 5 / III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL - extractive body cue:** However, we propose an alternative methodology enabled through differentiable optimization that allows the parameters to be learned and adapted online through minimization of an appropriately ...
- **p. 8 / IV. DIFFERENTIABLE TUBE-BASED MPC - extractive body cue:** In order to optimize both the nominal and ancillary controller, we propose to use a loss function of the form L(τ ∗(θ), ¯τ(¯θ)) =
- **p. 8 / IV. DIFFERENTIABLE TUBE-BASED MPC - extractive body cue:** Next, we propose an algorithm that applies the DOC methodology presented in Section III to the real-time tuning of tube-based controllers of the form given ...
- **p. 3 / II. MATHEMATICAL BACKGROUND - extractive body cue:** To address this shortcoming, tube-based MPC augments the nominal controller with a feedback model predictive controller that drives the state of the true system towards ...
- **p. 4 / III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL - extractive body cue:** This prevents needing to store the entire trajectory of derivatives in memory at once, which is an important consideration for highly parameterized problems, e.g., when ...
- **p. 7 / III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL - extractive body cue:** Let the Jacobians of the dynamics fxk, fuk, fθk and the Hessians of the stateaction value function Q(k) uu , Q(k) ux , and Q(k) ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The first formulates the problem as a min-max optimization, finding a control policy that minimizes the cost under worst-case disturbances.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / error representation | motion·force 목표를 제어 error로 바꾼다 | joint/task state, reference, wrench | task frame, Jacobian, impedance, selection 또는 error coordinates를 구성 | desired task command | However, we propose an alternative methodology enabled through differentiable optimization that allows the parameters to be learned and adapted online through minimization ... | p. 5 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC) |
| Dynamics / constraint solve | 목표를 feasible actuator command로 바꾼다 | error, model, constraints | inverse dynamics, QP, MPC, operational mapping 또는 feedback law를 계산 | torque, force, velocity 또는 position command | In order to optimize both the nominal and ancillary controller, we propose to use a loss function of the form L(τ ∗(θ), ... | p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC), p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC) |
| Feedback / actuation | 실제 state와 disturbance에 따라 command를 닫힌 loop로 보정한다 | sensor feedback과 nominal command | tracking correction, saturation, null-space, fallback 또는 replan을 수행 | next actuation과 response | Next, we propose an algorithm that applies the DOC methodology presented in Section III to the real-time tuning of tube-based controllers of ... | p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC), p. 3 (II. MATHEMATICAL BACKGROUND) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL - extractive body cue:** Algorithm 1: Differentiable Optimal Control (DOC) Input: Derivatives of L (equivalently f, ℓ, ϕ, and ξ) and L along the solution z∗ Output: Gradient of ...
- **p. 4 / III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL - extractive body cue:** Consider the unconstrained minimization problem z∗(θ) = arg min z φ(z, θ), (3) where φ : Rnz×Rnθ →R is twice continuously differentiable, z is the ...
- **p. 2 / II. MATHEMATICAL BACKGROUND - extractive body cue:** The nominal MPC problem is, therefore, given as: Problem 1 (Nominal MPC). ¯τ = arg min τ ¯J(τ) := N-1 X k=0 ¯ℓ(xk, uk) + ...
- **p. 5 / III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL - extractive body cue:** The solution τ ∗depends on the problem parameters θ, which represent the parts of the dynamics and the objective that are learnable or adaptable, such ...
- **p. 8 / IV. DIFFERENTIABLE TUBE-BASED MPC - extractive body cue:** In our algorithm, the parameterization of ¯X with ¯θ is enabled through the adoption of barrier states for enforcing safety constraints and their penalizations in ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The first formulates the problem as a min-max optimization, finding a control policy that minimizes the cost under worst-case disturbances.
- **Formal bridge:** q, q̇, x, wrench -> u/τ subject to dynamics and actuator/contact constraints -> tracking or interaction error -> stability, tracking and constraint satisfaction.
- **Equation/algorithm anchors:** p. 6 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 5 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 5 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 6 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC), p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Safety, enforced, through, discrete, barrier, states, enables, scalable, constraint, satisfaction, safe, planning, control, executed | joint/task state, reference와 sensor feedback | body cue; exact tensor/frame verify |
| State/latent | Safety, enforced, through, discrete, barrier, states, enables, scalable, constraint, satisfaction | state estimate, task-space error와 control decision | body cue; notation verify |
| Action/output | main, contribution, development, novel, differentiable, tube-based, MPC, DT-MPC, framework, safe | torque, force, velocity 또는 position command | body cue; unit/decoder verify |
| Objective/constraint | Algorithm, Differentiable, Optimal, Control, DOC, Input, Derivatives, equivalently, along, solution | tracking or interaction error | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / I. INTRODUCTION - extractive body cue:** Safety is enforced through the use of discrete barrier states [3], which enables scalable constraint satisfaction such that safe planning and control can be executed ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This allows for an implicit form of feedback since the controls are reoptimized from the current state of the system at every time step of ...
- **p. 3 / II. MATHEMATICAL BACKGROUND - extractive body cue:** To address this shortcoming, tube-based MPC augments the nominal controller with a feedback model predictive controller that drives the state of the true system towards ...
- **p. 3 / II. MATHEMATICAL BACKGROUND - extractive body cue:** In essence, the barrier function B is replaced with the relaxed barrier function by taking a Taylor series approximation of the safety function h around ...
- **p. 6 / III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL - extractive body cue:** Algorithm 1: Differentiable Optimal Control (DOC) Input: Derivatives of L (equivalently f, ℓ, ϕ, and ξ) and L along the solution z∗ Output: Gradient of ...
- **p. 7 / III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL - extractive body cue:** Let the Jacobians of the dynamics fxk, fuk, fθk and the Hessians of the stateaction value function Q(k) uu , Q(k) ux , and Q(k) ...
- **p. 8 / IV. DIFFERENTIABLE TUBE-BASED MPC - extractive body cue:** This has the effect of increasing the state dimension of the problem but does not affect the algorithm computationally as the input dimension is unchanged ...
- **Normalized interface:** observation=joint/task state, reference와 sensor feedback; state=state estimate, task-space error와 control decision; output/action=torque, force, velocity 또는 position command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instantaneous or receding-horizon reference tracking; exact prediction horizon은 exact value not recovered from the selected body cues. | The nominal MPC problem is, therefore, given as: Problem 1 (Nominal MPC). ¯τ = arg min τ ¯J(τ) := N-1 X k=0 ... | episode/sequence/action-chunk boundary |
| Rate / latency | sensor/actuator control tick마다 feedback solve; numeric rate는 paper-specific. | This puts the proposed framework to the test, especially in comparison to the non-adaptive, nonlinear tube-based MPC. | Hz/fps, inference time and control rate |
| Memory | 현재 joint/task state, reference, contact/wrench feedback; long history 여부 확인 필요. | not recovered | window and reset |
| Compute | dynamics/Jacobian evaluation, QP/MPC/inverse-dynamics solve와 actuator latency가 결정한다. | The nominal MPC problem is, therefore, given as: Problem 1 (Nominal MPC). ¯τ = arg min τ ¯J(τ) := N-1 X k=0 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL - extractive body cue:** However, we propose an alternative methodology enabled through differentiable optimization that allows the parameters to be learned and adapted online through minimization of an appropriately ...
- **p. 1 / Abstract - extractive body cue:** The proposed algorithm is benchmarked on multiple nonlinear robotic systems, including two systems in the MuJoCo simulator environment and one hardware experiment on the Robotarium ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** However, alternative, methodology, enabled, through, differentiable, optimization, allows, parameters, learned, adapted, online, minimization, appropriately, specified, loss, function, describing, desired, task.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / error representation | The generality of the proposed DT-MPC is established through benchmarks on five nonlinear robotics systems subject to highly non-convex constraints such as ... | p. 9 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS) |
| Dynamics / constraint solve | 8), a state-of-the-art, remotely accessible robotics hardware platform for multi-agent control [52]. | p. 11 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS) |
| Feedback / actuation | On the other hand, the proposed DT-MPC bounds the true system within a safer tube around the nominal trajectory by tuning the ... | p. 10 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 9 / V. EXPERIMENTS - extractive body cue:** In the experiments that follow, the nominal MPC is tuned to perform the task successfully and then the algorithms are deployed on the true system, ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** For this task, the nominal controller (tuned for deterministic task completion) is too aggressive for the magnitude of disturbances received, leading to a large number ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** The results in Table I show that, while NT-MPC fails to reach the target in the majority of the cases and occasionally violates the safety ...
- **p. 11 / V. EXPERIMENTS - extractive body cue:** While the deterministic nominal trajectory reaches the target state during every trial, the ancillary controller cannot keep up with the desired aggressive jumping maneuver due ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 4: Controlled Dubins vehicle trajectories subject to large noise. NT-MPC trajectories diverge from the nominal trajec- tory and the uncertainty increases over time. Meanwhile, ...
- **p. 11 / V. EXPERIMENTS - extractive body cue:** NT-MPC is robust to disturbances due to both modeling error and process noise and can reach the target state successfully (Fig.
- **p. 9 / V. EXPERIMENTS - extractive body cue:** While both algorithms remain safe and avoid collisions (see Table I), only DT-MPC is able to complete the task the majority of the time.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC), p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC), p. 3 (II. MATHEMATICAL BACKGROUND), p. 4 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 7 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), objective p. 6 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 4 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 2 (II. MATHEMATICAL BACKGROUND), p. 5 (III. GENERALIZED DIFFERENTIABLE OPTIMAL CONTROL), p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC), p. 1 (I. INTRODUCTION), temporal p. 2 (II. MATHEMATICAL BACKGROUND), p. 9 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 10 (V. EXPERIMENTS), p. 11 (VI. CONCLUSION), p. 1 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
