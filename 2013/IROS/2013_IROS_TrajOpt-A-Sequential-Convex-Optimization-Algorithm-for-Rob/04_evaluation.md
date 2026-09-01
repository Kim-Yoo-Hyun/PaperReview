# Evaluation - TrajOpt: A Sequential Convex Optimization Algorithm for Robot Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1310.7730; PDF retrieval source: https://arxiv.org/pdf/1310.7730. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (V. MOTION PLANNING BENCHMARK), p. 13 (Figure/Table caption), p. 8 (V. MOTION PLANNING BENCHMARK), p. 9 (V. MOTION PLANNING BENCHMARK), p. 12 (Figure/Table caption)): Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and CHOMP.

## Evaluation Body Digest

- **p. 8 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Left and center: two of the scenes used for the arm planning benchmark.
- **p. 8 / V. MOTION PLANNING BENCHMARK - extractive body cue:** For each scene we set up the robot in a number of diverse configurations.
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** For collision checking, we took the convex hull of the geometry of each link of the robot, where each link is made of one or ...
- **p. 9 / VI. PHYSICAL EXPERIMENTS - extractive body cue:** The mesh is viewed as a soup of triangles (which are convex shapes), and we penalize collision between each triangle and the robot's links.
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and CHOMP.
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 13. Effect of noise level on the success rate. Re-planning after each time step greatly increases the probability of success. Collocation consistently outperforms shooting ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 11. Stop and turn strategy: Apply a rotation φt to the pose Xt at time step t and then propagate the frame by a ...
- **p. 8 / V. MOTION PLANNING BENCHMARK - extractive body cue:** We generated up to 5 initializations this way.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** graph, configuration space 또는 task-and-motion planning domain.
- **Input boundary:** start/goal, map, dynamics와 successor/operator description.
- **Output/decision under evaluation:** feasible action sequence 또는 minimum-cost plan.
- **Primary target:** path cost, goal reachability, feasibility와 computation.
- **Detected evaluation headings:** V. MOTION PLANNING BENCHMARK (p. 8); VI. PHYSICAL EXPERIMENTS (p. 9).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| V. MOTION PLANNING BENCHMARK | SYSTEM / EVALUATION SCOPE UNRESOLVED | Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and CHOMP. | p. 9 (V. MOTION PLANNING BENCHMARK) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Fig. 13. Effect of noise level on the success rate. Re-planning after each time step greatly increases the probability of success. Collocation consistently outperforms ... | p. 13 (Figure/Table caption) |
| V. MOTION PLANNING BENCHMARK | SYSTEM / EVALUATION SCOPE UNRESOLVED | Note that even though we initialize with tucked arms, the optimization typically untucks the arms to improve the cost. | p. 8 (V. MOTION PLANNING BENCHMARK) |
| V. MOTION PLANNING BENCHMARK | SYSTEM / EVALUATION SCOPE UNRESOLVED | TrajOpt with multiple initializations outperformed the other approaches in both sets of problems. | p. 9 (V. MOTION PLANNING BENCHMARK) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Fig. 12. Changing the value of the parameter αO influences the clearance of the trajectory from obstacles in the environment. Zoomed in view of ... | p. 12 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Left and center: two of the scenes used for the arm planning benchmark.
- **p. 8 / V. MOTION PLANNING BENCHMARK - extractive body cue:** For each scene we set up the robot in a number of diverse configurations.
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** For collision checking, we took the convex hull of the geometry of each link of the robot, where each link is made of one or ...
- **p. 9 / VI. PHYSICAL EXPERIMENTS - extractive body cue:** The mesh is viewed as a soup of triangles (which are convex shapes), and we penalize collision between each triangle and the robot's links.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. TrajOpt applied to several motion planning scenarios: (a) planning an arm trajectory for the PR2 in simulation, (b) PR2 opening a door with ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 2. Minimal translational distance and closest points. The convex-convex signed distance computation can be performed efficiently. The distance between two shapes can be calculated ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3. Hinge penalty for collisions a user-defined distance dcheck between them where dcheck > dsafe, and formulate the collision penalty based on these pairs. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. Illustration of the non-differentiability of the signed distance function. Here, a square is rotated about its center by angle θ. The true function ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. Illustration of swept volume for use in our continuous collision cost. Consider a moving object A and a static object B, for 0 ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6. Illustration of the difference between swept out shape and convex hull. The figure shows a triangle undergoing translation and uniform rotation. The swept-out ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7. Scenes in our benchmark tests. Left and center: two of the scenes used for the arm planning benchmark. Right: a third scene, showing ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 8. The Atlas humanoid robot in simulation walking across the room while avoiding the door frame and other obstacles in the environment, and pushing ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Left and center: two of the scenes used for the arm planning benchmark. | embodiment, simulator version and control stack | p. 8 (V. MOTION PLANNING BENCHMARK), p. 8 (V. MOTION PLANNING BENCHMARK) |
| Task/environment | For each scene we set up the robot in a number of diverse configurations. | reset, timeout, object/scene variation | p. 8 (V. MOTION PLANNING BENCHMARK), p. 9 (V. MOTION PLANNING BENCHMARK) |
| Observation/sensor | start/goal, map, dynamics와 successor/operator description | calibration, preprocessing, privileged input | p. 8 (V. MOTION PLANNING BENCHMARK), p. 1 (I. INTRODUCTION) |
| Output/decision | feasible action sequence 또는 minimum-cost plan | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and CHOMP. | definition/direction/unit from same section | p. 9 (V. MOTION PLANNING BENCHMARK) |
| Fig. 13. Effect of noise level on the success rate. Re-planning after each time step greatly increases the probability of success. Collocation consistently outperforms ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Fig. 11. Stop and turn strategy: Apply a rotation φt to the pose Xt at time step t and then propagate the frame by ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| We generated up to 5 initializations this way. | definition/direction/unit from same section | p. 8 (V. MOTION PLANNING BENCHMARK) |
| After finding a collision-free configuration W of this sort, we initialized with the trajectory SWG as described above. | definition/direction/unit from same section | p. 8 (V. MOTION PLANNING BENCHMARK) |
| We used the Bullet collision checker [7] for convex-convex collision queries. | definition/direction/unit from same section | p. 9 (V. MOTION PLANNING BENCHMARK) |
| Fig. 3. Hinge penalty for collisions a user-defined distance dcheck between them where dcheck > dsafe, and formulate the collision penalty based on these ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Fig. 4. Illustration of the non-differentiability of the signed distance function. Here, a square is rotated about its center by angle θ. The true ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We also compared TrajOpt to a recent implementation of CHOMP [61] on the arm planning problems. | comparison identity and matched condition | p. 8 (V. MOTION PLANNING BENCHMARK) |
| We compared TrajOpt to open-source implementations of bi-directional RRT [23] and a variant of KPIECE [46] from OMPL/MoveIt! | comparison identity and matched condition | p. 8 (V. MOTION PLANNING BENCHMARK) |
| TrajOpt with multiple initializations outperformed the other approaches in both sets of problems. | comparison identity and matched condition | p. 9 (V. MOTION PLANNING BENCHMARK) |
| We evaluated TrajOpt and compared it with other planners in terms of (1) average computation time for all successful planning runs computed over all ... | comparison identity and matched condition | p. 9 (V. MOTION PLANNING BENCHMARK) |
| Fig. 12. Changing the value of the parameter αO influences the clearance of the trajectory from obstacles in the environment. Zoomed in view of ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |
| Fig. 13. Effect of noise level on the success rate. Re-planning after each time step greatly increases the probability of success. Collocation consistently outperforms ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 13. Effect of noise level on the success rate. Re-planning after each time step greatly increases the probability of success. Collocation consistently outperforms ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| We compared TrajOpt to open-source implementations of bi-directional RRT [23] and a variant of KPIECE [46] from OMPL/MoveIt! | component/input/data sensitivity | p. 8 (V. MOTION PLANNING BENCHMARK) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method for handling collisions yields a polyhedral approximation of the free part of configuration space, which is directly incorporated into the convex optimization ... | Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and CHOMP. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (V. MOTION PLANNING BENCHMARK), p. 13 (Figure/Table caption), p. 8 (V. MOTION PLANNING BENCHMARK), p. 9 (V. MOTION PLANNING BENCHMARK), p. 12 (Figure/Table caption) |
| Primary metric/result | Fig. 13. Effect of noise level on the success rate. Re-planning after each time step greatly increases the probability of success. Collocation consistently outperforms ... | numeric claim only at cited anchor | p. 13 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** OMPL-RRTConnect OMPL-LBKPIECE CHOMP-HMC CHOMP-HMC-Multi TrajOpt TrajOpt-Multi success fraction 0.85 0.76 0.65 0.83 0.82 0.96 avg. time (s) 0.62 1.30 4.91 9.27 0.19 0.30 avg. norm ...
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** OMPL-RRTConnect OMPL-LBKPIECE TrajOpt TrajOpt-multi success fraction 0.41 0.51 0.73 0.88 avg. time (s) 20.3 18.7 2.2 6.1 avg. norm length 1.54 1.51 1.06 1.05 TABLE ...
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** OMPL-RRTConnect OMPL-LBKPIECE CHOMP-HMC CHOMP-HMC-Multi TrajOpt TrajOpt-Multi success fraction 0.85 0.76 0.65 0.83 0.82 0.96 avg. time (s) 0.62 1.30 4.91 9.27 0.19 0.30 avg. norm ...
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** OMPL-RRTConnect OMPL-LBKPIECE TrajOpt TrajOpt-multi success fraction 0.41 0.51 0.73 0.88 avg. time (s) 20.3 18.7 2.2 6.1 avg. norm length 1.54 1.51 1.06 1.05 TABLE ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 14. Failure cases when using TrajOpt. (a) shows the initial path for full-body planning. (b) is the trajectory optimization outcome, which is stuck ... | p. 14 (Figure/Table caption) |
| body limitation/failure cue | Fig. 5. Illustration of swept volume for use in our continuous collision cost. Consider a moving object A and a static object B, for ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Implementation details: Our current implementation of the continuous-time collision cost does not consider selfcollisions, but we penalized self-collisions at discrete times as described in ... | p. 9 (V. MOTION PLANNING BENCHMARK) |
| body limitation/failure cue | At the core of our approach is the use of sequential convex optimization with ℓ1 penalty terms for satisfying constraints, an efficient formulation of ... | p. 14 (XI. CONCLUSION) |
| body limitation/failure cue | Fig. 3. Hinge penalty for collisions a user-defined distance dcheck between them where dcheck > dsafe, and formulate the collision penalty based on these ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | After finding a collision-free configuration W of this sort, we initialized with the trajectory SWG as described above. | p. 8 (V. MOTION PLANNING BENCHMARK) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We used Khaled Mammou's implementation of HACD, which, in our experience, robustly produced good decompositions, even on the open meshes we generated from single ... | p. 9 (VI. PHYSICAL EXPERIMENTS) |
| In this work, we consider the trajectory optimization problem defined over the special Euclidean group SE(3), which is a 6D configuration space consisting of ... | p. 5 (A. Sequential Convex Optimization over SE(3)) |
| The local neighborhood X of a nominal pose ˆX ∈SE(3) is defined in terms of ¯x ∈R6 as X = ˆX · exp(¯x ∧), ... | p. 5 (A. Sequential Convex Optimization over SE(3)) |
| We ran all the experiments on a machine with an Intel i7 3.5 GHz CPU. | p. 8 (V. MOTION PLANNING BENCHMARK) |
| We also compared TrajOpt to a recent implementation of CHOMP [61] on the arm planning problems. | p. 8 (V. MOTION PLANNING BENCHMARK) |
| We used T = 11 timesteps for the arm and T = 41 timesteps for the full-body trajectories. | p. 9 (V. MOTION PLANNING BENCHMARK) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 14. Failure cases when using TrajOpt. (a) shows the initial path for full-body planning. (b) is the trajectory optimization outcome, which is stuck in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. Illustration of swept volume for use in our continuous collision cost. Consider a moving object A and a static object B, for 0 ...
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Implementation details: Our current implementation of the continuous-time collision cost does not consider selfcollisions, but we penalized self-collisions at discrete times as described in Sec.
- **p. 14 / XI. CONCLUSION - extractive body cue:** At the core of our approach is the use of sequential convex optimization with ℓ1 penalty terms for satisfying constraints, an efficient formulation of the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3. Hinge penalty for collisions a user-defined distance dcheck between them where dcheck > dsafe, and formulate the collision penalty based on these pairs. ...
- **p. 8 / V. MOTION PLANNING BENCHMARK - extractive body cue:** After finding a collision-free configuration W of this sort, we initialized with the trajectory SWG as described above.

- **PDF anchors reviewed:** datasets p. 8 (V. MOTION PLANNING BENCHMARK), p. 8 (V. MOTION PLANNING BENCHMARK), p. 9 (V. MOTION PLANNING BENCHMARK), p. 9 (VI. PHYSICAL EXPERIMENTS), metrics p. 9 (V. MOTION PLANNING BENCHMARK), p. 13 (Figure/Table caption), p. 11 (Figure/Table caption), p. 8 (V. MOTION PLANNING BENCHMARK), p. 8 (V. MOTION PLANNING BENCHMARK), p. 9 (V. MOTION PLANNING BENCHMARK), baselines p. 8 (V. MOTION PLANNING BENCHMARK), p. 8 (V. MOTION PLANNING BENCHMARK), p. 9 (V. MOTION PLANNING BENCHMARK), p. 9 (V. MOTION PLANNING BENCHMARK), p. 12 (Figure/Table caption), p. 13 (Figure/Table caption), results p. 9 (V. MOTION PLANNING BENCHMARK), p. 13 (Figure/Table caption), p. 8 (V. MOTION PLANNING BENCHMARK), p. 9 (V. MOTION PLANNING BENCHMARK), p. 12 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
