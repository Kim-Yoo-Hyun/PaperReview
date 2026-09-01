# Evaluation - A New Approach to Linear Filtering and Prediction Problems

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1115/1.3662552; PDF retrieval source: https://doi.org/10.1115/1.3662552. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Introduction), p. 4 (Introduction), p. 4 (Introduction), p. 7 (Introduction), p. 7 (Introduction), p. 8 (Introduction)): This is due to two things: (1) The time dependence of Φ(t + 1; t) and M(t); (2) the fact that the estimation starts at t = t0 and improves ...

## Evaluation Body Digest

- **p. 7 / Introduction - extractive body cue:** Of course, the solution of Equation (32), or of its differential-equation equivalent, is a much simpler task than solution of the Wiener-Hopf equation.
- **p. 7 / Introduction - extractive body cue:** The covariance matrix of the estimation error is
- **p. 6 / Introduction - extractive body cue:** The estimation error is also governed by a linear dynamic system.
- **p. 7 / Introduction - extractive body cue:** Thus Φ* is also the transition matrix of the linear dynamic system governing the error.
- **p. 8 / Introduction - extractive body cue:** Qˆ (T - τ) matrix of quadratic form defining error criterion.
- **p. 4 / Introduction - extractive body cue:** This shows that, if w also minimizes the quadratic loss, we must have 0 ) ( 2 = -w x E
- **p. 4 / Introduction - extractive body cue:** Without being able to separate in some sense causes and effects, i.e., without the assumption of causality, one can hardly hope for useful results.
- **p. 6 / Introduction - extractive body cue:** In any case, y~ (t/t - 1) generates a linear manifold (possibly 0) which we denote by Z(t).

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 부분 관측·noise가 있는 동적 시스템.
- **Input boundary:** 시간별 sensor observation과 알려진 model/control input.
- **Output/decision under evaluation:** causal estimate, prediction 또는 smoothing output.
- **Primary target:** estimation error, covariance 또는 downstream state quality.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Introduction | SYSTEM / EVALUATION SCOPE UNRESOLVED | This is due to two things: (1) The time dependence of Φ(t + 1; t) and M(t); (2) the fact that the estimation starts ... | p. 8 (Introduction) |
| Introduction | SYSTEM / EVALUATION SCOPE UNRESOLVED | These results may be summarized as follows: | p. 4 (Introduction) |
| Introduction | SYSTEM / EVALUATION SCOPE UNRESOLVED | These results are well-known though not easily accessible in the control systems literature. | p. 4 (Introduction) |
| Introduction | SYSTEM / EVALUATION SCOPE UNRESOLVED | (i) The results stated in Theorem 3 do not resolve completely Problem I. | p. 7 (Introduction) |
| Introduction | SYSTEM / EVALUATION SCOPE UNRESOLVED | If t1 ≥ t + 1, we first observe by repeated application of (16) that x(t + s) = Φ(t + s; t + ... | p. 7 (Introduction) |

## Dataset / Benchmark Role

- **p. 7 / Introduction - extractive body cue:** Of course, the solution of Equation (32), or of its differential-equation equivalent, is a much simpler task than solution of the Wiener-Hopf equation.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Of course, the solution of Equation (32), or of its differential-equation equivalent, is a much simpler task than solution of the Wiener-Hopf equation. | embodiment, simulator version and control stack | p. 7 (Introduction) |
| Task/environment | not recovered | reset, timeout, object/scene variation | 본문 anchor 없음 |
| Observation/sensor | 시간별 sensor observation과 알려진 model/control input | calibration, preprocessing, privileged input | p. 5 (Introduction), p. 4 (Introduction) |
| Output/decision | causal estimate, prediction 또는 smoothing output | action frame, controller and termination | p. 4 (Introduction), p. 5 (Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The covariance matrix of the estimation error is | definition/direction/unit from same section | p. 7 (Introduction) |
| The estimation error is also governed by a linear dynamic system. | definition/direction/unit from same section | p. 6 (Introduction) |
| Thus Φ* is also the transition matrix of the linear dynamic system governing the error. | definition/direction/unit from same section | p. 7 (Introduction) |
| Qˆ (T - τ) matrix of quadratic form defining error criterion. | definition/direction/unit from same section | p. 8 (Introduction) |
| This shows that, if w also minimizes the quadratic loss, we must have 0 ) ( 2 = -w x E | definition/direction/unit from same section | p. 4 (Introduction) |
| Without being able to separate in some sense causes and effects, i.e., without the assumption of causality, one can hardly hope for useful results. | definition/direction/unit from same section | p. 4 (Introduction) |
| In any case, y~ (t/t - 1) generates a linear manifold (possibly 0) which we denote by Z(t). | definition/direction/unit from same section | p. 6 (Introduction) |
| 9 Q(t0 + τ) covariance of random excitation. | definition/direction/unit from same section | p. 8 (Introduction) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Without being able to separate in some sense causes and effects, i.e., without the assumption of causality, one can hardly hope for useful results. | comparison identity and matched condition | p. 4 (Introduction) |
| In a few cases, ∆* and Φ* can be put into "closed form." Without discussing here how (if at all) such closed forms can ... | comparison identity and matched condition | p. 9 (Introduction) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Without being able to separate in some sense causes and effects, i.e., without the assumption of causality, one can hardly hope for useful results. | component/input/data sensitivity | p. 4 (Introduction) |
| 8 M(t0 + τ) effect of state on observation. | component/input/data sensitivity | p. 8 (Introduction) |
| Mˆ (T - τ) effect of control vectors on state. | component/input/data sensitivity | p. 8 (Introduction) |
| If all coefficients of F(t), D(t), M(t) are constants, we say that the dynamic system (12) is timeinvariant or stationary. | component/input/data sensitivity | p. 5 (Introduction) |
| Now we remove the restriction that t1 = t + 1. | component/input/data sensitivity | p. 7 (Introduction) |
| In a few cases, ∆* and Φ* can be put into "closed form." Without discussing here how (if at all) such closed forms can ... | component/input/data sensitivity | p. 9 (Introduction) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The new method developed here is applied to two well-known problems, confirming and extending earlier results. | This is due to two things: (1) The time dependence of Φ(t + 1; t) and M(t); (2) the fact that the estimation starts ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Introduction), p. 4 (Introduction), p. 4 (Introduction), p. 7 (Introduction), p. 7 (Introduction), p. 8 (Introduction) |
| Primary metric/result | These results may be summarized as follows: | numeric claim only at cited anchor | p. 4 (Introduction) |

- Numeric sentences retained from the body:
- **p. 6 / Introduction - extractive body cue:** Therefore if t ≥ s we have Ex(t)x'(s) = ∑ - -∞ = 1 s r Φ(t; r + 1)Q(r) Φ'(s; r + 1).
- **p. 7 / Introduction - extractive body cue:** If t1 ≥ t + 1, we first observe by repeated application of (16) that x(t + s) = Φ(t + s; t + 1)x(t ...
- **p. 8 / Introduction - extractive body cue:** Problem I Problem II 1 x(t) (unobservable) state variables of random process. x(t) (observable) state variables of plant to be regulated.
- **p. 6 / Introduction - extractive body cue:** Therefore if t ≥ s we have Ex(t)x'(s) = ∑ - -∞ = 1 s r Φ(t; r + 1)Q(r) Φ'(s; r + 1).
- **p. 7 / Introduction - extractive body cue:** If t1 ≥ t + 1, we first observe by repeated application of (16) that x(t + s) = Φ(t + s; t + 1)x(t ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In any case, x2*(t/t - 1) = 0 at all times; one cannot predict independent noise! | p. 9 (Introduction) |
| body limitation/failure cue | but of course now Φ(t + 1; t), ∆(t) cannot be expressed in general in closed form. | p. 5 (Introduction) |
| body limitation/failure cue | If y~ (t/t - 1) ≡0, which means that the values of all components of this random vector are zero for almost every possible ... | p. 6 (Introduction) |
| body limitation/failure cue | It is a fairly generally accepted fact that primary macroscopic sources of random phenomena are independent gaussian processes.5 A well-known example is the noise ... | p. 5 (Introduction) |
| body limitation/failure cue | The first general solution of the noise-free regulator problem is due to the author [18]. | p. 8 (Introduction) |
| body limitation/failure cue | The Dual Problem Let us now consider another problem which is conceptually very different from optimal estimation, namely, the noise-free regulator problem. | p. 8 (Introduction) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Once P*(t) has been computed via (32) starting at t = t0, the explicit specification of the optimal linear filter is immediately available from ... | p. 7 (Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / Introduction - extractive body cue:** In any case, x2*(t/t - 1) = 0 at all times; one cannot predict independent noise!
- **p. 5 / Introduction - extractive body cue:** but of course now Φ(t + 1; t), ∆(t) cannot be expressed in general in closed form.
- **p. 6 / Introduction - extractive body cue:** If y~ (t/t - 1) ≡0, which means that the values of all components of this random vector are zero for almost every possible event, ...
- **p. 5 / Introduction - extractive body cue:** It is a fairly generally accepted fact that primary macroscopic sources of random phenomena are independent gaussian processes.5 A well-known example is the noise voltage ...
- **p. 8 / Introduction - extractive body cue:** The first general solution of the noise-free regulator problem is due to the author [18].
- **p. 8 / Introduction - extractive body cue:** The Dual Problem Let us now consider another problem which is conceptually very different from optimal estimation, namely, the noise-free regulator problem.

- **PDF anchors reviewed:** datasets p. 7 (Introduction), metrics p. 7 (Introduction), p. 6 (Introduction), p. 7 (Introduction), p. 8 (Introduction), p. 4 (Introduction), p. 4 (Introduction), baselines p. 4 (Introduction), p. 9 (Introduction), results p. 8 (Introduction), p. 4 (Introduction), p. 4 (Introduction), p. 7 (Introduction), p. 7 (Introduction), p. 8 (Introduction).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
