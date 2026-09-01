# Method - RT-H: Action Hierarchies Using Language

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p049.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p049.html. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 1 (Abstract)): Motivated by the benefits of language motions, we propose an end-to-end framework, RT-H (Robot Transformer with Action Hierarchies), for learning these action hierarchies: at each step, RT-H conditions on the ...

## Method Body Digest

- **p. 2 / I. INTRODUCTION - extractive body cue:** Motivated by the benefits of language motions, we propose an end-to-end framework, RT-H (Robot Transformer with Action Hierarchies), for learning these action hierarchies: at each ...
- **p. 1 / Abstract - extractive body cue:** Our method RT-H builds an action hierarchy using language motions: it first learns to predict language motions, and conditioned on this along with the high-level ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Then RT-H uses the observation, the task, and the inferred language motion to predict the action for that step (action query), where the language motion ...
- **p. 1 / Abstract - extractive body cue:** Predicting these language motions as an intermediate step between high-level tasks and actions forces the policy to learn the shared structure of low-level motions across ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The advantage of language in these settings is to encode the shared structure between similar tasks (e.g., "pick coke can" vs. "pick an apple"), reducing ...
- **p. 1 / Abstract - extractive body cue:** Recent works in robot imitation learning have proposed learning language-conditioned policies that predict actions given visual observations and the high-level task specified in language.
- **p. 2 / I. INTRODUCTION - extractive body cue:** These works often share a common paradigm: given a high-level task described in language like "pick coke can", they learn policies that map observations and ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** Motivated by the benefits of language motions, we propose an end-to-end framework, RT-H (Robot Transformer with Action Hierarchies), for learning these action hierarchies: at each ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Creating such an action hierarchy leads to several benefits: (1) It enables much better data sharing between different tasks at the level of language motions, ...
- **p. 1 / Abstract - extractive body cue:** Our method RT-H builds an action hierarchy using language motions: it first learns to predict language motions, and conditioned on this along with the high-level ...

## Source Evidence Cues

- **p. 2 / I. INTRODUCTION - extractive body cue:** Motivated by the benefits of language motions, we propose an end-to-end framework, RT-H (Robot Transformer with Action Hierarchies), for learning these action hierarchies: at each ...
- **p. 1 / Abstract - extractive body cue:** Our method RT-H builds an action hierarchy using language motions: it first learns to predict language motions, and conditioned on this along with the high-level ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Then RT-H uses the observation, the task, and the inferred language motion to predict the action for that step (action query), where the language motion ...
- **p. 1 / Abstract - extractive body cue:** Predicting these language motions as an intermediate step between high-level tasks and actions forces the policy to learn the shared structure of low-level motions across ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | Motivated by the benefits of language motions, we propose an end-to-end framework, RT-H (Robot Transformer with Action Hierarchies), for learning these action ... | p. 2 (I. INTRODUCTION), p. 1 (Abstract) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Our method RT-H builds an action hierarchy using language motions: it first learns to predict language motions, and conditioned on this along ... | p. 1 (Abstract), p. 2 (I. INTRODUCTION) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Then RT-H uses the observation, the task, and the inferred language motion to predict the action for that step (action query), where ... | p. 2 (I. INTRODUCTION), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / I. INTRODUCTION - extractive body cue:** The advantage of language in these settings is to encode the shared structure between similar tasks (e.g., "pick coke can" vs. "pick an apple"), reducing ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Recent, works, robot, imitation, learning, have, language-conditioned, policies, predict, actions, given, visual, observations, high-level | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Recent, works, robot, imitation, learning, have, language-conditioned, policies, predict, actions | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | Motivated, benefits, language, motions, end-to-end, framework, RT-H, Robot, Transformer, Action | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | advantage, language, settings, encode, shared, structure, between, similar, tasks, pick | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive body cue:** Recent works in robot imitation learning have proposed learning language-conditioned policies that predict actions given visual observations and the high-level task specified in language.
- **p. 1 / Abstract - extractive body cue:** Predicting these language motions as an intermediate step between high-level tasks and actions forces the policy to learn the shared structure of low-level motions across ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** These works often share a common paradigm: given a high-level task described in language like "pick coke can", they learn policies that map observations and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Motivated by the benefits of language motions, we propose an end-to-end framework, RT-H (Robot Transformer with Action Hierarchies), for learning these action hierarchies: at each ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Thus to cheaply extract reliable language motions z at each time step in each episode, we develop an automated labeling scheme relying ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | However, this process doubles inference time since the two queries must be run sequentially at each time step. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 7 / V. EXPERIMENTS - extractive body cue:** In Table I, we report the minimum MSE across training checkpoints for RT-H, RT-H-Joint, and RT-2 when trained on either the Diverse+Kitchen dataset or the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Motivated, benefits, language, motions, end-to-end, framework, RT-H, Robot, Transformer, Action, Hierarchies, learning, step, conditions, observation, highlevel, task, description, predict, current.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We use RT-H trained on only the Kitchen dataset [6] unless otherwise noted (i.e., not including the Diverse data), which consists of ... | p. 10 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Action / skill decoding | Fig. 7: Results when models trained on Kitchen data [6] are deployed on the same tasks, but in a new building with ... | p. 11 (Figure/Table caption), p. 8 (V. EXPERIMENTS) |
| Receding execution / feedback | Fig. 3: Results on Diverse+Kitchen multi-task dataset, consisting of eight challenging evaluation tasks. 95% Wilson Score confidence intervals [54] are shown on ... | p. 6 (Figure/Table caption), p. 9 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / V. EXPERIMENTS - extractive body cue:** Offline Performance: We investigate if language motions as an intermediate layer for action prediction has any noticeable effect by comparing the offline validation mean squared ...
- **p. 7 / V. EXPERIMENTS - extractive body cue:** RTH-Cluster replaces the automating labeling procedure with action clustering, and without language it performs slightly worse than RT-H on average.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** See Appendix A for exact queries and a deeper dive into each RT-H variant implementation.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** Note that RT-H-Joint, RT-H-Cluster, and RT-H-OneHot are variants of RT-H that still utilize an action hierarchy.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** Training on Online Corrections In this section we are interested in how well RT-H can learn from language motion corrections compared to methods without action ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** 8 also shows the shared structure between seemingly diverse tasks: each of these tasks require some picking behavior to begin the task, and by learning ...
- **p. 9 / V. EXPERIMENTS - extractive body cue:** RT-HInterveneAction performs better than RT-H, but fine-tuning actions sometimes leads to policy degeneration, since actions produced by RT-H during intervention can be suboptimal. human decides ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 1 (Abstract), objective p. 2 (I. INTRODUCTION), temporal p. 4 (II. RELATED WORK), p. 5 (II. RELATED WORK), p. 5 (II. RELATED WORK), p. 2 (I. INTRODUCTION), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
