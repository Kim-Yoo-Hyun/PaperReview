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

- **Paper-specific interface:** In general planar tasks, external forces other than the pusher force (e.g., gravity) can alter the dynamics of contact interactions between the pusher, object, and gripper/support-plane. (p. 1, I. INTRODUCTION).
- **Paper-specific mechanism:** We present three main contributions: • Mechanics of motion cones for planar tasks in the gravity plane. (p. 1, I. INTRODUCTION).
- **Evidence boundary:** the reported outcome is We compare the performance in terms of planning time and the quality of the solutions. (p. 7, VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS); the relevant task/metric cue is We compare the performance in terms of planning time and the quality of the solutions. (p. 7, VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS). The PDF does not establish downstream robotics benefit beyond those conditions.
- **Failure implication:** These include sampling with rejection by a feasibility check for stable pushing [3], and a complementarity formulation (MNCP) that allows both sticking and slipping at the pusher contact [2]. (p. 7, VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS).
- Preserve the paper's observation/action/data/control boundary before attributing any gain to a new downstream module.

### Dependency and evolution

- **Registry position:** `NEXT` in `Manipulation, contact, tactile, and dexterity`; tags: `Robotics, contact-rich manipulation, in-hand manipulation, motion cones`.
- **Reading predecessor in the generated track queue:** Control-Limited Differential Dynamic Programming (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** Towards Tight Convex Relaxations for Contact-Rich Manipulation (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Fig. 4: To make a push inside the gravity-free motion cone stable in the gravity plane, the unit grasp wrench can be scaled such that the net pusher wrench required for the ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the PDF-described interface and mechanism: In general planar tasks, external forces other than the pusher force (e.g., gravity) can alter the dynamics of contact interactions between the pusher, object, and gripper/support-plane. (p. 1, I. INTRODUCTION); preserve the objective/update rule: We define the configuration cost as the distance from the goal. (p. 6, VI. PLANNING IN-HAND MANIPULATIONS VIA).
2. Use the paper-reported task/data/environment cue: 9: Simulation and experimental run for a pushing strategy to regrasp the aluminum object with low friction pushers. (p. 8, VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS).
3. Compare against the reported or matched baseline: While there are no comparable available algorithms that can solve the type of regrasps we are interested in, we provide comparisons with our own implementations of the same high-level planner ... (p. 7, VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS).
4. Report the body metric with its denominator and aggregation: We compare the performance in terms of planning time and the quality of the solutions. (p. 7, VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS).
5. Re-run the reported ablation or stress/failure condition: When we replace the pushers with high-friction pushers (pushers with rubber coating), the planner detects that the desired object twist lies inside the motion cone for the side pusher at ... (p. 8, VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS); if none is reported, design one around: These include sampling with rejection by a feasibility check for stable pushing [3], and a complementarity formulation (MNCP) that allows both sticking and slipping at the pusher contact [2]. (p. 7, VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS).
6. Keep observation, action, data, compute, horizon and controller fixed when isolating the mechanism.

### What would count as a successful reproduction

- A faithful reproduction must recover the mechanism at p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), match the reported outcome at p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), and measure the boundary at p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 6 (IV. MOTION CONE FOR PLANAR PUSHING).

## Falsifiable research question

Under the paper's stated interface (In general planar tasks, external forces other than the pusher force (e.g., gravity) can alter the dynamics of contact interactions between the ...), does the paper-specific mechanism (We present three main contributions: • Mechanics of motion cones for planar tasks in the gravity plane.) retain the reported evaluation outcome (We compare the performance in terms of planning time and the quality of the solutions.) when tested against the paper's strongest explicit boundary (These include sampling with rejection by a feasibility check for stable pushing [3], and a complementarity formulation (MNCP) ...)?

**Reject the hypothesis if** Reject the hypothesis if the body-reported metric (We compare the performance in terms of planning time and the quality of the solutions.) does not improve at matched observation, action, data and compute, or if the added mechanism changes the reported failure/latency/data boundary without a measured compensating gain.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-supported mechanism:** We present three main contributions: • Mechanics of motion cones for planar tasks in the gravity plane. (p. 1, I. INTRODUCTION).
- **Paper-supported outcome:** We compare the performance in terms of planning time and the quality of the solutions. (p. 7, VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS).
- **Strongest explicit boundary:** These include sampling with rejection by a feasibility check for stable pushing [3], and a complementarity formulation (MNCP) that allows both sticking and slipping at the pusher contact [2]. (p. 7, VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS).
- **Researcher interpretation rule:** the falsifiable question below tests the mechanism under a matched protocol; it does not upgrade a queue neighbor into a citation lineage.
