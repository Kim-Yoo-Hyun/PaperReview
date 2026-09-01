# Method - GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: official NVIDIA technical page body (no public PDF identified) checked on 2026-09-02 (1 source page(s); official NVIDIA technical page body (no public PDF identified); extraction quality: high); canonical paper source: https://research.nvidia.com/labs/gear/gr00t-n1_5/; body source: https://research.nvidia.com/labs/gear/gr00t-n1_5/. The note is an evidence-anchored official source body analysis; exact tables/equations or section details remain at the cited source anchors. Evidence boundary: selected official source body statements and source anchors were used; no PDF was identified at review time. Reading tracker status/evidence was not changed.

## Method in One Sentence

official source body method statement (p. 1 (Joint Policy Learning and World Modeling Objective), p. 1 (Model and Data Updates)): We used FLARE loss coefficient 0.2 for both pretraining and posttraining.

## Method Body Digest

- **p. 1 / Joint Policy Learning and World Modeling Objective - extractive body cue:** We used FLARE loss coefficient 0.2 for both pretraining and posttraining.
- **p. 1 / Model and Data Updates - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.
- **p. 1 / Post-training on Unitree G1 - extractive body cue:** We attribute these improvements to the improved grounding capabilities, usage of the FLARE loss and the diverse data from DreamGen.
- **p. 1 / GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** GR00T N1.5 Policy rollout with language prompt: "Pick the apple from table to plate"

## Design Rationale

- **p. 1 / GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.
- **p. 1 / Learning to manipulate novel objects from human ego videos - extractive body cue:** As shown in the FLARE project , future latent representation alignment enables learning directly from human ego videos.

## Source Evidence Cues

- **p. 1 / Joint Policy Learning and World Modeling Objective - extractive body cue:** We used FLARE loss coefficient 0.2 for both pretraining and posttraining.
- **p. 1 / Model and Data Updates - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.
- **Detected method headings:** GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots (p. 1); Model and Data Updates (p. 1); Joint Policy Learning and World Modeling Objective (p. 1); Architecture validation (p. 1)

## Pipeline

| Module | Purpose | Input | Operation | Output | official source body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | We used FLARE loss coefficient 0.2 for both pretraining and posttraining. | p. 1 (Joint Policy Learning and World Modeling Objective), p. 1 (Model and Data Updates) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions. | p. 1 (Model and Data Updates) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | We used FLARE loss coefficient 0.2 for both pretraining and posttraining. | p. 1 (Joint Policy Learning and World Modeling Objective) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Post-training on Unitree G1 - extractive body cue:** We attribute these improvements to the improved grounding capabilities, usage of the FLARE loss and the diverse data from DreamGen.
- **p. 1 / Joint Policy Learning and World Modeling Objective - extractive body cue:** We used FLARE loss coefficient 0.2 for both pretraining and posttraining.
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 1 (Joint Policy Learning and World Modeling Objective), p. 1 (Joint Policy Learning and World Modeling Objective).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | vision-language, embeddings, VLM, then, cross-attended, DiT, processes, state, noised, actions, GR00T, Policy, rollout, language | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | vision-language, embeddings, VLM, then, cross-attended, DiT, processes, state, noised, actions | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | introduce, GR00T, upgraded, version, foundation, model, humanoid, robots, FLARE, project | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | attribute, improvements, improved, grounding, capabilities, usage, FLARE, loss, diverse, data | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Model and Data Updates - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.
- **p. 1 / GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots - extractive body cue:** GR00T N1.5 Policy rollout with language prompt: "Pick the apple from table to plate"
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | official source body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | We trained GR00T N1.5 for 250K steps on 1K H100 GPUs with global batch size 16384. | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | GR00T N1.5 Policy rollout with language prompt: "Pick the apple from table to plate" | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not recovered | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Joint Policy Learning and World Modeling Objective - extractive body cue:** We used FLARE loss coefficient 0.2 for both pretraining and posttraining.
- **p. 1 / Joint Policy Learning and World Modeling Objective - extractive body cue:** We trained GR00T N1.5 for 250K steps on 1K H100 GPUs with global batch size 16384.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** FLARE, loss, coefficient, pretraining, posttraining, vision-language, embeddings, VLM, then, cross-attended, DiT, processes, state, noised, actions, attribute, improvements, improved, grounding, capabilities.
- **Relevant PDF headings:** GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots (p. 1); Model and Data Updates (p. 1); Joint Policy Learning and World Modeling Objective (p. 1); Architecture validation (p. 1).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | In order to tune the model architecture for N1.5, we trained policies from scratch on two sim robot benchmarks requiring language following: ... | p. 1 (Architecture validation), p. 1 (Post-training on Unitree G1) |
| Balance-aware whole-body execution | We expect users of N1.5 should observe better performance compared to N1, in particular improved generalization and better language following ability. | p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots), p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots) |
| Recovery / adaptation | It achieves higher success rate, can use more diverse data sources, and has significantly improved language following capabilities. | p. 1 (Post-training on Unitree G1), p. 1 (Architecture validation) |

## Failure and Ablation Link

- **p. 1 / Joint Policy Learning and World Modeling Objective - extractive body cue:** Distribution of training data in GR00T N1.5 pretraining.
- **p. 1 / Model and Data Updates - extractive body cue:** The VLM model is frozen during both pretraining and finetuning.
- **p. 1 / Generalization to novel behaviors using Neural Trajectories - extractive body cue:** Although these new verbs can be considered "zero-shot" in the sense that we never collected teleoperation data for these tasks, we still train explicitly on ...
- **p. 1 / Model and Data Updates - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Joint Policy Learning and World Modeling Objective), p. 1 (Model and Data Updates), objective p. 1 (Post-training on Unitree G1), p. 1 (Joint Policy Learning and World Modeling Objective), temporal p. 1 (Joint Policy Learning and World Modeling Objective), p. 1 (GR00T N1.5 An Improved Open Foundation Model for Generalist Humanoid Robots).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
