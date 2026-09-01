# Evaluation - Constrained Bimanual Planning with Analytic Inverse Kinematics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.08770; PDF retrieval source: https://arxiv.org/pdf/2309.08770. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (IV. RESULTS), p. 6 (IV. RESULTS)): AtlasBiRRT runtimes were only averaged over successful runs (not including timeouts).

## Evaluation Body Digest

- **p. 6 / IV. RESULTS - extractive PDF cue:** GCS can use such regions to plan motions for objects of different sizes; we include hardware demonstrations in our results video.
- **p. 6 / IV. RESULTS - extractive PDF cue:** 4: Robot configurations sampled from various IRIS regions. average path length and planning time.
- **p. 5 / IV. RESULTS - extractive PDF cue:** To evaluate the merits of our IK parametrization for constrained planning, we consider a task where the two arms must move an object around a ...
- **p. 5 / IV. RESULTS - extractive PDF cue:** Constrained Trajectory Optimization.
- **p. 6 / IV. RESULTS - extractive PDF cue:** (c) A region that represents varying grasp distances, in addition to collision-free configurations in the shelf (not shown).
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Hardware setup for our experiments. The two arms must work together to move an objects between the shelves, avoiding collisions and respecting the ...
- **p. 5 / IV. RESULTS - extractive PDF cue:** We use the analytic IK map presented in [42].
- **p. 5 / IV. RESULTS - extractive PDF cue:** Paths marked with an asterisk were not collision-free.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** robot mechanism의 state와 task-space dynamics.
- **Input boundary:** joint/task state, reference와 sensor feedback.
- **Output/decision under evaluation:** torque, force, velocity 또는 position command.
- **Primary target:** tracking, stability, constraint satisfaction과 contact behavior.
- **Detected evaluation headings:** IV. RESULTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | AtlasBiRRT runtimes were only averaged over successful runs (not including timeouts). | p. 5 (IV. RESULTS) |
| IV. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | GCS can use such regions to plan motions for objects of different sizes; we include hardware demonstrations in our results video. | p. 6 (IV. RESULTS) |

## Dataset / Benchmark Role

