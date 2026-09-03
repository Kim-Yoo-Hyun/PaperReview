# Method - ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1. Introduction), p. 4 (3.2. Short-Horizon Force-to-Control Loop), p. 5 (3.2.2. Adaptive Routing and Decoding), p. 1 (Abstract), p. 2 (1. Introduction), p. 1 (Body text (section boundary not confidently recovered))): Our contributions are summarized as follows: • We introduce ForceVLA2, the first end-to-end hybrid force-position control framework with force awareness for VLAs, enhancing contact-rich manipulation by integrating force-prompt-driven VL ...

## Method Body Digest

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We introduce ForceVLA2, the first end-to-end hybrid force-position control framework with force awareness for VLAs, enhancing contact-rich manipulation ...
- **p. 4 / 3.2. Short-Horizon Force-to-Control Loop - extractive body cue:** (3) The encoded EE 6D pose and force tokens are concatenated to form a multi-modal state representation, Estate = [EP ; EF ], which is ...
- **p. 5 / 3.2.2. Adaptive Routing and Decoding - extractive body cue:** By conditioning the denoising process on the fused visual-language-force representation, the model achieves closed-loop, context-aware control that adapts fluidly to contact-rich interaction.
- **p. 1 / Abstract - extractive body cue:** We propose ForceVLA2, an end-to-end vision-language-action framework that equips robots with hybrid force-position control and explicit force awareness.
- **p. 2 / 1. Introduction - extractive body cue:** To overcome these limitations, we propose ForceVLA2, a novel framework that equips VLAs with active hybrid force-position control with force awareness to enhance contact-rich manipulation, ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Contact-rich manipulation requires force regulation, beyond visual and state observations (left).
- **p. 3 / 3. ForceVLA2 Framework - extractive body cue:** Building upon these principles, we propose the ForceVLA2 architecture, which integrates multi-scale perception, contextual reasoning, and force-aware manipulation into a unified VLA framework.
- **p. 3 / 3. ForceVLA2 Framework - extractive body cue:** In parallel, force observation bypasses high-level fusion and modulates the action expert via a direct gradient pathway, enabling a reactive response to observed force during ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We introduce ForceVLA2, the first end-to-end hybrid force-position control framework with force awareness for VLAs, enhancing contact-rich manipulation ...
- **p. 2 / 1. Introduction - extractive body cue:** To overcome these limitations, we propose ForceVLA2, a novel framework that equips VLAs with active hybrid force-position control with force awareness to enhance contact-rich manipulation, ...
- **p. 1 / Abstract - extractive body cue:** We propose ForceVLA2, an end-to-end vision-language-action framework that equips robots with hybrid force-position control and explicit force awareness.

