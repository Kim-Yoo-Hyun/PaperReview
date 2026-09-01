# Method - TrajOpt: A Sequential Convex Optimization Algorithm for Robot Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1310.7730; PDF retrieval source: https://arxiv.org/pdf/1310.7730. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (A. Sequential Convex Optimization over SE(3)), p. 5 (A. Sequential Convex Optimization over SE(3)), p. 9 (V. MOTION PLANNING BENCHMARK), p. 9 (V. MOTION PLANNING BENCHMARK), p. 8 (V. MOTION PLANNING BENCHMARK), p. 8 (V. MOTION PLANNING BENCHMARK)): This distortion can severely slow down an optimization algorithm, by reducing the neighborhood where local (first and second-order) approximations are good.

## Method Body Digest

- **p. 5 / A. Sequential Convex Optimization over SE(3) - extractive body cue:** This distortion can severely slow down an optimization algorithm, by reducing the neighborhood where local (first and second-order) approximations are good.
- **p. 5 / A. Sequential Convex Optimization over SE(3) - extractive body cue:** In this work, at the ith iteration of SQP our trajectory consists of a sequence of nominal poses ˆ X (i) = { ˆX(i) 0 ...
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** The termination conditions we used for the optimization were (i) maximum of 40 iterations, (ii) minimum merit function improvement ratio of 10-4, (iii) minimum trust ...
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and CHOMP.
- **p. 8 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Let S and G denote the start and goal states for a planning problem.
- **p. 8 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Right: a third scene, showing the path found by our planner on an 18-DOF full-body planning problem.
- **p. 8 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Note that even though we initialize with tucked arms, the optimization typically untucks the arms to improve the cost.
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Implementation details: Our current implementation of the continuous-time collision cost does not consider selfcollisions, but we penalized self-collisions at discrete times as described in Sec.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our method for handling collisions yields a polyhedral approximation of the free part of configuration space, which is directly incorporated into the convex optimization problem ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The ability to add new constraints and costs to the optimization problem allows our approach to tackle a larger range of motion planning problems, including ...
- **p. 5 / A. Sequential Convex Optimization over SE(3) - extractive body cue:** In this work, at the ith iteration of SQP our trajectory consists of a sequence of nominal poses ˆ X (i) = { ˆX(i) 0 ...

## Source Evidence Cues

- **p. 5 / A. Sequential Convex Optimization over SE(3) - extractive body cue:** This distortion can severely slow down an optimization algorithm, by reducing the neighborhood where local (first and second-order) approximations are good.
- **p. 5 / A. Sequential Convex Optimization over SE(3) - extractive body cue:** In this work, at the ith iteration of SQP our trajectory consists of a sequence of nominal poses ˆ X (i) = { ˆX(i) 0 ...
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** The termination conditions we used for the optimization were (i) maximum of 40 iterations, (ii) minimum merit function improvement ratio of 10-4, (iii) minimum trust ...
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and CHOMP.
- **p. 8 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Let S and G denote the start and goal states for a planning problem.
- **p. 8 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Right: a third scene, showing the path found by our planner on an 18-DOF full-body planning problem.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Problem / state representation | decision state와 feasible set을 만든다 | state, map, goal, constraints | source-specific graph, symbolic state, belief 또는 configuration representation을 구성 | search/optimization state | This distortion can severely slow down an optimization algorithm, by reducing the neighborhood where local (first and second-order) approximations are good. | p. 5 (A. Sequential Convex Optimization over SE(3)), p. 5 (A. Sequential Convex Optimization over SE(3)) |
| Search / trajectory decision | goal을 향한 candidate를 생성·개선한다 | state와 cost/heuristic | search, sampling, dynamic programming 또는 trajectory optimization을 적용 | plan, path, option 또는 trajectory | In this work, at the ith iteration of SQP our trajectory consists of a sequence of nominal poses ˆ X (i) = ... | p. 5 (A. Sequential Convex Optimization over SE(3)), p. 9 (V. MOTION PLANNING BENCHMARK) |
| Execution interface | 계획을 실행 가능한 command로 변환한다 | plan과 current feedback | collision/contact/dynamics check, smoothing, replanning 또는 controller handoff를 수행 | waypoint, option, action 또는 reference | The termination conditions we used for the optimization were (i) maximum of 40 iterations, (ii) minimum merit function improvement ratio of 10-4, ... | p. 9 (V. MOTION PLANNING BENCHMARK), p. 9 (V. MOTION PLANNING BENCHMARK) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 8 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Note that even though we initialize with tucked arms, the optimization typically untucks the arms to improve the cost.
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Implementation details: Our current implementation of the continuous-time collision cost does not consider selfcollisions, but we penalized self-collisions at discrete times as described in Sec.
- **p. 5 / A. Sequential Convex Optimization over SE(3) - extractive body cue:** The optimization method outlined above operates in vector spaces of the form Rn.
- **p. 5 / A. Sequential Convex Optimization over SE(3) - extractive body cue:** To perform local optimization over SE(3), we will need to form a local coordinate parametrization of the manifold.
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and CHOMP.
- **Formal bridge:** s/q -> a/ξ ∈ feasible decisions -> path/task cost or expected utility -> success/reachability and constraint satisfaction.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Let, denote, start, goal, states, planning, problem, Trajectory, optimization, fundamental, optimal, control, where, objective | start/goal, map, dynamics와 successor/operator description | body cue; exact tensor/frame verify |
| State/latent | Let, denote, start, goal, states, planning, problem, Trajectory, optimization, fundamental | path, trajectory, symbolic state 또는 task-motion decision | body cue; notation verify |
| Action/output | handling, collisions, yields, polyhedral, approximation, free, part, configuration, space, directly | feasible action sequence 또는 minimum-cost plan | body cue; unit/decoder verify |
| Objective/constraint | Note, even, though, initialize, tucked, arms, optimization, typically, untucks, improve | path/task cost or expected utility | equation anchor required |

## Observation–State–Action Interface

- **p. 8 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Let S and G denote the start and goal states for a planning problem.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Trajectory optimization is fundamental in optimal control where the objective is to solve for a trajectory encoded as a sequence of states and controls that ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** TrajOpt applied to several motion planning scenarios: (a) planning an arm trajectory for the PR2 in simulation, (b) PR2 opening a door with a full-body ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Overall, our experimental results indicate that TrajOpt was computationally faster than the alternatives on the considered benchmark (around 100 -200 ms on arm-planning problems and ...
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** OMPL-RRTConnect OMPL-LBKPIECE TrajOpt TrajOpt-multi success fraction 0.41 0.51 0.73 0.88 avg. time (s) 20.3 18.7 2.2 6.1 avg. norm length 1.54 1.51 1.06 1.05 TABLE ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 1(b)), and for planning foot placements with 28 DOF (+ 6 DOF pose) of the Atlas humanoid robot as it maintains static stability and avoids ...
- **p. 5 / A. Sequential Convex Optimization over SE(3) - extractive body cue:** (6) Intuitively, ¯r represents the incremental rotation and ¯p represents the incremental translation to be applied to a nominal pose.
- **Normalized interface:** observation=start/goal, map, dynamics와 successor/operator description; state=path, trajectory, symbolic state 또는 task-motion decision; output/action=feasible action sequence 또는 minimum-cost plan.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | start/goal 또는 task sequence까지의 long-horizon plan; exact horizon은 paper-specific. | In this work, we consider the trajectory optimization problem defined over the special Euclidean group SE(3), which is a 6D configuration space ... | episode/sequence/action-chunk boundary |
| Rate / latency | query/event-driven planning 뒤 controller가 partial plan을 실행; numeric rate 확인 필요. | At each time step t : 0 ≤t ≤T-1, we apply a rotation φt to the pose Xt and then propagate the ... | Hz/fps, inference time and control rate |
| Memory | graph/tree/roadmap/plan and current state; history size는 method-specific. | not recovered | window and reset |
| Compute | collision checking, search branching 또는 optimization iterations가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** distortion, severely, slow, down, optimization, algorithm, reducing, neighborhood, where, local, first, second-order, approximations, good, iteration, SQP, trajectory, consists, sequence, nominal.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Problem / state representation | Left and center: two of the scenes used for the arm planning benchmark. | p. 8 (V. MOTION PLANNING BENCHMARK), p. 8 (V. MOTION PLANNING BENCHMARK) |
| Search / trajectory decision | We also compared TrajOpt to a recent implementation of CHOMP [61] on the arm planning problems. | p. 8 (V. MOTION PLANNING BENCHMARK), p. 8 (V. MOTION PLANNING BENCHMARK) |
| Execution interface | Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and ... | p. 9 (V. MOTION PLANNING BENCHMARK), p. 13 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 13. Effect of noise level on the success rate. Re-planning after each time step greatly increases the probability of success. Collocation consistently outperforms shooting ...
- **p. 8 / V. MOTION PLANNING BENCHMARK - extractive body cue:** We compared TrajOpt to open-source implementations of bi-directional RRT [23] and a variant of KPIECE [46] from OMPL/MoveIt!
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 14. Failure cases when using TrajOpt. (a) shows the initial path for full-body planning. (b) is the trajectory optimization outcome, which is stuck in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. Illustration of swept volume for use in our continuous collision cost. Consider a moving object A and a static object B, for 0 ...
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Implementation details: Our current implementation of the continuous-time collision cost does not consider selfcollisions, but we penalized self-collisions at discrete times as described in Sec.
- **p. 14 / XI. CONCLUSION - extractive body cue:** At the core of our approach is the use of sequential convex optimization with ℓ1 penalty terms for satisfying constraints, an efficient formulation of the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3. Hinge penalty for collisions a user-defined distance dcheck between them where dcheck > dsafe, and formulate the collision penalty based on these pairs. ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (A. Sequential Convex Optimization over SE(3)), p. 5 (A. Sequential Convex Optimization over SE(3)), p. 9 (V. MOTION PLANNING BENCHMARK), p. 9 (V. MOTION PLANNING BENCHMARK), p. 8 (V. MOTION PLANNING BENCHMARK), p. 8 (V. MOTION PLANNING BENCHMARK), objective p. 8 (V. MOTION PLANNING BENCHMARK), p. 9 (V. MOTION PLANNING BENCHMARK), p. 5 (A. Sequential Convex Optimization over SE(3)), p. 5 (A. Sequential Convex Optimization over SE(3)), p. 9 (V. MOTION PLANNING BENCHMARK), temporal p. 5 (A. Sequential Convex Optimization over SE(3)), p. 11 (VIII. NEEDLE STEERING AND CHANNEL LAYOUT), p. 14 (X. SOURCE CODE AND REPRODUCIBILITY), p. 8 (3) Calculate the Jacobians of those points), p. 2 (I. INTRODUCTION), p. 5 (IV. NO-COLLISIONS CONSTRAINT).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
