# Evaluation - VLM-GroNav: Robot Navigation Using Physically Grounded Vision-Language Models in Outdoor Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2409.20445v1. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (Figure/Table caption)): Fig. 1: Overview of our VLM-GroNav system: Our method uses the given information to achieve a navigation objective. We leverage VLMs and aerial imagery to estimate initial terrain traversability. The ...

## Evaluation Body Digest

- **p. 5 / V. RESULTS AND ANALYSIS - extractive PDF cue:** Implementation For the real-world experiments, we utilize both the Ghost Vision 60 legged robot and the Clearpath Husky wheeled robot.
- **p. 5 / V. RESULTS AND ANALYSIS - extractive PDF cue:** Comparison Methods • DWA [30]: A baseline motion planner that performs simple collision avoidance and goal-reaching behaviors. • GA-Nav [4]:
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 2: The VLM-GroNav system employs a reasoning module that integrates visual inputs from aerial imagery, weather conditions, and proprioceptive data through a large VLM ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3: Comparison of navigation trajectories across various environments using different methods: DWA (Black), GA-Nav (orange), CoNVOI (Dark purple), ViNT (light purple), and our method ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Overview of our VLM-GroNav system: Our method uses the given information to achieve a navigation objective. We leverage VLMs and aerial imagery to ...
- **p. 6 / 3. VLM-GroNav consistently achieves the highest success - extractive PDF cue:** We observe that this results in errors in predicting the terrain's traversbility while navigating, which in turn ill-informs the local and global planners, causing failures.
- **p. 4 / IV. OUR APPROACH - extractive PDF cue:** The difference between these measurements reflects the degree of slippage experienced by the robot.
- **p. 4 / IV. OUR APPROACH - extractive PDF cue:** The traversability indicator (τsinkage and τslip) are time-shifted to match the visual inputs, τshifted(t) = τ(t -∆t).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** V. RESULTS AND ANALYSIS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1: Overview of our VLM-GroNav system: Our method uses the given information to achieve a navigation objective. We leverage VLMs and aerial imagery ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / V. RESULTS AND ANALYSIS - extractive PDF cue:** Implementation For the real-world experiments, we utilize both the Ghost Vision 60 legged robot and the Clearpath Husky wheeled robot.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Overview of our VLM-GroNav system: Our method uses the given information to achieve a navigation objective. We leverage VLMs and aerial imagery to ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 2: The VLM-GroNav system employs a reasoning module that integrates visual inputs from aerial imagery, weather conditions, and proprioceptive data through a large VLM ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3: Comparison of navigation trajectories across various environments using different methods: DWA (Black), GA-Nav (orange), CoNVOI (Dark purple), ViNT (light purple), and our method ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Implementation For the real-world experiments, we utilize both the Ghost Vision 60 legged robot and the Clearpath Husky wheeled robot. | embodiment, simulator version and control stack | p. 5 (V. RESULTS AND ANALYSIS) |
| Task/environment | not recovered | reset, timeout, object/scene variation | 본문 anchor 없음 |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (IV. OUR APPROACH), p. 3 (III. BACKGROUND) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (IV. OUR APPROACH), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Comparison Methods • DWA [30]: A baseline motion planner that performs simple collision avoidance and goal-reaching behaviors. • GA-Nav [4]: | definition/direction/unit from same section | p. 5 (V. RESULTS AND ANALYSIS) |
| Fig. 2: The VLM-GroNav system employs a reasoning module that integrates visual inputs from aerial imagery, weather conditions, and proprioceptive data through a large ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 3: Comparison of navigation trajectories across various environments using different methods: DWA (Black), GA-Nav (orange), CoNVOI (Dark purple), ViNT (light purple), and our ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Comparison Methods • DWA [30]: A baseline motion planner that performs simple collision avoidance and goal-reaching behaviors. • GA-Nav [4]: | comparison identity and matched condition | p. 5 (V. RESULTS AND ANALYSIS) |
| Fig. 3: Comparison of navigation trajectories across various environments using different methods: DWA (Black), GA-Nav (orange), CoNVOI (Dark purple), ViNT (light purple), and our ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |

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
| Main contributions: We present VLM-GroNav, a novel navigation method that integrates Vision-Language Models (VLMs) with proprioception-based sensing. | Fig. 1: Overview of our VLM-GroNav system: Our method uses the given information to achieve a navigation objective. We leverage VLMs and aerial imagery ... | PDF body cue; verify exact table/figure and matched conditions | p. 1 (Figure/Table caption) |
| Primary metric/result | not separately recovered | numeric claim only at cited anchor | 본문 anchor 없음 |

