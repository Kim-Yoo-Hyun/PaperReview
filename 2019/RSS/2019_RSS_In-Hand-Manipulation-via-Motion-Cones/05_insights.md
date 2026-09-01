# Insights — In-Hand Manipulation via Motion Cones

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1810.00219; PDF retrieval source: https://arxiv.org/pdf/1810.00219. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 1 / I. INTRODUCTION - extractive body cue:** We present three main contributions: • Mechanics of motion cones for planar tasks in the gravity plane.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We propose a polyhedral approximation to the motion cone for efficient computation. • Experimental validation of the stick/slip condition of motion cones in a prehensile ...
- **p. 6 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** In [3], we present a planning framework where at the highlevel, a T-RRT∗-based architecture samples different object poses in the grasp [4, 16].
- **p. 7 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** The use of motion cones for fast low-level unit-step propagation of the system and T-RRT∗-based framework for highlevel planning allows us to explore the configuration ...
- **p. 7 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** Algorithm 1 : In-Hand Manipulation Planner input : qinit, qgoal output : tree T T ←initialize tree(qinit) generate motionCones(T , qinit) while qgoal /∈T or ...
- **p. 6 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** We assume the following physical properties of the system: · Object geometry and mass. · Initial and goal pose of an object in a grasp, ...
- **p. 7 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** The planner initiates a tree T with qinit and generates motion cones at qinit.
- **Contribution anchor:** p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** We show this yields significant speed improvements with respect to our prior work [2, 3].
- **p. 1 / I. INTRODUCTION - extractive body cue:** Lynch and Mason [21] generalized the construction of motion cones to line contacts in a horizontal plane.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The generalization of motion cones to interactions with gravity opens a door for efficient and robust planning of inhand manipulations that respect and exploit the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: To make a push inside the gravity-free motion cone stable in the gravity plane, the unit grasp wrench can be scaled such that ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 8: 2000 random prehensile pushes in the configuration shown in Fig. 7 are characterized by the slip observed at the pusher contact. The motion ...
- **p. 7 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** These include sampling with rejection by a feasibility check for stable pushing [3], and a complementarity formulation (MNCP) that allows both sticking and slipping at ...
- **p. 8 / VIII. DISCUSSION - extractive body cue:** We believe that the extension and application of motion cones to more general settings provides new opportunities for fast and robust manipulation through contact.
- **Boundary to test:** Fig. 4: To make a push inside the gravity-free motion cone stable in the gravity plane, the unit grasp wrench can be scaled such that the net pusher wrench required for the ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We present three main contributions: • Mechanics of motion cones for planar tasks in the gravity plane. | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Reported outcome | Similar to [3], our planner finds a strategy to achieve the regrasp using only one pusher. | p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| Failure/limitation | Fig. 4: To make a push inside the gravity-free motion cone stable in the gravity plane, the unit grasp wrench can be scaled such that the net pusher wrench required for the ... | p. 4 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D/point cloud, object state와 contact/task observation → object geometry, affordance, contact mode 또는 end-effector state → grasp, pose, force 또는 end-effector trajectory`.
- 이 논문의 재사용 가능한 지점은 Algorithm 1 : In-Hand Manipulation Planner input : qinit, qgoal output : tree T T ←initialize tree(qinit) generate motionCones(T , qinit) while qgoal /∈T or cost(qgoal) > cost threshold do qrand ←sample ...를 In general planar tasks, external forces other than the pusher force (e.g., gravity) can alter the dynamics of contact interactions between the pusher, object, and gripper/support-plane.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 object geometry, affordance, contact mode 또는 end-effector state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Fig. 4: To make a push inside the gravity-free motion cone stable in the gravity plane, the unit grasp wrench can be scaled such that the net pusher wrench required for the ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We present three main contributions: • Mechanics of motion cones for planar tasks in the gravity plane.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, contact-rich manipulation, in-hand manipulation, motion cones`.
- **Reading predecessor in the generated track queue:** Control-Limited Differential Dynamic Programming (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Towards Tight Convex Relaxations for Contact-Rich Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 4: To make a push inside the gravity-free motion cone stable in the gravity plane, the unit grasp wrench can be scaled such that the net pusher wrench required for the ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 9: Simulation and experimental run for a pushing strategy to regrasp the aluminum object with low friction pushers..
3. Compare against the body-reported baseline or a matched simpler baseline: While there are no comparable available algorithms that can solve the type of regrasps we are interested in, we provide comparisons with our own implementations of the same high-level planner paired with ....
4. Report the body metric and its denominator/aggregation: We compare the performance in terms of planning time and the quality of the solutions..
5. Re-run the body-reported ablation/failure condition: When we replace the pushers with high-friction pushers (pushers with rubber coating), the planner detects that the desired object twist lies inside the motion cone for the side pusher at the initial ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA); the primary result is directionally consistent at p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 present, three, main mechanism이 While there are no comparable available algorithms that can solve the type of regrasps we are ... 대비 We compare the performance in terms of planning time and the quality of the solutions.을 개선하고, Fig. 4: To make a push inside the gravity-free motion cone stable in the gravity plane, ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
