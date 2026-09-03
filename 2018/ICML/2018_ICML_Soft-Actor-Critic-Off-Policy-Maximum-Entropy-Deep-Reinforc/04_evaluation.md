# Evaluation - Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v80/haarnoja18b.html; PDF retrieval source: https://arxiv.org/pdf/1801.01290. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5. Experiments), p. 7 (5.1. Comparative Evaluation), p. 6 (5. Experiments), p. 7 (5.2. Ablation Study), p. 8 (5.2. Ablation Study), p. 8 (5.2. Ablation Study)): The stability of the algorithm also plays a large role in performance: easier tasks make it more practical to tune hyperparameters to achieve good results, while the already narrow basins ...

## Evaluation Body Digest

- **p. 6 / 5. Experiments - extractive body cue:** We compare our method to prior techniques on a range of challenging continuous control tasks from the OpenAI gym benchmark suite (Brockman et al., 2016) ...
- **p. 6 / 5. Experiments - extractive body cue:** Although the easier tasks can be solved by a wide range of different algorithms, the more complex benchmarks, such as the 21-dimensional Humanoid (rllab), are ...
- **p. 7 / 5.2. Ablation Study - extractive body cue:** In this comparison, we updated the target value network weights with hard updates, by periodically overwriting the target network parameters to match the current value ...
- **p. 7 / 5.1. Comparative Evaluation - extractive body cue:** The quantitative results attained by SAC in our experiments also compare very favorably to results reported by other methods in prior work (Duan et al., ...
- **p. 8 / 5.2. Ablation Study - extractive body cue:** The optimal reward scale varies between environments, and should be tuned for each task separately.
- **p. 8 / 5.2. Ablation Study - extractive body cue:** Sensitivity of soft actor-critic to selected hyperparameters on Ant-v1 task.
- **p. 8 / 5.2. Ablation Study - extractive body cue:** With the right reward scaling, the model balances exploration and exploitation, leading to faster learning and better asymptotic performance.
- **p. 7 / 5.2. Ablation Study - extractive body cue:** Larger reward magnitudes correspond to lower entries.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** robot/environment의 sequential decision process.
- **Input boundary:** state 또는 observation, action, reward와 transition history.
- **Output/decision under evaluation:** action policy와 induced trajectory.
- **Primary target:** expected return, task success, stability와 sample efficiency.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.1. Comparative Evaluation (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | The stability of the algorithm also plays a large role in performance: easier tasks make it more practical to tune hyperparameters to achieve good ... | p. 6 (5. Experiments) |
| 5.1. Comparative Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results show that, overall, SAC performs comparably to the baseline methods on the easier tasks and outperforms them on the harder tasks with ... | p. 7 (5.1. Comparative Evaluation) |
| 5. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our SQL implementation also includes two Q-functions, which we found to improve its performance in most environments. | p. 6 (5. Experiments) |
| 5.2. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results in the previous section suggest that algorithms based on the maximum entropy principle can outperform conventional RL methods on challenging tasks such ... | p. 7 (5.2. Ablation Study) |
| 5.2. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | We found this variant to benefit from taking more than one gradient step between the environment steps, which can improve performance but also increases ... | p. 8 (5.2. Ablation Study) |

## Dataset / Benchmark Role

- **p. 6 / 5. Experiments - extractive body cue:** We compare our method to prior techniques on a range of challenging continuous control tasks from the OpenAI gym benchmark suite (Brockman et al., 2016) ...
- **p. 6 / 5. Experiments - extractive body cue:** Although the easier tasks can be solved by a wide range of different algorithms, the more complex benchmarks, such as the 21-dimensional Humanoid (rllab), are ...
- **p. 7 / 5.2. Ablation Study - extractive body cue:** In this comparison, we updated the target value network weights with hard updates, by periodically overwriting the target network parameters to match the current value ...
- **p. 7 / 5.1. Comparative Evaluation - extractive body cue:** The quantitative results attained by SAC in our experiments also compare very favorably to results reported by other methods in prior work (Duan et al., ...
- **p. 8 / 5.2. Ablation Study - extractive body cue:** The optimal reward scale varies between environments, and should be tuned for each task separately.
- **p. 8 / 5.2. Ablation Study - extractive body cue:** Sensitivity of soft actor-critic to selected hyperparameters on Ant-v1 task.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 6 / Figure/Table caption - extractive body cue:** Figure 1. Training curves on continuous control benchmarks. Soft actor-critic (yellow) performs consistently across all tasks and outperforming both on-policy and off-policy methods in the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 2. Comparison of SAC (blue) and a deterministic variant of SAC (red) in terms of the stability of individual random seeds on the Humanoid ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3. Sensitivity of soft actor-critic to selected hyperparameters on Ant-v1 task. (a) Evaluating the policy using the mean action generally results in a higher ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 1. SAC Hyperparameters Parameter Value Shared optimizer Adam (Kingma & Ba, 2015) learning rate 3 · 10-4
- **p. 13 / Figure/Table caption - extractive body cue:** Table 2. SAC Environment Specific Parameters Environment Action Dimensions Reward Scale Hopper-v1 3 5 Walker2d-v1
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 4. Training curves for additional baseline (Trust-PCL) and for two SAC variants. Soft actor-critic with hard target update (blue) differs from standard SAC in ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We compare our method to prior techniques on a range of challenging continuous control tasks from the OpenAI gym benchmark suite (Brockman et al., ... | embodiment, simulator version and control stack | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Task/environment | Although the easier tasks can be solved by a wide range of different algorithms, the more complex benchmarks, such as the 21-dimensional Humanoid (rllab), ... | reset, timeout, object/scene variation | p. 6 (5. Experiments), p. 7 (5.2. Ablation Study) |
| Observation/sensor | state 또는 observation, action, reward와 transition history | calibration, preprocessing, privileged input | p. 3 (3.1. Notation), p. 6 (4.2. Soft Actor-Critic) |
| Output/decision | action policy와 induced trajectory | action frame, controller and termination | p. 3 (3.1. Notation), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The optimal reward scale varies between environments, and should be tuned for each task separately. | definition/direction/unit from same section | p. 8 (5.2. Ablation Study) |
| With the right reward scaling, the model balances exploration and exploitation, leading to faster learning and better asymptotic performance. | definition/direction/unit from same section | p. 8 (5.2. Ablation Study) |
| Larger reward magnitudes correspond to lower entries. | definition/direction/unit from same section | p. 7 (5.2. Ablation Study) |
| For large reward magnitudes, the model learns quickly at first, | definition/direction/unit from same section | p. 7 (5.2. Ablation Study) |
| Table 2. SAC Environment Specific Parameters Environment Action Dimensions Reward Scale Hopper-v1 3 5 Walker2d-v1 | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Our SQL implementation also includes two Q-functions, which we found to improve its performance in most environments. | definition/direction/unit from same section | p. 6 (5. Experiments) |
| The stability of the algorithm also plays a large role in performance: easier tasks make it more practical to tune hyperparameters to achieve good ... | definition/direction/unit from same section | p. 6 (5. Experiments) |
| Table 1. SAC Hyperparameters Parameter Value Shared optimizer Adam (Kingma & Ba, 2015) learning rate 3 · 10-4 | definition/direction/unit from same section | p. 13 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The results show that, overall, SAC performs comparably to the baseline methods on the easier tasks and outperforms them on the harder tasks with ... | comparison identity and matched condition | p. 7 (5.1. Comparative Evaluation) |
| The results in the previous section suggest that algorithms based on the maximum entropy principle can outperform conventional RL methods on challenging tasks such ... | comparison identity and matched condition | p. 7 (5.2. Ablation Study) |
| Figure 4. Training curves for additional baseline (Trust-PCL) and for two SAC variants. Soft actor-critic with hard target update (blue) differs from standard SAC ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |
| We use an exponentially moving average, with a smoothing constant τ, to update the target value network weights as common in the prior work ... | comparison identity and matched condition | p. 8 (5.2. Ablation Study) |
| Figure 1. Training curves on continuous control benchmarks. Soft actor-critic (yellow) performs consistently across all tasks and outperforming both on-policy and off-policy methods in ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 4. Training curves for additional baseline (Trust-PCL) and for two SAC variants. Soft actor-critic with hard target update (blue) differs from standard SAC ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| We have included trust region path consistency learning (Trust-PCL) (Nachum et al., 2017b) and two other variants of SAC in Appendix E. | component/input/data sensitivity | p. 6 (5. Experiments) |
| Comparison of SAC (blue) and a deterministic variant of SAC (red) in terms of the stability of individual random seeds on the Humanoid (rllab) ... | component/input/data sensitivity | p. 7 (5.2. Ablation Study) |
| Soft actor-critic performs much more consistently, while the deterministic variant exhibits very high variability across seeds, indicating substantially worse stability. | component/input/data sensitivity | p. 7 (5.2. Ablation Study) |
| Sensitivity of soft actor-critic to selected hyperparameters on Ant-v1 task. | component/input/data sensitivity | p. 8 (5.2. Ablation Study) |
| We found this variant to benefit from taking more than one gradient step between the environment steps, which can improve performance but also increases ... | component/input/data sensitivity | p. 8 (5.2. Ablation Study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present empirical results that show that soft actor-critic attains a substantial improvement in both performance and sample efficiency over both off-policy and on-policy ... | The stability of the algorithm also plays a large role in performance: easier tasks make it more practical to tune hyperparameters to achieve good ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5. Experiments), p. 7 (5.1. Comparative Evaluation), p. 6 (5. Experiments), p. 7 (5.2. Ablation Study), p. 8 (5.2. Ablation Study), p. 8 (5.2. Ablation Study) |
| Primary metric/result | The results show that, overall, SAC performs comparably to the baseline methods on the easier tasks and outperforms them on the harder tasks with ... | numeric claim only at cited anchor | p. 7 (5.1. Comparative Evaluation) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our results suggest that stochastic, entropy maximizing reinforcement learning algorithms can provide a promising avenue for improved robustness and stability, and further exploration of ... | p. 8 (6. Conclusion) |
| body limitation/failure cue | For example, DDPG fails to make any progress on Ant-v1, Humanoidv1, and Humanoid (rllab), a result that is corroborated by prior work (Gu et ... | p. 7 (5.1. Comparative Evaluation) |
| body limitation/failure cue | To compare how the stochasticity of the policy and entropy maximization affects the performance, we compare to a deterministic variant of SAC that does ... | p. 7 (5.2. Ablation Study) |
| body limitation/failure cue | Figure 4. Training curves for additional baseline (Trust-PCL) and for two SAC variants. Soft actor-critic with hard target update (blue) differs from standard SAC ... | p. 14 (Figure/Table caption) |
| body limitation/failure cue | Note that the policy is trained to maximize also the entropy, and the mean action does not, in general, correspond the optimal action for ... | p. 8 (5.2. Ablation Study) |
| body limitation/failure cue | We turned off the exploration noise for evaluation for DDPG and PPO. | p. 6 (5. Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The source code of our SAC implementation1 and videos2 are available online. | p. 6 (5. Experiments) |
| We train five different instances of each algorithm with different random seeds, with each performing one evaluation rollout every 1000 environment steps. | p. 7 (5.1. Comparative Evaluation) |
| SAC also learns considerably faster than PPO as a consequence of the large batch sizes PPO needs to learn stably on more high-dimensional and ... | p. 7 (5.1. Comparative Evaluation) |
| Our SQL implementation also includes two Q-functions, which we found to improve its performance in most environments. | p. 6 (5. Experiments) |
| Sensitivity of soft actor-critic to selected hyperparameters on Ant-v1 task. | p. 8 (5.2. Ablation Study) |
| We found this variant to benefit from taking more than one gradient step between the environment steps, which can improve performance but also increases ... | p. 8 (5.2. Ablation Study) |
| In the policy evaluation step of soft policy iteration, we wish to compute the value of a policy π according to the maximum entropy ... | p. 4 (4.1. Derivation of Soft Policy Iteration) |
| The full soft policy iteration algorithm alternates between the soft policy evaluation and the soft policy improvement steps, and it will provably converge to ... | p. 4 (4.1. Derivation of Soft Policy Iteration) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive body cue:** Our results suggest that stochastic, entropy maximizing reinforcement learning algorithms can provide a promising avenue for improved robustness and stability, and further exploration of maximum ...
- **p. 7 / 5.1. Comparative Evaluation - extractive body cue:** For example, DDPG fails to make any progress on Ant-v1, Humanoidv1, and Humanoid (rllab), a result that is corroborated by prior work (Gu et al., ...
- **p. 7 / 5.2. Ablation Study - extractive body cue:** To compare how the stochasticity of the policy and entropy maximization affects the performance, we compare to a deterministic variant of SAC that does not ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 4. Training curves for additional baseline (Trust-PCL) and for two SAC variants. Soft actor-critic with hard target update (blue) differs from standard SAC in ...
- **p. 8 / 5.2. Ablation Study - extractive body cue:** Note that the policy is trained to maximize also the entropy, and the mean action does not, in general, correspond the optimal action for the ...
- **p. 6 / 5. Experiments - extractive body cue:** We turned off the exploration noise for evaluation for DDPG and PPO.

- **Evidence anchors reviewed:** datasets p. 6 (5. Experiments), p. 6 (5. Experiments), p. 7 (5.2. Ablation Study), p. 7 (5.1. Comparative Evaluation), p. 8 (5.2. Ablation Study), p. 8 (5.2. Ablation Study), metrics p. 8 (5.2. Ablation Study), p. 8 (5.2. Ablation Study), p. 7 (5.2. Ablation Study), p. 7 (5.2. Ablation Study), p. 13 (Figure/Table caption), p. 6 (5. Experiments), baselines p. 7 (5.1. Comparative Evaluation), p. 7 (5.2. Ablation Study), p. 14 (Figure/Table caption), p. 8 (5.2. Ablation Study), p. 6 (Figure/Table caption), results p. 6 (5. Experiments), p. 7 (5.1. Comparative Evaluation), p. 6 (5. Experiments), p. 7 (5.2. Ablation Study), p. 8 (5.2. Ablation Study), p. 8 (5.2. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** The results show that, overall, SAC performs comparably to the baseline methods on the easier tasks and outperforms them on the harder tasks with a large margin, both in terms ... (p. 7, 5.1. Comparative Evaluation).
- **Metric evidence:** With the right reward scaling, the model balances exploration and exploitation, leading to faster learning and better asymptotic performance. (p. 8, 5.2. Ablation Study).
- **Baseline/ablation evidence:** The results show that, overall, SAC performs comparably to the baseline methods on the easier tasks and outperforms them on the harder tasks with a large margin, both in terms ... (p. 7, 5.1. Comparative Evaluation).
- **Failure/negative evidence:** For maximum entropy algorithms, which do not explicitly inject exploration noise, we either evaluated with the exploration noise (SQL) or use the mean action (SAC). (p. 6, 5. Experiments).
