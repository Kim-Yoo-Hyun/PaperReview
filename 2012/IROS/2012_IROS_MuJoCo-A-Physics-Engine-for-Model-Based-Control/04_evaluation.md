# Evaluation - MuJoCo: A Physics Engine for Model-Based Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/IROS.2012.6386109; PDF retrieval source: https://doi.org/10.1109/IROS.2012.6386109. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 2 (I. INTRODUCTION), p. 4 (5) Integrate numerically to obtain the next state), p. 5 (5) Integrate numerically to obtain the next state), p. 5 (5) Integrate numerically to obtain the next state), p. 3 (5) Integrate numerically to obtain the next state), p. 4 (5) Integrate numerically to obtain the next state)): Although this approach is a significant improvement over earlier spring-damper models of contact, it still requires manual tuning and small time steps.

## Evaluation Body Digest

- **p. 5 / 5) Integrate numerically to obtain the next state - extractive body cue:** It can be used to analyze data or to compute the torques that will cause a robot to follow a reference trajectory.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This limits their applications to robotics where contact dynamics are key.
- **p. 5 / 5) Integrate numerically to obtain the next state - extractive body cue:** However in the presence of branch-induced sparsity typical in robotics these algorithms are not much faster than the present approach [4].
- **p. 6 / III. MODELING - extractive body cue:** Once a valid model object is created in the runtime environment by either method, the built-in compiler converts it into a low-level C structure used ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Note that contact simulation is an area of active research, unlike simulation of smooth multi-joint dynamics where the book has basically been written [4].
- **p. 4 / 5) Integrate numerically to obtain the next state - extractive body cue:** Furthermore the number of Newton-like iterations 0 200 400 600 simulation time (ms) vertical velocity normal impulse Fig.
- **p. 4 / 5) Integrate numerically to obtain the next state - extractive body cue:** Instead of following the LCP approach, MuJoCo implements three new algorithms for contact simulation based on our recent work, as summarized next.
- **p. 6 / III. MODELING - extractive body cue:** The built-in parser loads the MJCF file and creates a runtime C++ object describing the entire model.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** physics simulation의 robot/environment model.
- **Input boundary:** simulated state, geometry, contact와 control input.
- **Output/decision under evaluation:** simulation step, trajectory 또는 environment query.
- **Primary target:** physical plausibility, speed, reproducibility와 task utility.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| I. INTRODUCTION | BENCHMARK / DATASET | Although this approach is a significant improvement over earlier spring-damper models of contact, it still requires manual tuning and small time steps. | p. 2 (I. INTRODUCTION) |
| 5) Integrate numerically to obtain the next state | BENCHMARK / DATASET | Each iteration involves factorization of a -by-matrix; this could potentially be improved using Hessian-free methods. | p. 4 (5) Integrate numerically to obtain the next state) |
| 5) Integrate numerically to obtain the next state | BENCHMARK / DATASET | Of course violations should be difficult to achieve, i.e. the inferred control force should be large in the corresponding subspace. | p. 5 (5) Integrate numerically to obtain the next state) |
| 5) Integrate numerically to obtain the next state | BENCHMARK / DATASET | While these theoretical results are important for understanding how the CPU time will scale with the number of DOFs, in practice the performance of ... | p. 5 (5) Integrate numerically to obtain the next state) |
| 5) Integrate numerically to obtain the next state | BENCHMARK / DATASET | The vector v0 is the contact velocity which results in the absence of an impulse. | p. 3 (5) Integrate numerically to obtain the next state) |

## Dataset / Benchmark Role

