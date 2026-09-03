# Evaluation - Temporal Difference Calibration in Sequential Tasks: Application to Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2604.20472; PDF retrieval source: https://arxiv.org/pdf/2604.20472. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 23 (Figure/Table caption), p. 2 (Figure/Table caption), p. 10 (Figure/Table caption), p. 22 (Figure/Table caption), p. 28 (Figure/Table caption), p. 25 (Figure/Table caption)): Figure 5. Extended Analysis of Guided Action Search and TDQC Efficiency. The results demonstrate that RNN-TDQC provides the highest success rates, while the Threshold 0.35 variant offers a significant reduction ...

## Evaluation Body Digest

- **p. 8 / 6.2. Benchmarks - extractive body cue:** Real-World Franka We consider the Franka Emika Panda Robot in Gu et al.
- **p. 8 / 6.2. Benchmarks - extractive body cue:** An episode in LIBERO is stopped once the robot completes its task.
- **p. 7 / 6. Experiments - extractive body cue:** We test TDQC, our sequentially calibrated success predictor in sequential tasks.
- **p. 28 / Figure/Table caption - extractive body cue:** Figure 11. Analysis of VLA Calibration and Success Rates. (a-f) Scatter plots showing the strong negative correlation between Brier Score at Stop Time ( ˆT) ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Sequential Brier scores across benchmarks. Sequential Brier score (lower is better) on an unseen validation set averaged over 21 random seeds (train/validation task ...
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 5. Extended Analysis of Guided Action Search and TDQC Efficiency. The results demonstrate that RNN-TDQC provides the highest success rates, while the Threshold 0.35 ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 4. Averaged success rates over additional simulation steps for action selection configurations. All experiments evalu- ate 3 unseen tasks from LIBERO-10 taken with OpenVLA, ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 5. LIBERO-10 Task success rates across models LIBERO-10 We evaluate the VLA models on LIBERO-10, which consists of 10 long-horizon manipulation tasks and contains ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** 6. Experiments (p. 7); 6.2. Benchmarks (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5. Extended Analysis of Guided Action Search and TDQC Efficiency. The results demonstrate that RNN-TDQC provides the highest success rates, while the Threshold ... | p. 23 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. Sequential Brier scores across benchmarks. Sequential Brier score (lower is better) on an unseen validation set averaged over 21 random seeds (train/validation ... | p. 2 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4. Averaged success rates over additional simulation steps for action selection configurations. All experiments evalu- ate 3 unseen tasks from LIBERO-10 taken with ... | p. 10 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 13. ROC-AUC results on simulation and real robot experiment (higher is better). Results are averaged over 21 seeds that determined different train-test split ... | p. 22 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 11. Analysis of VLA Calibration and Success Rates. (a-f) Scatter plots showing the strong negative correlation between Brier Score at Stop Time ( ... | p. 28 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 6.2. Benchmarks - extractive body cue:** Real-World Franka We consider the Franka Emika Panda Robot in Gu et al.
- **p. 8 / 6.2. Benchmarks - extractive body cue:** An episode in LIBERO is stopped once the robot completes its task.
- **p. 7 / 6. Experiments - extractive body cue:** We test TDQC, our sequentially calibrated success predictor in sequential tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Sequential Brier scores across benchmarks. Sequential Brier score (lower is better) on an unseen validation set averaged over 21 random seeds (train/validation task ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2. Two-step MDP from Example 4.1. success predictor by its two-component decomposition. Let Ft = f(ht) denote the random event that the model predicts ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1. Brier Score results on simulation and real robot experiment. Results are averaged over 21 seeds which determine different train-test splits of the tasks. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. ROC-AUC results on simulation and real robot experiment. Results are averaged over 21 seeds which determine different train-test splits of the tasks. "-" ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 3. ROC-AUC vs Brier score over all learned baselines in all benchmarks at the minimum rollout length. Points are grouped by method and split, ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 4. Averaged success rates over additional simulation steps for action selection configurations. All experiments evalu- ate 3 unseen tasks from LIBERO-10 taken with OpenVLA, ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 3. Benchmark statistics: task split into seen/unseen subsets and corresponding numbers of training and evaluation rollouts. Table 3 summarize each benchmark statistics on the ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 4. Episode horizon by benchmark and model. We report the maximum rollout length (environment time limit) used in each evaluation setting.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Real-World Franka We consider the Franka Emika Panda Robot in Gu et al. | embodiment, simulator version and control stack | p. 8 (6.2. Benchmarks), p. 8 (6.2. Benchmarks) |
| Task/environment | An episode in LIBERO is stopped once the robot completes its task. | reset, timeout, object/scene variation | p. 8 (6.2. Benchmarks), p. 7 (6. Experiments) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 6 (5. Method), p. 7 (1. TD loss improves calibration and failure detection re) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 2 (1. Introduction), p. 6 (5. Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 11. Analysis of VLA Calibration and Success Rates. (a-f) Scatter plots showing the strong negative correlation between Brier Score at Stop Time ( ... | definition/direction/unit from same section | p. 28 (Figure/Table caption) |
| Figure 1. Sequential Brier scores across benchmarks. Sequential Brier score (lower is better) on an unseen validation set averaged over 21 random seeds (train/validation ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 5. Extended Analysis of Guided Action Search and TDQC Efficiency. The results demonstrate that RNN-TDQC provides the highest success rates, while the Threshold ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| Figure 4. Averaged success rates over additional simulation steps for action selection configurations. All experiments evalu- ate 3 unseen tasks from LIBERO-10 taken with ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Table 5. LIBERO-10 Task success rates across models LIBERO-10 We evaluate the VLA models on LIBERO-10, which consists of 10 long-horizon manipulation tasks and ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| Figure 6. Failures and successes detected by RNN-TDQC (top-10 probabilities) align with the actual robot failures, as shown in the observations from OpenVLA + ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |
| Table 16. Performance degregation as a function of failed trajectories, evaluated on π0-FAST LIBERO-10 (unseen tasks). We vary the proportion of failed trajectories retained ... | definition/direction/unit from same section | p. 26 (Figure/Table caption) |
| Figure 3. ROC-AUC vs Brier score over all learned baselines in all benchmarks at the minimum rollout length. Points are grouped by method and ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 5. Extended Analysis of Guided Action Search and TDQC Efficiency. The results demonstrate that RNN-TDQC provides the highest success rates, while the Threshold ... | comparison identity and matched condition | p. 23 (Figure/Table caption) |
| Table 15. Computational cost of all failure prediction methods trained on π0-FAST LIBERO-10 benchmark. Columns report reserved and peak GPU VRAM (MB), number of ... | comparison identity and matched condition | p. 24 (Figure/Table caption) |
| Figure 1. Sequential Brier scores across benchmarks. Sequential Brier score (lower is better) on an unseen validation set averaged over 21 random seeds (train/validation ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Figure 3. ROC-AUC vs Brier score over all learned baselines in all benchmarks at the minimum rollout length. Points are grouped by method and ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Table 3. Benchmark statistics: task split into seen/unseen subsets and corresponding numbers of training and evaluation rollouts. Table 3 summarize each benchmark statistics on ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |
| Table 13. ROC-AUC results on simulation and real robot experiment (higher is better). Results are averaged over 21 seeds that determined different train-test split ... | comparison identity and matched condition | p. 22 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 1. Sequential Brier scores across benchmarks. Sequential Brier score (lower is better) on an unseen validation set averaged over 21 random seeds (train/validation ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Figure 5. Extended Analysis of Guided Action Search and TDQC Efficiency. The results demonstrate that RNN-TDQC provides the highest success rates, while the Threshold ... | component/input/data sensitivity | p. 23 (Figure/Table caption) |
| Figure 9. Ablation results for TD methods Overall, we see that TD-0 with the top 10 probabilities achieve best performance 25 | component/input/data sensitivity | p. 25 (Figure/Table caption) |
| Figure 7. Successful rollout with informative failure scores of TDQC top 10 probabilities on OpenVLA LIBERO-10 benckmark. task: "put both the alphabet soup and ... | component/input/data sensitivity | p. 25 (Figure/Table caption) |
| Figure 2. Two-step MDP from Example 4.1. success predictor by its two-component decomposition. Let Ft = f(ht) denote the random event that the model ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Figure 11. Analysis of VLA Calibration and Success Rates. (a-f) Scatter plots showing the strong negative correlation between Brier Score at Stop Time ( ... | component/input/data sensitivity | p. 28 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Before that, in Algorithm 1, we provide a brief summary of our method, which we call TemporalDifference Q-based Calibration, TDQC for short. | Figure 5. Extended Analysis of Guided Action Search and TDQC Efficiency. The results demonstrate that RNN-TDQC provides the highest success rates, while the Threshold ... | PDF body cue; verify exact table/figure and matched conditions | p. 23 (Figure/Table caption), p. 2 (Figure/Table caption), p. 10 (Figure/Table caption), p. 22 (Figure/Table caption), p. 28 (Figure/Table caption), p. 25 (Figure/Table caption) |
| Primary metric/result | Figure 1. Sequential Brier scores across benchmarks. Sequential Brier score (lower is better) on an unseen validation set averaged over 21 random seeds (train/validation ... | numeric claim only at cited anchor | p. 2 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 8 / 6.2. Benchmarks - extractive body cue:** The dataset contains 532 rollouts on 8 lifting pick-and-place tasks.
- **p. 8 / 6.2. Benchmarks - extractive body cue:** All tasks have rollouts with exactly Ti = 50 steps; if the policy succeeds earlier, the robot keeps taking actions in the environment until reaching ...
- **p. 5 / 5. Method - extractive body cue:** The future rewards predictor ˆf(ht) that minimizes the Sequential Brier Score Eπ ht∈Ht h Eπ hT ∈HT h ( ˆf(ht) -R(hT ))2 / ht ii ...
- **p. 8 / 6.1. Vision-Language-Action Models - extractive body cue:** Results are averaged over 21 seeds which determine different train-test splits of the tasks. "-" indicates that the Brier score can't be calculated on the ...
- **p. 8 / 6.1. Vision-Language-Action Models - extractive body cue:** Results are averaged over 21 seeds which determine different train-test splits of the tasks. "-" indicates that the ROC-AUC can't be calculated on the method.
- **p. 10 / 6.6. Application to guided test-time action search - extractive body cue:** To increase variance in sampled actions, we generated 10 samples per timestep in all value guided methods using a sampling temperature of 1.5.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 4. Averaged success rates over additional simulation steps for action selection configurations. All experiments evalu- ate 3 unseen tasks from LIBERO-10 taken with ... | p. 10 (Figure/Table caption) |
| body limitation/failure cue | Figure 6. Failures and successes detected by RNN-TDQC (top-10 probabilities) align with the actual robot failures, as shown in the observations from OpenVLA + ... | p. 24 (Figure/Table caption) |
| body limitation/failure cue | A failure is flagged once the conformal prediction threshold is exceeded. | p. 9 (6.4. TD loss improves calibration and failure detection) |
| body limitation/failure cue | Methods with lower sequential Brier score tend to achieve higher ROC-AUC, suggesting that better calibrated success probabilities are useful for failure detection. | p. 9 (6.4. TD loss improves calibration and failure detection) |
| body limitation/failure cue | First, we observe that the failure predictor generalizes across unseen tasks within an environment but not across environments, embodiments, or action parameterizations. | p. 10 (7. Conclusion and Future Works) |
| body limitation/failure cue | Figure 7. Successful rollout with informative failure scores of TDQC top 10 probabilities on OpenVLA LIBERO-10 benckmark. task: "put both the alphabet soup and ... | p. 25 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our goal is to understand, during the run of the policy, whether it will succeed or fail in its task. | p. 4 (4. Problem Formulation) |
| We would like to evaluate success during the run of the policy, and we henceforth define a sequential counterpart to the conventional Brier score ... | p. 4 (4. Problem Formulation) |
| 2021 for details) to compute a time-varying confidence upper bound {δt}T t=1. | p. 6 (5.1. Early Stopping with Conformal Prediction) |
| The target network parameters θ-are updated with the current parameters θ every C steps and are held fixed between individual updates. | p. 6 (5. Method) |
| The pseudocode of the procedure is reported in Algorithm 3. | p. 7 (5.2. Application to Test-Time Guided Action Search) |
| To reduce test-time compute using the calibrated model, we apply the action search only when the predicted Q value exceeds a threshold ¯T. | p. 7 (5.2. Application to Test-Time Guided Action Search) |
| (2025) using π0-FAST-DROID checkpoints (Pertsch et al., 2025). | p. 8 (6.2. Benchmarks) |
| Real-World WidowX We consider the WidowX data and OpenVLA checkpoints published in Gu et al. | p. 8 (6.2. Benchmarks) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / Figure/Table caption - extractive body cue:** Figure 4. Averaged success rates over additional simulation steps for action selection configurations. All experiments evalu- ate 3 unseen tasks from LIBERO-10 taken with OpenVLA, ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 6. Failures and successes detected by RNN-TDQC (top-10 probabilities) align with the actual robot failures, as shown in the observations from OpenVLA + LIBERO-10 ...
- **p. 9 / 6.4. TD loss improves calibration and failure detection - extractive body cue:** A failure is flagged once the conformal prediction threshold is exceeded.
- **p. 9 / 6.4. TD loss improves calibration and failure detection - extractive body cue:** Methods with lower sequential Brier score tend to achieve higher ROC-AUC, suggesting that better calibrated success probabilities are useful for failure detection.
- **p. 10 / 7. Conclusion and Future Works - extractive body cue:** First, we observe that the failure predictor generalizes across unseen tasks within an environment but not across environments, embodiments, or action parameterizations.
- **p. 25 / Figure/Table caption - extractive body cue:** Figure 7. Successful rollout with informative failure scores of TDQC top 10 probabilities on OpenVLA LIBERO-10 benckmark. task: "put both the alphabet soup and the ...

- **Evidence anchors reviewed:** datasets p. 8 (6.2. Benchmarks), p. 8 (6.2. Benchmarks), p. 7 (6. Experiments), metrics p. 28 (Figure/Table caption), p. 2 (Figure/Table caption), p. 23 (Figure/Table caption), p. 10 (Figure/Table caption), p. 18 (Figure/Table caption), p. 24 (Figure/Table caption), baselines p. 23 (Figure/Table caption), p. 24 (Figure/Table caption), p. 2 (Figure/Table caption), p. 9 (Figure/Table caption), p. 17 (Figure/Table caption), p. 22 (Figure/Table caption), results p. 23 (Figure/Table caption), p. 2 (Figure/Table caption), p. 10 (Figure/Table caption), p. 22 (Figure/Table caption), p. 28 (Figure/Table caption), p. 25 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (31 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 3. Benchmark statistics: task split into seen/unseen subsets and corresponding numbers of training and evaluation rollouts. Table 3 summarize each benchmark statistics on the number of tasks and rollouts. ... (p. 17, Figure/Table caption).
- **Metric evidence:** Table 16. Performance degregation as a function of failed trajectories, evaluated on π0-FAST LIBERO-10 (unseen tasks). We vary the proportion of failed trajectories retained during training from 100% down to ... (p. 26, Figure/Table caption).
- **Baseline/ablation evidence:** Figure 5. Extended Analysis of Guided Action Search and TDQC Efficiency. The results demonstrate that RNN-TDQC provides the highest success rates, while the Threshold 0.35 variant offers a significant reduction ... (p. 23, Figure/Table caption).
- **Failure/negative evidence:** We evaluate failure detection using ROC-AUC, which measures how well a score ranks failed rollouts above successful ones and is widely used for uncertainty quantification in LLMs (Huang et al., ... (p. 9, 6.4. TD loss improves calibration and failure detection).
