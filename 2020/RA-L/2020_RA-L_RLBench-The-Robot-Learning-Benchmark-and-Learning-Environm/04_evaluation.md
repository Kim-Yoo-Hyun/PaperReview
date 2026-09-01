# Evaluation - RLBench: The Robot Learning Benchmark & Learning Environment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1909.12271; PDF retrieval source: https://arxiv.org/pdf/1909.12271. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (Figure/Table caption)): Fig. 6: An example of a task python file. When using the task building tool, users are able to simultaneously edit the V-REP scene whilst also changing the various behaviour ...

## Evaluation Body Digest

- **p. 3 / III. BENCHMARK PROPERTIES - extractive body cue:** However, with the rise of deep-learning methods becoming more prominent in robotics, we believe it is important to find the potential and limits of these ...
- **p. 3 / III. BENCHMARK PROPERTIES - extractive body cue:** Moving to simulation solves this, but at the risk of developing solutions that may not run as well in the real-world.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: Example usage of the RLBench Environment for training a reinforcement learning agent. When using demon- strations, users can either point to a set ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6: An example of a task python file. When using the task building tool, users are able to simultaneously edit the V-REP scene whilst ...
- **p. 3 / III. BENCHMARK PROPERTIES - extractive body cue:** We therefore wanted to have a range of tasks, including both easy tasks, such as reaching, which would be well suited to new and emerging ...
- **p. 5 / IV. RLBENCH - extractive body cue:** Once a task has been created, we provide a task validation tool, that attempts to collect a number of demonstrations of the designed task in ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** III. BENCHMARK PROPERTIES (p. 3).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Fig. 6: An example of a task python file. When using the task building tool, users are able to simultaneously edit the V-REP scene ... | p. 5 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 3 / III. BENCHMARK PROPERTIES - extractive body cue:** However, with the rise of deep-learning methods becoming more prominent in robotics, we believe it is important to find the potential and limits of these ...
- **p. 3 / III. BENCHMARK PROPERTIES - extractive body cue:** Moving to simulation solves this, but at the risk of developing solutions that may not run as well in the real-world.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: RLBench is a large-scale benchmark consisting of 100 completely unique, hand-designed tasks. In this figure we show a sample of 24 tasks that ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: The V-REP scene consists of a Franka Panda af- fixed to a wooden table, surrounded by 3 directional lights. Observations include rgb, depth, ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: A sample of the visual observations given from both the over-the-shoulder stereo and eye-in-hand monocular cameras, which supply rgb, depth, and mask images. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: An example showing the distinction between task, variation, and episode. In this case, the ‘stack blocks' task has V variations, each with E ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: Example usage of the RLBench Environment for training a reinforcement learning agent. When using demon- strations, users can either point to a set ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6: An example of a task python file. When using the task building tool, users are able to simultaneously edit the V-REP scene whilst ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7: Top shows the frequency of words in the variation descriptions with function words removed, leaving only content words. Bottom shows the average length ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | However, with the rise of deep-learning methods becoming more prominent in robotics, we believe it is important to find the potential and limits of ... | embodiment, simulator version and control stack | p. 3 (III. BENCHMARK PROPERTIES), p. 3 (III. BENCHMARK PROPERTIES) |
| Task/environment | Moving to simulation solves this, but at the risk of developing solutions that may not run as well in the real-world. | reset, timeout, object/scene variation | p. 3 (III. BENCHMARK PROPERTIES) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 4 (IV. RLBENCH) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 3 (III. BENCHMARK PROPERTIES), p. 4 (IV. RLBENCH) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 5: Example usage of the RLBench Environment for training a reinforcement learning agent. When using demon- strations, users can either point to a ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 6: An example of a task python file. When using the task building tool, users are able to simultaneously edit the V-REP scene ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We therefore wanted to have a range of tasks, including both easy tasks, such as reaching, which would be well suited to new and ... | comparison identity and matched condition | p. 3 (III. BENCHMARK PROPERTIES) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 7: Top shows the frequency of words in the variation descriptions with function words removed, leaving only content words. Bottom shows the average ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| We therefore wanted to have a range of tasks, including both easy tasks, such as reaching, which would be well suited to new and ... | component/input/data sensitivity | p. 3 (III. BENCHMARK PROPERTIES) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To that end, we present RLBench, which is an ambitious large-scale benchmark and learning environment designed to facilitate research in a number of both ... | Fig. 6: An example of a task python file. When using the task building tool, users are able to simultaneously edit the V-REP scene ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (Figure/Table caption) |
| Primary metric/result | not separately recovered | numeric claim only at cited anchor | 본문 anchor 없음 |

- Numeric sentences retained from the body:
- **p. 1 / I. INTRODUCTION - extractive body cue:** Each of the 100 tasks comes with a number of textual descriptions and an infinite set of demonstrations made possible through our task building tools ...
- **p. 5 / IV. RLBENCH - extractive body cue:** 1 from rlbench.environment import Environment 2 from rlbench.action_modes import ActionMode 3 from rlbench.tasks import ReachTarget 4 5 DATASET = 'path/to/demo/dataset' 6 7 env = Environment( ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We therefore wanted to have a range of tasks, including both easy tasks, such as reaching, which would be well suited to new and ... | p. 3 (III. BENCHMARK PROPERTIES) |
| body limitation/failure cue | Once a task has been created, we provide a task validation tool, that attempts to collect a number of demonstrations of the designed task ... | p. 5 (IV. RLBENCH) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Benchmarking code and videos can be found here1. | p. 1 (Abstract) |
| This large-scale benchmark aims to accelerate progress in a number of vision-guided manipulation research areas, including: reinforcement learning, imitation learning, multi-task learning, geometric computer ... | p. 1 (Abstract) |
| Moving to simulation solves this, but at the risk of developing solutions that may not run as well in the real-world. | p. 3 (III. BENCHMARK PROPERTIES) |
| 1 from rlbench.environment import Environment 2 from rlbench.action_modes import ActionMode 3 from rlbench.tasks import ReachTarget 4 5 DATASET = 'path/to/demo/dataset' 6 7 env = ... | p. 5 (IV. RLBENCH) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / III. BENCHMARK PROPERTIES - extractive body cue:** We therefore wanted to have a range of tasks, including both easy tasks, such as reaching, which would be well suited to new and emerging ...
- **p. 5 / IV. RLBENCH - extractive body cue:** Once a task has been created, we provide a task validation tool, that attempts to collect a number of demonstrations of the designed task in ...

- **PDF anchors reviewed:** datasets p. 3 (III. BENCHMARK PROPERTIES), p. 3 (III. BENCHMARK PROPERTIES), metrics p. 5 (Figure/Table caption), p. 5 (Figure/Table caption), baselines p. 3 (III. BENCHMARK PROPERTIES), results p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
