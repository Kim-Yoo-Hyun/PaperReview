# Method - ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=2845H8Ua5D; PDF retrieval source: https://openreview.net/pdf/f2c61f8b6264a4b3e7b4a7a87c0a7f09e8cc9b48.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction)): To address these limitations, we introduce ForceVLA, a novel framework that augments VLA models with a force-aware Mixture-of-Experts (MoE) module, enabling effective reasoning and context-sensitive, force-informed action generation in ...

## Method Body Digest

- **p. 2 / 1 Introduction - extractive PDF cue:** To address these limitations, we introduce ForceVLA, a novel framework that augments VLA models with a force-aware Mixture-of-Experts (MoE) module, enabling effective reasoning and context-sensitive, ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Key to our approach is a force-aware Mixture-of-Experts-based fusion module, which enables dynamic processing and deep integration of force, visual, and language features during action ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Flow-based architectures such as π0 [10, 21] integrate pretrained vision-language encoders with fast action decoders to achieve high-frequency outputs.
- **p. 4 / 1 Introduction - extractive PDF cue:** Given a language instruction L, the objective is to learn an end-to-end policy π(At/Ot, L) that outputs low-level, executable action chunk At = {at, at+1, ...
- **p. 4 / 1 Introduction - extractive PDF cue:** The robot's observation at timestep t consists of base and hand visual inputs V b t and V h t , the proprioceptive state st ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Factory [43] introduces a powerful simulation toolkit for contact-rich interactions at scale, providing virtual assets and controllers for policy training in simulated environments.
- **p. 5 / 1 Introduction - extractive PDF cue:** Action Expert Perceive New Force 𝑓! 𝑓!"# Update Linear Self Attention LayerNorm Execute FVL feature FVLMoE Visual Tokens Language Tokens Force Tokens Figure 3: Overview ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Diffusion-based models [5, 27, 28, 29, 30] introduce stochastic generation for diverse, long-horizon behaviors, though they often incur high training and inference costs.

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** Key to our approach is a force-aware Mixture-of-Experts-based fusion module, which enables dynamic processing and deep integration of force, visual, and language features during action ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our main contributions are: • We present a novel framework that integrates force, vision, language, and action for improved precision and stability on contact-rich manipulation ...
- **p. 3 / 1 Introduction - extractive PDF cue:** In contrast, our ForceVLA-Data provides three unique contributions: (1) pre-processed data in the SOTA Lerobot format with conversion tools for plug-and-play compatibility, significantly reducing data-wrangling ...

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive PDF cue:** To address these limitations, we introduce ForceVLA, a novel framework that augments VLA models with a force-aware Mixture-of-Experts (MoE) module, enabling effective reasoning and context-sensitive, ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Key to our approach is a force-aware Mixture-of-Experts-based fusion module, which enables dynamic processing and deep integration of force, visual, and language features during action ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Flow-based architectures such as π0 [10, 21] integrate pretrained vision-language encoders with fast action decoders to achieve high-frequency outputs.
- **p. 4 / 1 Introduction - extractive PDF cue:** Given a language instruction L, the objective is to learn an end-to-end policy π(At/Ot, L) that outputs low-level, executable action chunk At = {at, at+1, ...
- **p. 4 / 1 Introduction - extractive PDF cue:** The robot's observation at timestep t consists of base and hand visual inputs V b t and V h t , the proprioceptive state st ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Factory [43] introduces a powerful simulation toolkit for contact-rich interactions at scale, providing virtual assets and controllers for policy training in simulated environments.
- **p. 5 / 1 Introduction - extractive PDF cue:** Action Expert Perceive New Force 𝑓! 𝑓!"# Update Linear Self Attention LayerNorm Execute FVL feature FVLMoE Visual Tokens Language Tokens Force Tokens Figure 3: Overview ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multi-modal contact encoding | vision과 touch를 contact feature로 결합한다 | tactile image/force, vision, proprioception | tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행 | contact feature/state | To address these limitations, we introduce ForceVLA, a novel framework that augments VLA models with a force-aware Mixture-of-Experts (MoE) module, enabling effective ... | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Contact / dynamics inference | contact mode와 object response를 추정한다 | contact feature와 action history | mode classifier, force/dynamics model 또는 state estimator를 update | contact/force prediction | Key to our approach is a force-aware Mixture-of-Experts-based fusion module, which enables dynamic processing and deep integration of force, visual, and language ... | p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Force-aware action correction | interaction feedback으로 command를 보정한다 | predicted contact와 current wrench/touch | policy/control law가 action, force 또는 grasp를 재계산 | contact-safe action/torque | Flow-based architectures such as π0 [10, 21] integrate pretrained vision-language encoders with fast action decoders to achieve high-frequency outputs. | p. 3 (1 Introduction), p. 4 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 1 Introduction - extractive PDF cue:** Given a language instruction L, the objective is to learn an end-to-end policy π(At/Ot, L) that outputs low-level, executable action chunk At = {at, at+1, ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Diffusion-based models [5, 27, 28, 29, 30] introduce stochastic generation for diverse, long-horizon behaviors, though they often incur high training and inference costs.
- **p. 6 / 1 Introduction - extractive PDF cue:** For each task, operators were instructed to complete the objective while ensuring diverse and successful interaction patterns.
- **p. 1 / 1 Introduction - extractive PDF cue:** Building on this progress, OpenVLA [9] introduced Vision-Language-Action (VLA) models to bridge perception and control for real-world robotic manipulation.
- **p. 5 / 1 Introduction - extractive PDF cue:** Action Expert Perceive New Force 𝑓! 𝑓!"# Update Linear Self Attention LayerNorm Execute FVL feature FVLMoE Visual Tokens Language Tokens Force Tokens Figure 3: Overview ...
- **Formal bridge:** visual/tactile/proprioceptive contact history -> contact-aware action/force -> contact prediction/control error -> slip/contact success and safe interaction.
- **Equation/algorithm anchors:** p. 4 (1 Introduction), p. 6 (1 Introduction), p. 5 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, language, instruction, objective, learn, end-to-end, policy, At/Ot, outputs, low-level, executable, action, chunk, H-1 | tactile image/force, vision과 proprioceptive history | body cue; exact tensor/frame verify |
| State/latent | Given, language, instruction, objective, learn, end-to-end, policy, At/Ot, outputs, low-level | contact geometry, force state 또는 latent dynamics | body cue; notation verify |
| Action/output | Key, force-aware, Mixture-of-Experts-based, fusion, module, enables, dynamic, processing, deep, integration | grasp/contact action, force command 또는 object motion | body cue; unit/decoder verify |
| Objective/constraint | Given, language, instruction, objective, learn, end-to-end, policy, At/Ot, outputs, low-level | contact prediction/control error | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 1 Introduction - extractive PDF cue:** Given a language instruction L, the objective is to learn an end-to-end policy π(At/Ot, L) that outputs low-level, executable action chunk At = {at, at+1, ...
- **p. 4 / 1 Introduction - extractive PDF cue:** The robot's observation at timestep t consists of base and hand visual inputs V b t and V h t , the proprioceptive state st ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Other works incorporate reasoning mechanisms [22, 23, 24, 25], action space compression, or 3D point cloud inputs [26] to improve instruction grounding and task execution.
- **p. 2 / 1 Introduction - extractive PDF cue:** By adaptively activating these experts based on high-level task instructions and low-level interaction feedback, ForceVLA captures subtle yet critical, phase-dependent variations during physical interaction and ...
- **p. 1 / Abstract - extractive PDF cue:** ForceVLA introduces FVLMoE, a force-aware Mixture-of-Experts fusion module that dynamically integrates pretrained visual-language embeddings with real-time 6-axis force feedback during action decoding.
- **p. 2 / 1 Introduction - extractive PDF cue:** Without force feedback, the policy fails to correct pose errors and completes insertion incorrectly.
- **p. 5 / 1 Introduction - extractive PDF cue:** The VL features, denoted as EV L ∈RNV L×Dmodel, are outputs from the primary Vision-Language Model, encapsulating contextual understanding derived from processed image streams and ...
- **Normalized interface:** observation=tactile image/force, vision과 proprioceptive history; state=contact geometry, force state 또는 latent dynamics; output/action=grasp/contact action, force command 또는 object motion.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | contact episode 또는 action chunk horizon; contact event timing이 핵심이다. | TCP position is represented by Cartesian coordinates (x, y, z) and orientation is represented by Euler angles (α, β, γ). ft is ... | episode/sequence/action-chunk boundary |
| Rate / latency | tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요. | However, this stuttering limits its inference speed and reactiveness to real-time force changes, making it less competitive for general contact-rich manipulation tasks ... | Hz/fps, inference time and control rate |
| Memory | recent tactile/force history와 visual state; recurrent memory 여부 확인 필요. | not recovered | window and reset |
| Compute | sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다. | The resulting dataset, which we term ForceVLA-Data, comprises a total of 244 trajectories, amounting to 140 thousand synchronized timesteps. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 1 Introduction - extractive PDF cue:** Flow-based architectures such as π0 [10, 21] integrate pretrained vision-language encoders with fast action decoders to achieve high-frequency outputs.
- **p. 3 / 1 Introduction - extractive PDF cue:** Factory [43] introduces a powerful simulation toolkit for contact-rich interactions at scale, providing virtual assets and controllers for policy training in simulated environments.
- **p. 1 / 1 Introduction - extractive PDF cue:** By leveraging VLM-based encoders, these models demonstrate strong performance in semantic grounding, language following, and zeroshot generalization. π0 [10] further enhances this framework using stronger ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Flow-based architectures such as π0 [10, 21] integrate pretrained vision-language encoders with fast action decoders to achieve high-frequency outputs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** address, limitations, introduce, ForceVLA, novel, framework, augments, VLA, models, force-aware, Mixture-of-Experts, MoE, module, enabling, effective, reasoning, context-sensitive, force-informed, action, generation.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multi-modal contact encoding | The evaluation is structured around four core research questions: (1) the overall effectiveness of ForceVLA compared to baselines that incorporate force without ... | p. 6 (5 Experiments), p. 6 (5 Experiments) |
| Contact / dynamics inference | The evaluation is structured around four core research questions: (1) the overall effectiveness of ForceVLA compared to baselines that incorporate force without ... | p. 6 (5 Experiments), p. 7 (5 Experiments) |
| Force-aware action correction | Figure 5: Main task success rates across different methods. ForceVLA significantly outperforms all baselines on five contact-rich tasks. Incorporating external force feedback ... | p. 7 (Figure/Table caption), p. 7 (5 Experiments) |

## Failure and Ablation Link

- **p. 7 / 5 Experiments - extractive PDF cue:** The specific variants include π0-base[10] w/o F (standard π0 without force input), π0-base[10] w/ F (π0 with force signals directly concatenated to state inputs), and ...
- **p. 6 / 5 Experiments - extractive PDF cue:** The evaluation is structured around four core research questions: (1) the overall effectiveness of ForceVLA compared to baselines that incorporate force without our specialized fusion ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 6: Variants of generalization settings used in our experiments. (a-b) Different object geome- tries; (c) variation in socket height; (d) partial visual occlusion; (e) ...
- **p. 25 / Figure/Table caption - extractive PDF cue:** Table 6: Success rates comparison between ForceVLA and ForceVLA without force inputs. The drop column indicates the absolute percentage decrease in success rate when force ...
- **p. 7 / 5 Experiments - extractive PDF cue:** Compared to the standard π0-base model without force feedback (π0-base w/ F), which achieved an average of 37.3%, ForceVLA shows an improvement of 23.2%.
- **p. 8 / 5 Experiments - extractive PDF cue:** For our foundational baseline, we evaluated π0-base and π0-fast variants.
- **p. 8 / 5 Experiments - extractive PDF cue:** We attribute this sensitivity to its highly optimized and compact token space, which is likely disrupted by naively projected force tokens lacking corresponding large-scale pre-training.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction), objective p. 4 (1 Introduction), p. 3 (1 Introduction), p. 6 (1 Introduction), p. 1 (1 Introduction), p. 5 (1 Introduction), temporal p. 4 (1 Introduction), p. 8 (5 Experiments), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 6 (1 Introduction), p. 6 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
