# Method - STOMP: Stochastic Trajectory Optimization for Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (6 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ICRA.2011.5980280; PDF retrieval source: https://whiteoak.umd.edu/roswiki/attachments/Papers%282f%29ICRA2011_Kalakrishnan/kalakrishnan_icra2011.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (III. THE STOMP ALGORITHM), p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM), p. 3 (IV. MOTION PLANNING FOR A ROBOT ARM)): Inspired by previous work in the probability matching literature [10] as well as recent work in the areas of path integral reinforcement learning [11], we propose an estimated gradient formulated ...

## Method Body Digest

- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** Inspired by previous work in the probability matching literature [10] as well as recent work in the areas of path integral reinforcement learning [11], we ...
- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** In order to keep the notation simple, we first derive the algorithm for a 1-dimensional trajectory; this naturally extends later to multiple dimensions.
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** 3) Torque costs: Given a suitable dynamics model of the robot, we can compute the feed-forward torque required at each joint to track the desired ...
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** 1) Obstacle costs: We use an obstacle cost function similar to that used in previous work on optimizationbased motion planning [9].
- **p. 3 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** In this section, we discuss the application of the stochastic trajectory optimization algorithm in Table I to the problem of motion planning of a high-dimensional ...
- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** We treat motion planning as an optimization problem, to search for a smooth trajectory that minimizes costs corresponding to collisions and constraints.
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** We address the design of a cost function that allows planning for obstacle avoidance, optimization of task constraints, and minimization of joint torques.
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** Cost Function The cost function we use is comprised of obstacle costs qo, constraint costs qc, and torque costs qt. q(θ) = T X t=0 ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present a new approach to motion planning that can deal with general constraints.
- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** Inspired by previous work in the probability matching literature [10] as well as recent work in the areas of path integral reinforcement learning [11], we ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our approach involves stochastic trajectory optimization using a series of noisy trajectories.

## Source Evidence Cues

- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** Inspired by previous work in the probability matching literature [10] as well as recent work in the areas of path integral reinforcement learning [11], we ...
- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** In order to keep the notation simple, we first derive the algorithm for a 1-dimensional trajectory; this naturally extends later to multiple dimensions.
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** 3) Torque costs: Given a suitable dynamics model of the robot, we can compute the feed-forward torque required at each joint to track the desired ...
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** 1) Obstacle costs: We use an obstacle cost function similar to that used in previous work on optimizationbased motion planning [9].
- **p. 3 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** In this section, we discuss the application of the stochastic trajectory optimization algorithm in Table I to the problem of motion planning of a high-dimensional ...
- **Detected method headings:** III. THE STOMP ALGORITHM (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Problem / state representation | decision state와 feasible set을 만든다 | state, map, goal, constraints | source-specific graph, symbolic state, belief 또는 configuration representation을 구성 | search/optimization state | Inspired by previous work in the probability matching literature [10] as well as recent work in the areas of path integral reinforcement ... | p. 2 (III. THE STOMP ALGORITHM), p. 2 (III. THE STOMP ALGORITHM) |
| Search / trajectory decision | goal을 향한 candidate를 생성·개선한다 | state와 cost/heuristic | search, sampling, dynamic programming 또는 trajectory optimization을 적용 | plan, path, option 또는 trajectory | In order to keep the notation simple, we first derive the algorithm for a 1-dimensional trajectory; this naturally extends later to multiple ... | p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM) |
| Execution interface | 계획을 실행 가능한 command로 변환한다 | plan과 current feedback | collision/contact/dynamics check, smoothing, replanning 또는 controller handoff를 수행 | waypoint, option, action 또는 reference | 3) Torque costs: Given a suitable dynamics model of the robot, we can compute the feed-forward torque required at each joint to ... | p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** We treat motion planning as an optimization problem, to search for a smooth trajectory that minimizes costs corresponding to collisions and constraints.
- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** Inspired by previous work in the probability matching literature [10] as well as recent work in the areas of path integral reinforcement learning [11], we ...
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** We address the design of a cost function that allows planning for obstacle avoidance, optimization of task constraints, and minimization of joint torques.
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** Cost Function The cost function we use is comprised of obstacle costs qo, constraint costs qc, and torque costs qt. q(θ) = T X t=0 ...
- **p. 3 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** In this section, we discuss the application of the stochastic trajectory optimization algorithm in Table I to the problem of motion planning of a high-dimensional ...
- **Formal bridge:** s/q -> a/ξ ∈ feasible decisions -> path/task cost or expected utility -> success/reachability and constraint satisfaction.
- **Equation/algorithm anchors:** p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM), p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Inspired, previous, probability, matching, literature, well, recent, areas, path, integral, reinforcement, learning, estimated, gradient | start/goal, map, dynamics와 successor/operator description | body cue; exact tensor/frame verify |
| State/latent | Inspired, previous, probability, matching, literature, well, recent, areas, path, integral | path, trajectory, symbolic state 또는 task-motion decision | body cue; notation verify |
| Action/output | present, motion, planning, deal, general, constraints, Inspired, previous, probability, matching | feasible action sequence 또는 minimum-cost plan | body cue; unit/decoder verify |
| Objective/constraint | treat, motion, planning, optimization, problem, search, smooth, trajectory, minimizes, costs | path/task cost or expected utility | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** Inspired by previous work in the probability matching literature [10] as well as recent work in the areas of path integral reinforcement learning [11], we ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Domestic and retail scenarios, in particular, will have lots of cases where constraint satisfaction may be a prime goal, e.g. carrying a glass of water.
- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** We start with the following optimization problem: min ˜θ E " N X i=1 q( ˜θi) + 1 2 ˜θ TR˜θ # (1) where ˜θ ...
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** The motor torques at every instant of time are a function of the joint states and their derivatives: τ t = f(xt, ˙xt, ¨xt), (15) ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Motion planning for avoiding collision has been the most common goal, but there are other objectives like constraint handling, torque or energy minimization and achieving ...
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** We assume that the start and goal configurations are provided in joint space.
- **Normalized interface:** observation=start/goal, map, dynamics와 successor/operator description; state=path, trajectory, symbolic state 또는 task-motion decision; output/action=feasible action sequence 또는 minimum-cost plan.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | start/goal 또는 task sequence까지의 long-horizon plan; exact horizon은 paper-specific. | Thus the stochastic gradient is now formulated as follows: δˆθG = Z exp  -1 λS(θ)  δθ d(δθ) (10) Even though ... | episode/sequence/action-chunk boundary |
| Rate / latency | query/event-driven planning 뒤 controller가 partial plan을 실행; numeric rate 확인 필요. | Each trajectory was 5 seconds long, discretized into 100 time-steps. | Hz/fps, inference time and control rate |
| Memory | graph/tree/roadmap/plan and current state; history size는 method-specific. | not recovered | window and reset |
| Compute | collision checking, search branching 또는 optimization iterations가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / V. EXPERIMENTS - extractive body cue:** In the constrained scenario, 93.3% of trials resulted in plans that were both collision-free and satisfied the task constraints.
- **p. 2 / III. THE STOMP ALGORITHM - extractive body cue:** Thus the stochastic gradient is now formulated as follows: δˆθG = Z exp  -1 λS(θ)  δθ d(δθ) (10) Even though our optimization procedure ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Inspired, previous, probability, matching, literature, well, recent, areas, path, integral, reinforcement, learning, estimated, gradient, formulated, follows, Essentially, equation, above, expectation.
- **Relevant PDF headings:** III. THE STOMP ALGORITHM (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Problem / state representation | We conduct experiments on a simulation of the Willow Garage PR2 robot in a simulated world, followed by a demonstration of performance ... | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Search / trajectory decision | (a) Plan obtained without torque minimization: arm is stretched. | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Execution interface | The execution times are comparable, even though CHOMP usually requires more iterations to achieve success. | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 5 / V. EXPERIMENTS - extractive body cue:** (a) Plan obtained without torque minimization: arm is stretched.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** The exploration noise magnitude for STOMP, and the gradient descent step size for CHOMP were both tuned to achieve good performance without instability.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. (a) The Willow Garage PR2 robot manipulating objects in a household environment. (b) Simulation of the PR2 robot avoiding a pole in a ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5. (a) Iterative evolution of trajectory costs for 10 trials of STOMP on a constrained planning task. (b) Feed-forward torques used in the planning ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. (a) The Willow Garage PR2 robot manipulating objects in a household environment. (b) Simulation of the PR2 robot avoiding a pole in a ...
- **p. 4 / IV. MOTION PLANNING FOR A ROBOT ARM - extractive body cue:** (c) Trajectory optimized by STOMP to avoid collision with the shelf, constrained to maintain the upright orientation of the gripper.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** STOMP produced a collision-free trajectory in all (a) (b) (c) Fig.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (III. THE STOMP ALGORITHM), p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM), p. 3 (IV. MOTION PLANNING FOR A ROBOT ARM), objective p. 2 (III. THE STOMP ALGORITHM), p. 2 (III. THE STOMP ALGORITHM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM), p. 4 (IV. MOTION PLANNING FOR A ROBOT ARM), p. 3 (IV. MOTION PLANNING FOR A ROBOT ARM), temporal p. 2 (III. THE STOMP ALGORITHM), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 1 (Abstract), p. 1 (II. RELATED WORK), p. 2 (III. THE STOMP ALGORITHM).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
