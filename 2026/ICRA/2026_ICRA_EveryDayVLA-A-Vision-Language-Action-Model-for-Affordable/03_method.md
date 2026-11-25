# Method - EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://api.crossref.org/works/10.1109/icra57385.2026.11696905; PDF retrieval source: https://arxiv.org/pdf/2511.05397. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 2 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD)): Instead, EveryDayVLA takes advantage of action chunking, parallel decoding, and a collaborative training recipe, predicting discrete autoregressive and continuous action chunks, using an L1-regression objective, to achieve high performa ...

## Method Body Digest

- **p. 2 / III. METHOD - extractive body cue:** Instead, EveryDayVLA takes advantage of action chunking, parallel decoding, and a collaborative training recipe, predicting discrete autoregressive and continuous action chunks, using an L1-regression objective, ...
- **원문 대조:** Discrete action에는 cross-entropy, continuous action에는 L1 loss를 사용하며 두 항을 결합해 학습한다. 식 (1)의 log 항은 예측한 discrete-action probability에 적용된다. ([PDF p. 3](https://arxiv.org/pdf/2511.05397#page=3), §III-A Collaborative Training, Eqs. (1)–(3)).
- **p. 3 / III. METHOD - extractive body cue:** The VLA takes as input an image and natural language instruction and these are tokenized via the vision and language encoders, and sent to the ...
- **p. 2 / III. METHOD - extractive body cue:** To further improve performance, we introduce a novel adaptive horizon module, allowing the
- **p. 4 / III. METHOD - extractive body cue:** Algorithm 1 Adaptive Horizon Ensembler Require: Continuous actions {ac t}T t=1, Discrete actions {ad t }T t=1 Require: Parameters: min actions, replan threshold, threshold, max ...
- **p. 4 / III. METHOD - extractive body cue:** 5: end for 6: if ∃t ∈ [1, . . . , min actions] : madt > replan threshold and min actions > 1 then ...
- **p. 3 / III. METHOD - extractive body cue:** Hardware We built a $300 6-DOF robotic manipulator (see Figure 3), using brackets on online marketplaces due to cost constraints.
- **p. 4 / III. METHOD - extractive body cue:** The base was secured to 1/2 inch plywood board cut to 0.5m (length) x 1.0m (width) to be centered along the width and at the ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we present a full-stack system, and present three distinct contributions. • Collaborative training with adaptive horizon control (AdaHorizon).
- **p. 3 / III. METHOD - extractive body cue:** We term our method AdaHorizon, and find that it enables discrete actions to match or exceed the precision of continuous controls, even on dexterous tasks ...
- **p. 2 / III. METHOD - extractive body cue:** To further improve performance, we introduce a novel adaptive horizon module, allowing the

## Source Evidence Cues

- **p. 2 / III. METHOD - extractive body cue:** Instead, EveryDayVLA takes advantage of action chunking, parallel decoding, and a collaborative training recipe, predicting discrete autoregressive and continuous action chunks, using an L1-regression objective, ...
- **원문 대조:** Discrete action에는 cross-entropy, continuous action에는 L1 loss를 사용하며 두 항을 결합해 학습한다. 식 (1)의 log 항은 예측한 discrete-action probability에 적용된다. ([PDF p. 3](https://arxiv.org/pdf/2511.05397#page=3), §III-A Collaborative Training, Eqs. (1)–(3)).
- **p. 3 / III. METHOD - extractive body cue:** The VLA takes as input an image and natural language instruction and these are tokenized via the vision and language encoders, and sent to the ...
- **p. 2 / III. METHOD - extractive body cue:** To further improve performance, we introduce a novel adaptive horizon module, allowing the
- **p. 4 / III. METHOD - extractive body cue:** Algorithm 1 Adaptive Horizon Ensembler Require: Continuous actions {ac t}T t=1, Discrete actions {ad t }T t=1 Require: Parameters: min actions, replan threshold, threshold, max ...
- **p. 4 / III. METHOD - extractive body cue:** 5: end for 6: if ∃t ∈ [1, . . . , min actions] : madt > replan threshold and min actions > 1 then ...
- **Detected method headings:** III. METHOD (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Instead, EveryDayVLA takes advantage of action chunking, parallel decoding, and a collaborative training recipe, predicting discrete autoregressive and continuous action chunks, using ... | p. 2 (III. METHOD), p. 3 (III. METHOD) |
| Collaborative action training | Discrete/continuous action을 함께 감독 | Expert action chunk | Cross-entropy + λ·L1 | 두 action representation의 예측 | 원문 대조: Discrete action에는 cross-entropy, continuous action에는 L1 loss를 사용하며 두 항을 결합해 학습한다. 식 (1)의 log 항은 예측한 discrete-action probability에 적용된다. ([PDF p. 3](https://arxiv.org/pdf/2511.05397#page=3), §III-A Collaborative Training, Eqs. (1)–(3)) | [PDF p. 3](https://arxiv.org/pdf/2511.05397#page=3), §III-A Collaborative Training, Eqs. (1)–(3) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | The VLA takes as input an image and natural language instruction and these are tokenized via the vision and language encoders, and ... | p. 3 (III. METHOD), p. 2 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHOD - extractive body cue:** Hardware We built a $300 6-DOF robotic manipulator (see Figure 3), using brackets on online marketplaces due to cost constraints.
- **p. 2 / III. METHOD - extractive body cue:** Instead, EveryDayVLA takes advantage of action chunking, parallel decoding, and a collaborative training recipe, predicting discrete autoregressive and continuous action chunks, using an L1-regression objective, ...
- **원문 대조:** Discrete action에는 cross-entropy, continuous action에는 L1 loss를 사용하며 두 항을 결합해 학습한다. 식 (1)의 log 항은 예측한 discrete-action probability에 적용된다. ([PDF p. 3](https://arxiv.org/pdf/2511.05397#page=3), §III-A Collaborative Training, Eqs. (1)–(3)).
- **p. 4 / III. METHOD - extractive body cue:** The base was secured to 1/2 inch plywood board cut to 0.5m (length) x 1.0m (width) to be centered along the width and at the ...
- **p. 4 / III. METHOD - extractive body cue:** 5: end for 6: if ∃t ∈ [1, . . . , min actions] : madt > replan threshold and min actions > 1 then ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | EveryDayVLA, ingests, input, demonstration, consisting, image, observation, language, instruction, VLA, takes, natural, tokenized, vision | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | EveryDayVLA, ingests, input, demonstration, consisting, image, observation, language, instruction, VLA | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | address, challenges, present, full-stack, system, three, distinct, contributions, Collaborative, training | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Hardware, built, DOF, robotic, manipulator, Figure, brackets, online, marketplaces, cost | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHOD - extractive body cue:** EveryDayVLA EveryDayVLA ingests as input a demonstration consisting of an image observation ot and a language instruction lt.
- **p. 3 / III. METHOD - extractive body cue:** The VLA takes as input an image and natural language instruction and these are tokenized via the vision and language encoders, and sent to the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Vision-Language-Action (VLA) models [1] have transformed robotics by learning a direct mapping from raw images and natural-language instructions to motor commands, bypassing hand-designed perception or ...
- **p. 4 / III. METHOD - extractive body cue:** Algorithm 1 Adaptive Horizon Ensembler Require: Continuous actions {ac t}T t=1, Discrete actions {ad t }T t=1 Require: Parameters: min actions, replan threshold, threshold, max ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** We streamline teleoperation to collect trajectories with language instructions, video, and end-effector poses, releasing more than 1,200 task executions to enable scalable fine-tuning across diverse ...
- **p. 2 / III. METHOD - extractive body cue:** Instead, EveryDayVLA takes advantage of action chunking, parallel decoding, and a collaborative training recipe, predicting discrete autoregressive and continuous action chunks, using an L1-regression objective, ...
- **p. 4 / III. METHOD - extractive body cue:** 5: end for 6: if ∃t ∈ [1, . . . , min actions] : madt > replan threshold and min actions > 1 then ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | To satisfy real-time constraints, we enforce a minimum execution length of four actions per eight-step chunk. | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Accordingly, rather than fusing actions based on confidence thresholds [39], we adaptively adjust the planning horizon using our difference threshold-executing only those ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | We also achieve an inference rate of up to 108.4 Hz (Table III), adding only 0.9 ms of latency relative to OpenVLA-OFT ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / III. METHOD - extractive body cue:** Instead, EveryDayVLA takes advantage of action chunking, parallel decoding, and a collaborative training recipe, predicting discrete autoregressive and continuous action chunks, using an L1-regression objective, ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Implementation Details We extended the [35] codebase to jointly train autoregressive and regression heads and deploy with our AdaHorizon ensembler.
- **p. 2 / III. METHOD - extractive body cue:** On the other hand, diffusion-based VLAs suffer from long training times [33] [34], and multiple denoising steps.
- **p. 3 / III. METHOD - extractive body cue:** Hardware We built a $300 6-DOF robotic manipulator (see Figure 3), using brackets on online marketplaces due to cost constraints.
- **p. 3 / III. METHOD - extractive body cue:** EveryDayVLA uses the Prismatic-7B VLM [45], which uses a two part visual encoder, containing pretrained SigLIP [46] and DinoV2 [47] models.

## Method-Specific Formal Details

- **Body-defined terms:** Instead, EveryDayVLA, takes, advantage, action, chunking, parallel, decoding, collaborative, training, recipe, predicting, discrete, autoregressive, continuous, chunks, L1-regression, objective, achieve, high.
- **Relevant PDF headings:** III. METHOD (p. 2).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | Baselines On the LIBERO simulation benchmark, we report success rates across all four task suites, comparing against Diffusion Policy [3], Octo [5], ... | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Action / skill decoding | For all experiments, we use the discrete actions, with the adaptive horizon ensembler (AdaHorizon), which yields higher success rates and improved grasp ... | p. 4 (IV. EXPERIMENTS), p. 6 (V. RESULTS) |
| Receding execution / feedback | For all experiments, we use the discrete actions, with the adaptive horizon ensembler (AdaHorizon), which yields higher success rates and improved grasp ... | p. 4 (IV. EXPERIMENTS), p. 6 (V. RESULTS) |

## Failure and Ablation Link

- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Dataset We fine-tune the OpenVLA-7B model [19] on our custom dataset of 1,200 demonstrations-each pairing a naturallanguage instruction with an RGB observation sequence and corresponding ...
- **p. 6 / V. RESULTS - extractive body cue:** On ball pick-and-place, EverydayVLA exceeds both baselines in every variant except "pick-and-place right." For rock manipulation, our model achieves comparable success, underscoring its robustness across ...
- **p. 6 / V. RESULTS - extractive body cue:** In an ablation against using only continuous (Cont-L1) or only discrete (AR) actions, AdaHorizon consistently improves performance in every suite-on average by 0.8 % over ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Policy inputs: third-person image, language instruction Spatial SR (%) Object SR (%) Goal SR (%) Long SR (%) Average SR (%) Diffusion Policy (scratch) [3] ...
- **p. 6 / VI. CONCLUSIONS - extractive body cue:** We also experience limitations in executing fine-grained manipulation, which is due to the limited servo precision as well as relatively low number of expert demonstrations ...
- **p. 6 / V. RESULTS - extractive body cue:** The primary failure mode for EverydayVLA is delayed object release and not finishing the task in a timely manner.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. EveryDayVLA system. Top: EveryDayVLA finetunes a VLA for a low-cost manipulator to generate continuous and discrete actions, which are passed to an adaptive ...

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 2 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), objective p. 3 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), temporal p. 3 (III. METHOD), p. 3 (III. METHOD), p. 6 (V. RESULTS), p. 2 (III. METHOD), p. 2 (III. METHOD), p. 1 (I. INTRODUCTION).
