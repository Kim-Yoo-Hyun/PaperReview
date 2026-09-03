# Method - Linear-time Differential Inverse Kinematics: an Augmented Lagrangian Perspective

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p110.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p110.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND), p. 6 (IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 3 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 5 (IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE)): By embracing AL techniques in the spirit of the rigid-body dynamics algorithms proposed by Featherstone, we introduce a method that solves equality-constrained differential IK problems with lineartime complexity.

## Method Body Digest

- **p. 1 / Abstract - extractive body cue:** By embracing AL techniques in the spirit of the rigid-body dynamics algorithms proposed by Featherstone, we introduce a method that solves equality-constrained differential IK problems ...
- **p. 2 / II. BACKGROUND - extractive body cue:** First introduced in the 1970s by [21], ADMM is tailored to convex constrained optimization problems with separable decision variables and objectives.
- **p. 2 / II. BACKGROUND - extractive body cue:** This idea has been first used to develop linear complexity forward dynamics algorithms by Vereshchagin [46], resulting in an algorithm practically identical to Featherstone's articulated ...
- **p. 6 / IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** Algorithm 1 Constrained IK algorithm LOIK Require: robot model, q, vinit i s, νinit, Href i s, vref i s, Ais, bis, νlb, νub, ρv, ...
- **p. 3 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** The proposed algorithm exploits this recursive relationship and enforces satisfaction of kinematics constraints (2a) and (2b) through back substitutions, resulting in an efficient and linear ...
- **p. 5 / IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** We first present the final constrained IK algorithm in Algorithm 1, where the equality-constrained QP IK sub-problem is solved on line 5 using the proposed ...
- **p. 6 / IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** Convergence checking in our solver is presented below: Algorithm 3 Convergence criteria Require: vis, ν, z, y, w, f, Href i s, vref i s, ...
- **p. 3 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** Consider the following IK problem: minimizing a quadratic tracking objective in link spatial velocities, subject to forward kinematics constraints, task space equality constraints and joint ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** 2) Inequality constraints: We propose an ADMM-based strategy dealing with inequality constraints, where each ADMM iteration is made efficient by using the aforementioned inner solver.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Therefore, our contributions can significantly accelerate these downstream computationally expensive downstream tasks.
- **p. 2 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** Constrained inverse kinematics ADMM formulation In the most general sense, first order constrained differential inverse kinematics can be formulated as a constrained QP problem: min ...

## Source Evidence Cues

