# Method - Expressive Whole-Body Control for Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p107.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p107.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (II. PROBLEM FORMULATION), p. 3 (II. PROBLEM FORMULATION)): We assume in the rest of this paper, without loss of generality, that the observation and action space are given by the H1 humanoid robot design.

## Method Body Digest

- **p. 3 / II. PROBLEM FORMULATION - extractive body cue:** We assume in the rest of this paper, without loss of generality, that the observation and action space are given by the H1 humanoid robot ...
- **p. 3 / II. PROBLEM FORMULATION - extractive body cue:** We consider humanoid motion control as learning a goalconditioned motor policy π : G ×S 7→A, where G is the goal space that specifies the ...
- **p. 3 / II. PROBLEM FORMULATION - extractive body cue:** However, our proposed approach should generalize to similar body forms that differ in the exact number of actuated degrees of freedom. a) Command-conditioned Locomotion Control: ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We propose to train a novel controller that takes both a reference motion and a root movement command as inputs for real humanoid robot control.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our work benefits from prior research from the computer graphics community on physics-based character animation [35], and from the robotics community on using deep reinforcement ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** We also compare our method with applying more imitation constraints on legged motion in both simulation and the real world and show our approach that ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We propose to train a novel controller that takes both a reference motion and a root movement command as inputs for real humanoid robot control.

## Source Evidence Cues

- **p. 3 / II. PROBLEM FORMULATION - extractive body cue:** We assume in the rest of this paper, without loss of generality, that the observation and action space are given by the H1 humanoid robot ...
- **p. 3 / II. PROBLEM FORMULATION - extractive body cue:** We consider humanoid motion control as learning a goalconditioned motor policy π : G ×S 7→A, where G is the goal space that specifies the ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | We assume in the rest of this paper, without loss of generality, that the observation and action space are given by the ... | p. 3 (II. PROBLEM FORMULATION), p. 3 (II. PROBLEM FORMULATION) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | We consider humanoid motion control as learning a goalconditioned motor policy π : G ×S 7→A, where G is the goal space ... | p. 3 (II. PROBLEM FORMULATION) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | We assume in the rest of this paper, without loss of generality, that the observation and action space are given by the ... | p. 3 (II. PROBLEM FORMULATION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / II. PROBLEM FORMULATION - extractive body cue:** We assume in the rest of this paper, without loss of generality, that the observation and action space are given by the H1 humanoid robot ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 3 (II. PROBLEM FORMULATION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | consider, humanoid, motion, control, learning, goalconditioned, motor, policy, where, goal, space, specifies, behavior, observation | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | consider, humanoid, motion, control, learning, goalconditioned, motor, policy, where, goal | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | compare, applying, more, imitation, constraints, legged, motion, simulation, real, world | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | assume, rest, without, loss, generality, observation, action, space, given, humanoid | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / II. PROBLEM FORMULATION - extractive body cue:** We consider humanoid motion control as learning a goalconditioned motor policy π : G ×S 7→A, where G is the goal space that specifies the ...
- **p. 3 / II. PROBLEM FORMULATION - extractive body cue:** However, our proposed approach should generalize to similar body forms that differ in the exact number of actuated degrees of freedom. a) Command-conditioned Locomotion Control: ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We propose to train a novel controller that takes both a reference motion and a root movement command as inputs for real humanoid robot control.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our work benefits from prior research from the computer graphics community on physics-based character animation [35], and from the robotics community on using deep reinforcement ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | How expressive goal Ge affects stepping frequency We do | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | 7: We sample 20-second simulation rollouts with 4096 environments and take the mean episode length as our metric. | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not recovered | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** assume, rest, without, loss, generality, observation, action, space, given, humanoid, robot, design, consider, motion, control, learning, goalconditioned, motor, policy, where.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | In this section we aim to answer the following questions through extensive experiments both in sim and the real world: • How ... | p. 5 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Balance-aware whole-body execution | We compare with baselines to show that our approach ExBody is superior compared with other design choices. | p. 6 (IV. RESULTS), p. 8 (IV. RESULTS) |
| Recovery / adaptation | V, our method achieves the best linear velocity tracking performance (MELV). | p. 6 (IV. RESULTS), p. 6 (IV. RESULTS) |

## Failure and Ablation Link

- **p. 5 / IV. RESULTS - extractive body cue:** We can see that our policy can track roll, pitch and root height well without being affected by walking velocity.
- **p. 5 / IV. RESULTS - extractive body cue:** Our baselines are as follows: • ExBody + AMP: This baseline uses an AMP reward to encourage the policy's transitions to be similar to those ...
- **p. 7 / IV. RESULTS - extractive body cue:** ExBody + AMP NoReg tries to replace the regularization terms in Tab.
- **p. 9 / VII. LIMITATIONS - extractive body cue:** Auto recovery and initialization could be explored to reduce the cost of doing experiments.
- **p. 9 / VI. DISCUSSIONS - extractive body cue:** We introduce a method designed to enable a humanoid robot to track expressive upper body motions while ensuring the maintenance of robust locomotion capabilities in ...
- **p. 5 / IV. RESULTS - extractive body cue:** Note that although Random Sample looks better than Motion Sample, the heatmap does not consider the sample density.
- **p. 6 / IV. RESULTS - extractive body cue:** Why does not ExBody do full DoF tracking?

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (II. PROBLEM FORMULATION), p. 3 (II. PROBLEM FORMULATION), objective p. 3 (II. PROBLEM FORMULATION), temporal p. 7 (IV. RESULTS), p. 7 (IV. RESULTS), p. 8 (IV. RESULTS), p. 8 (IV. RESULTS), p. 1 (I. INTRODUCTION), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
