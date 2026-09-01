# Method - Learning to Act Anywhere with Task-centric Latent Actions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p014.html; PDF retrieval source: https://arxiv.org/pdf/2505.06111. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 4 (III. METHODOLOGY)): Drawing inspiration from the wellestablished Chain-of-Thought (CoT) reasoning paradigm [80] in large language models (LLMs), which generates intermediate reasoning steps to address complex tasks, we propose leveraging historical latent ...

## Method Body Digest

- **p. 5 / III. METHODOLOGY - extractive body cue:** Drawing inspiration from the wellestablished Chain-of-Thought (CoT) reasoning paradigm [80] in large language models (LLMs), which generates intermediate reasoning steps to address complex tasks, we ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** To mitigate the unfavorable effect of task-irrelevant dynamics, we incorporate readily available language instructions into the first training stage of latent action model (Fig.
- **p. 3 / III. METHODOLOGY - extractive body cue:** To derive latent actions from videos, our latent action model is constructed around an Inverse Dynamics Model (IDM) based encoder I(at/ot, ot+k) and a Forward ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** In Stage 2, a novel set of latent actions is introduced, specifically designed to replace the role of language and to capture task-centric dynamics from ...
- **p. 5 / III. METHODOLOGY - extractive body cue:** Specifically, the sequence of visual embeddings is first aggregated into a single token through multi-head attention pooling [43], which then functions as the query to ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Pretraining of Generalist Policy With the latent action model trained in the preceding step, we proceed to label any video frame ot with latent actions ...
- **p. 6 / 1) LIBERO-Spatial requires the policy to infer spatial - extractive body cue:** relationships to accurately place a bowl, evaluating the model's ability to reason about geometric configurations;
- **p. 3 / III. METHODOLOGY - extractive body cue:** Our selfsupervised objective minimizes the embedding reconstruction error: ∥ˆOt+k -Ot+k∥2.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, our main contributions are three-folds: • We propose UniVLA, a recipe towards generalist policy by planning in a unified, embodiment-agnostic action space, enabling ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To address these challenges, we propose UniVLA, a generalist policy learning framework that enables scalable and efficient planning across various embodiments and environments.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our recipe for generalist policy consists of three key stages: 1) Task-centric Latent Action Learning, where we extract task-relevant action representations from massive cross-embodiment videos ...

## Source Evidence Cues

