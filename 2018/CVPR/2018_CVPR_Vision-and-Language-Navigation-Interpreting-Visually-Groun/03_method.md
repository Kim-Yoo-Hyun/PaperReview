# Method - Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1711.07280; PDF retrieval source: https://arxiv.org/pdf/1711.07280. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (5.1. Sequence-to-Sequence Model), p. 6 (5.1. Sequence-to-Sequence Model), p. 7 (5.1. Sequence-to-Sequence Model), p. 7 (5.2. Training)): At each step t, the decoder observes representations of the current image ot and the previous action at-1 as input, applies an attention mechanism to the hidden states of the ...

## Method Body Digest

- **p. 6 / 5.1. Sequence-to-Sequence Model - extractive PDF cue:** At each step t, the decoder observes representations of the current image ot and the previous action at-1 as input, applies an attention mechanism to ...
- **p. 6 / 5.1. Sequence-to-Sequence Model - extractive PDF cue:** Image and action embedding For each image observation ot, we use a ResNet-152 [22] CNN pretrained on ImageNet [46] to extract a mean-pooled feature vector.
- **p. 7 / 5.1. Sequence-to-Sequence Model - extractive PDF cue:** When then compute an attentional hidden state ˜ht = tanh (Wc[ct; h ′ t]), and calculate the predictive distribution over the next action as at ...
- **p. 7 / 5.2. Training - extractive PDF cue:** We use dropout of 0.5 on embeddings, CNN features and within the attention model.
- **p. 7 / 5.2. Training - extractive PDF cue:** In both cases, we use cross entropy loss at each step to maximize the likelihood of the ground-truth target action a∗ t given the previous ...
- **p. 7 / 5.2. Training - extractive PDF cue:** We train in PyTorch using the Adam optimizer [28] with weight decay and a batch size of 100.
- **p. 6 / 5.1. Sequence-to-Sequence Model - extractive PDF cue:** Action prediction with attention mechanism To predict a distribution over actions at step t, we first use an attention mechanism to identify the most relevant ...
- **p. 2 / 1. Introduction - extractive PDF cue:** However, VLN sequences are much longer and, uniquely among vision and language benchmark tasks using real images, the model outputs actions ⟨a0, a1, . . ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** To enable the reproducible evaluation of VLN methods, we present the Matterport3D Simulator.
- **p. 2 / 1. Introduction - extractive PDF cue:** We introduce the Matterport3D Simulator, a software framework for visual reinforcement learning using the Matterport3D panoramic RGB-D dataset [11]; 2.
- **p. 1 / 1. Introduction - extractive PDF cue:** The dataset particularly has been designed to simplify the application of vision and language methods to what might otherwise seem a distant problem.

## Source Evidence Cues

