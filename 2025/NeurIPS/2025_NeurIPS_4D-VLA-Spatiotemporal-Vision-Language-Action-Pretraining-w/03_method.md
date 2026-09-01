# Method - 4D-VLA:  Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=yFjgV3cJje; PDF retrieval source: https://openreview.net/pdf/d30c75fa560b194e7ca1144a7d0d1dad6a0ee401.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3 Method), p. 3 (3 Method), p. 3 (3 Method), p. 8 (Method), p. 5 (3 Method), p. 4 (3 Method)): 3.4 Loss functions Algorithm 1: memory bank sampling Input: t, {It-j / j = 0, 1, . . . , n -1}, sample size k, feature extractor ϕ Output: A ...

## Method Body Digest

- **p. 5 / 3 Method - extractive PDF cue:** 3.4 Loss functions Algorithm 1: memory bank sampling Input: t, {It-j / j = 0, 1, . . . , n -1}, sample size k, ...
- **p. 3 / 3 Method - extractive PDF cue:** Vision-language model backbone We leverage a pretrained large vision-language model (VLM) as the backbone, specifically InternVL-4B [12], which consists of a text tokenizer T , ...
- **p. 3 / 3 Method - extractive PDF cue:** Specifically, VLA with a low-level control policy refers to a class of models that use the current observations as input to predict an action for ...
- **p. 8 / Method - extractive PDF cue:** In long-horizon tasks (Task 2 and 4), the model often succeeds in the first step but fails the second without access to history, due to ...
- **p. 5 / 3 Method - extractive PDF cue:** To enhance the model's flexibility and generalization, we introduce a time encoding token eT , which captures the relative temporal offset between the historical and ...
- **p. 4 / 3 Method - extractive PDF cue:** 𝑥 𝑦 𝑧 Spatial PE … Vision encoder … Sampled inputs LLM Transformer … … … Tokens from frame k Last hidden feature Tokens from ...
- **p. 8 / Method - extractive PDF cue:** We use 4 fixed cameras to capture each demonstration from different angles, collecting 50 trajectories per task per camera-resulting in a total of 200 trajectories ...
- **p. 5 / 3 Method - extractive PDF cue:** Our total training loss can be written as follows: L = Lt + Lr + Lg + λdLd, (3) where the translation loss Lt = ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** Our contributions are: (i) We propose 4D-VLA, an efficient VLA model that integrates a spatial module with vision features to generate 3D-aware spatial vision tokens, ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our approach enables robust pretraining, improving generalization to novel scenarios while outperforming baselines.
- **p. 5 / 3 Method - extractive PDF cue:** 3.5 MV-Bench We propose the MV-Bench to provide a comprehensive evaluation of model capabilities in learning control policies across diverse viewpoints and generalizing to novel ...

## Source Evidence Cues