- **p. 1 / Abstract - extractive body cue:** By embracing AL techniques in the spirit of the rigid-body dynamics algorithms proposed by Featherstone, we introduce a method that solves equality-constrained differential IK problems ...
- **p. 2 / II. BACKGROUND - extractive body cue:** First introduced in the 1970s by [21], ADMM is tailored to convex constrained optimization problems with separable decision variables and objectives.
- **p. 2 / II. BACKGROUND - extractive body cue:** This idea has been first used to develop linear complexity forward dynamics algorithms by Vereshchagin [46], resulting in an algorithm practically identical to Featherstone's articulated ...
- **p. 6 / IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** Algorithm 1 Constrained IK algorithm LOIK Require: robot model, q, vinit i s, νinit, Href i s, vref i s, Ais, bis, νlb, νub, ρv, ...
- **p. 3 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** The proposed algorithm exploits this recursive relationship and enforces satisfaction of kinematics constraints (2a) and (2b) through back substitutions, resulting in an efficient and linear ...
- **p. 5 / IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** We first present the final constrained IK algorithm in Algorithm 1, where the equality-constrained QP IK sub-problem is solved on line 5 using the proposed ...
- **p. 6 / IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** Convergence checking in our solver is presented below: Algorithm 3 Convergence criteria Require: vis, ν, z, y, w, f, Href i s, vref i s, ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | By embracing AL techniques in the spirit of the rigid-body dynamics algorithms proposed by Featherstone, we introduce a method that solves equality-constrained ... | p. 1 (Abstract), p. 2 (II. BACKGROUND) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | First introduced in the 1970s by [21], ADMM is tailored to convex constrained optimization problems with separable decision variables and objectives. | p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | This idea has been first used to develop linear complexity forward dynamics algorithms by Vereshchagin [46], resulting in an algorithm practically identical ... | p. 2 (II. BACKGROUND), p. 6 (IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** Consider the following IK problem: minimizing a quadratic tracking objective in link spatial velocities, subject to forward kinematics constraints, task space equality constraints and joint ...
- **p. 2 / II. BACKGROUND - extractive body cue:** This strategy was found to result in a computational cost comparable to the weighted QP strategy despite supporting strict prioritization of constraints.
- **p. 7 / B. Feasibility Detection - extractive body cue:** However, on links where no motion constraints are defined, the cost of computing them are fixed.
- **p. 7 / B. Feasibility Detection - extractive body cue:** The cost of computing quantities on line 3 and 4 varies depending on the dimension of the motion constraint on a specific link.
- **p. 6 / IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** Algorithm 1 Constrained IK algorithm LOIK Require: robot model, q, vinit i s, νinit, Href i s, vref i s, Ais, bis, νlb, νub, ρv, ...
- **p. 4 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** To make this explicit: zk+1 = arg min z LA(vk+1, νk+1, z, yk, wk) = arg min z ( IKbox(z) + wk⊤(νk+1 -z) + µk ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 3 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 6 (IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 5 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 6 (IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | indicates, form, state-feedback, control, hypothesis, when, viewing, problem, LQR, perspective, will, verified, Sec, causal | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | indicates, form, state-feedback, control, hypothesis, when, viewing, problem, LQR, perspective | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | Inequality, constraints, ADMM-based, strategy, dealing, where, ADMM, iteration, made, efficient | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | Consider, following, problem, minimizing, quadratic, tracking, objective, link, spatial, velocities | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** (14) indicates that νi is in the form of the state-feedback "control" hypothesis proposed in (9), when viewing problem (8) from the LQR perspective.
- **p. 4 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** This state-feedback "control" hypothesis (9) will be verified in Sec.
- **p. 4 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** The causal relationship defined by the index-shifted "dynamics" equation implies that in the state-feedback control sense, the feedback "control" νi should be defined using the ...
- **p. 3 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** The proposed algorithm exploits this recursive relationship and enforces satisfaction of kinematics constraints (2a) and (2b) through back substitutions, resulting in an efficient and linear ...
- **p. 2 / II. BACKGROUND - extractive body cue:** However, one major distinction between the current state-of-the-arts and our proposed solution is that our solver is able to efficiently exploit the specific sparsity patterns ...
- **p. 1 / Abstract - extractive body cue:** We measure computation times 2-3× shorter than the QP-based state of the art.
- **p. 1 / Abstract - extractive body cue:** Differential inverse kinematics is a core robotics problem whose state-of-the-art solutions are currently based on quadratic programming.
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | Our benchmark unrolls target trajectories for each scenario, with a time step δt = 5 ms and a trajectory duration of 10 ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | Top: primal residual at each time step. | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | Our benchmark unrolls target trajectories for each scenario, with a time step δt = 5 ms and a trajectory duration of 10 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Abstract - extractive body cue:** By embracing AL techniques in the spirit of the rigid-body dynamics algorithms proposed by Featherstone, we introduce a method that solves equality-constrained differential IK problems ...
- **p. 2 / II. BACKGROUND - extractive body cue:** First introduced in the 1970s by [21], ADMM is tailored to convex constrained optimization problems with separable decision variables and objectives.
- **p. 6 / IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** Algorithm 1 Constrained IK algorithm LOIK Require: robot model, q, vinit i s, νinit, Href i s, vref i s, Ais, bis, νlb, νub, ρv, ...
- **p. 3 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** The proposed algorithm exploits this recursive relationship and enforces satisfaction of kinematics constraints (2a) and (2b) through back substitutions, resulting in an efficient and linear ...
- **p. 5 / IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** We first present the final constrained IK algorithm in Algorithm 1, where the equality-constrained QP IK sub-problem is solved on line 5 using the proposed ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** For one, solving a differential IK quadratic program is still a resource-constrained operation, with computation times on the same scale of order as the frequency ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** embracing, techniques, spirit, rigid-body, dynamics, algorithms, Featherstone, introduce, solves, equality-constrained, differential, problems, lineartime, complexity, First, introduced, ADMM, tailored, convex, constrained.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | Each benchmark scenario then consists of three tasks: • position p∗ com(t) for the upper-body target where the robot should place its ... | p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| Balance-aware whole-body execution | Comparison to QP-based inverse kinematics With the parameters we have described, the benchmark produces 92,000 IK problems. | p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| Recovery / adaptation | Supporting closed-loops is a relevant future research direction since several recent robots include them to improve some mechanical properties. | p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |

## Failure and Ablation Link

- **p. 8 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** A tasks consists of two components: a target, as detailed in the latter two sections for the scenarios in this benchmark, and dynamics.
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 9: Additional solver information from LOIK for the 67-DOF Romeo humanoid scenario. Top: number of active inequality constraints at termination for each time step. ...
- **p. 9 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** LOIK scales essentially like the "QP lower bound" of frame Jacobian computations (another linear-time algorithm), with 3This means in particular that, for "OSQP (Drake)", (1) ...
- **p. 10 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** First, LOIK does not support robot topologies with internal closed loops, as its recursive derivation relies on a tree topology.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Abstract), p. 2 (II. BACKGROUND), p. 2 (II. BACKGROUND), p. 6 (IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 3 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 5 (IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE), objective p. 3 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 2 (II. BACKGROUND), p. 7 (B. Feasibility Detection), p. 7 (B. Feasibility Detection), p. 6 (IV. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), temporal p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The proposed algorithm exploits this recursive relationship and enforces satisfaction of kinematics constraints (2a) and (2b) through back substitutions, resulting in an efficient and linear complexity algorithm. (p. 3, III. LOW-COMPLEXITY DIFFERENTIAL INVERSE).
- **Objective/update evidence:** Embracing optimization further enabled the integration of configuration and joint-velocity limits as inequality constraints. (p. 1, I. INTRODUCTION).
- **Temporal/runtime evidence:** We place robotic arms at the origin of the initial frame for the scaling factor to make sense. (p. 8, V. EXPERIMENTAL VALIDATION AND BENCHMARKS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
