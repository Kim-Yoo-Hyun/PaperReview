# Method - A Generalist Agent

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (42 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2205.06175; PDF retrieval source: https://arxiv.org/abs/2205.06175. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (1 Introduction), p. 3 (1 Introduction), p. 2 (Abstract), p. 3 (1 Introduction), p. 2 (Abstract), p. 7 (1 Introduction)): The training loss for a batch B can then be written as L(θ, B) = - /B/ X b=1 L X l=1 m (b, l) log pθ  s(b) l ...

## Method Body Digest

- **p. 4 / 1 Introduction - extractive body cue:** The training loss for a batch B can then be written as L(θ, B) = - /B/ X b=1 L X l=1 m (b, l) ...
- **p. 3 / 1 Introduction - extractive body cue:** After converting data into tokens, we use the following canonical sequence ordering. • Text tokens in the same order as the raw input text. • ...
- **p. 2 / Abstract - extractive body cue:** Masking is used such that the loss function is applied only to target outputs, i.e. text and various actions.
- **p. 3 / 1 Introduction - extractive body cue:** Below we report the tokenization scheme we found to produce the best results for Gato at the current scale using contemporary hardware and model architectures. ...
- **p. 2 / Abstract - extractive body cue:** Data from different tasks and modalities is serialized into a flat sequence of tokens, batched, and processed by a transformer neural network akin to a ...
- **p. 7 / 1 Introduction - extractive body cue:** We used several sources of training data for these tasks.
- **p. 7 / 1 Introduction - extractive body cue:** The environment consists of a Sawyer robot arm with 3-DoF cartesian velocity control, an additional DoF for velocity, and a discrete gripper action.
- **p. 3 / 1 Introduction - extractive body cue:** In the following subsections, we describe Gato's tokenization, network architecture, loss function, and deployment.

## Design Rationale

- **p. 4 / 1 Introduction - extractive body cue:** During evaluation, the agent can be prompted using a successful demonstration of the desired task, which we do by default in all control results that ...
- **p. 6 / 1 Introduction - extractive body cue:** ALIGN (Jia et al., 2021) consists of 1.8B images and their alternative text (alt-text) annotations.
- **p. 6 / 1 Introduction - extractive body cue:** LTIP (Long Text & Image Pairs), consists of 312 million images with captions (Alayrac et al., 2022).

## Source Evidence Cues

- **p. 4 / 1 Introduction - extractive body cue:** The training loss for a batch B can then be written as L(θ, B) = - /B/ X b=1 L X l=1 m (b, l) ...
- **p. 3 / 1 Introduction - extractive body cue:** After converting data into tokens, we use the following canonical sequence ordering. • Text tokens in the same order as the raw input text. • ...
- **p. 2 / Abstract - extractive body cue:** Masking is used such that the loss function is applied only to target outputs, i.e. text and various actions.
- **p. 3 / 1 Introduction - extractive body cue:** Below we report the tokenization scheme we found to produce the best results for Gato at the current scale using contemporary hardware and model architectures. ...
- **p. 2 / Abstract - extractive body cue:** Data from different tasks and modalities is serialized into a flat sequence of tokens, batched, and processed by a transformer neural network akin to a ...
- **p. 7 / 1 Introduction - extractive body cue:** We used several sources of training data for these tasks.
- **p. 7 / 1 Introduction - extractive body cue:** The environment consists of a Sawyer robot arm with 3-DoF cartesian velocity control, an additional DoF for velocity, and a discrete gripper action.
- **Detected method headings:** A Model card (p. 28); C Model Architecture (p. 33)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | The training loss for a batch B can then be written as L(θ, B) = - /B/ X b=1 L X l=1 ... | p. 4 (1 Introduction), p. 3 (1 Introduction) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | After converting data into tokens, we use the following canonical sequence ordering. • Text tokens in the same order as the raw ... | p. 3 (1 Introduction), p. 2 (Abstract) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Masking is used such that the loss function is applied only to target outputs, i.e. text and various actions. | p. 2 (Abstract), p. 3 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / Abstract - extractive body cue:** Masking is used such that the loss function is applied only to target outputs, i.e. text and various actions.
- **p. 3 / 1 Introduction - extractive body cue:** In the following subsections, we describe Gato's tokenization, network architecture, loss function, and deployment.
- **p. 4 / 1 Introduction - extractive body cue:** Targets for these non-predicted tokens are set to an unused value and their contribution to the loss is masked out.
- **p. 4 / 1 Introduction - extractive body cue:** The training loss for a batch B can then be written as L(θ, B) = - /B/ X b=1 L X l=1 m (b, l) ...
- **p. 5 / 1 Introduction - extractive body cue:** For each environment we record a subset of the experience the agent generates (states, actions, and rewards) while it is training.
- **p. 8 / 1 Introduction - extractive body cue:** However, such demonstrations are slow and costly to collect.
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 2 (Abstract), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 6 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Embedding, input, tokens, setting, output, targets, After, tokenization, sequencing, apply, parameterized, function, token, applied | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Embedding, input, tokens, setting, output, targets, After, tokenization, sequencing, apply | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | During, evaluation, agent, prompted, successful, demonstration, desired, task, default, control | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Masking, loss, function, applied, only, target, outputs, text, various, actions | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1 Introduction - extractive body cue:** 2.2 Embedding input tokens and setting output targets After tokenization and sequencing, we apply a parameterized embedding function f(·; θe) to each token (i.e. it ...
- **p. 3 / 1 Introduction - extractive body cue:** After converting data into tokens, we use the following canonical sequence ordering. • Text tokens in the same order as the raw input text. • ...
- **p. 2 / Abstract - extractive body cue:** A: It's a cute cat Images and questions Text Images, proprioception and continuous actions Images and questions Atari images and discrete actions 0 1 0 ...
- **p. 5 / 1 Introduction - extractive body cue:** The simulated environments include Meta-World (Yu et al., 2020) introduced to benchmark metareinforcement learning and multi-task learning, Sokoban (Racanière et al., 2017) proposed as a ...
- **p. 1 / Abstract - extractive body cue:** Gato was trained on 604 distinct tasks with varying modalities, observations and action specifications.
- **p. 2 / Abstract - extractive body cue:** Masking is used such that the loss function is applied only to target outputs, i.e. text and various actions.
- **p. 4 / 1 Introduction - extractive body cue:** Because distinct tasks within a domain can share identical embodiments, observation formats and action specifications, the model sometimes needs further context to disambiguate tasks.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | After converting data into tokens, we use the following canonical sequence ordering. • Text tokens in the same order as the raw ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Episodes have a fixed length of 400 timesteps at 20 Hz for a total of 20 seconds, and at the end of ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | Hence for certain environments only a short chunk of a demonstration episode fits in the transformer memory. | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | Episodes have a fixed length of 400 timesteps at 20 Hz for a total of 20 seconds, and at the end of ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 1 Introduction - extractive body cue:** The training loss for a batch B can then be written as L(θ, B) = - /B/ X b=1 L X l=1 m (b, l) ...
- **p. 7 / 1 Introduction - extractive body cue:** We used several sources of training data for these tasks.
- **p. 4 / 1 Introduction - extractive body cue:** Training of the model is performed on a 16x16 TPU v3 slice for 1M steps with batch size 512 and token sequence length L = ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** training, loss, batch, then, written, described, above, Gato, network, architecture, main, components, parameterized, embedding, function, transforms, tokens, token, embeddings, sequence.
- **Relevant PDF headings:** A Model card (p. 28); C Model Architecture (p. 33).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | However, the Skill Mastery allows the agent to train on data involving the object shapes used for evaluation, i.e. the test set ... | p. 14 (1 Introduction), p. 14 (1 Introduction) |
| Action / skill decoding | Figure 10: Robotics fine-tuning results. Left: Comparison of real robot Skill Generalization success rate averaged across test triplets for Gato, expert, and ... | p. 12 (Figure/Table caption), p. 39 (Figure/Table caption) |
| Receding execution / feedback | The specialist Atari agent outperforms our generalist agent Gato, which achieved super-human performance on 23 games. | p. 14 (1 Introduction), p. 14 (1 Introduction) |

## Failure and Ablation Link

- **p. 39 / Figure/Table caption - extractive body cue:** Figure 19: Few-shot performance of Gato for Skill Generalization in simulation. Each test set object is plotted separately. We ablate over different pretraining datasets. I ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 10: Robotics fine-tuning results. Left: Comparison of real robot Skill Generalization success rate averaged across test triplets for Gato, expert, and CRR trained on ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 11: Comparing training/test task goal variations. Top: the standard "stack red on blue" task tested in the Skill Generalization benchmark. Bottom: the novel "stack ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 9: Few-shot performance, ablating over various pretraining settings. Orange corresponds to the base Gato pretrained on all data. Red is trained from scratch only ...
- **p. 14 / 1 Introduction - extractive body cue:** Both of them were trained on data from a single domain only and rolled out 500 times for each training task without any per-task fine-tuning.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6: Image captions generated by Gato. Gato prompted to be an image captioner, describing the first several held-out images from MS-COCO. We report the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Gato's performance on simulated control tasks. Number of tasks where the performance of the pretrained model is above a percentage of expert score, ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (1 Introduction), p. 3 (1 Introduction), p. 2 (Abstract), p. 3 (1 Introduction), p. 2 (Abstract), p. 7 (1 Introduction), objective p. 2 (Abstract), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 8 (1 Introduction), temporal p. 3 (1 Introduction), p. 7 (1 Introduction), p. 19 (6 Related Work), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 6 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
