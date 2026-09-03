# Evaluation - Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://papers.nips.cc/paper_files/paper/2024/hash/e0f393e7980a24fd12fa6f15adfa25fb-Abstract-Conference.html; PDF retrieval source: https://arxiv.org/pdf/2409.20537. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 22 (Figure/Table caption), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 10 (Figure/Table caption)): Figure 17: Simulation Task Performance compared with Single-Task Policy in LeRobot Implementation. We do evaluation in a different implementation in unseen simulation benchmarks. Left) we show that an improvement in ...

## Evaluation Body Digest

- **p. 17 / A.1 Dataset Details - extractive body cue:** For the additional 7 simulation dataset, we use the simulator benchmarks across all popular simulators Drake [81], Mujoco [89, 49], Isaac Sim [20], and PyBullet ...
- **p. 17 / A.1 Dataset Details - extractive body cue:** This dataset is composed of deployed mobile robots in the wild.
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 12: Transfer Learning in the Real World. We evaluate the pre-trained HPTs on four tasks / two embodiments. The average success rate with standard ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 10: Success Rates in Simulation Experiments. (a) We evaluate transfer learning performance of models from HPT-B to HPT-XL on tasks across 4 different simulator ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Data Scaling. We run scaling HPT experiments along dataset sizes and the number of datasets. Each point is the validation loss of a ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Epoch Scaling. We run scaling HPT experiments along the number of total samples. Each point is the validation loss of a full pre-training ...
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 15: Additional Architectural Ablation. (a) We found that architecture changes on HPT-Base such as adding previous actions as inputs, multiview as inputs, and language ...
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 17: Simulation Task Performance compared with Single-Task Policy in LeRobot Implementation. We do evaluation in a different implementation in unseen simulation benchmarks. Left) we ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** multi-robot demonstration/dataset ecosystem.
- **Input boundary:** multi-view observation, language/task label과 action trajectory.
- **Output/decision under evaluation:** dataset sample 또는 learned policy action.
- **Primary target:** coverage, cross-embodiment transfer, data efficiency와 task success.
- **Detected evaluation headings:** A Implementation Details (p. 17); A.1 Dataset Details (p. 17); 28 Datasets (p. 18); 15 Datasets (p. 18); 5 Datasets (p. 18); 50 Datasets (p. 18); Dataset (p. 19); A.3 Pre-training Experiment Details (p. 19); A.4 Simulation Experiment Details (p. 20); A.5 Real-World Experiment Details (p. 21); B Additional Experiments (p. 21); B.1 Additional Simulation Experiments (p. 21).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 17: Simulation Task Performance compared with Single-Task Policy in LeRobot Implementation. We do evaluation in a different implementation in unseen simulation benchmarks. Left) ... | p. 22 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 10: Success Rates in Simulation Experiments. (a) We evaluate transfer learning performance of models from HPT-B to HPT-XL on tasks across 4 different ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 12: Transfer Learning in the Real World. We evaluate the pre-trained HPTs on four tasks / two embodiments. The average success rate with ... | p. 10 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Table 2: Dataset Details of Pre-train Settings. The default setup is trained with 27 datasets from RT-X with 16k trajectories (maximum 1000 trajectories each) ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 6: Epoch Scaling. We run scaling HPT experiments along the number of total samples. Each point is the validation loss of a full ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 17 / A.1 Dataset Details - extractive body cue:** For the additional 7 simulation dataset, we use the simulator benchmarks across all popular simulators Drake [81], Mujoco [89, 49], Isaac Sim [20], and PyBullet ...
- **p. 17 / A.1 Dataset Details - extractive body cue:** This dataset is composed of deployed mobile robots in the wild.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: The Heterogeneous Pre-training concept. It maps different embodiments, each with its own proprioception and vision sensors, onto a shared la- tent space by ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: HPT architecture. HPT is modularized into stems, trunk, and heads. The stem, consist- ing of a proprioception tokenizer and a vision tokenizer, maps ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Stem Architecture in HPT. In the HPT stem, the proprioceptive tokenizer uses an MLP to map proprioceptive information to a feature which is ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Dataset Heterogeneity in Robotics. We show illustrations of dataset mixtures (each color is a distinct embodiment) from different domains including real robot teleop ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: Network Details of HPT. The width denotes the latent dimension size of the trunk transformer and the depth denotes the number of blocks. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2: Dataset Details of Pre-train Settings. The default setup is trained with 27 datasets from RT-X with 16k trajectories (maximum 1000 trajectories each) and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5: Data Scaling. We run scaling HPT experiments along dataset sizes and the number of datasets. Each point is the validation loss of a ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6: Epoch Scaling. We run scaling HPT experiments along the number of total samples. Each point is the validation loss of a full pre-training ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For the additional 7 simulation dataset, we use the simulator benchmarks across all popular simulators Drake [81], Mujoco [89, 49], Isaac Sim [20], and ... | embodiment, simulator version and control stack | p. 17 (A.1 Dataset Details), p. 17 (A.1 Dataset Details) |
| Task/environment | This dataset is composed of deployed mobile robots in the wild. | reset, timeout, object/scene variation | p. 17 (A.1 Dataset Details) |
| Observation/sensor | multi-view observation, language/task label과 action trajectory | calibration, preprocessing, privileged input | p. 6 (1 Introduction), p. 4 (1 Introduction) |
| Output/decision | dataset sample 또는 learned policy action | action frame, controller and termination | p. 5 (1 Introduction), p. 5 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 12: Transfer Learning in the Real World. We evaluate the pre-trained HPTs on four tasks / two embodiments. The average success rate with ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Figure 10: Success Rates in Simulation Experiments. (a) We evaluate transfer learning performance of models from HPT-B to HPT-XL on tasks across 4 different ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Figure 5: Data Scaling. We run scaling HPT experiments along dataset sizes and the number of datasets. Each point is the validation loss of ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 6: Epoch Scaling. We run scaling HPT experiments along the number of total samples. Each point is the validation loss of a full ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 15: Additional Architectural Ablation. (a) We found that architecture changes on HPT-Base such as adding previous actions as inputs, multiview as inputs, and ... | definition/direction/unit from same section | p. 21 (Figure/Table caption) |
| Figure 17: Simulation Task Performance compared with Single-Task Policy in LeRobot Implementation. We do evaluation in a different implementation in unseen simulation benchmarks. Left) ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| Figure 3: Stem Architecture in HPT. In the HPT stem, the proprioceptive tokenizer uses an MLP to map proprioceptive information to a feature which ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Table 2: Dataset Details of Pre-train Settings. The default setup is trained with 27 datasets from RT-X with 16k trajectories (maximum 1000 trajectories each) ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 17: Simulation Task Performance compared with Single-Task Policy in LeRobot Implementation. We do evaluation in a different implementation in unseen simulation benchmarks. Left) ... | comparison identity and matched condition | p. 22 (Figure/Table caption) |
| Figure 8: Joint Pre-training with Simulation and Hu- man Videos. The baseline denotes the default setting without simulation and human datasets. Setting: We run ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 3: Comparison on the Sweep Leftover. We compare the fine-tuned HPT models with several baselines in- cluding vision-only pre-trained models. 6 | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| Figure 16: Transfer Learning Objective. We run transfer learning across several simulator benchmarks [81, 49, 89]. We compare the validation loss curves of several ... | comparison identity and matched condition | p. 22 (Figure/Table caption) |
| Figure 10: Success Rates in Simulation Experiments. (a) We evaluate transfer learning performance of models from HPT-B to HPT-XL on tasks across 4 different ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Figure 3: Stem Architecture in HPT. In the HPT stem, the proprioceptive tokenizer uses an MLP to map proprioceptive information to a feature which ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 3: Stem Architecture in HPT. In the HPT stem, the proprioceptive tokenizer uses an MLP to map proprioceptive information to a feature which ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Figure 8: Joint Pre-training with Simulation and Hu- man Videos. The baseline denotes the default setting without simulation and human datasets. Setting: We run ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 15: Additional Architectural Ablation. (a) We found that architecture changes on HPT-Base such as adding previous actions as inputs, multiview as inputs, and ... | component/input/data sensitivity | p. 21 (Figure/Table caption) |
| Figure 16: Transfer Learning Objective. We run transfer learning across several simulator benchmarks [81, 49, 89]. We compare the validation loss curves of several ... | component/input/data sensitivity | p. 22 (Figure/Table caption) |
| Figure 17: Simulation Task Performance compared with Single-Task Policy in LeRobot Implementation. We do evaluation in a different implementation in unseen simulation benchmarks. Left) ... | component/input/data sensitivity | p. 22 (Figure/Table caption) |
| Figure 18: Ablation Study on HPT Stem. We ablate the pre-training performance for (a) proprioception, (b) vision stems, and (c) vision encoders. Setting: HPT-S, ... | component/input/data sensitivity | p. 23 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce Heterogeneous Pre-trained Transformers (HPT), a family of architecture designed to scalably learn from data across heterogeneous embodiments. | Figure 17: Simulation Task Performance compared with Single-Task Policy in LeRobot Implementation. We do evaluation in a different implementation in unseen simulation benchmarks. Left) ... | PDF body cue; verify exact table/figure and matched conditions | p. 22 (Figure/Table caption), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 10 (Figure/Table caption) |
| Primary metric/result | Figure 10: Success Rates in Simulation Experiments. (a) We evaluate transfer learning performance of models from HPT-B to HPT-XL on tasks across 4 different ... | numeric claim only at cited anchor | p. 9 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 17 / A Implementation Details - extractive body cue:** We use maximum episode counts per dataset ranging from 10 trajectories to 100000 trajectories, and the total trajectories range from around 300 trajectories and 6000 ...
- **p. 17 / A Implementation Details - extractive body cue:** When training with 80k iterations, the approximate training epochs with fixed batch size 512 range from 200 epochs to 2 epochs.
- **p. 17 / A.1 Dataset Details - extractive body cue:** We use in total of 2000 trajectories of video clips from EPIC kitchen with a maximum trajectory length of 500.
- **p. 17 / A.1 Dataset Details - extractive body cue:** We use a total of 150 trajectories and each trajectory contains more than 500 steps.
- **p. 17 / A Implementation Details - extractive body cue:** We use maximum episode counts per dataset ranging from 10 trajectories to 100000 trajectories, and the total trajectories range from around 300 trajectories and 6000 ...
- **p. 17 / A Implementation Details - extractive body cue:** When training with 80k iterations, the approximate training epochs with fixed batch size 512 range from 200 epochs to 2 epochs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | See Appendix §C for some failure modes. | p. 10 (6 Conclusion) |
| body limitation/failure cue | Figure 18: Ablation Study on HPT Stem. We ablate the pre-training performance for (a) proprioception, (b) vision stems, and (c) vision encoders. Setting: HPT-S, ... | p. 23 (Figure/Table caption) |
| body limitation/failure cue | Figure 19: (a) Initial Condition Overlay. We visualize different rollout initial conditions during test times. (b) Failure Cases of the Learned Policy in the ... | p. 23 (Figure/Table caption) |
| body limitation/failure cue | We hope this perspective will inspire future work in handling the heterogeneous nature of robotic data for robotic foundation models. | p. 10 (6 Conclusion) |
| body limitation/failure cue | Figure 10: Success Rates in Simulation Experiments. (a) We evaluate transfer learning performance of models from HPT-B to HPT-XL on tasks across 4 different ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Figure 13: Large-scale Dataset Heterogeneity in Robotics. We show different dataset mixtures at increasing scales (top row) across trajectory counts, dataset sample counts, and ... | p. 18 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| When training with 80k iterations, the approximate training epochs with fixed batch size 512 range from 200 epochs to 2 epochs. | p. 17 (A Implementation Details) |
| Specifically, the default training setup is to train 80000 iterations with a batch size 256, which is around 0.65B tokens in the latent space ... | p. 17 (A Implementation Details) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 6 Conclusion - extractive body cue:** See Appendix §C for some failure modes.
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 18: Ablation Study on HPT Stem. We ablate the pre-training performance for (a) proprioception, (b) vision stems, and (c) vision encoders. Setting: HPT-S, batch ...
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 19: (a) Initial Condition Overlay. We visualize different rollout initial conditions during test times. (b) Failure Cases of the Learned Policy in the Real ...
- **p. 10 / 6 Conclusion - extractive body cue:** We hope this perspective will inspire future work in handling the heterogeneous nature of robotic data for robotic foundation models.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 10: Success Rates in Simulation Experiments. (a) We evaluate transfer learning performance of models from HPT-B to HPT-XL on tasks across 4 different simulator ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 13: Large-scale Dataset Heterogeneity in Robotics. We show different dataset mixtures at increasing scales (top row) across trajectory counts, dataset sample counts, and sampling ...

