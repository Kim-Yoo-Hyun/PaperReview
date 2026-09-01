# Method - Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://papers.nips.cc/paper_files/paper/2024/hash/e0f393e7980a24fd12fa6f15adfa25fb-Abstract-Conference.html; PDF retrieval source: https://arxiv.org/pdf/2409.20537. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 17 (A Implementation Details), p. 17 (A.1 Dataset Details)): Different from previous work [55, 86], we use minimal amounts of processing and cleaning of the observation and actions in the raw trajectories.

## Method Body Digest

- **p. 17 / A Implementation Details - extractive body cue:** Different from previous work [55, 86], we use minimal amounts of processing and cleaning of the observation and actions in the raw trajectories.
- **p. 17 / A.1 Dataset Details - extractive body cue:** Since the human datasets do not contain proprioception and action information, we use hand poses and 2D positions in the image space as surrogates for ...
- **p. 6 / 1 Introduction - extractive body cue:** We reinitialize the head and stem parameters with embodiment-specific input and output dimensions (such as different proprioception and action dimensions), and freeze the weights of ...
- **p. 4 / 1 Introduction - extractive body cue:** 3 Heterogenoues Pre-trained Transformers (HPT) In heterogeneous robot learning with cross embodiments, the data are generated from different domains such as simulation and real robots, ...
- **p. 5 / 1 Introduction - extractive body cue:** MLP) that takes as input the pooled feature of the trunk and outputs a normalized action trajectory.
- **p. 5 / 1 Introduction - extractive body cue:** The policy head θhead takes the output of the trunk transformer and maps it to the action space A in each dataset.
- **p. 4 / 1 Introduction - extractive body cue:** Although we mainly focus on proprioception and vision, handling other kinds of sensor heterogeneity in tactile, 3D, and action inputs can be flexibly extended in ...
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we consider robots equipped with a distinct set of sensors and actuators with the associated observation and action space to be a ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** We introduce Heterogeneous Pre-trained Transformers (HPT), a family of architecture designed to scalably learn from data across heterogeneous embodiments.
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose to address this issue by aligning the proprioception and vision information from different embodiments to a shared "language" of policies ...
- **p. 5 / 1 Introduction - extractive body cue:** This is used as the input sequence to the trunk that we introduce below.

## Source Evidence Cues

- **p. 17 / A Implementation Details - extractive body cue:** Different from previous work [55, 86], we use minimal amounts of processing and cleaning of the observation and actions in the raw trajectories.
- **p. 17 / A.1 Dataset Details - extractive body cue:** Since the human datasets do not contain proprioception and action information, we use hand poses and 2D positions in the image space as surrogates for ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | Different from previous work [55, 86], we use minimal amounts of processing and cleaning of the observation and actions in the raw ... | p. 17 (A Implementation Details), p. 17 (A.1 Dataset Details) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | Since the human datasets do not contain proprioception and action information, we use hand poses and 2D positions in the image space ... | p. 17 (A.1 Dataset Details) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | Different from previous work [55, 86], we use minimal amounts of processing and cleaning of the observation and actions in the raw ... | p. 17 (A Implementation Details) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 17 / A.1 Dataset Details - extractive body cue:** Since the human datasets do not contain proprioception and action information, we use hand poses and 2D positions in the image space as surrogates for ...
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 17 (A.1 Dataset Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | reinitialize, head, stem, parameters, embodiment-specific, input, output, dimensions, different, proprioception, action, freeze, weights, trunk | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | reinitialize, head, stem, parameters, embodiment-specific, input, output, dimensions, different, proprioception | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | introduce, Heterogeneous, Pre-trained, Transformers, HPT, family, architecture, designed, scalably, learn | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | Since, human, datasets, contain, proprioception, action, information, hand, poses, positions | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 1 Introduction - extractive body cue:** We reinitialize the head and stem parameters with embodiment-specific input and output dimensions (such as different proprioception and action dimensions), and freeze the weights of ...
- **p. 4 / 1 Introduction - extractive body cue:** 3 Heterogenoues Pre-trained Transformers (HPT) In heterogeneous robot learning with cross embodiments, the data are generated from different domains such as simulation and real robots, ...
- **p. 5 / 1 Introduction - extractive body cue:** MLP) that takes as input the pooled feature of the trunk and outputs a normalized action trajectory.
- **p. 5 / 1 Introduction - extractive body cue:** The policy head θhead takes the output of the trunk transformer and maps it to the action space A in each dataset.
- **p. 4 / 1 Introduction - extractive body cue:** Although we mainly focus on proprioception and vision, handling other kinds of sensor heterogeneity in tactile, 3D, and action inputs can be flexibly extended in ...
- **p. 8 / 1 Introduction - extractive body cue:** For the human datasets that lack proprioception and action information, we use poses and 2D positions as surrogates for the supervised policy learning objectives.
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we consider robots equipped with a distinct set of sensors and actuators with the associated observation and action space to be a ...
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | The episode lengths of real-world teleoperation vary from 50 steps to 150 steps with 10 Hz control frequencies. | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | We use a total of 150 trajectories and each trajectory contains more than 500 steps. | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | not recovered | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | The episode lengths of real-world teleoperation vary from 50 steps to 150 steps with 10 Hz control frequencies. | hardware, batch and throughput |

