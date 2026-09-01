# Evaluation - Push Anything: Single- and Multi-Object Pushing From First Sight with Contact-Implicit MPC

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2510.19974; PDF retrieval source: https://arxiv.org/pdf/2510.19974. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS), p. 2 (Figure/Table caption), p. 6 (V. HARDWARE EXPERIMENTS)): The system achieved a 99.9% success rate (700/701), with the only failure occurring when the large egg carton was pushed out of the robot's

## Evaluation Body Digest

- **p. 6 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** 8, we evaluated our method in 701 hardware trials, testing 25 objects, with each object run until 28 successful trials were obtained.
- **p. 7 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** All failures occurred when an object moved beyond the robot's reach.
- **p. 7 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** The few outliers for the chicken broth and milk bottle occurred when the robot took longer to bring the objects back into reach, while the ...
- **p. 6 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** The system achieved a 99.9% success rate (700/701), with the only failure occurring when the large egg carton was pushed out of the robot's
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2. System diagram of the Push Anything framework. ject-environment contacts (demonstrated with up to 19 contact pairs), while planning over a multi-step horizon to ...
- **p. 7 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** Under the tight tolerance, our method achieved a 92.5% success rate (210/227), with time-to-goal statistics for both tight and loose tolerances reported in Table II.
- **p. 7 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** The mean time-to-goal across all trials is approximately 31 s, evaluated under tight success criterion requiring translational error ≤2 cm and rotational error ≤0.1 rad ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 4. Visualization of the sampling strategy for end effector locations. The gray plane indicates the ground, and the orange planes represent local tangent planes ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** robot mechanism의 state와 task-space dynamics.
- **Input boundary:** joint/task state, reference와 sensor feedback.
- **Output/decision under evaluation:** torque, force, velocity 또는 position command.
- **Primary target:** tracking, stability, constraint satisfaction과 contact behavior.
- **Detected evaluation headings:** V. HARDWARE EXPERIMENTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| V. HARDWARE EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The system achieved a 99.9% success rate (700/701), with the only failure occurring when the large egg carton was pushed out of the robot's | p. 6 (V. HARDWARE EXPERIMENTS) |
| V. HARDWARE EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Under the tight tolerance, our method achieved a 92.5% success rate (210/227), with time-to-goal statistics for both tight and loose tolerances reported in Table ... | p. 7 (V. HARDWARE EXPERIMENTS) |
| V. HARDWARE EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Each experiment was run until 10 successful trials were achieved. | p. 7 (V. HARDWARE EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 2. System diagram of the Push Anything framework. ject-environment contacts (demonstrated with up to 19 contact pairs), while planning over a multi-step horizon ... | p. 2 (Figure/Table caption) |
| V. HARDWARE EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 7, this results in 16 contact pairs, yielding λ ∈R64. | p. 6 (V. HARDWARE EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** 8, we evaluated our method in 701 hardware trials, testing 25 objects, with each object run until 28 successful trials were obtained.
- **p. 7 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** All failures occurred when an object moved beyond the robot's reach.
- **p. 7 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** The few outliers for the chicken broth and milk bottle occurred when the robot took longer to bring the objects back into reach, while the ...
- **p. 6 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** The system achieved a 99.9% success rate (700/701), with the only failure occurring when the large egg carton was pushed out of the robot's

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1. Experimental Setup: The Franka Emika Panda arm uses a spherical end effector to push and rearrange four objects from an initial cluttered configuration. ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2. System diagram of the Push Anything framework. ject-environment contacts (demonstrated with up to 19 contact pairs), while planning over a multi-step horizon to ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 3. Illustration of sampling-based CI-MPC on the planar Push-T task [27]. Different end effector positions are shown with their associated MPC costs. The black ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 4. Visualization of the sampling strategy for end effector locations. The gray plane indicates the ground, and the orange planes represent local tangent planes ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 5. The C3+ projection step maps each point (λ◦, η◦) (blue) to its closest point (δλ k , δη k)∗(yellow) on the feasible complementarity ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 6. Diverse objects in Push Anything hardware experiments. object-wall object-ground object-object Nearest contact pairs: end effector-object
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 7. Visualization of the selected contact pairs in planar pushing task. yielding a significant overall speedup. As defined below and illustrated in Fig. 5, ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 8. Time-to-goal distributions for various objects. Boxplots show the median and interquartile range, while orange dots represent individual data points from each trial. For ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 8, we evaluated our method in 701 hardware trials, testing 25 objects, with each object run until 28 successful trials were obtained. | embodiment, simulator version and control stack | p. 6 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS) |
| Task/environment | All failures occurred when an object moved beyond the robot's reach. | reset, timeout, object/scene variation | p. 7 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS) |
| Observation/sensor | joint/task state, reference와 sensor feedback | calibration, preprocessing, privileged input | p. 4 (IV. METHODS), p. 3 (A. Hybrid Models for Contact Dynamics) |
| Output/decision | torque, force, velocity 또는 position command | action frame, controller and termination | p. 3 (A. Hybrid Models for Contact Dynamics), p. 4 (IV. METHODS) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 2. System diagram of the Push Anything framework. ject-environment contacts (demonstrated with up to 19 contact pairs), while planning over a multi-step horizon ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| The system achieved a 99.9% success rate (700/701), with the only failure occurring when the large egg carton was pushed out of the robot's | definition/direction/unit from same section | p. 6 (V. HARDWARE EXPERIMENTS) |
| Under the tight tolerance, our method achieved a 92.5% success rate (210/227), with time-to-goal statistics for both tight and loose tolerances reported in Table ... | definition/direction/unit from same section | p. 7 (V. HARDWARE EXPERIMENTS) |
| The mean time-to-goal across all trials is approximately 31 s, evaluated under tight success criterion requiring translational error ≤2 cm and rotational error ≤0.1 ... | definition/direction/unit from same section | p. 7 (V. HARDWARE EXPERIMENTS) |
| 8, we evaluated our method in 701 hardware trials, testing 25 objects, with each object run until 28 successful trials were obtained. | definition/direction/unit from same section | p. 6 (V. HARDWARE EXPERIMENTS) |
| Fig. 4. Visualization of the sampling strategy for end effector locations. The gray plane indicates the ground, and the orange planes represent local tangent ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 7. Visualization of the selected contact pairs in planar pushing task. yielding a significant overall speedup. As defined below and illustrated in Fig. ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For the Push T task, our framework achieves a mean time-to-goal of 26.9 s, improving upon prior work [4] at 30.5 s by 3.5 ... | comparison identity and matched condition | p. 7 (V. HARDWARE EXPERIMENTS) |
| Comparison of Solve Times for C3 and C3+ We benchmark our CI-MPC algorithm C3+ against its predecessor, C3 [1], to highlight its substantial speedup. ... | comparison identity and matched condition | p. 7 (V. HARDWARE EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 7. Visualization of the selected contact pairs in planar pushing task. yielding a significant overall speedup. As defined below and illustrated in Fig. ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce Push Anything, a manipulation pipeline for real-time planar pushing of a wide variety of objects, including multi-object scenes. | The system achieved a 99.9% success rate (700/701), with the only failure occurring when the large egg carton was pushed out of the robot's | PDF body cue; verify exact table/figure and matched conditions | p. 6 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS), p. 2 (Figure/Table caption), p. 6 (V. HARDWARE EXPERIMENTS) |
| Primary metric/result | Under the tight tolerance, our method achieved a 92.5% success rate (210/227), with time-to-goal statistics for both tight and loose tolerances reported in Table ... | numeric claim only at cited anchor | p. 7 (V. HARDWARE EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** We select a diverse set of 33 objects including convex and non-convex shapes, from 3Dprinted letters to household objects (Fig.
- **p. 6 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** 7), three contact pairs for each object with the ground (purple circles), one contact pair for each object with the wall (green arrow, omitted in ...
- **p. 6 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** 8, we evaluated our method in 701 hardware trials, testing 25 objects, with each object run until 28 successful trials were obtained.
- **p. 7 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** The mean time-to-goal across all trials is approximately 31 s, evaluated under tight success criterion requiring translational error ≤2 cm and rotational error ≤0.1 rad ...
- **p. 7 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** For the Push T task, our framework achieves a mean time-to-goal of 26.9 s, improving upon prior work [4] at 30.5 s by 3.5 s ...
- **p. 7 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** With these settings, we conducted a total of 227 trials, comprising 10 experiments for the 2-object case, 6 for the 3-object, and 5 for the ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Another limitation is we model all objects with identical mass and inertia. | p. 7 (VI. LIMITATIONS AND FUTURE WORK) |
| body limitation/failure cue | The system achieved a 99.9% success rate (700/701), with the only failure occurring when the large egg carton was pushed out of the robot's | p. 6 (V. HARDWARE EXPERIMENTS) |
| body limitation/failure cue | All failures occurred when an object moved beyond the robot's reach. | p. 7 (V. HARDWARE EXPERIMENTS) |
| body limitation/failure cue | We predefine contact geometries, but contact point pairs and their corresponding normals are determined dynamically via collision detection at each control loop. | p. 6 (V. HARDWARE EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 8, we evaluated our method in 701 hardware trials, testing 25 objects, with each object run until 28 successful trials were obtained. | p. 6 (V. HARDWARE EXPERIMENTS) |
| Each experiment was run until 10 successful trials were achieved. | p. 7 (V. HARDWARE EXPERIMENTS) |
| All computers communicate via LCM [37]. | p. 6 (V. HARDWARE EXPERIMENTS) |
| With these settings, we conducted a total of 227 trials, comprising 10 experiments for the 2-object case, 6 for the 3-object, and 5 for ... | p. 7 (V. HARDWARE EXPERIMENTS) |
| In the online phase, our controller uses robot and object state estimates to compute end effector trajectories. | p. 3 (IV. METHODS) |
| 2) Multi-Object Tracking: To track multiple objects, we run multiple instances of FoundationPose [31] in parallel, directly sharing memory access to the camera frames. | p. 3 (IV. METHODS) |
| To resolve this, we detect and correct sudden, implausibly large changes in orientation between consecutive timesteps by selecting the pose that maintains temporal consistency. | p. 4 (IV. METHODS) |
| (6) Here, zT = [zT 0 , zT 1 , ..., zT N-1], δT = [δT 0 , δT 1 , ..., δT N-1], ... | p. 4 (IV. METHODS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / VI. LIMITATIONS AND FUTURE WORK - extractive PDF cue:** Another limitation is we model all objects with identical mass and inertia.
- **p. 6 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** The system achieved a 99.9% success rate (700/701), with the only failure occurring when the large egg carton was pushed out of the robot's
- **p. 7 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** All failures occurred when an object moved beyond the robot's reach.
- **p. 6 / V. HARDWARE EXPERIMENTS - extractive PDF cue:** We predefine contact geometries, but contact point pairs and their corresponding normals are determined dynamically via collision detection at each control loop.

- **PDF anchors reviewed:** datasets p. 6 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS), p. 6 (V. HARDWARE EXPERIMENTS), metrics p. 2 (Figure/Table caption), p. 6 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS), p. 6 (V. HARDWARE EXPERIMENTS), p. 4 (Figure/Table caption), baselines p. 7 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS), results p. 6 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS), p. 7 (V. HARDWARE EXPERIMENTS), p. 2 (Figure/Table caption), p. 6 (V. HARDWARE EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
