# Method - GR00T N1.5: An Improved Open Foundation Model for Generalist Humanoid Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (3 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/labs/gear/gr00t-n1_5/; PDF retrieval source: https://research.nvidia.com/labs/gear/gr00t-n1_5/. PDF provenance note: official NVIDIA technical page rendered to a task-scoped PDF snapshot; no author-supplied publication PDF identified. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (Architecture), p. 1 (Architecture), p. 2 (Architecture validation), p. 2 (Data-limited post-training in simulated environments), p. 3 (Post-training on Unitree G1), p. 3 (Post-training on Unitree G1)): We used FLARE loss coefficient 0.2 for both pretraining and posttraining.

## Method Body Digest

- **p. 1 / Architecture - extractive body cue:** We used FLARE loss coefficient 0.2 for both pretraining and posttraining.
- **p. 1 / Architecture - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.
- **p. 2 / Architecture validation - extractive body cue:** We find that the N1.5 architecture achieves significantly higher success rates on both benchmarks, indicating stronger language-conditioned control ability.
- **p. 2 / Data-limited post-training in simulated environments - extractive body cue:** Following the GR00T N1 evaluation protocol, we evaluate N1.5's performance in data-limited post-training.
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** We observe that the post-trained GR00T N1.5 achieves much higher success rate than N1 for previously seen objects (toy fruits seen in the GR-1 pretraining ...
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** Model / GR00T N1, 1K Demos / GR00T N1.5, 1K Demos / GR00T N1.5, 1K Demos Task / Place 1 of 2 fruits onto plate; ...
- **p. 1 / Architecture - extractive body cue:** Joint Policy Learning and World Modeling Objective
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** As in the GR-1 language following experiment, we initialize the scene with one target object and one distractor object, with the target object having equal ...

## Design Rationale

- **p. 1 / Introduction - extractive body cue:** We introduce GR00T N1.5, an upgraded version of the GR00T N1 foundation model for humanoid robots.
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** Novel Objects As shown in the FLARE project, future latent representation alignment enables learning directly from human ego videos.
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** This allows learning to manipulate novel objects from human videos and minimal robot demonstrations.

## Source Evidence Cues

- **p. 1 / Architecture - extractive body cue:** We used FLARE loss coefficient 0.2 for both pretraining and posttraining.
- **p. 1 / Architecture - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.
- **p. 2 / Architecture validation - extractive body cue:** We find that the N1.5 architecture achieves significantly higher success rates on both benchmarks, indicating stronger language-conditioned control ability.
- **p. 2 / Data-limited post-training in simulated environments - extractive body cue:** Following the GR00T N1 evaluation protocol, we evaluate N1.5's performance in data-limited post-training.
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** We observe that the post-trained GR00T N1.5 achieves much higher success rate than N1 for previously seen objects (toy fruits seen in the GR-1 pretraining ...
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** Model / GR00T N1, 1K Demos / GR00T N1.5, 1K Demos / GR00T N1.5, 1K Demos Task / Place 1 of 2 fruits onto plate; ...
- **Detected method headings:** Model and Data Updates (p. 1); Architecture (p. 1); Architecture validation (p. 1)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | We used FLARE loss coefficient 0.2 for both pretraining and posttraining. | p. 1 (Architecture), p. 1 (Architecture) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions. | p. 1 (Architecture), p. 2 (Architecture validation) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | We find that the N1.5 architecture achieves significantly higher success rates on both benchmarks, indicating stronger language-conditioned control ability. | p. 2 (Architecture validation), p. 2 (Data-limited post-training in simulated environments) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Architecture - extractive body cue:** Joint Policy Learning and World Modeling Objective
- **p. 1 / Architecture - extractive body cue:** We used FLARE loss coefficient 0.2 for both pretraining and posttraining.
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** As in the GR-1 language following experiment, we initialize the scene with one target object and one distractor object, with the target object having equal ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 1 (Architecture), p. 1 (Architecture).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | vision-language, embeddings, VLM, then, cross-attended, DiT, processes, state, noised, actions, find, adding, FLARE, improves | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | vision-language, embeddings, VLM, then, cross-attended, DiT, processes, state, noised, actions | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | introduce, GR00T, upgraded, version, foundation, model, humanoid, robots, Novel, Objects | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | Joint, Policy, Learning, World, Modeling, Objective, FLARE, loss, coefficient, pretraining | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Architecture - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.
- **p. 1 / Architecture - extractive body cue:** We find that adding FLARE both improves policy performance and unlocks the ability to learn from human videos.
- **p. 2 / Real GR-1 language following - extractive body cue:** Setting / GR00T N1 / GR00T N1.5 Language following rate / 46.6% / 93.3% Overall success rate / 43.3% / 83.0% We find that N1.5 ...
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** This allows learning to manipulate novel objects from human videos and minimal robot demonstrations.
- **p. 3 / Discussion - extractive body cue:** It achieves higher success rate, can use more diverse data sources, and has significantly improved language following capabilities.
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** As in the GR-1 language following experiment, we initialize the scene with one target object and one distractor object, with the target object having equal ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | We trained GR00T N1.5 for 250K steps on 1K H100 GPUs with global batch size 16384. | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | Rather than generatively modeling future frames, FLARE aligns the model with target future embeddings. | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not recovered | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / Architecture - extractive body cue:** We used FLARE loss coefficient 0.2 for both pretraining and posttraining.
- **p. 2 / Data-limited post-training in simulated environments - extractive body cue:** Following the GR00T N1 evaluation protocol, we evaluate N1.5's performance in data-limited post-training.
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** We observe that the post-trained GR00T N1.5 achieves much higher success rate than N1 for previously seen objects (toy fruits seen in the GR-1 pretraining ...
- **p. 1 / Architecture - extractive body cue:** We trained GR00T N1.5 for 250K steps on 1K H100 GPUs with global batch size 16384.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** FLARE, loss, coefficient, pretraining, posttraining, vision-language, embeddings, VLM, then, cross-attended, DiT, processes, state, noised, actions, find, architecture, achieves, significantly, higher.
- **Relevant PDF headings:** Model and Data Updates (p. 1); Architecture (p. 1); Architecture validation (p. 1).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | With several architecture, data and modeling improvements, we find that N1.5 outperforms N1 on both simulated manipulation benchmarks and on the real ... | p. 1 (Introduction), p. 3 (Post-training on Unitree G1) |
| Balance-aware whole-body execution | We expect users of N1.5 should observe better performance compared to N1, in particular improved generalization and better language following ability. | p. 1 (Introduction), p. 1 (Introduction) |
| Recovery / adaptation | It achieves higher success rate, can use more diverse data sources, and has significantly improved language following capabilities. | p. 3 (Discussion), p. 2 (Architecture validation) |

## Failure and Ablation Link

- **p. 1 / Architecture - extractive body cue:** We used FLARE loss coefficient 0.2 for both pretraining and posttraining.
- **p. 1 / Architecture - extractive body cue:** Our pretraining mixture included internal GR-1 data, OpenXE, simulated GR-1 (a.k.a.
- **p. 2 / Generalization to novel behaviors using Neural Trajectories - extractive body cue:** GR00T N1 showed only weak generalization to new verbs, only repeating the tasks contained in pretraining
- **p. 2 / Learning to manipulate novel objects from human ego videos - extractive body cue:** To evaluate the model's generalization ability, we evaluate pick and place performance using a set of 10 novel objects not seen during pretraining.
- **p. 3 / Post-training on Unitree G1 - extractive body cue:** We observe that the post-trained GR00T N1.5 achieves much higher success rate than N1 for previously seen objects (toy fruits seen in the GR-1 pretraining ...
- **p. 3 / Generalization to novel behaviors using Neural Trajectories - extractive body cue:** Although these new verbs can be considered "zero-shot" in the sense that we never collected teleoperation data for these tasks, we still train explicitly on ...
- **p. 1 / Architecture - extractive body cue:** The vision-language embeddings from the VLM are then cross-attended to by the DiT which processes the state and noised actions.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Architecture), p. 1 (Architecture), p. 2 (Architecture validation), p. 2 (Data-limited post-training in simulated environments), p. 3 (Post-training on Unitree G1), p. 3 (Post-training on Unitree G1), objective p. 1 (Architecture), p. 1 (Architecture), p. 3 (Post-training on Unitree G1), temporal p. 1 (Architecture), p. 1 (Architecture), p. 3 (Post-training on Unitree G1).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
