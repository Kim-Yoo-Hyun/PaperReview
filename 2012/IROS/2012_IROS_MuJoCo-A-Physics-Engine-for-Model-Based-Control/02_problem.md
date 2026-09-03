# Problem - MuJoCo: A Physics Engine for Model-Based Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/IROS.2012.6386109; PDF retrieval source: https://doi.org/10.1109/IROS.2012.6386109. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): However they lack the speed, accuracy and overall feature sets needed to automate the controller design process itself.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We describe a new physics engine tailored to model-based control.
- **p. 1 / Abstract - extractive body cue:** Multi-joint dynamics are represented in generalized coordinates and computed via recursive algorithms.
- **p. 1 / Abstract - extractive body cue:** Contact responses are computed via efficient new algorithms we have developed, based on the modern velocity-stepping approach which avoids the difficulties with spring-dampers.
- **p. 1 / Abstract - extractive body cue:** Models are specified using either a high-level C++ API or an intuitive XML file format.
- **p. 1 / Abstract - extractive body cue:** A built-in compiler transforms the user model into an optimized data structure used for runtime computation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However they lack the speed, accuracy and overall feature sets needed to automate the controller design process itself.
- **p. 1 / I. INTRODUCTION - extractive body cue:** What is less obvious however is that, in the context of control optimization, these requirements become so demanding that none of the existing physics engines ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However they lack the speed, accuracy and overall feature sets needed to automate the controller design process itself. | physics simulation의 robot/environment model | body wording is the source claim |
| Observation / input | The tendon path is the shortest path that passes through a sequence of specified sites or wraps around specified geoms. h) Actuator: ... | simulated state, geometry, contact와 control input | exact sensor/frame/preprocessing from PDF body |
| State / latent | tendon, path, shortest, passes, through, sequence, specified, sites, wraps, around | dynamics/contact state 또는 learned simulator representation | notation and tensor shape require body check |
| Output / action | other, spectrum, engines, SD/FAST, OpenSim, represent, system, state | simulation step, trajectory 또는 environment query | exact unit/frame/decoder require body check |
| Target outcome | fidelity, throughput and downstream task utility | physical plausibility, speed, reproducibility와 task utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sim state s_t and parameters δ; body terms: tendon, path, shortest, passes, through, sequence, specified, sites, wraps, around | p. 7 (III. MODELING), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Decision / output variable | sim action/rollout; body terms: useful, approximating, derivatives, finite, differencing, turn, enables, numerical | p. 2 (I. INTRODUCTION), p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 6 (III. MODELING) |
| Objective / loss / cost | physics/model/planning objective; cue terms: Equations, motion, smooth, dynamics, will, following, notation, position | p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 7 (III. MODELING), p. 7 (III. MODELING) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 7 (III. MODELING), p. 7 (III. MODELING) |
| Success / guarantee | fidelity, throughput and downstream task utility | p. 4 (5) Integrate numerically to obtain the next state), p. 4 (5) Integrate numerically to obtain the next state), p. 5 (5) Integrate numerically to obtain the next state) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** What is less obvious however is that, in the context of control optimization, these requirements become so demanding that none of the existing physics engines ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Another issue with game engines lies in the contact dynamics, formulated as (approximations to) linear complementarity problems or LCPs [8].
- **p. 2 / I. INTRODUCTION - extractive body cue:** Section IV presents timing tests and comparisons to SD/FAST - which does not handle contacts, but is the best prior engine for multi-joint dynamics in ...

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 6 (III. MODELING), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): This is useful for approximating derivatives via finite differencing, which in turn enables numerical optimization. • Inverse dynamics can always be computed, even in the presence of contacts and equality ...

- **p. 2 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** The procedure for solving the above equations of motion consists of the following steps:
- **p. 6 / III. MODELING - extractive body cue:** A MuJoCo model consists of one or several kinematic trees, which can have f1oating bases including isolated objects.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Existing physics engines can be used to test controllers that are already designed.
- **p. 1 / I. INTRODUCTION - extractive body cue:** As Sims [7] pointed out, if the physics engine allows cheating the optimization algorithm will find a way to exploit it - and produce a ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | 1) Compute the Cartesian positions and orientations of all rigid bodies (i.e. the forward kinematics), detect potential collisions ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | In the tangent plane we have vF parallel to fF ­ vFfF® ≤0 (5) °°fF°° ≤N The first ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Since the underlying problem is NP-hard, the algorithm cannot always find the exact solution (which has 0 residual). | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | It is needed for three reasons: is often singular; without the inverse cannot be defined (see below); one ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

simulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 7 (III. MODELING), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 7 (III. MODELING). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 7 (III. MODELING), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 7 (III. MODELING), objective p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 7 (III. MODELING), p. 7 (III. MODELING).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However they lack the speed, accuracy and overall feature sets needed to automate the controller design process itself. (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** This is useful for approximating derivatives via finite differencing, which in turn enables numerical optimization. • Inverse dynamics can always be computed, even in the presence of contacts and equality ... (p. 2, I. INTRODUCTION).
- **Assumption/failure evidence:** In the absence of adequate tools, the field continues to rely on manual controller designs - which may be a large part of the reason why present-day robots do not ... (p. 1, I. INTRODUCTION).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
