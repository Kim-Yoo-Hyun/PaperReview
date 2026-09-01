# Method - Dynamic Whole-Body Motion Generation under Rigid Contacts and Other Unilateral Constraints

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://hal.science/lirmm-00831097; PDF retrieval source: https://hal-lirmm.ccsd.cnrs.fr/file/index/docid/831097/filename/2013_itro_saab-Dynamic_Whole_Body_Motion_Generation.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 9 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 9 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS)): Including the contact forces within the QP Solver Condition (32) must now be introduced in the HQP proposed at the end of Section IV-B 1) A first way of modeling ...

## Method Body Digest

- **p. 7 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Including the contact forces within the QP Solver Condition (32) must now be introduced in the HQP proposed at the end of Section IV-B 1) ...
- **p. 7 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** To cope with this problem we propose to include the contact forces f in the optimization variables of the QP resolution.
- **p. 8 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Opening to other classes of contacts The model (22)-(38) is built on the rigid point contact.
- **p. 8 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Finally, the complete HQP for n contacts and k tasks is written: (39) ≺(22.1) ≺(38.1) ≺... ≺(22.n) ≺(38.n) ≺ (14.1) ≺... ≺(14.k) ≺(40), with the ...
- **p. 9 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Submitted to IEEE Transaction on Robotics 8 of motion (22) [40].
- **p. 9 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Motions with slips are made possible by removing the motion constraint (22) in the tangent directions, and setting a constraint on the tangent force to ...
- **p. 8 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Elastic contact can be defined by modifying the equation 8Similarly, the constraint can be imposed on a least-square τ.
- **p. 8 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** The choice of using the minimum velocity constraint is arbitrary.

## Design Rationale

- **p. 3 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a generic solution to take into account equalities and inequalities in a strict hierarchy to generate a dynamic motion.
- **p. 7 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** To cope with this problem we propose to include the contact forces f in the optimization variables of the QP resolution.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In total, the motion has to be designed in a set that lives in the high-dimensional configuration space but is implicitly limited to a much ...

## Source Evidence Cues

