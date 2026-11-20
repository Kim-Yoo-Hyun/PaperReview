# Method - OmniVLA: Physically-Grounded Multimodal VLA with Unified Multi-Sensor Perception for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://api.crossref.org/works/10.1109/icra57385.2026.11695776; PDF retrieval source: https://arxiv.org/pdf/2511.01210. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 2 (I. INTRODUCTION), p. 3 (III. SYSTEM DESIGN), p. 2 (I. INTRODUCTION), p. 4 (III. SYSTEM DESIGN), p. 4 (III. SYSTEM DESIGN), p. 1 (I. INTRODUCTION)): Then, to generate masks for interested objects in the scene, we use a cloud-based Vision-Language Model (VLM) to interpret task request and generate a prompt for grounded SAM [5] to ...

## Method Body Digest

- **p. 2 / I. INTRODUCTION - extractive body cue:** Then, to generate masks for interested objects in the scene, we use a cloud-based Vision-Language Model (VLM) to interpret task request and generate a prompt ...
- **p. 3 / III. SYSTEM DESIGN - extractive body cue:** The tokens are concatenated together with language tokens as input for the large language model in the architecture, and then we generate the final action ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Building on the sensor-masked images, we propose a tailored VLA model architecture (Figure 2).
- **p. 4 / III. SYSTEM DESIGN - extractive body cue:** We use SmolVLA as our base model by default, modify its architecture, and train our model from its pretrained weights.
- **원문 대조:** 각 sensor-masked image를 공통 image encoder와 sensor별 MLP에 통과시켜 token으로 만들고, task-language token과 이어 붙여 VLA에 입력한다. 식 (4)는 이 multi-sensor token flow를 요약한다. ([PDF p. 4](https://arxiv.org/pdf/2511.01210#page=4), §III-C Model architecture and training, Eq. (4)).
- **p. 1 / I. INTRODUCTION - extractive body cue:** First, VLA models need to effectively interpret heterogeneous sensor information and use them to guide the action; naively feeding raw sensor streams leads to poor ...
- **p. 3 / III. SYSTEM DESIGN - extractive body cue:** Then we overlay the sensor images on the masked regions of RGB images to output sensor-masked images, which are the input for our multi-sensor vision-language-action ...
- **p. 4 / III. SYSTEM DESIGN - extractive body cue:** These prompts are initialized when the task begins and are updated periodically to accommodate scene dynamics, such as the introduction of new objects.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** We present OmniVLA, the first multisensory VLA that integrates novel sensing modalities to enable beyond-RGB robotic perception and manipulation by unifying heterogeneous sensors into an ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Building on the sensor-masked images, we propose a tailored VLA model architecture (Figure 2).
- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables robots to combine the strong generalization of foundation models and physical information from various sensors seamlessly, to enable physically-grounded spatial intelligence.

## Source Evidence Cues

- **p. 2 / I. INTRODUCTION - extractive body cue:** Then, to generate masks for interested objects in the scene, we use a cloud-based Vision-Language Model (VLM) to interpret task request and generate a prompt ...
- **p. 3 / III. SYSTEM DESIGN - extractive body cue:** The tokens are concatenated together with language tokens as input for the large language model in the architecture, and then we generate the final action ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Building on the sensor-masked images, we propose a tailored VLA model architecture (Figure 2).
- **p. 4 / III. SYSTEM DESIGN - extractive body cue:** We use SmolVLA as our base model by default, modify its architecture, and train our model from its pretrained weights.
- **원문 대조:** 각 sensor-masked image를 공통 image encoder와 sensor별 MLP에 통과시켜 token으로 만들고, task-language token과 이어 붙여 VLA에 입력한다. 식 (4)는 이 multi-sensor token flow를 요약한다. ([PDF p. 4](https://arxiv.org/pdf/2511.01210#page=4), §III-C Model architecture and training, Eq. (4)).
- **p. 1 / I. INTRODUCTION - extractive body cue:** First, VLA models need to effectively interpret heterogeneous sensor information and use them to guide the action; naively feeding raw sensor streams leads to poor ...
- **p. 3 / III. SYSTEM DESIGN - extractive body cue:** Then we overlay the sensor images on the masked regions of RGB images to output sensor-masked images, which are the input for our multi-sensor vision-language-action ...
- **Detected method headings:** 3) We present a lightweight OmniVLA model architec (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Then, to generate masks for interested objects in the scene, we use a cloud-based Vision-Language Model (VLM) to interpret task request and ... | p. 2 (I. INTRODUCTION), p. 3 (III. SYSTEM DESIGN) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | The tokens are concatenated together with language tokens as input for the large language model in the architecture, and then we generate ... | p. 3 (III. SYSTEM DESIGN), p. 2 (I. INTRODUCTION) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Building on the sensor-masked images, we propose a tailored VLA model architecture (Figure 2). | p. 2 (I. INTRODUCTION), p. 4 (III. SYSTEM DESIGN) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. SYSTEM DESIGN - extractive body cue:** The tokens are concatenated together with language tokens as input for the large language model in the architecture, and then we generate the final action ...
- **p. 4 / III. SYSTEM DESIGN - extractive body cue:** These prompts are initialized when the task begins and are updated periodically to accommodate scene dynamics, such as the introduction of new objects.
- **p. 4 / III. SYSTEM DESIGN - extractive body cue:** We run these updates in the background at a lower frequency than the robot's primary action-generation loop, so that VLM output delay does not affect ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (III. SYSTEM DESIGN), p. 4 (III. SYSTEM DESIGN).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Then, overlay, sensor, images, masked, regions, RGB, output, sensor-masked, input, multi-sensor, vision-language-action, model, They | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Then, overlay, sensor, images, masked, regions, RGB, output, sensor-masked, input | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | present, OmniVLA, first, multisensory, VLA, integrates, novel, sensing, modalities, enable | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | tokens, concatenated, together, language, input, large, model, architecture, then, generate | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. SYSTEM DESIGN - extractive body cue:** Then we overlay the sensor images on the masked regions of RGB images to output sensor-masked images, which are the input for our multi-sensor vision-language-action ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** They leverage vision-language pretraining to map user prompts and camera observations to robot actions, showing great generalization and instruction following capability.
- **p. 3 / III. SYSTEM DESIGN - extractive body cue:** The second part is a multi-sensor vision-language-action model backbone that is designed for sensor-masked images to capture each sensor's input and avoid requiring a large ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Finally, a LLM backbone processes the input tokens and conditions the diffusion-based action expert for the robot action output.
- **p. 4 / III. SYSTEM DESIGN - extractive body cue:** We propose a general sensor data processing pipeline applicable to various sensors, including (a) thermal camera, (b) mmWave radar, and (c) acoustic microphone array, by ...
- **원문 대조:** 각 sensor-masked image를 공통 image encoder와 sensor별 MLP에 통과시켜 token으로 만들고, task-language token과 이어 붙여 VLA에 입력한다. 식 (4)는 이 multi-sensor token flow를 요약한다. ([PDF p. 4](https://arxiv.org/pdf/2511.01210#page=4), §III-C Model architecture and training, Eq. (4)).
- **p. 5 / III. SYSTEM DESIGN - extractive body cue:** This design is a general and flexible framework to process beyond-RGB sensor-masked images, compatible with existing Vision-Language-Action models.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | We run these updates in the background at a lower frequency than the robot's primary action-generation loop, so that VLM output delay ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | We expect to have lower delays with code optimization. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Depending on the size of the demonstration dataset, the time required for training is around 14 hours for 50 K optimization steps ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / III. SYSTEM DESIGN - extractive body cue:** We use SmolVLA as our base model by default, modify its architecture, and train our model from its pretrained weights.
- **p. 1 / I. INTRODUCTION - extractive body cue:** First, VLA models need to effectively interpret heterogeneous sensor information and use them to guide the action; naively feeding raw sensor streams leads to poor ...
- **p. 5 / IV. EVALUATION - extractive body cue:** Depending on the size of the demonstration dataset, the time required for training is around 14 hours for 50 K optimization steps with batch size ...
- **p. 2 / 2) We - extractive body cue:** introduce sensor-masked images, a spatially grounded and semantically aligned representation that allows reusing pre-trained vision encoders, provides a uniform representation across sensor hardware, and improves ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** This brings several benefits that solve the challenges above: (i) making sensor information spatially grounded in RGB pixel coordinates to facilitate robotic manipulation on target ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Second, sensors differ in format, field of view, and resolution, calling for a scalable, uniform representation rather than training sensor fusion models that depend on ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, generate, masks, interested, objects, scene, cloud-based, Vision-Language, Model, VLM, interpret, task, request, prompt, grounded, SAM, provide, semantic-based, segmentation, tokens.
- **Relevant PDF headings:** 3) We present a lightweight OmniVLA model architec (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | This is likely due to SmolVLA is pretrained with lerobot robot arm dataset [2]. | p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION) |
| Action / skill decoding | Second, we show that our approach provides superior generalization capability for sensor-related tasks, outperforming baselines. | p. 5 (IV. EVALUATION), p. 6 (IV. EVALUATION) |
| Receding execution / feedback | On average, OmniVLA outperforms VLA-RGB model and VLA-RAW model by 59% and 28% in success rate respectively. | p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION) |

## Failure and Ablation Link

- **p. 6 / IV. EVALUATION - extractive body cue:** For baselines, we compare our approach against the following ablation baselines: (1) VLA-RGB (modality ablation): VLA models with standard RGB input only for training and ...
- **p. 6 / IV. EVALUATION - extractive body cue:** (2) VLARAW (representation ablation): VLA models with raw sensor data/images for training and inference input.
- **p. 5 / IV. EVALUATION - extractive body cue:** (3) Acoustic modality: Locating a ringing mobile phone concealed beneath opaque coverings using spatial audio cues from the microphone array, and removing the covering to ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Instead of relying solely on RGB cameras, OmniVLA equips robots with multi-sensor perception. We use beam- forming heatmaps as acoustic and mmWave sensor ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: System Overview. OmniVLA processes diverse sensor data into image-like 2D spatial representations, and then overlays sensor information onto RGB images to produce spatially ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Success rates when adapting to unseen tasks. We compare the pretrained OmniVLA model with two base- lines, OmniVLA-Base (no pretraining), Pretrained VLA- RAW ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Sensor Data Processing Illustration. We propose a general sensor data processing pipeline applicable to various sensors, including (a) thermal camera, (b) mmWave radar, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (I. INTRODUCTION), p. 3 (III. SYSTEM DESIGN), p. 2 (I. INTRODUCTION), p. 4 (III. SYSTEM DESIGN), p. 4 (III. SYSTEM DESIGN), p. 1 (I. INTRODUCTION), objective p. 3 (III. SYSTEM DESIGN), p. 4 (III. SYSTEM DESIGN), p. 4 (III. SYSTEM DESIGN), temporal p. 4 (III. SYSTEM DESIGN), p. 5 (IV. EVALUATION), p. 5 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 6 (IV. EVALUATION), p. 3 (III. SYSTEM DESIGN).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
