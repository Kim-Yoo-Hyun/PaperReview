# Method - Momentum Control with Hierarchical Inverse Dynamics on a Torque-Controlled Humanoid

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1410.7284; PDF retrieval source: https://arxiv.org/pdf/1410.7284. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 17 (6.2 Relation to other balancing approaches), p. 17 (6.2 Relation to other balancing approaches), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 4 (2.1 Modelling Assumptions and Problem Formulation), p. 4 (2.1 Modelling Assumptions and Problem Formulation)): However, with the optimization problem being complicated, they actually solve a simpler problem where the contact forces are first determined and then desired accelerations and torques are computed through a ...

## Method Body Digest

- **p. 17 / 6.2 Relation to other balancing approaches - extractive PDF cue:** However, with the optimization problem being complicated, they actually solve a simpler problem where the contact forces are first determined and then desired accelerations and ...
- **p. 17 / 6.2 Relation to other balancing approaches - extractive PDF cue:** In [36], the authors write the whole optimization procedure using Equation (1) with constraints similar to the ones we use.
- **p. 3 / 2.1 Modelling Assumptions and Problem Formulation - extractive PDF cue:** This can be expressed as a linear inequality by expressing the ground reaction force at the zero moment point.
- **p. 3 / 2.1 Modelling Assumptions and Problem Formulation - extractive PDF cue:** In our case, we approximate the cones by pyramids to have linear inequality constraints in the contact forces.
- **p. 4 / 2.1 Modelling Assumptions and Problem Formulation - extractive PDF cue:** Desired contact forces can be directly expressed as equalities on the generalized forces λ.
- **p. 4 / 2.1 Modelling Assumptions and Problem Formulation - extractive PDF cue:** The goal of the controller is to find ¨q, λ and τ (and therefore a control command) that satisfies these objectives as well as possible.
- **p. 6 / 3.1 Linear and angular momentum models - extractive PDF cue:** [x]×λ = x × λ and xi is the position of the ith contact point.
- **p. 4 / 2.1 Modelling Assumptions and Problem Formulation - extractive PDF cue:** At every control cycle, the equations of motion (Equation (1)), the constraints for physical consistency (torque saturation, CoP constraints, etc.) and our control objectives are ...

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** This leads us to the main contribution of this paper, where we show experiments with extensive quantitative analysis for various tasks (Sections 4 and 5).
- **p. 1 / 1 Introduction - extractive PDF cue:** Recent contributions have also demonstrated the relevance of torque control approaches for humanoid robots [13,28,36].
- **p. 2 / 1 Introduction - extractive PDF cue:** It has been shown in several contributions [39,21] that the regulation of momentum could be very powerful for control on humanoids.

## Source Evidence Cues

