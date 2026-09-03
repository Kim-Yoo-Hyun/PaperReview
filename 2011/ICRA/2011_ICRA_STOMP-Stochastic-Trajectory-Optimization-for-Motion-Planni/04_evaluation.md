# Evaluation - STOMP: Stochastic Trajectory Optimization for Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ICRA.2011.5980280; PDF retrieval source: https://whiteoak.umd.edu/roswiki/attachments/Papers%282f%29ICRA2011_Kalakrishnan/kalakrishnan_icra2011.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 1 (Figure/Table caption), p. 6 (Figure/Table caption)): The execution times are comparable, even though CHOMP usually requires more iterations to achieve success.

## Evaluation Body Digest

- **p. 5 / V. EXPERIMENTS - extractive body cue:** We conduct experiments on a simulation of the Willow Garage PR2 robot in a simulated world, followed by a demonstration of performance on the real ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Real Robot The attached video shows demonstrations of trajectories planned using STOMP in a household environment, executed 1This result was obtained using the standard CHOMP ...
- **p. 4 / V. EXPERIMENTS - extractive body cue:** STOMP is an algorithm that performs local optimization, i.e. it finds a locally optimum trajectory rather than a global one.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Success in this scenario implies the generation of a collision-free trajectory.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. (a) The Willow Garage PR2 robot manipulating objects in a household environment. (b) Simulation of the PR2 robot avoiding a pole in a ...
- **p. 4 / V. EXPERIMENTS - extractive body cue:** Hence, performance will vary depending on the initial
- **p. 5 / V. EXPERIMENTS - extractive body cue:** STOMP produced a collision-free trajectory in all (a) (b) (c) Fig.
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. (a) Each curve depicts a column/row of the symmetric matrix R-1. (b) 20 random samples of ϵ, drawn from a zero mean normal ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** graph, configuration space 또는 task-and-motion planning domain.
- **Input boundary:** start/goal, map, dynamics와 successor/operator description.
- **Output/decision under evaluation:** feasible action sequence 또는 minimum-cost plan.
- **Primary target:** path cost, goal reachability, feasibility와 computation.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The execution times are comparable, even though CHOMP usually requires more iterations to achieve success. | p. 5 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The exploration noise magnitude for STOMP, and the gradient descent step size for CHOMP were both tuned to achieve good performance without instability. | p. 5 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Hence, performance will vary depending on the initial | p. 4 (V. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1. (a) The Willow Garage PR2 robot manipulating objects in a household environment. (b) Simulation of the PR2 robot avoiding a pole in ... | p. 1 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 5. (a) Iterative evolution of trajectory costs for 10 trials of STOMP on a constrained planning task. (b) Feed-forward torques used in the ... | p. 6 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / V. EXPERIMENTS - extractive body cue:** We conduct experiments on a simulation of the Willow Garage PR2 robot in a simulated world, followed by a demonstration of performance on the real ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Real Robot The attached video shows demonstrations of trajectories planned using STOMP in a household environment, executed 1This result was obtained using the standard CHOMP ...
- **p. 4 / V. EXPERIMENTS - extractive body cue:** STOMP is an algorithm that performs local optimization, i.e. it finds a locally optimum trajectory rather than a global one.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. (a) The Willow Garage PR2 robot manipulating objects in a household environment. (b) Simulation of the PR2 robot avoiding a pole in a ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. (a) Each curve depicts a column/row of the symmetric matrix R-1. (b) 20 random samples of ϵ, drawn from a zero mean normal ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. (a) Simulation setup used to evaluate STOMP as a robot arm motion planner. (b) Initial straight-line trajectory between two shelves. (c) Trajectory optimized ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4. Planning problem used to evaluate torque minimization. (a) Plan obtained without torque minimization: arm is stretched. (b,c) Two different plans obtained with torque ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5. (a) Iterative evolution of trajectory costs for 10 trials of STOMP on a constrained planning task. (b) Feed-forward torques used in the planning ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We conduct experiments on a simulation of the Willow Garage PR2 robot in a simulated world, followed by a demonstration of performance on the ... | embodiment, simulator version and control stack | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Task/environment | Real Robot The attached video shows demonstrations of trajectories planned using STOMP in a household environment, executed 1This result was obtained using the standard ... | reset, timeout, object/scene variation | p. 5 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS) |
| Observation/sensor | start/goal, map, dynamics와 successor/operator description | calibration, preprocessing, privileged input | p. 2 (III. THE STOMP ALGORITHM), p. 1 (I. INTRODUCTION) |
| Output/decision | feasible action sequence 또는 minimum-cost plan | action frame, controller and termination | p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Success in this scenario implies the generation of a collision-free trajectory. | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| Fig. 1. (a) The Willow Garage PR2 robot manipulating objects in a household environment. (b) Simulation of the PR2 robot avoiding a pole in ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Hence, performance will vary depending on the initial | definition/direction/unit from same section | p. 4 (V. EXPERIMENTS) |
| STOMP produced a collision-free trajectory in all (a) (b) (c) Fig. | definition/direction/unit from same section | p. 5 (V. EXPERIMENTS) |
| Fig. 2. (a) Each curve depicts a column/row of the symmetric matrix R-1. (b) 20 random samples of ϵ, drawn from a zero mean ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 3. (a) Simulation setup used to evaluate STOMP as a robot arm motion planner. (b) Initial straight-line trajectory between two shelves. (c) Trajectory ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| (a) Plan obtained without torque minimization: arm is stretched. | comparison identity and matched condition | p. 5 (V. EXPERIMENTS) |
| The exploration noise magnitude for STOMP, and the gradient descent step size for CHOMP were both tuned to achieve good performance without instability. | comparison identity and matched condition | p. 5 (V. EXPERIMENTS) |
| Fig. 1. (a) The Willow Garage PR2 robot manipulating objects in a household environment. (b) Simulation of the PR2 robot avoiding a pole in ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Fig. 5. (a) Iterative evolution of trajectory costs for 10 trials of STOMP on a constrained planning task. (b) Feed-forward torques used in the ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| (a) Plan obtained without torque minimization: arm is stretched. | component/input/data sensitivity | p. 5 (V. EXPERIMENTS) |
| The exploration noise magnitude for STOMP, and the gradient descent step size for CHOMP were both tuned to achieve good performance without instability. | component/input/data sensitivity | p. 5 (V. EXPERIMENTS) |
| Fig. 1. (a) The Willow Garage PR2 robot manipulating objects in a household environment. (b) Simulation of the PR2 robot avoiding a pole in ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Fig. 5. (a) Iterative evolution of trajectory costs for 10 trials of STOMP on a constrained planning task. (b) Feed-forward torques used in the ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we present a new approach to motion planning that can deal with general constraints. | The execution times are comparable, even though CHOMP usually requires more iterations to achieve success. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 1 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Primary metric/result | The exploration noise magnitude for STOMP, and the gradient descent step size for CHOMP were both tuned to achieve good performance without instability. | numeric claim only at cited anchor | p. 5 (V. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Scenario STOMP CHOMP STOMP Unconstrained Unconstrained Constrained Number of 210 / 210 149 / 210 196 / 210 successful plans Avg. planning time 0.88 ± ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Seven of these cabinets were reachable by the 7 degree-of-freedom right arm of the PR2.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** In order to test the part of the cost function that deals with minimization of torques, we ran 10 trials on the planning problem shown ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 1. (a) The Willow Garage PR2 robot manipulating objects in a household environment. (b) Simulation of the PR2 robot avoiding a pole in ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | (c) Trajectory optimized by STOMP to avoid collision with the shelf, constrained to maintain the upright orientation of the gripper. | p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM) |
| body limitation/failure cue | STOMP produced a collision-free trajectory in all (a) (b) (c) Fig. | p. 5 (V. EXPERIMENTS) |
| body limitation/failure cue | Success in this scenario implies the generation of a collision-free trajectory. | p. 5 (V. EXPERIMENTS) |
| body limitation/failure cue | An additional advantage is that no gradient step-size parameter is required; the only open parameter in this algorithm is the magnitude of the exploration ... | p. 3 (5) Update θ ←θ + δθ) |
| body limitation/failure cue | Additionally, since the convex combination of noise is smoothed through the M matrix, the resulting updated trajectory smoothly touches the joint limit as opposed ... | p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each trajectory was 5 seconds long, discretized into 100 time-steps. | p. 5 (V. EXPERIMENTS) |
| In the constrained scenario, 93.3% of trials resulted in plans that were both collision-free and satisfied the task constraints. | p. 5 (V. EXPERIMENTS) |
| In the case of the path integral stochastic optimal control formalism, these controls are computed for every state xti as δˆu = R p(x)δu ... | p. 2 (III. THE STOMP ALGORITHM) |
| Thus the stochastic gradient is now formulated as follows: δˆθG = Z exp  -1 λS(θ)  δθ d(δθ) (10) Even though our optimization ... | p. 2 (III. THE STOMP ALGORITHM) |
| (N -1), compute: [ ˜ δθ]i = PK k=1 P(˜θk,i)[ϵk]i 4) Compute δθ = M ˜ δθ | p. 3 (III. THE STOMP ALGORITHM) |
| Scaling this to multiple dimensions simply involves performing the sampling and update steps for each dimension independently in each iteration. | p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM) |
| The signed EDT d(x), computed throughout the voxel grid, provides information about the distance to the boundary of the closest obstacle, both inside and ... | p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. (a) The Willow Garage PR2 robot manipulating objects in a household environment. (b) Simulation of the PR2 robot avoiding a pole in a ...
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** (c) Trajectory optimized by STOMP to avoid collision with the shelf, constrained to maintain the upright orientation of the gripper.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** STOMP produced a collision-free trajectory in all (a) (b) (c) Fig.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Success in this scenario implies the generation of a collision-free trajectory.
- **p. 3 / 5) Update θ ←θ + δθ - extractive body cue:** An additional advantage is that no gradient step-size parameter is required; the only open parameter in this algorithm is the magnitude of the exploration noise.
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** Additionally, since the convex combination of noise is smoothed through the M matrix, the resulting updated trajectory smoothly touches the joint limit as opposed to ...

- **Evidence anchors reviewed:** datasets p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), metrics p. 5 (V. EXPERIMENTS), p. 1 (Figure/Table caption), p. 4 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), results p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 4 (V. EXPERIMENTS), p. 1 (Figure/Table caption), p. 6 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
