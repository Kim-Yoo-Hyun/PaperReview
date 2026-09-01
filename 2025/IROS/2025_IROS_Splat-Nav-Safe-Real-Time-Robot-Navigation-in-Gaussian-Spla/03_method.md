# Method - Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2403.02751; PDF retrieval source: https://arxiv.org/pdf/2403.02751. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 7 (IV. PLANNING WITH SAFE POLYTOPES), p. 8 (IV. PLANNING WITH SAFE POLYTOPES), p. 8 (IV. PLANNING WITH SAFE POLYTOPES), p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 5 (IV. PLANNING WITH SAFE POLYTOPES)): We propose to solve maxs∈[0,1] K(s) using Algorithm 1.

## Method Body Digest

- **p. 6 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** We propose to solve maxs∈[0,1] K(s) using Algorithm 1.
- **p. 7 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** While there are many ways one could convert the ellipsoidal representation into a conservative occupancy grid, we propose the following method that is parallelizable and ...
- **p. 8 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** (7f) Without the dynamics constraints (7f), the optimization problem reduces to a quadratic program that can be solved in real-time, producing a trajectory that can ...
- **p. 8 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** 4) Spline Optimization: Given the safe flight corridor represented as P polytopes and initial and final configurations (x0, xf), we compute a set of P ...
- **p. 6 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** Algorithm 1: K(s) Bisection Search Input: number of iterations k; Output: maximal estimator ˆs; // Initialize lower and upper bounds sl ←0, sh ←1; for ...
- **p. 5 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** We leverage the ellipsoidal representations of the robot and the environment to derive an efficient collision-checking algorithm, based on [45], where we take advantage of ...
- **p. 7 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** The use of a uniform grid to run algorithms like Dijkstra Search are optimal and typically faster than those of random trees if there exists ...
- **p. 7 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** There are four primary components: (1) feasible path seeding through graph-based search, (2) construction of a collision set around each part of the path, (3) ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** The key contributions of this paper are as follows: • We develop a fast polytope corridor generation algorithm to enable provably safe planning for drone ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we introduce Splat-Nav, a pipeline for drone navigation in GSplat maps with a monocular camera.
- **p. 2 / I. INTRODUCTION - extractive body cue:** 1: Splat-Nav, consists of a safe planning module, Splat-Plan, and robust localization module, Splat-Loc, both operating on a Gaussian Splatting environment representation.

## Source Evidence Cues

