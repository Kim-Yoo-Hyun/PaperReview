# Problem - In-Hand Manipulation via Motion Cones

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1810.00219; PDF retrieval source: https://arxiv.org/pdf/1810.00219. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): We show this yields significant speed improvements with respect to our prior work [2, 3].

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In this paper, we present the mechanics and algorithms to compute the set of feasible motions of an object pushed in a plane.
- **p. 1 / Abstract - extractive body cue:** This set is known as the motion cone and was previously described for non-prehensile manipulation tasks in the horizontal plane.
- **p. 1 / Abstract - extractive body cue:** We generalize its geometric construction to a broader set of planar tasks, where external forces such as gravity influence the dynamics of pushing, and prehensile ...
- **p. 1 / Abstract - extractive body cue:** We show that the motion cone is defined by a set of low-curvature surfaces and provide a polyhedral cone approximation to it.
- **p. 1 / Abstract - extractive body cue:** We verify its validity with 2000 pushing experiments recorded with motion tracking system.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We show this yields significant speed improvements with respect to our prior work [2, 3].
- **p. 1 / I. INTRODUCTION - extractive body cue:** Lynch and Mason [21] generalized the construction of motion cones to line contacts in a horizontal plane.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We show this yields significant speed improvements with respect to our prior work [2, 3]. | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | Algorithm 1 : In-Hand Manipulation Planner input : qinit, qgoal output : tree T T ←initialize tree(qinit) generate motionCones(T , qinit) while ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF |
| State / latent | Algorithm, In-Hand, Manipulation, Planner, input, qinit, qgoal, output, tree, initialize | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | assume, following, physical, properties, system, Object, geometry, mass | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: Algorithm, In-Hand, Manipulation, Planner, input, qinit, qgoal, output, tree, initialize | p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 1 (I. INTRODUCTION), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: present, three, main, contributions, Mechanics, motion, cones, planar | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA) |
| Objective / loss / cost | task/contact/pose objective; cue terms: define, configuration, cost, distance, goal, selective, exploration, TRRT | p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA) |
| Success / guarantee | completion, contact success and robustness | p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 7 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS), p. 8 (VII. REGRASP EXAMPLES AND EXPERIMENTAL RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Lynch and Mason [21] generalized the construction of motion cones to line contacts in a horizontal plane.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The generalization of motion cones to interactions with gravity opens a door for efficient and robust planning of inhand manipulations that respect and exploit the ...

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA)): We present three main contributions: • Mechanics of motion cones for planar tasks in the gravity plane.

- **p. 1 / I. INTRODUCTION - extractive body cue:** We propose a polyhedral approximation to the motion cone for efficient computation. • Experimental validation of the stick/slip condition of motion cones in a prehensile ...
- **p. 6 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** In [3], we present a planning framework where at the highlevel, a T-RRT∗-based architecture samples different object poses in the grasp [4, 16].
- **p. 7 / VI. PLANNING IN-HAND MANIPULATIONS VIA - extractive body cue:** The use of motion cones for fast low-level unit-step propagation of the system and T-RRT∗-based framework for highlevel planning allows us to explore the configuration ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 4 | Fig. 4: To make a push inside the gravity-free motion cone stable in the gravity plane, the unit ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Fig. 8: 2000 random prehensile pushes in the configuration shown in Fig. 7 are characterized by the slip ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | These include sampling with rejection by a feasibility check for stable pushing [3], and a complementarity formulation (MNCP) ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | We believe that the extension and application of motion cones to more general settings provides new opportunities for ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 1 (I. INTRODUCTION), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 7 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 1 (I. INTRODUCTION), p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA), p. 1 (I. INTRODUCTION), objective p. 6 (VI. PLANNING IN-HAND MANIPULATIONS VIA).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
