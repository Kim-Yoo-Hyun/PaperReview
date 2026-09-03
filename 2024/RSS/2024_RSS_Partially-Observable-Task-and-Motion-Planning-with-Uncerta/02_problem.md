# Problem - Partially Observable Task and Motion Planning with Uncertainty and Risk Awareness

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p118.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p118.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (III. BACKGROUND), p. 1 (I. INTRODUCTION), p. 3 (III. BACKGROUND), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): However, computing 1A reference for all notation introduced henceforth is provided in Table IV in the appendix. the belief updates exactly is intractable in many problems.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Integrated task and motion planning (TAMP) has proven to be a valuable approach to generalizable long-horizon robotic manipulation and navigation problems.
- **p. 1 / Abstract - extractive body cue:** However, the typical TAMP problem formulation assumes full observability and deterministic action effects.
- **p. 1 / Abstract - extractive body cue:** These assumptions limit the ability of the planner to gather information and make decisions that are risk-aware.
- **p. 1 / Abstract - extractive body cue:** We propose a strategy for TAMP with Uncertainty and Risk Awareness (TAMPURA) that is capable of efficiently solving long-horizon planning problems with initialstate and action ...
- **p. 1 / Abstract - extractive body cue:** Our planner reasons under uncertainty at both the abstract task level and continuous controller level.
- **p. 3 / III. BACKGROUND - extractive body cue:** However, computing 1A reference for all notation introduced henceforth is provided in Table IV in the appendix. the belief updates exactly is intractable in many ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, these methods typically do not generalize to solving arbitrary complex goals over long time horizons.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, computing 1A reference for all notation introduced henceforth is provided in Table IV in the appendix. the belief updates exactly is ... | robot mechanism의 state와 task-space dynamics | body wording is the source claim |
| Observation / input | Belief-State Controller MDP When the action space A represents primitive controls to the robot such as joint torques or end-effector velocity commands, ... | joint/task state, reference와 sensor feedback | exact sensor/frame/preprocessing from PDF body |
| State / latent | Belief-State, Controller, MDP, When, action, space, represents, primitive, controls, robot | state estimate, task-space error와 control decision | notation and tensor shape require body check |
| Output / action | them, contains, unique, type, uncertainty, including, classsification, pose | torque, force, velocity 또는 position command | exact unit/frame/decoder require body check |
| Target outcome | stability, tracking and constraint satisfaction | tracking, stability, constraint satisfaction과 contact behavior | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | q, q̇, x, wrench; body terms: Belief-State, Controller, MDP, When, action, space, represents, primitive, controls, robot | p. 3 (III. BACKGROUND), p. 3 (III. BACKGROUND), p. 2 (I. INTRODUCTION) |
| Decision / output variable | u/τ subject to dynamics and actuator/contact constraints; body terms: mitigate, introduce, concept, belief-space, controller, takes, current, belief | p. 3 (III. BACKGROUND), p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | tracking or interaction error; cue terms: focus, planning, problems, objectives, modeled, goals, belief, space | p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 9 (VII. REAL-WORLD IMPLEMENTATION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 9 (VII. REAL-WORLD IMPLEMENTATION) |
| Success / guarantee | stability, tracking and constraint satisfaction | p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (VI. SIMULATED EXPERIMENTS & ANALYSIS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, these methods typically do not generalize to solving arbitrary complex goals over long time horizons.
- **p. 3 / III. BACKGROUND - extractive body cue:** Fortunately, in cases where exact belief updates cannot be computed, it can suffice to compute approximate belief states using approximate Bayesian inference methods like particle ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This paper shows how to extend TAMP to settings with partial observability, uncertainty, and imperfect symbolic descriptions of controllers.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The resulting MDP is sparse enough that high-quality uncertainty-aware solvers like LAO* [10] can be applied.

## What the Paper Changes

PDF body contribution framing (p. 3 (III. BACKGROUND), p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): To mitigate this, we introduce the concept of a belief-space controller, which takes the current belief as input and executes in closedloop fashion over extended time horizons.

- **p. 5 / IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP - extractive body cue:** We introduce an extension to PDDL for specifying schemata for controllers with uncertain effects.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our approach, TAMPURA, is to exploit a coarse model of each controller's preconditions and effects to rapidly solve deterministic, symbolic planning problems that guide the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that in tasks requiring risk sensitivity, information gathering, and robustness to uncertainty, TAMPURA significantly outperforms reinforcement learning, Monte Carlo tree search, and determinized ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Advances in techniques like behavior cloning (BC) [1, 2], reinforcement learning (RL) [3, 4], and model-based control [5, 6] have made it possible to develop ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Despite these novelties, TAMPURA, and TAMP in general, have several limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | The primary failure modes were (1) failure in perception (due, we believe, to improperly calibrated hard-coded camera poses), ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Fig. 3: Uncertainty and Risk Aware Task and Motion Planning. (a) The robot's continuous space of probabilistic beliefs ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

control writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. BACKGROUND), p. 3 (III. BACKGROUND), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (III. BACKGROUND), p. 1 (I. INTRODUCTION), p. 3 (III. BACKGROUND), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 3 (III. BACKGROUND), p. 3 (III. BACKGROUND), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), objective p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 4 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 5 (IV. PLANNING WITH AN ABSTRACT BELIEF-STATE MDP), p. 9 (VII. REAL-WORLD IMPLEMENTATION), p. 9 (VII. REAL-WORLD IMPLEMENTATION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, computing 1A reference for all notation introduced henceforth is provided in Table IV in the appendix. the belief updates exactly is intractable in many problems. (p. 3, III. BACKGROUND).
- **Formulation-changing contribution:** Our approach, TAMPURA, is to exploit a coarse model of each controller's preconditions and effects to rapidly solve deterministic, symbolic planning problems that guide the construction of a non-deterministic Markov ... (p. 1, I. INTRODUCTION).
- **Assumption/failure evidence:** 20:⃗ s ←[D[x] : x ∈zip(⃗Ψpre,⃗c,⃗Ψeff)] 21: ▷Compute f, num "failures" where c in Ψpre did not cause Ψeff. (p. 6, V. LEARNING THE SPARSE ABSTRACT MDP).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
