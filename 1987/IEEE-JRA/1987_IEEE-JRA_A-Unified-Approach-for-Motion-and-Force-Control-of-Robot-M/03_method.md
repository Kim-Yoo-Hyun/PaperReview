# Method - A Unified Approach for Motion and Force Control of Robot Manipulators: The Operational Space Formulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://cs.stanford.edu/group/manips/publications.html; PDF retrieval source: https://cs.stanford.edu/group/manips/publications/pdfs/Khatib_1987_RA.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (IV. Exp-Errecror Morton Controt), p. 1 (I. Inrropucrion), p. 1 (I. Inrropucrion), p. 3 (I. Inrropucrion), p. 6 (V. Constnainep Motion Operarions), p. 2 (I. Inrropucrion)): The real-time computation of these coefficients can then be paced by the rate of configuration changes, which is much lower than that of the mechanism dynamics, This leads to the ...

## Method Body Digest

- **p. 6 / IV. Exp-Errecror Morton Controt - extractive body cue:** The real-time computation of these coefficients can then be paced by the rate of configuration changes, which is much lower than that of the mechanism ...
- **p. 1 / I. Inrropucrion - extractive body cue:** However, task specification for motion and contact forces, dynamics, and force sensing feedback are closely linked to the end-effector.
- **p. 1 / I. Inrropucrion - extractive body cue:** ‘The issue of end-effector dynamic modeling and control is yet more acute for tasks that involve combined motion and ‘contact forces of the end-effector.
- **p. 3 / I. Inrropucrion - extractive body cue:** However, the control of end-effector motion and contact forces, or the analysis and characterization of endeffector dynamic performance requires the construction of the model describing ...
- **p. 6 / V. Constnainep Motion Operarions - extractive body cue:** ‘The Jacobian matrix J(q) associated with a given representation of the end-effector orientation x, can then be expressed in the form [13]
- **p. 2 / I. Inrropucrion - extractive body cue:** ‘The end-effector motion and contact forces are among the ‘most important components in the planning, description, and control of assembly operations of robot manipulators. ‘The ...
- **p. 3 / I. Inrropucrion - extractive body cue:** associated with specifications of motion and contact forces, respectively.
- **p. 2 / I. Inrropucrion - extractive body cue:** The number of degrees of freedom of the constrained end-effector is given by the difference between mo and the number of independent ‘equations specifying the ...

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** These results are used in the development ofa new and approach for dealing with the problems arising at kinematic sn
- **p. 1 / Abstract - extractive body cue:** A framework for the analysis and control of manipulator systems with respect to the dynamic behavior of their end-effectors is developed.
- **p. 3 / I. Inrropucrion - extractive body cue:** This allows a more efficient implementation of the control system for real-time operations.

## Source Evidence Cues

