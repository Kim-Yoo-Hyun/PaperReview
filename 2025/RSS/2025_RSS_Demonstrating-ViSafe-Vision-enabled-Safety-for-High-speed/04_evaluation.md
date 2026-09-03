# Evaluation - Demonstrating ViSafe: Vision-enabled Safety for High-speed Detect and Avoid

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p002.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p002.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (Evaluation/Results): evaluation statement was not stated or recoverable in the selected PDF body.

## Evaluation Body Digest

- **p. 7 / A. Experiment Design - extractive body cue:** These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings.
- **p. 7 / A. Experiment Design - extractive body cue:** The ViSafeenabled ego agent is tested against an airborne intruder in various collision geometries.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 6. Horizontal rate of closure comparisons across diferent weather conditions in the digital twin: Higher values ind apart, showcasing diverging & safe wajectories. Across ...
- **p. 10 / VI. LEARNED CHALLENGES AND LIMITATIONS - extractive body cue:** 3) Inaecuracies in vision-based inference: Vision-based state estimation is not perfect; therefore, false positives can often throw the safety module off, We had to use ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** A. Experiment Design (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| A. Experiment Design | EMPIRICAL / REAL-ROBOT OR HARDWARE | These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings. | p. 7 (A. Experiment Design) |

## Dataset / Benchmark Role

- **p. 7 / A. Experiment Design - extractive body cue:** These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 5 / Figure/Table caption - extractive body cue:** Fig.3. Encounter geometry and information required for visionenabled ‘and heading with iy. The intruer's
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings. Table I shows the various agents, collision geometries, commanded ground ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 6. Horizontal rate of closure comparisons across diferent weather conditions in the digital twin: Higher values ind apart, showcasing diverging & safe wajectories. Across ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings. | embodiment, simulator version and control stack | p. 7 (A. Experiment Design) |
| Task/environment | not stated or recoverable in the selected PDF body | reset, timeout, object/scene variation | 본문 anchor 없음 |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 2 (4) First-of-its-kind real-world flight tests demonstrating that), p. 2 (2) Custom-built SWaP-C hardware that simultaneously) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 4 (IV. ViSafe FRAMEWORK), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The ViSafeenabled ego agent is tested against an airborne intruder in various collision geometries. | definition/direction/unit from same section | p. 7 (A. Experiment Design) |
| Fig. 4. These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings. Table I shows the various agents, collision geometries, commanded ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 6. Horizontal rate of closure comparisons across diferent weather conditions in the digital twin: Higher values ind apart, showcasing diverging & safe wajectories. ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 6. Horizontal rate of closure comparisons across diferent weather conditions in the digital twin: Higher values ind apart, showcasing diverging & safe wajectories. ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| There are variants of this algorithm for different agent types in different airspaces (ACAS Xa, Xu), etc. ‘The key factor driving the development of ... | no result cue | PDF body cue; verify exact table/figure and matched conditions | 본문 anchor 없음 |
| Primary metric/result | not separately recovered | numeric claim only at cited anchor | 본문 anchor 없음 |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 3) Inaecuracies in vision-based inference: Vision-based state estimation is not perfect; therefore, false positives can often throw the safety module off, We had to ... | p. 10 (VI. LEARNED CHALLENGES AND LIMITATIONS) |
| body limitation/failure cue | The ViSafeenabled ego agent is tested against an airborne intruder in various collision geometries. | p. 7 (A. Experiment Design) |
| body limitation/failure cue | Fig. 4. These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings. Table I shows the various agents, collision geometries, commanded ... | p. 7 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use a simple PD controller as our nominal controller, where the computed desired safe control ujaje is then converted into low-level drone control ... | p. 7 (C. Supervisory Safety Controller) |
| where ¢ > 0,n >0 and k >0 are hyperparameters to be tuned. | p. 6 (C. Supervisory Safety Controller) |
| A is another hyperparameter that controls the rate of change of the barrier function. | p. 6 (C. Supervisory Safety Controller) |
| (13), which can be solved to compute the desired safe control tjafe. | p. 7 (C. Supervisory Safety Controller) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / VI. LEARNED CHALLENGES AND LIMITATIONS - extractive body cue:** 3) Inaecuracies in vision-based inference: Vision-based state estimation is not perfect; therefore, false positives can often throw the safety module off, We had to use ...
- **p. 7 / A. Experiment Design - extractive body cue:** The ViSafeenabled ego agent is tested against an airborne intruder in various collision geometries.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings. Table I shows the various agents, collision geometries, commanded ground ...

- **Evidence anchors reviewed:** datasets p. 7 (A. Experiment Design), metrics p. 7 (A. Experiment Design), p. 7 (Figure/Table caption), p. 10 (Figure/Table caption), baselines p. 10 (Figure/Table caption), results 본문 anchor 없음.
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings. (p. 7, A. Experiment Design).
- **Metric evidence:** The ViSafeenabled ego agent is tested against an airborne intruder in various collision geometries. (p. 7, A. Experiment Design).
- **Baseline/ablation evidence:** Fig. 6. Horizontal rate of closure comparisons across diferent weather conditions in the digital twin: Higher values ind apart, showcasing diverging & safe wajectories. Across the diferent weather scenarios, ViSafeshoweases ... (p. 10, Figure/Table caption).
- **Failure/negative evidence:** Across our wide array of simulation and real-world tests, ‘we find that our current system struggles when the intruder is below the horizon, As acknowledged in the benchmarking of ‘our ... (p. 11, B. Limitations).
