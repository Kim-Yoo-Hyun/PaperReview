# Evaluation - FOCI: Trajectory Optimization on Gaussian Splats

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2505.08510; PDF retrieval source: https://arxiv.org/pdf/2505.08510. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (A. Trajectory Evaluation), p. 3 (III. METHOD)): Environment Initial Guess Time Solve Time # of Gaussians Narrow Corridor 0.24s 0.47s 24k Pillars 0.25s 0.45s 49k Machine Hall 0.22s 2.12s 243k Stonehenge 0.55s 0.83s 138k TABLE II: Planning ...

## Evaluation Body Digest

- **p. 5 / A. Trajectory Evaluation - extractive body cue:** Environment Initial Guess Time Solve Time # of Gaussians Narrow Corridor 0.24s 0.47s 24k Pillars 0.25s 0.45s 49k Machine Hall 0.22s 2.12s 243k Stonehenge 0.55s ...
- **p. 5 / A. Trajectory Evaluation - extractive body cue:** 3: Trajectories planned for a 3 Gaussian robot rotating through realistic scenes.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** In this section, we evaluate our algorithm by applying it to planning problems in different environments represented by 3DGS.
- **p. 5 / A. Trajectory Evaluation - extractive body cue:** As Figure 2b shows, the planning algorithm effectively leverages the asymmetry of ANYmal to pass through the narrow opening collision-free.
- **p. 5 / A. Trajectory Evaluation - extractive body cue:** The algorithm gracefully handles trajectories requiring additional turns while adapting the orientation to keep a maximum distance from the wall.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Trajectories planned for the ANYmal robot through real world obstacles. On the bottom the actual robot can be seen at the site following ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of control ...
- **p. 3 / III. METHOD - extractive body cue:** The spline can then be evaluated with x(s′) =  1 s′ s′2 s′3 1 6   1 4 1 0 -3 0 3 ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 4); A. Trajectory Evaluation (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| A. Trajectory Evaluation | SYSTEM / EVALUATION SCOPE UNRESOLVED | Environment Initial Guess Time Solve Time # of Gaussians Narrow Corridor 0.24s 0.47s 24k Pillars 0.25s 0.45s 49k Machine Hall 0.22s 2.12s 243k Stonehenge ... | p. 5 (A. Trajectory Evaluation) |
| III. METHOD | SYSTEM / EVALUATION SCOPE UNRESOLVED | The spline can then be evaluated with x(s′) =  1 s′ s′2 s′3 1 6   1 4 1 0 -3 0 ... | p. 3 (III. METHOD) |

## Dataset / Benchmark Role

- **p. 5 / A. Trajectory Evaluation - extractive body cue:** Environment Initial Guess Time Solve Time # of Gaussians Narrow Corridor 0.24s 0.47s 24k Pillars 0.25s 0.45s 49k Machine Hall 0.22s 2.12s 243k Stonehenge 0.55s ...
- **p. 5 / A. Trajectory Evaluation - extractive body cue:** 3: Trajectories planned for a 3 Gaussian robot rotating through realistic scenes.
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** In this section, we evaluate our algorithm by applying it to planning problems in different environments represented by 3DGS.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Four different orientation-aware trajectories planned through a Stonehenge environment for an ANYmal
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2: Sample trajectories created on synthetic testing data showing a 3 Gaussian robot rotating to navigate the environ- ments. The 3 Gaussians are shown ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Trajectories planned for a 3 Gaussian robot rotating through realistic scenes. 2) General Trajectory Planning Through 3DGS: Figure 3 shows that we can ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Trajectories planned for the ANYmal robot through real world obstacles. On the bottom the actual robot can be seen at the site following ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Comparison of the solver's creation and runtime running on the CPU and GPU for 50k environmental Gaus- sians and one robot Gaussian. The ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Optimization time for orientation-aware planning using increasingly complex robot models. These are planned through the Stonehenge environment with 138k Gaussians.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: The collection of paths used to evaluate different methods with various start and end goals around Stonehenge. The RRT* path is is shown ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of control ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Environment Initial Guess Time Solve Time # of Gaussians Narrow Corridor 0.24s 0.47s 24k Pillars 0.25s 0.45s 49k Machine Hall 0.22s 2.12s 243k Stonehenge ... | embodiment, simulator version and control stack | p. 5 (A. Trajectory Evaluation), p. 5 (A. Trajectory Evaluation) |
| Task/environment | 3: Trajectories planned for a 3 Gaussian robot rotating through realistic scenes. | reset, timeout, object/scene variation | p. 5 (A. Trajectory Evaluation), p. 4 (IV. EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (III. METHOD), p. 6 (Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (III. METHOD), p. 3 (III. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| As Figure 2b shows, the planning algorithm effectively leverages the asymmetry of ANYmal to pass through the narrow opening collision-free. | definition/direction/unit from same section | p. 5 (A. Trajectory Evaluation) |
| The algorithm gracefully handles trajectories requiring additional turns while adapting the orientation to keep a maximum distance from the wall. | definition/direction/unit from same section | p. 5 (A. Trajectory Evaluation) |
| Fig. 4: Trajectories planned for the ANYmal robot through real world obstacles. On the bottom the actual robot can be seen at the site ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Fig. 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 5: Comparison of the solver's creation and runtime running on the CPU and GPU for 50k environmental Gaus- sians and one robot Gaussian. ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

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
| In this paper, we propose an algorithm that enables a robot to perform trajectory optimization directly on the 3D Gaussians. | Environment Initial Guess Time Solve Time # of Gaussians Narrow Corridor 0.24s 0.47s 24k Pillars 0.25s 0.45s 49k Machine Hall 0.22s 2.12s 243k Stonehenge ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (A. Trajectory Evaluation), p. 3 (III. METHOD) |
| Primary metric/result | The spline can then be evaluated with x(s′) =  1 s′ s′2 s′3 1 6   1 4 1 0 -3 0 ... | numeric claim only at cited anchor | p. 3 (III. METHOD) |

- Numeric sentences retained from the body:
- **p. 5 / A. Trajectory Evaluation - extractive body cue:** Environment Initial Guess Time Solve Time # of Gaussians Narrow Corridor 0.24s 0.47s 24k Pillars 0.25s 0.45s 49k Machine Hall 0.22s 2.12s 243k Stonehenge 0.55s ...
- **p. 3 / III. METHOD - extractive body cue:** The spline can then be evaluated with x(s′) =  1 s′ s′2 s′3 1 6   1 4 1 0 -3 0 3 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of control ... | p. 7 (V. LIMITATIONS) |
| body limitation/failure cue | This means that when computing the overlap integral over the environment, flat regions with text or patterns have a slightly higher collision cost than | p. 7 (V. LIMITATIONS) |
| body limitation/failure cue | As Figure 2b shows, the planning algorithm effectively leverages the asymmetry of ANYmal to pass through the narrow opening collision-free. | p. 5 (A. Trajectory Evaluation) |
| body limitation/failure cue | 2) General Trajectory Planning Through 3DGS: Figure 3 shows that we can plan collision-free trajectories through splats that were created directly from the real-world ... | p. 5 (A. Trajectory Evaluation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Runtime We evaluate the performance of our method by comparing the runtimes of the Casadi optimization on a single CPU core, multiple CPU cores, ... | p. 6 (Method) |
| While a significant speedup can be observed when optimizing on multiple CPU cores using OpenMP, our custom GPU-enabled implementation is 320 times faster, often ... | p. 6 (Method) |
| The "serial" method is on a single CPU core, "OpenMP" runs on multiple CPU cores and CasADi Warp is our custom GPU implementation. | p. 7 (Method) |
| 5: Comparison of the solver's creation and runtime running on the CPU and GPU for 50k environmental Gaussians and one robot Gaussian. | p. 7 (Method) |
| All experiments are run on an Intel i7-8750H with 16 GB of RAM and an NVIDIA RTX 2070 Max-Q. | p. 4 (IV. EXPERIMENTS) |
| Furthermore, we demonstrate the use of the algorithm for navigating an ANYmal robot on hardware to highlight the importance of orientation-aware planning. | p. 5 (A. Trajectory Evaluation) |
| We exploit the independent summation structure of the collision measure (Equation 5) and run this computation on the GPU in parallel. | p. 4 (III. METHOD) |
| We compute the time derivative with dix dti = dix dsi   ds dt i and assume m := ds dt to be constant. | p. 3 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / V. LIMITATIONS - extractive body cue:** 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of control points.
- **p. 7 / V. LIMITATIONS - extractive body cue:** This means that when computing the overlap integral over the environment, flat regions with text or patterns have a slightly higher collision cost than
- **p. 5 / A. Trajectory Evaluation - extractive body cue:** As Figure 2b shows, the planning algorithm effectively leverages the asymmetry of ANYmal to pass through the narrow opening collision-free.
- **p. 5 / A. Trajectory Evaluation - extractive body cue:** 2) General Trajectory Planning Through 3DGS: Figure 3 shows that we can plan collision-free trajectories through splats that were created directly from the real-world environments.

- **Evidence anchors reviewed:** datasets p. 5 (A. Trajectory Evaluation), p. 5 (A. Trajectory Evaluation), p. 4 (IV. EXPERIMENTS), metrics p. 5 (A. Trajectory Evaluation), p. 5 (A. Trajectory Evaluation), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 7 (Figure/Table caption), results p. 5 (A. Trajectory Evaluation), p. 3 (III. METHOD).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Environment Initial Guess Time Solve Time # of Gaussians Narrow Corridor 0.24s 0.47s 24k Pillars 0.25s 0.45s 49k Machine Hall 0.22s 2.12s 243k Stonehenge 0.55s 0.83s 138k TABLE II: Planning ... (p. 5, A. Trajectory Evaluation).
- **Metric evidence:** The algorithm gracefully handles trajectories requiring additional turns while adapting the orientation to keep a maximum distance from the wall. (p. 5, A. Trajectory Evaluation).
- **Baseline/ablation evidence:** Fig. 5: Comparison of the solver's creation and runtime running on the CPU and GPU for 50k environmental Gaus- sians and one robot Gaussian. The "serial" method is on a ... (p. 7, Figure/Table caption).
- **Failure/negative evidence:** 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of control points. (p. 7, V. LIMITATIONS).
