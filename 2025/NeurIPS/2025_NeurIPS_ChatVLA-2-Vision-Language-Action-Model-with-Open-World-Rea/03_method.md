# Method - ChatVLA-2: Vision-Language-Action Model with Open-World Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=1lyKflUOhp; PDF retrieval source: https://openreview.net/pdf/c88d737915ea445cb600d21cb0c7125912b7053b.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3 Methodology), p. 6 (3 Methodology), p. 5 (3 Methodology), p. 6 (3 Methodology), p. 7 (3 Methodology), p. 22 (B.2 Data details)): We introduce an enhanced reasoning-following module designed to improve reasoning capabilities in action models.

## Method Body Digest

- **p. 5 / 3 Methodology - extractive PDF cue:** We introduce an enhanced reasoning-following module designed to improve reasoning capabilities in action models.
- **p. 6 / 3 Methodology - extractive PDF cue:** 3.3 Training Strategy Our previous section introduced the neural architecture of ChatVLA-2, which primarily focuses on enabling the VLA model to more effectively extract common ...
- **p. 5 / 3 Methodology - extractive PDF cue:** This reasoning representation is then combined with the current timestep embeddings and used to condition the generation of scale and shift parameters, effectively injecting reasoning ...
- **p. 6 / 3 Methodology - extractive PDF cue:** The model undergoes training for 50k steps, beginning with an initial learning rate of 2e-5 and a warm-up phase for the first 3k steps.
- **p. 7 / 3 Methodology - extractive PDF cue:** Our experiments demonstrate that the proposed method successfully completes tasks involving previously unseen spatial instructions and novel objects. also significantly by the reasoning outputs generated ...
- **p. 22 / B.2 Data details - extractive PDF cue:** We initialize these reasoning annotations with fixed templates and then augment them using GPT-4o, following a pipeline analogous to the one employed in training large ...
- **p. 4 / 3 Methodology - extractive PDF cue:** We adopt DexVLA [2] as our foundational model architecture.
- **p. 22 / B.1 Training details - extractive PDF cue:** The total training cost is 340 GPU hours.

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** To achieve this, we propose a novel VLA model architecture employing a dynamic mixture-ofexperts within the VLM backbone.
- **p. 3 / 1 Introduction - extractive PDF cue:** Additionally, we introduce a straightforward reasoning-enhancement module designed to align the action expert's output more closely with the model's internal reasoning process.
- **p. 5 / 3 Methodology - extractive PDF cue:** We introduce an enhanced reasoning-following module designed to improve reasoning capabilities in action models.

## Source Evidence Cues

