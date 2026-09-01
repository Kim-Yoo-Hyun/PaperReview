# Method - VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/He_VIRAL_Visual_Sim-to-Real_at_Scale_for_Humanoid_Loco-Manipulation_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/He_VIRAL_Visual_Sim-to-Real_at_Scale_for_Humanoid_Loco-Manipulation_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (2.1. Key Elements of Teacher Training), p. 4 (2.2. Key Elements of Student Training), p. 3 (2.1. Key Elements of Teacher Training), p. 4 (2.2. Key Elements of Student Training), p. 5 (2.2. Key Elements of Student Training), p. 5 (2.2. Key Elements of Student Training)): Proprioception consists of oprop-priv t = [vt, ωt, gt, at→1, qt, ˙qt, f finger t ] where vt, ωt are base linear and angular velocities, gt is base projected gravity, ...

## Method Body Digest

- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** Proprioception consists of oprop-priv t = [vt, ωt, gt, at→1, qt, ˙qt, f finger t ] where vt, ωt are base linear and angular velocities, ...
- **p. 4 / 2.2. Key Elements of Student Training - extractive body cue:** For the student's vision backbone, we adopt a state-of-the-art image encoder [61] to extract high-quality RGB features, which are fused with proprioceptive to the policy ...
- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** At time step t, the teacher ωteacher(at/opriv t ) outputs a high-level command for the low-level WBC policy given privileged observation.
- **p. 4 / 2.2. Key Elements of Student Training - extractive body cue:** This mixed-policy rollout combines the fast initialization of BC with the state-coverage benefits of DAgger, producing a more resilient vision-based controller.
- **p. 5 / 2.2. Key Elements of Student Training - extractive body cue:** We identify scaling up GPUs for both teacher and student training as critical in our ablation studies in Figure 14 and Figure 15.
- **p. 5 / 2.2. Key Elements of Student Training - extractive body cue:** This implementation preserves the simplicity of single-GPU training while enabling near-linear scaling to large clusters for high-throughput visual sim-to-real learning.
- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** Therefore, we define four key rewards: 1.
- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** Full reward definitions are provided in Section 7.2.

## Design Rationale

- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** Proprioception consists of oprop-priv t = [vt, ωt, gt, at→1, qt, ˙qt, f finger t ] where vt, ωt are base linear and angular velocities, ...
- **p. 2 / 1. Introduction - extractive body cue:** Our goal is not to propose yet another novel RL or sim-to-real algorithm, but to provide a technical recipe on the full stack required to ...

## Source Evidence Cues

- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** Proprioception consists of oprop-priv t = [vt, ωt, gt, at→1, qt, ˙qt, f finger t ] where vt, ωt are base linear and angular velocities, ...
- **p. 4 / 2.2. Key Elements of Student Training - extractive body cue:** For the student's vision backbone, we adopt a state-of-the-art image encoder [61] to extract high-quality RGB features, which are fused with proprioceptive to the policy ...
- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** At time step t, the teacher ωteacher(at/opriv t ) outputs a high-level command for the low-level WBC policy given privileged observation.
- **p. 4 / 2.2. Key Elements of Student Training - extractive body cue:** This mixed-policy rollout combines the fast initialization of BC with the state-coverage benefits of DAgger, producing a more resilient vision-based controller.
- **p. 5 / 2.2. Key Elements of Student Training - extractive body cue:** We identify scaling up GPUs for both teacher and student training as critical in our ablation studies in Figure 14 and Figure 15.
- **p. 5 / 2.2. Key Elements of Student Training - extractive body cue:** This implementation preserves the simplicity of single-GPU training while enabling near-linear scaling to large clusters for high-throughput visual sim-to-real learning.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | Proprioception consists of oprop-priv t = [vt, ωt, gt, at→1, qt, ˙qt, f finger t ] where vt, ωt are base linear ... | p. 3 (2.1. Key Elements of Teacher Training), p. 4 (2.2. Key Elements of Student Training) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | For the student's vision backbone, we adopt a state-of-the-art image encoder [61] to extract high-quality RGB features, which are fused with proprioceptive ... | p. 4 (2.2. Key Elements of Student Training), p. 3 (2.1. Key Elements of Teacher Training) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | At time step t, the teacher ωteacher(at/opriv t ) outputs a high-level command for the low-level WBC policy given privileged observation. | p. 3 (2.1. Key Elements of Teacher Training), p. 4 (2.2. Key Elements of Student Training) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** Therefore, we define four key rewards: 1.
- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** Full reward definitions are provided in Section 7.2.
- **p. 4 / 2.1. Key Elements of Teacher Training - extractive body cue:** This reference-biased exploration greatly reduces reliance on brittle reward tuning and improves sim-to-real transfer, as human-provided grasping and placement poses offer strong priors.
- **p. 4 / 2.1. Key Elements of Teacher Training - extractive body cue:** Frames of reference state initialization for teacher RL. skills for high-DoF humanoids with RL typically demands heavy reward engineering still often yields suboptimal or poor ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 4 (2.2. Key Elements of Student Training), p. 3 (2.1. Key Elements of Teacher Training).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Phase, simulation, privileged, teacher, policy, receives, full-state, proprioception, exteroception, task, information, outputs, WBC, commands | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | Phase, simulation, privileged, teacher, policy, receives, full-state, proprioception, exteroception, task | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | Proprioception, consists, oprop-priv, finger, where, base, linear, angular, velocities, projected | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | Therefore, define, four, rewards, Full, reward, definitions, provided, Section, reference-biased | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive body cue:** Phase 1: In simulation, a privileged RL teacher policy ωteacher receives full-state proprioception and exteroception of the task information and outputs WBC commands.
- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** At time step t, the teacher ωteacher(at/opriv t ) outputs a high-level command for the low-level WBC policy given privileged observation.
- **p. 2 / 1. Introduction - extractive body cue:** Teacher Action Privileged Exteroception Privileged Proprioception Sim-to-Real Student Policy a Privileged Teacher Policy 50Hz Phase 2 Supervised Learning Phase 1 Reinforcement Learning PD Controller (200Hz) ...
- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** Specifically, the teacher policy outputs at = (!vt, !ωyaw t , !qarm t , !qfinger t ) as the command for the WBC policy [6], ...
- **p. 4 / 2.2. Key Elements of Student Training - extractive body cue:** For the student's vision backbone, we adopt a state-of-the-art image encoder [61] to extract high-quality RGB features, which are fused with proprioceptive to the policy ...
- **p. 4 / 2.2. Key Elements of Student Training - extractive body cue:** The resulting student observation ostudent therefore integrates both visual embeddings and the proprioception available on real hardware, enabling the policy to reason over rich visual ...
- **p. 1 / 1. Introduction - extractive body cue:** Humanoid robots are often framed as the natural embodiment of general-purpose physical intelligence: machines that could ultimately take on a large fraction of physical work ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | We also evaluate choices for the student policy head, including a single-step MLP and a history-aware architecture that incorporates temporal context. | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | At time step t, the teacher ωteacher(at/opriv t ) outputs a high-level command for the low-level WBC policy given privileged observation. | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | We also evaluate choices for the student policy head, including a single-step MLP and a history-aware architecture that incorporates temporal context. | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 2.2. Key Elements of Student Training - extractive body cue:** This mixed-policy rollout combines the fast initialization of BC with the state-coverage benefits of DAgger, producing a more resilient vision-based controller.
- **p. 5 / 2.2. Key Elements of Student Training - extractive body cue:** We identify scaling up GPUs for both teacher and student training as critical in our ablation studies in Figure 14 and Figure 15.
- **p. 5 / 2.2. Key Elements of Student Training - extractive body cue:** This implementation preserves the simplicity of single-GPU training while enabling near-linear scaling to large clusters for high-throughput visual sim-to-real learning.
- **p. 5 / 2.2. Key Elements of Student Training - extractive body cue:** This implementation preserves the simplicity of single-GPU training while enabling near-linear scaling to large clusters for high-throughput visual sim-to-real learning.
- **p. 5 / 2.2. Key Elements of Student Training - extractive body cue:** To scale up visual simulation training throughput, we implement a customized version of TRL [68] with support of Accelerate [22] for efficient scaling across multiple ...
- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** The teacher is trained with PPO [59] with a custom implementation of TRL [68] to train across GPUs in a distributed manner.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Proprioception, consists, oprop-priv, finger, where, base, linear, angular, velocities, projected, gravity, last, action, joint, positions, fingertip, forces, student, vision, backbone.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | We assess real-world generalization by systematically varying the environment along multiple factors, including tray start position, robot start pose, table height, lighting, ... | p. 6 (3.2. Generalization), p. 6 (3.1. Robustness) |
| Balance-aware whole-body execution | These results show that although expert-level success remains challenging, VIRAL achieves near-expert success performance while being faster than the expert, and it ... | p. 6 (3.1. Robustness), p. 5 (Figure/Table caption) |
| Recovery / adaptation | These results show that although expert-level success remains challenging, VIRAL achieves near-expert success performance while being faster than the expert, and it ... | p. 6 (3.1. Robustness), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / Figure/Table caption - extractive body cue:** Figure 9. Ablations of teacher policy training. Training rewards (left) and success rates (right) for the full method (RSI + delta ac- tion), without demonstration ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. VIRAL teacher-student pipeline. Phase 1: In simulation, a privileged RL teacher policy ωteacher receives full-state proprioception and exteroception of the task information and ...
- **p. 6 / 3.2. Generalization - extractive body cue:** Across these variations, VIRAL consistently completes the task without additional tuning, indicating strong robustness.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 10. Ablation of vision backbone for student policy.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 11. Ablation of ratio of DAgger/BC of student policy.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 16. Ablation of object generalization of teacher policy.
- **p. 3 / 2.1. Key Elements of Teacher Training - extractive body cue:** Note that VIRAL framework does not have designs overfitting to specific WBC policy, and can be extended to other humanoid WBC controllers [44, 78].

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (2.1. Key Elements of Teacher Training), p. 4 (2.2. Key Elements of Student Training), p. 3 (2.1. Key Elements of Teacher Training), p. 4 (2.2. Key Elements of Student Training), p. 5 (2.2. Key Elements of Student Training), p. 5 (2.2. Key Elements of Student Training), objective p. 3 (2.1. Key Elements of Teacher Training), p. 3 (2.1. Key Elements of Teacher Training), p. 4 (2.1. Key Elements of Teacher Training), p. 4 (2.1. Key Elements of Teacher Training), temporal p. 4 (2.2. Key Elements of Student Training), p. 3 (2.1. Key Elements of Teacher Training), p. 5 (2.3. Key Elements of Sim-to-Real Transfer), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