## Source Evidence Cues

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We introduce ForceVLA2, the first end-to-end hybrid force-position control framework with force awareness for VLAs, enhancing contact-rich manipulation ...
- **p. 4 / 3.2. Short-Horizon Force-to-Control Loop - extractive body cue:** (3) The encoded EE 6D pose and force tokens are concatenated to form a multi-modal state representation, Estate = [EP ; EF ], which is ...
- **p. 5 / 3.2.2. Adaptive Routing and Decoding - extractive body cue:** By conditioning the denoising process on the fused visual-language-force representation, the model achieves closed-loop, context-aware control that adapts fluidly to contact-rich interaction.
- **p. 1 / Abstract - extractive body cue:** We propose ForceVLA2, an end-to-end vision-language-action framework that equips robots with hybrid force-position control and explicit force awareness.
- **p. 2 / 1. Introduction - extractive body cue:** To overcome these limitations, we propose ForceVLA2, a novel framework that equips VLAs with active hybrid force-position control with force awareness to enhance contact-rich manipulation, ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Contact-rich manipulation requires force regulation, beyond visual and state observations (left).
- **p. 3 / 3. ForceVLA2 Framework - extractive body cue:** Building upon these principles, we propose the ForceVLA2 architecture, which integrates multi-scale perception, contextual reasoning, and force-aware manipulation into a unified VLA framework.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multi-modal contact encoding | vision과 touch를 contact feature로 결합한다 | tactile image/force, vision, proprioception | tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행 | contact feature/state | Our contributions are summarized as follows: • We introduce ForceVLA2, the first end-to-end hybrid force-position control framework with force awareness for VLAs, ... | p. 2 (1. Introduction), p. 4 (3.2. Short-Horizon Force-to-Control Loop) |
| Contact / dynamics inference | contact mode와 object response를 추정한다 | contact feature와 action history | mode classifier, force/dynamics model 또는 state estimator를 update | contact/force prediction | (3) The encoded EE 6D pose and force tokens are concatenated to form a multi-modal state representation, Estate = [EP ; EF ... | p. 4 (3.2. Short-Horizon Force-to-Control Loop), p. 5 (3.2.2. Adaptive Routing and Decoding) |
| Force-aware action correction | interaction feedback으로 command를 보정한다 | predicted contact와 current wrench/touch | policy/control law가 action, force 또는 grasp를 재계산 | contact-safe action/torque | By conditioning the denoising process on the fused visual-language-force representation, the model achieves closed-loop, context-aware control that adapts fluidly to contact-rich interaction. | p. 5 (3.2.2. Adaptive Routing and Decoding), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3. ForceVLA2 Framework - extractive body cue:** In parallel, force observation bypasses high-level fusion and modulates the action expert via a direct gradient pathway, enabling a reactive response to observed force during ...
- **p. 4 / 3.2. Short-Horizon Force-to-Control Loop - extractive body cue:** This design preserves gradient fidelity for rapid force feedback, avoids over-reliance on past trajectories, and enables active exploration (Appendix A).
- **p. 5 / 3.2.2. Adaptive Routing and Decoding - extractive body cue:** We define the ground truth for the subtask transition probability as the joint event that these quantities satisfy their respective progress conditions.
- **p. 2 / 1. Introduction - extractive body cue:** It is further enhanced by adding force prompts and incorporating force into the action space, bridging the gap between embodied hybrid force-position interaction and force-aware ...
- **p. 3 / 3.1. Long-Horizon Force Awareness via Prompting - extractive body cue:** This mechanism enables ForceVLA2 to inherit VLM knowledge, assess subtask completion, transition across stages, and explicitly update force cues to guide force-aware manipulation.
- **p. 4 / 3.1. Long-Horizon Force Awareness via Prompting - extractive body cue:** The cross-scale MoE integrates these modalities to produce hybrid force-position actions and track sub-task progress for adaptive, contact-rich manipulation.
- **Formal bridge:** visual/tactile/proprioceptive contact history -> contact-aware action/force -> contact prediction/control error -> slip/contact success and safe interaction.
- **Equation/algorithm anchors:** p. 3 (3. ForceVLA2 Framework), p. 4 (3.2. Short-Horizon Force-to-Control Loop), p. 3 (3.1. Long-Horizon Force Awareness via Prompting).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | force/torque, sensor, attached, end-effector, recorded, interaction, forces, while, robot, joint, states, poses, logged, synchronously | tactile image/force, vision과 proprioceptive history | body cue; exact tensor/frame verify |
| State/latent | force/torque, sensor, attached, end-effector, recorded, interaction, forces, while, robot, joint | contact geometry, force state 또는 latent dynamics | body cue; notation verify |
| Action/output | contributions, summarized, follows, introduce, ForceVLA2, first, end-to-end, hybrid, force-position, control | grasp/contact action, force command 또는 object motion | body cue; unit/decoder verify |
| Objective/constraint | parallel, force, observation, bypasses, high-level, fusion, modulates, action, expert, direct | contact prediction/control error | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 4. ForceVLA2-Dataset - extractive body cue:** A 6D force/torque sensor attached to the end-effector recorded interaction forces at 300 Hz, while the robot joint states and end-effector (EE) 6D poses were ...
- **p. 4 / 3.1. Long-Horizon Force Awareness via Prompting - extractive body cue:** ForceVLA2 takes multi-view images, task and force prompts, and proprioceptive states (EE pose and force) as input.
- **p. 3 / 3. ForceVLA2 Framework - extractive body cue:** Inspired by findings in human sensorimotor control, we posit that force acts as a unifying signal across the perception-planning-execution hierarchy, providing essential feedback for dynamic ...
- **p. 3 / 3.1. Long-Horizon Force Awareness via Prompting - extractive body cue:** Current VLA models rely on pre-trained priors for task decomposition; however, purely vision-language inputs are insufficient in contact-rich settings that require human-like task awareness and ...
- **p. 4 / 3.2. Short-Horizon Force-to-Control Loop - extractive body cue:** ForceVLA2 encodes proprioceptive state and force differently within the action expert, passing them through the multi-modal encoder to fuse with visual-language embeddings for long-horizon reasoning, ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Contact-rich manipulation requires force regulation, beyond visual and state observations (left).
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** It builds force awareness into task planning through incoming force signals, and it outputs hybrid force-position actions with dynamic balance (right).
- **Normalized interface:** observation=tactile image/force, vision과 proprioceptive history; state=contact geometry, force state 또는 latent dynamics; output/action=grasp/contact action, force command 또는 object motion.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | contact episode 또는 action chunk horizon; contact event timing이 핵심이다. | At the beginning of each time step t, a noisy action sample a(0) t ∼N(0, I) is iteratively refined according to the ... | episode/sequence/action-chunk boundary |
| Rate / latency | tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요. | 2, we conduct a stepwise ablation in which we progressively add the Force Prompt (FP), Cross-Scale MoE (CM), and Multimodal Encoder (ME) ... | Hz/fps, inference time and control rate |
| Memory | recent tactile/force history와 visual state; recurrent memory 여부 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다. | The resulting dataset comprises 1000 trajectories and approximately 500K synchronized timesteps. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** contributions, summarized, follows, introduce, ForceVLA2, first, end-to-end, hybrid, force-position, control, framework, force, awareness, VLAs, enhancing, contact-rich, manipulation, integrating, force-prompt-driven, VLM.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multi-modal contact encoding | Our experimental benchmark consists of 5 contact-rich manipulation tasks within the proposed ForceVLA2-Dataset: Press the bottle, Clean the vase, Clean the board, ... | p. 6 (5.1. Experiment Setting), p. 5 (4. ForceVLA2-Dataset) |
| Contact / dynamics inference | 1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks. | p. 6 (5.2. Main Experiment Results), p. 8 (5.2. Main Experiment Results) |
| Force-aware action correction | 1, ForceVLA2 significantly outperforms all baselines, achieving a 66% average success rate across all tasks. | p. 6 (5.2. Main Experiment Results), p. 7 (5.2. Main Experiment Results) |

## Failure and Ablation Link

- **p. 8 / 5.3. Ablation Study - extractive body cue:** In particular, we conduct an ablation on the CrossScale MoE module by varying its modality inputs and outputs to verify the effectiveness of our design.
- **p. 8 / 5.3. Ablation Study - extractive body cue:** Component-wise ablations on FP, CM, and ME (Q2).
- **p. 6 / 5.2. Main Experiment Results - extractive body cue:** Compared with models without force inputs, ForceVLA2 and ForceVLA, which incorporate force feedback, show remarkable improvements 8916
- **p. 6 / 5. Experiments - extractive body cue:** The experiments address the following research questions: • Q1: How does ForceVLA2 perform in real-world contact-rich manipulation tasks, and what specific advantages and technical benefits ...
- **p. 8 / 6. Conclusion - extractive body cue:** The model also consistently reduces failures caused by arm overload and unstable contact, and ablation studies show monotonically improved performance as force prompts, the CrossScale ...
- **p. 8 / 5.2. Main Experiment Results - extractive body cue:** In contrast, other VLAs slowly chase the new EE 6D pose, leading to failure to maintain stable contact.
- **p. 7 / 5.2. Main Experiment Results - extractive body cue:** ForceVLA2 exhibits robust position and orientation following, and in object search tasks, it can still perform successful re-grasps even when visual observations fail. on force-sensitive ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1. Introduction), p. 4 (3.2. Short-Horizon Force-to-Control Loop), p. 5 (3.2.2. Adaptive Routing and Decoding), p. 1 (Abstract), p. 2 (1. Introduction), p. 1 (Body text (section boundary not confidently recovered)), objective p. 3 (3. ForceVLA2 Framework), p. 4 (3.2. Short-Horizon Force-to-Control Loop), p. 5 (3.2.2. Adaptive Routing and Decoding), p. 2 (1. Introduction), p. 3 (3.1. Long-Horizon Force Awareness via Prompting), p. 4 (3.1. Long-Horizon Force Awareness via Prompting), temporal p. 5 (3.2.2. Adaptive Routing and Decoding), p. 8 (5.3. Ablation Study), p. 5 (4. ForceVLA2-Dataset), p. 1 (Abstract), p. 1 (1. Introduction), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** ForceVLA2 encodes proprioceptive state and force differently within the action expert, passing them through the multi-modal encoder to fuse with visual-language embeddings for long-horizon reasoning, while transient force signals bypass ... (p. 4, 3.2. Short-Horizon Force-to-Control Loop).
- **Objective/update evidence:** This mechanism enables ForceVLA2 to inherit VLM knowledge, assess subtask completion, transition across stages, and explicitly update force cues to guide force-aware manipulation. (p. 3, 3.1. Long-Horizon Force Awareness via Prompting).
- **Temporal/runtime evidence:** 2, we conduct a stepwise ablation in which we progressively add the Force Prompt (FP), Cross-Scale MoE (CM), and Multimodal Encoder (ME) modules on top of π0, and measure the ... (p. 8, 5.3. Ablation Study).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
