# Method - SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p011.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p011.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (A. The SpatialVLA Model Architecture), p. 5 (B. The Pre-training and Post-training Scheme), p. 4 (B. The Pre-training and Post-training Scheme), p. 4 (A. The SpatialVLA Model Architecture), p. 3 (A. The SpatialVLA Model Architecture), p. 5 (B. The Pre-training and Post-training Scheme)): During training, SpatialVLA model is trained to take the ego3D position encoding representation Ogq and natural language task instruction Las inputs, and autoregressively generate spatial action tokens a using the ...

## Method Body Digest

- **p. 3 / A. The SpatialVLA Model Architecture - extractive body cue:** During training, SpatialVLA model is trained to take the ego3D position encoding representation Ogq and natural language task instruction Las inputs, and autoregressively generate spatial ...
- **p. 5 / B. The Pre-training and Post-training Scheme - extractive body cue:** In detail, we ft a new Gaussian distribution AV (jig, Yacw) for each action variable on posttraining datasets and create discrete spatial action grids Gey ...
- **p. 4 / B. The Pre-training and Post-training Scheme - extractive body cue:** ‘To obtain a generalist robot policy model, the training procedure of SpatialVLA consists of pre-training stage and posttraining stage.
- **p. 4 / A. The SpatialVLA Model Architecture - extractive body cue:** 2, we first employ SigLIP [68] visual encoder to extract 2D semantic visual features X ¢ R4**" to inherit the alignment between vision and language, ...
- **p. 3 / A. The SpatialVLA Model Architecture - extractive body cue:** The ego3D position encoding representation Osa aims to capture 3D scene structure via integrating 3D spatial information with 2D semantic features. ‘The adaptive action grids ...
- **p. 5 / B. The Pre-training and Post-training Scheme - extractive body cue:** initialized, and then they are optimized during training, as well as the parameters of vision encoder and LLM backbone.
- **p. 4 / A. The SpatialVLA Model Architecture - extractive body cue:** where f(x) is the probability density function of Gaussian distribution V(yi*,%*).
- **p. 4 / A. The SpatialVLA Model Architecture - extractive body cue:** 1,a2),.-,{ayt1saq = 1]} with equal probability 1/M on each normalized action variable, ie,

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this work consist of a novel generalist robot policy that explores spatial representations for robot foundation models, sophisticated designs on ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** OpenVLA [30] adopts a similar action discretization approach and fine-tune Prismatic VLM [28] only on the OXE dataset [13], which consists of robot data from ...
- **p. 4 / B. The Pre-training and Post-training Scheme - extractive body cue:** ‘To obtain a generalist robot policy model, the training procedure of SpatialVLA consists of pre-training stage and posttraining stage.

## Source Evidence Cues

