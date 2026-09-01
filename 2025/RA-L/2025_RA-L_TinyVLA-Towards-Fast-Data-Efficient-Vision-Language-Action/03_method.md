# Method - TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2409.12514; PDF retrieval source: https://arxiv.org/pdf/2409.12514. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 2 (III. METHOD)): TinyVLA encompasses several crucial designs: 1) We adopt a pre-trained VLM as the initialization of a policy network; 2) During training the robot data, we freeze the pre-trained parts and ...

## Method Body Digest

- **p. 2 / III. METHOD - extractive PDF cue:** TinyVLA encompasses several crucial designs: 1) We adopt a pre-trained VLM as the initialization of a policy network; 2) During training the robot data, we ...
- **p. 3 / III. METHOD - extractive PDF cue:** After training is completed, we apply re-parameterization techniques to integrate the LoRA module seamlessly into the standard language model, thereby enhancing inference speed.
- **p. 3 / III. METHOD - extractive PDF cue:** Then, these normalized features are subsequently concatenated with the robot's proprioceptive state vector.
- **p. 2 / III. METHOD - extractive PDF cue:** We then followed the training pipeline of LLaVA [13], using their vision-language dataset to train this family of VLMs.
- **p. 3 / III. METHOD - extractive PDF cue:** We adopt diffusion policy as our policy head. limits gradient updates to a low-dimensional space.
- **p. 3 / III. METHOD - extractive PDF cue:** First, the visuallanguage model (VLM) backbone encodes raw observations and language instructions into multimodal embedding vectors.
- **p. 3 / III. METHOD - extractive PDF cue:** Learning action with diffusion policy decoder.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Then, instead of using the next token prediction technique to predict action tokens independently, we attach a diffusion-based head to the pre-trained multimodal model for ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Our contribution are the three folds: • We introduce a novel VLA architecture that combines lightweight vision-language models with a diffusion model, enabling fast inference, ...
- **p. 6 / 1 Background - extractive PDF cue:** In Figure 9, we present the spatial generalization performance of our methods.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** In this work, we propose TinyVLA, a compact visionlanguage-action model designed for fast inference.

## Source Evidence Cues

