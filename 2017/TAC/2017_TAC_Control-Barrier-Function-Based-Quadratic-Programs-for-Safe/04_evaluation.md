# Evaluation - Control Barrier Function Based Quadratic Programs for Safety Critical Systems

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1609.06408; PDF retrieval source: https://arxiv.org/pdf/1609.06408. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS), p. 14 (0.1 N), p. 11 (Figure/Table caption), p. 15 (Figure/Table caption)): A video of the results is available on YouTube [57].

## Evaluation Body Digest

- **p. 13 / VI. SIMULATION RESULTS - extractive body cue:** The parameters used for the simulation are given in Table I.
- **p. 13 / VI. SIMULATION RESULTS - extractive body cue:** Simulation results for ACC Various problem formulations are compared here.
- **p. 14 / VI. SIMULATION RESULTS - extractive body cue:** 14 ZCBFs generate a smoother input trajectory (see Fig.
- **p. 14 / 0.1 N - extractive body cue:** Simulation results for lane keeping are shown in Fig.6.
- **p. 14 / 0.1 N - extractive body cue:** The feedforward term xff = [0, 0, 0, rd]⊤reduces tracking error.
- **p. 13 / VI. SIMULATION RESULTS - extractive body cue:** Comparison of two QPs Recall that Figure 2 showed simulation results obtained by applying the QP controller in (ACC QP), where the force constraints were ...
- **p. 13 / VI. SIMULATION RESULTS - extractive body cue:** Since RCBF Bo F is less conservative than Bc F , the car maintains a smaller following distance, but the specified time-headway constraint is always ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. Relationships among reciprocal barrier functions (RBFs), zeroing barrier functions (ZBFs), and forward invariance that are developed in the paper. The underlying analysis can ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** VI. SIMULATION RESULTS (p. 13).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| VI. SIMULATION RESULTS | EMPIRICAL / SIMULATION | A video of the results is available on YouTube [57]. | p. 13 (VI. SIMULATION RESULTS) |
| VI. SIMULATION RESULTS | EMPIRICAL / SIMULATION | Simulation results for ACC Various problem formulations are compared here. | p. 13 (VI. SIMULATION RESULTS) |
| 0.1 N | EMPIRICAL / SIMULATION | Simulation results for lane keeping are shown in Fig.6. | p. 14 (0.1 N) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 2. Simulation results of the ACC problem based on (ACC QP) (left) speed of the lead car and the controlled car with the ... | p. 11 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Fig. 6. Simulation results of the QP-based controller for LK problem. (left) lateral displacement with ymax = 0.9m (middle) lateral acceleration with amax = ... | p. 15 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 13 / VI. SIMULATION RESULTS - extractive body cue:** The parameters used for the simulation are given in Table I.
- **p. 13 / VI. SIMULATION RESULTS - extractive body cue:** Simulation results for ACC Various problem formulations are compared here.
- **p. 14 / VI. SIMULATION RESULTS - extractive body cue:** 14 ZCBFs generate a smoother input trajectory (see Fig.
- **p. 14 / 0.1 N - extractive body cue:** Simulation results for lane keeping are shown in Fig.6.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. Relationships among reciprocal barrier functions (RBFs), zeroing barrier functions (ZBFs), and forward invariance that are developed in the paper. The underlying analysis can ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 2. Simulation results of the ACC problem based on (ACC QP) (left) speed of the lead car and the controlled car with the desired ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 3. The projection of CF onto the (y, ˙y)-plane is bounded by the upper and lower curves. The subset CLK ⊂Int(CF ) is bounded ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 4. Comparison of QP (ACC QP) with QP (ACC-QP2). (top) speed of the lead car and the controlled car based on QP (ACC QP) ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 5. Comparison of the input force generated from QP (ACC-QP2) using ZCBFs and RCBFs. (top) conservative CBFs (bottom) optimal CBFs D. LK simulation The ...
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 6. Simulation results of the QP-based controller for LK problem. (left) lateral displacement with ymax = 0.9m (middle) lateral acceleration with amax = 0.3g ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The parameters used for the simulation are given in Table I. | embodiment, simulator version and control stack | p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS) |
| Task/environment | Simulation results for ACC Various problem formulations are compared here. | reset, timeout, object/scene variation | p. 13 (VI. SIMULATION RESULTS), p. 14 (VI. SIMULATION RESULTS) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 10 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 13 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 10 (V. TWO AUTOMOTIVE SAFETY PROBLEMS VIA QPS), p. 2 (B. Contributions) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The feedforward term xff = [0, 0, 0, rd]⊤reduces tracking error. | definition/direction/unit from same section | p. 14 (0.1 N) |
| Comparison of two QPs Recall that Figure 2 showed simulation results obtained by applying the QP controller in (ACC QP), where the force constraints ... | definition/direction/unit from same section | p. 13 (VI. SIMULATION RESULTS) |
| Since RCBF Bo F is less conservative than Bc F , the car maintains a smaller following distance, but the specified time-headway constraint is ... | definition/direction/unit from same section | p. 13 (VI. SIMULATION RESULTS) |
| 14 ZCBFs generate a smoother input trajectory (see Fig. | definition/direction/unit from same section | p. 14 (VI. SIMULATION RESULTS) |
| Fig. 1. Relationships among reciprocal barrier functions (RBFs), zeroing barrier functions (ZBFs), and forward invariance that are developed in the paper. The underlying analysis ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Simulation results for ACC Various problem formulations are compared here. | comparison identity and matched condition | p. 13 (VI. SIMULATION RESULTS) |
| Comparison of RCBFs and ZCBFs We also consider the ZCBFs for our ACC problem, which are associated with functions ho F and hc F ... | comparison identity and matched condition | p. 13 (VI. SIMULATION RESULTS) |
| Comparison of the input force generated from QP (ACC-QP2) using ZCBFs and RCBFs. | comparison identity and matched condition | p. 14 (VI. SIMULATION RESULTS) |
| Fig. 4. Comparison of QP (ACC QP) with QP (ACC-QP2). (top) speed of the lead car and the controlled car based on QP (ACC ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 3. The projection of CF onto the (y, ˙y)-plane is bounded by the upper and lower curves. The subset CLK ⊂Int(CF ) is ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Importantly, under mild conditions on C, it is demonstrated that the conditions we propose are also necessary and sufficient for forward invariance, and result ... | A video of the results is available on YouTube [57]. | PDF body cue; verify exact table/figure and matched conditions | p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS), p. 14 (0.1 N), p. 11 (Figure/Table caption), p. 15 (Figure/Table caption) |
| Primary metric/result | Simulation results for ACC Various problem formulations are compared here. | numeric claim only at cited anchor | p. 13 (VI. SIMULATION RESULTS) |

- Numeric sentences retained from the body:
- **p. 14 / 0.1 N - extractive body cue:** f2 0.25 Ns2/m2 a′ f 0.25 a 1.11 m Cf 133000 N/rad af 0.25 b 1.59 m Cr 98800 N/rad c 10 v0 27.7 m/s ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Future work will be devoted to building upon the foundations presented in this paper in the context of safety-critical control of cyber-physical systems, with ... | p. 14 (VII. CONCLUSIONS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Unbounded function values, however, may be undesirable when real-time/embedded implementations are considered. | p. 5 (II. RECIPROCAL AND ZEROING BARRIER FUNCTIONS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / VII. CONCLUSIONS - extractive body cue:** Future work will be devoted to building upon the foundations presented in this paper in the context of safety-critical control of cyber-physical systems, with a ...

- **PDF anchors reviewed:** datasets p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS), p. 14 (VI. SIMULATION RESULTS), p. 14 (0.1 N), metrics p. 14 (0.1 N), p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS), p. 14 (VI. SIMULATION RESULTS), p. 2 (Figure/Table caption), baselines p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS), p. 14 (VI. SIMULATION RESULTS), p. 14 (Figure/Table caption), results p. 13 (VI. SIMULATION RESULTS), p. 13 (VI. SIMULATION RESULTS), p. 14 (0.1 N), p. 11 (Figure/Table caption), p. 15 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
