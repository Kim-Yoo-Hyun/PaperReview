# Method - Reasoning-VLA: An Efficient and Spatial-Guided General Vision-Language-Action Reasoning Model for Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=c4iSIrb6Iv; PDF retrieval source: https://openreview.net/pdf/2958fe5249a1a673a414d689de7784b306b2a02a.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.4. How Do Actions Interact with Vision-Language), p. 3 (3. Method), p. 4 (3.5. Action Refinement Module), p. 3 (3.2. The Structure of Reasoning-VLA), p. 5 (3.7. Reward Functions), p. 5 (3.7. Reward Functions)): Since the action queries are not tied to the VLM's token representations, they first perform self-attention and then interact with the VLM through cross-attention, as illustrated in Fig.

## Method Body Digest

- **p. 4 / 3.4. How Do Actions Interact with Vision-Language - extractive PDF cue:** Since the action queries are not tied to the VLM's token representations, they first perform self-attention and then interact with the VLM through cross-attention, as ...
- **p. 3 / 3. Method - extractive PDF cue:** Qwen2.5-VL incorporates several architectural innovations: a redesigned Vision Transformer (ViT) with 2D-RoPE and windowed attention for computational efficiency; an MLP-based vision-language merger that compresses visual ...
- **p. 4 / 3.5. Action Refinement Module - extractive PDF cue:** To further enhance the representation quality and accuracy of the predicted action trajectories, we introduce an Action Refinement Module (ARM).
- **p. 3 / 3.2. The Structure of Reasoning-VLA - extractive PDF cue:** 1, the learnable action queries are designed with the same feature dimensionality as the Qwen2.5-VL reasoning model.
- **p. 5 / 3.7. Reward Functions - extractive PDF cue:** To address this limitation, we propose a Vehicle Dynamics Reward that explicitly accounts for steering and acceleration to constrain the limitations of real-world vehicle dynamics.
- **p. 5 / 3.7. Reward Functions - extractive PDF cue:** Normally, AD methods use BEV 2-dimensions coordinates x, y to optimize the loss function, while neglecting physical trajectory constraints and vehicle dynamics.
- **p. 6 / 3.7. Reward Functions - extractive PDF cue:** Reasoning-VLA-7B represents our general model.
- **p. 5 / 3.7. Reward Functions - extractive PDF cue:** This design establishes a dynamic constraint optimization objective that ensures physically feasible and stable motion trajectories.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** To summarize, the main contributions are as follows: • We propose Reasoning-VLA, an efficient and fast VLA framework that employs learnable action queries to interact ...
- **p. 3 / 3. Method - extractive PDF cue:** In the following sections, we present a detailed description of our approach to developing a VLA framework for autonomous driving and highlight key insights.
- **p. 1 / 1. Introduction - extractive PDF cue:** To address these challenges, we propose ReasoningVLA, an efficient and generalist VLA framework that establishes a new state-of-the-art for autonomous driving.

## Source Evidence Cues

