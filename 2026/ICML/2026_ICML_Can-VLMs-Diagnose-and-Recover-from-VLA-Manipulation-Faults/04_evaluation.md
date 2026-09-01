# Evaluation - Can VLMs Diagnose and Recover from VLA Manipulation Faults?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`.
> Analysis basis: official ICML proceedings page (abstract only; public PDF unavailable) checked on 2026-09-02 (1 source page(s); official ICML proceedings page (abstract only; public PDF unavailable); extraction quality: medium); canonical paper source: https://kakigo.github.io/VLA-FixBench/; body source: https://icml.cc/virtual/2026/poster/64203. The note is an evidence-anchored abstract/source-page analysis; exact tables/equations or section details remain at the cited source anchors. Evidence boundary: abstract/source-page only; method details, exact metrics, limitations and failure cases require full-text review. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

abstract/source-page evaluation/result cue (p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?)): The upper-bound analysis using human expert intervention shows that an idealized feedback loop can improve task success rates by 13\% on LIBERO and 35\% on real-world robots.

## Evaluation Body Digest

- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** The upper-bound analysis using human expert intervention shows that an idealized feedback loop can improve task success rates by 13\% on LIBERO and 35\% on ...
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** We introduce VLA-FixBench, a dataset of robot manipulation failures covering problems in perception, planning, and control.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** Our results show that current AI models are still limited in reliable robot recovery, but accurate human-level feedback can substantially improve task success.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** This suggests that better failure diagnosis and recovery could make future robotic systems safer and more reliable.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** We also build an evaluation framework to test how well different vision-language models can detect failures, locate when and where they happen, and provide useful ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | abstract/source-page experiment/result cue | Anchor |
|---|---|---|---|
| Can VLMs Diagnose and Recover from VLA Manipulation Faults? | BENCHMARK / DATASET | The upper-bound analysis using human expert intervention shows that an idealized feedback loop can improve task success rates by 13\% on LIBERO and 35\% ... | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| Can VLMs Diagnose and Recover from VLA Manipulation Faults? | BENCHMARK / DATASET | Our results show that current AI models are still limited in reliable robot recovery, but accurate human-level feedback can substantially improve task success. | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |

## Dataset / Benchmark Role

- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** The upper-bound analysis using human expert intervention shows that an idealized feedback loop can improve task success rates by 13\% on LIBERO and 35\% on ...
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** We introduce VLA-FixBench, a dataset of robot manipulation failures covering problems in perception, planning, and control.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | abstract/source-page-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The upper-bound analysis using human expert intervention shows that an idealized feedback loop can improve task success rates by 13\% on LIBERO and 35\% ... | embodiment, simulator version and control stack | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| Task/environment | We introduce VLA-FixBench, a dataset of robot manipulation failures covering problems in perception, planning, and control. | reset, timeout, object/scene variation | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | 본문 anchor 없음 |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The upper-bound analysis using human expert intervention shows that an idealized feedback loop can improve task success rates by 13\% on LIBERO and 35\% ... | definition/direction/unit from same section | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| Our results show that current AI models are still limited in reliable robot recovery, but accurate human-level feedback can substantially improve task success. | definition/direction/unit from same section | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| no baseline sentence selected | not reported | verify comparison table |

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
| We introduce VLA-FixBench, a dataset of robot manipulation failures covering problems in perception, planning, and control. | The upper-bound analysis using human expert intervention shows that an idealized feedback loop can improve task success rates by 13\% on LIBERO and 35\% ... | abstract/source-page cue; verify exact table/figure and matched conditions | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| Primary metric/result | Our results show that current AI models are still limited in reliable robot recovery, but accurate human-level feedback can substantially improve task success. | numeric claim only at cited anchor | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This suggests that better failure diagnosis and recovery could make future robotic systems safer and more reliable. | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |
| body limitation/failure cue | We also build an evaluation framework to test how well different vision-language models can detect failures, locate when and where they happen, and provide ... | p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| no implementation/reproducibility sentence selected | verify appendix and code/project |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** This suggests that better failure diagnosis and recovery could make future robotic systems safer and more reliable.
- **p. 1 / Can VLMs Diagnose and Recover from VLA Manipulation Faults? - extractive body cue:** We also build an evaluation framework to test how well different vision-language models can detect failures, locate when and where they happen, and provide useful ...

- **Evidence anchors reviewed:** datasets p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), metrics p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), baselines 본문 anchor 없음, results p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?), p. 1 (Can VLMs Diagnose and Recover from VLA Manipulation Faults?).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
