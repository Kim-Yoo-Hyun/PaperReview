# Insights — Towards Tight Convex Relaxations for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p132.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p132.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method approximates these bilinearities using a tight Semidefinite Programming (SDP) relaxation for each contact mode.
- **p. 1 / I. INTRODUCTION - extractive body cue:** As a first application for evaluating our method, this work explores the task of planar pushing, first studied by Mason in [2].
- **p. 2 / I. INTRODUCTION - extractive body cue:** of planar pushing, the technique we introduce generalizes naturally to more complex multi-contact problems.
- **p. 3 / IV. HIGH-LEVEL APPROACH - extractive body cue:** The second step in our method is to formulate the global motion planning problem as an SPP in a GCS [1].
- **p. 2 / III. PROBLEM STATEMENT - extractive body cue:** As a first application of our method, we explore planar pushing, a non-prehensile manipulation task where the robot uses a cylindrical finger to manipulate the ...
- **p. 7 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** A feasible path p through G then has the interpretation as a continuous trajectory from the initial state to the target state, that consists of ...
- **p. 3 / IV. HIGH-LEVEL APPROACH - extractive body cue:** The first step in formulating our motion planning method is to consider the dynamics and kinematics in a fixed contact mode.
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. HIGH-LEVEL APPROACH), p. 2 (III. PROBLEM STATEMENT), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING)

### Strongest assumption and failure boundary

- **p. 3 / V. BACKGROUND AND OPTIMIZATION TOOLS - extractive body cue:** The optimality gap δopt can then be overestimated as δopt = Cround -Copt Copt ≤Cround -Crelax Crelax = δrelax (2) Finally, we note that the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** It generally involves both a hybrid and underactuated dynamical system, making planning and control difficult.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We evaluate our motion planner through thorough numerical experiments, which show that the trajectories we generate typically have a very small optimality gap (10% on ...
- **p. 3 / V. BACKGROUND AND OPTIMIZATION TOOLS - extractive body cue:** Additionally, the GCS framework naturally gives us an upper bound on the optimality gap to a solution; Let Crelax ≤Copt ≤Cround be the costs of ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** of planar pushing, the technique we introduce generalizes naturally to more complex multi-contact problems.
- **p. 10 / IX. CONCLUSION AND FUTURE WORK - extractive body cue:** Future work will explore the ability of these reduction methods to accelerate the planning.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: a) An example of a configuration-space partitioning Q1, . . . , Q4 and the linear approximations ϕ1, . . . , ϕ4 ...
- **Boundary to test:** Future work will explore the ability of these reduction methods to accelerate the planning.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our method approximates these bilinearities using a tight Semidefinite Programming (SDP) relaxation for each contact mode. | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | For both slider geometries, we achieve a success rate of 100%, that is, the rounding step is able to retrieve a feasible solution for all the generated problem instances. | p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS) |
| Failure/limitation | Future work will explore the ability of these reduction methods to accelerate the planning. | p. 10 (IX. CONCLUSION AND FUTURE WORK), p. 6 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- 이 논문의 재사용 가능한 지점은 We represent a trajectory segment within each mode for the slider-pusher system by N discrete knot points for the state and N -1 knot points for the input: x0, x1, . . ...를 The point xv ∈Xv now corresponds to a trajectory of length N of states and inputs for the sliderpusher system in mode Ci.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 object geometry, affordance, contact mode 또는 end-effector state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Future work will explore the ability of these reduction methods to accelerate the planning.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our method approximates these bilinearities using a tight Semidefinite Programming (SDP) relaxation for each contact mode.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, contact-rich manipulation, convex relaxation, trajectory optimization`.
- **Reading predecessor in the generated track queue:** In-Hand Manipulation via Motion Cones (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Future work will explore the ability of these reduction methods to accelerate the planning.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Execution on real hardware Finally, we demonstrate the feasibility of the obtained motion plans on a Kuka LBR iiwa 7 R800 7-DOF robotic arm, with a T-shaped slider object..
3. Compare against the body-reported baseline or a matched simpler baseline: Comparison with contact-implicit trajectory optimization To compare our method with a state-of-the-art baseline for contact-rich planning, we select a direct, contact-implicit trajectory optimization method similar to those proposed in ....
4. Report the body metric and its denominator/aggregation: As our method is capable of global reasoning and does not rely on an initial guess, it has a much higher success rate compared to the baseline..
5. Re-run the body-reported ablation/failure condition: This highlights a key advantage of our approach: by reasoning on a global level, our method (empirically) always finds a solution, without relying on an initial guess..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 3 (IV. HIGH-LEVEL APPROACH), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING); the primary result is directionally consistent at p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 8 (VIII. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 approximates, bilinearities, tight mechanism이 Comparison with contact-implicit trajectory optimization To compare our method with a state-of-the-art baseline for contact-rich planning, ... 대비 As our method is capable of global reasoning and does not rely on an initial guess, it has ...을 개선하고, Future work will explore the ability of these reduction methods to accelerate the planning. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
