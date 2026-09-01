# Evaluation - Towards Tight Convex Relaxations for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p132.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p132.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 8 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS)): For both slider geometries, we achieve a success rate of 100%, that is, the rounding step is able to retrieve a feasible solution for all the generated problem instances.

## Evaluation Body Digest

- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** Execution on real hardware Finally, we demonstrate the feasibility of the obtained motion plans on a Kuka LBR iiwa 7 R800 7-DOF robotic arm, with ...
- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** For extra stability, we use a feedback controller to execute the plans on hardware, and employ a hybrid Model-Predictive Controller (MPC) commonly used for pushing ...
- **p. 8 / VIII. EXPERIMENTS - extractive body cue:** This section contains both numerical and hardware experiments.
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** Our method also guarantees that the trajectory stays collision-free between contacts, while the baseline can be seen to clip the corners of the slider.
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** Our method picks the shortest path around the object, while the baseline goes the longer way around twice, highlighting the fact that our method is ...
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** As our method is capable of global reasoning and does not rely on an initial guess, it has a much higher success rate compared to ...
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** For both slider geometries, we achieve a success rate of 100%, that is, the rounding step is able to retrieve a feasible solution for all ...
- **p. 8 / VIII. EXPERIMENTS - extractive body cue:** We show an example of a generated motion plan in Figure 4.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** VIII. EXPERIMENTS (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| VIII. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | For both slider geometries, we achieve a success rate of 100%, that is, the rounding step is able to retrieve a feasible solution for ... | p. 9 (VIII. EXPERIMENTS) |
| VIII. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | As our method is capable of global reasoning and does not rely on an initial guess, it has a much higher success rate compared ... | p. 9 (VIII. EXPERIMENTS) |
| VIII. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Planner performance We evaluate the global optimality of the motion planner by generating 100 motion plans for the two slider geometries, with random initial ... | p. 8 (VIII. EXPERIMENTS) |
| VIII. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We start by pointing out that the performance of the contactimplicit method in table III required significant tuning of the cost function and problem ... | p. 10 (VIII. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** Execution on real hardware Finally, we demonstrate the feasibility of the obtained motion plans on a Kuka LBR iiwa 7 R800 7-DOF robotic arm, with ...
- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** For extra stability, we use a feedback controller to execute the plans on hardware, and employ a hybrid Model-Predictive Controller (MPC) commonly used for pushing ...
- **p. 8 / VIII. EXPERIMENTS - extractive body cue:** This section contains both numerical and hardware experiments.
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** Our method also guarantees that the trajectory stays collision-free between contacts, while the baseline can be seen to clip the corners of the slider.
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** Our method picks the shortest path around the object, while the baseline goes the longer way around twice, highlighting the fact that our method is ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: The experimental planar pushing setup. A cylindrical finger is attached to a robotic arm that is pushing a T-shaped object on the table ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: a) The slider-pusher kinematic quantities. b) The contact point and the contact forces.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: a) An example of a configuration-space partitioning Q1, . . . , Q4 and the linear approximations ϕ1, . . . , ϕ4 ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 4: Our planner simultaneously reasons about both discrete mode switches and continuous motion. Here, an example of a planar pushing plan with multiple mode ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 5: Our method is able to generate close-to globally optimal plans for pushing tasks with collision-free motion planning between contact modes. Here, two different ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4. We choose the cost weights for contact modes to kpP = kpS = kvP = 10, kvS = 100, kf = 10, kT ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 6: A comparative example between our method and a contact-implicit method. Our method picks the shortest path around the object, while the baseline goes ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Execution on real hardware Finally, we demonstrate the feasibility of the obtained motion plans on a Kuka LBR iiwa 7 R800 7-DOF robotic arm, ... | embodiment, simulator version and control stack | p. 10 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS) |
| Task/environment | For extra stability, we use a feedback controller to execute the plans on hardware, and employ a hybrid Model-Predictive Controller (MPC) commonly used for ... | reset, timeout, object/scene variation | p. 10 (VIII. EXPERIMENTS), p. 8 (VIII. EXPERIMENTS) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 6 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 3 (III. PROBLEM STATEMENT) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| As our method is capable of global reasoning and does not rely on an initial guess, it has a much higher success rate compared ... | definition/direction/unit from same section | p. 9 (VIII. EXPERIMENTS) |
| For both slider geometries, we achieve a success rate of 100%, that is, the rounding step is able to retrieve a feasible solution for ... | definition/direction/unit from same section | p. 9 (VIII. EXPERIMENTS) |
| We show an example of a generated motion plan in Figure 4. | definition/direction/unit from same section | p. 8 (VIII. EXPERIMENTS) |
| For reference, both slider geometries have a maximum "radius" close to 0.25 meters, and the plans are generated within a box with sides 0.6 ... | definition/direction/unit from same section | p. 8 (VIII. EXPERIMENTS) |
| We find that the plans generated with these friction parameters often perform well open-loop. | definition/direction/unit from same section | p. 10 (VIII. EXPERIMENTS) |
| We start by pointing out that the performance of the contactimplicit method in table III required significant tuning of the cost function and problem ... | definition/direction/unit from same section | p. 10 (VIII. EXPERIMENTS) |
| Fig. 3: a) An example of a configuration-space partitioning Q1, . . . , Q4 and the linear approximations ϕ1, . . . , ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Comparison with contact-implicit trajectory optimization To compare our method with a state-of-the-art baseline for contact-rich planning, we select a direct, contact-implicit trajectory optimization method ... | comparison identity and matched condition | p. 9 (VIII. EXPERIMENTS) |
| As our method is capable of global reasoning and does not rely on an initial guess, it has a much higher success rate compared ... | comparison identity and matched condition | p. 9 (VIII. EXPERIMENTS) |
| The T-shaped slider has a significantly higher number of possible mode sequences and a more complex SDF compared to the box-shaped geometry, making it ... | comparison identity and matched condition | p. 10 (VIII. EXPERIMENTS) |
| Our method also provides a good metric for evaluating solution quality through the obtained upper bound on the optimality gap, unlike the baseline, where ... | comparison identity and matched condition | p. 10 (VIII. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This highlights a key advantage of our approach: by reasoning on a global level, our method (empirically) always finds a solution, without relying on ... | component/input/data sensitivity | p. 10 (VIII. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method approximates these bilinearities using a tight Semidefinite Programming (SDP) relaxation for each contact mode. | For both slider geometries, we achieve a success rate of 100%, that is, the rounding step is able to retrieve a feasible solution for ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 8 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS) |
| Primary metric/result | As our method is capable of global reasoning and does not rely on an initial guess, it has a much higher success rate compared ... | numeric claim only at cited anchor | p. 9 (VIII. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 8 / VIII. EXPERIMENTS - extractive body cue:** For reference, both slider geometries have a maximum "radius" close to 0.25 meters, and the plans are generated within a box with sides 0.6 meters.
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** Slider SDP solve time Rounding time Optimality gap (δround) Box 7.05s (6.87s) 0.05s (0.05)s 8.33% (5.39%) Tee 83.61s (80.12) 0.36s (0.014s) s 10.41% (7.47%) TABLE ...
- **p. 6 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** The cost takes the following form: N-1 X k=0 L(xk, xk+1) + E(xk, xk+1, uk) + kfh∥fk∥2 2 + N X k=0 ψ(xk) (17) where ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Future work will explore the ability of these reduction methods to accelerate the planning. | p. 10 (IX. CONCLUSION AND FUTURE WORK) |
| body limitation/failure cue | Fig. 3: a) An example of a configuration-space partitioning Q1, . . . , Q4 and the linear approximations ϕ1, . . . , ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Fig. 5: Our method is able to generate close-to globally optimal plans for pushing tasks with collision-free motion planning between contact modes. Here, two ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Our method also guarantees that the trajectory stays collision-free between contacts, while the baseline can be seen to clip the corners of the slider. | p. 9 (VIII. EXPERIMENTS) |
| body limitation/failure cue | This limitation is not surprising, as the baseline is a local method that relies heavily on its initial guess. | p. 10 (VIII. EXPERIMENTS) |
| body limitation/failure cue | As our method is capable of global reasoning and does not rely on an initial guess, it has a much higher success rate compared ... | p. 9 (VIII. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| This section contains both numerical and hardware experiments. | p. 8 (VIII. EXPERIMENTS) |
| This method encodes contact modes implicitly using complementarity constraints that are relaxed and solves the problem as a sequence of NLPs with increasingly strict ... | p. 9 (VIII. EXPERIMENTS) |
| Execution on real hardware Finally, we demonstrate the feasibility of the obtained motion plans on a Kuka LBR iiwa 7 R800 7-DOF robotic arm, ... | p. 10 (VIII. EXPERIMENTS) |
| For extra stability, we use a feedback controller to execute the plans on hardware, and employ a hybrid Model-Predictive Controller (MPC) commonly used for ... | p. 10 (VIII. EXPERIMENTS) |
| Additionally, we decompose the collision-free subset of the configuration space into convex regions, which are also added to the graph to encode collision-free motion ... | p. 3 (IV. HIGH-LEVEL APPROACH) |
| Since the denominator is always positive, this function is a maximum over convex functions and is thus readily encoded through NF Rotated Second-Order Cone ... | p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING) |
| The vertices and edges of Gij are added to G, as well as a bi-directional edge connecting the vertices corresponding to contact modes Ci ... | p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / IX. CONCLUSION AND FUTURE WORK - extractive body cue:** Future work will explore the ability of these reduction methods to accelerate the planning.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: a) An example of a configuration-space partitioning Q1, . . . , Q4 and the linear approximations ϕ1, . . . , ϕ4 ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 5: Our method is able to generate close-to globally optimal plans for pushing tasks with collision-free motion planning between contact modes. Here, two different ...
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** Our method also guarantees that the trajectory stays collision-free between contacts, while the baseline can be seen to clip the corners of the slider.
- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** This limitation is not surprising, as the baseline is a local method that relies heavily on its initial guess.
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** As our method is capable of global reasoning and does not rely on an initial guess, it has a much higher success rate compared to ...

- **PDF anchors reviewed:** datasets p. 10 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), p. 8 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), metrics p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 8 (VIII. EXPERIMENTS), p. 8 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), baselines p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), results p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 8 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
