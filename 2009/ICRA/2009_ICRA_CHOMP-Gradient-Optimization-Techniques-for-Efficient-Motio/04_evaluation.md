# Evaluation - CHOMP: Gradient Optimization Techniques for Efficient Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ri.cmu.edu/publications/chomp-gradient-optimization-techniques-for-efficient-motion-planning/; PDF retrieval source: https://www.ri.cmu.edu/pub_files/2009/5/icra09-chomp.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT), p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT)): Surprisingly, when CHOMP successfully finds a collision free trajectory, straight-line 4We found that adding a small amount (.001) to the diagonal of A improved performance by avoiding situations where preferring ...

## Evaluation Body Digest

- **p. 5 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** We chose 15 different configurations in a given scene representing various tasks such as picking up an object 3The last degree of freedom simply rotates ...
- **p. 5 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** Section II-C discusses a heuristic based on the signed distance field under which the obstacles themselves specify how the robot should best remove itself from ...
- **p. 6 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** Left: This figure shows the joint angle traces that result from running CHOMP on the robot arm described in section III using the smooth projection ...
- **p. 6 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** For this implementation, we modeled each link of the robot arm as a straight line, which we subsequently discretized into 10 evenly spaced points to ...
- **p. 7 / IV. IMPLEMENTATION ON A QUADRUPED ROBOT - extractive body cue:** The Robotics Institute team has been quite competitive in phase II, the most recent phase of the Learning Locomotion project.
- **p. 7 / IV. IMPLEMENTATION ON A QUADRUPED ROBOT - extractive body cue:** Its effect in practice is to add a small gradient term that sends colliding points of the robot upwards regardless of the gradient of the ...
- **p. 7 / IV. IMPLEMENTATION ON A QUADRUPED ROBOT - extractive body cue:** Because the amount of rotation over a footstep is generally quite small (under 30◦), the error between the inner product on exponential map vectors and ...
- **p. 6 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** CHOMP successfully found collision-free trajectories for 99 of the 105 problem.4 We additionally compared the performance of CHOMP when initialized to a straight-line trajectory through ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** graph, configuration space 또는 task-and-motion planning domain.
- **Input boundary:** start/goal, map, dynamics와 successor/operator description.
- **Output/decision under evaluation:** feasible action sequence 또는 minimum-cost plan.
- **Primary target:** path cost, goal reachability, feasibility와 computation.
- **Detected evaluation headings:** III. EXPERIMENTS ON A ROBOTIC ARM (p. 5); IV. IMPLEMENTATION ON A QUADRUPED ROBOT (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| III. EXPERIMENTS ON A ROBOTIC ARM | EMPIRICAL / SOURCE-REPORTED EVALUATION | Surprisingly, when CHOMP successfully finds a collision free trajectory, straight-line 4We found that adding a small amount (.001) to the diagonal of A improved ... | p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| III. EXPERIMENTS ON A ROBOTIC ARM | EMPIRICAL / SOURCE-REPORTED EVALUATION | On average, excluding those problems that CHOMP could not solve, the log-objective value achieved when starting from a straight-line trajectory was approximately .5 units ... | p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| III. EXPERIMENTS ON A ROBOTIC ARM | EMPIRICAL / SOURCE-REPORTED EVALUATION | This section presents experimental results for our implementation of CHOMP on Barrett Technology's WAM arm shown in figure 1. | p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| III. EXPERIMENTS ON A ROBOTIC ARM | EMPIRICAL / SOURCE-REPORTED EVALUATION | Experimental results Our first experiment was designed to evaluate the efficacy of CHOMP and its probabilistic variants as a replacement for planning on a ... | p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| IV. IMPLEMENTATION ON A QUADRUPED ROBOT | EMPIRICAL / SOURCE-REPORTED EVALUATION | We have made no attempt to parallelize CHOMP in the current implementation, but we expect performance to scale nearly linearly with the number of ... | p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT) |

## Dataset / Benchmark Role

- **p. 5 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** We chose 15 different configurations in a given scene representing various tasks such as picking up an object 3The last degree of freedom simply rotates ...
- **p. 5 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** Section II-C discusses a heuristic based on the signed distance field under which the obstacles themselves specify how the robot should best remove itself from ...
- **p. 6 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** Left: This figure shows the joint angle traces that result from running CHOMP on the robot arm described in section III using the smooth projection ...
- **p. 6 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** For this implementation, we modeled each link of the robot arm as a straight line, which we subsequently discretized into 10 evenly spaced points to ...
- **p. 7 / IV. IMPLEMENTATION ON A QUADRUPED ROBOT - extractive body cue:** The Robotics Institute team has been quite competitive in phase II, the most recent phase of the Learning Locomotion project.
- **p. 7 / IV. IMPLEMENTATION ON A QUADRUPED ROBOT - extractive body cue:** Its effect in practice is to add a small gradient term that sends colliding points of the robot upwards regardless of the gradient of the ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Experimental robotic platforms: Boston Dynamics's LittleDog (left), and Barrett Technology's WAM arm (right). collision free. As a result, CHOMP can often transform a ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2. Potential function for obstacle avoidance A smoother version, shown in figure 2, is given by c(x) =    -d(x) + 1
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Left: A simple two-dimensional trajectory traveling through an obstacle potential (with large potentials are in red and small potentials in blue). The gradient ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Left: This figure shows the joint angle traces that result from running CHOMP on the robot arm described in section III using the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5. Left: the objective value per iteration of the first 100 iterations of CHOMP. Right: a comparison between the progression of objective values produced ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6. Left: the initial straight-line trajectory through configuration space. Middle: the final trajectory post optimization. Right: the 15 end point configurations used to create ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7. The LittleDog robot, designed and built by Boston Dynamics, Inc., along with sample terrains. Leftmost: Jersey barrier. Middle left: steps. Using CHOMP to ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We chose 15 different configurations in a given scene representing various tasks such as picking up an object 3The last degree of freedom simply ... | embodiment, simulator version and control stack | p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| Task/environment | Section II-C discusses a heuristic based on the signed distance field under which the obstacles themselves specify how the robot should best remove itself ... | reset, timeout, object/scene variation | p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| Observation/sensor | start/goal, map, dynamics와 successor/operator description | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Output/decision | feasible action sequence 또는 minimum-cost plan | action frame, controller and termination | p. 2 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Because the amount of rotation over a footstep is generally quite small (under 30◦), the error between the inner product on exponential map vectors ... | definition/direction/unit from same section | p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT) |
| CHOMP successfully found collision-free trajectories for 99 of the 105 problem.4 We additionally compared the performance of CHOMP when initialized to a straight-line trajectory ... | definition/direction/unit from same section | p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| Surprisingly, when CHOMP successfully finds a collision free trajectory, straight-line 4We found that adding a small amount (.001) to the diagonal of A improved ... | definition/direction/unit from same section | p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| Section II-C discusses a heuristic based on the signed distance field under which the obstacles themselves specify how the robot should best remove itself ... | definition/direction/unit from same section | p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| We avoid this behavior by adding an indicator function to the objective that makes all workspace terms that appear after the first collision along ... | definition/direction/unit from same section | p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| For the trunk trajectory, in addition to the workspace obstacle potential, the objective function includes terms which penalize kinematic reachability errors (which occur when ... | definition/direction/unit from same section | p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT) |
| Fig. 1. Experimental robotic platforms: Boston Dynamics's LittleDog (left), and Barrett Technology's WAM arm (right). collision free. As a result, CHOMP can often transform ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 7. The LittleDog robot, designed and built by Boston Dynamics, Inc., along with sample terrains. Leftmost: Jersey barrier. Middle left: steps. Using CHOMP ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| CHOMP successfully found collision-free trajectories for 99 of the 105 problem.4 We additionally compared the performance of CHOMP when initialized to a straight-line trajectory ... | comparison identity and matched condition | p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| Surprisingly, when CHOMP successfully finds a collision free trajectory, straight-line 4We found that adding a small amount (.001) to the diagonal of A improved ... | comparison identity and matched condition | p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| Fig. 1. Experimental robotic platforms: Boston Dynamics's LittleDog (left), and Barrett Technology's WAM arm (right). collision free. As a result, CHOMP can often transform ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 1. Experimental robotic platforms: Boston Dynamics's LittleDog (left), and Barrett Technology's WAM arm (right). collision free. As a result, CHOMP can often transform ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Experimental results Our first experiment was designed to evaluate the efficacy of CHOMP and its probabilistic variants as a replacement for planning on a ... | component/input/data sensitivity | p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| Section II-C discusses a heuristic based on the signed distance field under which the obstacles themselves specify how the robot should best remove itself ... | component/input/data sensitivity | p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| However, we made little effort to make our code efficient; we stress that our algorithm is performing essentially the same amount of work as ... | component/input/data sensitivity | p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| Without explicitly optimizing trajectory dynamics, the RRT returns a poor initial trajectory which causes CHOMP to quickly fall into a suboptimal local minimum. from ... | component/input/data sensitivity | p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| Fig. 3. Left: A simple two-dimensional trajectory traveling through an obstacle potential (with large potentials are in red and small potentials in blue). The ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we present Covariant Hamiltonian Optimization for Motion Planning (CHOMP), a novel method for generating and optimizing trajectories for robotic systems. | Surprisingly, when CHOMP successfully finds a collision free trajectory, straight-line 4We found that adding a small amount (.001) to the diagonal of A improved ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT), p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT) |
| Primary metric/result | On average, excluding those problems that CHOMP could not solve, the log-objective value achieved when starting from a straight-line trajectory was approximately .5 units ... | numeric claim only at cited anchor | p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |

