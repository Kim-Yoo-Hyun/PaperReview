# Method - Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2303.18240; PDF retrieval source: https://arxiv.org/abs/2303.18240. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 16 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 16 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 18 (A.6 Scaling Hypothesis Pretraining Details), p. 18 (A.6 Scaling Hypothesis Pretraining Details)): We use patch representations for ViT-based PVRs and grid-features from last convolutional layer for ResNet models, passed through a compression layer [14] for a lower dimensional representation for use by ...

## Method Body Digest

- **p. 16 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** We use patch representations for ViT-based PVRs and grid-features from last convolutional layer for ResNet models, passed through a compression layer [14] for a lower ...
- **p. 16 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** When using vision transformers (ViT) based PVRs, we use the [CLS] token as input to the policy, and with ResNets we use features from the ...
- **p. 17 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** For Reach-Cube, the state for the BC policy is [xft t , zt], where xft t is the current fingertip position and zt is the ...
- **p. 17 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** Specifically, we used a learning rate of 10-4 for the visual encoder and 10-3 for all other elements, with the AdamW optimizer.
- **p. 18 / A.6 Scaling Hypothesis Pretraining Details - extractive body cue:** However, we do vary the number of epochs we use to train the different models in Section 5 given the different dataset sizes.
- **p. 18 / A.6 Scaling Hypothesis Pretraining Details - extractive body cue:** To train the MAE models, we use the official codebase released by the authors on GitHub [18] and use the default hyperparameters provided by the ...
- **p. 19 / A.8 Additional Analysis of All Models Evaluated on CORTEXBENCH - extractive body cue:** Similarly, Table 8 provides results for all models evaluated in this study is collected.
- **p. 17 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** We train agents with the reward functions presented in [67] utilizing the following settings: success weighting cs = 5.0, angle success weighting ca = 5.0, ...

## Design Rationale

- **p. 1 / 1 Introduction - extractive body cue:** The visual cortex is a region of an organism's brain, which together with the motor cortex, enables sight to be converted into movement.
- **p. 1 / 1 Introduction - extractive body cue:** In this work, we ask the same question that Fukushima [1, 2] asked nearly 50 years ago - how do we design an artificial visual ...
- **p. 2 / 1 Introduction - extractive body cue:** The exhaustiveness of this study enables us to draw conclusions with unprecedented scope and confidence.

## Source Evidence Cues

