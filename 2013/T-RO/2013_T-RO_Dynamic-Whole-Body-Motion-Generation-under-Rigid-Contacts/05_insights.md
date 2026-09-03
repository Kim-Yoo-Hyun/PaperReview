# Insights — Dynamic Whole-Body Motion Generation under Rigid Contacts and Other Unilateral Constraints

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://hal.science/lirmm-00831097; PDF retrieval source: https://hal-lirmm.ccsd.cnrs.fr/file/index/docid/831097/filename/2013_itro_saab-Dynamic_Whole_Body_Motion_Generation.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 3 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a generic solution to take into account equalities and inequalities in a strict hierarchy to generate a dynamic motion.
- **p. 7 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** To cope with this problem we propose to include the contact forces f in the optimization variables of the QP resolution.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In total, the motion has to be designed in a set that lives in the high-dimensional configuration space but is implicitly limited to a much ...
- **p. 7 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Including the contact forces within the QP Solver Condition (32) must now be introduced in the HQP proposed at the end of Section IV-B 1) ...
- **p. 8 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Opening to other classes of contacts The model (22)-(38) is built on the rigid point contact.
- **p. 8 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Finally, the complete HQP for n contacts and k tasks is written: (39) ≺(22.1) ≺(38.1) ≺... ≺(22.n) ≺(38.n) ≺ (14.1) ≺... ≺(14.k) ≺(40), with the ...
- **p. 9 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Submitted to IEEE Transaction on Robotics 8 of motion (22) [40].
- **Contribution anchor:** p. 3 (I. INTRODUCTION), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 2 (I. INTRODUCTION), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS)

### Strongest assumption and failure boundary

- **p. 2 / I. INTRODUCTION - extractive body cue:** However, inequality constraints cannot be taken into account explicitly.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The motion manifold cannot be sampled directly but by projection [10].
- **p. 3 / I. INTRODUCTION - extractive body cue:** In [36], a first solution to handle inequalities in the stack of tasks was proposed, but cannot set any inequality constraint on the contact forces.
- **p. 3 / I. INTRODUCTION - extractive body cue:** In [25], a method to extend the QP formulation to any number of priority levels is given.
- **p. 10 / VII. EXPERIMENTS - extractive body cue:** The simulator checks the collision, computes the acceleration from the collision set and the torque input using a linear solver and numerically integrates ¨q using ...
- **p. 12 / VII. EXPERIMENTS - extractive body cue:** To prevent a collision when grasping, an intermediate point is first reached, above the grasping position.
- **p. 12 / VII. EXPERIMENTS - extractive body cue:** In reaction, all the other aligned joints move to overrun the neck limitation (chest joint of course, but also hip and ankle joints).
- **Boundary to test:** The simulator checks the collision, computes the acceleration from the collision set and the torque input using a linear solver and numerically integrates ¨q using a classical Runge-Kutta of the fourth order.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In this paper, we propose a generic solution to take into account equalities and inequalities in a strict hierarchy to generate a dynamic motion. | p. 3 (I. INTRODUCTION), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS) |
| Reported outcome | To improve the naturalness of the motion, a task egaze defined by (50) is set to constrain the gaze toward the armrest to be grasped. | p. 12 (VII. EXPERIMENTS), p. 14 (VII. EXPERIMENTS) |
| Failure/limitation | The simulator checks the collision, computes the acceleration from the collision set and the torque input using a linear solver and numerically integrates ¨q using a classical Runge-Kutta of the fourth order. | p. 10 (VII. EXPERIMENTS), p. 12 (VII. EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Paper-specific interface:** Using this notation, the necessary and sufficient condition to ensure the contact stability (in the sense that the contact remains in the same phase of the complementary condition, i.e. no ... (p. 7, V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS).
- **Paper-specific mechanism:** In this paper, we propose a generic solution to take into account equalities and inequalities in a strict hierarchy to generate a dynamic motion. (p. 3, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is 2) Results: The experiment is summed up by Figures 3 to 6. (p. 11, VII. EXPERIMENTS); the relevant task/metric cue is However, this solution has the drawback that the servo is on the position variables, while, as explained in the previous section, the robustness mainly relies on the accuracy of the ... (p. 10, VII. EXPERIMENTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** In reaction, all the other aligned joints move to overrun the neck limitation (chest joint of course, but also hip and ankle joints). (p. 12, VII. EXPERIMENTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, whole-body control, rigid contact, hierarchical control`.
- **Reading predecessor in the generated track queue:** PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Hierarchical Quadratic Programming: Fast Online Humanoid-Robot Motion Generation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The simulator checks the collision, computes the acceleration from the collision set and the torque input using a linear solver and numerically integrates ¨q using a classical Runge-Kutta of the fourth order.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: Using this notation, the necessary and sufficient condition to ensure the contact stability (in the sense that the contact remains in the same phase of the complementary condition, i.e. no ... (p. 7, V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS); preserve the objective/update rule: Including the contact forces within the QP Solver Condition (32) must now be introduced in the HQP proposed at the end of Section IV-B 1) A first way of modeling ... (p. 7, V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS).
2. Use the paper-reported task/data/environment cue: The result of this simulation is a joint trajectory of the robot, that complies to the multi-body dynamics. (p. 10, VII. EXPERIMENTS).
3. Compare against the reported or matched baseline: All the joints are properly stopped at the limit, and can leave the neighborhood of the limit without being stuck as it may appear with some avoidance techniques. (p. 12, VII. EXPERIMENTS).
4. Report the body metric with its denominator and aggregation: However, this solution has the drawback that the servo is on the position variables, while, as explained in the previous section, the robustness mainly relies on the accuracy of the ... (p. 10, VII. EXPERIMENTS).
5. Re-run the reported ablation or stress/failure condition: All the joints are properly stopped at the limit, and can leave the neighborhood of the limit without being stuck as it may appear with some avoidance techniques. (p. 12, VII. EXPERIMENTS); if none is reported, design one around: In reaction, all the other aligned joints move to overrun the neck limitation (chest joint of course, but also hip and ankle joints). (p. 12, VII. EXPERIMENTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 3 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), match the reported outcome at p. 11 (VII. EXPERIMENTS), p. 14 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS), and measure the boundary at p. 12 (VII. EXPERIMENTS), p. 14 (VII. EXPERIMENTS).

## Falsifiable research question

Under the paper's stated interface (Using this notation, the necessary and sufficient condition to ensure the contact stability (in the sense that the contact remains in the ...), does the paper-specific mechanism (In this paper, we propose a generic solution to take into account equalities and inequalities in a strict hierarchy to generate a ...) retain the reported evaluation outcome (However, this solution has the drawback that the servo is on the position variables, while, as explained in ...) when tested against the paper's strongest explicit boundary (In reaction, all the other aligned joints move to overrun the neck limitation (chest joint of course, but ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (However, this solution has the drawback that the servo is on the position variables, while, as explained in ...) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (18 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** In this paper, we propose a generic solution to take into account equalities and inequalities in a strict hierarchy to generate a dynamic motion. (p. 3, I. INTRODUCTION).
- **Paper-supported outcome:** 2) Results: The experiment is summed up by Figures 3 to 6. (p. 11, VII. EXPERIMENTS).
- **Strongest explicit boundary:** In reaction, all the other aligned joints move to overrun the neck limitation (chest joint of course, but also hip and ankle joints). (p. 12, VII. EXPERIMENTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
