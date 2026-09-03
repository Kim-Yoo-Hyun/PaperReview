# Method - Sim2Real VLA: Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=H4SyKHjd4c; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247063. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 17 (A.2 CONFIGURING REWARDS IN VLA MODELS)): Utilizing a tokenize-thenconcatenate strategy, the model fuses these action embeddings with the predicted affordance outputs.

## Method Body Digest

- **p. 16 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** Utilizing a tokenize-thenconcatenate strategy, the model fuses these action embeddings with the predicted affordance outputs.
- **p. 16 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** This architecture is complemented by two additional transformer blocks of identical configuration dedicated to affordance inference and guidance, alongside multiple MLP adapters that facilitate dimensional ...
- **p. 17 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** Constructed as a regressive transformer classifier, the validtion modeal takes maksed visual observation and state as input, current target affordance as condation, and output a ...
- **p. 17 / A.2 CONFIGURING REWARDS IN VLA MODELS - extractive body cue:** These functions are crucial for reinforcement learning (RL), particularly following Supervised Fine-Tuning (SFT) of VLA models.
- **p. 17 / A.2 CONFIGURING REWARDS IN VLA MODELS - extractive body cue:** When more detailed or nuanced reward structures are needed, AI agents can design sophisticated reward functions (Ma et al., 2024a).
- **p. 17 / A.2 CONFIGURING REWARDS IN VLA MODELS - extractive body cue:** In such cases, the reward function can be interpreted as R(s, a) = 1 if the robot successfully completes the task, and R(s, a) = ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Within the robot's operational environment, our objective is to learn a control policy π(at, . . . , at+M / ot-H, . . . , ...
- **p. 16 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** The pipeline initiates by employing a diffusion-based action expert to generate action trajectories through denoising, conditioned on the aforementioned masked visual observations and proprioceptive inputs.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** These findings call for an alternative approach: instead of focusing on generating high-fidelity data, we propose addressing the Sim2Real by redesigning the VLA architecture.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this study, we introduce Sim2Real-VLA, which, despite being trained solely on synthetic data, demonstrates generalizable and sustained manipulation performance across diverse real-world environments.
- **p. 6 / 1 INTRODUCTION - extractive body cue:** We present more details in Appendix A.4.

## Source Evidence Cues