## Training vs Inference

- **p. 17 / A Implementation Details - extractive body cue:** When training with 80k iterations, the approximate training epochs with fixed batch size 512 range from 200 epochs to 2 epochs.
- **p. 17 / A Implementation Details - extractive body cue:** Specifically, the default training setup is to train 80000 iterations with a batch size 256, which is around 0.65B tokens in the latent space that ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Different, previous, minimal, amounts, processing, cleaning, observation, actions, trajectories, Since, human, datasets, contain, proprioception, action, information, hand, poses, positions, image.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | For the additional 7 simulation dataset, we use the simulator benchmarks across all popular simulators Drake [81], Mujoco [89, 49], Isaac Sim ... | p. 17 (A.1 Dataset Details), p. 17 (A.1 Dataset Details) |
| Coverage / augmentation | Figure 17: Simulation Task Performance compared with Single-Task Policy in LeRobot Implementation. We do evaluation in a different implementation in unseen simulation ... | p. 22 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Downstream learning interface | Figure 17: Simulation Task Performance compared with Single-Task Policy in LeRobot Implementation. We do evaluation in a different implementation in unseen simulation ... | p. 22 (Figure/Table caption), p. 9 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Stem Architecture in HPT. In the HPT stem, the proprioceptive tokenizer uses an MLP to map proprioceptive information to a feature which is ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 8: Joint Pre-training with Simulation and Hu- man Videos. The baseline denotes the default setting without simulation and human datasets. Setting: We run the ...
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 15: Additional Architectural Ablation. (a) We found that architecture changes on HPT-Base such as adding previous actions as inputs, multiview as inputs, and language ...
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 16: Transfer Learning Objective. We run transfer learning across several simulator benchmarks [81, 49, 89]. We compare the validation loss curves of several baselines ...
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 17: Simulation Task Performance compared with Single-Task Policy in LeRobot Implementation. We do evaluation in a different implementation in unseen simulation benchmarks. Left) we ...
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 18: Ablation Study on HPT Stem. We ablate the pre-training performance for (a) proprioception, (b) vision stems, and (c) vision encoders. Setting: HPT-S, batch ...
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 19: (a) Initial Condition Overlay. We visualize different rollout initial conditions during test times. (b) Failure Cases of the Learned Policy in the Real ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 17 (A Implementation Details), p. 17 (A.1 Dataset Details), objective p. 17 (A.1 Dataset Details), temporal p. 9 (1 Introduction), p. 17 (A.1 Dataset Details), p. 17 (A Implementation Details), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