- **p. 3 / A. The SpatialVLA Model Architecture - extractive body cue:** During training, SpatialVLA model is trained to take the ego3D position encoding representation Ogq and natural language task instruction Las inputs, and autoregressively generate spatial ...
- **p. 5 / B. The Pre-training and Post-training Scheme - extractive body cue:** In detail, we ft a new Gaussian distribution AV (jig, Yacw) for each action variable on posttraining datasets and create discrete spatial action grids Gey ...
- **p. 4 / B. The Pre-training and Post-training Scheme - extractive body cue:** ‘To obtain a generalist robot policy model, the training procedure of SpatialVLA consists of pre-training stage and posttraining stage.
- **p. 4 / A. The SpatialVLA Model Architecture - extractive body cue:** 2, we first employ SigLIP [68] visual encoder to extract 2D semantic visual features X ¢ R4**" to inherit the alignment between vision and language, ...
- **p. 3 / A. The SpatialVLA Model Architecture - extractive body cue:** The ego3D position encoding representation Osa aims to capture 3D scene structure via integrating 3D spatial information with 2D semantic features. ‘The adaptive action grids ...
- **p. 5 / B. The Pre-training and Post-training Scheme - extractive body cue:** initialized, and then they are optimized during training, as well as the parameters of vision encoder and LLM backbone.
- **Detected method headings:** A. The SpatialVLA Model Architecture (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | During training, SpatialVLA model is trained to take the ego3D position encoding representation Ogq and natural language task instruction Las inputs, and ... | p. 3 (A. The SpatialVLA Model Architecture), p. 5 (B. The Pre-training and Post-training Scheme) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | In detail, we ft a new Gaussian distribution AV (jig, Yacw) for each action variable on posttraining datasets and create discrete spatial ... | p. 5 (B. The Pre-training and Post-training Scheme), p. 4 (B. The Pre-training and Post-training Scheme) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | ‘To obtain a generalist robot policy model, the training procedure of SpatialVLA consists of pre-training stage and posttraining stage. | p. 4 (B. The Pre-training and Post-training Scheme), p. 4 (A. The SpatialVLA Model Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / B. The Pre-training and Post-training Scheme - extractive body cue:** In detail, we ft a new Gaussian distribution AV (jig, Yacw) for each action variable on posttraining datasets and create discrete spatial action grids Gey ...
- **p. 3 / A. The SpatialVLA Model Architecture - extractive body cue:** During training, SpatialVLA model is trained to take the ego3D position encoding representation Ogq and natural language task instruction Las inputs, and autoregressively generate spatial ...
- **p. 5 / B. The Pre-training and Post-training Scheme - extractive body cue:** initialized, and then they are optimized during training, as well as the parameters of vision encoder and LLM backbone.
- **p. 4 / A. The SpatialVLA Model Architecture - extractive body cue:** where f(x) is the probability density function of Gaussian distribution V(yi*,%*).
- **p. 4 / A. The SpatialVLA Model Architecture - extractive body cue:** 1,a2),.-,{ayt1saq = 1]} with equal probability 1/M on each normalized action variable, ie,
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (A. The SpatialVLA Model Architecture), p. 5 (B. The Pre-training and Post-training Scheme).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | find, model, Spatial, VLA, bridges, observation, inputs, aetion, outputs, universal, robot-agnostic, manner, explores, powerful | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | find, model, Spatial, VLA, bridges, observation, inputs, aetion, outputs, universal | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, contributions, consist, novel, generalist, robot, policy, explores, spatial, representations | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | detail, Gaussian, distribution, Yacw, action, variable, posttraining, datasets, create, discrete | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / I. INTRODUCTION - extractive body cue:** We find that the proposed model Spatial VLA bridges observation inputs and aetion outputs in a universal robot-agnostic manner, which explores powerful 3D spatial-aware representations ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, as illustrated in Fig. /, we propose a generalist robot policy SpatialVLA, which equips the VLA model with 3D spatial intelligence by ...
- **p. 3 / A. The SpatialVLA Model Architecture - extractive body cue:** During training, SpatialVLA model is trained to take the ego3D position encoding representation Ogq and natural language task instruction Las inputs, and autoregressively generate spatial ...
- **p. 3 / A. The SpatialVLA Model Architecture - extractive body cue:** To empower SpatialVLA with 3D spatial intelligence, we augment the VLM backbone with robotics-specific 3D-aware inputs and outputs, namely, Ego3D Position Encoding and Adaptive Action ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Recent advances in Vision-Language-Action (VLA) models [7, 30, 5, 33] show a promising paradigm in building such generalist policy by finetuning the pre-trained Vision-Language Models ...
- **p. 5 / B. The Pre-training and Post-training Scheme - extractive body cue:** Formally, for new spatial action grids Grey, suppose ith 3D grid Gi, in translation space ag, with centroid (hoes Olous Toon) and its adjacent 3D ...
- **p. 5 / B. The Pre-training and Post-training Scheme - extractive body cue:** ‘The goal of our experimental evaluations is to test SpatialVLA's ability to serve as a generalist robot control policy ‘out of the box, as well ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | SpatialVLA is, first prestrained on top of a vision-language model with 1.1 Million real-world robot episodes, to learn a generalist manipulation policy ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | This position encoding is derived in the egocentric ‘camera frame that eliminates the need for specific robot- ‘camera calibration, which is universally ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Moreover, itis worth noting that the model only needs 10 generate 3 tokens for one-step robot actions rather than 7 tokens as ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / A. The SpatialVLA Model Architecture - extractive body cue:** During training, SpatialVLA model is trained to take the ego3D position encoding representation Ogq and natural language task instruction Las inputs, and autoregressively generate spatial ...
- **p. 5 / B. The Pre-training and Post-training Scheme - extractive body cue:** In detail, we ft a new Gaussian distribution AV (jig, Yacw) for each action variable on posttraining datasets and create discrete spatial action grids Gey ...
- **p. 4 / B. The Pre-training and Post-training Scheme - extractive body cue:** ‘To obtain a generalist robot policy model, the training procedure of SpatialVLA consists of pre-training stage and posttraining stage.
- **p. 5 / B. The Pre-training and Post-training Scheme - extractive body cue:** initialized, and then they are optimized during training, as well as the parameters of vision encoder and LLM backbone.
- **p. 5 / 3) How well does SpatialVLA perform in scenarios that - extractive body cue:** Implementation Details. ‘The SpatialVLA model is pre~ trained with 1.1 Million real-robot demonstrations from the OXE [15] and RH2OT dataset {18} on a cluster of ...
- **p. 9 / B. Adapting to New Robot Setups - extractive body cue:** All the models are trained from seratch on 8 A100 GPUs with 128 batch size for 120k steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** During, training, SpatialVLA, model, trained, take, ego3D, position, encoding, representation, Ogq, natural, language, task, instruction, Las, inputs, autoregressively, generate, spatial.
- **Relevant PDF headings:** A. The SpatialVLA Model Architecture (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We train SpatialVLA from Paligemma2 backbone [62] on a cross-robot dataset mixture with 1.1 Million real robot demonstrations {615 Gu}> covering a ... | p. 4 (B. The Pre-training and Post-training Scheme), p. 5 (3) How well does SpatialVLA perform in scenarios that) |
| Action / skill decoding | In particular, SpatialVLA also matches or outperforms te latest SOTA model 7, Tab, I! summarizes the esults across different manipulation policies on ... | p. 7 (10 Ablations on Design), p. 5 (B. The Pre-training and Post-training Scheme) |
| Receding execution / feedback | Spatial VLA achieves the highest average success rate, outperforming all generalist manipulation policies. | p. 7 (10 Ablations on Design), p. 9 (B. Adapting to New Robot Setups) |

