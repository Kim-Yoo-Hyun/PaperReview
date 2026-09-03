# Evaluation - A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ri.cmu.edu/publications/a-reduction-of-imitation-learning-and-structured-prediction-to-no-regret-online-learning/; PDF retrieval source: https://www.ri.cmu.edu/pub_files/2011/4/Ross-AISTATS11-NoRegret.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS)): Though even after 5 iterations, the policy we obtain almost never falls off the track and is significantly outperforming both SMILe and the baseline supervised approach.

## Evaluation Body Digest

- **p. 8 / 5 EXPERIMENTS - extractive body cue:** We use the dataset of Taskar et al.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** This dataset contains roughly 6600 words (for a total of over 52000 characters) partitioned in 10 folds.
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** A human expert is used to provide demonstrations of the correct steering (analog joystick value in [-1,1]) for each of the observed game images.
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** To demonstrate the efficacy and scalability of DAGGER, we apply it to two challenging imitation learning problems and a sequence labeling task (handwriting recognition).
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** We used the simulator from a recent Mario Bros.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** The kth output binary variable ˆyk = I(wT k x + bk > 0), where wk, bk optimizes the SVM objective with regularizer λ = ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Average distance/stage as a function of data. approach, performance stagnates as we collect more data from the expert demonstrations, as this does not ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Performance is measured in terms of the character accuracy on the test folds.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 EXPERIMENTS | EMPIRICAL / SIMULATION | Though even after 5 iterations, the policy we obtain almost never falls off the track and is significantly outperforming both SMILe and the baseline ... | p. 6 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SIMULATION | DAgger (βi = I(i=1)) SMILe (α = 0.1) Supervised Figure 2: Average falls/lap as a function of training data. supervised approach where training always ... | p. 6 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SIMULATION | The baseline result without structure achieves 82% character accuracy by just using an SVM that predicts each character independently. | p. 8 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SIMULATION | Again in this experiment, DAGGER outperforms SMILe, and also outperforms SEARN for all choice of α we considered. | p. 7 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / SIMULATION | When using βi = 0.9i-1, convergence is significantly slower could have benefited from more iterations as performance was still improving at the end of ... | p. 7 (5 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 8 / 5 EXPERIMENTS - extractive body cue:** We use the dataset of Taskar et al.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** This dataset contains roughly 6600 words (for a total of over 52000 characters) partitioned in 10 folds.
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** A human expert is used to provide demonstrations of the correct steering (analog joystick value in [-1,1]) for each of the observed game images.
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** To demonstrate the efficacy and scalability of DAGGER, we apply it to two challenging imitation learning problems and a sequence labeling task (handwriting recognition).
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** We used the simulator from a recent Mario Bros.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** The kth output binary variable ˆyk = I(wT k x + bk > 0), where wk, bk optimizes the SVM objective with regularizer λ = ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 6 / Figure/Table caption - extractive body cue:** Figure 1: Image from Super Tux Kart's Star Track. controller as the base learner which updates the steering at 5Hz based on the vector of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2: Average falls/lap as a function of training data. supervised approach where training always occurs under the expert's trajectories that performance does not improve ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Captured image from Super Mario Bros. all methods, we use 4 independent linear SVM as the base learner which update the 4 binary ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Average distance/stage as a function of data. approach, performance stagnates as we collect more data from the expert demonstrations, as this does not ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Character accuracy as a function of iteration. predicted character feature) this makes this approach not as unstable as in general reinforcement/imitation learning problems ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We use the dataset of Taskar et al. | embodiment, simulator version and control stack | p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Task/environment | This dataset contains roughly 6600 words (for a total of over 52000 characters) partitioned in 10 folds. | reset, timeout, object/scene variation | p. 8 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 2 (2 PRELIMINARIES), p. 5 (2 PRELIMINARIES) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 4: Average distance/stage as a function of data. approach, performance stagnates as we collect more data from the expert demonstrations, as this does ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Performance is measured in terms of the character accuracy on the test folds. | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| We compare performance in terms of the average distance travelled by Mario per stage before dying, running out of time or completing the stage, ... | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| The baseline result without structure achieves 82% character accuracy by just using an SVM that predicts each character independently. | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| We compare performance on a race track called Star Track. | definition/direction/unit from same section | p. 6 (5 EXPERIMENTS) |
| We measure performance in terms of the average number of falls per lap. | definition/direction/unit from same section | p. 6 (5 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Though even after 5 iterations, the policy we obtain almost never falls off the track and is significantly outperforming both SMILe and the baseline ... | comparison identity and matched condition | p. 6 (5 EXPERIMENTS) |
| The baseline result without structure achieves 82% character accuracy by just using an SVM that predicts each character independently. | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| We first observe that with the baseline 0 0.5 1 1.5 2 2.5 x 10 4 0 0.5 1 1.5 2 2.5 3 3.5 ... | comparison identity and matched condition | p. 6 (5 EXPERIMENTS) |
| Again in this experiment, DAGGER outperforms SMILe, and also outperforms SEARN for all choice of α we considered. | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| Similar techniques can be applied to multi-pass or beam-search decoding leading to results that are competitive with the state-of-the-art. | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The baseline result without structure achieves 82% character accuracy by just using an SVM that predicts each character independently. | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose a new meta-algorithm for imitation learning which learns a stationary deterministic policy guaranteed to perform well under its induced distribution of states ... | Though even after 5 iterations, the policy we obtain almost never falls off the track and is significantly outperforming both SMILe and the baseline ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Primary metric/result | DAgger (βi = I(i=1)) SMILe (α = 0.1) Supervised Figure 2: Average falls/lap as a function of training data. supervised approach where training always ... | numeric claim only at cited anchor | p. 6 (5 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** For all methods, we use a linear Figure 1: Image from Super Tux Kart's Star Track. controller as the base learner which updates the steering ...
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** We first observe that with the baseline 0 0.5 1 1.5 2 2.5 x 10 4 0 0.5 1 1.5 2 2.5 3 3.5 4 ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** For Figure 3: Captured image from Super Mario Bros. all methods, we use 4 independent linear SVM as the base learner which update the 4 ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Again here we observe that with the supervised 0 1 2 3 4 5 6 7 8 9 10 x 10 4 1000 1200 1400 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | DAgger (βi = I(i=1)) SMILe (α = 0.1) Supervised Figure 2: Average falls/lap as a function of training data. supervised approach where training always ... | p. 6 (5 EXPERIMENTS) |
| body limitation/failure cue | We measure performance in terms of the average number of falls per lap. | p. 6 (5 EXPERIMENTS) |
| body limitation/failure cue | Andrew Bagnell ing being hit by enemies and falling into gaps, and before running out of time. | p. 7 (5 EXPERIMENTS) |
| body limitation/failure cue | DAgger (βi=I(i=1)) SEARN (α=1) SEARN (α=0.8) SEARN (α=0.1) SMILe (α=0.1) Supervised No Structure Figure 5: Character accuracy as a function of iteration. predicted character ... | p. 8 (5 EXPERIMENTS) |
| body limitation/failure cue | D0 D0.5 D0.9 Se1 Se0.4 Sm0.1 Sup Figure 4: Average distance/stage as a function of data. approach, performance stagnates as we collect more data ... | p. 7 (5 EXPERIMENTS) |
| body limitation/failure cue | 6 FUTURE WORK We show that by batching over iterations of interaction with a system, no-regret methods, including the presented DAGGER approach can provide ... | p. 8 (5 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For SMILe and DAGGER, we used 1 lap of training per iteration (∼1000 data points) and run both methods for 20 iterations. | p. 6 (5 EXPERIMENTS) |
| Our goal is to train the computer to steer the kart moving at fixed speed on a particular race track, based on the current ... | p. 6 (5 EXPERIMENTS) |
| With each approach we collect 5000 data points per iteration (each stage is about 150 data points if run to completion) and run the ... | p. 7 (5 EXPERIMENTS) |
| Again we try all choice of α ∈{0.1, 0.2, . . . , 1} for SEARN, and report results for α = 0.1, α ... | p. 8 (5 EXPERIMENTS) |
| Because there is only a small part of the input that is influenced by the current policy (the previous 7Each character is 8x16 binary ... | p. 8 (5 EXPERIMENTS) |
| In particular, a classifier that makes a mistake with probability ϵ under the distribution of states/observations encountered by the expert can make as many ... | p. 1 (1 INTRODUCTION) |
| Furthermore, we denote dπ = 1 T PT t=1 dt π the average distribution of states if we follow policy π for T steps. | p. 2 (2 PRELIMINARIES) |
| The total cost of executing policy π for T-steps (i.e., the cost-to-go) is denoted J(π) = PT t=1 Es∼dtπ[Cπ(s)] = TEs∼dπ[Cπ(s)]. | p. 2 (2 PRELIMINARIES) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 5 EXPERIMENTS - extractive body cue:** DAgger (βi = I(i=1)) SMILe (α = 0.1) Supervised Figure 2: Average falls/lap as a function of training data. supervised approach where training always occurs ...
- **p. 6 / 5 EXPERIMENTS - extractive body cue:** We measure performance in terms of the average number of falls per lap.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Andrew Bagnell ing being hit by enemies and falling into gaps, and before running out of time.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** DAgger (βi=I(i=1)) SEARN (α=1) SEARN (α=0.8) SEARN (α=0.1) SMILe (α=0.1) Supervised No Structure Figure 5: Character accuracy as a function of iteration. predicted character feature) ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** D0 D0.5 D0.9 Se1 Se0.4 Sm0.1 Sup Figure 4: Average distance/stage as a function of data. approach, performance stagnates as we collect more data from ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** 6 FUTURE WORK We show that by batching over iterations of interaction with a system, no-regret methods, including the presented DAGGER approach can provide a ...

- **Evidence anchors reviewed:** datasets p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), metrics p. 7 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), baselines p. 6 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), results p. 6 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (9 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** The baseline result without structure achieves 82% character accuracy by just using an SVM that predicts each character independently. (p. 8, 5 EXPERIMENTS).
- **Metric evidence:** We compare performance in terms of the average distance travelled by Mario per stage before dying, running out of time or completing the stage, on randomly generated stages of difficulty ... (p. 7, 5 EXPERIMENTS).
- **Baseline/ablation evidence:** Though even after 5 iterations, the policy we obtain almost never falls off the track and is significantly outperforming both SMILe and the baseline supervised approach. (p. 6, 5 EXPERIMENTS).
- **Failure/negative evidence:** We measure performance in terms of the average number of falls per lap. (p. 6, 5 EXPERIMENTS).