- **p. 5 / 5) Integrate numerically to obtain the next state - extractive body cue:** It can be used to analyze data or to compute the torques that will cause a robot to follow a reference trajectory.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This limits their applications to robotics where contact dynamics are key.
- **p. 5 / 5) Integrate numerically to obtain the next state - extractive body cue:** However in the presence of branch-induced sparsity typical in robotics these algorithms are not much faster than the present approach [4].
- **p. 6 / III. MODELING - extractive body cue:** Once a valid model object is created in the runtime environment by either method, the built-in compiler converts it into a low-level C structure used ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Note that contact simulation is an area of active research, unlike simulation of smooth multi-joint dynamics where the book has basically been written [4].
- **p. 4 / 5) Integrate numerically to obtain the next state - extractive body cue:** Furthermore the number of Newton-like iterations 0 200 400 600 simulation time (ms) vertical velocity normal impulse Fig.
- **p. 4 / 5) Integrate numerically to obtain the next state - extractive body cue:** Instead of following the LCP approach, MuJoCo implements three new algorithms for contact simulation based on our recent work, as summarized next.
- **p. 6 / III. MODELING - extractive body cue:** The built-in parser loads the MJCF file and creates a runtime C++ object describing the entire model.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 1. Left: the algorithm is tested on a system consisting of several balls moving inside a cube. Right: average number of Newton-like iterations as ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2. Left: Rendering of a humanoid (used for testing) in the MuJoCo interactive 3D GUI. Right: a ball-drop test of the convex contact solver. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Number of smooth dynamics evaluations per second in a single thread, rounded to 1000. The key observation here is that MuJoCo is quite ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: CPU time (in seconds) for one evaluation of the trajectory cost, gradient and Hessian. The number of states where the dynamics are evaluated ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 3. Illustration of projects where we have used MuJoCo for control synthesis and modeling. A,B are from [9]. C is from [3]. D is ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: This is the inverse of Table 2. Here we show the number of dynamics evaluations per second. The results are quite remarkable. One ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | It can be used to analyze data or to compute the torques that will cause a robot to follow a reference trajectory. | embodiment, simulator version and control stack | p. 5 (5) Integrate numerically to obtain the next state), p. 2 (I. INTRODUCTION) |
| Task/environment | This limits their applications to robotics where contact dynamics are key. | reset, timeout, object/scene variation | p. 2 (I. INTRODUCTION), p. 5 (5) Integrate numerically to obtain the next state) |
| Observation/sensor | simulated state, geometry, contact와 control input | calibration, preprocessing, privileged input | p. 7 (III. MODELING), p. 2 (I. INTRODUCTION) |
| Output/decision | simulation step, trajectory 또는 environment query | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 7 (III. MODELING) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Furthermore the pyramid approximation introduces errors. | definition/direction/unit from same section | p. 4 (5) Integrate numerically to obtain the next state) |
| Convex solver A favorable trade-off between speed and accuracy is obtained by replacing the nonlinear complementarity constraints (4, 5) with a convex optimization problem, ... | definition/direction/unit from same section | p. 4 (5) Integrate numerically to obtain the next state) |
| Gauss-Seidel) may be faster and have comparable accuracy. | definition/direction/unit from same section | p. 5 (5) Integrate numerically to obtain the next state) |
| This is sensible when simulating a large number of mostly disconnected bodies with few joint constraints, however it becomes both inaccurate and inefficient when ... | definition/direction/unit from same section | p. 2 (I. INTRODUCTION) |
| Solving for the contact impulse We now return to step 4. | definition/direction/unit from same section | p. 3 (5) Integrate numerically to obtain the next state) |
| Once this is done, we use (2) to obtain v+, and then integrate the position. | definition/direction/unit from same section | p. 3 (5) Integrate numerically to obtain the next state) |
| Diagonal solver The least accurate but fastest contact solver is a diagonal solver, which can be thought of as a mass-aware springdamper. | definition/direction/unit from same section | p. 5 (5) Integrate numerically to obtain the next state) |
| Different ways to construct a MuJoCo model MuJoCo models can exist on three levels of description: • XML model file in a new format ... | definition/direction/unit from same section | p. 6 (III. MODELING) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Performance on smooth dynamics compared to SD/FAST We measured the speed of multi-joint dynamics simulation in the absence of contacts or equality constraints. | comparison identity and matched condition | p. 7 (IV. TIMING TESTS) |
| Section IV presents timing tests and comparisons to SD/FAST - which does not handle contacts, but is the best prior engine for multi-joint dynamics ... | comparison identity and matched condition | p. 2 (I. INTRODUCTION) |
| It is needed for three reasons: is often singular; without the inverse cannot be defined (see below); one can enable contact interactions from a ... | comparison identity and matched condition | p. 4 (5) Integrate numerically to obtain the next state) |
| When there are no equality constraints and the contact solver has an exact inverse, the inverse dynamics can be computed without resorting to posthoc ... | comparison identity and matched condition | p. 6 (5) Integrate numerically to obtain the next state) |
| A unique feature of MuJoCo is that the primitive joint types can be composed into more complex joints, without having to define intermediate dummy ... | comparison identity and matched condition | p. 6 (III. MODELING) |
| This was done not only for speed comparisons, but also for debugging MuJoCo and making sure the results are numerically correct. | comparison identity and matched condition | p. 7 (IV. TIMING TESTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| It is needed for three reasons: is often singular; without the inverse cannot be defined (see below); one can enable contact interactions from a ... | component/input/data sensitivity | p. 4 (5) Integrate numerically to obtain the next state) |
| When there are no equality constraints and the contact solver has an exact inverse, the inverse dynamics can be computed without resorting to posthoc ... | component/input/data sensitivity | p. 6 (5) Integrate numerically to obtain the next state) |
| A unique feature of MuJoCo is that the primitive joint types can be composed into more complex joints, without having to define intermediate dummy ... | component/input/data sensitivity | p. 6 (III. MODELING) |
| Focusing for the moment on a single contact, let the contact impulse fbe partitioned as £ N; f F¤ where N is the normal ... | component/input/data sensitivity | p. 3 (5) Integrate numerically to obtain the next state) |
| In the normal direction for example, if the corresponding component of x is positive it encodes force (in which case the velocity is 0), ... | component/input/data sensitivity | p. 4 (5) Integrate numerically to obtain the next state) |
| This is done by computing the components of findependently for each contact (the diagonal solver ignores contact interactions by definition) and enforcing the friction-cone ... | component/input/data sensitivity | p. 5 (5) Integrate numerically to obtain the next state) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This is useful for approximating derivatives via finite differencing, which in turn enables numerical optimization. • Inverse dynamics can always be computed, even in ... | Although this approach is a significant improvement over earlier spring-damper models of contact, it still requires manual tuning and small time steps. | PDF body cue; verify exact table/figure and matched conditions | p. 2 (I. INTRODUCTION), p. 4 (5) Integrate numerically to obtain the next state), p. 5 (5) Integrate numerically to obtain the next state), p. 5 (5) Integrate numerically to obtain the next state), p. 3 (5) Integrate numerically to obtain the next state), p. 4 (5) Integrate numerically to obtain the next state) |
| Primary metric/result | Each iteration involves factorization of a -by-matrix; this could potentially be improved using Hessian-free methods. | numeric claim only at cited anchor | p. 4 (5) Integrate numerically to obtain the next state) |