- **p. 16 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** We use patch representations for ViT-based PVRs and grid-features from last convolutional layer for ResNet models, passed through a compression layer [14] for a lower ...
- **p. 16 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** When using vision transformers (ViT) based PVRs, we use the [CLS] token as input to the policy, and with ResNets we use features from the ...
- **p. 17 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** For Reach-Cube, the state for the BC policy is [xft t , zt], where xft t is the current fingertip position and zt is the ...
- **p. 17 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** Specifically, we used a learning rate of 10-4 for the visual encoder and 10-3 for all other elements, with the AdamW optimizer.
- **p. 18 / A.6 Scaling Hypothesis Pretraining Details - extractive body cue:** However, we do vary the number of epochs we use to train the different models in Section 5 given the different dataset sizes.
- **p. 18 / A.6 Scaling Hypothesis Pretraining Details - extractive body cue:** To train the MAE models, we use the official codebase released by the authors on GitHub [18] and use the default hyperparameters provided by the ...
- **p. 19 / A.8 Additional Analysis of All Models Evaluated on CORTEXBENCH - extractive body cue:** Similarly, Table 8 provides results for all models evaluated in this study is collected.
- **Detected method headings:** A.2 Overview of Downstream Policy Learning in CORTEXBENCH (p. 16); A.8 Additional Analysis of All Models Evaluated on CORTEXBENCH (p. 19); A.9 Additional Analysis of Scaling Model Size (p. 19)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | We use patch representations for ViT-based PVRs and grid-features from last convolutional layer for ResNet models, passed through a compression layer [14] ... | p. 16 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 16 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | When using vision transformers (ViT) based PVRs, we use the [CLS] token as input to the policy, and with ResNets we use ... | p. 16 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | For Reach-Cube, the state for the BC policy is [xft t , zt], where xft t is the current fingertip position and ... | p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 17 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** We train agents with the reward functions presented in [67] utilizing the following settings: success weighting cs = 5.0, angle success weighting ca = 5.0, ...
- **p. 18 / A.6 Scaling Hypothesis Pretraining Details - extractive body cue:** We choose the number of epochs per run such that the number of model updates remain constant across all runs and match the number of ...
- **p. 17 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** Unless otherwise specified, we use a learning rate of 2.5 × 10-4 for training the agents and update the parameters using the AdamW optimizer with ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 18 (A.6 Scaling Hypothesis Pretraining Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Reach-Cube, state, policy, where, current, fingertip, position, latent, visual, vector, obtained, passing, image, observation | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | Reach-Cube, state, policy, where, current, fingertip, position, latent, visual, vector | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | visual, cortex, region, organism, brain, together, motor, enables, sight, converted | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | train, agents, reward, functions, presented, utilizing, following, settings, success, weighting | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 17 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** For Reach-Cube, the state for the BC policy is [xft t , zt], where xft t is the current fingertip position and zt is the ...
- **p. 1 / 1 Introduction - extractive body cue:** In this work, we ask the same question that Fukushima [1, 2] asked nearly 50 years ago - how do we design an artificial visual ...
- **p. 17 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** For Push-Cube, the state for the BC policy is [xft t , zt, ∆xc g], where ∆xc g is the goal position for the cube, ...
- **p. 16 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** When using vision transformers (ViT) based PVRs, we use the [CLS] token as input to the policy, and with ResNets we use features from the ...
- **p. 16 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** The input to the policy is the [CLS] token for ViT-based PVRs and average pooled features from the last convolutional layer for ResNet-based models. "Habitat ...
- **p. 3 / 1 Introduction - extractive body cue:** To our knowledge, VC-1 (adapted) is the first PVR that is competitive with (or outperforms) state-of-art results on such a diverse set of EAI tasks ...
- **p. 18 / A.2 Overview of Downstream Policy Learning in CORTEXBENCH - extractive body cue:** We train a policy network with hidden layers of size 2000 and learning rate 10-4 for up to 100 epochs for the reach task and ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | The episode length for this task is 20 steps. | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | The motors are controlled at a frequency of 1kHz and the action sent to the robot is a 9 dimensional vector specifying ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | The episode length for this task is 20 steps. | hardware, batch and throughput |

## Training vs Inference

- **p. 18 / A.6 Scaling Hypothesis Pretraining Details - extractive body cue:** However, we do vary the number of epochs we use to train the different models in Section 5 given the different dataset sizes.
- **p. 18 / A.6 Scaling Hypothesis Pretraining Details - extractive body cue:** To train the MAE models, we use the official codebase released by the authors on GitHub [18] and use the default hyperparameters provided by the ...
- **p. 22 / A.12 Franka Hardware Experiment Setup - extractive body cue:** For PVR (frozen encoders), we use Adam optimizer with a learning rate 10-3 to train the policies.
- **p. 22 / A.12 Franka Hardware Experiment Setup - extractive body cue:** For fine-tuning, we use the same learning rate for policies but a lower learning rate (10-5) for the visual encoders.
- **p. 18 / A.6 Scaling Hypothesis Pretraining Details - extractive body cue:** To train the MAE models, we use the official codebase released by the authors on GitHub [18] and use the default hyperparameters provided by the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** patch, representations, ViT-based, PVRs, grid-features, last, convolutional, layer, ResNet, models, passed, through, compression, lower, dimensional, representation, policy, layers, LSTM, navigation.
- **Relevant PDF headings:** A.2 Overview of Downstream Policy Learning in CORTEXBENCH (p. 16); A.8 Additional Analysis of All Models Evaluated on CORTEXBENCH (p. 19); A.9 Additional Analysis of Scaling Model Size (p. 19).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | We carried out experiments on the real TriFinger robot (shown in Figure 9) for the Push-Cube task, after training a model using ... | p. 21 (A.11 TriFinger Hardware Experiment Setup), p. 5 (Results) |
| Baseline harness | However, we find that several of these pre-trained models often outperform a random training from scratch baseline. | p. 5 (Results), p. 8 (Figure/Table caption) |
| Metric / failure reporting | Figure 1: An artificial visual cortex for embodied in- telligence must support a diverse range of sensorimotor skills, environments, and embodiments; we ... | p. 2 (Figure/Table caption), p. 8 (Results) |

## Failure and Ablation Link

- **p. 5 / Results - extractive body cue:** For all evaluations preceding Section 6, we consider frozen visual representations to disentangle the effect of learned representations from downstream task learning.
- **p. 6 / Results - extractive body cue:** 5.2 Scaling Hypothesis Findings We now turn to analyzing the effect of increasing model size, dataset size, and dataset diversity.
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 7: Scaling model size has a positive effect on (a) every benchmark and on (b) fifteen out of the seventeen tasks. A.10 Attention Visualizations ...
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 8: Attention Visualization: (left) Random ViT-L; (middle) VC-1 frozen; (right) VC-1 E2E finetuned. We overlay the mean attention matrix in the last layer of ...
- **p. 4 / Dataset - extractive body cue:** Adroit Dexterous … … … 7 datasets 7 methods 17 tasks Ego4D RealEstate10K encoder .... .... decoder input target MAE "stirs the snacks…" Time Contrastive ...
- **p. 6 / Results - extractive body cue:** 5.1 Constructing a Pre-training Dataset for EAI Table 3: Datasets assembled to study effects of pretraining dataset size, diversity, and relevance - the largest (Ego4D+MNI) ...
- **p. 22 / A.12 Franka Hardware Experiment Setup - extractive body cue:** For fine-tuning, we use the same learning rate for policies but a lower learning rate (10-5) for the visual encoders.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 16 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 16 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 18 (A.6 Scaling Hypothesis Pretraining Details), p. 18 (A.6 Scaling Hypothesis Pretraining Details), objective p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 18 (A.6 Scaling Hypothesis Pretraining Details), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), temporal p. 21 (A.11 TriFinger Hardware Experiment Setup), p. 21 (A.11 TriFinger Hardware Experiment Setup), p. 22 (A.12 Franka Hardware Experiment Setup), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 17 (A.2 Overview of Downstream Policy Learning in CORTEXBENCH), p. 2 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (23 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** For Reach-Cube, the state for the BC policy is [xft t , zt], where xft t is the current fingertip position and zt is the latent visual state vector, obtained ... (p. 17, A.2 Overview of Downstream Policy Learning in CORTEXBENCH).
- **Objective/update evidence:** We choose the number of epochs per run such that the number of model updates remain constant across all runs and match the number of model updates taken by MAE ... (p. 18, A.6 Scaling Hypothesis Pretraining Details).
- **Temporal/runtime evidence:** The episode length for this task is 20 steps. (p. 21, A.11 TriFinger Hardware Experiment Setup).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
