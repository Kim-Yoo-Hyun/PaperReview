# Method - GR00T N1.6: An Improved Open Foundation Model for Generalist Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (2 pages; PyMuPDF text; extraction quality: medium); canonical paper source: https://research.nvidia.com/labs/gear/gr00t-n1_6/; PDF retrieval source: https://research.nvidia.com/labs/gear/gr00t-n1_6/. PDF provenance note: official NVIDIA technical page rendered to a task-scoped PDF snapshot; no author-supplied publication PDF identified. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (Model and Data Improvements), p. 1 (Model and Data Improvements)): Predicts state-relative action chunks for most embodiments, rather than absolute joint angles or EEF positions.

## Method Body Digest

- **p. 1 / Model and Data Improvements - extractive body cue:** Predicts state-relative action chunks for most embodiments, rather than absolute joint angles or EEF positions.
- **p. 1 / Model and Data Improvements - extractive body cue:** Removes N1.5's post-VLM 4-layer transformer adapter.
- **p. 1 / Model and Data Improvements - extractive body cue:** The VLM is trained on both general vision-language tasks and embodied reasoning tasks like next action prediction.
- **p. 2 / Discussion - extractive body cue:** More fine-grained subtask annotation can improve language following, but not yet reaching robust generalization.
- **p. 2 / Discussion - extractive body cue:** Multi-task language following and out-of-distribution task generalization continue to be challenging for current VLA models.

## Design Rationale

- **p. 1 / Introduction - extractive body cue:** We introduce GR00T N1.6, an improved version of the GR00T N1.5 foundation model for humanoid robots.

## Source Evidence Cues

- **p. 1 / Model and Data Improvements - extractive body cue:** Predicts state-relative action chunks for most embodiments, rather than absolute joint angles or EEF positions.
- **p. 1 / Model and Data Improvements - extractive body cue:** Removes N1.5's post-VLM 4-layer transformer adapter.
- **Detected method headings:** Model and Data Improvements (p. 1)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | Predicts state-relative action chunks for most embodiments, rather than absolute joint angles or EEF positions. | p. 1 (Model and Data Improvements), p. 1 (Model and Data Improvements) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | Removes N1.5's post-VLM 4-layer transformer adapter. | p. 1 (Model and Data Improvements) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | Predicts state-relative action chunks for most embodiments, rather than absolute joint angles or EEF positions. | p. 1 (Model and Data Improvements) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Model and Data Improvements - extractive body cue:** The VLM is trained on both general vision-language tasks and embodied reasoning tasks like next action prediction.
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Predicts, state-relative, action, chunks, most, embodiments, rather, absolute, joint, angles, EEF, positions, VLM, trained | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | Predicts, state-relative, action, chunks, most, embodiments, rather, absolute, joint, angles | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | introduce, GR00T, improved, version, foundation, model, humanoid, robots, Predicts, state-relative | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | VLM, trained, general, vision-language, tasks, embodied, reasoning, like, next, action | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Model and Data Improvements - extractive body cue:** Predicts state-relative action chunks for most embodiments, rather than absolute joint angles or EEF positions.
- **p. 1 / Model and Data Improvements - extractive body cue:** The VLM is trained on both general vision-language tasks and embodied reasoning tasks like next action prediction.
- **p. 2 / Discussion - extractive body cue:** More fine-grained subtask annotation can improve language following, but not yet reaching robust generalization.
- **p. 2 / Discussion - extractive body cue:** Multi-task language following and out-of-distribution task generalization continue to be challenging for current VLA models.
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | In the following robot experiments, we further post-train on small task-specific datasets; typically 10K-30K steps with global batch size 1K or less. | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | Predicts state-relative action chunks for most embodiments, rather than absolute joint angles or EEF positions. | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not recovered | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Experiments - extractive body cue:** In the following robot experiments, we further post-train on small task-specific datasets; typically 10K-30K steps with global batch size 1K or less.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Predicts, state-relative, action, chunks, most, embodiments, rather, absolute, joint, angles, EEF, positions, Removes, post-VLM, layer, transformer, adapter, VLM, trained, general.
- **Relevant PDF headings:** Model and Data Improvements (p. 1).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | In the following robot experiments, we further post-train on small task-specific datasets; typically 10K-30K steps with global batch size 1K or less. | p. 1 (Experiments), p. 1 (Discussion) |
| Balance-aware whole-body execution | We expect users of N1.6 should observe better post-training performance compared to N1.5. | p. 1 (Introduction), p. 1 (Introduction) |
| Recovery / adaptation | When scaling up real-world experiments, we incorporate various lessons learned from the robot learning community to improve model success rates during rollouts. | p. 1 (Discussion), p. 1 (Introduction) |

## Failure and Ablation Link

- **p. 1 / Model and Data Improvements - extractive body cue:** Removes N1.5's post-VLM 4-layer transformer adapter.
- **p. 1 / Model and Data Improvements - extractive body cue:** Architectural changes: Base VLM: We use an internal NVIDIA Cosmos-2B VLM variant.
- **p. 2 / Discussion - extractive body cue:** More fine-grained subtask annotation can improve language following, but not yet reaching robust generalization.
- **p. 2 / Discussion - extractive body cue:** Test-time and train-time RTC provide performance boosts to motion smoothness and robustness during asynchronous rollouts.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Model and Data Improvements), p. 1 (Model and Data Improvements), objective p. 1 (Model and Data Improvements), temporal p. 1 (Experiments), p. 1 (Model and Data Improvements), p. 2 (Discussion).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
