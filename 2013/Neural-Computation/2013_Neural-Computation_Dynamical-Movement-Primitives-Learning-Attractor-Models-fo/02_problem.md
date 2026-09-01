# Problem - Dynamical Movement Primitives: Learning Attractor Models for Motor Behaviors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (47 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://is.mpg.de/ics/publications/ijspeert_nc_2013; PDF retrieval source: https://www.pure.ed.ac.uk/ws/portalfiles/portal/7874487/NECO_a_00393.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction)): Finding an appropriate dynamical systems model for a given behavioral phenomenon is nontrivial due to the parameter sensitivity of nonlinear differential equations and their lack of analytical predictability.

## PDF Body Digest

- **p. 3 / 1 Introduction - extractive PDF cue:** In the wake of the development of nonlinear systems theory (Guckenheimer & Holmes, 1983; Strogatz, 1994; Scott, 2005), it has become common practice in several ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Such approaches are motivated by the insight that coupling effects of nonlinear systems exhibit rich abilities for forming complex coordinated patterns without the need to ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Among the many different forms of nonlinear systems (e.g., high-dimensional, weakly coupled, strongly coupled, chaotic, Hamiltonian, dissipative), this letter addresses low-dimensional nonlinear systems, for example, ...
- **p. 3 / 1 Introduction - extractive PDF cue:** First, a model of a baseline behavior is required, as in generating a basic pattern for bipedal locomotion or reach-and-grasp in arm movement.
- **p. 3 / 1 Introduction - extractive PDF cue:** Such behaviors are goal oriented; the focus is less on emergent coordination phenomena and more on achieving a task objective.
- **p. 3 / 1 Introduction - extractive PDF cue:** Finding an appropriate dynamical systems model for a given behavioral phenomenon is nontrivial due to the parameter sensitivity of nonlinear differential equations and their lack ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Many impressive studies have been generated in this manner (Schoner & Kelso, 1988; Sch¨oner, 1990; Taga, Yamaguchi, & Shimizu, 1991; Schaal & Sternad, 1998; Kelso, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Finding an appropriate dynamical systems model for a given behavioral phenomenon is nontrivial due to the parameter sensitivity of nonlinear differential equations ... | robot mechanism의 state와 task-space dynamics | body wording is the source claim |
| Observation / input | Since the forcing term is chosen to be nonlinear in the state of the differential equations and since it transforms the simple ... | joint/task state, reference와 sensor feedback | exact sensor/frame/preprocessing from PDF |
| State / latent | Since, forcing, term, chosen, nonlinear, state, differential, equations, transforms, simple | state estimate, task-space error와 control decision | notation and tensor shape require body check |
| Output / action | start, time, evolution, equations, goal, canonical, system, state | torque, force, velocity 또는 position command | exact unit/frame/decoder require body check |
| Target outcome | stability, tracking and constraint satisfaction | tracking, stability, constraint satisfaction과 contact behavior | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | q, q̇, x, wrench; body terms: Since, forcing, term, chosen, nonlinear, state, differential, equations, transforms, simple | p. 6 (2 A Learnable Nonlinear Attractor Systems), p. 6 (2 A Learnable Nonlinear Attractor Systems), p. 8 (2 A Learnable Nonlinear Attractor Systems) |
| Decision / output variable | u/τ subject to dynamics and actuator/contact constraints; body terms: letter, generic, modeling, generate, multidimensional, systems, weakly, nonlinear | p. 3 (1 Introduction), p. 4 (1 Introduction), p. 6 (2 A Learnable Nonlinear Attractor Systems) |
| Objective / loss / cost | tracking or interaction error; cue terms: order, allow, investigations, second, objectives, dynamical, systems, model | p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (2 A Learnable Nonlinear Attractor Systems), p. 5 (2 A Learnable Nonlinear Attractor Systems), p. 5 (2 A Learnable Nonlinear Attractor Systems) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (2 A Learnable Nonlinear Attractor Systems), p. 5 (2 A Learnable Nonlinear Attractor Systems), p. 5 (2 A Learnable Nonlinear Attractor Systems) |
| Success / guarantee | stability, tracking and constraint satisfaction | p. 22 (3 Evaluations), p. 29 (3 Evaluations), p. 29 (3 Evaluations) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 3 / 1 Introduction - extractive PDF cue:** Many impressive studies have been generated in this manner (Schoner & Kelso, 1988; Sch¨oner, 1990; Taga, Yamaguchi, & Shimizu, 1991; Schaal & Sternad, 1998; Kelso, ...
- **p. 4 / 1 Introduction - extractive PDF cue:** Here, we review previous work and present our system in more detail, introduce examples of spatial and temporal couplings, and discuss issues related to generalization ...

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 4 (1 Introduction), p. 6 (2 A Learnable Nonlinear Attractor Systems), p. 4 (1 Introduction), p. 3 (1 Introduction)): In this letter, we propose a generic modeling approach to generate multidimensional systems of weakly nonlinear differential equations to 1With low-dimensional, we refer to systems with less than about 100 ...

- **p. 4 / 1 Introduction - extractive PDF cue:** The essence of our methodology is to transform well-understood simple attractor systems with the help of a learnable forcing function term into a desired attractor ...
- **p. 6 / 2 A Learnable Nonlinear Attractor Systems - extractive PDF cue:** Thus, as a novel component, we introduce a replacement of time by means of the following first-order linear dynamics in x τ ˙x = -αxx, ...
- **p. 4 / 1 Introduction - extractive PDF cue:** Our approach also provides a metric to compare different dynamical systems in a scale-invariant and temporally invariant way.
- **p. 3 / 1 Introduction - extractive PDF cue:** In the wake of the development of nonlinear systems theory (Guckenheimer & Holmes, 1983; Strogatz, 1994; Scott, 2005), it has become common practice in several ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 24 | Those online modulations are among the most important properties offered by a dynamical systems approach, and these properties ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 26 | Trajectories starting at points where the direct line to the goal does not intersect with the obstacle are ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 26 | Figure 8: Illustration of obstacle avoidance with a coupling term. The obstacle is the large (red) sphere in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 29 | In this section, we illustrate how both temporal and spatial coupling can be used together to model disturbance ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

control writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (2 A Learnable Nonlinear Attractor Systems), p. 6 (2 A Learnable Nonlinear Attractor Systems), p. 8 (2 A Learnable Nonlinear Attractor Systems), p. 8 (2 A Learnable Nonlinear Attractor Systems). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), interface p. 6 (2 A Learnable Nonlinear Attractor Systems), p. 6 (2 A Learnable Nonlinear Attractor Systems), p. 8 (2 A Learnable Nonlinear Attractor Systems), p. 8 (2 A Learnable Nonlinear Attractor Systems), objective p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (2 A Learnable Nonlinear Attractor Systems), p. 5 (2 A Learnable Nonlinear Attractor Systems), p. 5 (2 A Learnable Nonlinear Attractor Systems).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