- **p. 6 / 5.1. Sequence-to-Sequence Model - extractive PDF cue:** At each step t, the decoder observes representations of the current image ot and the previous action at-1 as input, applies an attention mechanism to ...
- **p. 6 / 5.1. Sequence-to-Sequence Model - extractive PDF cue:** Image and action embedding For each image observation ot, we use a ResNet-152 [22] CNN pretrained on ImageNet [46] to extract a mean-pooled feature vector.
- **p. 7 / 5.1. Sequence-to-Sequence Model - extractive PDF cue:** When then compute an attentional hidden state ˜ht = tanh (Wc[ct; h ′ t]), and calculate the predictive distribution over the next action as at ...
- **p. 7 / 5.2. Training - extractive PDF cue:** We use dropout of 0.5 on embeddings, CNN features and within the attention model.
- **Detected method headings:** 5.1. Sequence-to-Sequence Model (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | At each step t, the decoder observes representations of the current image ot and the previous action at-1 as input, applies an ... | p. 6 (5.1. Sequence-to-Sequence Model), p. 6 (5.1. Sequence-to-Sequence Model) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | Image and action embedding For each image observation ot, we use a ResNet-152 [22] CNN pretrained on ImageNet [46] to extract a ... | p. 6 (5.1. Sequence-to-Sequence Model), p. 7 (5.1. Sequence-to-Sequence Model) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | When then compute an attentional hidden state ˜ht = tanh (Wc[ct; h ′ t]), and calculate the predictive distribution over the next ... | p. 7 (5.1. Sequence-to-Sequence Model), p. 7 (5.2. Training) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / 5.2. Training - extractive PDF cue:** In both cases, we use cross entropy loss at each step to maximize the likelihood of the ground-truth target action a∗ t given the previous ...
- **p. 7 / 5.2. Training - extractive PDF cue:** We train in PyTorch using the Adam optimizer [28] with weight decay and a batch size of 100.
- **p. 6 / 5.1. Sequence-to-Sequence Model - extractive PDF cue:** Action prediction with attention mechanism To predict a distribution over actions at step t, we first use an attention mechanism to identify the most relevant ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 7 (5.2. Training).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | step, decoder, observes, representations, current, image, previous, action, at-1, input, applies, attention, mechanism, hidden | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | step, decoder, observes, representations, current, image, previous, action, at-1, input | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | enable, reproducible, evaluation, VLN, methods, present, Matterport3D, Simulator, introduce, software | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | cases, cross, entropy, loss, step, maximize, likelihood, ground-truth, target, action | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 5.1. Sequence-to-Sequence Model - extractive PDF cue:** At each step t, the decoder observes representations of the current image ot and the previous action at-1 as input, applies an attention mechanism to ...
- **p. 2 / 1. Introduction - extractive PDF cue:** However, VLN sequences are much longer and, uniquely among vision and language benchmark tasks using real images, the model outputs actions ⟨a0, a1, . . ...
- **p. 6 / 5.1. Sequence-to-Sequence Model - extractive PDF cue:** Recall that the agent begins with a natural language instruction ¯x = ⟨x1, x2, . . . xL⟩, and an initial image observation o0.
- **p. 7 / 5.2. Training - extractive PDF cue:** The target output action a∗ t is always defined as the next action in the groundtruth shortest-path trajectory from the agent's current pose st = ...
- **p. 7 / 5.2. Training - extractive PDF cue:** In this approach, at each step the next action is sampled from the agent's output probability distribution.
- **p. 1 / 1. Introduction - extractive PDF cue:** Although interpreting natural-language navigation instructions has received significant attention previously [12, 13, 20, 38, 41, 52], it is the recent success of recurrent neural network ...
- **p. 2 / 1. Introduction - extractive PDF cue:** As illustrated in Figure 1, the associated task requires an agent to follow natural-language instructions to navigate to a goal location in a previously unseen ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | We consider an episode to be a success if the navigation error is less than 3m. | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | Central to our evaluation is the requirement for the agent to choose to end the episode when the goal location is identified. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 5.1. Sequence-to-Sequence Model - extractive PDF cue:** Image and action embedding For each image observation ot, we use a ResNet-152 [22] CNN pretrained on ImageNet [46] to extract a mean-pooled feature vector.
- **p. 7 / 5.2. Training - extractive PDF cue:** We train in PyTorch using the Adam optimizer [28] with weight decay and a batch size of 100.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** step, decoder, observes, representations, current, image, previous, action, at-1, input, applies, attention, mechanism, hidden, states, language, encoder, predicts, distribution, over.
- **Relevant PDF headings:** 5.1. Sequence-to-Sequence Model (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | These datasets typically offer only one or two paths through a scene, making them inadequate for simulating robot motion. | p. 3 (3.1. Matterport3D Dataset), p. 3 (3.1. Matterport3D Dataset) |
| Baseline harness | To disentangle the problem of recognizing the goal location, we also report success for each agent under an oracle stopping rule, i.e. ... | p. 6 (4.4. Evaluation Protocol), p. 8 (6. Results) |
| Metric / failure reporting | As illustrated in Table 1, our exploitative RANDOM agent achieves an average success rate of 13.2% on the test set (which appears ... | p. 7 (6. Results), p. 8 (6. Results) |

## Failure and Ablation Link

- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Example navigation graph for a partial floor of one building-scale scene in the Matterport3D Simulator. Navigable paths between panoramic viewpoints are illustrated in ...
- **p. 7 / 6. Results - extractive PDF cue:** Nevertheless, people are not infallible when it comes to navigation.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (5.1. Sequence-to-Sequence Model), p. 6 (5.1. Sequence-to-Sequence Model), p. 7 (5.1. Sequence-to-Sequence Model), p. 7 (5.2. Training), objective p. 7 (5.2. Training), p. 7 (5.2. Training), p. 6 (5.1. Sequence-to-Sequence Model), temporal p. 6 (4.4. Evaluation Protocol), p. 6 (4.4. Evaluation Protocol), p. 7 (5.2. Training), p. 7 (5.2. Training), p. 1 (Abstract), p. 2 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
