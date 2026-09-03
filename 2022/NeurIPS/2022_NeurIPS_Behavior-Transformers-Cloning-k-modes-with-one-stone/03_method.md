# Method - Behavior Transformers: Cloning k modes with one stone

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2022/hash/90d17e882adbdda42349db6f50123817-Abstract-Conference.html; PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2022/hash/90d17e882adbdda42349db6f50123817-Abstract-Conference.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction)): We use a transformer decoder model, namely minGPT [11], with minor modifications, as our backbone.

## Method Body Digest

- **p. 4 / 1 Introduction - extractive body cue:** We use a transformer decoder model, namely minGPT [11], with minor modifications, as our backbone.
- **p. 3 / 1 Introduction - extractive body cue:** To operationalize these two features in a single behavior model, we make use of transformers since (a) they are effective in utilizing prior observational history, ...
- **p. 4 / 1 Introduction - extractive body cue:** (C) Rollouts from BeT in test time, where it first chooses a bin and then picks the corresponding offset to reconstruct a continuous action. distributions ...
- **p. 2 / 1 Introduction - extractive body cue:** First, we leverage the context based multi-token prediction ability of transformer-based sequence models [78] to predict multimodal actions.
- **p. 3 / 1 Introduction - extractive body cue:** 2 Behavior Transformers Given a dataset of continuous observation and action pairs D ⌘{(o, a)} ⇢O ⇥A that contains behaviors we are interested in, our ...
- **p. 5 / 1 Introduction - extractive body cue:** To predict the complete continuous action, we add an extra head to the transformer decoder that offsets the discretized action centers based on the observations.
- **p. 1 / Abstract - extractive body cue:** This allows us to leverage the multi-modal modeling ability of modern transformers to predict multi-modal continuous actions.
- **p. 3 / 1 Introduction - extractive body cue:** Following this convention, our objective is to find the parameter ✓that maximizes the probability of the observed data ✓⇤:= arg max ✓ Y t P(at ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we present Behavior Transformers (BeT), a new method for learning behaviors from rich, distributionally multi-modal data.
- **p. 4 / 1 Introduction - extractive body cue:** To address this, we propose a new factoring of the action prediction task by dividing each action in two parts: a categorical variable denoting an ...
- **p. 1 / Abstract - extractive body cue:** In this work, we present Behavior Transformer (BeT), a new technique to model unlabeled demonstration data with multiple modes.

## Source Evidence Cues

- **p. 4 / 1 Introduction - extractive body cue:** We use a transformer decoder model, namely minGPT [11], with minor modifications, as our backbone.
- **p. 3 / 1 Introduction - extractive body cue:** To operationalize these two features in a single behavior model, we make use of transformers since (a) they are effective in utilizing prior observational history, ...
- **p. 4 / 1 Introduction - extractive body cue:** (C) Rollouts from BeT in test time, where it first chooses a bin and then picks the corresponding offset to reconstruct a continuous action. distributions ...
- **p. 2 / 1 Introduction - extractive body cue:** First, we leverage the context based multi-token prediction ability of transformer-based sequence models [78] to predict multimodal actions.
- **p. 3 / 1 Introduction - extractive body cue:** 2 Behavior Transformers Given a dataset of continuous observation and action pairs D ⌘{(o, a)} ⇢O ⇥A that contains behaviors we are interested in, our ...
- **p. 5 / 1 Introduction - extractive body cue:** To predict the complete continuous action, we add an extra head to the transformer decoder that offsets the discretized action centers based on the observations.
- **p. 1 / Abstract - extractive body cue:** This allows us to leverage the multi-modal modeling ability of modern transformers to predict multi-modal continuous actions.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Demonstration representation | expert trajectory를 training pair/context로 정렬한다 | observation history, goal, expert action | temporal alignment, relabeling 또는 latent context construction을 수행 | training sample/context | We use a transformer decoder model, namely minGPT [11], with minor modifications, as our backbone. | p. 4 (1 Introduction), p. 3 (1 Introduction) |
| Policy fitting | expert action distribution을 학습한다 | context와 action target | behavior cloning, adversarial, sequence, diffusion 또는 flow objective를 최적화 | policy/action distribution | To operationalize these two features in a single behavior model, we make use of transformers since (a) they are effective in utilizing ... | p. 3 (1 Introduction), p. 4 (1 Introduction) |
| Closed-loop rollout | distribution shift와 recovery를 확인한다 | current observation/history | action/chunk을 실행하고 feedback으로 다음 prediction을 갱신 | trajectory/failure signal | (C) Rollouts from BeT in test time, where it first chooses a bin and then picks the corresponding offset to reconstruct a ... | p. 4 (1 Introduction), p. 2 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 1 Introduction - extractive body cue:** Following this convention, our objective is to find the parameter ✓that maximizes the probability of the observed data ✓⇤:= arg max ✓ Y t P(at ...
- **p. 4 / 1 Introduction - extractive body cue:** While the standard cross entropy loss for binary classification can be thought of Lce(pt) = -log(pt), Focal loss adds a term (1 -pt)γ to this, ...
- **p. 4 / 1 Introduction - extractive body cue:** Focal loss is a simple modification over the standard cross entropy loss.
- **p. 1 / 1 Introduction - extractive body cue:** However, such methods have yet to tackle domains where task-specific reward labels are not present.
- **p. 1 / Abstract - extractive body cue:** Human behaviors have wide variance, multiple modes, and human demonstrations typically do not come with reward labels.
- **p. 3 / 1 Introduction - extractive body cue:** The MSE-BC model takes 0 action to minimize MSE.
- **Formal bridge:** observation history o_{t−H:t} -> expert-like action/chunk a_{t:t+H} -> imitation or action-distribution loss -> closed-loop task success and robustness.
- **Equation/algorithm anchors:** p. 4 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 5 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Behavior, Transformers, Given, dataset, continuous, observation, action, pairs, contains, behaviors, interested, goal, learn, policy | observation history와 expert trajectory/action | body cue; exact tensor/frame verify |
| State/latent | Behavior, Transformers, Given, dataset, continuous, observation, action, pairs, contains, behaviors | behavior policy와 temporal action context | body cue; notation verify |
| Action/output | present, Behavior, Transformers, BeT, learning, behaviors, rich, distributionally, multi-modal, data | predicted action 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | Following, convention, objective, find, parameter, maximizes, probability, observed, data, When | imitation or action-distribution loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1 Introduction - extractive body cue:** 2 Behavior Transformers Given a dataset of continuous observation and action pairs D ⌘{(o, a)} ⇢O ⇥A that contains behaviors we are interested in, our ...
- **p. 5 / 1 Introduction - extractive body cue:** For each observation oi in the sequence, the head produces a k ⇥dim(A) matrix with k proposed residual action vectors, ⇣ ha(j) i i ⌘k ...
- **p. 1 / 1 Introduction - extractive body cue:** Without priors on how to behave, state-of-the-art RL methods require online interactions on the order of 1-10M ‘reward-labeled' samples for benchmark control tasks [81].
- **p. 3 / 1 Introduction - extractive body cue:** To operationalize these two features in a single behavior model, we make use of transformers since (a) they are effective in utilizing prior observational history, ...
- **p. 4 / 1 Introduction - extractive body cue:** The transformer T takes in a sequence of continuous observations (oi, oi+1, · · · , oi+h-1) and learns a sequence-to-sequence model mapping each observation ...
- **p. 4 / 1 Introduction - extractive body cue:** Continuous action binning MinGPT Observation Sequence 0.4 0.1 0.0 0.5 0.0 Per-class action offsets (k x a) Bin probs (1 x k) Ground truth action ...
- **p. 5 / 1 Introduction - extractive body cue:** To predict the complete continuous action, we add an extra head to the transformer decoder that offsets the discretized action centers based on the observations.
- **Normalized interface:** observation=observation history와 expert trajectory/action; state=behavior policy와 temporal action context; output/action=predicted action 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single-step 또는 action chunk/trajectory horizon; exact chunk length는 exact value was not selected from the PDF body. | The participants completed a sequence of four object-interaction tasks in each episode [34]. | episode/sequence/action-chunk boundary |
| Rate / latency | training inference와 deployed control tick을 분리; action chunk면 receding execution 여부 확인. | Each task is colored differently, and frequency is shown out of a 1,000 unconditional rollouts from the models. | Hz/fps, inference time and control rate |
| Memory | current observation, temporal history 또는 recurrent/sequence context. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | backbone/decoder inference, sampling steps와 action horizon이 latency를 결정한다. | Our models contain on the order of 104-106 parameters, and even with a small batch size trains within an hour for our ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 1 Introduction - extractive body cue:** (C) Rollouts from BeT in test time, where it first chooses a bin and then picks the corresponding offset to reconstruct a continuous action. distributions ...
- **p. 9 / 3 Experiments - extractive body cue:** Our models contain on the order of 104-106 parameters, and even with a small batch size trains within an hour for our largest datasets (Block ...
- **p. 5 / 3 Experiments - extractive body cue:** For visual observations with BeT, we use a frozen ResNet-18 [36] pretrained on ImageNet [18] as an encoder.
- **p. 3 / 1 Introduction - extractive body cue:** All of our datasets, code, and trained models will be made publicly available.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** transformer, decoder, model, namely, minGPT, minor, modifications, backbone, operationalize, features, single, behavior, make, transformers, since, they, effective, utilizing, prior, observational.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Demonstration representation | 3.1 Environments and datasets We experiment with five broad environments. | p. 5 (3 Experiments), p. 5 (3 Experiments) |
| Policy fitting | Figure 5: Comparison between an RBC model and two BeT models, trained with and without historical context on a dataset with three ... | p. 8 (Figure/Table caption), p. 6 (3 Experiments) |
| Closed-loop rollout | Figure 1: Unconditional rollouts from BeT models trained from multi-modal demonstartions on the CARLA, Block push, and Franka Kitchen environments. Due to ... | p. 2 (Figure/Table caption), p. 6 (3 Experiments) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Relative performance of ablated variants of BeT, normalized by average BeT successes at the task Ablations CARLA Block push Kitchen No offsets 0.94
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Comparison between an RBC model and two BeT models, trained with and without historical context on a dataset with three distinct modes. BeT ...
- **p. 5 / 3 Experiments - extractive body cue:** (c) How important are the individual components of BeT?
- **p. 5 / 3 Experiments - extractive body cue:** For visual observations with BeT, we use a frozen ResNet-18 [36] pretrained on ImageNet [18] as an encoder.
- **p. 6 / 3 Experiments - extractive body cue:** Since the models are all behavioral cloning algorithms, they share the failure mode of failing once the observations go out of distribution (OOD).
- **p. 6 / 3 Experiments - extractive body cue:** On the other hand, we observe that BeT's primary failure mode is not realizing a block has not completely entered the target yet, while other ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Comparison between a regular MSE-based BC model and a BeT models that can capture multi-modal distributions. The MSE-BC model takes 0 action to ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction), objective p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction), temporal p. 6 (3 Experiments), p. 7 (3 Experiments), p. 7 (3 Experiments), p. 8 (3 Experiments), p. 2 (1 Introduction), p. 6 (3 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** 2 Behavior Transformers Given a dataset of continuous observation and action pairs D ⌘{(o, a)} ⇢O ⇥A that contains behaviors we are interested in, our goal is to learn a ... (p. 3, 1 Introduction).
- **Objective/update evidence:** While the standard cross entropy loss for binary classification can be thought of Lce(pt) = -log(pt), Focal loss adds a term (1 -pt)γ to this, to make the new loss ... (p. 4, 1 Introduction).
- **Temporal/runtime evidence:** The participants completed a sequence of four object-interaction tasks in each episode [34]. (p. 6, 3 Experiments).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
