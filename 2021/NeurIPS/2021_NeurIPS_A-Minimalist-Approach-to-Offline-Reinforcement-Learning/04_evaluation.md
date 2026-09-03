# Evaluation - A Minimalist Approach to Offline Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2106.06860; PDF retrieval source: https://arxiv.org/pdf/2106.06860. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 18 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (6 Experiments), p. 8 (6 Experiments)): Table 3: Run time comparison of training each offline RL algorithm (does not include evaluation costs). (Left) Breakdown of the cost of the added implementation details (mainly architecture changes) and ...

## Evaluation Body Digest

- **p. 7 / 6 Experiments - extractive body cue:** We evaluate our proposed approach on the D4RL benchmark of OpenAI gym MuJoCo tasks [Todorov et al., 2012, Brockman et al., 2016, Fu et al., ...
- **p. 7 / 6 Experiments - extractive body cue:** Each evaluation consists of 10 episodes.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Average normalized score over the final 10 evaluations and 5 seeds. The highest performing scores are highlighted. CQL and Fisher-BRC are re-run using ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 8: Average normalized score over the final 10 evaluations and 5 seeds on the AntMaze environments. ± captures the standard deviation over seeds. C.2 ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 9: Average normalized score using the D4RL -v2 datasets. The highest performing scores are highlighted. ± captures the standard deviation over seeds. Total (DT) ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 7: Average normalized score over the final 10 evaluations and 5 seeds on a mixture of 50% of the random D4RL dataset and 50% ...
- **p. 8 / 6 Experiments - extractive body cue:** BC CQL Fisher-BRC TD3+BC 0.0 0.2 0.4 0.6 0.8 1.0 0 20 40 60 80 100 120 Normalized Score HalfCheetah-Random 0.0 0.2 0.4 0.6 0.8 ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 6. Heuristics for selecting λ. While we find a single setting of λ works across all datasets, some practitioners may be interested in guidelines ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** offline robot transition/trajectory dataset과 deployment MDP.
- **Input boundary:** dataset state/observation, action, reward와 return-to-go.
- **Output/decision under evaluation:** dataset-supported action sequence.
- **Primary target:** offline policy value, OOD safety와 closed-loop success.
- **Detected evaluation headings:** 6 Experiments (p. 7); B Experimental Details (p. 14); C Additional Experiments (p. 17); C.1 Additional Datasets (p. 17); C.3 Benchmarking against the Decision Transformer (p. 18).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 3: Run time comparison of training each offline RL algorithm (does not include evaluation costs). (Left) Breakdown of the cost of the added ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 2: Average normalized score over the final 10 evaluations and 5 seeds. The highest performing scores are highlighted. CQL and Fisher-BRC are re-run ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 9: Average normalized score using the D4RL -v2 datasets. The highest performing scores are highlighted. ± captures the standard deviation over seeds. Total ... | p. 18 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 5: Percent difference of the performance of an ablation of our proposed approach, compared to the full algorithm. TD3+λ+BC+Norm refers to the complete ... | p. 9 (Figure/Table caption) |
| 6 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We report the final performance results in Table 2 and display the learning curves in Figure 4. | p. 7 (6 Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 6 Experiments - extractive body cue:** We evaluate our proposed approach on the D4RL benchmark of OpenAI gym MuJoCo tasks [Todorov et al., 2012, Brockman et al., 2016, Fu et al., ...
- **p. 7 / 6 Experiments - extractive body cue:** Each evaluation consists of 10 episodes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: Implementation changes offline RL algorithms make to the underlying base RL algorithm. † corresponds to details that add additional hyperparameter(s), and ‡ corresponds ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1: Percent difference of performance of offline RL algorithms and their simplified versions which remove implementation adjustments to their underlying algorithm. HC = HalfCheetah, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Percent difference of the worst episode during the 10 evaluation episodes at the last evaluation. This measures the deviations in performance at single ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Percent difference of the worst evaluation during the last 10 evaluations. This measures the deviations in performance over a period of time. HC ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Average normalized score over the final 10 evaluations and 5 seeds. The highest performing scores are highlighted. CQL and Fisher-BRC are re-run using ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Learning curves comparing the performance of TD3+BC against offline RL baselines in the D4RL datasets. Curves are averaged over 5 seeds, with the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Run time comparison of training each offline RL algorithm (does not include evaluation costs). (Left) Breakdown of the cost of the added implementation ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Percent difference of the performance of an ablation of our proposed approach, compared to the full algorithm. TD3+λ+BC+Norm refers to the complete algorithm, ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our proposed approach on the D4RL benchmark of OpenAI gym MuJoCo tasks [Todorov et al., 2012, Brockman et al., 2016, Fu et ... | embodiment, simulator version and control stack | p. 7 (6 Experiments), p. 7 (6 Experiments) |
| Task/environment | Each evaluation consists of 10 episodes. | reset, timeout, object/scene variation | p. 7 (6 Experiments) |
| Observation/sensor | dataset state/observation, action, reward와 return-to-go | calibration, preprocessing, privileged input | p. 1 (1 Introduction), p. 3 (3 Background) |
| Output/decision | dataset-supported action sequence | action frame, controller and termination | p. 1 (1 Introduction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2: Average normalized score over the final 10 evaluations and 5 seeds. The highest performing scores are highlighted. CQL and Fisher-BRC are re-run ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 8: Average normalized score over the final 10 evaluations and 5 seeds on the AntMaze environments. ± captures the standard deviation over seeds. ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Table 9: Average normalized score using the D4RL -v2 datasets. The highest performing scores are highlighted. ± captures the standard deviation over seeds. Total ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| Table 7: Average normalized score over the final 10 evaluations and 5 seeds on a mixture of 50% of the random D4RL dataset and ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| BC CQL Fisher-BRC TD3+BC 0.0 0.2 0.4 0.6 0.8 1.0 0 20 40 60 80 100 120 Normalized Score HalfCheetah-Random 0.0 0.2 0.4 0.6 ... | definition/direction/unit from same section | p. 8 (6 Experiments) |
| Table 6. Heuristics for selecting λ. While we find a single setting of λ works across all datasets, some practitioners may be interested in ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| Figure 4: Learning curves comparing the performance of TD3+BC against offline RL baselines in the D4RL datasets. Curves are averaged over 5 seeds, with ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| We report the final performance results in Table 2 and display the learning curves in Figure 4. | definition/direction/unit from same section | p. 7 (6 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our offline RL baselines include two state-of-the-art algorithms, CQL [Kumar et al., 2020] and Fisher-BRC [Kostrikov et al., 2021], as well as BRAC [Wu ... | comparison identity and matched condition | p. 7 (6 Experiments) |
| Figure 4: Learning curves comparing the performance of TD3+BC against offline RL baselines in the D4RL datasets. Curves are averaged over 5 seeds, with ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 3: Run time comparison of training each offline RL algorithm (does not include evaluation costs). (Left) Breakdown of the cost of the added ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Although our method is very simplistic in nature, it surpasses, or matches, the performance of the current state-of-the-art offline RL algorithms in most tasks. | comparison identity and matched condition | p. 7 (6 Experiments) |
| Figure 6: Percent difference of the performance of an ablation over α, compared to the full algorithm. Recall the form of the sole hyperparameter ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Figure 5: Percent difference of the performance of an ablation of our proposed approach, compared to the full algorithm. TD3+λ+BC+Norm refers to the complete ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 5: Percent difference of the performance of an ablation of our proposed approach, compared to the full algorithm. TD3+λ+BC+Norm refers to the complete ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Table 3: Run time comparison of training each offline RL algorithm (does not include evaluation costs). (Left) Breakdown of the cost of the added ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 6: Percent difference of the performance of an ablation over α, compared to the full algorithm. Recall the form of the sole hyperparameter ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Figure 3: Percent difference of the worst evaluation during the last 10 evaluations. This measures the deviations in performance over a period of time. ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Figure 1: Percent difference of performance of offline RL algorithms and their simplified versions which remove implementation adjustments to their underlying algorithm. HC = ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Figure 4: Learning curves comparing the performance of TD3+BC against offline RL baselines in the D4RL datasets. Curves are averaged over 5 seeds, with ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Consequently, offline RL enables the use of previously logged data or leveraging an expert, such as a human operator, without any of the risk ... | Table 3: Run time comparison of training each offline RL algorithm (does not include evaluation costs). (Left) Breakdown of the cost of the added ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 18 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (6 Experiments), p. 8 (6 Experiments) |
| Primary metric/result | Table 2: Average normalized score over the final 10 evaluations and 5 seeds. The highest performing scores are highlighted. CQL and Fisher-BRC are re-run ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / 6 Experiments - extractive body cue:** Each evaluation consists of 10 episodes.
- **p. 8 / 120 HalfCheetah-Medium-Expert - extractive body cue:** Curves are averaged over 5 seeds, with the shaded area representing the standard deviation across seeds.
- **p. 8 / 120 HalfCheetah-Medium-Expert - extractive body cue:** CQL Fisher-BRC Fisher-BRC TD3+BC (GitHub) (GitHub) (Ours) (Ours) Implementation 25m 39m 15m < 1s Algorithmic 1h 29m 33m 58m < 5s Total 4h 11m 2h ...
- **p. 8 / 120 HalfCheetah-Medium-Expert - extractive body cue:** All run time experiments were run with a single GeForce GTX 1080 GPU and an Intel Core i7-6700K CPU at 4.00GHz.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Finally, we believe the sheer simplicity of our approach highlights a possible overemphasis on algorithmic complexity made by the community, and we hope to ... | p. 9 (7 Conclusion) |
| body limitation/failure cue | Additionally, we highlight existing open challenges in offline RL research, including not only the extra implementation, computation, and hyperparameter-tuning complexities that we successfully address ... | p. 9 (7 Conclusion) |
| body limitation/failure cue | Table 3: Run time comparison of training each offline RL algorithm (does not include evaluation costs). (Left) Breakdown of the cost of the added ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Figure 8: Benchmarking wall-clock training time of DT and TD3+BC over 1 million steps. Does not include evaluation costs. We remark that the DT ... | p. 19 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| CQL Fisher-BRC TD3+BC [Kumar et al., 2020] [Kostrikov et al., 2021] (Ours) Algorithmic Adjustments Add regularizer to critic† Train a generative model†‡ Add a ... | p. 4 (3 Background) |
| To ensure a fair and identical experimental evaluation across algorithms, we re-run the state-of-theart algorithms CQL and Fisher-BRC using the author-provided implementations23. | p. 7 (6 Experiments) |
| CQL and Fisher-BRC are re-run using author-provided implementations to ensure an identical evaluation process, while BRAC and AWAC use previously reported results. ± captures ... | p. 7 (3 Background) |
| All run time experiments were run with a single GeForce GTX 1080 GPU and an Intel Core i7-6700K CPU at 4.00GHz. | p. 8 (120 HalfCheetah-Medium-Expert) |
| We evaluate run time of training each of the offline RL algorithms for 1 million time steps, using the author-provoided implementations. | p. 8 (120 HalfCheetah-Medium-Expert) |
| Most offline RL algorithms are built explicitly on top of an existing off-policy deep RL algorithm, such as TD3 [Fujimoto et al., 2018] or ... | p. 4 (3 Background) |
| As discussed in Section 4 a minimalist approach has a variety of benefits, such as reducing the number of hyperparameters to tune, increasing scalability ... | p. 6 (3 Background) |
| Offline RL algorithms introduce new hyperparameters and often leverage secondary components such as generative models, while adjusting the underlying RL algorithm. | p. 1 (Abstract) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 7 Conclusion - extractive body cue:** Finally, we believe the sheer simplicity of our approach highlights a possible overemphasis on algorithmic complexity made by the community, and we hope to inspire ...
- **p. 9 / 7 Conclusion - extractive body cue:** Additionally, we highlight existing open challenges in offline RL research, including not only the extra implementation, computation, and hyperparameter-tuning complexities that we successfully address in ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Run time comparison of training each offline RL algorithm (does not include evaluation costs). (Left) Breakdown of the cost of the added implementation ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 8: Benchmarking wall-clock training time of DT and TD3+BC over 1 million steps. Does not include evaluation costs. We remark that the DT was ...

- **Evidence anchors reviewed:** datasets p. 7 (6 Experiments), p. 7 (6 Experiments), metrics p. 7 (Figure/Table caption), p. 17 (Figure/Table caption), p. 18 (Figure/Table caption), p. 17 (Figure/Table caption), p. 8 (6 Experiments), p. 14 (Figure/Table caption), baselines p. 7 (6 Experiments), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (6 Experiments), p. 9 (Figure/Table caption), p. 9 (Figure/Table caption), results p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 18 (Figure/Table caption), p. 9 (Figure/Table caption), p. 7 (6 Experiments), p. 8 (6 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (19 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 9: Average normalized score using the D4RL -v2 datasets. The highest performing scores are highlighted. ± captures the standard deviation over seeds. Total (DT) sums scores over the subset ... (p. 18, Figure/Table caption).
- **Metric evidence:** BC CQL Fisher-BRC TD3+BC 0.0 0.2 0.4 0.6 0.8 1.0 0 20 40 60 80 100 120 Normalized Score HalfCheetah-Random 0.0 0.2 0.4 0.6 0.8 1.0 0 20 40 60 ... (p. 8, 6 Experiments).
- **Baseline/ablation evidence:** Our offline RL baselines include two state-of-the-art algorithms, CQL [Kumar et al., 2020] and Fisher-BRC [Kostrikov et al., 2021], as well as BRAC [Wu et al., 2019] and AWAC [Nair ... (p. 7, 6 Experiments).
- **Failure/negative evidence:** We use the hyperparameters defined in the CQL paper rather than the default settings in the CQL GitHub as we found those settings performed poorly. † denotes hyperparameters which deviate ... (p. 15, B Experimental Details).