- **p. 5 / III. METHODOLOGY - extractive body cue:** Drawing inspiration from the wellestablished Chain-of-Thought (CoT) reasoning paradigm [80] in large language models (LLMs), which generates intermediate reasoning steps to address complex tasks, we ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** To mitigate the unfavorable effect of task-irrelevant dynamics, we incorporate readily available language instructions into the first training stage of latent action model (Fig.
- **p. 3 / III. METHODOLOGY - extractive body cue:** To derive latent actions from videos, our latent action model is constructed around an Inverse Dynamics Model (IDM) based encoder I(at/ot, ot+k) and a Forward ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** In Stage 2, a novel set of latent actions is introduced, specifically designed to replace the role of language and to capture task-centric dynamics from ...
- **p. 5 / III. METHODOLOGY - extractive body cue:** Specifically, the sequence of visual embeddings is first aggregated into a single token through multi-head attention pooling [43], which then functions as the query to ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Pretraining of Generalist Policy With the latent action model trained in the preceding step, we proceed to label any video frame ot with latent actions ...
- **p. 6 / 1) LIBERO-Spatial requires the policy to infer spatial - extractive body cue:** relationships to accurately place a bowl, evaluating the model's ability to reason about geometric configurations;
- **Detected method headings:** III. METHODOLOGY (p. 3); 1) LIBERO-Spatial requires the policy to infer spatial (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Drawing inspiration from the wellestablished Chain-of-Thought (CoT) reasoning paradigm [80] in large language models (LLMs), which generates intermediate reasoning steps to address ... | p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | To mitigate the unfavorable effect of task-irrelevant dynamics, we incorporate readily available language instructions into the first training stage of latent action ... | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | To derive latent actions from videos, our latent action model is constructed around an Inverse Dynamics Model (IDM) based encoder I(at/ot, ot+k) ... | p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHODOLOGY - extractive body cue:** Our selfsupervised objective minimizes the embedding reconstruction error: ∥ˆOt+k -Ot+k∥2.
- **p. 5 / III. METHODOLOGY - extractive body cue:** The entire model is trained end-to-end, optimizing both the next-latent action prediction loss and the L1 loss between the ground-truth and predicted low-level actions.
- **p. 3 / III. METHODOLOGY - extractive body cue:** Quantized action tokens az ∈RN×d are optimized with VQ-VAE [76] objective, with a codebook of /C/ vocabulary size.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Specifically, our policy model πϕ receives observation ot, task instructions l and prefixes of latent action tokens az,<i, and is optimized to minimize the sum ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** 2 Right), where the objective is to learn a new set of task-centric latent actions ˆaTC upon which the policy is trained.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | III-B, train, auto-regressive, transformer-based, vision-language-action, model, takes, visual, observations, task, instructions, inputs, predict, latent | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | III-B, train, auto-regressive, transformer-based, vision-language-action, model, takes, visual, observations, task | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | summary, main, contributions, three-folds, UniVLA, recipe, towards, generalist, policy, planning | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | selfsupervised, objective, minimizes, embedding, reconstruction, error, entire, model, trained, end-to-end | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHODOLOGY - extractive body cue:** III-B) Based on this, we train an auto-regressive transformer-based vision-language-action model, which takes visual observations and task instructions as inputs to predict latent action tokens ...
- **p. 5 / III. METHODOLOGY - extractive body cue:** Our policy architecture is founded on the Prismatic-7B Vision-Language Model (VLM) [37], which processes projected visual embeddings and tokenized task instructions as inputs to predict ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Specifically, our policy model πϕ receives observation ot, task instructions l and prefixes of latent action tokens az,<i, and is optimized to minimize the sum ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** In Stage 2, a novel set of latent actions is introduced, specifically designed to replace the role of language and to capture task-centric dynamics from ...
- **p. 5 / III. METHODOLOGY - extractive body cue:** Drawing inspiration from the wellestablished Chain-of-Thought (CoT) reasoning paradigm [80] in large language models (LLMs), which generates intermediate reasoning steps to address complex tasks, we ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, our main contributions are three-folds: • We propose UniVLA, a recipe towards generalist policy by planning in a unified, embodiment-agnostic action space, enabling ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** To mitigate the unfavorable effect of task-irrelevant dynamics, we incorporate readily available language instructions into the first training stage of latent action model (Fig.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Pretraining of Generalist Policy With the latent action model trained in the preceding step, we proceed to label any video frame ot ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Much like LLMs resolve questions step-by-step, we incorporate past actions into the input prompt at each timestep during rollouts. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | At inference time, one step of historical latent action (encoded as N = 4 tokens) is incorporated at each timestep, with the ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / III. METHODOLOGY - extractive body cue:** To mitigate the unfavorable effect of task-irrelevant dynamics, we incorporate readily available language instructions into the first training stage of latent action model (Fig.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Pretraining of Generalist Policy With the latent action model trained in the preceding step, we proceed to label any video frame ot with latent actions ...
- **p. 5 / III. METHODOLOGY - extractive body cue:** At inference time, one step of historical latent action (encoded as N = 4 tokens) is incorporated at each timestep, with the exception of the ...
- **p. 7 / 2) Navigation Benchmark on Room2Room - extractive body cue:** It uses a pretrained vision encoder to encode visual observations and a pretrained LLM to predict actions.
- **p. 7 / 2) Navigation Benchmark on Room2Room - extractive body cue:** We introduce several special tokens to tokenize navigation actions and finetune the model on the R2R training split. • NaVid [91] is a video-based large ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Drawing, inspiration, wellestablished, Chain-of-Thought, CoT, reasoning, paradigm, large, language, models, LLMs, generates, intermediate, steps, address, complex, tasks, leveraging, historical, latent.
- **Relevant PDF headings:** III. METHODOLOGY (p. 3); 1) LIBERO-Spatial requires the policy to infer spatial (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | These benchmarks offer a set of languageguided navigation tasks and continuous environments for executing low-level actions in reconstructed photorealistic indoor scenes. | p. 7 (2) Navigation Benchmark on Room2Room), p. 6 (1) Manipulation Benchmark on LIBERO) |
| Action / skill decoding | Fig. 4: Task setup on the LIBERO benchmark. TABLE I: Results on LIBERO benchmark across four evaluation suites. Our proposed UniVLA exhibits ... | p. 6 (Figure/Table caption), p. 7 (2) Navigation Benchmark on Room2Room) |
| Receding execution / feedback | Fig. 6: Oracle success rate on R2R in VLN-CE. With only a single-frame RGB input, UniVLA demonstrates performance on par with NaVid, ... | p. 7 (Figure/Table caption), p. 7 (2) Navigation Benchmark on Room2Room) |

## Failure and Ablation Link

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We introduce UniVLA, a unified vision-language-action (VLA) framework that enables policy learning across different environments. By deriving task-centric latent actions in an unsupervised ...
- **p. 5 / IV. EVALUATIONS - extractive body cue:** Additionally, we conduct latent action analysis to quantify the task-centric property, and perform ablation studies to explore critical design choices.
- **p. 7 / 2) Navigation Benchmark on Room2Room - extractive body cue:** To ensure a fair comparison with UniVLA, we evaluate RGB-only methods that operate without depth or odometry data, directly predicting low-level actions within the VLN-CE ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Data scalability. UniVLA effectively expands its pretraining corpus by incorporating cross-embodiment data from OpenX and unlabeled human demonstrations, leading to continuously improved downstream ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 10: Data efficiency. We present the success rate of UniVLA across varying dataset proportions (10%, 20%, 50%, and the full dataset). Our policy can ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Task-centric latent action learning. We propose a two-stage training framework aimed at disentangling task-centric visual dynamics and changes from extraneous factors. In Stage ...
- **p. 6 / 1) Manipulation Benchmark on LIBERO - extractive body cue:** The pretraining details can be found in Sec.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), objective p. 3 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), temporal p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