- Numeric sentences retained from the body:
- **p. 5 / V. RESULTS AND ANALYSIS - extractive PDF cue:** The Ghost Vision 60 is equipped with a front-facing wide-angle camera, an OS1-32 LiDAR, GPS, and an onboard Intel NUC 11 system, which includes an ...
- **p. 6 / A method - extractive PDF cue:** 4 DWA [30] 20 0.97 31923 GA-NAV [4] 40 1.51 28345 CoNVOI [51] 60 1.44 29473 ViNT [50] 40 1.16 25451 VLM-GroNav w/o GP 60 ...
- **p. 6 / A method - extractive PDF cue:** Evaluation Metrics • Success Rate: The ratio of successful navigation trials where the robot was able to reach its goal without freezing or colliding with ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We observe that this results in errors in predicting the terrain's traversbility while navigating, which in turn ill-informs the local and global planners, causing ... | p. 6 (3. VLM-GroNav consistently achieves the highest success) |
| body limitation/failure cue | The difference between these measurements reflects the degree of slippage experienced by the robot. | p. 4 (IV. OUR APPROACH) |
| body limitation/failure cue | The traversability indicator (τsinkage and τslip) are time-shifted to match the visual inputs, τshifted(t) = τ(t -∆t). | p. 4 (IV. OUR APPROACH) |
| body limitation/failure cue | Comparison Methods • DWA [30]: A baseline motion planner that performs simple collision avoidance and goal-reaching behaviors. • GA-Nav [4]: | p. 5 (V. RESULTS AND ANALYSIS) |
| body limitation/failure cue | Scenarios 3 and 4 involve the wheeled robot navigating through unstructured and slippery terrains, VLM-GroNav excels at maintaining a high success rate and reduced ... | p. 6 (3. VLM-GroNav consistently achieves the highest success) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The Ghost Vision 60 is equipped with a front-facing wide-angle camera, an OS1-32 LiDAR, GPS, and an onboard Intel NUC 11 system, which includes ... | p. 5 (V. RESULTS AND ANALYSIS) |
| Adaptive Local Planner Our local planner adapts in real-time to changes in terrain traversability by integrating proprioceptive feedback with a light VLM (with low ... | p. 5 (IV. OUR APPROACH) |
| To compute the traversability indicator τ, we normalize the sinkage indicator by applying a scaling factor Γ. | p. 3 (IV. OUR APPROACH) |
| 4 DWA [30] 20 0.97 31923 GA-NAV [4] 40 1.51 28345 CoNVOI [51] 60 1.44 29473 ViNT [50] 40 1.16 25451 VLM-GroNav w/o GP ... | p. 6 (A method) |
| Evaluation Metrics • Success Rate: The ratio of successful navigation trials where the robot was able to reach its goal without freezing or colliding ... | p. 6 (A method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 3. VLM-GroNav consistently achieves the highest success - extractive PDF cue:** We observe that this results in errors in predicting the terrain's traversbility while navigating, which in turn ill-informs the local and global planners, causing failures.
- **p. 4 / IV. OUR APPROACH - extractive PDF cue:** The difference between these measurements reflects the degree of slippage experienced by the robot.
- **p. 4 / IV. OUR APPROACH - extractive PDF cue:** The traversability indicator (τsinkage and τslip) are time-shifted to match the visual inputs, τshifted(t) = τ(t -∆t).
- **p. 5 / V. RESULTS AND ANALYSIS - extractive PDF cue:** Comparison Methods • DWA [30]: A baseline motion planner that performs simple collision avoidance and goal-reaching behaviors. • GA-Nav [4]:
- **p. 6 / 3. VLM-GroNav consistently achieves the highest success - extractive PDF cue:** Scenarios 3 and 4 involve the wheeled robot navigating through unstructured and slippery terrains, VLM-GroNav excels at maintaining a high success rate and reduced IMU ...

- **PDF anchors reviewed:** datasets p. 5 (V. RESULTS AND ANALYSIS), metrics p. 5 (V. RESULTS AND ANALYSIS), p. 4 (Figure/Table caption), p. 5 (Figure/Table caption), baselines p. 5 (V. RESULTS AND ANALYSIS), p. 5 (Figure/Table caption), results p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
