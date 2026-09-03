# Evaluation - Efficient Online Reinforcement Learning with Offline Data

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v202/ball23a.html; PDF retrieval source: https://proceedings.mlr.press/v202/ball23a/ball23a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 15 (Figure/Table caption), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (5.1. RLPD Analysis and Ablation Study)): Figure 7. LayerNorm is crucial for strong performance, particu- larly when data are limited or narrowly distributed. results in collapsed performance, with no progress made on any task. We further ...

## Evaluation Body Digest

- **p. 7 / 5.1. RLPD Analysis and Ablation Study - extractive body cue:** To more clearly illustrate this effect, we construct a dataset of only the expert human demonstration data from the Adroit Sparse tasks (see "Expert Adroit ...
- **p. 7 / 5.1. RLPD Analysis and Ablation Study - extractive body cue:** This subset comprises just 22 of the 500 trajectories in the original dataset and is much more narrowly distributed by nature-representing a task with sparse ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 21. Visualizations of the environments we consider. We provide further details about the key domains we evaluate on. In Figure 21 we provide visualizations ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 10. Symmetric sampling improves sample efficiency and reduces variance across seeds, and does not work by simply in- creasing the reward density in a ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 9. In general, critic ensembling provides the best perfor- mance. Dropout performs worse in sparse reward tasks. In Figure 9, we see that ensembling ...
- **p. 5 / 5. Experiments - extractive body cue:** We design our experiments to not only demonstrate the importance of our design choices, but also provide the insights that allow practitioners to quickly adapt ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Using SAC with our symmetric sampling method can result in instabilities due to diverging Q-values; with LayerNorm in the critic this disappears, improving ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. RLPD exceeds prior state-of-the-art performance on a number of different popular benchmarks whilst being significantly simpler. Results are aggregated over 21 different environments ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** offline robot transition/trajectory dataset과 deployment MDP.
- **Input boundary:** dataset state/observation, action, reward와 return-to-go.
- **Output/decision under evaluation:** dataset-supported action sequence.
- **Primary target:** offline policy value, OOD safety와 closed-loop success.
- **Detected evaluation headings:** 5. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 7. LayerNorm is crucial for strong performance, particu- larly when data are limited or narrowly distributed. results in collapsed performance, with no progress ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 18. D4RL Ablations. The impact of LayerNorm is not so clear cut in Figure 18; this is to be expected as online approaches ... | p. 15 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. Our approach, RLPD, extends standard off-policy RL and achieves reliable state-of-the-art online performance on a num- ber of tasks using offline data. ... | p. 1 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 2. Using SAC with our symmetric sampling method can result in instabilities due to diverging Q-values; with LayerNorm in the critic this disappears, ... | p. 3 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4. RLPD exceeds prior state-of-the-art performance on a number of different popular benchmarks whilst being significantly simpler. Results are aggregated over 21 different ... | p. 6 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 5.1. RLPD Analysis and Ablation Study - extractive body cue:** To more clearly illustrate this effect, we construct a dataset of only the expert human demonstration data from the Adroit Sparse tasks (see "Expert Adroit ...
- **p. 7 / 5.1. RLPD Analysis and Ablation Study - extractive body cue:** This subset comprises just 22 of the 500 trajectories in the original dataset and is much more narrowly distributed by nature-representing a task with sparse ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Our approach, RLPD, extends standard off-policy RL and achieves reliable state-of-the-art online performance on a num- ber of tasks using offline data. Here ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Using SAC with our symmetric sampling method can result in instabilities due to diverging Q-values; with LayerNorm in the critic this disappears, improving ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. We fit data (left) with a two-layer MLP without Layer- Norm (center) and with LayerNorm (right). LayerNorm bounds the values and prevents catastrophic ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. RLPD exceeds prior state-of-the-art performance on a number of different popular benchmarks whilst being significantly simpler. Results are aggregated over 21 different environments ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Our approach generalizes to vision-based domains, pro- viding consistent improvements over existing approaches. We see in Figure 52 that RLPD provides consistent improve- ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. Increasing UTD with RLPD greatly im- proves sample efficiency from pixels. Lastly, we test increasing UTD to 10 on one of the tasks-Cheetah
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7. LayerNorm is crucial for strong performance, particu- larly when data are limited or narrowly distributed. results in collapsed performance, with no progress made ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 8. Our recommended starting design choices and workflow leads to strong performance on all tasks. We see in Figure 8 that with the recommended ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To more clearly illustrate this effect, we construct a dataset of only the expert human demonstration data from the Adroit Sparse tasks (see "Expert ... | embodiment, simulator version and control stack | p. 7 (5.1. RLPD Analysis and Ablation Study), p. 7 (5.1. RLPD Analysis and Ablation Study) |
| Task/environment | This subset comprises just 22 of the 500 trajectories in the original dataset and is much more narrowly distributed by nature-representing a task with ... | reset, timeout, object/scene variation | p. 7 (5.1. RLPD Analysis and Ablation Study) |
| Observation/sensor | dataset state/observation, action, reward와 return-to-go | calibration, preprocessing, privileged input | p. 4 (4. Online RL with Offline Data), p. 5 (4.4. Per-Environment Design Choices) |
| Output/decision | dataset-supported action sequence | action frame, controller and termination | p. 3 (3. Preliminaries), p. 3 (3. Preliminaries) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 21. Visualizations of the environments we consider. We provide further details about the key domains we evaluate on. In Figure 21 we provide ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |
| Figure 10. Symmetric sampling improves sample efficiency and reduces variance across seeds, and does not work by simply in- creasing the reward density in ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| This subset comprises just 22 of the 500 trajectories in the original dataset and is much more narrowly distributed by nature-representing a task with ... | definition/direction/unit from same section | p. 7 (5.1. RLPD Analysis and Ablation Study) |
| Figure 9. In general, critic ensembling provides the best perfor- mance. Dropout performs worse in sparse reward tasks. In Figure 9, we see that ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| We design our experiments to not only demonstrate the importance of our design choices, but also provide the insights that allow practitioners to quickly ... | definition/direction/unit from same section | p. 5 (5. Experiments) |
| Figure 2. Using SAC with our symmetric sampling method can result in instabilities due to diverging Q-values; with LayerNorm in the critic this disappears, ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 4. RLPD exceeds prior state-of-the-art performance on a number of different popular benchmarks whilst being significantly simpler. Results are aggregated over 21 different ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| In Figure 7, we see LayerNorm is crucial for strong performance in the Adroit domain; excluding LayerNorm results in significantly higher variance across seeds ... | definition/direction/unit from same section | p. 7 (5.1. RLPD Analysis and Ablation Study) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 18. D4RL Ablations. The impact of LayerNorm is not so clear cut in Figure 18; this is to be expected as online approaches ... | comparison identity and matched condition | p. 15 (Figure/Table caption) |
| Figure 1. Our approach, RLPD, extends standard off-policy RL and achieves reliable state-of-the-art online performance on a num- ber of tasks using offline data. ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Is RLPD competitive with prior work despite using no pre-training nor having explicit constraints? | comparison identity and matched condition | p. 5 (5. Experiments) |
| Figure 4. RLPD exceeds prior state-of-the-art performance on a number of different popular benchmarks whilst being significantly simpler. Results are aggregated over 21 different ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 5. Our approach generalizes to vision-based domains, pro- viding consistent improvements over existing approaches. We see in Figure 52 that RLPD provides consistent ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 3. We fit data (left) with a two-layer MLP without Layer- Norm (center) and with LayerNorm (right). LayerNorm bounds the values and prevents ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Here, we address (3) and (4) by quantifying the effect of LayerNorm, and demonstrating the reliability of our proposed workflow (see Subsection 4.5). | component/input/data sensitivity | p. 7 (5.1. RLPD Analysis and Ablation Study) |
| Figure 3. We fit data (left) with a two-layer MLP without Layer- Norm (center) and with LayerNorm (right). LayerNorm bounds the values and prevents ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Figure 15. SAC with and without Layer Normalization. In Figure 16, we see the impact of increasing the number of gradient steps per time-step. ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Figure 18. D4RL Ablations. The impact of LayerNorm is not so clear cut in Figure 18; this is to be expected as online approaches ... | component/input/data sensitivity | p. 15 (Figure/Table caption) |
| Figure 20. VD4RL Ablations. As we see, LayerNorm helps significantly in the Walker and Humanoid environments. We also see the positive impact of our ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |
| Figure 19. D4RL Ablation on Expert Data. We also test on the narrow Expert dataset, not tested by (Lee et al., 2021). In Figure ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| First, we propose a simple mechanism for incorporating the prior data. | Figure 7. LayerNorm is crucial for strong performance, particu- larly when data are limited or narrowly distributed. results in collapsed performance, with no progress ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 15 (Figure/Table caption), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (5.1. RLPD Analysis and Ablation Study) |
| Primary metric/result | Figure 18. D4RL Ablations. The impact of LayerNorm is not so clear cut in Figure 18; this is to be expected as online approaches ... | numeric claim only at cited anchor | p. 15 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / 5.1. RLPD Analysis and Ablation Study - extractive body cue:** This subset comprises just 22 of the 500 trajectories in the original dataset and is much more narrowly distributed by nature-representing a task with sparse ...
- **p. 1 / 1. Introduction - extractive body cue:** Here we show the difficult D4RL AntMaze domain (10 seeds, 1 std. shaded), averaged over all 6 tasks.
- **p. 5 / 4.4. Per-Environment Design Choices - extractive body cue:** To simplify the search space, we consider the impact of having 2 or 3 layers in the actor and critic, which have been shown to ...
- **p. 5 / 4.4. Per-Environment Design Choices - extractive body cue:** For environment specific choices, we recommend the following as a starting point: • Line 3: Subset 2 critics • Line 16: Remove entropy • Line ...
- **p. 6 / 4. Does the proposed workflow around environment - extractive body cue:** Results are aggregated over 21 different environments (10 Seeds, 1 std. shaded).
- **p. 6 / 4. Does the proposed workflow around environment - extractive body cue:** We consider the following 21 tasks from established benchmarks: • Sparse Adroit (Nair et al., 2020).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 10. Symmetric sampling improves sample efficiency and reduces variance across seeds, and does not work by simply in- creasing the reward density in ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Figure 9. In general, critic ensembling provides the best perfor- mance. Dropout performs worse in sparse reward tasks. In Figure 9, we see that ... | p. 8 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We run RLPD for 300k steps due to early convergence. on having large amounts of online interaction with an environment, which is usually made ... | p. 1 (1. Introduction) |
| 0 100 200 300 0 20 40 60 80 Cheetah Run Expert UTD=1 (Online) UTD=1 (RLPD) UTD=10 (Online) UTD=10 (RLPD) Environment steps (£103) Normalized ... | p. 7 (4. Does the proposed workflow around environment) |
| 0 100 200 0 20 40 60 80 100 120 walker2d-medium-v0 Best In Dataset Online Seeded Symmetric (Ours) Environment steps (£103) Normalized Return Figure ... | p. 8 (2 Layers) |
| 0 50 Normalized Return Pen Sparse Door Sparse 0 200 400 600 800 1000 0 50 % Batch Reward Non-Zero 0 200 400 600 ... | p. 8 (2 Layers) |
| However, each approach has its drawbacks, such as additional training time and hyperparamters, or limited improvement beyond the behavior policy respectively. | p. 1 (1. Introduction) |
| Crucially, as our changes are minimal, we maintain the attractive properties of online algorithms, such as ease of implementation and computational efficiency. | p. 2 (1. Introduction) |
| Concretely, we first introduce a remarkably simple approach to sampling the offline data, which we call "symmetric sampling", that performs well over a large ... | p. 2 (1. Introduction) |
| AntMaze Large Play Pen Sparse Environment steps (£103) Figure 2. | p. 3 (4. Online RL with Offline Data) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 10. Symmetric sampling improves sample efficiency and reduces variance across seeds, and does not work by simply in- creasing the reward density in a ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 9. In general, critic ensembling provides the best perfor- mance. Dropout performs worse in sparse reward tasks. In Figure 9, we see that ensembling ...

- **Evidence anchors reviewed:** datasets p. 7 (5.1. RLPD Analysis and Ablation Study), p. 7 (5.1. RLPD Analysis and Ablation Study), metrics p. 17 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (5.1. RLPD Analysis and Ablation Study), p. 8 (Figure/Table caption), p. 5 (5. Experiments), p. 3 (Figure/Table caption), baselines p. 15 (Figure/Table caption), p. 1 (Figure/Table caption), p. 5 (5. Experiments), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 4 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 15 (Figure/Table caption), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (5.1. RLPD Analysis and Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Figure 18. D4RL Ablations. The impact of LayerNorm is not so clear cut in Figure 18; this is to be expected as online approaches already achieve strong results in this ... (p. 15, Figure/Table caption).
- **Metric evidence:** Figure 21. Visualizations of the environments we consider. We provide further details about the key domains we evaluate on. In Figure 21 we provide visualizations of the environments. Sparse Adroit ... (p. 17, Figure/Table caption).
- **Baseline/ablation evidence:** Is RLPD competitive with prior work despite using no pre-training nor having explicit constraints? (p. 5, 5. Experiments).
- **Failure/negative evidence:** To this end, we show that Layer Normalization (LayerNorm) (Ba et al., 2016) can bound the extrapolation of networks but, crucially, does not explicitly constrain the policy to remain close ... (p. 4, 4. Online RL with Offline Data).
