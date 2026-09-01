# Method - Hierarchical Quadratic Programming: Fast Online Humanoid-Robot Motion Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (32 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1177/0278364914521306; PDF retrieval source: https://gepettoweb.laas.fr/uploads/Publications/2014_escande_ijrr.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 28 (B.2 Algorithm 3 termination)): We prove here that each outer loop of Algorithm 3 terminates.

## Method Body Digest

- **p. 28 / B.2 Algorithm 3 termination - extractive body cue:** We prove here that each outer loop of Algorithm 3 terminates.
- **p. 28 / B.2 Algorithm 3 termination - extractive body cue:** We note m the total number of constraints, and w = (∥w1∥, · · · , ∥wp∥).
- **p. 28 / B.2 Algorithm 3 termination - extractive body cue:** The first outer iteration (k = 1) begins with a sequence of activations (at most m) until all the constraints are active or satisfied.
- **p. 3 / 1 Introduction - extractive body cue:** Consider a robot defined by its configuration vector q and whose control input is the joint velocity ˙q.
- **p. 3 / 1 Introduction - extractive body cue:** The evolution in the image space (or task space) with respect to the robot input is given by ˙e = J ˙q, with J = ...
- **p. 4 / 1 Introduction - extractive body cue:** This observation was exploited in [Escande et al., 2010] (which constitute a preliminary version of this work) to fasten the computation of (10).
- **p. 1 / 1 Introduction - extractive body cue:** Time derivatives of this function depend linearly on the robot velocity or acceleration, which gives a set of linear constraints, to be satisfied at best ...
- **p. 2 / 1 Introduction - extractive body cue:** In the cases where damping is not sufficient, clamping was proposed [Raunhardt and Boulic, 2007].

## Design Rationale

- **p. 6 / 1 Introduction - extractive body cue:** We propose an original decomposition that encompasses the hierarchy among the constraints.
- **p. 6 / 1 Introduction - extractive body cue:** 2 Equality hierarchical quadratic program We propose in this section a method to solve a hierarchy of linear equality in the least-square sense.
- **p. 5 / 1 Introduction - extractive body cue:** However, this expressivity reduction enables to obtain very impressive result for walking, jumping or, as shown in [Mordatch et al., 2012], for planning contacts and ...

## Source Evidence Cues

- **p. 28 / B.2 Algorithm 3 termination - extractive body cue:** We prove here that each outer loop of Algorithm 3 terminates.
- **Detected method headings:** B.2 Algorithm 3 termination (p. 28)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | We prove here that each outer loop of Algorithm 3 terminates. | p. 28 (B.2 Algorithm 3 termination) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | We prove here that each outer loop of Algorithm 3 terminates. | p. 28 (B.2 Algorithm 3 termination) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | We prove here that each outer loop of Algorithm 3 terminates. | p. 28 (B.2 Algorithm 3 termination) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 28 / B.2 Algorithm 3 termination - extractive body cue:** We note m the total number of constraints, and w = (∥w1∥, · · · , ∥wp∥).
- **p. 28 / B.2 Algorithm 3 termination - extractive body cue:** The first outer iteration (k = 1) begins with a sequence of activations (at most m) until all the constraints are active or satisfied.
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 28 (B.2 Algorithm 3 termination), p. 28 (B.2 Algorithm 3 termination).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Consider, robot, defined, configuration, vector, whose, control, input, joint, velocity, evolution, image, space, task | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | Consider, robot, defined, configuration, vector, whose, control, input, joint, velocity | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | original, decomposition, encompasses, hierarchy, among, constraints, Equality, hierarchical, quadratic, program | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | note, total, number, constraints, first, outer, iteration, begins, sequence, activations | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1 Introduction - extractive body cue:** Consider a robot defined by its configuration vector q and whose control input is the joint velocity ˙q.
- **p. 3 / 1 Introduction - extractive body cue:** The evolution in the image space (or task space) with respect to the robot input is given by ˙e = J ˙q, with J = ...
- **p. 4 / 1 Introduction - extractive body cue:** This observation was exploited in [Escande et al., 2010] (which constitute a preliminary version of this work) to fasten the computation of (10).
- **p. 1 / 1 Introduction - extractive body cue:** Time derivatives of this function depend linearly on the robot velocity or acceleration, which gives a set of linear constraints, to be satisfied at best ...
- **p. 2 / 1 Introduction - extractive body cue:** In the cases where damping is not sufficient, clamping was proposed [Raunhardt and Boulic, 2007].
- **p. 2 / 1 Introduction - extractive body cue:** In [Mansard et al., 2009], it was proposed to realize an homotopy between the control law with and without avoidance.
- **p. 4 / 1 Introduction - extractive body cue:** The complete solution solving (A1, b1) at best and (A2, b2) if possible is: x∗ 2 = A+ 1 b1 + (A2P1)+(b2 -A2A+ 1 b1) ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | Sequence of subtasks naturally appears from the use of the hierarchy. control in the frame of instantaneous task resolution [De Schutter and ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | Hierarchical Quadratic Programming: Fast Online Humanoid-Robot Motion Generation Adrien Escande JRL-CNRS/AIST Tsukuba, Japan Nicolas Mansard LAAS-CNRS, Univ. | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not recovered | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** prove, here, outer, loop, Algorithm, terminates, note, total, number, constraints, first, iteration, begins, sequence, activations, most, until, active, satisfied, Consider.
- **Relevant PDF headings:** B.2 Algorithm 3 termination (p. 28).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | The robot has to grasp a point object while looking at it and avoiding its joint limits and the collisions with the ... | p. 25 (6.2.2 Results), p. 22 (6.2.2 Results) |
| Balance-aware whole-body execution | 10: Simulation A: Number of algorithm iterations and computation time when using a cascade of QP [Kanoun et al., 2011] and using ... | p. 21 (6.2.2 Results), p. 21 (6.2.2 Results) |
| Recovery / adaptation | Moreover, the numerical behavior is improved by limiting the number of iteration in the search loop. | p. 22 (6.2.2 Results), p. 22 (6.2.2 Results) |

## Failure and Ablation Link

- **p. 21 / 6.2.2 Results - extractive body cue:** 10: Simulation A: Number of algorithm iterations and computation time when using a cascade of QP [Kanoun et al., 2011] and using the HQP without ...
- **p. 21 / 6.2.2 Results - extractive body cue:** In the beginning of each motion sequence (when the ball is just moved), the visibility constraint (67) might be violated without the FOV task (68) ...
- **p. 22 / 6.2.2 Results - extractive body cue:** 6.3 Simulation B: opening a valve The previous movement cannot be generated using the method presented in [De Lasa et al., 2010] since inequality tasks ...
- **p. 22 / 6.2.2 Results - extractive body cue:** The maximal number of iterations is 6 (at the first iteration after the change of the ball position at T=7), the mean number is 0.03 ...
- **p. 23 / 6.2.2 Results - extractive body cue:** Using a warm start of the HQP, the active search loop converges without any update in 97.5% of the 23
- **p. 25 / 6.2.2 Results - extractive body cue:** The grasping task is finally removed when the last position is reached.
- **p. 25 / 6.2.2 Results - extractive body cue:** In exchange, the number of control cycles without update decreases to 96.6%.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 28 (B.2 Algorithm 3 termination), objective p. 28 (B.2 Algorithm 3 termination), p. 28 (B.2 Algorithm 3 termination), temporal p. 1 (1 Introduction), p. 1 (Front matter), p. 6 (1 Introduction), p. 6 (1 Introduction), p. 7 (1 U T), p. 12 (2.6 Conclusion).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
