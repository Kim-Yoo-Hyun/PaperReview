# Problem - Towards Tight Convex Relaxations for Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p132.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p132.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (V. BACKGROUND AND OPTIMIZATION TOOLS), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (V. BACKGROUND AND OPTIMIZATION TOOLS), p. 2 (I. INTRODUCTION)): The optimality gap δopt can then be overestimated as δopt = Cround -Copt Copt ≤Cround -Crelax Crelax = δrelax (2) Finally, we note that the original problem description in [1], ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We present a novel method for global motion planning of robotic systems that interact with the environment through contacts.
- **p. 1 / Abstract - extractive body cue:** Our method directly handles the hybrid nature of such tasks using tools from convex optimization.
- **p. 1 / Abstract - extractive body cue:** We formulate the motion-planning problem as a shortest-path problem in a graph of convex sets, where a path in the graph corresponds to a contact ...
- **p. 1 / Abstract - extractive body cue:** For each contact mode, we use semidefinite programming to relax the nonconvex dynamics that results from the simultaneous optimization of the object's pose, contact locations, ...
- **p. 1 / Abstract - extractive body cue:** The result is a tight convex relaxation of the overall planning problem, that can be efficiently solved and quickly rounded to find a feasible contact-rich ...
- **p. 3 / V. BACKGROUND AND OPTIMIZATION TOOLS - extractive body cue:** The optimality gap δopt can then be overestimated as δopt = Cround -Copt Copt ≤Cround -Crelax Crelax = δrelax (2) Finally, we note that the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** It generally involves both a hybrid and underactuated dynamical system, making planning and control difficult.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The optimality gap δopt can then be overestimated as δopt = Cround -Copt Copt ≤Cround -Crelax Crelax = δrelax (2) Finally, we ... | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | We represent a trajectory segment within each mode for the slider-pusher system by N discrete knot points for the state and N ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF body |
| State / latent | represent, trajectory, segment, within, mode, slider-pusher, system, discrete, knot, points | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | enforce, continuity, between, state, trajectories, path, graph, assume | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: represent, trajectory, segment, within, mode, slider-pusher, system, discrete, knot, points | p. 6 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: approximates, bilinearities, tight, Semidefinite, Programming, SDP, relaxation, contact | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | task/contact/pose objective; cue terms: principle, does, include, tightening, constraints, yields, potentially, weaker | p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 3 (V. BACKGROUND AND OPTIMIZATION TOOLS), p. 3 (IV. HIGH-LEVEL APPROACH), p. 5 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 6 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 6 (VII. MOTION PLANNING FOR PLANAR PUSHING) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (V. BACKGROUND AND OPTIMIZATION TOOLS), p. 3 (V. BACKGROUND AND OPTIMIZATION TOOLS), p. 4 (V. BACKGROUND AND OPTIMIZATION TOOLS) |
| Success / guarantee | completion, contact success and robustness | p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 8 (VIII. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** It generally involves both a hybrid and underactuated dynamical system, making planning and control difficult.
- **p. 1 / I. INTRODUCTION - extractive body cue:** We evaluate our motion planner through thorough numerical experiments, which show that the trajectories we generate typically have a very small optimality gap (10% on ...
- **p. 3 / V. BACKGROUND AND OPTIMIZATION TOOLS - extractive body cue:** Additionally, the GCS framework naturally gives us an upper bound on the optimality gap to a solution; Let Crelax ≤Copt ≤Cround be the costs of ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** of planar pushing, the technique we introduce generalizes naturally to more complex multi-contact problems.

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. HIGH-LEVEL APPROACH), p. 2 (III. PROBLEM STATEMENT)): Our method approximates these bilinearities using a tight Semidefinite Programming (SDP) relaxation for each contact mode.

- **p. 1 / I. INTRODUCTION - extractive body cue:** As a first application for evaluating our method, this work explores the task of planar pushing, first studied by Mason in [2].
- **p. 2 / I. INTRODUCTION - extractive body cue:** of planar pushing, the technique we introduce generalizes naturally to more complex multi-contact problems.
- **p. 3 / IV. HIGH-LEVEL APPROACH - extractive body cue:** The second step in our method is to formulate the global motion planning problem as an SPP in a GCS [1].
- **p. 2 / III. PROBLEM STATEMENT - extractive body cue:** As a first application of our method, we explore planar pushing, a non-prehensile manipulation task where the robot uses a cylindrical finger to manipulate the ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | Future work will explore the ability of these reduction methods to accelerate the planning. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Fig. 3: a) An example of a configuration-space partitioning Q1, . . . , Q4 and the linear ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Fig. 5: Our method is able to generate close-to globally optimal plans for pushing tasks with collision-free motion ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Our method also guarantees that the trajectory stays collision-free between contacts, while the baseline can be seen to ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 6 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 3 (III. PROBLEM STATEMENT). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (V. BACKGROUND AND OPTIMIZATION TOOLS), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (V. BACKGROUND AND OPTIMIZATION TOOLS), p. 2 (I. INTRODUCTION), interface p. 6 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 3 (III. PROBLEM STATEMENT), objective p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 3 (V. BACKGROUND AND OPTIMIZATION TOOLS), p. 3 (IV. HIGH-LEVEL APPROACH), p. 5 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 6 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 6 (VII. MOTION PLANNING FOR PLANAR PUSHING).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** It generally involves both a hybrid and underactuated dynamical system, making planning and control difficult. (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** Our method approximates these bilinearities using a tight Semidefinite Programming (SDP) relaxation for each contact mode. (p. 1, I. INTRODUCTION).
- **Assumption/failure evidence:** In contrast, the baseline often fails, finding a solution in 58% of the instances for the box-shaped slider geometry and a mere 12% for the T-shaped slider. (p. 10, VIII. EXPERIMENTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
