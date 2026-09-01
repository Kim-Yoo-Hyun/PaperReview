# Method - Synthesis of Whole-Body Behaviors through Hierarchical Control of Behavioral Primitives

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ai.stanford.edu/~lsentis/files/publications.html; PDF retrieval source: https://ai.stanford.edu/manips/publications/pdfs/Sentis_2005_IJHR.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3. Integration of constraints), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3. Integration of constraints), p. 5 (3. Integration of constraints)): In this context, redundancy has received much attention, with most algorithms

## Method Body Digest

- **p. 4 / 3. Integration of constraints - extractive PDF cue:** In this context, redundancy has received much attention, with most algorithms
- **p. 1 / 1. Introduction - extractive PDF cue:** Emerging applications of humanoids demand higher and higher degrees of autonomy for efficient interactions in human-populated environments.
- **p. 2 / 1. Introduction - extractive PDF cue:** In this context, infeasible movements result from the presence of constraining objects or from inconsistent or conflicting control primitives.
- **p. 2 / 1. Introduction - extractive PDF cue:** Additionally, this formulation introduces null-space projections directly at the kinematic level, allowing us to implement operational space compliant controllers while complying with the constraints and ...
- **p. 5 / 3. Integration of constraints - extractive PDF cue:** (8) Here, J is the Jacobian of an operational task, x is a desired task-space trajectory, (I -J# J) is the kinematically-consistent null-space, and qnull ...
- **p. 5 / 3. Integration of constraints - extractive PDF cue:** Based on the operational space formulation for redundant robots, further represented by the torque decomposition Γ = J T F + N T Γnull, (9) ...
- **p. 6 / 3. Integration of constraints - extractive PDF cue:** In Figure 2 we depict a sequence where the robot's right hand is controlled to remain at a fixed location while an object is moved ...
- **p. 6 / 3. Integration of constraints - extractive PDF cue:** To accomplish the task and handle the constraint efficiently, we apply the control described in Equation (10).

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In contrast, our methodology integrates constraints in the control formulation as primary controls and projects the operational tasks and the posture primitives into the constraint ...
- **p. 2 / 1. Introduction - extractive PDF cue:** In Section 2 we describe previous related work, and also lay the mathematical foundations for this research based on our previous work.9 In Section 3 ...
- **p. 5 / 3. Integration of constraints - extractive PDF cue:** Based on the operational space formulation for redundant robots, further represented by the torque decomposition Γ = J T F + N T Γnull, (9) ...

## Source Evidence Cues

- **p. 4 / 3. Integration of constraints - extractive PDF cue:** In this context, redundancy has received much attention, with most algorithms
- **p. 1 / 1. Introduction - extractive PDF cue:** Emerging applications of humanoids demand higher and higher degrees of autonomy for efficient interactions in human-populated environments.
- **p. 2 / 1. Introduction - extractive PDF cue:** In this context, infeasible movements result from the presence of constraining objects or from inconsistent or conflicting control primitives.
- **p. 2 / 1. Introduction - extractive PDF cue:** Additionally, this formulation introduces null-space projections directly at the kinematic level, allowing us to implement operational space compliant controllers while complying with the constraints and ...
- **p. 5 / 3. Integration of constraints - extractive PDF cue:** (8) Here, J is the Jacobian of an operational task, x is a desired task-space trajectory, (I -J# J) is the kinematically-consistent null-space, and qnull ...
- **p. 5 / 3. Integration of constraints - extractive PDF cue:** Based on the operational space formulation for redundant robots, further represented by the torque decomposition Γ = J T F + N T Γnull, (9) ...
- **p. 6 / 3. Integration of constraints - extractive PDF cue:** In Figure 2 we depict a sequence where the robot's right hand is controlled to remain at a fixed location while an object is moved ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | In this context, redundancy has received much attention, with most algorithms | p. 4 (3. Integration of constraints), p. 1 (1. Introduction) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | Emerging applications of humanoids demand higher and higher degrees of autonomy for efficient interactions in human-populated environments. | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | In this context, infeasible movements result from the presence of constraining objects or from inconsistent or conflicting control primitives. | p. 2 (1. Introduction), p. 2 (1. Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3. Integration of constraints - extractive PDF cue:** To accomplish the task and handle the constraint efficiently, we apply the control described in Equation (10).
- **p. 7 / 4. Multi-level hierarchy - extractive PDF cue:** With this notation, Equation (12) becomes Γ = Γconstraints + Γ1/prec(1) + Γ2/prec(2) + · · · + ΓN/prec(N), (14) where Γk/prec(k) = N T ...
- **p. 7 / 4. Multi-level hierarchy - extractive PDF cue:** The following torque equation embodies a multi-level control hierarchy integrating both constraints and tasks into a single torque control reference: Γ =Γconstraints + N T ...
- **p. 6 / 4. Multi-level hierarchy - extractive PDF cue:** We create this hierarchy to integrate constraints and organize additional tasks according to desired priorities, while optimizing the execution of the global task.
- **p. 1 / 1. Introduction - extractive PDF cue:** To guarantee the safety of the robot and its environment we have designed a control hierarchy among primitives, where the control of the most critical ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Constraints, operational tasks, and postures are treated as independent control entities.
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 6 (3. Integration of constraints), p. 7 (4. Multi-level hierarchy), p. 7 (4. Multi-level hierarchy), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Emerging, applications, humanoids, demand, higher, degrees, autonomy, efficient, interactions, human-populated, environments, December, WSPC/INSTRUCTION, FILE | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | Emerging, applications, humanoids, demand, higher, degrees, autonomy, efficient, interactions, human-populated | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | contrast, methodology, integrates, constraints, control, formulation, primary, controls, projects, operational | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | accomplish, task, handle, constraint, efficiently, apply, control, described, Equation, notation | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive PDF cue:** Emerging applications of humanoids demand higher and higher degrees of autonomy for efficient interactions in human-populated environments.
- **p. 2 / 1. Introduction - extractive PDF cue:** December 19, 2005 17:13 WSPC/INSTRUCTION FILE ijhr-II-v4 2 guaranteed while non-safety related primitives (i.e. operational tasks and postures) are controlled without violating higher priority controls.
- **p. 5 / 3. Integration of constraints - extractive PDF cue:** December 19, 2005 17:13 WSPC/INSTRUCTION FILE ijhr-II-v4 5 being based on instantaneous kinematic solutions with constraint-handling criteria projected into the task null-space, i.e. dq = ...
- **p. 8 / 4.3. Movement feasibility - extractive PDF cue:** However, by choosing the control input Fk/prec(k) = ³ Ur(k)Σ-1 r(k)U T r(k) ´ ¨xk(ref) + µk/prec(k) + pk/prec(k), (23) we accomplish dynamic decoupling in ...
- **p. 8 / 4.1. Recursive null-spaces - extractive PDF cue:** December 19, 2005 17:13 WSPC/INSTRUCTION FILE ijhr-II-v4 8 This mathematical constraint leads to the following unique solution Nprec(k) = I - k-1 X i=1 Ji/prec(i)Ji/prec(i), ...
- **p. 5 / 3. Integration of constraints - extractive PDF cue:** Based on the operational space formulation for redundant robots, further represented by the torque decomposition Γ = J T F + N T Γnull, (9) ...
- **p. 2 / 1. Introduction - extractive PDF cue:** The hierarchies imposed among these categories allows us to study movement feasibility in realtime and stop or change the global behavior if needed.
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | Section 4 presents a multi-level prioritized framework that allows us to establish multiple priority levels among categories. | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | We briefly explore the experimental setup in Section 5 and demonstrate the framework's capability by evaluating an example scenario. | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not recovered | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1. Introduction - extractive PDF cue:** In this context, infeasible movements result from the presence of constraining objects or from inconsistent or conflicting control primitives.
- **p. 2 / 1. Introduction - extractive PDF cue:** Additionally, this formulation introduces null-space projections directly at the kinematic level, allowing us to implement operational space compliant controllers while complying with the constraints and ...
- **p. 5 / 3. Integration of constraints - extractive PDF cue:** (8) Here, J is the Jacobian of an operational task, x is a desired task-space trajectory, (I -J# J) is the kinematically-consistent null-space, and qnull ...
- **p. 5 / 3. Integration of constraints - extractive PDF cue:** Based on the operational space formulation for redundant robots, further represented by the torque decomposition Γ = J T F + N T Γnull, (9) ...
- **p. 6 / 3. Integration of constraints - extractive PDF cue:** In Figure 2 we depict a sequence where the robot's right hand is controlled to remain at a fixed location while an object is moved ...
- **p. 13 / 6. Summary and discussion - extractive PDF cue:** While today the interactive control of humanoids is limited to the online selection of a few preplanned motions, with this new controller, we construct complex ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** context, redundancy, received, much, attention, most, algorithms, Emerging, applications, humanoids, demand, higher, degrees, autonomy, efficient, interactions, human-populated, environments, infeasible, movements.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | Collision avoidance and control of multiple task primitives: This sequence depicts a robot avoiding an obstacle that is moved interactively towards several ... | p. 5 (3. Integration of constraints), p. 5 (3. Integration of constraints) |
| Balance-aware whole-body execution | We can then modify the task trajectory or remove its control while the control of other higher priority tasks such as balancing ... | p. 9 (4.3. Movement feasibility), p. 5 (3. Integration of constraints) |
| Recovery / adaptation | But first, to evaluate the performance and determine the optimal ordering we examine a scenario where the center of gravity control shares ... | p. 10 (4.3. Movement feasibility), p. 12 (X Direction) |

## Failure and Ablation Link

- **p. 9 / 4.3. Movement feasibility - extractive PDF cue:** We can then modify the task trajectory or remove its control while the control of other higher priority tasks such as balancing or control of ...
- **p. 5 / 3. Integration of constraints - extractive PDF cue:** Based on the operational space formulation for redundant robots, further represented by the torque decomposition Γ = J T F + N T Γnull, (9) ...
- **p. 6 / 3. Integration of constraints - extractive PDF cue:** This projection ensures that the operational task does not introduce acceleration components into the constrained directions.
- **p. 13 / 6. Summary and discussion - extractive PDF cue:** Our research has addressed a wide set of constraints, such as joint-limits, collision avoidance, and self-collision avoidance, based on reactive techniques at the whole-body level.
- **p. 5 / 3. Integration of constraints - extractive PDF cue:** Collision avoidance and control of multiple task primitives: This sequence depicts a robot avoiding an obstacle that is moved interactively towards several points near the ...
- **p. 11 / X Direction - extractive PDF cue:** However, the center of gravity horizontal position cannot be maintained (a), because its control is directly affected by the hand control. i.e. Γ = ΓJLC ...
- **p. 12 / X Direction - extractive PDF cue:** Because the hierarchy assigns higher priority to the center of gravity task, it maintains its desired goal position (above the robot's feet) at all times, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3. Integration of constraints), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3. Integration of constraints), p. 5 (3. Integration of constraints), objective p. 6 (3. Integration of constraints), p. 7 (4. Multi-level hierarchy), p. 7 (4. Multi-level hierarchy), p. 6 (4. Multi-level hierarchy), p. 1 (1. Introduction), p. 2 (1. Introduction), temporal p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Related work), p. 4 (2. Related work), p. 5 (3. Integration of constraints), p. 6 (4. Multi-level hierarchy).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
