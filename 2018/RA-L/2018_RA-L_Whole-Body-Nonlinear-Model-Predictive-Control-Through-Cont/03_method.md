# Method - Whole-Body Nonlinear Model Predictive Control Through Contacts for Quadrupeds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1712.02889; PDF retrieval source: https://arxiv.org/pdf/1712.02889. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (III. NMPC APPROACH), p. 3 (III. NMPC APPROACH), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 4 (IV. SOFTWARE IMPLEMENTATION)): In contrast, the GNMS-NMPC algorithm, which is summarized in Algorithm 2, designs a state reference trajectory simultaneously with the new control policy.

## Method Body Digest

- **p. 3 / III. NMPC APPROACH - extractive body cue:** In contrast, the GNMS-NMPC algorithm, which is summarized in Algorithm 2, designs a state reference trajectory simultaneously with the new control policy.
- **p. 3 / III. NMPC APPROACH - extractive body cue:** It designs time-varying state-feedback controllers of the form un(x) = uff n + Kn(xn -xref n ) (8) where uff n is the feedforward control ...
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Integration and Sensitivity Computation Our system dynamics include a contact model that needs to be chosen stiff enough to approximate the real physics of contact ...
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Our LQOC solver requires us to compute sensitivities along the trajectory, i.e. partial derivatives of the integrated state with respect to the start state and ...
- **p. 3 / III. NMPC APPROACH - extractive body cue:** AN-1, B1, . . . , BN-1. - quadratize cost function (1) around X, U for multiple-shooting intervals 1 to N. policy update.
- **p. 3 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Also, many computational routines such as integrating a differential equation over time, are naturally sequential operations that cannot be parallelized easily.
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** The cost and sensitivity computation, which can be distributed among all available cores, is parallelizable for all our algorithm variants.
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** The optimized control input obtained from the NMPC solver is then augmented with the output of two tracking controllers. instructions.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present a whole-body Nonlinear Model Predictive Control (NMPC) approach for Rigid Body Dynamics (RBD) systems subject to contacts.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Contributions In this work, we demonstrate whole-body, contact invariant nonlinear MPC for highly dynamic motions that require explicit reasoning about the full dynamics of the ...
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Since our code mostly consists of matrix and vector manipulations and register sizes of AVX are doubled over SSE, we obtained an additional speedup of ...

## Source Evidence Cues