- **p. 4 / 3.4. How Do Actions Interact with Vision-Language - extractive PDF cue:** Since the action queries are not tied to the VLM's token representations, they first perform self-attention and then interact with the VLM through cross-attention, as ...
- **p. 3 / 3. Method - extractive PDF cue:** Qwen2.5-VL incorporates several architectural innovations: a redesigned Vision Transformer (ViT) with 2D-RoPE and windowed attention for computational efficiency; an MLP-based vision-language merger that compresses visual ...
- **p. 4 / 3.5. Action Refinement Module - extractive PDF cue:** To further enhance the representation quality and accuracy of the predicted action trajectories, we introduce an Action Refinement Module (ARM).
- **p. 3 / 3.2. The Structure of Reasoning-VLA - extractive PDF cue:** 1, the learnable action queries are designed with the same feature dimensionality as the Qwen2.5-VL reasoning model.
- **p. 5 / 3.7. Reward Functions - extractive PDF cue:** To address this limitation, we propose a Vehicle Dynamics Reward that explicitly accounts for steering and acceleration to constrain the limitations of real-world vehicle dynamics.
- **p. 5 / 3.7. Reward Functions - extractive PDF cue:** Normally, AD methods use BEV 2-dimensions coordinates x, y to optimize the loss function, while neglecting physical trajectory constraints and vehicle dynamics.
- **p. 6 / 3.7. Reward Functions - extractive PDF cue:** Reasoning-VLA-7B represents our general model.
- **Detected method headings:** 2.2. Vision-Language-Action Models (p. 2); 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Since the action queries are not tied to the VLM's token representations, they first perform self-attention and then interact with the VLM ... | p. 4 (3.4. How Do Actions Interact with Vision-Language), p. 3 (3. Method) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Qwen2.5-VL incorporates several architectural innovations: a redesigned Vision Transformer (ViT) with 2D-RoPE and windowed attention for computational efficiency; an MLP-based vision-language merger ... | p. 3 (3. Method), p. 4 (3.5. Action Refinement Module) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | To further enhance the representation quality and accuracy of the predicted action trajectories, we introduce an Action Refinement Module (ARM). | p. 4 (3.5. Action Refinement Module), p. 3 (3.2. The Structure of Reasoning-VLA) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.7. Reward Functions - extractive PDF cue:** This design establishes a dynamic constraint optimization objective that ensures physically feasible and stable motion trajectories.
- **p. 5 / 3.7. Reward Functions - extractive PDF cue:** Normally, AD methods use BEV 2-dimensions coordinates x, y to optimize the loss function, while neglecting physical trajectory constraints and vehicle dynamics.
- **p. 3 / 3.2. The Structure of Reasoning-VLA - extractive PDF cue:** To bridge vision-language representations and action prediction, Reasoning-VLA comprises three primary components: A pre-trained VLM reasoning backbone; A VL-to-Action module that leverages a set of ...
- **p. 6 / 3.7. Reward Functions - extractive PDF cue:** The final reward rtotal is defined as the weighted sum of rtraj, rsteer and racc. rtotal = θ1rtraj + θ2rsteer + θ3racc (5) Here, θ1, ...
- **p. 4 / 3.2. The Structure of Reasoning-VLA - extractive PDF cue:** The architectural design of Reasoning-VLA offers four key advantages: 1.
- **p. 4 / 3.5. Action Refinement Module - extractive PDF cue:** This design preserves the efficiency benefits of parallel action prediction while improving the precision and smoothness of the resulting action trajectories.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (3.7. Reward Functions), p. 5 (3.7. Reward Functions).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | VLM, Question, CoT, Reasoning, Prompt, Refinement, Parallel, Action, VLto, Interaction, Ego, Status, answer, Hidden | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | VLM, Question, CoT, Reasoning, Prompt, Refinement, Parallel, Action, VLto, Interaction | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summarize, main, contributions, follows, Reasoning-VLA, efficient, fast, VLA, framework, employs | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | design, establishes, dynamic, constraint, optimization, objective, ensures, physically, feasible, stable | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** VLM Question CoT Reasoning Prompt Refinement Parallel Action VLto A Interaction Ego Status Prompt ...... <answer></answer> N Hidden States Gaussian Distribution Initializing CoT Reasoning Text ...
- **p. 4 / 3.5. Action Refinement Module - extractive PDF cue:** Specifically, the ARM takes the selected hidden states of the action queries as input and refines them through a combination of multilayer perceptron (MLP) and ...
- **p. 3 / 3.2. The Structure of Reasoning-VLA - extractive PDF cue:** Most existing Vision-Language-Action (VLA) methods either rely on a specialized action tokenizer to convert actions into a format compatible with LLMs-followed by autoregressive generation or ...
- **p. 4 / 3.3.1. Learnable Action Queries - extractive PDF cue:** Unlike VLMs, which embedded input tokens into embeddings, our action queries are initialized as learnable parameters.
- **p. 2 / 1. Introduction - extractive PDF cue:** To summarize, the main contributions are as follows: • We propose Reasoning-VLA, an efficient and fast VLA framework that employs learnable action queries to interact ...
- **p. 3 / 3. Method - extractive PDF cue:** 1, the Reasoning-VLA framework comprises three main components: (1) a reasoningenhanced vision-language model (VLM) backbone, (2) an action module that interacts with the VLM and ...
- **p. 1 / 1. Introduction - extractive PDF cue:** To address these challenges, we propose ReasoningVLA, an efficient and generalist VLA framework that establishes a new state-of-the-art for autonomous driving.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Despite these promising results, several challenges hinder the widespread deployment of VLAs in autonomous driving: 1) Most existing VLA architectures are based ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | By employing additional learnable queries, Reasoning-VLA can predict action chunks in a single step, rather than generating actions token by token, as ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | To achieve comfortable and safe driving behavior, the steering constraint reward is defined as: rsteer = 1 N -1 N-1 X j=1 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3. Method - extractive PDF cue:** Qwen2.5-VL incorporates several architectural innovations: a redesigned Vision Transformer (ViT) with 2D-RoPE and windowed attention for computational efficiency; an MLP-based vision-language merger that compresses visual ...
- **p. 5 / 3.7. Reward Functions - extractive PDF cue:** To address this limitation, we propose a Vehicle Dynamics Reward that explicitly accounts for steering and acceleration to constrain the limitations of real-world vehicle dynamics.
- **p. 5 / 3.7. Reward Functions - extractive PDF cue:** Normally, AD methods use BEV 2-dimensions coordinates x, y to optimize the loss function, while neglecting physical trajectory constraints and vehicle dynamics.
- **p. 7 / 5.1. Experiment Setups - extractive PDF cue:** Training is performed for 4 epochs for SFT and 1 epoch for RL, using a total batch size of 8 distributed across 8 H200 GPUs.
- **p. 6 / 3.7. Reward Functions - extractive PDF cue:** Reasoning-VLA-7B+ is fine-tuned with an additional RL process using the corresponding nuScenes training clips from the unified dataset. *: Official checkpoints re-validated with corrected metrics, ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Since, action, queries, tied, VLM, token, representations, they, first, perform, self-attention, then, interact, through, cross-attention, illustrated, Fig, Qwen2, incorporates, several.
- **Relevant PDF headings:** 2.2. Vision-Language-Action Models (p. 2); 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | When fine-tuned with GRPO on specific datasets (i.e., selected nuScenes training clips from the unified dataset), our generalized model demonstrates excellent task-specific ... | p. 7 (5.2.1. Open-loop Evaluation), p. 6 (4. Unified Datasets) |
| Action / skill decoding | Reasoning-VLA-3B also achieves results comparable to state-of-the-art methods. | p. 7 (5.2.1. Open-loop Evaluation), p. 7 (5.2.2. Closed-loop Evaluation) |
| Receding execution / feedback | As shown in the last row of Table 1, the additional fine-tuning further improves performance across all time intervals: Reasoning-VLA-7B+ achieves increases ... | p. 7 (5.2.1. Open-loop Evaluation), p. 7 (5.2.1. Open-loop Evaluation) |