- **Evidence anchors reviewed:** datasets p. 17 (A.1 Dataset Details), p. 17 (A.1 Dataset Details), metrics p. 10 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), p. 21 (Figure/Table caption), p. 22 (Figure/Table caption), baselines p. 22 (Figure/Table caption), p. 8 (Figure/Table caption), p. 10 (Figure/Table caption), p. 22 (Figure/Table caption), p. 9 (Figure/Table caption), p. 4 (Figure/Table caption), results p. 22 (Figure/Table caption), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 10 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 17: Simulation Task Performance compared with Single-Task Policy in LeRobot Implementation. We do evaluation in a different implementation in unseen simulation benchmarks. Left) we show that an improvement in ... (p. 22, Figure/Table caption).
- **Metric evidence:** Figure 10: Success Rates in Simulation Experiments. (a) We evaluate transfer learning performance of models from HPT-B to HPT-XL on tasks across 4 different simulator benchmarks. (b) We compare with ... (p. 9, Figure/Table caption).
- **Baseline/ablation evidence:** Figure 17: Simulation Task Performance compared with Single-Task Policy in LeRobot Implementation. We do evaluation in a different implementation in unseen simulation benchmarks. Left) we show that an improvement in ... (p. 22, Figure/Table caption).
- **Failure/negative evidence:** In Figure 19, we show some failure cases of the learned HPT policies in the real world. (p. 24, C Failure Cases).
