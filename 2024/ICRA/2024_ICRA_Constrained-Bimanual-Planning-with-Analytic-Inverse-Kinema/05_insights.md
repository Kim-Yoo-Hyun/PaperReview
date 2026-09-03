# Insights — Constrained Bimanual Planning with Analytic Inverse Kinematics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.08770; PDF retrieval source: https://arxiv.org/pdf/2309.08770. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** Then, we present our parametrization of the constraint manifold for bimanual planning, and discuss its relevant geometric and topological properties.
- **p. 1 / I. INTRODUCTION - extractive body cue:** If a robot must move an object that it is holding with both hands, we propose constructing a plan for one "controllable" arm, and then ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Finally, we present various experiments demonstrating the efficacy of these new techniques.
- **p. 2 / III. METHODOLOGY - extractive body cue:** We introduce a bijective mapping between joint angles and end-effector pose for a single arm with analytic IK.
- **p. 4 / III. METHODOLOGY - extractive body cue:** In Section IV, we demonstrate that this theoretical limitation is not a major roadblock to our framework's efficacy.
- **p. 4 / III. METHODOLOGY - extractive body cue:** 2) Trajectory Optimization: Trajectory optimization in configuration space is already nonconvex, so implementing constraints (5b) and (5c) requires no algorithmic changes.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Although this constraint would be enforced by the later constraints, specifically handling this case first greatly improves the performance of the later counterexample searches.
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** Such task space constraints appear as complicated nonlinear equality constraints in configuration space, posing a major challenge to traditional motion planning algorithms.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Configurations where the subordinate arm cannot reach the end-effector of the primary arm, or where doing so would require violating joint limits, are treated as ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Hardware setup for our experiments. The two arms must work together to move an objects between the shelves, avoiding collisions and respecting the ...
- **p. 5 / IV. RESULTS - extractive body cue:** Paths marked with an asterisk were not collision-free.
- **p. 5 / IV. RESULTS - extractive body cue:** Plans from the trajectory optimization baseline also had slight collisions with obstacles.
- **p. 6 / IV. RESULTS - extractive body cue:** (c) A region that represents varying grasp distances, in addition to collision-free configurations in the shelf (not shown).
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Robot configurations sampled from various IRIS regions. average path length and planning time. We set a maximum planning time of 10 minutes for ...
- **Boundary to test:** Fig. 1: Hardware setup for our experiments. The two arms must work together to move an objects between the shelves, avoiding collisions and respecting the kinematic constraint. by these general methods. For ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Then, we present our parametrization of the constraint manifold for bimanual planning, and discuss its relevant geometric and topological properties. | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | AtlasBiRRT runtimes were only averaged over successful runs (not including timeouts). | p. 5 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Failure/limitation | Fig. 1: Hardware setup for our experiments. The two arms must work together to move an objects between the shelves, avoiding collisions and respecting the kinematic constraint. by these general methods. For ... | p. 1 (Figure/Table caption), p. 5 (IV. RESULTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `start/goal, map, dynamics와 successor/operator description → path, trajectory, symbolic state 또는 task-motion decision → feasible action sequence 또는 minimum-cost plan`.
- 이 논문의 재사용 가능한 지점은 Algorithm 1: Constrained IRIS (Single Iteration) Input: Bounding Box H0(A0, b0) Hyperellipsoid E(C, d) s.t. d ∈H0(A0, b0) Constraint Sets CS1, . . . , CSk Output: Halfspace Intersection H(A, b) 1 ...를 When a rigid object is held with both end effectors, a rigid transformation T ∈SE(3) between them becomes fixed; we let ϕT : XL →SE(3) take in an end-effector pose for the ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 path, trajectory, symbolic state 또는 task-motion decision가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 1: Hardware setup for our experiments. The two arms must work together to move an objects between the shelves, avoiding collisions and respecting the kinematic constraint. by these general methods. For ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Then, we present our parametrization of the constraint manifold for bimanual planning, and discuss its relevant geometric and topological properties.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, bimanual manipulation, motion planning, inverse kinematics`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 1: Hardware setup for our experiments. The two arms must work together to move an objects between the shelves, avoiding collisions and respecting the kinematic constraint. by these general methods. For ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: GCS can use such regions to plan motions for objects of different sizes; we include hardware demonstrations in our results video..
3. Compare against the body-reported baseline or a matched simpler baseline: We do not compare to any GCS baseline without IK, as the constraint manifold is inherently nonconvex; IK-GCS is the first proposal for extending GCS to this class of problems..
4. Report the body metric and its denominator/aggregation: (c) A region that represents varying grasp distances, in addition to collision-free configurations in the shelf (not shown)..
5. Re-run the body-reported ablation/failure condition: We do not compare to any GCS baseline without IK, as the constraint manifold is inherently nonconvex; IK-GCS is the first proposal for extending GCS to this class of problems..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY); the primary result is directionally consistent at p. 5 (IV. RESULTS), p. 6 (IV. RESULTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Then, present, parametrization mechanism이 We do not compare to any GCS baseline without IK, as the constraint manifold is inherently ... 대비 (c) A region that represents varying grasp distances, in addition to collision-free configurations in the shelf (not shown).을 개선하고, Fig. 1: Hardware setup for our experiments. The two arms must work together to move an ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