- **p. 6 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** We propose to solve maxs∈[0,1] K(s) using Algorithm 1.
- **p. 7 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** While there are many ways one could convert the ellipsoidal representation into a conservative occupancy grid, we propose the following method that is parallelizable and ...
- **p. 8 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** (7f) Without the dynamics constraints (7f), the optimization problem reduces to a quadratic program that can be solved in real-time, producing a trajectory that can ...
- **p. 8 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** 4) Spline Optimization: Given the safe flight corridor represented as P polytopes and initial and final configurations (x0, xf), we compute a set of P ...
- **p. 6 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** Algorithm 1: K(s) Bisection Search Input: number of iterations k; Output: maximal estimator ˆs; // Initialize lower and upper bounds sl ←0, sh ←1; for ...
- **p. 5 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** We leverage the ellipsoidal representations of the robot and the environment to derive an efficient collision-checking algorithm, based on [45], where we take advantage of ...
- **p. 7 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** The use of a uniform grid to run algorithms like Dijkstra Search are optimal and typically faster than those of random trees if there exists ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | We propose to solve maxs∈[0,1] K(s) using Algorithm 1. | p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 7 (IV. PLANNING WITH SAFE POLYTOPES) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | While there are many ways one could convert the ellipsoidal representation into a conservative occupancy grid, we propose the following method that ... | p. 7 (IV. PLANNING WITH SAFE POLYTOPES), p. 8 (IV. PLANNING WITH SAFE POLYTOPES) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | (7f) Without the dynamics constraints (7f), the optimization problem reduces to a quadratic program that can be solved in real-time, producing a ... | p. 8 (IV. PLANNING WITH SAFE POLYTOPES), p. 8 (IV. PLANNING WITH SAFE POLYTOPES) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 8 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** 4) Spline Optimization: Given the safe flight corridor represented as P polytopes and initial and final configurations (x0, xf), we compute a set of P ...
- **p. 7 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** There are four primary components: (1) feasible path seeding through graph-based search, (2) construction of a collision set around each part of the path, (3) ...
- **p. 8 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** (7f) Without the dynamics constraints (7f), the optimization problem reduces to a quadratic program that can be solved in real-time, producing a trajectory that can ...
- **p. 6 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** Consequently, the max-min problem results is an inner minimization problem of a quadratic, which is solved in closed-form.
- **p. 6 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** The point-wise minimum of concave functions K(s, t∗(s)) is concave, hence the outer maximization is still over a concave function.
- **p. 7 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** By stacking the hyperplane constraints (aj, bj), we arrive at a polytope Ax ≥b that is guaranteed to be safe.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 7 (IV. PLANNING WITH SAFE POLYTOPES), p. 7 (IV. PLANNING WITH SAFE POLYTOPES), p. 8 (IV. PLANNING WITH SAFE POLYTOPES), p. 8 (IV. PLANNING WITH SAFE POLYTOPES), p. 6 (IV. PLANNING WITH SAFE POLYTOPES).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Algorithm, Bisection, Search, Input, number, iterations, Output, maximal, estimator, Initialize, lower, upper, bounds, Test | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Algorithm, Bisection, Search, Input, number, iterations, Output, maximal, estimator, Initialize | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | contributions, follows, develop, fast, polytope, corridor, generation, algorithm, enable, provably | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Spline, Optimization, Given, safe, flight, corridor, represented, polytopes, initial, final | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** Algorithm 1: K(s) Bisection Search Input: number of iterations k; Output: maximal estimator ˆs; // Initialize lower and upper bounds sl ←0, sh ←1; for ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Splat-Nav comprises a lightweight pose estimation module, Splat-Loc, coupled with a planning module, Splat-Plan, to enable safe navigation from RGB-only (monocular) camera observations, as illustrated ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Given an incoming RGB frame, Splat-Loc performs Perspective-n-Point (PnP)- based localization, leveraging the GSplat map to estimate the RGB and depth values rendered at candidate ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In Splat-Loc we localize the robot using only RGB images through a PnP algorithm, using the GSplat to render a point cloud.
- **p. 5 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** For completeness, we restate the collision-checking method from [45, Proposition 2].
- **p. 6 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** Sion's minimax theorem states that switching the order of the minimum and maximum yields identical solutions when K(s, t) is concave in s and convex ...
- **p. 9 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** For simplicity of notation, we will refer to the output of Splat-Plan as X(T), which takes in metric time, finds the associated spline Xp, and ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | We show online re-planning at more than 2 Hz and pose estimation at about 25 Hz, an order of magnitude faster than ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | At a frequency of about 3 Hz, the drone transmits images from its cameras and associated VIO poses to the desktop computer. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | We show online re-planning at more than 2 Hz and pose estimation at about 25 Hz, an order of magnitude faster than ... | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / IV. PLANNING WITH SAFE POLYTOPES - extractive body cue:** (7f) Without the dynamics constraints (7f), the optimization problem reduces to a quadratic program that can be solved in real-time, producing a trajectory that can ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** solve, maxs, Algorithm, While, there, many, ways, could, convert, ellipsoidal, representation, conservative, occupancy, grid, following, parallelizable, efficient, Section, Without, dynamics.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Simulation Results 1) Test Environments: We benchmark Splat-Plan and SplatLoc independently on four different environments: Stonehenge, a fully-synthetic scene, and three real-world ... | p. 10 (VI. EXPERIMENTS), p. 10 (VI. EXPERIMENTS) |
| Global / local decision | Furthermore, we perform ablations against variations of the point-cloud planner in order to expose flaws when planning against point clouds compared to ... | p. 11 (VI. EXPERIMENTS), p. 11 (VI. EXPERIMENTS) |
| Motion execution / recovery | However, Splat-Loc-SIFT achieves a lower success rate, compared to Splat-Loc-Glue, which achieves a perfect success rate. | p. 11 (VI. EXPERIMENTS), p. 13 (VI. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 11 / VI. EXPERIMENTS - extractive body cue:** Number of Gaussians is reported for both dense and sparse variants of the same scene.
- **p. 11 / VI. EXPERIMENTS - extractive body cue:** Furthermore, we perform ablations against variations of the point-cloud planner in order to expose flaws when planning against point clouds compared to the full scene ...
- **p. 12 / VI. EXPERIMENTS - extractive body cue:** To this end, we developed four variants of the Safe Flight Corridor (SFC) [13].
- **p. 12 / VI. EXPERIMENTS - extractive body cue:** These variants are all potential solutions to apply SFC to GSplat environments.
- **p. 13 / VI. EXPERIMENTS - extractive body cue:** Gaussian Splat for the location of these objects using the following text prompts: "keyboard," "beachball," "phonebook" and "microwave," corresponding to these objects, without negative prompts.
- **p. 13 / VI. EXPERIMENTS - extractive body cue:** 6) Splat-Loc Evaluations: We validate the performance of Splat-Loc in hardware experiments in the Maze scene, showing that Splat-Loc achieves relatively the same level of ...
- **p. 14 / VI. EXPERIMENTS - extractive body cue:** Meanwhile, Splat-Loc needed no such alignment, and was kept running continuously throughout all experiments without zero-ing (even

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 7 (IV. PLANNING WITH SAFE POLYTOPES), p. 8 (IV. PLANNING WITH SAFE POLYTOPES), p. 8 (IV. PLANNING WITH SAFE POLYTOPES), p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 5 (IV. PLANNING WITH SAFE POLYTOPES), objective p. 8 (IV. PLANNING WITH SAFE POLYTOPES), p. 7 (IV. PLANNING WITH SAFE POLYTOPES), p. 8 (IV. PLANNING WITH SAFE POLYTOPES), p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 7 (IV. PLANNING WITH SAFE POLYTOPES), temporal p. 1 (Abstract), p. 12 (VI. EXPERIMENTS), p. 15 (VII. CONCLUSION), p. 9 (V. MONOCULAR POSE ESTIMATION), p. 10 (VI. EXPERIMENTS), p. 11 (VI. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
