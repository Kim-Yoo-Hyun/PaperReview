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

- **Paper-specific interface:** Equations of motion and smooth dynamics We will use the following notation: q position in generalized coordinates v velocity in generalized coordinates  inertia matrix in generalized coordinates b "bias" ... (p. 2, II. ALGORITHMIC FOUNDATIONS).
- **Paper-specific mechanism:** This is useful for approximating derivatives via finite differencing, which in turn enables numerical optimization. • Inverse dynamics can always be computed, even in the presence of contacts and equality ... (p. 2, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is Table 3: This is the inverse of Table 2. Here we show the number of dynamics evaluations per second. The results are quite remarkable. One a single desktop machine, we ... (p. 8, Figure/Table caption); the relevant task/metric cue is Solving for the contact impulse We now return to step 4. (p. 3, 5) Integrate numerically to obtain the next state). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** In the absence of adequate tools, the field continues to rely on manual controller designs - which may be a large part of the reason why present-day robots do not ... (p. 1, I. INTRODUCTION).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, simulation, Physics Engine, Control`.
- **Reading predecessor in the generated track queue:** TrajOpt: A Sequential Convex Optimization Algorithm for Robot Motion Planning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Information Theoretic MPC for Model-Based Reinforcement Learning (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** 1) Compute the Cartesian positions and orientations of all rigid bodies (i.e. the forward kinematics), detect potential collisions (with some safety margin), and construct the Jacobians .; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Equations of motion and smooth dynamics We will use the following notation: q position in generalized coordinates v velocity in generalized coordinates  inertia matrix in generalized coordinates b "bias" ... (p. 2, II. ALGORITHMIC FOUNDATIONS); preserve the objective/update rule: Equations of motion and smooth dynamics We will use the following notation: q position in generalized coordinates v velocity in generalized coordinates  inertia matrix in generalized coordinates b "bias" ... (p. 2, II. ALGORITHMIC FOUNDATIONS).
2. Use the paper-reported task/data/environment cue: It can be used to analyze data or to compute the torques that will cause a robot to follow a reference trajectory. (p. 5, 5) Integrate numerically to obtain the next state).
3. Compare against the reported or matched baseline: Section IV presents timing tests and comparisons to SD/FAST - which does not handle contacts, but is the best prior engine for multi-joint dynamics in our opinion. (p. 2, I. INTRODUCTION).
4. Report the body metric with its denominator and aggregation: Solving for the contact impulse We now return to step 4. (p. 3, 5) Integrate numerically to obtain the next state).
5. Re-run the reported ablation or stress/failure condition: It is needed for three reasons: is often singular; without the inverse cannot be defined (see below); one can enable contact interactions from a distance - which can be very ... (p. 4, 5) Integrate numerically to obtain the next state); if none is reported, design one around: In the absence of adequate tools, the field continues to rely on manual controller designs - which may be a large part of the reason why present-day robots do not ... (p. 1, I. INTRODUCTION).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), match the reported outcome at p. 8 (Figure/Table caption), p. 5 (5) Integrate numerically to obtain the next state), p. 7 (IV. TIMING TESTS), and measure the boundary at p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION).

## Falsifiable research question

Under the paper's stated interface (Equations of motion and smooth dynamics We will use the following notation: q position in generalized coordinates v velocity in generalized coordinates ...), does the paper-specific mechanism (This is useful for approximating derivatives via finite differencing, which in turn enables numerical optimization. • Inverse dynamics can always be computed, ...) retain the reported evaluation outcome (Solving for the contact impulse We now return to step 4.) when tested against the paper's strongest explicit boundary (In the absence of adequate tools, the field continues to rely on manual controller designs - which may ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (Solving for the contact impulse We now return to step 4.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** This is useful for approximating derivatives via finite differencing, which in turn enables numerical optimization. • Inverse dynamics can always be computed, even in the presence of contacts and equality ... (p. 2, I. INTRODUCTION).
- **Paper-supported outcome:** Table 3: This is the inverse of Table 2. Here we show the number of dynamics evaluations per second. The results are quite remarkable. One a single desktop machine, we ... (p. 8, Figure/Table caption).
- **Strongest explicit boundary:** In the absence of adequate tools, the field continues to rely on manual controller designs - which may be a large part of the reason why present-day robots do not ... (p. 1, I. INTRODUCTION).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
