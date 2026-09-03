# Evaluation - Linear-time Differential Inverse Kinematics: an Augmented Lagrangian Perspective

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p110.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p110.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS)): Supporting closed-loops is a relevant future research direction since several recent robots include them to improve some mechanical properties.

## Evaluation Body Digest

- **p. 8 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** Each benchmark scenario then consists of three tasks: • position p∗ com(t) for the upper-body target where the robot should place its center of mass ...
- **p. 8 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** Scenarios are defined as task target trajectories that evolve independently from the robot configuration.
- **p. 9 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** Following the steps (24), (26), (27), QP matrices and vectors are uniquely defined from task targets and the current robot configuration (see e.g. the documentation ...
- **p. 9 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** Comparison to QP-based inverse kinematics With the parameters we have described, the benchmark produces 92,000 IK problems.
- **p. 10 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** First, LOIK does not support robot topologies with internal closed loops, as its recursive derivation relies on a tree topology.
- **p. 10 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** Supporting closed-loops is a relevant future research direction since several recent robots include them to improve some mechanical properties.
- **p. 9 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** They solve the same underlying problem by computing the Jacobian matrix Ji(q) of the frame at the current configuration, and setting: AQP i = Ji(q) ...
- **p. 9 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** We perform one rollout integrating solutions from one method (calling both methods on each configuration qt) and one rollout integrating solutions from the other. edo ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** V. EXPERIMENTAL VALIDATION AND BENCHMARKS (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTAL VALIDATION AND BENCHMARKS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Supporting closed-loops is a relevant future research direction since several recent robots include them to improve some mechanical properties. | p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| V. EXPERIMENTAL VALIDATION AND BENCHMARKS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We evaluate the performance of differential IK solvers in a benchmark of inverse kinematics scenarios, which we plan to release as open source software ... | p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| V. EXPERIMENTAL VALIDATION AND BENCHMARKS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We observe in these results that, while LOIK is 1.5-2× faster than QP-based approaches on single-task arm scenarios, it scales more favorably when moving ... | p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| V. EXPERIMENTAL VALIDATION AND BENCHMARKS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Bottom: number of iterations each solver took to converge at each time step. roughly a factor of two. b) Residuals: We take a closer ... | p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |

## Dataset / Benchmark Role

- **p. 8 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** Each benchmark scenario then consists of three tasks: • position p∗ com(t) for the upper-body target where the robot should place its center of mass ...
- **p. 8 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** Scenarios are defined as task target trajectories that evolve independently from the robot configuration.
- **p. 9 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** Following the steps (24), (26), (27), QP matrices and vectors are uniquely defined from task targets and the current robot configuration (see e.g. the documentation ...
- **p. 9 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** Comparison to QP-based inverse kinematics With the parameters we have described, the benchmark produces 92,000 IK problems.
- **p. 10 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** First, LOIK does not support robot topologies with internal closed loops, as its recursive derivation relies on a tree topology.
- **p. 10 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** Supporting closed-loops is a relevant future research direction since several recent robots include them to improve some mechanical properties.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 9 / Figure/Table caption - extractive body cue:** Figure 7: Computation times for each method, on average over the 10 seconds of motion of each scenario (x-axis) with confidence intervals of ± one ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 8: Comparison of solution quality from LOIK, OSQP, and ProxQP for the 67-DOF Romeo humanoid scenario. Top: primal residual at each time step. Bottom: ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 9: Additional solver information from LOIK for the 67-DOF Romeo humanoid scenario. Top: number of active inequality constraints at termination for each time step. ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 11: LOIK iteration count with random initialization and warm-starting edo fanuc gen2 ur10 ur3 ur5 z1
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 12: Number of active inequality constraints associated with the problem set solved in Figure 11 It can be seen that LOIK's iteration count is ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Each benchmark scenario then consists of three tasks: • position p∗ com(t) for the upper-body target where the robot should place its center of ... | embodiment, simulator version and control stack | p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| Task/environment | Scenarios are defined as task target trajectories that evolve independently from the robot configuration. | reset, timeout, object/scene variation | p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 5 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE), p. 3 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| They solve the same underlying problem by computing the Jacobian matrix Ji(q) of the frame at the current configuration, and setting: AQP i = ... | definition/direction/unit from same section | p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| We perform one rollout integrating solutions from one method (calling both methods on each configuration qt) and one rollout integrating solutions from the other. ... | definition/direction/unit from same section | p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| We evaluate the performance of differential IK solvers in a benchmark of inverse kinematics scenarios, which we plan to release as open source software ... | definition/direction/unit from same section | p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| We check in particular that the ADMM penalty parameter µ remains within a reasonable range even on the infeasible problems at the beginning of ... | definition/direction/unit from same section | p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| Bottom: number of iterations each solver took to converge at each time step. roughly a factor of two. b) Residuals: We take a closer ... | definition/direction/unit from same section | p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Comparison to QP-based inverse kinematics With the parameters we have described, the benchmark produces 92,000 IK problems. | comparison identity and matched condition | p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| These comparisons are depicted in Fig. | comparison identity and matched condition | p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| 0 250 500 750 1000 1250 1500 1750 2000 10 2 10 1 Primal residual [m/s] Solvers LOIK OSQP ProxQP 0 250 500 750 ... | comparison identity and matched condition | p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| A tasks consists of two components: a target, as detailed in the latter two sections for the scenarios in this benchmark, and dynamics. | component/input/data sensitivity | p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| 2) Inequality constraints: We propose an ADMM-based strategy dealing with inequality constraints, where each ADMM iteration is made efficient by using the aforementioned inner ... | Supporting closed-loops is a relevant future research direction since several recent robots include them to improve some mechanical properties. | PDF body cue; verify exact table/figure and matched conditions | p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| Primary metric/result | We evaluate the performance of differential IK solvers in a benchmark of inverse kinematics scenarios, which we plan to release as open source software ... | numeric claim only at cited anchor | p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |

- Numeric sentences retained from the body:
- **p. 8 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** Our benchmark unrolls target trajectories for each scenario, with a time step δt = 5 ms and a trajectory duration of 10 seconds large enough ...
- **p. 9 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** For another point of reference to the state of the art, we also consider the quadratic programming formulation from DRAKE [45] where an additional optimization ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** While analytical solutions can be found mathematically for systems with a few degrees of freedom, the approach scales to at most 6-7 degrees of freedom ...
- **p. 2 / II. BACKGROUND - extractive body cue:** Solving Constrained QP problems via ADMM A powerful strategy for solving constrained optimization problems is the class of augmented Lagrangian methods (ALM) (also known as ...
- **p. 2 / II. BACKGROUND - extractive body cue:** First introduced in the 1970s by [21], ADMM is tailored to convex constrained optimization problems with separable decision variables and objectives.
- **p. 3 / III. LOW-COMPLEXITY DIFFERENTIAL INVERSE - extractive body cue:** Please note that for floating-base robots, the floating-base link is assumed to be connected to the 0-th link with a ‘free'-joint that permits motions in ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 9: Additional solver information from LOIK for the 67-DOF Romeo humanoid scenario. Top: number of active inequality constraints at termination for each time ... | p. 10 (Figure/Table caption) |
| body limitation/failure cue | LOIK scales essentially like the "QP lower bound" of frame Jacobian computations (another linear-time algorithm), with 3This means in particular that, for "OSQP (Drake)", ... | p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| body limitation/failure cue | First, LOIK does not support robot topologies with internal closed loops, as its recursive derivation relies on a tree topology. | p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Humanoids walk forward in all scenarios, with a stationary center-of-mass height computed from the robot's initial configuration. | p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| For a task over frame i with target T∗ i and whose transform in the current configuration q ∈C is Ti(q), the task dynamics ... | p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| For (2), we used timings computed internally by each solver. | p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| The additional "QP lower bound" measures the time taken to compute frame placement and Jacobian matrices, a pre-requisite to build QP matrices. | p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| The hyperparameters used with LOIK are reported in Sec. | p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| For OSQP and ProxQP, the default hyperparameters were used, with one exception for OSQP where we enforced checking termination at every iteration rather than ... | p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS) |
| For one, solving a differential IK quadratic program is still a resource-constrained operation, with computation times on the same scale of order as the ... | p. 1 (I. INTRODUCTION) |
| The ADMM iterates for solving problem (5) are given as: (vk+1, νk+1) = arg min v,ν LA IK(v, ν, zk, yk, wk) (6a) s.t. ... | p. 4 (III. LOW-COMPLEXITY DIFFERENTIAL INVERSE) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / Figure/Table caption - extractive body cue:** Figure 9: Additional solver information from LOIK for the 67-DOF Romeo humanoid scenario. Top: number of active inequality constraints at termination for each time step. ...
- **p. 9 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** LOIK scales essentially like the "QP lower bound" of frame Jacobian computations (another linear-time algorithm), with 3This means in particular that, for "OSQP (Drake)", (1) ...
- **p. 10 / V. EXPERIMENTAL VALIDATION AND BENCHMARKS - extractive body cue:** First, LOIK does not support robot topologies with internal closed loops, as its recursive derivation relies on a tree topology.

- **Evidence anchors reviewed:** datasets p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), metrics p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), baselines p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), results p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 8 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 9 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS), p. 10 (V. EXPERIMENTAL VALIDATION AND BENCHMARKS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** We evaluate the performance of differential IK solvers in a benchmark of inverse kinematics scenarios, which we plan to release as open source software after peer-review of this work 2. (p. 8, V. EXPERIMENTAL VALIDATION AND BENCHMARKS).
- **Metric evidence:** We evaluate the performance of differential IK solvers in a benchmark of inverse kinematics scenarios, which we plan to release as open source software after peer-review of this work 2. (p. 8, V. EXPERIMENTAL VALIDATION AND BENCHMARKS).
- **Baseline/ablation evidence:** Comparison to QP-based inverse kinematics With the parameters we have described, the benchmark produces 92,000 IK problems. (p. 9, V. EXPERIMENTAL VALIDATION AND BENCHMARKS).
- **Failure/negative evidence:** Limitations While we have assessed the effectiveness of LOIK over a wide range of robots, we note that, at present, its expressivity presents a couple of limitations. (p. 10, V. EXPERIMENTAL VALIDATION AND BENCHMARKS).
