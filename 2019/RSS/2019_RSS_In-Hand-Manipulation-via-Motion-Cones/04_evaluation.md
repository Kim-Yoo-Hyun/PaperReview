# Evaluation - In-Hand Manipulation via Motion Cones

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1810.00219; PDF retrieval source: https://arxiv.org/pdf/1810.00219. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS)): Similar to [3], our planner finds a strategy to achieve the regrasp using only one pusher.

## Evaluation Body Digest

- **p. 8 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** 9: Simulation and experimental run for a pushing strategy to regrasp the aluminum object with low friction pushers.
- **p. 7 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** The initial pose of an object in the gripper is treated as [X, Z, θY ] = [0, 0, 0].
- **p. 7 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** We evaluate the performance of our planner with examples of a parallel-jaw gripper manipulating a variety of objects.
- **p. 8 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** 2 3) Manipulating a non-convex object: In this example, the goal is to regrasp a T-shaped object.
- **p. 7 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** We compare the performance in terms of planning time and the quality of the solutions.
- **p. 8 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** Similar to [3], our planner finds a strategy to achieve the regrasp using only one pusher.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: (top) Example friction cone and motion cone of an object moving in the vertical plane. The pusher can move the object along any ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Manipulating a T-shaped object in a parallel-jaw grasp by pushing it against features in the environment. The manipulation is shown from a side ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS | EMPIRICAL / SIMULATION | Similar to [3], our planner finds a strategy to achieve the regrasp using only one pusher. | p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS | EMPIRICAL / SIMULATION | We compare the performance in terms of planning time and the quality of the solutions. | p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS | EMPIRICAL / SIMULATION | We evaluate the performance of our planner with examples of a parallel-jaw gripper manipulating a variety of objects. | p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |

## Dataset / Benchmark Role

- **p. 8 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** 9: Simulation and experimental run for a pushing strategy to regrasp the aluminum object with low friction pushers.
- **p. 7 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** The initial pose of an object in the gripper is treated as [X, Z, θY ] = [0, 0, 0].
- **p. 7 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** We evaluate the performance of our planner with examples of a parallel-jaw gripper manipulating a variety of objects.
- **p. 8 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** 2 3) Manipulating a non-convex object: In this example, the goal is to regrasp a T-shaped object.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: (top) Example friction cone and motion cone of an object moving in the vertical plane. The pusher can move the object along any ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Manipulating a T-shaped object in a parallel-jaw grasp by pushing it against features in the environment. The manipulation is shown from a side ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: Pushing an object (a) on a horizontal surface, (b) on an inclined surface, (c) in a grasp in the gravity plane, and (d) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: To make a push inside the gravity-free motion cone stable in the gravity plane, the unit grasp wrench can be scaled such that ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: A depiction of the process for constructing a wrench-set ( ˜ Wc). The intersection of the limit surface with the sum of the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6: A graphical illustration for the construction of the motion cone ( ˜Vobj) from the wrench-set ( ˜ Wc). The motion cone is defined ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7: (top) The grasp-pusher configuration used for the experimental validation of the motion cone. (bottom) The analytically computed wrench cone ( ˜ Wc), motion ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 8: 2000 random prehensile pushes in the configuration shown in Fig. 7 are characterized by the slip observed at the pusher contact. The motion ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 9: Simulation and experimental run for a pushing strategy to regrasp the aluminum object with low friction pushers. | embodiment, simulator version and control stack | p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| Task/environment | The initial pose of an object in the gripper is treated as [X, Z, θY ] = [0, 0, 0]. | reset, timeout, object/scene variation | p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 1 (I. INTRODUCTION) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We compare the performance in terms of planning time and the quality of the solutions. | definition/direction/unit from same section | p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| We evaluate the performance of our planner with examples of a parallel-jaw gripper manipulating a variety of objects. | definition/direction/unit from same section | p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| 10: A pushing strategy for [X, Z, θY ] regrasp. | definition/direction/unit from same section | p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| Similar to [3], our planner finds a strategy to achieve the regrasp using only one pusher. | definition/direction/unit from same section | p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| Fig. 1: (top) Example friction cone and motion cone of an object moving in the vertical plane. The pusher can move the object along ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 2: Manipulating a T-shaped object in a parallel-jaw grasp by pushing it against features in the environment. The manipulation is shown from a ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| While there are no comparable available algorithms that can solve the type of regrasps we are interested in, we provide comparisons with our own ... | comparison identity and matched condition | p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| When we replace the pushers with high-friction pushers (pushers with rubber coating), the planner detects that the desired object twist lies inside the motion ... | component/input/data sensitivity | p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present three main contributions: • Mechanics of motion cones for planar tasks in the gravity plane. | Similar to [3], our planner finds a strategy to achieve the regrasp using only one pusher. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| Primary metric/result | We compare the performance in terms of planning time and the quality of the solutions. | numeric claim only at cited anchor | p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |

- Numeric sentences retained from the body:
- **p. 7 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** The planning times in Table II are the median times over 10 trials.
- **p. 8 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** Object Z Position (mm) -20 0 20 40 -40 Initial grasp Pushes 1 - 7 40 0 20 -20 Object X Position (mm) 40 0 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 4: To make a push inside the gravity-free motion cone stable in the gravity plane, the unit grasp wrench can be scaled such ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Fig. 8: 2000 random prehensile pushes in the configuration shown in Fig. 7 are characterized by the slip observed at the pusher contact. The ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | These include sampling with rejection by a feasibility check for stable pushing [3], and a complementarity formulation (MNCP) that allows both sticking and slipping ... | p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| body limitation/failure cue | We believe that the extension and application of motion cones to more general settings provides new opportunities for fast and robust manipulation through contact. | p. 8 (VIII. DISCUSSION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The planning times in Table II are the median times over 10 trials. | p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| All the computations are done in MATLAB R2017a on a computer with Intel Core i7 2.8 GHz processor. | p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| Snapshots of the experimental run are is shown in Fig. | p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| 9: Simulation and experimental run for a pushing strategy to regrasp the aluminum object with low friction pushers. | p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: To make a push inside the gravity-free motion cone stable in the gravity plane, the unit grasp wrench can be scaled such that ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 8: 2000 random prehensile pushes in the configuration shown in Fig. 7 are characterized by the slip observed at the pusher contact. The motion ...
- **p. 7 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** These include sampling with rejection by a feasibility check for stable pushing [3], and a complementarity formulation (MNCP) that allows both sticking and slipping at ...
- **p. 8 / VIII. DISCUSSION - extractive body cue:** We believe that the extension and application of motion cones to more general settings provides new opportunities for fast and robust manipulation through contact.

- **PDF anchors reviewed:** datasets p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), metrics p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption), baselines p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), results p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
