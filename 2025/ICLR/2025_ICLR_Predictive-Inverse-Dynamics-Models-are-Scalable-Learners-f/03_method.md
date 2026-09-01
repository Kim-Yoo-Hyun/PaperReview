# Method - Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=meRCKuUpmc; PDF retrieval source: https://arxiv.org/pdf/2412.15109. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 16 (A.2 NETWORK ARCHITECTURE), p. 15 (A.1 IMPLEMENTATION DETAILS), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 16 (A.2 NETWORK ARCHITECTURE), p. 3 (3 METHOD)): As presented in Figure A-1, Seer consists of the following modules: image encoder, perceiver resampler, robot state encoder, language encoder, transformer backbone, action decoder and image decoder.

## Method Body Digest

- **p. 16 / A.2 NETWORK ARCHITECTURE - extractive PDF cue:** As presented in Figure A-1, Seer consists of the following modules: image encoder, perceiver resampler, robot state encoder, language encoder, transformer backbone, action decoder and ...
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive PDF cue:** Hyperparameters Pre-training Fine-tuning Batch Size 640 (LIBERO & CALVIN) / 2048 (Real) 512 Learning Rate 1e-4 1e-3 Optimizer AdamW AdamW Learning Rate Schedule Cosine decay ...
- **p. 4 / 3 METHOD - extractive PDF cue:** For language inputs, we first tokenize the text and then use a CLIP text encoder (Radford et al., 2021) to obtain text embeddings, which are ...
- **p. 4 / 3 METHOD - extractive PDF cue:** Language 𝒍 Robot State 𝑺𝒕 Multi-Modal Encoder Action Token [INV] Foresight Token [FRS] Predicted Image Action Inverse Dynamics Prediction add Mask Token Current RGB image ...
- **p. 16 / A.2 NETWORK ARCHITECTURE - extractive PDF cue:** Details can be seen in Table A-II. • action decoder: MLPs that decode the latent feature into 7-DOF action. • image decoder: a ViT-based transformer ...
- **p. 3 / 3 METHOD - extractive PDF cue:** Seer takes as input a goal g in the form of language instructions or robot states, along with historical observations ht, and predicts the RGB ...
- **p. 10 / 3 METHOD - extractive PDF cue:** 6 CONCLUSION AND LIMITATIONS In this work, we introduce Seer, an end-to-end predictive inverse dynamics model that synergizes conditional visual foresight with inverse dynamics prediction ...
- **p. 4 / 3 METHOD - extractive PDF cue:** (3) The loss function Linv comprises the arm action loss Larm and the gripper action loss Lgripper Linv = Larm + λLgripper, (4) where Larm ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Additionally, We evaluate our method on six challenging real-world tasks with over 900 trials.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** We introduce a foresight token to predict future RGB images and an action token to estimate intermediate actions between current and predicted future observations.
- **p. 3 / 3 METHOD - extractive PDF cue:** Therefore, we propose conditional visual foresight ffore to effectively anticipate future visual representations.

## Source Evidence Cues