- **p. 6 / IV. RESULTS - extractive PDF cue:** GCS can use such regions to plan motions for objects of different sizes; we include hardware demonstrations in our results video.
- **p. 6 / IV. RESULTS - extractive PDF cue:** 4: Robot configurations sampled from various IRIS regions. average path length and planning time.
- **p. 5 / IV. RESULTS - extractive PDF cue:** To evaluate the merits of our IK parametrization for constrained planning, we consider a task where the two arms must move an object around a ...
- **p. 5 / IV. RESULTS - extractive PDF cue:** Constrained Trajectory Optimization.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Hardware setup for our experiments. The two arms must work together to move an objects between the shelves, avoiding collisions and respecting the ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2: A high level description of our parametrization. The controlled arm can move freely, and analytic IK is used to position the subordinate arm ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 3: Continuous (left) and discrete (right) self-motions of a 7DoF arm. The continuous self-motion yields an additional degree of freedom for the planner to ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4: Robot configurations sampled from various IRIS regions. average path length and planning time. We set a maximum planning time of 10 minutes for ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | GCS can use such regions to plan motions for objects of different sizes; we include hardware demonstrations in our results video. | embodiment, simulator version and control stack | p. 6 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Task/environment | 4: Robot configurations sampled from various IRIS regions. average path length and planning time. | reset, timeout, object/scene variation | p. 6 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Observation/sensor | joint/task state, reference와 sensor feedback | calibration, preprocessing, privileged input | p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Output/decision | torque, force, velocity 또는 position command | action frame, controller and termination | p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| (c) A region that represents varying grasp distances, in addition to collision-free configurations in the shelf (not shown). | definition/direction/unit from same section | p. 6 (IV. RESULTS) |
| Fig. 1: Hardware setup for our experiments. The two arms must work together to move an objects between the shelves, avoiding collisions and respecting ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| We use the analytic IK map presented in [42]. | definition/direction/unit from same section | p. 5 (IV. RESULTS) |
| Paths marked with an asterisk were not collision-free. | definition/direction/unit from same section | p. 5 (IV. RESULTS) |
| And in Figure 4 (c), we visualize an IRIS region that allows the grasp distance to vary. | definition/direction/unit from same section | p. 6 (IV. RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We do not compare to any GCS baseline without IK, as the constraint manifold is inherently nonconvex; IK-GCS is the first proposal for extending ... | comparison identity and matched condition | p. 5 (IV. RESULTS) |
| We compare these parametrized planners with constrained planning baselines. | comparison identity and matched condition | p. 5 (IV. RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We do not compare to any GCS baseline without IK, as the constraint manifold is inherently nonconvex; IK-GCS is the first proposal for extending ... | component/input/data sensitivity | p. 5 (IV. RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Then, we present our parametrization of the constraint manifold for bimanual planning, and discuss its relevant geometric and topological properties. | AtlasBiRRT runtimes were only averaged over successful runs (not including timeouts). | PDF body cue; verify exact table/figure and matched conditions | p. 5 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Primary metric/result | GCS can use such regions to plan motions for objects of different sizes; we include hardware demonstrations in our results video. | numeric claim only at cited anchor | p. 6 (IV. RESULTS) |

- Numeric sentences retained from the body:
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** (If n = 6, then the Mi are zero-dimensional, i.e., discrete points.) Examples of the continuous and discrete self motions for a 7DoF arm are ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 1: Hardware setup for our experiments. The two arms must work together to move an objects between the shelves, avoiding collisions and respecting ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Paths marked with an asterisk were not collision-free. | p. 5 (IV. RESULTS) |
| body limitation/failure cue | Plans from the trajectory optimization baseline also had slight collisions with obstacles. | p. 5 (IV. RESULTS) |
| body limitation/failure cue | (c) A region that represents varying grasp distances, in addition to collision-free configurations in the shelf (not shown). | p. 6 (IV. RESULTS) |
| body limitation/failure cue | Fig. 4: Robot configurations sampled from various IRIS regions. average path length and planning time. We set a maximum planning time of 10 minutes ... | p. 6 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The forward kinematic mapping f : C →SE(3) computes the end-effector pose of the arm for a given choice of each joint angle. | p. 3 (III. METHODOLOGY) |
| 4] takes the arccos of an argument w, so we encode (6c) as /w/ ≥1 + ϵ. | p. 4 (III. METHODOLOGY) |
| We now describe the constraint sets CS needed for Algorithm 1 to generate g-convex sets in QVALID ∩QFREE, and how to encode (6c). | p. 4 (III. METHODOLOGY) |
| We use GCS-planner [8] with 19 regions, constructed from hand-selected seed points. | p. 5 (IV. RESULTS) |
| AtlasBiRRT runtimes were only averaged over successful runs (not including timeouts). | p. 5 (IV. RESULTS) |
| Overall, the PRM methods have the shortest online runtimes. | p. 6 (IV. RESULTS) |
| IK-BiRRT never timed out; the longest plan took 81.17 seconds to compute. | p. 6 (IV. RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Hardware setup for our experiments. The two arms must work together to move an objects between the shelves, avoiding collisions and respecting the ...
- **p. 5 / IV. RESULTS - extractive PDF cue:** Paths marked with an asterisk were not collision-free.
- **p. 5 / IV. RESULTS - extractive PDF cue:** Plans from the trajectory optimization baseline also had slight collisions with obstacles.
- **p. 6 / IV. RESULTS - extractive PDF cue:** (c) A region that represents varying grasp distances, in addition to collision-free configurations in the shelf (not shown).
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4: Robot configurations sampled from various IRIS regions. average path length and planning time. We set a maximum planning time of 10 minutes for ...

- **PDF anchors reviewed:** datasets p. 6 (IV. RESULTS), p. 6 (IV. RESULTS), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), metrics p. 6 (IV. RESULTS), p. 1 (Figure/Table caption), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 6 (IV. RESULTS), baselines p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), results p. 5 (IV. RESULTS), p. 6 (IV. RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
