# Evaluation - SAFE: Multitask Failure Detection for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (36 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.neurips.cc/paper_files/paper/2025/hash/392d0d05e2f514063e6ce6f8b370834c-Abstract-Conference.html; PDF retrieval source: https://proceedings.neurips.cc/paper_files/paper/2025/file/392d0d05e2f514063e6ce6f8b370834c-Paper-Conference.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (6 Results), p. 10 (Figure/Table caption), p. 9 (6 Results), p. 9 (6 Results), p. 27 (Figure/Table caption), p. 6 (5 Experiments)): 75.54 53.93 82.37 70.00 Euclid. k-NN 80.35 60.27 72.01 53.64 Cosine k-NN 80.23 59.51 74.76 65.88 PCA-KMeans 49.98 51.03 75.62 47.22 RND 62.00 45.83 66.68 47.67 LogpZO 64.43 52.24 62.94 ...

## Evaluation Body Digest

- **p. 6 / 5 Experiments - extractive body cue:** Real-world WidowX Experiments: We also deploy the OpenVLA model pretrained on the "Open-X Magic Soup++" dataset [2] on a WidowX robot manipulator in our lab.
- **p. 6 / 5 Experiments - extractive body cue:** Real-world Franka Experiments: We deploy the π0-FAST-DROID checkpoint [4, 5]1 on a Franka Emika Panda Robot.
- **p. 9 / 6 Results - extractive body cue:** Averaged across simulation benchmarks, SAFE-MLP and SAFE-LSTM have similar performance, both outperforming the best baseline by 4-5% on unseen tasks, while still achieving the best ...
- **p. 10 / 6 Results - extractive body cue:** ROC-AUC values are averaged over five random seeds with different task splits. on par with the best baseline on the other two benchmarks.
- **p. 7 / 5 Experiments - extractive body cue:** Franka Emika Panda Robot ZED 2 Camera ZED Mini Camera "pick up the lid and place it on the pot" "pick up the marker and ...
- **p. 9 / 6 Results - extractive body cue:** Distr. methods perform well, achieving the best performance in two simulation benchmarks (π0 and π0-FAST) and are the second best in the real world.
- **p. 10 / 6 Results - extractive body cue:** This early detection allows early intervention for policy failures before they get stuck in execution or cause harm to the real-world environment.
- **p. 6 / 5 Experiments - extractive body cue:** We exclude the "pick up coke" task because π∗ 0 rarely fails on it (success rate at 98%).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 5 Experiments (p. 6); 6 Results (p. 9); B Experiment Details (p. 23); B.5 Benchmark Details (p. 24); B.6 Benchmark Statistics (p. 25); C Additional Results (p. 26); C.2 Conformal Prediction Results (p. 27); C.4 Result Variance (p. 28).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 6 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | 75.54 53.93 82.37 70.00 Euclid. k-NN 80.35 60.27 72.01 53.64 Cosine k-NN 80.23 59.51 74.76 65.88 PCA-KMeans 49.98 51.03 75.62 47.22 RND 62.00 45.83 ... | p. 10 (6 Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6: SAFE-MLP achieves the best failure detection performance in real-world experiments with both π0-FAST Franka and OpenVLA WidowX. Plot (a) presents quantitative results, ... | p. 10 (Figure/Table caption) |
| 6 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | With a higher ROC-AUC metric, a failure detector achieves higher accuracy averaged over all possible thresholds. | p. 9 (6 Results) |
| 6 Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Averaged across simulation benchmarks, SAFE-MLP and SAFE-LSTM have similar performance, both outperforming the best baseline by 4-5% on unseen tasks, while still achieving the ... | p. 9 (6 Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. However, the visualized embeddings of π0-FAST on the real Franka robot (Fig. 8e and f) are different, where embeddings from successful and ... | p. 27 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 5 Experiments - extractive body cue:** Real-world WidowX Experiments: We also deploy the OpenVLA model pretrained on the "Open-X Magic Soup++" dataset [2] on a WidowX robot manipulator in our lab.
- **p. 6 / 5 Experiments - extractive body cue:** Real-world Franka Experiments: We deploy the π0-FAST-DROID checkpoint [4, 5]1 on a Franka Emika Panda Robot.
- **p. 9 / 6 Results - extractive body cue:** Averaged across simulation benchmarks, SAFE-MLP and SAFE-LSTM have similar performance, both outperforming the best baseline by 4-5% on unseen tasks, while still achieving the best ...
- **p. 10 / 6 Results - extractive body cue:** ROC-AUC values are averaged over five random seeds with different task splits. on par with the best baseline on the other two benchmarks.
- **p. 7 / 5 Experiments - extractive body cue:** Franka Emika Panda Robot ZED 2 Camera ZED Mini Camera "pick up the lid and place it on the pot" "pick up the marker and ...
- **p. 9 / 6 Results - extractive body cue:** Distr. methods perform well, achieving the best performance in two simulation benchmarks (π0 and π0-FAST) and are the second best in the real world.
- **p. 10 / 6 Results - extractive body cue:** This early detection allows early intervention for policy failures before they get stuck in execution or cause harm to the real-world environment.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1: The internal features of a VLA capture high-level information about task success and failure. When the VLA is failing, the features, even those ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: The proposed failure detector, SAFE, has three major components: (1) SAFE extracts the latent feature from the last layer of a VLA model; ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Failure detection results on simulation benchmarks, measured by area under ROC (ROC- AUC). "-" indicates that the failure detection method does not apply. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Illustration of real-world experiment setup (left) and example rollouts collected (right). a total of 532 rollouts on the 8 lifting and pick-and-place tasks, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: In all simulation experiments, the proposed SAFE-LSTM and SAFE-MLP perform better than or on par with the best baselines. The plots show the ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Failures detected by SAFE-LSTM align well with the actual robot failures, as shown in the corresponding camera observations from simulation experiments. The blue-shaded ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 6: SAFE-MLP achieves the best failure detection performance in real-world experiments with both π0-FAST Franka and OpenVLA WidowX. Plot (a) presents quantitative results, while ...
- **p. 25 / Figure/Table caption - extractive body cue:** Table 2: List of tasks used in π∗ 0 + SimplerEnv benchmark. Embodiment Task ID Environment Name π∗

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Real-world WidowX Experiments: We also deploy the OpenVLA model pretrained on the "Open-X Magic Soup++" dataset [2] on a WidowX robot manipulator in our ... | embodiment, simulator version and control stack | p. 6 (5 Experiments), p. 6 (5 Experiments) |
| Task/environment | Real-world Franka Experiments: We deploy the π0-FAST-DROID checkpoint [4, 5]1 on a Franka Emika Panda Robot. | reset, timeout, object/scene variation | p. 6 (5 Experiments), p. 9 (6 Results) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 5 (4 Method), p. 1 (1 Introduction) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 2 (1 Introduction), p. 4 (4 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We exclude the "pick up coke" task because π∗ 0 rarely fails on it (success rate at 98%). | definition/direction/unit from same section | p. 6 (5 Experiments) |
| 6(b-c), where failure scores stop increasing after task completion. | definition/direction/unit from same section | p. 10 (6 Results) |
| Comparing SAFE's performance with the GT fail time, we can see that SAFE can detect failures with high accuracy in the early stages of ... | definition/direction/unit from same section | p. 10 (6 Results) |
| Figure 4: In all simulation experiments, the proposed SAFE-LSTM and SAFE-MLP perform better than or on par with the best baselines. The plots show ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| 6.2 What is the trade-off between detection accuracy and time using functional CP? | definition/direction/unit from same section | p. 9 (6 Results) |
| With a higher ROC-AUC metric, a failure detector achieves higher accuracy averaged over all possible thresholds. | definition/direction/unit from same section | p. 9 (6 Results) |
| Table 1. However, the visualized embeddings of π0-FAST on the real Franka robot (Fig. 8e and f) are different, where embeddings from successful and ... | definition/direction/unit from same section | p. 27 (Figure/Table caption) |
| Figure 2: The proposed failure detector, SAFE, has three major components: (1) SAFE extracts the latent feature from the last layer of a VLA ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Averaged across simulation benchmarks, SAFE-MLP and SAFE-LSTM have similar performance, both outperforming the best baseline by 4-5% on unseen tasks, while still achieving the ... | comparison identity and matched condition | p. 9 (6 Results) |
| Table 1. However, the visualized embeddings of π0-FAST on the real Franka robot (Fig. 8e and f) are different, where embeddings from successful and ... | comparison identity and matched condition | p. 27 (Figure/Table caption) |
| The proposed SAFE methods perform better or on par with the best baselines, consistently in all settings. | comparison identity and matched condition | p. 9 (6 Results) |
| This is negligible compared to large VLA models. | comparison identity and matched condition | p. 10 (6 Results) |
| ROC-AUC values are averaged over five random seeds with different task splits. on par with the best baseline on the other two benchmarks. | comparison identity and matched condition | p. 10 (6 Results) |
| Figure 3: Illustration of real-world experiment setup (left) and example rollouts collected (right). a total of 532 rollouts on the 8 lifting and pick-and-place ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| On SimplerEnv, we test pretrained π0 models from a reproduction [64], which we denote as π∗ 0 in this paper. | component/input/data sensitivity | p. 6 (5 Experiments) |
| Real-world WidowX Experiments: We also deploy the OpenVLA model pretrained on the "Open-X Magic Soup++" dataset [2] on a WidowX robot manipulator in our ... | component/input/data sensitivity | p. 6 (5 Experiments) |
| Figure 2: The proposed failure detector, SAFE, has three major components: (1) SAFE extracts the latent feature from the last layer of a VLA ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The contributions of our paper can be summarized as follows: • We analyze the VLA feature space and show that, across different task instructions ... | 75.54 53.93 82.37 70.00 Euclid. k-NN 80.35 60.27 72.01 53.64 Cosine k-NN 80.23 59.51 74.76 65.88 PCA-KMeans 49.98 51.03 75.62 47.22 RND 62.00 45.83 ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (6 Results), p. 10 (Figure/Table caption), p. 9 (6 Results), p. 9 (6 Results), p. 27 (Figure/Table caption), p. 6 (5 Experiments) |
| Primary metric/result | Figure 6: SAFE-MLP achieves the best failure detection performance in real-world experiments with both π0-FAST Franka and OpenVLA WidowX. Plot (a) presents quantitative results, ... | numeric claim only at cited anchor | p. 10 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 5 Experiments - extractive body cue:** In experiments, 3 out of 10 tasks are randomly picked and reserved as unseen tasks.
- **p. 6 / 5 Experiments - extractive body cue:** This leaves 4 tasks for each embodiment, among which 3 tasks are seen and 1 task is unseen.
- **p. 6 / 5 Experiments - extractive body cue:** We design 13 tasks and collect 30 successful and 30 failed rollouts for each task.
- **p. 6 / 5 Experiments - extractive body cue:** In experiments, 3 tasks out of 13 are randomly selected as unseen tasks.
- **p. 10 / 6 Results - extractive body cue:** SAFE uses a 1-2 layer MLP or LSTM and poses a minimal (less than 1%) computational overhead at runtime.
- **p. 10 / 6 Results - extractive body cue:** For example, SAFE-LSTM contains 2.3 million parameters and introduces an additional 0.73 ms of inference time.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1: The internal features of a VLA capture high-level information about task success and failure. When the VLA is failing, the features, even ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Figure 5: Failures detected by SAFE-LSTM align well with the actual robot failures, as shown in the corresponding camera observations from simulation experiments. The ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | Table 1: Failure detection results on simulation benchmarks, measured by area under ROC (ROC- AUC). "-" indicates that the failure detection method does not ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Inspired by this observation, we design SAFE, which uses the internal features of VLAs for failure detection. | p. 5 (3. Calibrate failure detection) |
| body limitation/failure cue | If the predicted score exceeds the threshold during testing, SAFE confidently detects a failure. timely manner. | p. 5 (3. Calibrate failure detection) |
| body limitation/failure cue | We use uppert as the failure flag threshold δt, and more details about functional CP can be found in Appendix. | p. 6 (3. Calibrate failure detection) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We adopt the model checkpoints that are finetuned on the LIBERO benchmark and released by their authors. | p. 6 (5 Experiments) |
| Real-world Franka Experiments: We deploy the π0-FAST-DROID checkpoint [4, 5]1 on a Franka Emika Panda Robot. | p. 6 (5 Experiments) |
| For instance, pi0 has 3.3 billion parameters and an inference time of 149 ms. | p. 10 (6 Results) |
| For example, SAFE-LSTM contains 2.3 million parameters and introduces an additional 0.73 ms of inference time. | p. 10 (6 Results) |
| 1(c), we can see that failure rollout initially stays out of the "failure zone" when it progresses normally, and when the robot mistakenly drops ... | p. 4 (4 Method) |
| Encoder 𝒐𝑡 𝑙𝑡 Decoder 𝒆𝑡 Action: 𝑨𝑡 Observation Instruction VLA Model 𝒆1 SAFE-MLP SAFE-LSTM MLP ǁ𝑠1 𝒆2 MLP ǁ𝑠2 𝒆3 MLP ǁ𝑠3 𝒆𝑇 MLP ... | p. 5 (4 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1: The internal features of a VLA capture high-level information about task success and failure. When the VLA is failing, the features, even those ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Failures detected by SAFE-LSTM align well with the actual robot failures, as shown in the corresponding camera observations from simulation experiments. The blue-shaded ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Failure detection results on simulation benchmarks, measured by area under ROC (ROC- AUC). "-" indicates that the failure detection method does not apply. ...
- **p. 5 / 3. Calibrate failure detection - extractive body cue:** Inspired by this observation, we design SAFE, which uses the internal features of VLAs for failure detection.
- **p. 5 / 3. Calibrate failure detection - extractive body cue:** If the predicted score exceeds the threshold during testing, SAFE confidently detects a failure. timely manner.
- **p. 6 / 3. Calibrate failure detection - extractive body cue:** We use uppert as the failure flag threshold δt, and more details about functional CP can be found in Appendix.

- **Evidence anchors reviewed:** datasets p. 6 (5 Experiments), p. 6 (5 Experiments), p. 9 (6 Results), p. 10 (6 Results), p. 7 (5 Experiments), p. 9 (6 Results), metrics p. 6 (5 Experiments), p. 10 (6 Results), p. 10 (6 Results), p. 8 (Figure/Table caption), p. 9 (6 Results), p. 9 (6 Results), baselines p. 9 (6 Results), p. 27 (Figure/Table caption), p. 9 (6 Results), p. 10 (6 Results), p. 10 (6 Results), p. 7 (Figure/Table caption), results p. 10 (6 Results), p. 10 (Figure/Table caption), p. 9 (6 Results), p. 9 (6 Results), p. 27 (Figure/Table caption), p. 6 (5 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (36 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 6: SAFE-MLP achieves the best failure detection performance in real-world experiments with both π0-FAST Franka and OpenVLA WidowX. Plot (a) presents quantitative results, while (b-e) show qualitative examples from ... (p. 10, Figure/Table caption).
- **Metric evidence:** We exclude the "pick up coke" task because π∗ 0 rarely fails on it (success rate at 98%). (p. 6, 5 Experiments).
- **Baseline/ablation evidence:** Averaged across simulation benchmarks, SAFE-MLP and SAFE-LSTM have similar performance, both outperforming the best baseline by 4-5% on unseen tasks, while still achieving the best performance on seen tasks. (p. 9, 6 Results).
- **Failure/negative evidence:** This means that the human annotator does not think these rollouts are failures until the very last moment, where the VLA model is probably on the right track and fails ... (p. 28, C.3 Failure Detection Time).
