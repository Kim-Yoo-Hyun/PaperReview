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

- **Closed-loop position:** `proprioception, reference pose/motion, visual or language command → whole-body pose, balance/contact state와 skill/mode → joint/whole-body action, motion target 또는 task trajectory`.
- 이 논문의 재사용 가능한 지점은 It also eases the use of sensory feedback, since the sensory space is often a good task-space candidate [14], [15].를 Using this notation, the necessary and sufficient condition to ensure the contact stability (in the sense that the contact remains in the same phase of the complementary condition, i.e. no take off) ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 whole-body pose, balance/contact state와 skill/mode가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 The simulator checks the collision, computes the acceleration from the collision set and the torque input using a linear solver and numerically integrates ¨q using a classical Runge-Kutta of the fourth order.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In this paper, we propose a generic solution to take into account equalities and inequalities in a strict hierarchy to generate a dynamic motion.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `CORE` in `Planning and control`; tags: `Robotics, whole-body control, rigid contact, hierarchical control`.
- **Reading predecessor in the generated track queue:** PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Hierarchical Quadratic Programming: Fast Online Humanoid-Robot Motion Generation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** The simulator checks the collision, computes the acceleration from the collision set and the torque input using a linear solver and numerically integrates ¨q using a classical Runge-Kutta of the fourth order.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: The result of this simulation is a joint trajectory of the robot, that complies to the multi-body dynamics..
3. Compare against the body-reported baseline or a matched simpler baseline: All the joints are properly stopped at the limit, and can leave the neighborhood of the limit without being stuck as it may appear with some avoidance techniques..
4. Report the body metric and its denominator/aggregation: However, this solution has the drawback that the servo is on the position variables, while, as explained in the previous section, the robustness mainly relies on the accuracy of the force variables..
5. Re-run the body-reported ablation/failure condition: All the joints are properly stopped at the limit, and can leave the neighborhood of the limit without being stuck as it may appear with some avoidance techniques..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS); the primary result is directionally consistent at p. 12 (VII. EXPERIMENTS), p. 14 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 generic, solution, take mechanism이 All the joints are properly stopped at the limit, and can leave the neighborhood of the ... 대비 However, this solution has the drawback that the servo is on the position variables, while, as explained in ...을 개선하고, The simulator checks the collision, computes the acceleration from the collision set and the torque input ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
