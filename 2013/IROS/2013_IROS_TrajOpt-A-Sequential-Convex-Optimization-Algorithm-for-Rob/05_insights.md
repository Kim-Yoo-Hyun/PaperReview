# Insights — TrajOpt: A Sequential Convex Optimization Algorithm for Robot Motion Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1310.7730; PDF retrieval source: https://arxiv.org/pdf/1310.7730. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our method for handling collisions yields a polyhedral approximation of the free part of configuration space, which is directly incorporated into the convex optimization problem ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The ability to add new constraints and costs to the optimization problem allows our approach to tackle a larger range of motion planning problems, including ...
- **p. 5 / A. Sequential Convex Optimization over SE(3) - extractive body cue:** In this work, at the ith iteration of SQP our trajectory consists of a sequence of nominal poses ˆ X (i) = { ˆX(i) 0 ...
- **p. 5 / A. Sequential Convex Optimization over SE(3) - extractive body cue:** This parametrization is provided by the Lie algebra se(3), which is defined as the tangent vector space at the identity of SE(3), and, informally, consists ...
- **p. 5 / A. Sequential Convex Optimization over SE(3) - extractive body cue:** This distortion can severely slow down an optimization algorithm, by reducing the neighborhood where local (first and second-order) approximations are good.
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** The termination conditions we used for the optimization were (i) maximum of 40 iterations, (ii) minimum merit function improvement ratio of 10-4, (iii) minimum trust ...
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and CHOMP.
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 5 (A. Sequential Convex Optimization over SE(3)), p. 5 (A. Sequential Convex Optimization over SE(3)), p. 5 (A. Sequential Convex Optimization over SE(3)), p. 9 (V. MOTION PLANNING BENCHMARK)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** Optimal planners such as RRT* [20] and discretization-based approaches [29, 28] are very promising but are currently computationally inefficient for solving high-dimensional motion planning problems.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, in addition to providing a revised and extended version of our work [43], (i) we describe an extension to the algorithm described ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** requires solving a non-convex, constrained optimization problem.
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 14. Failure cases when using TrajOpt. (a) shows the initial path for full-body planning. (b) is the trajectory optimization outcome, which is stuck in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. Illustration of swept volume for use in our continuous collision cost. Consider a moving object A and a static object B, for 0 ...
- **p. 9 / V. MOTION PLANNING BENCHMARK - extractive body cue:** Implementation details: Our current implementation of the continuous-time collision cost does not consider selfcollisions, but we penalized self-collisions at discrete times as described in Sec.
- **p. 14 / XI. CONCLUSION - extractive body cue:** At the core of our approach is the use of sequential convex optimization with ℓ1 penalty terms for satisfying constraints, an efficient formulation of the ...
- **Boundary to test:** Fig. 14. Failure cases when using TrajOpt. (a) shows the initial path for full-body planning. (b) is the trajectory optimization outcome, which is stuck in an infeasible condition. (c) shows the initial ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our method for handling collisions yields a polyhedral approximation of the free part of configuration space, which is directly incorporated into the convex optimization problem that is solved at each optimization iteration. | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and CHOMP. | p. 9 (V. MOTION PLANNING BENCHMARK), p. 13 (Figure/Table caption) |
| Failure/limitation | Fig. 14. Failure cases when using TrajOpt. (a) shows the initial path for full-body planning. (b) is the trajectory optimization outcome, which is stuck in an infeasible condition. (c) shows the initial ... | p. 14 (Figure/Table caption), p. 7 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `start/goal, map, dynamics와 successor/operator description → path, trajectory, symbolic state 또는 task-motion decision → feasible action sequence 또는 minimum-cost plan`.
- 이 논문의 재사용 가능한 지점은 Let S and G denote the start and goal states for a planning problem.를 Trajectory optimization is fundamental in optimal control where the objective is to solve for a trajectory encoded as a sequence of states and controls that optimizes a given objective subject to constraints ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 path, trajectory, symbolic state 또는 task-motion decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 14. Failure cases when using TrajOpt. (a) shows the initial path for full-body planning. (b) is the trajectory optimization outcome, which is stuck in an infeasible condition. (c) shows the initial ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our method for handling collisions yields a polyhedral approximation of the free part of configuration space, which is directly incorporated into the convex optimization problem that is solved at each optimization iteration.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, motion planning, trajectory optimization, collision avoidance`.
- **Reading predecessor in the generated track queue:** CHOMP: Gradient Optimization Techniques for Efficient Motion Planning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** MuJoCo: A Physics Engine for Model-Based Control (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 14. Failure cases when using TrajOpt. (a) shows the initial path for full-body planning. (b) is the trajectory optimization outcome, which is stuck in an infeasible condition. (c) shows the initial ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Left and center: two of the scenes used for the arm planning benchmark..
3. Compare against the body-reported baseline or a matched simpler baseline: We also compared TrajOpt to a recent implementation of CHOMP [61] on the arm planning problems..
4. Report the body metric and its denominator/aggregation: Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and CHOMP..
5. Re-run the body-reported ablation/failure condition: Fig. 13. Effect of noise level on the success rate. Re-planning after each time step greatly increases the probability of success. Collocation consistently outperforms shooting in terms of success rate for all ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 5 (A. Sequential Convex Optimization over SE(3)), p. 5 (A. Sequential Convex Optimization over SE(3)), p. 9 (V. MOTION PLANNING BENCHMARK); the primary result is directionally consistent at p. 9 (V. MOTION PLANNING BENCHMARK), p. 13 (Figure/Table caption), p. 8 (V. MOTION PLANNING BENCHMARK); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 handling, collisions, yields mechanism이 We also compared TrajOpt to a recent implementation of CHOMP [61] on the arm planning problems. 대비 Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate ...을 개선하고, Fig. 14. Failure cases when using TrajOpt. (a) shows the initial path for full-body planning. (b) ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