- **p. 17 / 6.2 Relation to other balancing approaches - extractive PDF cue:** However, with the optimization problem being complicated, they actually solve a simpler problem where the contact forces are first determined and then desired accelerations and ...
- **p. 17 / 6.2 Relation to other balancing approaches - extractive PDF cue:** In [36], the authors write the whole optimization procedure using Equation (1) with constraints similar to the ones we use.
- **p. 3 / 2.1 Modelling Assumptions and Problem Formulation - extractive PDF cue:** This can be expressed as a linear inequality by expressing the ground reaction force at the zero moment point.
- **p. 3 / 2.1 Modelling Assumptions and Problem Formulation - extractive PDF cue:** In our case, we approximate the cones by pyramids to have linear inequality constraints in the contact forces.
- **p. 4 / 2.1 Modelling Assumptions and Problem Formulation - extractive PDF cue:** Desired contact forces can be directly expressed as equalities on the generalized forces λ.
- **p. 4 / 2.1 Modelling Assumptions and Problem Formulation - extractive PDF cue:** The goal of the controller is to find ¨q, λ and τ (and therefore a control command) that satisfies these objectives as well as possible.
- **p. 6 / 3.1 Linear and angular momentum models - extractive PDF cue:** [x]×λ = x × λ and xi is the position of the ith contact point.
- **Detected method headings:** 2.1 Modelling Assumptions and Problem Formulation (p. 3); 3.1 Linear and angular momentum models (p. 6); 4.4 Dynamic model (p. 8); 5.2.2 Comparison of momentum controllers (p. 11); 6.2 Relation to other balancing approaches (p. 17)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | However, with the optimization problem being complicated, they actually solve a simpler problem where the contact forces are first determined and then ... | p. 17 (6.2 Relation to other balancing approaches), p. 17 (6.2 Relation to other balancing approaches) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | In [36], the authors write the whole optimization procedure using Equation (1) with constraints similar to the ones we use. | p. 17 (6.2 Relation to other balancing approaches), p. 3 (2.1 Modelling Assumptions and Problem Formulation) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | This can be expressed as a linear inequality by expressing the ground reaction force at the zero moment point. | p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 3 (2.1 Modelling Assumptions and Problem Formulation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 2.1 Modelling Assumptions and Problem Formulation - extractive PDF cue:** At every control cycle, the equations of motion (Equation (1)), the constraints for physical consistency (torque saturation, CoP constraints, etc.) and our control objectives are ...
- **p. 17 / 6.2 Relation to other balancing approaches - extractive PDF cue:** In [36], the authors write the whole optimization procedure using Equation (1) with constraints similar to the ones we use.
- **p. 4 / 2.1 Modelling Assumptions and Problem Formulation - extractive PDF cue:** In general, we assume that each control objective can be expressed as a linear combination of ¨q, λ and τ, which are the optimization variables ...
- **p. 17 / 6.2 Relation to other balancing approaches - extractive PDF cue:** Our formulation has the great advantage of solving a single optimization problem instead of several ones and can therefore guarantee that the control law will ...
- **p. 3 / 2.1 Modelling Assumptions and Problem Formulation - extractive PDF cue:** We get the following equality constraint Jc¨q + ˙Jc ˙q = 0.
- **p. 3 / 2.1 Modelling Assumptions and Problem Formulation - extractive PDF cue:** Contact constraints End effectors are constrained to remain stationary.
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 4 (2.1 Modelling Assumptions and Problem Formulation), p. 17 (6.2 Relation to other balancing approaches), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 4 (2.1 Modelling Assumptions and Problem Formulation), p. 6 (3.1 Linear and angular momentum models).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Therefore, possible, directly, control, interaction, forces, during, multi-contact, tasks, close, feedback, loop, around, interests | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | Therefore, possible, directly, control, interaction, forces, during, multi-contact, tasks, close | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | leads, main, contribution, where, experiments, extensive, quantitative, analysis, various, tasks | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | every, control, cycle, equations, motion, Equation, constraints, physical, consistency, torque | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive PDF cue:** Therefore it is not possible to directly control interaction forces during multi-contact tasks or to close a feedback loop directly around the tasks of interests, ...
- **p. 3 / 2.1 Modelling Assumptions and Problem Formulation - extractive PDF cue:** This can be expressed as a linear inequality by expressing the ground reaction force at the zero moment point.
- **p. 3 / 2.1 Modelling Assumptions and Problem Formulation - extractive PDF cue:** Friction cone For the feet not to slip we constraint the ground reaction forces (GRFs) to stay inside the friction cones.
- **p. 2 / 1 Introduction - extractive PDF cue:** But to the best of our knowledge, these controllers have never been used as feedback-controllers on real torque-controlled humanoids.
- **p. 6 / 3.1 Linear and angular momentum models - extractive PDF cue:** In addition, in Equation (21) external forces can be interpreted as the control inputs of the system, which is a useful interpretation for control design, ...
- **p. 4 / 2.1 Modelling Assumptions and Problem Formulation - extractive PDF cue:** The goal of the controller is to find ¨q, λ and τ (and therefore a control command) that satisfies these objectives as well as possible.
- **p. 17 / 6.2 Relation to other balancing approaches - extractive PDF cue:** However, with the optimization problem being complicated, they actually solve a simpler problem where the contact forces are first determined and then desired accelerations and ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | It would also be straightforward to linearize the dynamics at every control sequence and use a receding horizon controller with time-varying gains ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | We used a computer running a linux kernel patched with Xenomai 2.6.3 for real-time capabilities. | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not recovered | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | 2.1 3 3 eq PD control on CoG (2 -c) × 6 PD control on swing foot 4 25 + 6 eq ... | hardware, batch and throughput |

## Training vs Inference

- **p. 17 / 6.2 Relation to other balancing approaches - extractive PDF cue:** In [36], the authors write the whole optimization procedure using Equation (1) with constraints similar to the ones we use.
- **p. 3 / 2.1 Modelling Assumptions and Problem Formulation - extractive PDF cue:** In our case, we approximate the cones by pyramids to have linear inequality constraints in the contact forces.
- **p. 15 / 5.4 Single Support Experiments - extractive PDF cue:** Concerning computation time, the controller computes a solution in average well below 1ms but a maximum at 1.05ms is reached a few times during the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** However, optimization, problem, being, complicated, they, actually, solve, simpler, where, contact, forces, first, determined, then, desired, accelerations, torques, computed, through.
- **Relevant PDF headings:** 2.1 Modelling Assumptions and Problem Formulation (p. 3); 3.1 Linear and angular momentum models (p. 6); 4.4 Dynamic model (p. 8); 5.2.2 Comparison of momentum controllers (p. 11); 6.2 Relation to other balancing approaches (p. 17).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | In the following, however, we construct a more complex stepping task in simulation for the full 25 DoF robot. | p. 9 (5.1 Processing Time), p. 15 (5.4 Single Support Experiments) |
| Balance-aware whole-body execution | It is worth mentioning again that the foot size of the robot is rather small compared to other humanoids. | p. 16 (5.4 Single Support Experiments), p. 8 (4.4 Dynamic model) |
| Recovery / adaptation | This controller design allowed us to achieve good torque tracking performance. | p. 8 (4.2 Low-level torque control), p. 8 (4.2 Low-level torque control) |

## Failure and Ablation Link

- **p. 8 / 4.4 Dynamic model - extractive PDF cue:** We expect to have even better performance once we perform a good identification of the dynamics [1,24] but it is interesting to note that good ...
- **p. 9 / 5.1 Processing Time - extractive PDF cue:** It would not have been possible by using this algorithm without the simplification.
- **p. 9 / 5.1 Processing Time - extractive PDF cue:** The proposed decomposition removed 25 equality constraints and 25 optimization variables.
- **p. 10 / 5.2 Balance Control Experiments - extractive PDF cue:** 5 Processing time of a stepping task (see Table 1) using the decomposition proposed in Section 2.3 (red) and the same task performed without the ...
- **p. 11 / 5.2.2 Comparison of momentum controllers - extractive PDF cue:** For both momentum control tasks, the robot was able to withstand impacts with high peak forces and strong impulses without falling.
- **p. 15 / 5.4 Single Support Experiments - extractive PDF cue:** Then an unloading phase occurs during which the contact force regularization enforces a zero contact force to guarantee a continuous transition when the double support ...
- **p. 17 / 6.2 Relation to other balancing approaches - extractive PDF cue:** Also, separating the EoM from kinematic contact constraints allows to keep solutions consistent with the dynamics even in postures where the feet cannot be kept ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 17 (6.2 Relation to other balancing approaches), p. 17 (6.2 Relation to other balancing approaches), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 4 (2.1 Modelling Assumptions and Problem Formulation), p. 4 (2.1 Modelling Assumptions and Problem Formulation), objective p. 4 (2.1 Modelling Assumptions and Problem Formulation), p. 17 (6.2 Relation to other balancing approaches), p. 4 (2.1 Modelling Assumptions and Problem Formulation), p. 17 (6.2 Relation to other balancing approaches), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 3 (2.1 Modelling Assumptions and Problem Formulation), temporal p. 7 (3.2 LQR design for momentum control), p. 7 (4.1 Sarcos Humanoid Robot), p. 8 (4.5 Experimental tools), p. 9 (5.1 Processing Time), p. 9 (5.1 Processing Time), p. 10 (5.1 Processing Time).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