- **p. 7 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Including the contact forces within the QP Solver Condition (32) must now be introduced in the HQP proposed at the end of Section IV-B 1) ...
- **p. 7 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** To cope with this problem we propose to include the contact forces f in the optimization variables of the QP resolution.
- **p. 8 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Opening to other classes of contacts The model (22)-(38) is built on the rigid point contact.
- **p. 8 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Finally, the complete HQP for n contacts and k tasks is written: (39) ≺(22.1) ≺(38.1) ≺... ≺(22.n) ≺(38.n) ≺ (14.1) ≺... ≺(14.k) ≺(40), with the ...
- **p. 9 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Submitted to IEEE Transaction on Robotics 8 of motion (22) [40].
- **p. 9 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Motions with slips are made possible by removing the motion constraint (22) in the tangent directions, and setting a constraint on the tangent force to ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | Including the contact forces within the QP Solver Condition (32) must now be introduced in the HQP proposed at the end of ... | p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | To cope with this problem we propose to include the contact forces f in the optimization variables of the QP resolution. | p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | Opening to other classes of contacts The model (22)-(38) is built on the rigid point contact. | p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 8 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Elastic contact can be defined by modifying the equation 8Similarly, the constraint can be imposed on a least-square τ.
- **p. 7 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Including the contact forces within the QP Solver Condition (32) must now be introduced in the HQP proposed at the end of Section IV-B 1) ...
- **p. 8 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** The choice of using the minimum velocity constraint is arbitrary.
- **p. 9 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Motions with slips are made possible by removing the motion constraint (22) in the tangent directions, and setting a constraint on the tangent force to ...
- **p. 9 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** In the remaining of the paper, the reduced rigid planar formulation is used, since it keeps a relatively low computational cost while covering many possible ...
- **p. 7 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** To cope with this problem we propose to include the contact forces f in the optimization variables of the QP resolution.
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 9 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | eases, sensory, feedback, since, space, often, good, task-space, candidate, notation, necessary, sufficient, condition, ensure | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | eases, sensory, feedback, since, space, often, good, task-space, candidate, notation | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | generic, solution, take, account, equalities, inequalities, strict, hierarchy, generate, dynamic | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | Elastic, contact, defined, modifying, equation, Similarly, constraint, imposed, least-square, Including | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / I. INTRODUCTION - extractive body cue:** It also eases the use of sensory feedback, since the sensory space is often a good task-space candidate [14], [15].
- **p. 7 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Using this notation, the necessary and sufficient condition to ensure the contact stability (in the sense that the contact remains in the same phase of ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** Submitted to IEEE Transaction on Robotics 2 quadratic program (QP) [23].
- **p. 8 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** The point clouds display the ZMP of random forces admissible in the sense of (35).
- **p. 2 / I. INTRODUCTION - extractive body cue:** These constraints can typically be formulated as equalities (e.g. zero velocity at rigid-contact points [4]), and inequalities (e.g. joint position [5], velocity or torques bounds, ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** In [36], a first solution to handle inequalities in the stack of tasks was proposed, but cannot set any inequality constraint on the contact forces.
- **p. 7 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** To cope with this problem we propose to include the contact forces f in the optimization variables of the QP resolution.
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | The temporal sequence of tasks is given in Fig. | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | It is computed using the control framework SOT [33] and the dedicated solver [26]. | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not recovered | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Including the contact forces within the QP Solver Condition (32) must now be introduced in the HQP proposed at the end of Section IV-B 1) ...
- **p. 9 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Motions with slips are made possible by removing the motion constraint (22) in the tangent directions, and setting a constraint on the tangent force to ...
- **p. 11 / VII. EXPERIMENTS - extractive body cue:** Then the distance of the point ψ∗(46) to this constraint set is computed.
- **p. 11 / VII. EXPERIMENTS - extractive body cue:** First, the distance is computed to the constraint set of the solver (the 4cm-wide support polygon).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Including, contact, forces, within, Solver, Condition, must, introduced, HQP, Section, IV-B, first, modeling, problem, constraints, should, written, respect, optimization, variables.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | The result of this simulation is a joint trajectory of the robot, that complies to the multi-body dynamics. | p. 10 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS) |
| Balance-aware whole-body execution | All the joints are properly stopped at the limit, and can leave the neighborhood of the limit without being stuck as it ... | p. 12 (VII. EXPERIMENTS), p. 14 (VII. EXPERIMENTS) |
| Recovery / adaptation | To improve the naturalness of the motion, a task egaze defined by (50) is set to constrain the gaze toward the armrest ... | p. 12 (VII. EXPERIMENTS), p. 14 (VII. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 12 / VII. EXPERIMENTS - extractive body cue:** All the joints are properly stopped at the limit, and can leave the neighborhood of the limit without being stuck as it may appear with ...
- **p. 14 / VII. EXPERIMENTS - extractive body cue:** From t = 0.7s, the COM is out of the support polygon with a positive velocity: it is then impossible to bring it back to ...
- **p. 10 / VII. EXPERIMENTS - extractive body cue:** The simulator checks the collision, computes the acceleration from the collision set and the torque input using a linear solver and numerically integrates ¨q using ...
- **p. 12 / VII. EXPERIMENTS - extractive body cue:** To prevent a collision when grasping, an intermediate point is first reached, above the grasping position.
- **p. 12 / VII. EXPERIMENTS - extractive body cue:** In reaction, all the other aligned joints move to overrun the neck limitation (chest joint of course, but also hip and ankle joints).
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 4. At low frequency, the ZMP does not saturate because the demanded accelerations are small enough. At medium frequency, the accelerations are larger and ...
- **p. 15 / VIII. CONCLUSION - extractive body cue:** Experiment C: Robustness criterion VI-C.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 9 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 9 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), objective p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 9 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 9 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), temporal p. 12 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS), p. 11 (VII. EXPERIMENTS), p. 11 (VII. EXPERIMENTS), p. 12 (VII. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