- **p. 6 / IV. Exp-Errecror Morton Controt - extractive body cue:** The real-time computation of these coefficients can then be paced by the rate of configuration changes, which is much lower than that of the mechanism ...
- **p. 1 / I. Inrropucrion - extractive body cue:** However, task specification for motion and contact forces, dynamics, and force sensing feedback are closely linked to the end-effector.
- **p. 1 / I. Inrropucrion - extractive body cue:** ‘The issue of end-effector dynamic modeling and control is yet more acute for tasks that involve combined motion and ‘contact forces of the end-effector.
- **p. 3 / I. Inrropucrion - extractive body cue:** However, the control of end-effector motion and contact forces, or the analysis and characterization of endeffector dynamic performance requires the construction of the model describing ...
- **p. 6 / V. Constnainep Motion Operarions - extractive body cue:** ‘The Jacobian matrix J(q) associated with a given representation of the end-effector orientation x, can then be expressed in the form [13]
- **p. 2 / I. Inrropucrion - extractive body cue:** ‘The end-effector motion and contact forces are among the ‘most important components in the planning, description, and control of assembly operations of robot manipulators. ‘The ...
- **p. 3 / I. Inrropucrion - extractive body cue:** associated with specifications of motion and contact forces, respectively.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / error representation | motion·force 목표를 제어 error로 바꾼다 | joint/task state, reference, wrench | task frame, Jacobian, impedance, selection 또는 error coordinates를 구성 | desired task command | The real-time computation of these coefficients can then be paced by the rate of configuration changes, which is much lower than that ... | p. 6 (IV. Exp-Errecror Morton Controt), p. 1 (I. Inrropucrion) |
| Dynamics / constraint solve | 목표를 feasible actuator command로 바꾼다 | error, model, constraints | inverse dynamics, QP, MPC, operational mapping 또는 feedback law를 계산 | torque, force, velocity 또는 position command | However, task specification for motion and contact forces, dynamics, and force sensing feedback are closely linked to the end-effector. | p. 1 (I. Inrropucrion), p. 1 (I. Inrropucrion) |
| Feedback / actuation | 실제 state와 disturbance에 따라 command를 닫힌 loop로 보정한다 | sensor feedback과 nominal command | tracking correction, saturation, null-space, fallback 또는 replan을 수행 | next actuation과 response | ‘The issue of end-effector dynamic modeling and control is yet more acute for tasks that involve combined motion and ‘contact forces of ... | p. 1 (I. Inrropucrion), p. 3 (I. Inrropucrion) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / I. Inrropucrion - extractive body cue:** The number of degrees of freedom of the constrained end-effector is given by the difference between mo and the number of independent ‘equations specifying the ...
- **p. 1 / I. Inrropucrion - extractive body cue:** focused on developing the equations of joint motions, ‘These joint space dynamic models have been the basis for various approaches to dynamic control of manipulators.
- **p. 1 / Abstract - extractive body cue:** The extension of this formulation to redundant manipulator systems is also presented, constructing the end-effector equations of ‘motion and describing their behavior with respect to ...
- **p. 2 / I. Inrropucrion - extractive body cue:** These constraints restrict the freedom of motion displacements and rotations) of the end-effector.
- **p. 3 / X 1 column matrix x of independent configuration parame - extractive body cue:** In the reference frame (o, the system of my equations expressing the components of x as functions of joint coordinates, i.e., the geometric model, is ...
- **p. 3 / I. Inrropucrion - extractive body cue:** Control systems using specifications based only on the matrices 3, and 5, will require costly geometric, kinematic, and dynamic transformations between the reference frame and ...
- **Formal bridge:** q, q̇, x, wrench -> u/τ subject to dynamics and actuator/contact constraints -> tracking or interaction error -> stability, tracking and constraint satisfaction.
- **Equation/algorithm anchors:** p. 2 (I. Inrropucrion), p. 1 (I. Inrropucrion), p. 1 (Abstract), p. 2 (I. Inrropucrion), p. 3 (X 1 column matrix x of independent configuration parame), p. 3 (I. Inrropucrion).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | However, task, specification, motion, contact, forces, dynamics, force, sensing, feedback, closely, linked, end-effector, description | joint/task state, reference와 sensor feedback | body cue; exact tensor/frame verify |
| State/latent | However, task, specification, motion, contact, forces, dynamics, force, sensing, feedback | state estimate, task-space error와 control decision | body cue; notation verify |
| Action/output | development, dealing, problems, arising, kinematic, framework, analysis, control, manipulator, systems | torque, force, velocity 또는 position command | body cue; unit/decoder verify |
| Objective/constraint | number, degrees, freedom, constrained, end-effector, given, difference, between, independent, equations | tracking or interaction error | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. Inrropucrion - extractive body cue:** However, task specification for motion and contact forces, dynamics, and force sensing feedback are closely linked to the end-effector.
- **p. 1 / I. Inrropucrion - extractive body cue:** The description of the dynamic interaction between end-effector motions and the effects of these motions on the end-effector's behavior in the direction of force control ...
- **p. 2 / I. Inrropucrion - extractive body cue:** These are the vectors of total force and moment that are to be applied to maintain the imposed constraints, and the specification of the end-effector ...
- **p. 5 / IV. Exp-Errecror Morton Controt - extractive body cue:** The velocity vector 2 is in fact controlled to be pointed toward the goal position while its magnitude is limited to Vous.
- **p. 5 / IV. Exp-Errecror Morton Controt - extractive body cue:** The control of a manipulator in operational space is based ‘on the selection of the generalized operational forces F as a ‘command vector.
- **p. 6 / V. Constnainep Motion Operarions - extractive body cue:** The unified operational command vector for end-effector dynamic decoupling, motion, and active force control can be
- **p. 2 / I. Inrropucrion - extractive body cue:** The directions of force control are described by the force specification matrix 3, associated with 3 and defined by
- **Normalized interface:** observation=joint/task state, reference와 sensor feedback; state=state estimate, task-space error와 control decision; output/action=torque, force, velocity 또는 position command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instantaneous or receding-horizon reference tracking; exact prediction horizon은 exact value not recovered from the selected body cues. | Within this framework of control and at the level ‘f the uncoupled system linear, nonlinear, robust [32], and adaptive [3] control structures ... | episode/sequence/action-chunk boundary |
| Rate / latency | sensor/actuator control tick마다 feedback solve; numeric rate는 paper-specific. | Kinematic singularities is another area that has been ‘considered within the framework of joint space control and | Hz/fps, inference time and control rate |
| Memory | 현재 joint/task state, reference, contact/wrench feedback; long history 여부 확인 필요. | not recovered | window and reset |
| Compute | dynamics/Jacobian evaluation, QP/MPC/inverse-dynamics solve와 actuator latency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** real-time, computation, coefficients, then, paced, rate, configuration, changes, much, lower, mechanism, dynamics, leads, following, architecture, control, system, However, task, specification.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / error representation | 46 IEEE JOURNAL OF ROBOTICS AND AUTOMATION, VOL. | p. 4 (X 1 column matrix x of independent configuration parame), p. 5 (X 1 column matrix x of independent configuration parame) |
| Dynamics / constraint solve | These forces can be selected to actin the null space of the Jacobian matrix [16] This precludes any effect of the additional ... | p. 8 (VII. Contnot. oF REDUNDANT MANIPULATORS), p. 5 (X 1 column matrix x of independent configuration parame) |
| Feedback / actuation | The construction of the end-effector dynamic model is achieved by expressing the relationships between its ‘operational positions, velocities, accelerations, and the virtual ... | p. 3 (I. Inrropucrion), p. 6 (IV. Exp-Errecror Morton Controt) |

## Failure and Ablation Link

- **p. 8 / VII. Contnot. oF REDUNDANT MANIPULATORS - extractive body cue:** These forces can be selected to actin the null space of the Jacobian matrix [16] This precludes any effect of the additional forces on the ...
- **p. 5 / X 1 column matrix x of independent configuration parame - extractive body cue:** In the foregoing relations, the components involved in the endeffector equations of motion (14), i.e., A, 4, p, are expressed in terms of joint coordinates.
- **p. 3 / X 1 column matrix x of independent configuration parame - extractive body cue:** In the reference frame (o, the system of my equations expressing the components of x as functions of joint coordinates, i.e., the geometric model, is ...
- **p. 4 / X 1 column matrix x of independent configuration parame - extractive body cue:** Using the expression of A(x) in (18), the components of u(x, 48) in (19) can be written as,
- **p. 4 / X 1 column matrix x of independent configuration parame - extractive body cue:** ‘The components of the my X Mig matrices T(r) are the Christoffel symbols x, given as a function of the partial derivatives of A(x) with ...
- **p. 6 / V. Constnainep Motion Operarions - extractive body cue:** where Ag(q) and 6,(g, 4) are defined similarly to A(q) and (q, 4) with J(g) being replaced by Jo(q).
- **p. 7 / V. Constnainep Motion Operarions - extractive body cue:** Force rate feedback has also been used in F. ‘A more detailed description of the components involved in this control system, real-time implementation issues, and ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (IV. Exp-Errecror Morton Controt), p. 1 (I. Inrropucrion), p. 1 (I. Inrropucrion), p. 3 (I. Inrropucrion), p. 6 (V. Constnainep Motion Operarions), p. 2 (I. Inrropucrion), objective p. 2 (I. Inrropucrion), p. 1 (I. Inrropucrion), p. 1 (Abstract), p. 2 (I. Inrropucrion), p. 3 (X 1 column matrix x of independent configuration parame), p. 3 (I. Inrropucrion), temporal p. 5 (IV. Exp-Errecror Morton Controt), p. 1 (I. Inrropucrion), p. 1 (Abstract), p. 2 (I. Inrropucrion), p. 2 (I. Inrropucrion), p. 3 (I. Inrropucrion).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
