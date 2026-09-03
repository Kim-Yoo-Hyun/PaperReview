# In-Hand Manipulation via Motion Cones

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1810.00219.
> PDF retrieval source: https://arxiv.org/pdf/1810.00219. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, contact-rich manipulation, in-hand manipulation, motion cones
- Official paper: https://arxiv.org/abs/1810.00219
- Full-text retrieval: https://arxiv.org/pdf/1810.00219
- Code/Project: https://mcube.mit.edu/research/motion-cones.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 We show this yields significant speed improvements with respect to our prior work [2, 3].를 문제로 두고, We present three main contributions: • Mechanics of motion cones for planar tasks in the gravity plane.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper, we present the mechanics and algorithms to compute the set of feasible motions of an object pushed in a plane.
- **p. 1 / Abstract - extractive body cue:** This set is known as the motion cone and was previously described for non-prehensile manipulation tasks in the horizontal plane.
- **p. 1 / Abstract - extractive body cue:** We generalize its geometric construction to a broader set of planar tasks, where external forces such as gravity influence the dynamics of pushing, and prehensile ...
- **p. 1 / Abstract - extractive body cue:** We show that the motion cone is defined by a set of low-curvature surfaces and provide a polyhedral cone approximation to it.
- **p. 1 / Abstract - extractive body cue:** We verify its validity with 2000 pushing experiments recorded with motion tracking system.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We show this yields significant speed improvements with respect to our prior work [2, 3].
- **p. 1 / I. INTRODUCTION - extractive body cue:** Lynch and Mason [21] generalized the construction of motion cones to line contacts in a horizontal plane.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** We present three main contributions: • Mechanics of motion cones for planar tasks in the gravity plane.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We propose a polyhedral approximation to the motion cone for efficient computation. • Experimental validation of the stick/slip condition of motion cones in a prehensile ...
- **p. 6 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** In [3], we present a planning framework where at the highlevel, a T-RRT∗-based architecture samples different object poses in the grasp [4, 16].
- **p. 7 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** The use of motion cones for fast low-level unit-step propagation of the system and T-RRT∗-based framework for highlevel planning allows us to explore the configuration ...
- **p. 7 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** Algorithm 1 : In-Hand Manipulation Planner input : qinit, qgoal output : tree T T ←initialize tree(qinit) generate motionCones(T , qinit) while qgoal /∈T or ...
- **p. 6 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** We assume the following physical properties of the system: · Object geometry and mass. · Initial and goal pose of an object in a grasp, ...
- **p. 7 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** The planner initiates a tree T with qinit and generates motion cones at qinit.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Algorithm 1 : In-Hand Manipulation Planner input : qinit, qgoal output : tree T T ←initialize tree(qinit) generate motionCones(T , qinit) while qgoal /∈T or cost(qgoal) > cost threshold do qrand ←sample ... | RGB-D/point cloud, object state와 contact/task observation | p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 1 (I. INTRODUCTION) |
| State/latent | Algorithm, In-Hand, Manipulation, Planner, input, qinit, qgoal, output, tree, initialize, generate, motionCones | object geometry, affordance, contact mode 또는 end-effector state | p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 1 (I. INTRODUCTION), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA) |
| Output/action | In general planar tasks, external forces other than the pusher force (e.g., gravity) can alter the dynamics of contact interactions between the pusher, object, and gripper/support-plane. | grasp, pose, force 또는 end-effector trajectory | p. 1 (I. INTRODUCTION), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 1 (I. INTRODUCTION) |
| Objective/outcome | We define the configuration cost as the distance from the goal. | task completion, contact success, pose/force error와 generalization | p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** We present three main contributions: • Mechanics of motion cones for planar tasks in the gravity plane.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We propose a polyhedral approximation to the motion cone for efficient computation. • Experimental validation of the stick/slip condition of motion cones in a prehensile ...
- **p. 6 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** In [3], we present a planning framework where at the highlevel, a T-RRT∗-based architecture samples different object poses in the grasp [4, 16].
- **p. 7 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** The use of motion cones for fast low-level unit-step propagation of the system and T-RRT∗-based framework for highlevel planning allows us to explore the configuration ...
- **p. 8 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** Similar to [3], our planner finds a strategy to achieve the regrasp using only one pusher.
- **p. 7 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** We compare the performance in terms of planning time and the quality of the solutions.
- **p. 7 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** We evaluate the performance of our planner with examples of a parallel-jaw gripper manipulating a variety of objects.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| Embodiment/environment | 9: Simulation and experimental run for a pushing strategy to regrasp the aluminum object with low friction pushers. | hardware/simulator version and reset protocol | p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| Dataset/benchmark | We evaluate the performance of our planner with examples of a parallel-jaw gripper manipulating a variety of objects. | role, split, size and leakage | p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| Metric | We compare the performance in terms of planning time and the quality of the solutions. | definition, denominator, direction and uncertainty | p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |
| Baseline/ablation | While there are no comparable available algorithms that can solve the type of regrasps we are interested in, we provide comparisons with our own implementations of the same high-level planner paired with ... | fair input/data/compute/action matching | p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: To make a push inside the gravity-free motion cone stable in the gravity plane, the unit grasp wrench can be scaled such that ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 8: 2000 random prehensile pushes in the configuration shown in Fig. 7 are characterized by the slip observed at the pusher contact. The motion ...
- **p. 7 / VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS - extractive body cue:** These include sampling with rejection by a feasibility check for stable pushing [3], and a complementarity formulation (MNCP) that allows both sticking and slipping at ...
- **p. 8 / VIII. DISCUSSION - extractive body cue:** We believe that the extension and application of motion cones to more general settings provides new opportunities for fast and robust manipulation through contact.

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 We show this yields significant speed improvements with respect to our prior work [2, 3].를 문제로 두고, We present three main contributions: • Mechanics of motion cones for planar tasks in the gravity plane.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** We show this yields significant speed improvements with respect to our prior work [2, 3]. (p. 1, I. INTRODUCTION).
- **Actual contribution:** We present three main contributions: • Mechanics of motion cones for planar tasks in the gravity plane. (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** We compare the performance in terms of planning time and the quality of the solutions. (p. 7, VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS).
- **Explicit failure boundary:** These include sampling with rejection by a feasibility check for stable pushing [3], and a complementarity formulation (MNCP) that allows both sticking and slipping at the pusher contact [2]. (p. 7, VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS).