## Failure and Ablation Link

- **p. 8 / 5.2.2. Closed-loop Evaluation - extractive PDF cue:** Ablation study of components contributions.
- **p. 6 / 5.1. Experiment Setups - extractive PDF cue:** During training, we shuffle the unified datasets and fine-tune Reasoning-VLA sequen
- **p. 6 / 5. Experiments - extractive PDF cue:** How does each design affect the performance of fine-tuned Reasoning-VLA on general autonomous driving tasks?
- **p. 7 / 5.2.1. Open-loop Evaluation - extractive PDF cue:** ReasoningVLA-7B: Based on Qwen2.5-VL-7B and fine-tuned using the SFT and RL process.
- **p. 7 / 5.1. Experiment Setups - extractive PDF cue:** NeuroNCAP provides pretrained rendering model checkpoints, making it particularly wellsuited for evaluating our method.
- **p. 8 / 5.2.2. Closed-loop Evaluation - extractive PDF cue:** We trained two models using the unified dataset: Reasoning-VLA-7B + SFT: This model is fine-tuned using only supervised fine-tuning (SFT).
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Statistical distribution of the unified dataset. However, these constraints exert a non-negligible influence on the vehicle's behavior and overall driving safety. To ad- ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.4. How Do Actions Interact with Vision-Language), p. 3 (3. Method), p. 4 (3.5. Action Refinement Module), p. 3 (3.2. The Structure of Reasoning-VLA), p. 5 (3.7. Reward Functions), p. 5 (3.7. Reward Functions), objective p. 5 (3.7. Reward Functions), p. 5 (3.7. Reward Functions), p. 3 (3.2. The Structure of Reasoning-VLA), p. 6 (3.7. Reward Functions), p. 4 (3.2. The Structure of Reasoning-VLA), p. 4 (3.5. Action Refinement Module), temporal p. 1 (1. Introduction), p. 3 (3.2. The Structure of Reasoning-VLA), p. 4 (3.3.1. Learnable Action Queries), p. 5 (3.7. Reward Functions), p. 5 (3.7. Reward Functions), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
