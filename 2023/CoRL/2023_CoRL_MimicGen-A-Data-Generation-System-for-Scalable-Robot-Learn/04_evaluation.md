# Evaluation - MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (45 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v229/mandlekar23a.html; PDF retrieval source: https://arxiv.org/pdf/2310.17596. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 5 (6 Experiments), p. 6 (6 Experiments), p. 8 (Figure/Table caption), p. 5 (6 Experiments)): Figure 4: (left) Agent Performance on Source and Generated Datasets. Success rates (3 seeds) of image- based agents trained with BC on the 10 source demos and each 1000 demo ...

## Evaluation Body Digest

- **p. 5 / 6 Experiments - extractive body cue:** We present experiments that (1) highlight the diverse array of situations that MimicGen can generate data for, (2) show that MimicGen compares favorably to collecting ...
- **p. 5 / 6 Experiments - extractive body cue:** A straightforward application of MimicGen is to collect a small dataset on some task of interest and then generate more data for that task.
- **p. 6 / 6 Experiments - extractive body cue:** Assembly 1.3 ± 0.9 82.0 ± 1.6 62.7 ± 2.5 13.3 ± 3.8 Hammer Cleanup 59.3 ± 5.7 100.0 ± 0.0 62.7 ± 4.7 - ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: (left) Agent Performance on Source and Generated Datasets. Success rates (3 seeds) of image- based agents trained with BC on the 10 source ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: (left) Reset Distributions. Each task has a default reset distribution for the objects (D0), a broader one (D1), and some had a more ...
- **p. 5 / 6 Experiments - extractive body cue:** MimicGen data vastly improves agent performance on the source task.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: MimicGen Overview. We introduce a data generation system that can produce large diverse datasets from a small number of human demonstrations by re-purposing ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: MimicGen System Pipeline. (left) MimicGen first parses the demos from the source dataset into segments, where each segment corresponds to an object-centric subtask ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** 6 Experiments (p. 5); 1. How can I reproduce experiment results? (p. 17).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4: (left) Agent Performance on Source and Generated Datasets. Success rates (3 seeds) of image- based agents trained with BC on the 10 ... | p. 6 (Figure/Table caption) |
| 6 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | MimicGen data vastly improves agent performance on the source task. | p. 5 (6 Experiments) |
| 6 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Assembly 1.3 ± 0.9 82.0 ± 1.6 62.7 ± 2.5 13.3 ± 3.8 Hammer Cleanup 59.3 ± 5.7 100.0 ± 0.0 62.7 ± 4.7 ... | p. 6 (6 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 5: (left) Reset Distributions. Each task has a default reset distribution for the objects (D0), a broader one (D1), and some had a ... | p. 8 (Figure/Table caption) |
| 6 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We present experiments that (1) highlight the diverse array of situations that MimicGen can generate data for, (2) show that MimicGen compares favorably to ... | p. 5 (6 Experiments) |

## Dataset / Benchmark Role

- **p. 5 / 6 Experiments - extractive body cue:** We present experiments that (1) highlight the diverse array of situations that MimicGen can generate data for, (2) show that MimicGen compares favorably to collecting ...
- **p. 5 / 6 Experiments - extractive body cue:** A straightforward application of MimicGen is to collect a small dataset on some task of interest and then generate more data for that task.
- **p. 6 / 6 Experiments - extractive body cue:** Assembly 1.3 ± 0.9 82.0 ± 1.6 62.7 ± 2.5 13.3 ± 3.8 Hammer Cleanup 59.3 ± 5.7 100.0 ± 0.0 62.7 ± 4.7 - ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: MimicGen Overview. We introduce a data generation system that can produce large diverse datasets from a small number of human demonstrations by re-purposing ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: MimicGen System Pipeline. (left) MimicGen first parses the demos from the source dataset into segments, where each segment corresponds to an object-centric subtask ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Tasks. We use MimicGen to generate demonstrations for several tasks - these are a subset. They span a wide variety of behaviors including ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: (left) Agent Performance on Source and Generated Datasets. Success rates (3 seeds) of image- based agents trained with BC on the 10 source ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: (left) Reset Distributions. Each task has a default reset distribution for the objects (D0), a broader one (D1), and some had a more ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We present experiments that (1) highlight the diverse array of situations that MimicGen can generate data for, (2) show that MimicGen compares favorably to ... | embodiment, simulator version and control stack | p. 5 (6 Experiments), p. 5 (6 Experiments) |
| Task/environment | A straightforward application of MimicGen is to collect a small dataset on some task of interest and then generate more data for that task. | reset, timeout, object/scene variation | p. 5 (6 Experiments), p. 6 (6 Experiments) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 5 (4 Method), p. 4 (4 Method) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 4 (4 Method), p. 5 (4 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 4: (left) Agent Performance on Source and Generated Datasets. Success rates (3 seeds) of image- based agents trained with BC on the 10 ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Assembly 1.3 ± 0.9 82.0 ± 1.6 62.7 ± 2.5 13.3 ± 3.8 Hammer Cleanup 59.3 ± 5.7 100.0 ± 0.0 62.7 ± 4.7 ... | definition/direction/unit from same section | p. 6 (6 Experiments) |
| Figure 5: (left) Reset Distributions. Each task has a default reset distribution for the objects (D0), a broader one (D1), and some had a ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| We present experiments that (1) highlight the diverse array of situations that MimicGen can generate data for, (2) show that MimicGen compares favorably to ... | definition/direction/unit from same section | p. 5 (6 Experiments) |
| MimicGen data vastly improves agent performance on the source task. | definition/direction/unit from same section | p. 5 (6 Experiments) |
| Figure 1: MimicGen Overview. We introduce a data generation system that can produce large diverse datasets from a small number of human demonstrations by ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 2: MimicGen System Pipeline. (left) MimicGen first parses the demos from the source dataset into segments, where each segment corresponds to an object-centric ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Assembly 1.3 ± 0.9 82.0 ± 1.6 62.7 ± 2.5 13.3 ± 3.8 Hammer Cleanup 59.3 ± 5.7 100.0 ± 0.0 62.7 ± 4.7 ... | comparison identity and matched condition | p. 6 (6 Experiments) |
| Figure 4: (left) Agent Performance on Source and Generated Datasets. Success rates (3 seeds) of image- based agents trained with BC on the 10 ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 2: MimicGen System Pipeline. (left) MimicGen first parses the demos from the source dataset into segments, where each segment corresponds to an object-centric ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Figure 3: Tasks. We use MimicGen to generate demonstrations for several tasks - these are a subset. They span a wide variety of behaviors ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Figure 5: (left) Reset Distributions. Each task has a default reset distribution for the objects (D0), a broader one (D1), and some had a ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We make the following contributions: • We introduce MimicGen, a system for generating large diverse datasets from a small number of human demonstrations by ... | Figure 4: (left) Agent Performance on Source and Generated Datasets. Success rates (3 seeds) of image- based agents trained with BC on the 10 ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 5 (6 Experiments), p. 6 (6 Experiments), p. 8 (Figure/Table caption), p. 5 (6 Experiments) |
| Primary metric/result | MimicGen data vastly improves agent performance on the source task. | numeric claim only at cited anchor | p. 5 (6 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 6 Experiments - extractive body cue:** Task Source D0 D1 D2 Stack 26.0 ± 1.6 100.0 ± 0.0 99.3 ± 0.9 - Stack Three 0.7 ± 0.9 92.7 ± 1.9 86.7 ...
- **p. 6 / 6 Experiments - extractive body cue:** Assembly 1.3 ± 0.9 82.0 ± 1.6 62.7 ± 2.5 13.3 ± 3.8 Hammer Cleanup 59.3 ± 5.7 100.0 ± 0.0 62.7 ± 4.7 - ...
- **p. 4 / 4 Method - extractive body cue:** Let T A B be the homogeneous 4×4 matrix that represents the pose of frame A with respect to frame B.
- **p. 5 / 4 Method - extractive body cue:** Attempts that did not achieve task success were discarded, and data collection kept proceeding for each task variant until 1000 task successes were collected.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We hope that MimicGen motivates and enables exploring a more data-centric perspective on imitation learning in future work. | p. 8 (8 Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The steps above repeat for each subtask until the final segment has been executed. | p. 4 (4 Method) |
| 2 (right), this consists of three key steps for each subtask: (1) choosing a reference subtask segment in the source dataset, (2) transforming the ... | p. 4 (4 Method) |
| [7] for reporting policy performance - the maximum success rate across all policy evaluations, across 3 different seeds (full training details in Appendix O). | p. 5 (4 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 8 Conclusion - extractive body cue:** We hope that MimicGen motivates and enables exploring a more data-centric perspective on imitation learning in future work.

- **PDF anchors reviewed:** datasets p. 5 (6 Experiments), p. 5 (6 Experiments), p. 6 (6 Experiments), metrics p. 6 (Figure/Table caption), p. 6 (6 Experiments), p. 8 (Figure/Table caption), p. 5 (6 Experiments), p. 5 (6 Experiments), p. 2 (Figure/Table caption), baselines p. 6 (6 Experiments), p. 6 (Figure/Table caption), results p. 6 (Figure/Table caption), p. 5 (6 Experiments), p. 6 (6 Experiments), p. 8 (Figure/Table caption), p. 5 (6 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
