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

- **Paper-specific interface:** We assume isotropic Coulomb friction, i.e., that the coefficient of friction is constant, and the friction force at every contact point must have a constant magnitude and oppose the direction ... (p. 3, III. PROBLEM STATEMENT).
- **Paper-specific mechanism:** Our method approximates these bilinearities using a tight Semidefinite Programming (SDP) relaxation for each contact mode. (p. 1, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is As our method is capable of global reasoning and does not rely on an initial guess, it has a much higher success rate compared to the baseline. (p. 9, VIII. EXPERIMENTS); the relevant task/metric cue is For both slider geometries, we achieve a success rate of 100%, that is, the rounding step is able to retrieve a feasible solution for all the generated problem instances. (p. 9, VIII. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** In contrast, the baseline often fails, finding a solution in 58% of the instances for the box-shaped slider geometry and a mere 12% for the T-shaped slider. (p. 10, VIII. EXPERIMENTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, contact-rich manipulation, convex relaxation, trajectory optimization`.
- **Reading predecessor in the generated track queue:** In-Hand Manipulation via Motion Cones (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Future work will explore the ability of these reduction methods to accelerate the planning.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: We assume isotropic Coulomb friction, i.e., that the coefficient of friction is constant, and the friction force at every contact point must have a constant magnitude and oppose the direction ... (p. 3, III. PROBLEM STATEMENT); preserve the objective/update rule: In principle, this does not include all the tightening constraints (4d) and yields a potentially weaker convex relaxation, but in practice, we find that the loss in tightness is negligible ... (p. 7, VII. MOTION PLANNING FOR PLANAR PUSHING).
2. Use the paper-reported task/data/environment cue: Execution on real hardware Finally, we demonstrate the feasibility of the obtained motion plans on a Kuka LBR iiwa 7 R800 7-DOF robotic arm, with a T-shaped slider object. (p. 10, VIII. EXPERIMENTS).
3. Compare against the reported or matched baseline: Comparison with contact-implicit trajectory optimization To compare our method with a state-of-the-art baseline for contact-rich planning, we select a direct, contact-implicit trajectory optimization method similar to those proposed in ... (p. 9, VIII. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: For both slider geometries, we achieve a success rate of 100%, that is, the rounding step is able to retrieve a feasible solution for all the generated problem instances. (p. 9, VIII. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: This highlights a key advantage of our approach: by reasoning on a global level, our method (empirically) always finds a solution, without relying on an initial guess. (p. 10, VIII. EXPERIMENTS); if none is reported, design one around: In contrast, the baseline often fails, finding a solution in 58% of the instances for the box-shaped slider geometry and a mere 12% for the T-shaped slider. (p. 10, VIII. EXPERIMENTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), match the reported outcome at p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), and measure the boundary at p. 10 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS).

## Falsifiable research question

Under the paper's stated interface (We assume isotropic Coulomb friction, i.e., that the coefficient of friction is constant, and the friction force at every contact point must ...), does the paper-specific mechanism (Our method approximates these bilinearities using a tight Semidefinite Programming (SDP) relaxation for each contact mode.) retain the reported evaluation outcome (For both slider geometries, we achieve a success rate of 100%, that is, the rounding step is able ...) when tested against the paper's strongest explicit boundary (In contrast, the baseline often fails, finding a solution in 58% of the instances for the box-shaped slider ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (For both slider geometries, we achieve a success rate of 100%, that is, the rounding step is able ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** Our method approximates these bilinearities using a tight Semidefinite Programming (SDP) relaxation for each contact mode. (p. 1, I. INTRODUCTION).
- **Paper-supported outcome:** As our method is capable of global reasoning and does not rely on an initial guess, it has a much higher success rate compared to the baseline. (p. 9, VIII. EXPERIMENTS).
- **Strongest explicit boundary:** In contrast, the baseline often fails, finding a solution in 58% of the instances for the box-shaped slider geometry and a mere 12% for the T-shaped slider. (p. 10, VIII. EXPERIMENTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
