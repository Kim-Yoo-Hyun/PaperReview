# Insights — MuJoCo: A Physics Engine for Model-Based Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/IROS.2012.6386109; PDF retrieval source: https://doi.org/10.1109/IROS.2012.6386109. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** This is useful for approximating derivatives via finite differencing, which in turn enables numerical optimization. • Inverse dynamics can always be computed, even in the ...
- **p. 2 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** The procedure for solving the above equations of motion consists of the following steps:
- **p. 6 / III. MODELING - extractive body cue:** A MuJoCo model consists of one or several kinematic trees, which can have f1oating bases including isolated objects.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Existing physics engines can be used to test controllers that are already designed.
- **p. 1 / I. INTRODUCTION - extractive body cue:** As Sims [7] pointed out, if the physics engine allows cheating the optimization algorithm will find a way to exploit it - and produce a ...
- **p. 7 / III. MODELING - extractive body cue:** The tendon path is the shortest path that passes through a sequence of specified sites or wraps around specified geoms. h) Actuator: Actuators have control ...
- **p. 2 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** We start with notation and smooth dynamics which are fairly standard, then explain the contact simulation algorithms in more detail, followed by computational complexity and ...
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 6 (III. MODELING), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 7 (III. MODELING)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However they lack the speed, accuracy and overall feature sets needed to automate the controller design process itself.
- **p. 1 / I. INTRODUCTION - extractive body cue:** What is less obvious however is that, in the context of control optimization, these requirements become so demanding that none of the existing physics engines ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Another issue with game engines lies in the contact dynamics, formulated as (approximations to) linear complementarity problems or LCPs [8].
- **p. 2 / I. INTRODUCTION - extractive body cue:** Section IV presents timing tests and comparisons to SD/FAST - which does not handle contacts, but is the best prior engine for multi-joint dynamics in ...
- **p. 3 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** 1) Compute the Cartesian positions and orientations of all rigid bodies (i.e. the forward kinematics), detect potential collisions (with some safety margin), and construct the ...
- **p. 3 / 5) Integrate numerically to obtain the next state - extractive body cue:** In the tangent plane we have vF parallel to fF ­ vFfF® ≤0 (5) °°fF°° ≤N The first line means that if there is slip ...
- **p. 4 / 5) Integrate numerically to obtain the next state - extractive body cue:** Since the underlying problem is NP-hard, the algorithm cannot always find the exact solution (which has 0 residual).
- **Boundary to test:** 1) Compute the Cartesian positions and orientations of all rigid bodies (i.e. the forward kinematics), detect potential collisions (with some safety margin), and construct the Jacobians .

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | This is useful for approximating derivatives via finite differencing, which in turn enables numerical optimization. • Inverse dynamics can always be computed, even in the presence of contacts and equality constraints. | p. 2 (I. INTRODUCTION), p. 2 (II. ALGORITHMIC FOUNDATIONS) |
| Reported outcome | Although this approach is a significant improvement over earlier spring-damper models of contact, it still requires manual tuning and small time steps. | p. 2 (I. INTRODUCTION), p. 4 (5) Integrate numerically to obtain the next state) |
| Failure/limitation | 1) Compute the Cartesian positions and orientations of all rigid bodies (i.e. the forward kinematics), detect potential collisions (with some safety margin), and construct the Jacobians . | p. 3 (II. ALGORITHMIC FOUNDATIONS), p. 3 (5) Integrate numerically to obtain the next state) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `simulated state, geometry, contact와 control input → dynamics/contact state 또는 learned simulator representation → simulation step, trajectory 또는 environment query`.
- 이 논문의 재사용 가능한 지점은 The tendon path is the shortest path that passes through a sequence of specified sites or wraps around specified geoms. h) Actuator: Actuators have control inputs, optional activation states (used to model ...를 These observations indicated that we need a new engine, representing the state in joint coordinates and simulating contacts in ways that are related to LCP but better.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 dynamics/contact state 또는 learned simulator representation가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 1) Compute the Cartesian positions and orientations of all rigid bodies (i.e. the forward kinematics), detect potential collisions (with some safety margin), and construct the Jacobians .에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: This is useful for approximating derivatives via finite differencing, which in turn enables numerical optimization. • Inverse dynamics can always be computed, even in the presence of contacts and equality constraints.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, simulation, Physics Engine, Control`.
- **Reading predecessor in the generated track queue:** TrajOpt: A Sequential Convex Optimization Algorithm for Robot Motion Planning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Information Theoretic MPC for Model-Based Reinforcement Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 1) Compute the Cartesian positions and orientations of all rigid bodies (i.e. the forward kinematics), detect potential collisions (with some safety margin), and construct the Jacobians .; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: It can be used to analyze data or to compute the torques that will cause a robot to follow a reference trajectory..
3. Compare against the body-reported baseline or a matched simpler baseline: Performance on smooth dynamics compared to SD/FAST We measured the speed of multi-joint dynamics simulation in the absence of contacts or equality constraints..
4. Report the body metric and its denominator/aggregation: Furthermore the pyramid approximation introduces errors..
5. Re-run the body-reported ablation/failure condition: It is needed for three reasons: is often singular; without the inverse cannot be defined (see below); one can enable contact interactions from a distance - which can be very useful in ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (III. MODELING), p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 2 (II. ALGORITHMIC FOUNDATIONS); the primary result is directionally consistent at p. 2 (I. INTRODUCTION), p. 4 (5) Integrate numerically to obtain the next state), p. 5 (5) Integrate numerically to obtain the next state); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 useful, approximating, derivatives mechanism이 Performance on smooth dynamics compared to SD/FAST We measured the speed of multi-joint dynamics simulation in ... 대비 Furthermore the pyramid approximation introduces errors.을 개선하고, 1) Compute the Cartesian positions and orientations of all rigid bodies (i.e. the forward kinematics), detect ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
