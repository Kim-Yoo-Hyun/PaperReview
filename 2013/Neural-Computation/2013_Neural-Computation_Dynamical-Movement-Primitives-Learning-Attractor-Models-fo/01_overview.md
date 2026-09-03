# Dynamical Movement Primitives: Learning Attractor Models for Motor Behaviors

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (47 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://is.mpg.de/ics/publications/ijspeert_nc_2013.
> PDF retrieval source: https://www.pure.ed.ac.uk/ws/portalfiles/portal/7874487/NECO_a_00393.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2013 / Neural Computation
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Robotics, movement primitives, dynamical systems, motor control
- Official paper: https://is.mpg.de/ics/publications/ijspeert_nc_2013
- Full-text retrieval: https://www.pure.ed.ac.uk/ws/portalfiles/portal/7874487/NECO_a_00393.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (47 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 control 문제를 이해하기 위해 읽는다. 본문은 Finding an appropriate dynamical systems model for a given behavioral phenomenon is nontrivial due to the parameter sensitivity of nonlinear differential equations and their lack of analytical predictability.를 문제로 두고, In this letter, we propose a generic modeling approach to generate multidimensional systems of weakly nonlinear differential equations to 1With low-dimensional, we refer to systems with less than about 100 degrees of ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 3 / 1 Introduction - extractive body cue:** In the wake of the development of nonlinear systems theory (Guckenheimer & Holmes, 1983; Strogatz, 1994; Scott, 2005), it has become common practice in several ...
- **p. 3 / 1 Introduction - extractive body cue:** Such approaches are motivated by the insight that coupling effects of nonlinear systems exhibit rich abilities for forming complex coordinated patterns without the need to ...
- **p. 3 / 1 Introduction - extractive body cue:** Among the many different forms of nonlinear systems (e.g., high-dimensional, weakly coupled, strongly coupled, chaotic, Hamiltonian, dissipative), this letter addresses low-dimensional nonlinear systems, for example, ...
- **p. 3 / 1 Introduction - extractive body cue:** First, a model of a baseline behavior is required, as in generating a basic pattern for bipedal locomotion or reach-and-grasp in arm movement.
- **p. 3 / 1 Introduction - extractive body cue:** Such behaviors are goal oriented; the focus is less on emergent coordination phenomena and more on achieving a task objective.
- **p. 3 / 1 Introduction - extractive body cue:** Finding an appropriate dynamical systems model for a given behavioral phenomenon is nontrivial due to the parameter sensitivity of nonlinear differential equations and their lack ...
- **p. 3 / 1 Introduction - extractive body cue:** Many impressive studies have been generated in this manner (Schoner & Kelso, 1988; Sch¨oner, 1990; Taga, Yamaguchi, & Shimizu, 1991; Schaal & Sternad, 1998; Kelso, ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** In this letter, we propose a generic modeling approach to generate multidimensional systems of weakly nonlinear differential equations to 1With low-dimensional, we refer to systems ...
- **p. 4 / 1 Introduction - extractive body cue:** The essence of our methodology is to transform well-understood simple attractor systems with the help of a learnable forcing function term into a desired attractor ...
- **p. 6 / 2 A Learnable Nonlinear Attractor Systems - extractive body cue:** Thus, as a novel component, we introduce a replacement of time by means of the following first-order linear dynamics in x τ ˙x = -αxx, ...
- **p. 4 / 1 Introduction - extractive body cue:** Our approach also provides a metric to compare different dynamical systems in a scale-invariant and temporally invariant way.
- **p. 3 / 1 Introduction - extractive body cue:** In the wake of the development of nonlinear systems theory (Guckenheimer & Holmes, 1983; Strogatz, 1994; Scott, 2005), it has become common practice in several ...
- **p. 4 / 1 Introduction - extractive body cue:** The following sections first introduce our modeling approach (see section 1), then, examine its theoretical properties (see section 2), and finally explore our approach in ...
- **p. 3 / 1 Introduction - extractive body cue:** In order to allow investigations of such second objectives, a dynamical systems model has to be found first.
- **p. 4 / 1 Introduction - extractive body cue:** We evaluate our approach in the domain of motor control for robotics, where desired kinematic motor behaviors will be coded in attractor landscapes and then ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Since the forcing term is chosen to be nonlinear in the state of the differential equations and since it transforms the simple dynamics of the unforced systems into a desired (weakly) nonlinear ... | joint/task state, reference와 sensor feedback | p. 6 (2 A Learnable Nonlinear Attractor Systems), p. 6 (2 A Learnable Nonlinear Attractor Systems) |
| State/latent | Since, forcing, term, chosen, nonlinear, state, differential, equations, transforms, simple, dynamics, unforced | state estimate, task-space error와 control decision | p. 6 (2 A Learnable Nonlinear Attractor Systems), p. 6 (2 A Learnable Nonlinear Attractor Systems), p. 8 (2 A Learnable Nonlinear Attractor Systems) |
| Output/action | Starting from some arbitrarily chosen initial state x0, such as x0 = 1, the state x converges monotonically to zero. x can thus be conceived of as a phase variable, where x ... | torque, force, velocity 또는 position command | p. 6 (2 A Learnable Nonlinear Attractor Systems), p. 8 (2 A Learnable Nonlinear Attractor Systems), p. 8 (2 A Learnable Nonlinear Attractor Systems) |
| Objective/outcome | The essence of our approach is to start with a simple dynamical system, such as a set of linear differential equations, and transform those into a weakly nonlinear system with prescribed attractor ... | tracking, stability, constraint satisfaction과 contact behavior | p. 2 (Body text (section not recovered)), p. 3 (1 Introduction), p. 3 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** In this letter, we propose a generic modeling approach to generate multidimensional systems of weakly nonlinear differential equations to 1With low-dimensional, we refer to systems ...
- **p. 4 / 1 Introduction - extractive body cue:** The essence of our methodology is to transform well-understood simple attractor systems with the help of a learnable forcing function term into a desired attractor ...
- **p. 6 / 2 A Learnable Nonlinear Attractor Systems - extractive body cue:** Thus, as a novel component, we introduce a replacement of time by means of the following first-order linear dynamics in x τ ˙x = -αxx, ...
- **p. 4 / 1 Introduction - extractive body cue:** Our approach also provides a metric to compare different dynamical systems in a scale-invariant and temporally invariant way.
- **p. 3 / 1 Introduction - extractive body cue:** In the wake of the development of nonlinear systems theory (Guckenheimer & Holmes, 1983; Strogatz, 1994; Scott, 2005), it has become common practice in several ...
- **p. 29 / 3 Evaluations - extractive body cue:** Within two beats (the time needed to extract the frequency from the acoustic signal), perfect synchronization and phase locking is achieved with a 0.15 Hz ...
- **p. 30 / 3 Evaluations - extractive body cue:** It should be noted that many other coupling terms could be created to achieve similar behavior and that our realization is just a simple and ...
- **p. 22 / 3 Evaluations - extractive body cue:** For instance, Wada and Kawato (2004) presented an elegant algorithm that recursively fits a demonstrated trajectory with a growing number of spline nodes until an ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 29 (3 Evaluations), p. 30 (3 Evaluations) |
| Embodiment/environment | In the next sections, we present and review several experimental evaluations of applying our approach to learning attractor systems in the domain of motor control, using both simulation and robotic studies. | hardware/simulator version and reset protocol | p. 22 (3 Evaluations), p. 22 (3 Evaluations) |
| Dataset/benchmark | A state-space mixture model for our humanoid robot above would require a 60-dimension state space and thus would create computational and numerical problems. | role, split, size and leakage | p. 22 (3 Evaluations), p. 22 (3 Evaluations), p. 24 (3 Evaluations), p. 26 (3 Evaluations) |
| Metric | For instance, Wada and Kawato (2004) presented an elegant algorithm that recursively fits a demonstrated trajectory with a growing number of spline nodes until an accuracy criterion is reached. | definition, denominator, direction and uncertainty | p. 22 (3 Evaluations), p. 29 (3 Evaluations), p. 29 (3 Evaluations) |
| Baseline/ablation | The design parameters of the rhythmic system are g, the baseline of the oscillation; τ, the period divided by 2π; and r, the amplitude of oscillations. | fair input/data/compute/action matching | p. 23 (3 Evaluations), p. 33 (Figure/Table caption), p. 9 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 24 / 3 Evaluations - extractive body cue:** Those online modulations are among the most important properties offered by a dynamical systems approach, and these properties cannot easily be replicated without the attractor ...
- **p. 26 / 3 Evaluations - extractive body cue:** Trajectories starting at points where the direct line to the goal does not intersect with the obstacle are only minimally curved around the obstacle, while ...
- **p. 26 / Figure/Table caption - extractive body cue:** Figure 8: Illustration of obstacle avoidance with a coupling term. The obstacle is the large (red) sphere in the center of the plot. Various trajectories ...
- **p. 29 / 3 Evaluations - extractive body cue:** In this section, we illustrate how both temporal and spatial coupling can be used together to model disturbance rejection, a property that is inherent in ...
- **p. 31 / 3 Evaluations - extractive body cue:** Thus, for instance, a variation at the end of a movement will not affect the parameter values at the beginning of a movement, which creates ...

## Why Read It

Planning and control의 control 문제를 이해하기 위해 읽는다. 본문은 Finding an appropriate dynamical systems model for a given behavioral phenomenon is nontrivial due to the parameter sensitivity of nonlinear differential equations and their lack of analytical predictability.를 문제로 두고, In this letter, we propose a generic modeling approach to generate multidimensional systems of weakly nonlinear differential equations to 1With low-dimensional, we refer to systems with less than about 100 degrees of ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 6 (2 A Learnable Nonlinear Attractor Systems), p. 4 (1 Introduction), p. 3 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
