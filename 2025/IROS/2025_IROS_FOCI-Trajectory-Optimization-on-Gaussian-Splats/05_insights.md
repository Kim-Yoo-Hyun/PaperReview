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

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Since each spline segment lies within the convex hull of its control points, it is enough to constrain the norm of the velocity and acceleration control points, to guarantee constraint satisfaction along ...를 In comparisons with similar methods (Table III, Figure 7) we are able to surpass the speed of traditional methods such as RRT* on large complex scenes, while having similar time performance to ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of control points.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper, we propose an algorithm that enables a robot to perform trajectory optimization directly on the 3D Gaussians.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Planning and control`; tags: `Gaussian Splatting`.
- **Reading predecessor in the generated track queue:** Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** end of this track queue (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of control points.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Environment Initial Guess Time Solve Time # of Gaussians Narrow Corridor 0.24s 0.47s 24k Pillars 0.25s 0.45s 49k Machine Hall 0.22s 2.12s 243k Stonehenge 0.55s 0.83s 138k TABLE II: Planning time for ....
3. Compare against the body-reported baseline or a matched simpler baseline: Fig. 5: Comparison of the solver's creation and runtime running on the CPU and GPU for 50k environmental Gaus- sians and one robot Gaussian. The "serial" method is on a single CPU ....
4. Report the body metric and its denominator/aggregation: As Figure 2b shows, the planning algorithm effectively leverages the asymmetry of ANYmal to pass through the narrow opening collision-free..
5. Re-run the body-reported ablation/failure condition: 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of control points..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD); the primary result is directionally consistent at p. 5 (A. Trajectory Evaluation), p. 3 (III. METHOD); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 algorithm, enables, robot mechanism이 Fig. 5: Comparison of the solver's creation and runtime running on the CPU and GPU for ... 대비 As Figure 2b shows, the planning algorithm effectively leverages the asymmetry of ANYmal to pass through the narrow ...을 개선하고, 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