- Numeric sentences retained from the body:
- **p. 7 / IV. IMPLEMENTATION ON A QUADRUPED ROBOT - extractive body cue:** Typical footstep durations run between 0.6 s and 1.2 s.
- **p. 7 / IV. IMPLEMENTATION ON A QUADRUPED ROBOT - extractive body cue:** We discretize the trajectories at the LittleDog host computer control cycle frequency, which is 100 Hz.
- **p. 7 / IV. IMPLEMENTATION ON A QUADRUPED ROBOT - extractive body cue:** Typical footstep durations run between 0.6 s and 1.2 s.
- **p. 7 / IV. IMPLEMENTATION ON A QUADRUPED ROBOT - extractive body cue:** We discretize the trajectories at the LittleDog host computer control cycle frequency, which is 100 Hz.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 1. Experimental robotic platforms: Boston Dynamics's LittleDog (left), and Barrett Technology's WAM arm (right). collision free. As a result, CHOMP can often transform ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Section II-C discusses a heuristic based on the signed distance field under which the obstacles themselves specify how the robot should best remove itself ... | p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| body limitation/failure cue | Intuitively, this heuristic suggests simply that the workspace gradients encountered after then first collision of a given configuration are invalid and should therefore be ... | p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| body limitation/failure cue | Without explicitly optimizing trajectory dynamics, the RRT returns a poor initial trajectory which causes CHOMP to quickly fall into a suboptimal local minimum. from ... | p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| body limitation/failure cue | CHOMP successfully found collision-free trajectories for 99 of the 105 problem.4 We additionally compared the performance of CHOMP when initialized to a straight-line trajectory ... | p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| body limitation/failure cue | The prior is defined as penalizing the distance below some known obstacle-free height when the swing leg is in collision with the terrain. | p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| This section presents experimental results for our implementation of CHOMP on Barrett Technology's WAM arm shown in figure 1. | p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| This indicator factor can be written mathematically as I(minj≤i d(xj(q)), although implementationally it is implemented simply by ignoring all terms after the first collision ... | p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| Footsteps for the LittleDog robot consist of a stance phase, where all four feet have ground contact, and a swing phase, where the swing ... | p. 6 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT) |
| For this implementation, we modeled each link of the robot arm as a straight line, which we subsequently discretized into 10 evenly spaced points ... | p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| Typical footstep durations run between 0.6 s and 1.2 s. | p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT) |
| Timing for the footstep is decided by a heuristic which is evaluated before the CHOMP algorithm is run. | p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT) |
| Gradient descent minimizes an uninformed, isotropic quadratic approximation while more sophisticated methods, like Newton steps, compute tighter lower bounds using a Hessian. | p. 3 (II. THE CHOMP ALGORITHM) |
| In practice, we discretize our trajectory into a set of n waypoints q1, . . . , qn (excluding the end points) and compute ... | p. 2 (II. THE CHOMP ALGORITHM) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Experimental robotic platforms: Boston Dynamics's LittleDog (left), and Barrett Technology's WAM arm (right). collision free. As a result, CHOMP can often transform a ...
- **p. 5 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** Section II-C discusses a heuristic based on the signed distance field under which the obstacles themselves specify how the robot should best remove itself from ...
- **p. 5 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** Intuitively, this heuristic suggests simply that the workspace gradients encountered after then first collision of a given configuration are invalid and should therefore be ignored.
- **p. 6 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** Without explicitly optimizing trajectory dynamics, the RRT returns a poor initial trajectory which causes CHOMP to quickly fall into a suboptimal local minimum. from the ...
- **p. 6 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** CHOMP successfully found collision-free trajectories for 99 of the 105 problem.4 We additionally compared the performance of CHOMP when initialized to a straight-line trajectory through ...
- **p. 7 / IV. IMPLEMENTATION ON A QUADRUPED ROBOT - extractive body cue:** The prior is defined as penalizing the distance below some known obstacle-free height when the swing leg is in collision with the terrain.

- **PDF anchors reviewed:** datasets p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT), p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT), metrics p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT), baselines p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 1 (Figure/Table caption), results p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT), p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