- **p. 3 / III. NMPC APPROACH - extractive body cue:** In contrast, the GNMS-NMPC algorithm, which is summarized in Algorithm 2, designs a state reference trajectory simultaneously with the new control policy.
- **p. 3 / III. NMPC APPROACH - extractive body cue:** It designs time-varying state-feedback controllers of the form un(x) = uff n + Kn(xn -xref n ) (8) where uff n is the feedforward control ...
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Integration and Sensitivity Computation Our system dynamics include a contact model that needs to be chosen stiff enough to approximate the real physics of contact ...
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Our LQOC solver requires us to compute sensitivities along the trajectory, i.e. partial derivatives of the integrated state with respect to the start state and ...
- **Detected method headings:** III. NMPC APPROACH (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | In contrast, the GNMS-NMPC algorithm, which is summarized in Algorithm 2, designs a state reference trajectory simultaneously with the new control policy. | p. 3 (III. NMPC APPROACH), p. 3 (III. NMPC APPROACH) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | It designs time-varying state-feedback controllers of the form un(x) = uff n + Kn(xn -xref n ) (8) where uff n is ... | p. 3 (III. NMPC APPROACH), p. 4 (IV. SOFTWARE IMPLEMENTATION) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | Integration and Sensitivity Computation Our system dynamics include a contact model that needs to be chosen stiff enough to approximate the real ... | p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 4 (IV. SOFTWARE IMPLEMENTATION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. NMPC APPROACH - extractive body cue:** AN-1, B1, . . . , BN-1. - quadratize cost function (1) around X, U for multiple-shooting intervals 1 to N. policy update.
- **p. 3 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Also, many computational routines such as integrating a differential equation over time, are naturally sequential operations that cannot be parallelized easily.
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** The cost and sensitivity computation, which can be distributed among all available cores, is parallelizable for all our algorithm variants.
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** The optimized control input obtained from the NMPC solver is then augmented with the output of two tracking controllers. instructions.
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 3 (IV. SOFTWARE IMPLEMENTATION), p. 3 (III. NMPC APPROACH), p. 4 (IV. SOFTWARE IMPLEMENTATION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | designs, time-varying, state-feedback, controllers, form, xref, where, feedforward, control, action, linear, feedback, controller, regulating | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | designs, time-varying, state-feedback, controllers, form, xref, where, feedforward, control, action | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | present, whole-body, Nonlinear, Model, Predictive, Control, NMPC, Rigid, Body, Dynamics | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | AN-1, BN-1, quadratize, cost, function, around, multiple-shooting, intervals, policy, update | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. NMPC APPROACH - extractive body cue:** It designs time-varying state-feedback controllers of the form un(x) = uff n + Kn(xn -xref n ) (8) where uff n is the feedforward control ...
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** The optimized control input obtained from the NMPC solver is then augmented with the output of two tracking controllers. instructions.
- **p. 3 / III. NMPC APPROACH - extractive body cue:** In contrast, the GNMS-NMPC algorithm, which is summarized in Algorithm 2, designs a state reference trajectory simultaneously with the new control policy.
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Our LQOC solver requires us to compute sensitivities along the trajectory, i.e. partial derivatives of the integrated state with respect to the start state and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** While whole-body, contact invariant NMPC has been demonstrated on hardware before [15], the presented motions were rather slow or even quasi static, underlined by the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** We summarize our solver framework, which uses Auto-Differentiation and code generation to achieve high computational performance exceeding the current state of the art in robotics ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we demonstrate that an NMPC approach which continuously re-optimizes the state and control trajectories at high frequency, results in robust performance and ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | Yet, thorough numerical and software engineering allows for running the nonlinear Optimal Control solver at rates up to 190 Hz on a ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | While these approaches are very complete, their runtimes are still a few orders of magnitudes away from running in receding horizon or ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | Yet, thorough numerical and software engineering allows for running the nonlinear Optimal Control solver at rates up to 190 Hz on a ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** contrast, GNMS-NMPC, algorithm, summarized, designs, state, reference, trajectory, simultaneously, control, policy, time-varying, state-feedback, controllers, form, xref, where, feedforward, action, linear.
- **Relevant PDF headings:** III. NMPC APPROACH (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | While the robot does not always land perfectly, the MPC controller optimizes a trajectory from the current state and tries to get ... | p. 6 (VI. RESULTS), p. 4 (IV. SOFTWARE IMPLEMENTATION) |
| Balance-aware whole-body execution | Compared to ANYmal the magnitude of the deviations is slightly larger. | p. 6 (VI. RESULTS), p. 6 (VI. RESULTS) |
| Recovery / adaptation | Fig. 8. MPC update rate as recorded during two trotting experiments on ANYmal. While iLQR achieves update rates of around 80 Hz, ... | p. 7 (Figure/Table caption), p. 5 (VI. RESULTS) |

## Failure and Ablation Link

- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** The cost and sensitivity computation, which can be distributed among all available cores, is parallelizable for all our algorithm variants.
- **p. 4 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** Therefore, we compute them exactly by integrating a corresponding sensitivity ODE.
- **p. 5 / VI. RESULTS - extractive body cue:** HyQ can be perturbed significantly both on the base and the legs without reacting stiffly.
- **p. 5 / VI. RESULTS - extractive body cue:** In previous work [17], we have demonstrated that our approach can also discover a trotting gait without swing leg costs.
- **p. 6 / VI. RESULTS - extractive body cue:** The controller is able to return to a periodic motion after the disturbance is removed.
- **p. 6 / VI. RESULTS - extractive body cue:** On the torque level the robot stayed well below the admissible torque level of ANYmal (40 Nm) without imposing additional constraints.
- **p. 3 / IV. SOFTWARE IMPLEMENTATION - extractive body cue:** However, both parallel execution and vectorization cannot be leveraged automatically by standard compilers.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (III. NMPC APPROACH), p. 3 (III. NMPC APPROACH), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 4 (IV. SOFTWARE IMPLEMENTATION), objective p. 3 (III. NMPC APPROACH), p. 3 (IV. SOFTWARE IMPLEMENTATION), p. 4 (IV. SOFTWARE IMPLEMENTATION), p. 4 (IV. SOFTWARE IMPLEMENTATION), temporal p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 2 (II. NMPC FOR RIGID BODY SYSTEMS), p. 3 (IV. SOFTWARE IMPLEMENTATION), p. 3 (IV. SOFTWARE IMPLEMENTATION), p. 4 (IV. SOFTWARE IMPLEMENTATION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** It designs time-varying state-feedback controllers of the form un(x) = uff n + Kn(xn -xref n ) (8) where uff n is the feedforward control action and Kn a linear ... (p. 3, III. NMPC APPROACH).
- **Objective/update evidence:** AN-1, B1, . . . , BN-1. - quadratize cost function (1) around X, U for multiple-shooting intervals 1 to N. policy update. (p. 3, III. NMPC APPROACH).
- **Temporal/runtime evidence:** Modelling Framework Our NMPC controller relies heavily on evaluating Rigid Body Dynamics and Kinematics. (p. 3, IV. SOFTWARE IMPLEMENTATION).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
