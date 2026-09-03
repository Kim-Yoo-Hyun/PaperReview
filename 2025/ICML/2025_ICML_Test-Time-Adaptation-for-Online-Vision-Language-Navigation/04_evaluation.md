# Evaluation - Test-Time Adaptation for Online Vision-Language Navigation with Feedback-based Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=K4GaB4fdIq; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/168050. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (5.4. Effects of Stochastic Gradient Reversion), p. 5 (4.2. Evaluation Metrics), p. 7 (5.2. Quality and Quantity of Feedback), p. 7 (5.1. Main Navigation Results), p. 9 (5.4. Effects of Stochastic Gradient Reversion), p. 14 (Figure/Table caption)): Furthermore, while GD and GS exhibit catastrophic forgetting, the proposed SGR rather brings substantial improvements in the success rates, strengthening the policy's generalizability as well as adaptability on specific domain.

## Evaluation Body Digest

- **p. 6 / 4.3. Implementation Details - extractive body cue:** For the REVERIE dataset, the results in the paper are obtained with p = 0.01 and α = -0.2 for the validation seen split, and ...
- **p. 9 / 5.4. Effects of Stochastic Gradient Reversion - extractive body cue:** First, our FEEDTTA, without gradient regularization, enhances the OSR, SR and RGS metric after adaptation on the validation unseen dataset.
- **p. 6 / 5.1. Main Navigation Results - extractive body cue:** Specifically, our method improves SR and OSR of DUET up to 41.53% and 40.20% on the validation unseen split, respectively.
- **p. 7 / 5.2. Quality and Quantity of Feedback - extractive body cue:** Providing feedback for every navigation episode may not be feasible in real-world scenarios.
- **p. 7 / 5.1. Main Navigation Results - extractive body cue:** For instance, on the R2R validation unseen split, FEEDTTA improved 8.33% on SPL for DUET, while reducing 10.88% in NE.
- **p. 8 / 5.4. Effects of Stochastic Gradient Reversion - extractive body cue:** In the validation unseen split, GD shows the highest result in PSR, but rather decreases CSR, hindering the balance of the two metrics.
- **p. 8 / 5.4. Effects of Stochastic Gradient Reversion - extractive body cue:** To analyze our method in this perspective, we visualize the cumulative success rates and changes in the L1 weight magnitude on the validation unseen split ...
- **p. 9 / 5.4. Effects of Stochastic Gradient Reversion - extractive body cue:** Comparison of Feedback Strategies Feedback Strategy SR SPL RGSPL Distance-based (Dense) 63.25 42.89 28.46 Goal-based (Sparse) 66.49 45.38 30.75 re-evaluated after the TTA on the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experimental Setup (p. 5); 4.1. Dataset Description (p. 5); 4.2. Evaluation Metrics (p. 5); 4.3. Implementation Details (p. 5); 5. Experiments (p. 6); 5.1. Main Navigation Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.4. Effects of Stochastic Gradient Reversion | EMPIRICAL / REAL-ROBOT OR HARDWARE | Furthermore, while GD and GS exhibit catastrophic forgetting, the proposed SGR rather brings substantial improvements in the success rates, strengthening the policy's generalizability as ... | p. 9 (5.4. Effects of Stochastic Gradient Reversion) |
| 4.2. Evaluation Metrics | EMPIRICAL / REAL-ROBOT OR HARDWARE | In addition to these metrics, we propose the ‘Adapted Success Rate (ASR)' metric to accurately measure sample-wise transition of results before and after adaptation. | p. 5 (4.2. Evaluation Metrics) |
| 5.2. Quality and Quantity of Feedback | EMPIRICAL / REAL-ROBOT OR HARDWARE | The performance improves further in proportion to the increase in the percentage of episodes receiving feedback. | p. 7 (5.2. Quality and Quantity of Feedback) |
| 5.1. Main Navigation Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | First, FSTTA exhibits only a minimal performance improvement over the baseline and even shows a decline in scenes with short TLs. | p. 7 (5.1. Main Navigation Results) |
| 5.4. Effects of Stochastic Gradient Reversion | EMPIRICAL / REAL-ROBOT OR HARDWARE | We interpret the increase in TL as representing the minimal additional exploration required to achieve navigation success. | p. 9 (5.4. Effects of Stochastic Gradient Reversion) |

## Dataset / Benchmark Role

