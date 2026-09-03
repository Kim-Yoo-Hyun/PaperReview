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

- **Paper-specific interface:** 1(b)), and for planning foot placements with 28 DOF (+ 6 DOF pose) of the Atlas humanoid robot as it maintains static stability and avoids collisions (Fig. (p. 2, I. INTRODUCTION).
- **Paper-specific mechanism:** The ability to add new constraints and costs to the optimization problem allows our approach to tackle a larger range of motion planning problems, including planning for underactuated, nonholonomic systems. (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and CHOMP. (p. 9, V. MOTION PLANNING BENCHMARK); the relevant task/metric cue is Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and CHOMP. (p. 9, V. MOTION PLANNING BENCHMARK). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** The upshot is that the continuous collision cost solves problems with thin obstacles where the discrete-time cost fails to get the trajectory out of collision. (p. 8, 3) Calculate the Jacobians of those points).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, motion planning, trajectory optimization, collision avoidance`.
- **Reading predecessor in the generated track queue:** CHOMP: Gradient Optimization Techniques for Efficient Motion Planning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** MuJoCo: A Physics Engine for Model-Based Control (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 14. Failure cases when using TrajOpt. (a) shows the initial path for full-body planning. (b) is the trajectory optimization outcome, which is stuck in an infeasible condition. (c) shows the initial ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: 1(b)), and for planning foot placements with 28 DOF (+ 6 DOF pose) of the Atlas humanoid robot as it maintains static stability and avoids collisions (Fig. (p. 2, I. INTRODUCTION); preserve the objective/update rule: The optimization method outlined above operates in vector spaces of the form Rn. (p. 5, A. Sequential Convex Optimization over SE(3)).
2. Use the paper-reported task/data/environment cue: Left and center: two of the scenes used for the arm planning benchmark. (p. 8, V. MOTION PLANNING BENCHMARK).
3. Compare against the reported or matched baseline: We also compared TrajOpt to a recent implementation of CHOMP [61] on the arm planning problems. (p. 8, V. MOTION PLANNING BENCHMARK).
4. Report the body metric with its denominator and aggregation: Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and CHOMP. (p. 9, V. MOTION PLANNING BENCHMARK).
5. Re-run the reported ablation or stress/failure condition: We compared TrajOpt to open-source implementations of bi-directional RRT [23] and a variant of KPIECE [46] from OMPL/MoveIt! (p. 8, V. MOTION PLANNING BENCHMARK); if none is reported, design one around: The upshot is that the continuous collision cost solves problems with thin obstacles where the discrete-time cost fails to get the trajectory out of collision. (p. 8, 3) Calculate the Jacobians of those points).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 9 (V. MOTION PLANNING BENCHMARK), p. 8 (V. MOTION PLANNING BENCHMARK), p. 8 (V. MOTION PLANNING BENCHMARK), and measure the boundary at p. 8 (3) Calculate the Jacobians of those points), p. 14 (IX. IMPORTANCE OF TRAJECTORY INITIALIZATION).

## Falsifiable research question

Under the paper's stated interface (1(b)), and for planning foot placements with 28 DOF (+ 6 DOF pose) of the Atlas humanoid robot as it maintains static ...), does the paper-specific mechanism (The ability to add new constraints and costs to the optimization problem allows our approach to tackle a larger range of motion ...) retain the reported evaluation outcome (Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate ...) when tested against the paper's strongest explicit boundary (The upshot is that the continuous collision cost solves problems with thin obstacles where the discrete-time cost fails ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** The ability to add new constraints and costs to the optimization problem allows our approach to tackle a larger range of motion planning problems, including planning for underactuated, nonholonomic systems. (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** Multiple trajectory initializations are important to guide the optimization out of local minima and improves the success rate for both TrajOpt and CHOMP. (p. 9, V. MOTION PLANNING BENCHMARK).
- **Strongest explicit boundary:** The upshot is that the continuous collision cost solves problems with thin obstacles where the discrete-time cost fails to get the trajectory out of collision. (p. 8, 3) Calculate the Jacobians of those points).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