- **p. 2 / III. METHOD - extractive PDF cue:** TinyVLA encompasses several crucial designs: 1) We adopt a pre-trained VLM as the initialization of a policy network; 2) During training the robot data, we ...
- **p. 3 / III. METHOD - extractive PDF cue:** After training is completed, we apply re-parameterization techniques to integrate the LoRA module seamlessly into the standard language model, thereby enhancing inference speed.
- **p. 3 / III. METHOD - extractive PDF cue:** Then, these normalized features are subsequently concatenated with the robot's proprioceptive state vector.
- **p. 2 / III. METHOD - extractive PDF cue:** We then followed the training pipeline of LLaVA [13], using their vision-language dataset to train this family of VLMs.
- **Detected method headings:** III. METHOD (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | TinyVLA encompasses several crucial designs: 1) We adopt a pre-trained VLM as the initialization of a policy network; 2) During training the ... | p. 2 (III. METHOD), p. 3 (III. METHOD) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | After training is completed, we apply re-parameterization techniques to integrate the LoRA module seamlessly into the standard language model, thereby enhancing inference ... | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Then, these normalized features are subsequently concatenated with the robot's proprioceptive state vector. | p. 3 (III. METHOD), p. 2 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHOD - extractive PDF cue:** We adopt diffusion policy as our policy head. limits gradient updates to a low-dimensional space.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | TinyVLA, encompasses, several, crucial, designs, adopt, pre-trained, VLM, initialization, policy, network, During, training, robot | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | TinyVLA, encompasses, several, crucial, designs, adopt, pre-trained, VLM, initialization, policy | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contribution, three, folds, introduce, novel, VLA, architecture, combines, lightweight, vision-language | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | adopt, diffusion, policy, head, limits, gradient, updates, low-dimensional, space | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / III. METHOD - extractive PDF cue:** TinyVLA encompasses several crucial designs: 1) We adopt a pre-trained VLM as the initialization of a policy network; 2) During training the robot data, we ...
- **p. 3 / III. METHOD - extractive PDF cue:** First, the visuallanguage model (VLM) backbone encodes raw observations and language instructions into multimodal embedding vectors.
- **p. 3 / III. METHOD - extractive PDF cue:** Learning action with diffusion policy decoder.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Then, instead of using the next token prediction technique to predict action tokens independently, we attach a diffusion-based head to the pre-trained multimodal model for ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Recently, vision-language-action (VLA) models have garnered significant attention for their ability to extend pretrained vision-language models to robotics using a next-token prediction approach.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, these methods suffer from a critical drawback: extremely slow inference speeds, largely due to their dependence on large visionlanguage models and auto-regressive action token ...
- **p. 7 / 1 Background - extractive PDF cue:** WEN et al.: TINYVLA: TOWARDS FAST, DATA-EFFICIENT VISION-LANGUAGE-ACTION MODELS FOR ROBOTIC MANIPULATION 7 generalization can be seen in variations in background color, object texture, or ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Building TinyVLA with Efficient Vision-Language Models The initial step involves acquiring pre-trained visionlanguage models (VLM). | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | And the pipeline can be splited into 3 steps. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | And the pipeline can be splited into 3 steps. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / III. METHOD - extractive PDF cue:** TinyVLA encompasses several crucial designs: 1) We adopt a pre-trained VLM as the initialization of a policy network; 2) During training the robot data, we ...
- **p. 3 / III. METHOD - extractive PDF cue:** After training is completed, we apply re-parameterization techniques to integrate the LoRA module seamlessly into the standard language model, thereby enhancing inference speed.
- **p. 2 / III. METHOD - extractive PDF cue:** We then followed the training pipeline of LLaVA [13], using their vision-language dataset to train this family of VLMs.
- **p. 2 / III. METHOD - extractive PDF cue:** TinyVLA encompasses several crucial designs: 1) We adopt a pre-trained VLM as the initialization of a policy network; 2) During training the robot data, we ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** TinyVLA, encompasses, several, crucial, designs, adopt, pre-trained, VLM, initialization, policy, network, During, training, robot, data, freeze, parts, utilize, parameter-efficient, finetuning.
- **Relevant PDF headings:** III. METHOD (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | More Real-World Experiments: Bimanual Robot We further conducted experiments on the Bimanual UR5 Robot, applying it to three distinct tasks: PlaceBread, StackCube, ... | p. 5 (IV. EXPERIMENTS), p. 3 (IV. EXPERIMENTS) |
| Action / skill decoding | In our experiments, we aim to study the following questions: • Does TinyVLA achieve a higher success rate in multitasking robotic manipulation ... | p. 3 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Receding execution / feedback | In our experiments, we aim to study the following questions: • Does TinyVLA achieve a higher success rate in multitasking robotic manipulation ... | p. 3 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** For all the tasks we do not add additional distractors except in the remove the lid of the box task, in order to better evaluate ...
- **p. 4 / IV. EXPERIMENTS - extractive PDF cue:** Since TinyVLA uses a pre-trained multimodal model as its backbone, we observe similar embodied capabilities driven by the rich world knowledge implicitly stored in these ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: Model architecture. The left image illustrates the VLM pretraining pipeline, whereas the right image demon- strates the process of training TinyVLA using robotic ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 8: Object & Appearance generalization. For object generalization, we replace the objects with previously unseen ones that have different shapes or colors. For appearance ...
- **p. 7 / VI. CONCLUSION - extractive PDF cue:** Our approach overcomes the limitations of previous methods by
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** We use a cross mark to denote the failure of the model and a checkmark to indicate successful task completion.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 10: Types of failure for TinyVLA with different sizes of pre-trained vision-language models.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 2 (III. METHOD), objective p. 3 (III. METHOD), temporal p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