- Numeric sentences retained from the body:
- **p. 3 / 5) Integrate numerically to obtain the next state - extractive body cue:** When there are no equality constraints we have = -1 and r = -1s.
- **p. 3 / 5) Integrate numerically to obtain the next state - extractive body cue:** Along the normal we have N ≥0 N ≥0 N N = 0 (4) These conditions correspond to the fact that the contact impulse cannot ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 1) Compute the Cartesian positions and orientations of all rigid bodies (i.e. the forward kinematics), detect potential collisions (with some safety margin), and construct ... | p. 3 (II. ALGORITHMIC FOUNDATIONS) |
| body limitation/failure cue | In the tangent plane we have vF parallel to fF ­ vFfF® ≤0 (5) °°fF°° ≤N The first line means that if there is ... | p. 3 (5) Integrate numerically to obtain the next state) |
| body limitation/failure cue | Since the underlying problem is NP-hard, the algorithm cannot always find the exact solution (which has 0 residual). | p. 4 (5) Integrate numerically to obtain the next state) |
| body limitation/failure cue | It is needed for three reasons: is often singular; without the inverse cannot be defined (see below); one can enable contact interactions from a ... | p. 4 (5) Integrate numerically to obtain the next state) |
| body limitation/failure cue | Instead it computes the desired next-state velocity v∗ which would result if penetrations decayed like criticallydamped springs (similar to equality-constraint violations) and there was ... | p. 5 (5) Integrate numerically to obtain the next state) |
| body limitation/failure cue | Their primary use in the engine is collision detection as well as tendon wrapping. | p. 7 (III. MODELING) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In terms of implementation, multiplication by -1 is done using sparse back-substitution (following sparse factorization), and the recurring matrix -1T = ¡ -1¢T is ... | p. 3 (5) Integrate numerically to obtain the next state) |
| The procedure for solving the above equations of motion consists of the following steps: | p. 2 (II. ALGORITHMIC FOUNDATIONS) |
| Although this approach is a significant improvement over earlier spring-damper models of contact, it still requires manual tuning and small time steps. | p. 2 (I. INTRODUCTION) |
| The quantities v0 are known, while fvneed to be computed. | p. 3 (5) Integrate numerically to obtain the next state) |
| In the normal direction for example, if the corresponding component of x is positive it encodes force (in which case the velocity is 0), ... | p. 4 (5) Integrate numerically to obtain the next state) |
| Convex solver A favorable trade-off between speed and accuracy is obtained by replacing the nonlinear complementarity constraints (4, 5) with a convex optimization problem, ... | p. 4 (5) Integrate numerically to obtain the next state) |
| Forward dynamics in the absence of contacts can alternatively be computed using () recursive algorithms. | p. 5 (5) Integrate numerically to obtain the next state) |
| It can be used to analyze data or to compute the torques that will cause a robot to follow a reference trajectory. | p. 5 (5) Integrate numerically to obtain the next state) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** 1) Compute the Cartesian positions and orientations of all rigid bodies (i.e. the forward kinematics), detect potential collisions (with some safety margin), and construct the ...
- **p. 3 / 5) Integrate numerically to obtain the next state - extractive body cue:** In the tangent plane we have vF parallel to fF ­ vFfF® ≤0 (5) °°fF°° ≤N The first line means that if there is slip ...
- **p. 4 / 5) Integrate numerically to obtain the next state - extractive body cue:** Since the underlying problem is NP-hard, the algorithm cannot always find the exact solution (which has 0 residual).
- **p. 4 / 5) Integrate numerically to obtain the next state - extractive body cue:** It is needed for three reasons: is often singular; without the inverse cannot be defined (see below); one can enable contact interactions from a distance ...
- **p. 5 / 5) Integrate numerically to obtain the next state - extractive body cue:** Instead it computes the desired next-state velocity v∗ which would result if penetrations decayed like criticallydamped springs (similar to equality-constraint violations) and there was no ...
- **p. 7 / III. MODELING - extractive body cue:** Their primary use in the engine is collision detection as well as tendon wrapping.

