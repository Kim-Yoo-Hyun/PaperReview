# Insights — FOCI: Trajectory Optimization on Gaussian Splats

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2505.08510; PDF retrieval source: https://arxiv.org/pdf/2505.08510. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose an algorithm that enables a robot to perform trajectory optimization directly on the 3D Gaussians.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The contributions of this work are therefore summarized as follows: • A novel collision measure between Gaussian Splats based on the overlap integral between Gaussians. ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To overcome these challenges, we propose FOCI, a trajectory optimization algorithm that leverages the overlap integral - the spatial integral over the multiplication of two ...
- **p. 3 / III. METHOD - extractive body cue:** Our methodology can be split into three parts: 1) trajectory representation to create an initial spline, 2) collision measure and 3) optimization loop.
- **p. 6 / Method - extractive body cue:** Runtime We evaluate the performance of our method by comparing the runtimes of the Casadi optimization on a single CPU core, multiple CPU cores, and ...
- **p. 3 / III. METHOD - extractive body cue:** The spline can then be evaluated with x(s′) =  1 s′ s′2 s′3 1 6   1 4 1 0 -3 0 3 ...
- **p. 4 / III. METHOD - extractive body cue:** The optimization problem is then solved via the interior point method (IPOPT) [28] with the custom overlap integral functor.
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 6 (Method), p. 3 (III. METHOD)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** To overcome these challenges, we propose FOCI, a trajectory optimization algorithm that leverages the overlap integral - the spatial integral over the multiplication of two ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Although some steps have been taken in this direction [3], [4], [5], the huge number of Gaussians a scene can have, together with the specific ...
- **p. 7 / V. LIMITATIONS - extractive body cue:** 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of control points.
- **p. 7 / V. LIMITATIONS - extractive body cue:** This means that when computing the overlap integral over the environment, flat regions with text or patterns have a slightly higher collision cost than
- **p. 5 / A. Trajectory Evaluation - extractive body cue:** As Figure 2b shows, the planning algorithm effectively leverages the asymmetry of ANYmal to pass through the narrow opening collision-free.
- **p. 5 / A. Trajectory Evaluation - extractive body cue:** 2) General Trajectory Planning Through 3DGS: Figure 3 shows that we can plan collision-free trajectories through splats that were created directly from the real-world environments.
- **Boundary to test:** 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of control points.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper, we propose an algorithm that enables a robot to perform trajectory optimization directly on the 3D Gaussians. | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | Environment Initial Guess Time Solve Time # of Gaussians Narrow Corridor 0.24s 0.47s 24k Pillars 0.25s 0.45s 49k Machine Hall 0.22s 2.12s 243k Stonehenge 0.55s 0.83s 138k TABLE II: Planning time for ... | p. 5 (A. Trajectory Evaluation), p. 3 (III. METHOD) |
| Failure/limitation | 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of control points. | p. 7 (V. LIMITATIONS), p. 7 (V. LIMITATIONS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Since each spline segment lies within the convex hull of its control points, it is enough to constrain the norm of the velocity and acceleration control points, to guarantee constraint ... (p. 4, III. METHOD).
- **Paper-specific mechanism:** In this paper, we propose an algorithm that enables a robot to perform trajectory optimization directly on the 3D Gaussians. (p. 1, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Environment Initial Guess Time Solve Time # of Gaussians Narrow Corridor 0.24s 0.47s 24k Pillars 0.25s 0.45s 49k Machine Hall 0.22s 2.12s 243k Stonehenge 0.55s 0.83s 138k TABLE II: Planning ... (p. 5, A. Trajectory Evaluation); the relevant task/metric cue is The algorithm gracefully handles trajectories requiring additional turns while adapting the orientation to keep a maximum distance from the wall. (p. 5, A. Trajectory Evaluation). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of control points. (p. 7, V. LIMITATIONS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Gaussian Splatting`.
- **Reading predecessor in the generated track queue:** Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** end of this track queue (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of control points.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Since each spline segment lies within the convex hull of its control points, it is enough to constrain the norm of the velocity and acceleration control points, to guarantee constraint ... (p. 4, III. METHOD); preserve the objective/update rule: 3) It should be differentiable to allow for gradient evaluations in optimization. (p. 3, III. METHOD).
2. Use the paper-reported task/data/environment cue: Environment Initial Guess Time Solve Time # of Gaussians Narrow Corridor 0.24s 0.47s 24k Pillars 0.25s 0.45s 49k Machine Hall 0.22s 2.12s 243k Stonehenge 0.55s 0.83s 138k TABLE II: Planning ... (p. 5, A. Trajectory Evaluation).
3. Compare against the reported or matched baseline: Fig. 5: Comparison of the solver's creation and runtime running on the CPU and GPU for 50k environmental Gaus- sians and one robot Gaussian. The "serial" method is on a ... (p. 7, Figure/Table caption).
4. Report the body metric with its denominator and aggregation: The algorithm gracefully handles trajectories requiring additional turns while adapting the orientation to keep a maximum distance from the wall. (p. 5, A. Trajectory Evaluation).
5. Re-run the reported ablation or stress/failure condition: PDF body did not yield a recoverable ablation/stress condition; no ablation inferred; if none is reported, design one around: 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of control points. (p. 7, V. LIMITATIONS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 5 (A. Trajectory Evaluation), p. 5 (A. Trajectory Evaluation), p. 5 (A. Trajectory Evaluation), and measure the boundary at p. 7 (V. LIMITATIONS), p. 7 (V. LIMITATIONS).

## Falsifiable research question

Under the paper's stated interface (Since each spline segment lies within the convex hull of its control points, it is enough to constrain the norm of the ...), does the paper-specific mechanism (In this paper, we propose an algorithm that enables a robot to perform trajectory optimization directly on the 3D Gaussians.) retain the reported evaluation outcome (The algorithm gracefully handles trajectories requiring additional turns while adapting the orientation to keep a maximum distance from ...) when tested against the paper's strongest explicit boundary (8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (The algorithm gracefully handles trajectories requiring additional turns while adapting the orientation to keep a maximum distance from ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this paper, we propose an algorithm that enables a robot to perform trajectory optimization directly on the 3D Gaussians. (p. 1, I. INTRODUCTION).
- **Paper-supported outcome:** Environment Initial Guess Time Solve Time # of Gaussians Narrow Corridor 0.24s 0.47s 24k Pillars 0.25s 0.45s 49k Machine Hall 0.22s 2.12s 243k Stonehenge 0.55s 0.83s 138k TABLE II: Planning ... (p. 5, A. Trajectory Evaluation).
- **Strongest explicit boundary:** 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of control points. (p. 7, V. LIMITATIONS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