- **p. 6 / 4.3. Implementation Details - extractive body cue:** For the REVERIE dataset, the results in the paper are obtained with p = 0.01 and α = -0.2 for the validation seen split, and ...
- **p. 9 / 5.4. Effects of Stochastic Gradient Reversion - extractive body cue:** First, our FEEDTTA, without gradient regularization, enhances the OSR, SR and RGS metric after adaptation on the validation unseen dataset.
- **p. 6 / 5.1. Main Navigation Results - extractive body cue:** Specifically, our method improves SR and OSR of DUET up to 41.53% and 40.20% on the validation unseen split, respectively.
- **p. 7 / 5.2. Quality and Quantity of Feedback - extractive body cue:** Providing feedback for every navigation episode may not be feasible in real-world scenarios.
- **p. 7 / 5.1. Main Navigation Results - extractive body cue:** For instance, on the R2R validation unseen split, FEEDTTA improved 8.33% on SPL for DUET, while reducing 10.88% in NE.
- **p. 8 / 5.4. Effects of Stochastic Gradient Reversion - extractive body cue:** In the validation unseen split, GD shows the highest result in PSR, but rather decreases CSR, hindering the balance of the two metrics.
- **p. 8 / 5.4. Effects of Stochastic Gradient Reversion - extractive body cue:** To analyze our method in this perspective, we visualize the cumulative success rates and changes in the L1 weight magnitude on the validation unseen split ...
- **p. 9 / 5.4. Effects of Stochastic Gradient Reversion - extractive body cue:** Comparison of Feedback Strategies Feedback Strategy SR SPL RGSPL Distance-based (Dense) 63.25 42.89 28.46 Goal-based (Sparse) 66.49 45.38 30.75 re-evaluated after the TTA on the ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Illustration of the learning paradigm of FEEDTTA. The navigation agent adapts to streaming online test data by learning to maximize the cumulative binary ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Conceptual Illustration of SGR. (Left) By reversing the gradients, SGR reduces the distribution gap between the two extreme cases that may cause non-stationary ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Experimental results on the REVERIE dataset. † implies that the results are obtained from our re-implementation (same for Table 2 and Table 3). ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Experimental results on the R2R dataset. Methods Val Seen Val Unseen TL ↓ NE ↓ SR↑ SPL↑
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Experimental results on the R2R-CE dataset. Methods Val Seen Val Unseen TL ↓ NE ↓ OSR↑ SR↑
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Trajectory Length Analysis. We visualize the relation between the ground truth TL (x-axis) and the SR (y-axis) for the REVERIE dataset. The length ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. Feedback Analysis. We study the sensitivity of our method on (a) feedback accuracy, (b) number of first K feedback samples, and (c) update ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Experiments on Large Language Model Oracle. LLMs Feedback Accuracy Navigation Performance Accuracy Recall Precision OSR↑

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For the REVERIE dataset, the results in the paper are obtained with p = 0.01 and α = -0.2 for the validation seen split, ... | embodiment, simulator version and control stack | p. 6 (4.3. Implementation Details), p. 9 (5.4. Effects of Stochastic Gradient Reversion) |
| Task/environment | First, our FEEDTTA, without gradient regularization, enhances the OSR, SR and RGS metric after adaptation on the validation unseen dataset. | reset, timeout, object/scene variation | p. 9 (5.4. Effects of Stochastic Gradient Reversion), p. 6 (5.1. Main Navigation Results) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (3.2. Binary Episodic Feedback), p. 3 (3.1. Task Description) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 3 (3.2. Binary Episodic Feedback), p. 4 (3.2. Binary Episodic Feedback) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We follow the standard evaluation protocol from the previous works (Chen et al., 2021; 2022c; Gao et al., 2024a) and report Trajectory Length (TL), ... | definition/direction/unit from same section | p. 5 (4.2. Evaluation Metrics) |
| LLMs Feedback Accuracy Navigation Performance Accuracy Recall Precision OSR↑ SR↑ SPL↑ RGSPL↑ GPT-4o-mini 0.65 0.62 0.73 59.61 49.90 32.50 23.27 GPT-4o 0.72 0.84 0.68 ... | definition/direction/unit from same section | p. 8 (5.3. LLMs as Feedback Oracle) |
| In addition to these metrics, we propose the ‘Adapted Success Rate (ASR)' metric to accurately measure sample-wise transition of results before and after adaptation. | definition/direction/unit from same section | p. 5 (4.2. Evaluation Metrics) |
| We illustrate (left) cumulative success rates and (right) changes in weight magnitude over iterations. | definition/direction/unit from same section | p. 8 (5.4. Effects of Stochastic Gradient Reversion) |
| Furthermore, while GD and GS exhibit catastrophic forgetting, the proposed SGR rather brings substantial improvements in the success rates, strengthening the policy's generalizability as ... | definition/direction/unit from same section | p. 9 (5.4. Effects of Stochastic Gradient Reversion) |
| Comparison of Feedback Strategies Feedback Strategy SR SPL RGSPL Distance-based (Dense) 63.25 42.89 28.46 Goal-based (Sparse) 66.49 45.38 30.75 re-evaluated after the TTA on ... | definition/direction/unit from same section | p. 9 (5.4. Effects of Stochastic Gradient Reversion) |
| Figure 7. Hyperparameter Analysis of SGR. We illustrate the performance variations w.r.t. the reversion rate p and the reversion magnitude α. The red markers ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| However, FEEDTTA outperforms the baseline in SR with from 50%- 60% of the accuracy, implying that the method is robust to noisy or inaccurate ... | definition/direction/unit from same section | p. 7 (5.2. Quality and Quantity of Feedback) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For the test unseen split, we utilize LLMs as the feedback oracle due to the unavailability of goal-viewpoint data, yet the results remain promising ... | comparison identity and matched condition | p. 6 (5.1. Main Navigation Results) |
| Another noticeable aspect is that only with a single stream of online learning, FEEDTTA on DUET outperforms recent state-of-the-art offline training methods. | comparison identity and matched condition | p. 6 (5.1. Main Navigation Results) |
| However, FEEDTTA outperforms the baseline in SR with from 50%- 60% of the accuracy, implying that the method is robust to noisy or inaccurate ... | comparison identity and matched condition | p. 7 (5.2. Quality and Quantity of Feedback) |
| With 65% and 72% of feedback accuracies, respectively, the LLM oracles generally enhance the baseline performance, which corresponds to our experiment in Figure 4-(a). | comparison identity and matched condition | p. 8 (5.3. LLMs as Feedback Oracle) |
| We follow the standard evaluation protocol from the previous works (Chen et al., 2021; 2022c; Gao et al., 2024a) and report Trajectory Length (TL), ... | comparison identity and matched condition | p. 5 (4.2. Evaluation Metrics) |
| We use the REVERIE dataset and DUET as the baseline for this experiment. | comparison identity and matched condition | p. 7 (5.2. Quality and Quantity of Feedback) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 5. Effects of different gradient regularization variants on α. FEEDTTA w/o reg. denotes a variant of FEEDTTA without any regularization techniques applied. Methods ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| R2R-CE is a variant of R2R in a continuous environment. | component/input/data sensitivity | p. 5 (4.1. Dataset Description) |
| Another strategy to measure sensitivity on feedback quantity is to modify update intervals. | component/input/data sensitivity | p. 7 (5.2. Quality and Quantity of Feedback) |
| The following experiments address RQ2 by studying the sensitivity of FEEDTTA on the quality (e.g., based on accuracy) and the quantity (e.g., based on ... | component/input/data sensitivity | p. 7 (5.2. Quality and Quantity of Feedback) |
| This corresponds to the changes in weight magnitude, where the two variants exhibits the largest scale. | component/input/data sensitivity | p. 8 (5.4. Effects of Stochastic Gradient Reversion) |
| First, our FEEDTTA, without gradient regularization, enhances the OSR, SR and RGS metric after adaptation on the validation unseen dataset. | component/input/data sensitivity | p. 9 (5.4. Effects of Stochastic Gradient Reversion) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, the contributions of this work are as follows. • We introduce FEEDTTA, a novel TTA framework for online VLN utilizing feedback-based RL. | Furthermore, while GD and GS exhibit catastrophic forgetting, the proposed SGR rather brings substantial improvements in the success rates, strengthening the policy's generalizability as ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (5.4. Effects of Stochastic Gradient Reversion), p. 5 (4.2. Evaluation Metrics), p. 7 (5.2. Quality and Quantity of Feedback), p. 7 (5.1. Main Navigation Results), p. 9 (5.4. Effects of Stochastic Gradient Reversion), p. 14 (Figure/Table caption) |
| Primary metric/result | In addition to these metrics, we propose the ‘Adapted Success Rate (ASR)' metric to accurately measure sample-wise transition of results before and after adaptation. | numeric claim only at cited anchor | p. 5 (4.2. Evaluation Metrics) |

- Numeric sentences retained from the body:
- **p. 6 / 4.3. Implementation Details - extractive body cue:** In the last column, we report the average inference time per 4 episodes, measured in milliseconds.
- **p. 6 / 5.1. Main Navigation Results - extractive body cue:** Lastly, we compare the average inference time per 4 episodes.
- **p. 3 / 3.2. Binary Episodic Feedback - extractive body cue:** In FEEDTTA, the rewards are assigned as 0 for t < T -1, and a binary episodic feedback F for t = T -1, giving ...
- **p. 4 / 3.2. Binary Episodic Feedback - extractive body cue:** (Right) Specifically, among the variants of α, the negative value (reversion) shifts the original gradient closest to the counterfactual distribution. mated gradient of the policy ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The proposed adaptation strategy utilizing binary episodic feedback enables agents to dynamically interact with their external environment by providing them with a notion of ... | p. 9 (6. Conclusion) |
| body limitation/failure cue | Figure 1. Illustration of the learning paradigm of FEEDTTA. The navigation agent adapts to streaming online test data by learning to maximize the cumulative ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Feedback accuracies less than 50% leads to obvious adaptation failure. | p. 7 (5.2. Quality and Quantity of Feedback) |
| body limitation/failure cue | We leverage a two-step LLM architecture for determining the navigation success or failure. | p. 7 (5.3. LLMs as Feedback Oracle) |
| body limitation/failure cue | Specifically, for both data splits, SGR brings 14.21% and 10.28% improvements in CSR, respectively, indicating the flexibility of FEEDTTA in dealing with failure scenarios. | p. 8 (5.4. Effects of Stochastic Gradient Reversion) |
| body limitation/failure cue | Impact Statement Although our FEEDTTA leads significant performance improvements, it does not guarantee perfect prediction across the diverse environment. | p. 9 (6. Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our proposed FEEDTTA is applied at the inference time of these offline trained VLN policies. | p. 5 (4.3. Implementation Details) |
| Lastly, we compare the average inference time per 4 episodes. | p. 6 (5.1. Main Navigation Results) |
| We use a batch size of 1 to properly simulate the online environment. | p. 6 (4.3. Implementation Details) |
| Specifically, we freeze the language and visual encoders, updating the parameters starting from the cross-modal encoder onward. | p. 5 (4.3. Implementation Details) |
| The plotted results represent the average of 3 experiments conducted with different seeds. | p. 8 (5.3. LLMs as Feedback Oracle) |
| The results are averaged across 3 experiments with different seeds. policy's performance, its effectiveness is further amplified with the addition of gradient regularization. | p. 8 (5.4. Effects of Stochastic Gradient Reversion) |
| The rationale behind choosing a simple binary episodic feedback mechanism stems from the practical limitations of the online test-time navigation environment: (1) Human involvement ... | p. 9 (5.5. Comparison with Different Feedback Strategies) |
| Utilizing the modified gradient, the parameter update at the nth iteration becomes: θn+1 ←θn + η∇J(θ)′, (6) where η > 0 is the learning ... | p. 4 (3.3. Stochastic Gradient Reversion) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 6. Conclusion - extractive body cue:** The proposed adaptation strategy utilizing binary episodic feedback enables agents to dynamically interact with their external environment by providing them with a notion of success ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Illustration of the learning paradigm of FEEDTTA. The navigation agent adapts to streaming online test data by learning to maximize the cumulative binary ...
- **p. 7 / 5.2. Quality and Quantity of Feedback - extractive body cue:** Feedback accuracies less than 50% leads to obvious adaptation failure.
- **p. 7 / 5.3. LLMs as Feedback Oracle - extractive body cue:** We leverage a two-step LLM architecture for determining the navigation success or failure.
- **p. 8 / 5.4. Effects of Stochastic Gradient Reversion - extractive body cue:** Specifically, for both data splits, SGR brings 14.21% and 10.28% improvements in CSR, respectively, indicating the flexibility of FEEDTTA in dealing with failure scenarios.
- **p. 9 / 6. Conclusion - extractive body cue:** Impact Statement Although our FEEDTTA leads significant performance improvements, it does not guarantee perfect prediction across the diverse environment.

- **Evidence anchors reviewed:** datasets p. 6 (4.3. Implementation Details), p. 9 (5.4. Effects of Stochastic Gradient Reversion), p. 6 (5.1. Main Navigation Results), p. 7 (5.2. Quality and Quantity of Feedback), p. 7 (5.1. Main Navigation Results), p. 8 (5.4. Effects of Stochastic Gradient Reversion), metrics p. 5 (4.2. Evaluation Metrics), p. 8 (5.3. LLMs as Feedback Oracle), p. 5 (4.2. Evaluation Metrics), p. 8 (5.4. Effects of Stochastic Gradient Reversion), p. 9 (5.4. Effects of Stochastic Gradient Reversion), p. 9 (5.4. Effects of Stochastic Gradient Reversion), baselines p. 6 (5.1. Main Navigation Results), p. 6 (5.1. Main Navigation Results), p. 7 (5.2. Quality and Quantity of Feedback), p. 8 (5.3. LLMs as Feedback Oracle), p. 5 (4.2. Evaluation Metrics), p. 7 (5.2. Quality and Quantity of Feedback), results p. 9 (5.4. Effects of Stochastic Gradient Reversion), p. 5 (4.2. Evaluation Metrics), p. 7 (5.2. Quality and Quantity of Feedback), p. 7 (5.1. Main Navigation Results), p. 9 (5.4. Effects of Stochastic Gradient Reversion), p. 14 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
