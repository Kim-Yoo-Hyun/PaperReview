# Evaluation - MOPO: Model-based Offline Policy Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2005.13239; PDF retrieval source: https://arxiv.org/pdf/2005.13239. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 18 (Figure/Table caption), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 2 (Figure/Table caption)): Table 2: Average returns halfcheetah-jump and ant-angle that require out-of-distribution policy. The MOPO results are averaged over 6 random seeds, ± standard deviation, while the results of other methods are ...

## Evaluation Body Digest

- **p. 7 / 5 Experiments - extractive body cue:** 5.1 Evaluation on the D4RL benchmark To answer question (1), we evaluate our method on a large subset of datasets in the D4RL benchmark [18] ...
- **p. 8 / 5 Experiments - extractive body cue:** The datasets in this benchmark have been generated as follows: random: roll out a randomly initialized policy for 1M steps. medium: partially train a policy ...
- **p. 8 / 5 Experiments - extractive body cue:** In particular, model-free offline RL cannot outperform the best trajectory in the batch dataset, whereas MOPO exceeds the batch max by a significant margin.
- **p. 7 / 5 Experiments - extractive body cue:** In our experiments, we aim to study the follow questions: (1) How does MOPO perform on standard offline RL benchmarks in comparison to prior state-of-the-art ...
- **p. 9 / 5 Experiments - extractive body cue:** In halfcheetah-jump, the agent is asked to run while jumping as high as possible given an training offline dataset of halfcheetah running.
- **p. 9 / 5 Experiments - extractive body cue:** We include the mean and max undiscounted return of the episodes in the batch data (under Batch Mean and Batch Max, respectively) for comparison.
- **p. 7 / 5 Experiments - extractive body cue:** To extend the theory to an unknown reward function, we can consider the reward as being concatenated onto the state, so that the admissible error ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Results for D4RL datasets. Each number is the normalized score proposed in [18] of the policy at the last iteration of training, averaged ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** offline robot transition/trajectory dataset과 deployment MDP.
- **Input boundary:** dataset state/observation, action, reward와 return-to-go.
- **Output/decision under evaluation:** dataset-supported action sequence.
- **Primary target:** offline policy value, OOD safety와 closed-loop success.
- **Detected evaluation headings:** 5 Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SIMULATION | Table 2: Average returns halfcheetah-jump and ant-angle that require out-of-distribution policy. The MOPO results are averaged over 6 random seeds, ± standard deviation, while ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Table 2. We observe that different reward penalties can all lead to substantial improvement of the performance and reward penalty based on learned variance ... | p. 18 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / SIMULATION | In Table 2, we show that MOPO significantly outperforms the state-of-the-art model-free approaches. | p. 8 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SIMULATION | Thus, to achieve good performance for the new reward functions, the policy need to leave the observational distribution, as visualized in Figure 2. | p. 8 (5 Experiments) |
| 5 Experiments | EMPIRICAL / SIMULATION | As shown in the results, MOPO outperforms all the baselines by a large margin, indicating that MOPO is effective in generalizing to out-of-distribution states ... | p. 9 (5 Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 5 Experiments - extractive body cue:** 5.1 Evaluation on the D4RL benchmark To answer question (1), we evaluate our method on a large subset of datasets in the D4RL benchmark [18] ...
- **p. 8 / 5 Experiments - extractive body cue:** The datasets in this benchmark have been generated as follows: random: roll out a randomly initialized policy for 1M steps. medium: partially train a policy ...
- **p. 8 / 5 Experiments - extractive body cue:** In particular, model-free offline RL cannot outperform the best trajectory in the batch dataset, whereas MOPO exceeds the batch max by a significant margin.
- **p. 7 / 5 Experiments - extractive body cue:** In our experiments, we aim to study the follow questions: (1) How does MOPO perform on standard offline RL benchmarks in comparison to prior state-of-the-art ...
- **p. 9 / 5 Experiments - extractive body cue:** In halfcheetah-jump, the agent is asked to run while jumping as high as possible given an training offline dataset of halfcheetah running.
- **p. 9 / 5 Experiments - extractive body cue:** We include the mean and max undiscounted return of the episodes in the batch data (under Batch Mean and Batch Max, respectively) for comparison.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Comparison between vanilla model-based RL (MBPO [29]) with or without model ensembles and vanilla model-free RL (SAC [27]) on two offline RL tasks: ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Results for D4RL datasets. Each number is the normalized score proposed in [18] of the policy at the last iteration of training, averaged ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 2: We visualize the two out-of-distribution generalization environments halfcheetah-jump (bottom row) and ant-angle (top row). We show the training environments that generate the batch ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Average returns halfcheetah-jump and ant-angle that require out-of-distribution policy. The MOPO results are averaged over 6 random seeds, ± standard deviation, while the ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 3: Ablation study on two D4RL tasks halfcheetah-mixed and walker2d-mixed and two out-of- distribution tasks halfcheetah-jump and ant-angle. We use average returns where the ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 2. We observe that different reward penalties can all lead to substantial improvement of the performance and reward penalty based on learned variance is ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 4: Limit of generalization on ant-angle. F Experiments on HIV domains Beyond continous control tasks in MuJoCo, we test MOPO on an HIV treatment ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 5: HIV treatment results, averaged over 3 random seeds. G Experiment Details G.1 Details of out-of-distribution environments For halfcheetah-jump, the reward function that we ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 5.1 Evaluation on the D4RL benchmark To answer question (1), we evaluate our method on a large subset of datasets in the D4RL benchmark ... | embodiment, simulator version and control stack | p. 7 (5 Experiments), p. 8 (5 Experiments) |
| Task/environment | The datasets in this benchmark have been generated as follows: random: roll out a randomly initialized policy for 1M steps. medium: partially train a ... | reset, timeout, object/scene variation | p. 8 (5 Experiments), p. 8 (5 Experiments) |
| Observation/sensor | dataset state/observation, action, reward와 return-to-go | calibration, preprocessing, privileged input | p. 4 (3 Preliminaries), p. 2 (1 Introduction) |
| Output/decision | dataset-supported action sequence | action frame, controller and termination | p. 3 (3 Preliminaries), p. 3 (3 Preliminaries) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| To extend the theory to an unknown reward function, we can consider the reward as being concatenated onto the state, so that the admissible ... | definition/direction/unit from same section | p. 7 (5 Experiments) |
| Table 1: Results for D4RL datasets. Each number is the normalized score proposed in [18] of the policy at the last iteration of training, ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Thus, to achieve good performance for the new reward functions, the policy need to leave the observational distribution, as visualized in Figure 2. | definition/direction/unit from same section | p. 8 (5 Experiments) |
| Table 2. We observe that different reward penalties can all lead to substantial improvement of the performance and reward penalty based on learned variance ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| The theory in Sections 4.1 and 4.2 applies to the case where the reward function is known. | definition/direction/unit from same section | p. 7 (5 Experiments) |
| In ant-angle, the ant is rewarded for running forward in a 30 degree angle and the corresponding training offline dataset contains data of the ... | definition/direction/unit from same section | p. 9 (5 Experiments) |
| Table 2: Average returns halfcheetah-jump and ant-angle that require out-of-distribution policy. The MOPO results are averaged over 6 random seeds, ± standard deviation, while ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Table 5: HIV treatment results, averaged over 3 random seeds. G Experiment Details G.1 Details of out-of-distribution environments For halfcheetah-jump, the reward function that ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compare against several baselines, including the current state-of-the-art model-free offline RL algorithms. | comparison identity and matched condition | p. 7 (5 Experiments) |
| In Table 2, we show that MOPO significantly outperforms the state-of-the-art model-free approaches. | comparison identity and matched condition | p. 8 (5 Experiments) |
| As shown in the results, MOPO outperforms all the baselines by a large margin, indicating that MOPO is effective in generalizing to out-of-distribution states ... | comparison identity and matched condition | p. 9 (5 Experiments) |
| Table 2: Average returns halfcheetah-jump and ant-angle that require out-of-distribution policy. The MOPO results are averaged over 6 random seeds, ± standard deviation, while ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Figure 1: Comparison between vanilla model-based RL (MBPO [29]) with or without model ensembles and vanilla model-free RL (SAC [27]) on two offline RL ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| In our experiments, we aim to study the follow questions: (1) How does MOPO perform on standard offline RL benchmarks in comparison to prior ... | comparison identity and matched condition | p. 7 (5 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To answer question (3), we conduct a complete ablation study to analyze the effect of each module in MOPO in Appendix D. | component/input/data sensitivity | p. 7 (5 Experiments) |
| Table 3: Ablation study on two D4RL tasks halfcheetah-mixed and walker2d-mixed and two out-of- distribution tasks halfcheetah-jump and ant-angle. We use average returns where ... | component/input/data sensitivity | p. 18 (Figure/Table caption) |
| Figure 1: Comparison between vanilla model-based RL (MBPO [29]) with or without model ensembles and vanilla model-free RL (SAC [27]) on two offline RL ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| (3) How does each component in MOPO affect performance? | component/input/data sensitivity | p. 7 (5 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The primary contribution of this work is an offline model-based RL algorithm that optimizes a policy in an uncertainty-penalized MDP, where the reward function ... | Table 2: Average returns halfcheetah-jump and ant-angle that require out-of-distribution policy. The MOPO results are averaged over 6 random seeds, ± standard deviation, while ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 18 (Figure/Table caption), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 2 (Figure/Table caption) |
| Primary metric/result | Table 2. We observe that different reward penalties can all lead to substantial improvement of the performance and reward penalty based on learned variance ... | numeric claim only at cited anchor | p. 18 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 8 / 5 Experiments - extractive body cue:** Dataset type Environment BC MOPO (ours) MBPO SAC BEAR BRAC-v random halfcheetah 2.1 35.4 ± 2.5 30.7 ± 3.9 30.5 25.5 28.1 random hopper 1.6 ...
- **p. 8 / 5 Experiments - extractive body cue:** We omit BRAC-p in this table for space because BRAC-v obtains higher performance in 10 of these 12 tasks and is only slightly weaker on ...
- **p. 8 / 5 Experiments - extractive body cue:** Then, we assign these trajectories with new rewards that incentivize the cheetach to jump and the ant to run towards the top right corner with ...
- **p. 9 / 5 Experiments - extractive body cue:** In ant-angle, the ant is rewarded for running forward in a 30 degree angle and the corresponding training offline dataset contains data of the ant ...
- **p. 9 / 5 Experiments - extractive body cue:** Environment Batch Mean Batch Max MOPO (ours) MBPO SAC BEAR BRAC-p BRAC-v halfcheetah-jump -1022.6 1808.6 4016.6±144 2971.4±1262 -3588.2±1436 16.8±60 1069.9±232 871±41 ant-angle 866.7 2311.9 2530.9±137 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, uncertainty estimation does not explain the entire difference nor does it explain why model-free methods cannot also enjoy the benefits of uncertainty estimation. | p. 9 (6 Conclusion) |
| body limitation/failure cue | Our work opens up a number of questions and directions for future work. | p. 9 (6 Conclusion) |
| body limitation/failure cue | In particular, model-free offline RL cannot outperform the best trajectory in the batch dataset, whereas MOPO exceeds the batch max by a significant margin. | p. 8 (5 Experiments) |
| body limitation/failure cue | BRACv uses this penalty both when updating the critic and when updating the actor, while BRAC-p uses this penalty only when updating the actor ... | p. 7 (5 Experiments) |
| body limitation/failure cue | Numbers for model-free methods taken from [18], which does not report standard deviation. | p. 8 (5 Experiments) |
| body limitation/failure cue | Figure 1: Comparison between vanilla model-based RL (MBPO [29]) with or without model ensembles and vanilla model-free RL (SAC [27]) on two offline RL ... | p. 2 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For more details on the experimental set-up and hyperparameters, see Appendix G. | p. 7 (5 Experiments) |
| Concretely, we train SAC for 1M steps and use the entire training replay buffer as the trajectories for the batch data. | p. 8 (5 Experiments) |
| Each number is the normalized score proposed in [18] of the policy at the last iteration of training, averaged over 6 random seeds, ± ... | p. 8 (5 Experiments) |
| In halfcheetah-jump, the agent is asked to run while jumping as high as possible given an training offline dataset of halfcheetah running. | p. 9 (5 Experiments) |
| The MOPO results are averaged over 6 random seeds, ± standard deviation, while the results of other methods are averaged over 3 random seeds. | p. 9 (5 Experiments) |
| Reinforcement learning (RL) methods, in contrast, struggle to scale to many real-world applications, e.g., autonomous driving [74] and healthcare [22], because they rely on ... | p. 1 (1 Introduction) |
| Recent advances in machine learning using deep neural networks have shown significant successes in scaling to large realistic datasets, such as ImageNet [13] in ... | p. 1 (1 Introduction) |
| We discuss important practical implementation details in Section 4.3. | p. 4 (3 Preliminaries) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 6 Conclusion - extractive body cue:** However, uncertainty estimation does not explain the entire difference nor does it explain why model-free methods cannot also enjoy the benefits of uncertainty estimation.
- **p. 9 / 6 Conclusion - extractive body cue:** Our work opens up a number of questions and directions for future work.
- **p. 8 / 5 Experiments - extractive body cue:** In particular, model-free offline RL cannot outperform the best trajectory in the batch dataset, whereas MOPO exceeds the batch max by a significant margin.
- **p. 7 / 5 Experiments - extractive body cue:** BRACv uses this penalty both when updating the critic and when updating the actor, while BRAC-p uses this penalty only when updating the actor and ...
- **p. 8 / 5 Experiments - extractive body cue:** Numbers for model-free methods taken from [18], which does not report standard deviation.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Comparison between vanilla model-based RL (MBPO [29]) with or without model ensembles and vanilla model-free RL (SAC [27]) on two offline RL tasks: ...

- **Evidence anchors reviewed:** datasets p. 7 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 7 (5 Experiments), p. 9 (5 Experiments), p. 9 (5 Experiments), metrics p. 7 (5 Experiments), p. 8 (Figure/Table caption), p. 8 (5 Experiments), p. 18 (Figure/Table caption), p. 7 (5 Experiments), p. 9 (5 Experiments), baselines p. 7 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 9 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (5 Experiments), results p. 9 (Figure/Table caption), p. 18 (Figure/Table caption), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (19 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 1: Results for D4RL datasets. Each number is the normalized score proposed in [18] of the policy at the last iteration of training, averaged over 6 random seeds, ± ... (p. 8, Figure/Table caption).
- **Metric evidence:** To extend the theory to an unknown reward function, we can consider the reward as being concatenated onto the state, so that the admissible error estimator bounds the error on ... (p. 7, 5 Experiments).
- **Baseline/ablation evidence:** We compare against several baselines, including the current state-of-the-art model-free offline RL algorithms. (p. 7, 5 Experiments).
- **Failure/negative evidence:** These failures are generally caused by large extrapolation error when the Q-function is evaluated on out-of-distribution actions [19, 36], which can lead to unstable learning and divergence. (p. 1, 1 Introduction).