- **PDF anchors reviewed:** datasets p. 5 (5) Integrate numerically to obtain the next state), p. 2 (I. INTRODUCTION), p. 5 (5) Integrate numerically to obtain the next state), p. 6 (III. MODELING), p. 2 (I. INTRODUCTION), p. 4 (5) Integrate numerically to obtain the next state), metrics p. 4 (5) Integrate numerically to obtain the next state), p. 4 (5) Integrate numerically to obtain the next state), p. 5 (5) Integrate numerically to obtain the next state), p. 2 (I. INTRODUCTION), p. 3 (5) Integrate numerically to obtain the next state), p. 3 (5) Integrate numerically to obtain the next state), baselines p. 7 (IV. TIMING TESTS), p. 2 (I. INTRODUCTION), p. 4 (5) Integrate numerically to obtain the next state), p. 6 (5) Integrate numerically to obtain the next state), p. 6 (III. MODELING), p. 7 (IV. TIMING TESTS), results p. 2 (I. INTRODUCTION), p. 4 (5) Integrate numerically to obtain the next state), p. 5 (5) Integrate numerically to obtain the next state), p. 5 (5) Integrate numerically to obtain the next state), p. 3 (5) Integrate numerically to obtain the next state), p. 4 (5) Integrate numerically to obtain the next state).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