- **p. 5 / 3 Methodology - extractive PDF cue:** We introduce an enhanced reasoning-following module designed to improve reasoning capabilities in action models.
- **p. 6 / 3 Methodology - extractive PDF cue:** 3.3 Training Strategy Our previous section introduced the neural architecture of ChatVLA-2, which primarily focuses on enabling the VLA model to more effectively extract common ...
- **p. 5 / 3 Methodology - extractive PDF cue:** This reasoning representation is then combined with the current timestep embeddings and used to condition the generation of scale and shift parameters, effectively injecting reasoning ...
- **p. 6 / 3 Methodology - extractive PDF cue:** The model undergoes training for 50k steps, beginning with an initial learning rate of 2e-5 and a warm-up phase for the first 3k steps.
- **p. 7 / 3 Methodology - extractive PDF cue:** Our experiments demonstrate that the proposed method successfully completes tasks involving previously unseen spatial instructions and novel objects. also significantly by the reasoning outputs generated ...
- **p. 22 / B.2 Data details - extractive PDF cue:** We initialize these reasoning annotations with fixed templates and then augment them using GPT-4o, following a pipeline analogous to the one employed in training large ...
- **p. 4 / 3 Methodology - extractive PDF cue:** We adopt DexVLA [2] as our foundational model architecture.
- **Detected method headings:** 3 Methodology (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | We introduce an enhanced reasoning-following module designed to improve reasoning capabilities in action models. | p. 5 (3 Methodology), p. 6 (3 Methodology) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | 3.3 Training Strategy Our previous section introduced the neural architecture of ChatVLA-2, which primarily focuses on enabling the VLA model to more ... | p. 6 (3 Methodology), p. 5 (3 Methodology) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | This reasoning representation is then combined with the current timestep embeddings and used to condition the generation of scale and shift parameters, ... | p. 5 (3 Methodology), p. 6 (3 Methodology) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 22 / B.1 Training details - extractive PDF cue:** The total training cost is 340 GPU hours.
- **p. 4 / 3 Methodology - extractive PDF cue:** Benefiting from large-scale multi-modal pre-training, VLAs demonstrate significant advantages in bimanual manipulation [1, 2], long-horizon task planning [1, 61], and mobile manipulation [3].
- **p. 22 / B.1 Training details - extractive PDF cue:** We adopt mixed-precision training (FP16) and use the AdamW optimizer.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Consequently, robot, actions, guided, just, initial, language, instructions, image, observations, experiments, demonstrate, successfully, completes | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Consequently, robot, actions, guided, just, initial, language, instructions, image, observations | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | achieve, novel, VLA, model, architecture, employing, dynamic, mixture-ofexperts, within, VLM | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | total, training, cost, GPU, hours, Benefiting, large-scale, multi-modal, pre-training, VLAs | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 3 Methodology - extractive PDF cue:** Consequently, the robot's actions are guided not just by the initial language instructions and image observations but 6
- **p. 7 / 3 Methodology - extractive PDF cue:** Our experiments demonstrate that the proposed method successfully completes tasks involving previously unseen spatial instructions and novel objects. also significantly by the reasoning outputs generated ...
- **p. 5 / 3 Methodology - extractive PDF cue:** outputs: reasoning tokens and action tokens.
- **p. 5 / 3 Methodology - extractive PDF cue:** A distinctive feature of our method is that the model not only follows given instructions but also aligns robotic actions closely with the generated reasoning.
- **p. 6 / 3 Methodology - extractive PDF cue:** In the second stage, we freeze the entire VLM and train only the action expert, thereby preserving open-world reasoning while enhancing instruction-following abilities in VLA.
- **p. 4 / 3 Methodology - extractive PDF cue:** The image encoders project the robot's visual observations into the same embedding space as the language tokens.
- **p. 3 / 1 Introduction - extractive PDF cue:** Therefore, this task required the model to accurately interpret the visual scene, reason about novel spatial instructions, and execute appropriate actions.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | This reasoning representation is then combined with the current timestep embeddings and used to condition the generation of scale and shift parameters, ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Data collection is performed using teleoperation equipment at a frequency of 15 Hz. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Data collection is performed using teleoperation equipment at a frequency of 15 Hz. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3 Methodology - extractive PDF cue:** 3.3 Training Strategy Our previous section introduced the neural architecture of ChatVLA-2, which primarily focuses on enabling the VLA model to more effectively extract common ...
- **p. 6 / 3 Methodology - extractive PDF cue:** The model undergoes training for 50k steps, beginning with an initial learning rate of 2e-5 and a warm-up phase for the first 3k steps.
- **p. 22 / B.2 Data details - extractive PDF cue:** We initialize these reasoning annotations with fixed templates and then augment them using GPT-4o, following a pipeline analogous to the one employed in training large ...
- **p. 22 / B.1 Training details - extractive PDF cue:** The model is trained for 50k steps, starting with a learning rate of 2e-5 and a warm-up phase over the first 3k steps.
- **p. 22 / B.1 Training details - extractive PDF cue:** For training stage 1, we co-train on image-text data and robot data, setting the initial learning rate to 2e-5 and training for 15k steps.
- **p. 9 / 4 Experiments - extractive PDF cue:** When Stage 2 was excluded, the model's robotic control performance in open-world scenarios dropped to 23% under the same number of training steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** introduce, enhanced, reasoning-following, module, designed, improve, reasoning, capabilities, action, models, Training, Strategy, previous, section, introduced, neural, architecture, ChatVLA-2, primarily, focuses.
- **Relevant PDF headings:** 3 Methodology (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | 4.4 Results on Multimodal Understanding and Visual-Question Answering We have conducted extensive evaluations across 12 diverse multi-modal understanding benchmarks, covering tasks such ... | p. 9 (4 Experiments), p. 22 (B.2 Data details) |
| Action / skill decoding | Consequently, none of the compared methods successfully completed any manipulation tasks in open-world conditions. | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Receding execution / feedback | In contrast, our method achieved an average success rate of 81.4%, representing a 3.52-times improvement over DexVLA. | p. 8 (4 Experiments), p. 8 (4 Experiments) |

## Failure and Ablation Link

- **p. 8 / 4 Experiments - extractive PDF cue:** 4.3 Ablation Study How important is mixture-of-expert in VLA?
- **p. 9 / 4 Experiments - extractive PDF cue:** Ablation study on two-stage training.
- **p. 9 / 4 Experiments - extractive PDF cue:** Dynamic MoE 3.58 1.73 43/52 Static MoE + Dynamic MoE 2.38/4 0.92/2 11/52 Shared MoE + Dynamic MoE 3.07/4 1.12/2 25/52 3B Dense Model 0.04 ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Model architecture. Left: A reasoning-following enhancement module is incorporated to ensure that the VLA model adheres to logical reasoning when performing actions. Right: ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3: Training Strategy. We leverage a two-stage training strategy. In the first stage, we perform co-training on image-text data and robot data to empower ...
- **p. 22 / Figure/Table caption - extractive PDF cue:** Table 7: Ablation study on reasoning-following enhancement module.
- **p. 22 / Figure/Table caption - extractive PDF cue:** Table 6: Ablation study on number of experts. Expert numbers Top-k numbers OCR Math 8 2 3.58

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3 Methodology), p. 6 (3 Methodology), p. 5 (3 Methodology), p. 6 (3 Methodology), p. 7 (3 Methodology), p. 22 (B.2 Data details), objective p. 22 (B.1 Training details), p. 4 (3 Methodology), p. 22 (B.1 Training details), temporal p. 5 (3 Methodology), p. 8 (4 Experiments), p. 4 (3 Methodology), p. 6 (3 Methodology), p. 7 (3 Methodology), p. 9 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