- **p. 5 / 3 Method - extractive PDF cue:** 3.4 Loss functions Algorithm 1: memory bank sampling Input: t, {It-j / j = 0, 1, . . . , n -1}, sample size k, ...
- **p. 3 / 3 Method - extractive PDF cue:** Vision-language model backbone We leverage a pretrained large vision-language model (VLM) as the backbone, specifically InternVL-4B [12], which consists of a text tokenizer T , ...
- **p. 3 / 3 Method - extractive PDF cue:** Specifically, VLA with a low-level control policy refers to a class of models that use the current observations as input to predict an action for ...
- **p. 8 / Method - extractive PDF cue:** In long-horizon tasks (Task 2 and 4), the model often succeeds in the first step but fails the second without access to history, due to ...
- **p. 5 / 3 Method - extractive PDF cue:** To enhance the model's flexibility and generalization, we introduce a time encoding token eT , which captures the relative temporal offset between the historical and ...
- **p. 4 / 3 Method - extractive PDF cue:** 𝑥 𝑦 𝑧 Spatial PE … Vision encoder … Sampled inputs LLM Transformer … … … Tokens from frame k Last hidden feature Tokens from ...
- **p. 8 / Method - extractive PDF cue:** We use 4 fixed cameras to capture each demonstration from different angles, collecting 50 trajectories per task per camera-resulting in a total of 200 trajectories ...
- **Detected method headings:** 3 Method (p. 3); Method (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | 3.4 Loss functions Algorithm 1: memory bank sampling Input: t, {It-j / j = 0, 1, . . . , n -1}, ... | p. 5 (3 Method), p. 3 (3 Method) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Vision-language model backbone We leverage a pretrained large vision-language model (VLM) as the backbone, specifically InternVL-4B [12], which consists of a text ... | p. 3 (3 Method), p. 3 (3 Method) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Specifically, VLA with a low-level control policy refers to a class of models that use the current observations as input to predict ... | p. 3 (3 Method), p. 8 (Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3 Method - extractive PDF cue:** 3.4 Loss functions Algorithm 1: memory bank sampling Input: t, {It-j / j = 0, 1, . . . , n -1}, sample size k, ...
- **p. 5 / 3 Method - extractive PDF cue:** Our total training loss can be written as follows: L = Lt + Lr + Lg + λdLd, (3) where the translation loss Lt = ...
- **p. 3 / 3 Method - extractive PDF cue:** These multimodal tokens are then fed into the decoder D for next-token prediction.
- **p. 4 / 3 Method - extractive PDF cue:** 3.2 Spatial-aware visual tokens A reasonable action prediction requires awareness of both semantic perception and spatial perception of the scene.
- **p. 8 / Method - extractive PDF cue:** This task emphasizes the need for fine-grained action prediction.
- **p. 4 / 3 Method - extractive PDF cue:** Specifically, given current timestamp t, all image observations {It-j / j = 0, 1, 2, . . . , n-1} with a temporal window n, ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 5 (3 Method), p. 5 (3 Method), p. 4 (3 Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Specifically, VLA, low-level, control, policy, refers, class, models, current, observations, input, predict, action, robot | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Specifically, VLA, low-level, control, policy, refers, class, models, current, observations | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, D-VLA, efficient, VLA, model, integrates, spatial, module, vision, features | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Loss, functions, Algorithm, memory, bank, sampling, Input, It-j, sample, size | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 Method - extractive PDF cue:** Specifically, VLA with a low-level control policy refers to a class of models that use the current observations as input to predict an action for ...
- **p. 5 / 3 Method - extractive PDF cue:** 3.4 Loss functions Algorithm 1: memory bank sampling Input: t, {It-j / j = 0, 1, . . . , n -1}, sample size k, ...
- **p. 3 / 3 Method - extractive PDF cue:** 3.1 Preliminary Problem definition The vision-language action (VLA) model takes a language instruction as input and aims to control a robot to accomplish the specified ...
- **p. 4 / 3 Method - extractive PDF cue:** 𝑥 𝑦 𝑧 Spatial PE … Vision encoder … Sampled inputs LLM Transformer … … … Tokens from frame k Last hidden feature Tokens from ...
- **p. 2 / 1 Introduction - extractive PDF cue:** A real-world action distribution can be interpreted as a response function conditioned on observations or input, denoted as At(input).
- **p. 8 / Method - extractive PDF cue:** We set InternVL-4B with single RGB image inputs followed by an action head as our Base VLA model.
- **p. 2 / 1 Introduction - extractive PDF cue:** Previous approaches, such as OpenVLA [1], use only a single RGB image and a textual instruction as input.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | In long-horizon tasks (Task 2 and 4), the model often succeeds in the first step but fails the second without access to ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | To effectively exploit temporal information, we propose an adaptive historical frame sampling method based on a memory bank, aiming to capture rich ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | In long-horizon tasks (Task 2 and 4), the model often succeeds in the first step but fails the second without access to ... | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | We employed a cosine learning rate scheduler with a learning rate of 4e-5, using a batch size of 128 and training for ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / 3 Method - extractive PDF cue:** Vision-language model backbone We leverage a pretrained large vision-language model (VLM) as the backbone, specifically InternVL-4B [12], which consists of a text tokenizer T , ...
- **p. 8 / Method - extractive PDF cue:** We use 4 fixed cameras to capture each demonstration from different angles, collecting 50 trajectories per task per camera-resulting in a total of 200 trajectories ...
- **p. 7 / 4 Experiments - extractive PDF cue:** We employed a cosine learning rate scheduler with a learning rate of 4e-5, using a batch size of 128 and training for 20 epochs. λd ...
- **p. 6 / 4 Experiments - extractive PDF cue:** Our model was trained for 1 epoch with a batch size of 512, requiring around 20k steps to complete.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Loss, functions, Algorithm, memory, bank, sampling, Input, It-j, sample, size, feature, extractor, Output, sampled, timestamps, Initialize, Start, current, frame, Similarity.
- **Relevant PDF headings:** 3 Method (p. 3); Method (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | 4.1 Datasets and simulation environments DROID [2] A diverse real-world robot manipulation dataset with 76,000 demonstration trajectories, or 350 hours of interaction ... | p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Action / skill decoding | Our model significantly outperforms other competitors, with an average success rate 12.1 higher than OpenVLA. †Denotes no available standard deviation data. | p. 6 (4 Experiments), p. 7 (4 Experiments) |
| Receding execution / feedback | Our model significantly outperforms other competitors, with an average success rate 12.1 higher than OpenVLA. †Denotes no available standard deviation data. | p. 6 (4 Experiments), p. 7 (4 Experiments) |

## Failure and Ablation Link

- **p. 22 / Figure/Table caption - extractive PDF cue:** Table 7: Ablations on heads and inputs (Libero-Long). Left: action head vs. FPS and success (MLP, autoregressive, diffusion). Right: effect of pretraining, 3D coordinate embedding, ...
- **p. 22 / Figure/Table caption - extractive PDF cue:** Table 8: Frame sampling ablations on Libero-Spatial. MBS attains the highest success (0.866) with competitive efficiency, while single-frame is fastest and most memory-light but less ...
- **p. 6 / 4 Experiments - extractive PDF cue:** We remove frames with unchanged proprioception, specifically the stationary frames, and exclude trajectories with a total action count exceeding 600.
- **p. 7 / 4 Experiments - extractive PDF cue:** Unlike the pretraining phase, we used the simplest input settings to enable our model to learn the interaction effects between 3D information and historical data ...
- **p. 5 / 4 Experiments - extractive PDF cue:** We first introduce the datasets and simulation environment, then describe pretraining and fine-tuning.
- **p. 5 / 4 Experiments - extractive PDF cue:** Our model is pretrained on real-world data and fine-tuned with both simulation and real-world trajectories.
- **p. 7 / 4 Experiments - extractive PDF cue:** 4.3 LIBERO evaluation After pretraining, we fine-tune and conduct close-loop testing in the LIBERO simulation environment, using task success rate as the metric to evaluate ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3 Method), p. 3 (3 Method), p. 3 (3 Method), p. 8 (Method), p. 5 (3 Method), p. 4 (3 Method), objective p. 5 (3 Method), p. 5 (3 Method), p. 3 (3 Method), p. 4 (3 Method), p. 8 (Method), p. 4 (3 Method), temporal p. 8 (Method), p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (4 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