- **p. 16 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** Utilizing a tokenize-thenconcatenate strategy, the model fuses these action embeddings with the predicted affordance outputs.
- **p. 16 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** This architecture is complemented by two additional transformer blocks of identical configuration dedicated to affordance inference and guidance, alongside multiple MLP adapters that facilitate dimensional ...
- **p. 17 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** Constructed as a regressive transformer classifier, the validtion modeal takes maksed visual observation and state as input, current target affordance as condation, and output a ...
- **p. 17 / A.2 CONFIGURING REWARDS IN VLA MODELS - extractive body cue:** These functions are crucial for reinforcement learning (RL), particularly following Supervised Fine-Tuning (SFT) of VLA models.
- **Detected method headings:** A.1 MODEL ARCHITECTURE & KEY PARAMETERS (p. 16); A.2 CONFIGURING REWARDS IN VLA MODELS (p. 17)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Utilizing a tokenize-thenconcatenate strategy, the model fuses these action embeddings with the predicted affordance outputs. | p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | This architecture is complemented by two additional transformer blocks of identical configuration dedicated to affordance inference and guidance, alongside multiple MLP adapters ... | p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Constructed as a regressive transformer classifier, the validtion modeal takes maksed visual observation and state as input, current target affordance as condation, ... | p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 17 (A.2 CONFIGURING REWARDS IN VLA MODELS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 17 / A.2 CONFIGURING REWARDS IN VLA MODELS - extractive body cue:** When more detailed or nuanced reward structures are needed, AI agents can design sophisticated reward functions (Ma et al., 2024a).
- **p. 17 / A.2 CONFIGURING REWARDS IN VLA MODELS - extractive body cue:** In such cases, the reward function can be interpreted as R(s, a) = 1 if the robot successfully completes the task, and R(s, a) = ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 17 (A.3 DETAILS ON REAL2SIM DATA PROJECTION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Constructed, regressive, transformer, classifier, validtion, modeal, takes, maksed, visual, observation, state, input, current, target | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Constructed, regressive, transformer, classifier, validtion, modeal, takes, maksed, visual, observation | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | findings, call, alternative, instead, focusing, generating, high-fidelity, data, addressing, Sim2Real | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | When, more, detailed, nuanced, reward, structures, needed, agents, design, sophisticated | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 17 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** Constructed as a regressive transformer classifier, the validtion modeal takes maksed visual observation and state as input, current target affordance as condation, and output a ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Within the robot's operational environment, our objective is to learn a control policy π(at, . . . , at+M / ot-H, . . . , ...
- **p. 16 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** The pipeline initiates by employing a diffusion-based action expert to generate action trajectories through denoising, conditioned on the aforementioned masked visual observations and proprioceptive inputs.
- **p. 16 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** This architecture is complemented by two additional transformer blocks of identical configuration dedicated to affordance inference and guidance, alongside multiple MLP adapters that facilitate dimensional ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** The Vision-Language-Action (VLA) models, which integrate visual observations, natural language commands, and robotic control actions, have emerged as a prevailing architecture for implementing generalist agents ...
- **p. 6 / 1 INTRODUCTION - extractive body cue:** The embodied agent, equipped with a vision-language model, decomposes the task into atomic units (Nasiriany et al., 2024), identifies the target object from the input ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** By leveraging observations and language-based task annotations, the control policy can be effectively instantiated as a VLA model (Kim et al., 2024).
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | To benchmark our Sim2Real-VLA , we compare it against several representative baselines, including 1) Action Chunking with Transformers (ACT) (Zhao et al., ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | At a time step t, ot captures both proprioception op t and visual signals ov t from multi-view cameras. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | The training configuration utilizes a batch size of 8, requiring approximately 36 GPU hours to complete under these specified conditions. | hardware, batch and throughput |

## Training vs Inference

- **p. 16 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** This architecture is complemented by two additional transformer blocks of identical configuration dedicated to affordance inference and guidance, alongside multiple MLP adapters that facilitate dimensional ...
- **p. 17 / A.2 CONFIGURING REWARDS IN VLA MODELS - extractive body cue:** These functions are crucial for reinforcement learning (RL), particularly following Supervised Fine-Tuning (SFT) of VLA models.
- **p. 17 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** The training configuration utilizes a batch size of 8, requiring approximately 36 GPU hours to complete under these specified conditions.
- **p. 17 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** For the training protocol, we implement a cosine-annealing learning rate schedule with a maximum value of 1e-5 across 40,000 epochs, incorporating exponential moving average (EMA) ...
- **p. 16 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** Through the implementation of joint training and domain randomization, the module ensures robust generalization across diverse objects and environmental conditions.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Utilizing, tokenize-thenconcatenate, strategy, model, fuses, action, embeddings, predicted, affordance, outputs, architecture, complemented, additional, transformer, blocks, identical, configuration, dedicated, inference, guidance.
- **Relevant PDF headings:** A.1 MODEL ARCHITECTURE & KEY PARAMETERS (p. 16); A.2 CONFIGURING REWARDS IN VLA MODELS (p. 17).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Given either an egocentric video of a human manipulating objects or teleoperated demonstrations performed in the real environment, we project both the ... | p. 17 (A.3 DETAILS ON REAL2SIM DATA PROJECTION), p. 17 (A.3 DETAILS ON REAL2SIM DATA PROJECTION) |
| Action / skill decoding | Table 9: Success Rates with Few-Shot Real Data. Comparison across Sim Only, Real Only (10 demos), and Sim-then-Real (5/10 demos) strategies. Note ... | p. 24 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Receding execution / feedback | Figure 4: Visualization of environment configurations under the domain gaps of background texture, object features, and table texture across different manipulation tasks. ... | p. 9 (Figure/Table caption), p. 24 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1: The pipeline of our Sim2Real-VLA model consists of two main components: a planning system ( Section 4.1) that enables embodied reasoning through a ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Visualization of attention maps and relevant robot motions during robotic manipulation. Figure 5 visualizes the attention maps of Sim2Real-VLA's action transformer blocks and ...
- **p. 16 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** These refined action chunks are tokenized by a pretrained FAST tokenizer and embedded.
- **p. 17 / A.1 MODEL ARCHITECTURE & KEY PARAMETERS - extractive body cue:** A pretrained validation model is also needed in affordance chain inferrence.
- **p. 17 / A.2 CONFIGURING REWARDS IN VLA MODELS - extractive body cue:** These functions are crucial for reinforcement learning (RL), particularly following Supervised Fine-Tuning (SFT) of VLA models.
- **p. 8 / 1 INTRODUCTION - extractive body cue:** For unsuccessful trials where the robot fails to complete the task, we report the predefined maximum step limit as an upper bound.
- **p. 17 / A.3 DETAILS ON REAL2SIM DATA PROJECTION - extractive body cue:** However, in cases where three-view images capture only partial scene information (e.g., occluded object surfaces), or when the retrieved scene fails to semantically align with ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 17 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 17 (A.2 CONFIGURING REWARDS IN VLA MODELS), objective p. 17 (A.2 CONFIGURING REWARDS IN VLA MODELS), p. 17 (A.2 CONFIGURING REWARDS IN VLA MODELS), temporal p. 8 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 5 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS), p. 16 (A.1 MODEL ARCHITECTURE & KEY PARAMETERS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
