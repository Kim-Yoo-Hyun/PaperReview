# Method - Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=8xTDnj39Ti; PDF retrieval source: https://openreview.net/pdf/3656f9adb0d775aac722a69bef2d7db1e2db0ce2.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (2 METHOD), p. 5 (2 METHOD), p. 4 (2 METHOD), p. 4 (2 METHOD), p. 6 (2 METHOD), p. 18 (A.1 TRAINING DETAILS)): In the first training phase, we fine-tune InternVL3 using auto-regressive language modeling loss.

## Method Body Digest

- **p. 5 / 2 METHOD - extractive PDF cue:** In the first training phase, we fine-tune InternVL3 using auto-regressive language modeling loss.
- **p. 5 / 2 METHOD - extractive PDF cue:** Ii t, lt and qt are encoded via corresponding encoders and then projected via a linear projection layer into the same embedding space. θ represents ...
- **p. 4 / 2 METHOD - extractive PDF cue:** Published as a conference paper at ICLR 2026 2.1 MODEL STRUCTURE The structure of Vlaser consists of two major components: the typical vision-language backbone (Chen ...
- **p. 4 / 2 METHOD - extractive PDF cue:** During inference, we denoise the actions based on the image observation, language instruction, as well as the current robot state.
- **p. 6 / 2 METHOD - extractive PDF cue:** Therefore, the VLA optimization loss is as follows, Lvla = Ep(At/ot) ∥vθ(Aτ t , ot) -u(Aτ t /At)∥2 (2) Formally, following prior flow-matching based VLA ...
- **p. 18 / A.1 TRAINING DETAILS - extractive PDF cue:** Configurations Values LLM sequence length 16, 384 Dynamic Resolution True Patch Size 448 Max Patch num 12 Freeze vision tower False Freeze multimodal projector False ...
- **p. 3 / 2 METHOD - extractive PDF cue:** Section 2.3 discusses the training recipe that includes embodied reasoning pretraining and vision-language-action finetuning.
- **p. 5 / 2 METHOD - extractive PDF cue:** In particular, given the input images x ∈Rt×h×w×3 and textual prompt y ∈Rl, the language modeling loss Llm can be defined by Llm = -log ...

## Design Rationale

- **p. 4 / 2 METHOD - extractive PDF cue:** Here we present the overall data scale and sources for each reasoning modality, while more details about the construction methodologies are provided in Appendix A.2.
- **p. 4 / 2 METHOD - extractive PDF cue:** Published as a conference paper at ICLR 2026 2.1 MODEL STRUCTURE The structure of Vlaser consists of two major components: the typical vision-language backbone (Chen ...
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** In this paper, we aim to construct Vlaser, an embodied vision-language model that possesses strong ∗Equal contribution. †Corresponding authors.

## Source Evidence Cues

- **p. 5 / 2 METHOD - extractive PDF cue:** In the first training phase, we fine-tune InternVL3 using auto-regressive language modeling loss.
- **p. 5 / 2 METHOD - extractive PDF cue:** Ii t, lt and qt are encoded via corresponding encoders and then projected via a linear projection layer into the same embedding space. θ represents ...
- **p. 4 / 2 METHOD - extractive PDF cue:** Published as a conference paper at ICLR 2026 2.1 MODEL STRUCTURE The structure of Vlaser consists of two major components: the typical vision-language backbone (Chen ...
- **p. 4 / 2 METHOD - extractive PDF cue:** During inference, we denoise the actions based on the image observation, language instruction, as well as the current robot state.
- **p. 6 / 2 METHOD - extractive PDF cue:** Therefore, the VLA optimization loss is as follows, Lvla = Ep(At/ot) ∥vθ(Aτ t , ot) -u(Aτ t /At)∥2 (2) Formally, following prior flow-matching based VLA ...
- **p. 18 / A.1 TRAINING DETAILS - extractive PDF cue:** Configurations Values LLM sequence length 16, 384 Dynamic Resolution True Patch Size 448 Max Patch num 12 Freeze vision tower False Freeze multimodal projector False ...
- **p. 3 / 2 METHOD - extractive PDF cue:** Section 2.3 discusses the training recipe that includes embodied reasoning pretraining and vision-language-action finetuning.
- **Detected method headings:** 2 METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | In the first training phase, we fine-tune InternVL3 using auto-regressive language modeling loss. | p. 5 (2 METHOD), p. 5 (2 METHOD) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Ii t, lt and qt are encoded via corresponding encoders and then projected via a linear projection layer into the same embedding ... | p. 5 (2 METHOD), p. 4 (2 METHOD) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Published as a conference paper at ICLR 2026 2.1 MODEL STRUCTURE The structure of Vlaser consists of two major components: the typical ... | p. 4 (2 METHOD), p. 4 (2 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 2 METHOD - extractive PDF cue:** In particular, given the input images x ∈Rt×h×w×3 and textual prompt y ∈Rl, the language modeling loss Llm can be defined by Llm = -log ...
- **p. 4 / 2 METHOD - extractive PDF cue:** While InternVL3 excels in multimodal and linguistic tasks across various model sizes, Vlaser focuses on two sizes-2B and 8B-optimized for the computational constraints of robots.
- **p. 6 / 2 METHOD - extractive PDF cue:** Therefore, the VLA optimization loss is as follows, Lvla = Ep(At/ot) ∥vθ(Aτ t , ot) -u(Aτ t /At)∥2 (2) Formally, following prior flow-matching based VLA ...
- **p. 18 / A.1 TRAINING DETAILS - extractive PDF cue:** Configurations Values LLM sequence length 16, 384 Dynamic Resolution True Patch Size 448 Max Patch num 12 Freeze vision tower False Freeze multimodal projector False ...
- **p. 5 / 2 METHOD - extractive PDF cue:** In the first training phase, we fine-tune InternVL3 using auto-regressive language modeling loss.
- **p. 18 / A.1 TRAINING DETAILS - extractive PDF cue:** To maximize adaptation to embodied reasoning tasks, we keep all parameters trainable, including those in the large language model, the vision-language projector, and the visual ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 18 (A.1 TRAINING DETAILS), p. 4 (2 METHOD), p. 5 (2 METHOD), p. 5 (2 METHOD), p. 6 (2 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | During, inference, denoise, actions, image, observation, language, instruction, well, current, robot, state, action, expert | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | During, inference, denoise, actions, image, observation, language, instruction, well, current | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Here, present, overall, data, scale, sources, reasoning, modality, while, more | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | particular, given, input, images, textual, prompt, language, modeling, loss, Llm | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 2 METHOD - extractive PDF cue:** During inference, we denoise the actions based on the image observation, language instruction, as well as the current robot state.
- **p. 5 / 2 METHOD - extractive PDF cue:** The action expert is analogous to a mixture of experts(MoE) (Shazeer et al., 2017b; Du et al., 2022; Zhou et al., 2024) architecture with two ...
- **p. 5 / 2 METHOD - extractive PDF cue:** Specifically, we denote the action chunk At = [at, at+1, . . . , at+H-1], where at represents the action in the current timestep t ...
- **p. 4 / 2 METHOD - extractive PDF cue:** Specifically, we encode the robot state as a state token and noised actions as action tokens, and input them into the action expert.
- **p. 18 / A.1 TRAINING DETAILS - extractive PDF cue:** Configurations Values LLM sequence length 16, 384 Dynamic Resolution True Patch Size 448 Max Patch num 12 Freeze vision tower False Freeze multimodal projector False ...
- **p. 3 / 2 METHOD - extractive PDF cue:** Section 2.3 discusses the training recipe that includes embodied reasoning pretraining and vision-language-action finetuning.
- **p. 1 / 1 INTRODUCTION - extractive PDF cue:** Meanwhile, a significant body of work extends vision-language models (VLMs) into vision-language-action models (VLAs) (Kim et al., 2024; Intelligence et al., 2025; Driess et al., ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Specifically, we denote the action chunk At = [at, at+1, . . . , at+H-1], where at represents the action in the ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Therefore, the VLA optimization loss is as follows, Lvla = Ep(At/ot) ∥vθ(Aτ t , ot) -u(Aτ t /At)∥2 (2) Formally, following prior ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | Configurations Values LLM sequence length 384 Image Size 448 Freeze VLM False Global batch size 1024 Training epochs 10 VLM Peak Learning ... | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 2 METHOD - extractive PDF cue:** In the first training phase, we fine-tune InternVL3 using auto-regressive language modeling loss.
- **p. 4 / 2 METHOD - extractive PDF cue:** During inference, we denoise the actions based on the image observation, language instruction, as well as the current robot state.
- **p. 18 / A.1 TRAINING DETAILS - extractive PDF cue:** Configurations Values LLM sequence length 16, 384 Dynamic Resolution True Patch Size 448 Max Patch num 12 Freeze vision tower False Freeze multimodal projector False ...
- **p. 3 / 2 METHOD - extractive PDF cue:** Section 2.3 discusses the training recipe that includes embodied reasoning pretraining and vision-language-action finetuning.
- **p. 18 / A.1 TRAINING DETAILS - extractive PDF cue:** Configurations Values LLM sequence length 16, 384 Dynamic Resolution True Patch Size 448 Max Patch num 12 Freeze vision tower False Freeze multimodal projector False ...
- **p. 9 / 3 EXPERIMENTS - extractive PDF cue:** 3.3 ABLATION STUDIES In this section, we adopt ablation studies regarding three key hyperparameters for VLA end-to-end training, i.e.,, the predicted action length P, the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, training, phase, fine-tune, InternVL3, auto-regressive, language, modeling, loss, encoded, corresponding, encoders, then, projected, linear, projection, layer, same, embedding, space.
- **Relevant PDF headings:** 2 METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | SimplerENV is an open-source suite of purpose-built simulated environments with nearly 150K episodes for evaluating real-world robot manipulation policies in a scalable, ... | p. 8 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS) |
| Action / skill decoding | When compared against current state-of-the-art embodied-specific VLMs, including RoboBrain2.0 (Team et al., 2025a) and Embodied-R1 (Yuan et al., 2025), our method, Vlaser ... | p. 7 (3 EXPERIMENTS), p. 8 (3 EXPERIMENTS) |
| Receding execution / feedback | This suggests that pretraining with diverse in-domain multimodal data, spanning general QA, grounding, and spatial intelligence, could best facilitates transfer learning for ... | p. 9 (3 EXPERIMENTS), p. 7 (3 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 8 / 3 EXPERIMENTS - extractive PDF cue:** 3.1, without any in-domain data in Vlaser-6M dataset.
- **p. 8 / 3 EXPERIMENTS - extractive PDF cue:** Across Google Robot and WidowX/BridgeData V2 setups, SimplerEnv reports strong real-vs-sim correlations and faithfully reflects behavior under distribution shifts, enabling fast, comparable policy assessment without ...
- **p. 9 / 3 EXPERIMENTS - extractive PDF cue:** 3.3 ABLATION STUDIES In this section, we adopt ablation studies regarding three key hyperparameters for VLA end-to-end training, i.e.,, the predicted action length P, the ...
- **p. 9 / 3 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2026 Table 5: Ablation Studies on WidowX Robot Tasks Model Predict Length Execute Length Sample Steps Carrot on ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: An illustration of Vlaser architecture. Vlaser includes two components and corresponding training phases: 1) the Multimodal Pretraining is for embodied reasoning enhancement based ...
- **p. 7 / 3 EXPERIMENTS - extractive PDF cue:** In the following section, we further examine how these enhanced reasoning capabilities, embedded within VLMs, translate into improved performance when fine-tuned for downstream Vision-Language Action ...
- **p. 22 / A.3 SIMULATION EVALUATION DETAILS - extractive PDF cue:** We fine-tune and evaluate the VLA models using various base models within the SimplerEnv simulation environment.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (2 METHOD), p. 5 (2 METHOD), p. 4 (2 METHOD), p. 4 (2 METHOD), p. 6 (2 METHOD), p. 18 (A.1 TRAINING DETAILS), objective p. 5 (2 METHOD), p. 4 (2 METHOD), p. 6 (2 METHOD), p. 18 (A.1 TRAINING DETAILS), p. 5 (2 METHOD), p. 18 (A.1 TRAINING DETAILS), temporal p. 5 (2 METHOD), p. 6 (2 METHOD), p. 5 (2 METHOD), p. 19 (A.2 DATA GENERATION DETAILS), p. 2 (3. Paint the canvas), p. 6 (2 METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