- **p. 16 / A.2 NETWORK ARCHITECTURE - extractive PDF cue:** As presented in Figure A-1, Seer consists of the following modules: image encoder, perceiver resampler, robot state encoder, language encoder, transformer backbone, action decoder and ...
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive PDF cue:** Hyperparameters Pre-training Fine-tuning Batch Size 640 (LIBERO & CALVIN) / 2048 (Real) 512 Learning Rate 1e-4 1e-3 Optimizer AdamW AdamW Learning Rate Schedule Cosine decay ...
- **p. 4 / 3 METHOD - extractive PDF cue:** For language inputs, we first tokenize the text and then use a CLIP text encoder (Radford et al., 2021) to obtain text embeddings, which are ...
- **p. 4 / 3 METHOD - extractive PDF cue:** Language 𝒍 Robot State 𝑺𝒕 Multi-Modal Encoder Action Token [INV] Foresight Token [FRS] Predicted Image Action Inverse Dynamics Prediction add Mask Token Current RGB image ...
- **p. 16 / A.2 NETWORK ARCHITECTURE - extractive PDF cue:** Details can be seen in Table A-II. • action decoder: MLPs that decode the latent feature into 7-DOF action. • image decoder: a ViT-based transformer ...
- **p. 3 / 3 METHOD - extractive PDF cue:** Seer takes as input a goal g in the form of language instructions or robot states, along with historical observations ht, and predicts the RGB ...
- **p. 10 / 3 METHOD - extractive PDF cue:** 6 CONCLUSION AND LIMITATIONS In this work, we introduce Seer, an end-to-end predictive inverse dynamics model that synergizes conditional visual foresight with inverse dynamics prediction ...
- **Detected method headings:** 3 METHOD (p. 3); A.2 NETWORK ARCHITECTURE (p. 16)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | As presented in Figure A-1, Seer consists of the following modules: image encoder, perceiver resampler, robot state encoder, language encoder, transformer backbone, ... | p. 16 (A.2 NETWORK ARCHITECTURE), p. 15 (A.1 IMPLEMENTATION DETAILS) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | Hyperparameters Pre-training Fine-tuning Batch Size 640 (LIBERO & CALVIN) / 2048 (Real) 512 Learning Rate 1e-4 1e-3 Optimizer AdamW AdamW Learning Rate ... | p. 15 (A.1 IMPLEMENTATION DETAILS), p. 4 (3 METHOD) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | For language inputs, we first tokenize the text and then use a CLIP text encoder (Radford et al., 2021) to obtain text ... | p. 4 (3 METHOD), p. 4 (3 METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3 METHOD - extractive PDF cue:** (3) The loss function Linv comprises the arm action loss Larm and the gripper action loss Lgripper Linv = Larm + λLgripper, (4) where Larm ...
- **p. 8 / 3 METHOD - extractive PDF cue:** Integrating the conditional visual foresight objective Lfore and inverse dynamics prediction objective Linv yields the best performance among pre-training and fine-tuning.
- **p. 8 / 3 METHOD - extractive PDF cue:** 4.5 ABLATION STUDIES We investigate the contributions of conditional visual foresight objective Lfore and inverse dynamics prediction objective Linv during pre-training and fine-tuning on CALVIN ...
- **p. 6 / 3 METHOD - extractive PDF cue:** These results underscore the advantages Seer and demonstrate the effectiveness of our pre-training objectives.
- **p. 4 / 3 METHOD - extractive PDF cue:** The overall training loss L comprises Lfore and Linv L = αLfore + Linv, (5) where α is a hyperparameter set to 0.5.
- **p. 5 / 3 METHOD - extractive PDF cue:** The training objectives, conditional visual foresight and inverse dynamics prediction, remain consistent between pre-training and fine-tuning.
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 4 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 5 (3 METHOD), p. 8 (3 METHOD), p. 8 (3 METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Seer, takes, input, goal, form, language, instructions, robot, states, along, historical, observations, predicts, RGB | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | Seer, takes, input, goal, form, language, instructions, robot, states, along | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | Additionally, evaluate, challenging, real-world, tasks, over, trials, introduce, foresight, token | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | loss, function, Linv, comprises, action, Larm, gripper, Lgripper, where, Smooth-L1 | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3 METHOD - extractive PDF cue:** Seer takes as input a goal g in the form of language instructions or robot states, along with historical observations ht, and predicts the RGB ...
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive PDF cue:** Hyperparameters Pre-training Fine-tuning Batch Size 640 (LIBERO & CALVIN) / 2048 (Real) 512 Learning Rate 1e-4 1e-3 Optimizer AdamW AdamW Learning Rate Schedule Cosine decay ...
- **p. 5 / 3 METHOD - extractive PDF cue:** During inference, the complete language instruction l, robot states s, and image observations o are provided as inputs.
- **p. 3 / 3 METHOD - extractive PDF cue:** Each trajectory {(l, ot, st, at)T t=0} provides the time step t, language instruction l, RGB images ot from the eye-on-hand and eye-on-base views, robot ...
- **p. 5 / 3 METHOD - extractive PDF cue:** In turn, the [INV] token attends to the input tokens and one more foresight [FRS] token to perform inverse dynamics prediction, outputting the action.
- **p. 4 / 3 METHOD - extractive PDF cue:** As illustrated in Figure 2, the model processes three types of inputs: language, images, and robot states.
- **p. 4 / 3 METHOD - extractive PDF cue:** Language 𝒍 Robot State 𝑺𝒕 Multi-Modal Encoder Action Token [INV] Foresight Token [FRS] Predicted Image Action Inverse Dynamics Prediction add Mask Token Current RGB image ...
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | To incorporate temporal information, we also add a learnable position embedding to the tokens for each timestep. | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | Seer takes as input a goal g in the form of language instructions or robot states, along with historical observations ht, and ... | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | not recovered | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | Hyperparameters Pre-training Fine-tuning Batch Size 640 (LIBERO & CALVIN) / 2048 (Real) 512 Learning Rate 1e-4 1e-3 Optimizer AdamW AdamW Learning Rate ... | hardware, batch and throughput |

## Training vs Inference

- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive PDF cue:** Hyperparameters Pre-training Fine-tuning Batch Size 640 (LIBERO & CALVIN) / 2048 (Real) 512 Learning Rate 1e-4 1e-3 Optimizer AdamW AdamW Learning Rate Schedule Cosine decay ...
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive PDF cue:** Hyperparameters Pre-training Fine-tuning Batch Size 640 (LIBERO & CALVIN) / 2048 (Real) 512 Learning Rate 1e-4 1e-3 Optimizer AdamW AdamW Learning Rate Schedule Cosine decay ...
- **p. 16 / A.3 BASELINE IMPLEMENTATION - extractive PDF cue:** For MVP and MPI, we replace the vision encoder in our policy with their pretrained versions.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** presented, Figure, A-1, Seer, consists, following, modules, image, encoder, perceiver, resampler, robot, state, language, transformer, backbone, action, decoder, Hyperparameters, Pre-training.
- **Relevant PDF headings:** 3 METHOD (p. 3); A.2 NETWORK ARCHITECTURE (p. 16).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | LIBERO (Liu et al., 2024) is a novel benchmark for lifelong learning in robot manipulation, comprising four task suites: LIBERO-SPATIAL, LIBERO-OBJECT, LIBERO-GOAL, ... | p. 16 (A.4 LIBERO-LONG EXPERIMENT DETAILS), p. 19 (A.6.4 ACROSS EMBODIMENTS EXPERIMENTS) |
| Coverage / augmentation | Table 1: LIBERO-LONG results. For each task, we present the average performance of top-3 checkpoints averaged over 20 rollouts. The metric "Avg. ... | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Downstream learning interface | Table 1: LIBERO-LONG results. For each task, we present the average performance of top-3 checkpoints averaged over 20 rollouts. The metric "Avg. ... | p. 6 (Figure/Table caption), p. 19 (A.6.5 DETAILED REAL-WORLD RESULTS) |

## Failure and Ablation Link

- **p. 19 / A.6.4 ACROSS EMBODIMENTS EXPERIMENTS - extractive PDF cue:** We refer the subset mix-up recipe in Octo (Ghosh et al., 2024), remove all the subset that includes franka robots, filter subsets with odd action ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Ablation studies on fine-tuning and pre-training objectives. Integrating the conditional visual foresight objective Lfore and inverse dynamics prediction objective Linv yields the best ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Figure 5: Generalization evaluation. We design a generalization test per task with different dis- turbances. Top Left: In Flip Bowl, we put several bowls with ...
- **p. 16 / A.3 BASELINE IMPLEMENTATION - extractive PDF cue:** Thanks to the strong design of our policy, MVP and MPI show competitive performance, though they only approach the results of our policy without pretraining.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: In contrast to previous methods that (a) conduct end-to-end naive behavior cloning from large-scale robotic data or (b) use decoupled visual prediction and ...
- **p. 16 / A.4 LIBERO-LONG EXPERIMENT DETAILS - extractive PDF cue:** We use LIBERO-90 as the pretraining dataset, while LIBERO-LONG is utilized for the downstream finetuning and evaluation.
- **p. 17 / A.5 CALVIN ABC-D EXPERIMENT DETAILS - extractive PDF cue:** Data from Env A, B, and C, which lacks language annotations, is used to pretrain the policy, while data with language annotations is used for ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 16 (A.2 NETWORK ARCHITECTURE), p. 15 (A.1 IMPLEMENTATION DETAILS), p. 4 (3 METHOD), p. 4 (3 METHOD), p. 16 (A.2 NETWORK ARCHITECTURE), p. 3 (3 METHOD), objective p. 4 (3 METHOD), p. 8 (3 METHOD), p. 8 (3 METHOD), p. 6 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), temporal p. 5 (3 METHOD), p. 3 (3 METHOD), p. 3 (3 METHOD), p. 4 (3 METHOD), p. 5 (3 METHOD), p. 4 (3 METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
