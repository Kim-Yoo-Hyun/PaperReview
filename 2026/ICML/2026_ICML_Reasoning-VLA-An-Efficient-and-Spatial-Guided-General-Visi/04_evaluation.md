# Evaluation - Reasoning-VLA: An Efficient and Spatial-Guided General Vision-Language-Action Reasoning Model for Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=c4iSIrb6Iv; PDF retrieval source: https://openreview.net/pdf/2958fe5249a1a673a414d689de7784b306b2a02a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.2.1. Open-loop Evaluation), p. 7 (5.2.1. Open-loop Evaluation), p. 6 (4. Unified Datasets), p. 6 (5. Experiments), p. 8 (5.2.2. Closed-loop Evaluation), p. 8 (5.2.2. Closed-loop Evaluation)): As shown in the last row of Table 1, the additional fine-tuning further improves performance across all time intervals: Reasoning-VLA-7B+ achieves increases of 4.3% and 12.5% over Reasoning-VLA-7B in average ...

## Evaluation Body Digest

- **p. 7 / 5.2.1. Open-loop Evaluation - extractive body cue:** When fine-tuned with GRPO on specific datasets (i.e., selected nuScenes training clips from the unified dataset), our generalized model demonstrates excellent task-specific performance.
- **p. 6 / 4. Unified Datasets - extractive body cue:** To capture diverse driving scenarios and further improve generalization, we specifically selected eight widely used autonomous driving datasets as the foundation for our unified dataset: ...
- **p. 7 / 5.2.1. Open-loop Evaluation - extractive body cue:** The open-loop performance on the nuScenes dataset is summarized in Table 1.
- **p. 8 / 5.2.2. Closed-loop Evaluation - extractive body cue:** All experiments were conducted on our unified dataset and evaluated using a selected subset of the nuScenes dataset extracted from the unified dataset Methods L2 ...
- **p. 6 / 5.1. Experiment Setups - extractive body cue:** To fairly compare with existing methods, we retain the original training and testing splits of each dataset.
- **p. 8 / 5.2.2. Closed-loop Evaluation - extractive body cue:** For evaluation, the dataset splits follow the recommendations provided by each original dataset.
- **p. 7 / 5.1. Experiment Setups - extractive body cue:** Methods NeuroNCAP Score ↑ Collision Rate (%) ↓ Stationary Frontal Side Avg.
- **p. 7 / 5.2.2. Closed-loop Evaluation - extractive body cue:** The generalized model, Reasoning-VLA-7B, substantially outperforms prior methods in terms of NeuroNCAP Score and Collision Rate, achieving an average NeuroNCAP Score of 2.25 and an ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Unified Datasets (p. 6); 5. Experiments (p. 6); 5.1. Experiment Setups (p. 6); 5.2. Main Comparison Results (p. 7); 5.2.1. Open-loop Evaluation (p. 7); 5.2.2. Closed-loop Evaluation (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2.1. Open-loop Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in the last row of Table 1, the additional fine-tuning further improves performance across all time intervals: Reasoning-VLA-7B+ achieves increases of 4.3% ... | p. 7 (5.2.1. Open-loop Evaluation) |
| 5.2.1. Open-loop Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Reasoning-VLA-3B also achieves results comparable to state-of-the-art methods. | p. 7 (5.2.1. Open-loop Evaluation) |
| 4. Unified Datasets | EMPIRICAL / SOURCE-REPORTED EVALUATION | To capture diverse driving scenarios and further improve generalization, we specifically selected eight widely used autonomous driving datasets as the foundation for our unified ... | p. 6 (4. Unified Datasets) |
| 5. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | How does each design affect the performance of fine-tuned Reasoning-VLA on general autonomous driving tasks? | p. 6 (5. Experiments) |
| 5.2.2. Closed-loop Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Generalized performance on our unifed dataset. | p. 8 (5.2.2. Closed-loop Evaluation) |

## Dataset / Benchmark Role

- **p. 7 / 5.2.1. Open-loop Evaluation - extractive body cue:** When fine-tuned with GRPO on specific datasets (i.e., selected nuScenes training clips from the unified dataset), our generalized model demonstrates excellent task-specific performance.
- **p. 6 / 4. Unified Datasets - extractive body cue:** To capture diverse driving scenarios and further improve generalization, we specifically selected eight widely used autonomous driving datasets as the foundation for our unified dataset: ...
- **p. 7 / 5.2.1. Open-loop Evaluation - extractive body cue:** The open-loop performance on the nuScenes dataset is summarized in Table 1.
- **p. 8 / 5.2.2. Closed-loop Evaluation - extractive body cue:** All experiments were conducted on our unified dataset and evaluated using a selected subset of the nuScenes dataset extracted from the unified dataset Methods L2 ...
- **p. 6 / 5.1. Experiment Setups - extractive body cue:** To fairly compare with existing methods, we retain the original training and testing splits of each dataset.
- **p. 8 / 5.2.2. Closed-loop Evaluation - extractive body cue:** For evaluation, the dataset splits follow the recommendations provided by each original dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Reasoning-VLA is an efficient Vision-Language-Action (VLA) framework for autonomous driving that employs parallel actions to interact with reasoning-enhanced vision-language models (VLMs), enabling one-step ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The action module interacts with the vision-language model (VLM). The learnable action queries are initialized using a Gaussian distribution derived from the ground-truth ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Statistical distribution of the unified dataset. However, these constraints exert a non-negligible influence on the vehicle's behavior and overall driving safety. To ad- ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Open-loop performance on the nuScenes dataset. Our fully generalized methods, Reasoning-VLA-3B and Reasoning-VLA- 7B, follow the complete SFT and RL training process described ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Closed-loop performance on the NeuroNCAP. We utilize the challenging closed-loop NeuroNCAP simulator to emulate a wide range of complex real-world driving scenarios. NeuroNCAP ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Generalized performance on our unifed dataset. We trained two models using the unified dataset: Reasoning-VLA-7B + SFT: This model is fine-tuned using only ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Ablation study of components contributions. R-VLA (Reasoning-VLA) is a 7B-parameter model. All experiments were conducted on our unified dataset and evaluated using a ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 5. Zero shot performance on our unified dataset. The unified dataset is divided into two parts: the training set, which includes data from NAVSIM, ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | When fine-tuned with GRPO on specific datasets (i.e., selected nuScenes training clips from the unified dataset), our generalized model demonstrates excellent task-specific performance. | embodiment, simulator version and control stack | p. 7 (5.2.1. Open-loop Evaluation), p. 6 (4. Unified Datasets) |
| Task/environment | To capture diverse driving scenarios and further improve generalization, we specifically selected eight widely used autonomous driving datasets as the foundation for our unified ... | reset, timeout, object/scene variation | p. 6 (4. Unified Datasets), p. 7 (5.2.1. Open-loop Evaluation) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 4 (3.5. Action Refinement Module) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (3.2. The Structure of Reasoning-VLA), p. 4 (3.3.1. Learnable Action Queries) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Methods NeuroNCAP Score ↑ Collision Rate (%) ↓ Stationary Frontal Side Avg. | definition/direction/unit from same section | p. 7 (5.1. Experiment Setups) |
| The generalized model, Reasoning-VLA-7B, substantially outperforms prior methods in terms of NeuroNCAP Score and Collision Rate, achieving an average NeuroNCAP Score of 2.25 and ... | definition/direction/unit from same section | p. 7 (5.2.2. Closed-loop Evaluation) |
| NAVSIM[9] 0.05 0.18 0.43 0.22 0.04 0.18 0.41 0.21 nuScenes[4] 0.06 0.23 0.48 0.26 0.05 0.20 0.44 0.23 Waymo[40] 0.04 0.15 0.44 0.21 0.03 ... | definition/direction/unit from same section | p. 8 (5.2.2. Closed-loop Evaluation) |
| Table 7. Generalization performance on the Open-loop Metrics. Methods L2 (m) ↓ Collision Rate (%) ↓ 1s 2s 3s Avg. | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| Figure 1. Reasoning-VLA is an efficient Vision-Language-Action (VLA) framework for autonomous driving that employs parallel actions to interact with reasoning-enhanced vision-language models (VLMs), enabling ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| How does each design affect the performance of fine-tuned Reasoning-VLA on general autonomous driving tasks? | definition/direction/unit from same section | p. 6 (5. Experiments) |
| In our experiments, we mainly evaluate Reasoning-VLA's performance on unified AD datasets, which are constructed from eight autonomous driving datasets. | definition/direction/unit from same section | p. 6 (5.1. Experiment Setups) |
| Generalized performance on our unifed dataset. | definition/direction/unit from same section | p. 8 (5.2.2. Closed-loop Evaluation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Reasoning-VLA-3B also achieves results comparable to state-of-the-art methods. | comparison identity and matched condition | p. 7 (5.2.1. Open-loop Evaluation) |
| The generalized model, Reasoning-VLA-7B, substantially outperforms prior methods in terms of NeuroNCAP Score and Collision Rate, achieving an average NeuroNCAP Score of 2.25 and ... | comparison identity and matched condition | p. 7 (5.2.2. Closed-loop Evaluation) |
| Ablation study of components contributions. | comparison identity and matched condition | p. 8 (5.2.2. Closed-loop Evaluation) |
| Table 9. The Efficiency Comparisons. Steps: Theoretical num- ber of VLM inference steps required to complete a single predic- tion process. Speed(s): Measured inference ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation study of components contributions. | component/input/data sensitivity | p. 8 (5.2.2. Closed-loop Evaluation) |
| During training, we shuffle the unified datasets and fine-tune Reasoning-VLA sequen | component/input/data sensitivity | p. 6 (5.1. Experiment Setups) |
| How does each design affect the performance of fine-tuned Reasoning-VLA on general autonomous driving tasks? | component/input/data sensitivity | p. 6 (5. Experiments) |
| ReasoningVLA-7B: Based on Qwen2.5-VL-7B and fine-tuned using the SFT and RL process. | component/input/data sensitivity | p. 7 (5.2.1. Open-loop Evaluation) |
| NeuroNCAP provides pretrained rendering model checkpoints, making it particularly wellsuited for evaluating our method. | component/input/data sensitivity | p. 7 (5.1. Experiment Setups) |
| We trained two models using the unified dataset: Reasoning-VLA-7B + SFT: This model is fine-tuned using only supervised fine-tuning (SFT). | component/input/data sensitivity | p. 8 (5.2.2. Closed-loop Evaluation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, the main contributions are as follows: • We propose Reasoning-VLA, an efficient and fast VLA framework that employs learnable action queries to ... | As shown in the last row of Table 1, the additional fine-tuning further improves performance across all time intervals: Reasoning-VLA-7B+ achieves increases of 4.3% ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.2.1. Open-loop Evaluation), p. 7 (5.2.1. Open-loop Evaluation), p. 6 (4. Unified Datasets), p. 6 (5. Experiments), p. 8 (5.2.2. Closed-loop Evaluation), p. 8 (5.2.2. Closed-loop Evaluation) |
| Primary metric/result | Reasoning-VLA-3B also achieves results comparable to state-of-the-art methods. | numeric claim only at cited anchor | p. 7 (5.2.1. Open-loop Evaluation) |

- Numeric sentences retained from the body:
- **p. 7 / 5.1. Experiment Setups - extractive body cue:** Training is performed for 4 epochs for SFT and 1 epoch for RL, using a total batch size of 8 distributed across 8 H200 GPUs.
- **p. 8 / 5.2.2. Closed-loop Evaluation - extractive body cue:** Datasets Reasoning-VLA-7B + SFT Reasoning-VLA-7B + SFT + RL L2 (m) ↓ L2 (m) ↓ 1s 2s 3s Avg.
- **p. 8 / 5.2.2. Closed-loop Evaluation - extractive body cue:** All experiments were conducted on our unified dataset and evaluated using a selected subset of the nuScenes dataset extracted from the unified dataset Methods L2 ...
- **p. 5 / 3.7. Reward Functions - extractive body cue:** Specifically, the maximum steering angle is limited to 40 degrees, and the maximum acceleration is constrained to 0.6 gravity.
- **p. 5 / 3.7. Reward Functions - extractive body cue:** To achieve comfortable and safe driving behavior, the steering constraint reward is defined as: rsteer = 1 N -1 N-1 X j=1 ( 1, / ...
- **p. 5 / 3.7. Reward Functions - extractive body cue:** The acceleration reward is defined as: accj = p (xj+1 -xj)2 + (yj+1 -yj)2 T 2 - p (xj -xj-1)2 + (yj -yj-1)2 T 2 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 3. Statistical distribution of the unified dataset. However, these constraints exert a non-negligible influence on the vehicle's behavior and overall driving safety. To ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Methods NeuroNCAP Score ↑ Collision Rate (%) ↓ Stationary Frontal Side Avg. | p. 7 (5.1. Experiment Setups) |
| body limitation/failure cue | The generalized model, Reasoning-VLA-7B, substantially outperforms prior methods in terms of NeuroNCAP Score and Collision Rate, achieving an average NeuroNCAP Score of 2.25 and ... | p. 7 (5.2.2. Closed-loop Evaluation) |
| body limitation/failure cue | NAVSIM[9] 0.05 0.18 0.43 0.22 0.04 0.18 0.41 0.21 nuScenes[4] 0.06 0.23 0.48 0.26 0.05 0.20 0.44 0.23 Waymo[40] 0.04 0.15 0.44 0.21 0.03 ... | p. 8 (5.2.2. Closed-loop Evaluation) |
| body limitation/failure cue | Table 7. Generalization performance on the Open-loop Metrics. Methods L2 (m) ↓ Collision Rate (%) ↓ 1s 2s 3s Avg. | p. 14 (Figure/Table caption) |
| body limitation/failure cue | These results indicate that our method maintains robust generalization across different driving scenarios and vehicle configurations. | p. 8 (5.2.3. Generalized Performance) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Training is performed for 4 epochs for SFT and 1 epoch for RL, using a total batch size of 8 distributed across 8 H200 ... | p. 7 (5.1. Experiment Setups) |
| The decay learning rate are start from 5e-4 and e-6 form SFT and RL separately, the accumulated size is 2. | p. 7 (5.1. Experiment Setups) |
| Here T is the number of future time steps to be predicted, N is the dimensions of action trajectory coordinate, D is the feature ... | p. 4 (3.3.1. Learnable Action Queries) |
| Given that the total number of action values is T × N, in our method, we predict future T steps for N coordinates (e.g., ... | p. 4 (2. The reasonable initial values that reflect typical action) |
| Specifically, our physical trajectory reward is defined as: rtraj = 1 -1 N N X i=1 γi  α(xi -xi gt)2 + β(yi -yi gt)2 ... | p. 5 (3.7. Reward Functions) |
| The acceleration reward is defined as: accj = p (xj+1 -xj)2 + (yj+1 -yj)2 T 2 - p (xj -xj-1)2 + (yj -yj-1)2 T ... | p. 5 (3.7. Reward Functions) |
| Reasoning-VLA-7B+ is fine-tuned with an additional RL process using the corresponding nuScenes training clips from the unified dataset. *: Official checkpoints re-validated with corrected ... | p. 6 (3.7. Reward Functions) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Statistical distribution of the unified dataset. However, these constraints exert a non-negligible influence on the vehicle's behavior and overall driving safety. To ad- ...
- **p. 7 / 5.1. Experiment Setups - extractive body cue:** Methods NeuroNCAP Score ↑ Collision Rate (%) ↓ Stationary Frontal Side Avg.
- **p. 7 / 5.2.2. Closed-loop Evaluation - extractive body cue:** The generalized model, Reasoning-VLA-7B, substantially outperforms prior methods in terms of NeuroNCAP Score and Collision Rate, achieving an average NeuroNCAP Score of 2.25 and an ...
- **p. 8 / 5.2.2. Closed-loop Evaluation - extractive body cue:** NAVSIM[9] 0.05 0.18 0.43 0.22 0.04 0.18 0.41 0.21 nuScenes[4] 0.06 0.23 0.48 0.26 0.05 0.20 0.44 0.23 Waymo[40] 0.04 0.15 0.44 0.21 0.03 0.14 ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 7. Generalization performance on the Open-loop Metrics. Methods L2 (m) ↓ Collision Rate (%) ↓ 1s 2s 3s Avg.
- **p. 8 / 5.2.3. Generalized Performance - extractive body cue:** These results indicate that our method maintains robust generalization across different driving scenarios and vehicle configurations.

- **Evidence anchors reviewed:** datasets p. 7 (5.2.1. Open-loop Evaluation), p. 6 (4. Unified Datasets), p. 7 (5.2.1. Open-loop Evaluation), p. 8 (5.2.2. Closed-loop Evaluation), p. 6 (5.1. Experiment Setups), p. 8 (5.2.2. Closed-loop Evaluation), metrics p. 7 (5.1. Experiment Setups), p. 7 (5.2.2. Closed-loop Evaluation), p. 8 (5.2.2. Closed-loop Evaluation), p. 14 (Figure/Table caption), p. 2 (Figure/Table caption), p. 6 (5. Experiments), baselines p. 7 (5.2.1. Open-loop Evaluation), p. 7 (5.2.2. Closed-loop Evaluation), p. 8 (5.2.2. Closed-loop Evaluation), p. 14 (Figure/Table caption), results p. 7 (5.2.1. Open-loop Evaluation), p. 7 (5.2.1. Open-loop Evaluation), p. 6 (4. Unified Datasets), p. 6 (5. Experiments), p. 8 (5.2.2. Closed-loop Evaluation), p. 8 (5.2.2. Closed-loop Evaluation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