## Failure and Ablation Link

- **p. 6 / 10 Ablations on Design - extractive body cue:** On average, SpatialVLA achieves the highest overall visual matching and variant aggregation performance with a significant margin, Our SpatialVLA model yields 71.9% and 75.1% Visual ...
- **p. 8 / B. Adapting to New Robot Setups - extractive body cue:** In this section, we conduct ablation studies to investigate the effectiveness of the proposed 3D Spatial Presentation in both pre-training and post-rraining stages.
- **p. 6 / 10 Ablations on Design - extractive body cue:** a thorough ablation study on a mixed Fractal and Bridge dataset to verify our design decisions.
- **p. 7 / 10 Ablations on Design - extractive body cue:** conditions, characterized by varying visual appearances, which is further supported by its superior performance in variant aggregation.
- **p. 9 / B. Adapting to New Robot Setups - extractive body cue:** ‘TABLE V: Fine-tuning Ablations in Domain Datasets.
- **p. 5 / 3) How well does SpatialVLA perform in scenarios that - extractive body cue:** Finally, we conduct comprehensive ablation studies on a mixture of Fractal (6] and BridgeV2 [64] datasets to verify our design decisions in Spatial VLA.
- **p. 5 / B. The Pre-training and Post-training Scheme - extractive body cue:** With this embedding initialization, the new action tokenizer is capable of effectively transfering pretrained spatial action knowledge to new robot setups.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (A. The SpatialVLA Model Architecture), p. 5 (B. The Pre-training and Post-training Scheme), p. 4 (B. The Pre-training and Post-training Scheme), p. 4 (A. The SpatialVLA Model Architecture), p. 3 (A. The SpatialVLA Model Architecture), p. 5 (B. The Pre-training and Post-training Scheme), objective p. 5 (B. The Pre-training and Post-training Scheme), p. 3 (A. The SpatialVLA Model Architecture), p. 5 (B. The Pre-training and Post-training Scheme), p. 4 (A. The SpatialVLA Model Architecture), p. 4 (A. The SpatialVLA Model Architecture), temporal p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (030 Position Encoding), p. 3 (A. The SpatialVLA Model Architecture), p. 4 (A. The SpatialVLA Model Architecture).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
