# Hybrid Position/Force Control of Manipulators

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1115/1.3139652.
> PDF retrieval source: https://fab.cba.mit.edu/classes/865.15/classes/measurement/hybrid-position-force.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 1981 / Journal of Dynamic Systems, Measurement, and Control
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: CORE
- Tags: Robotics, force control, contact, manipulation
- Official paper: https://doi.org/10.1115/1.3139652
- Full-text retrieval: https://fab.cba.mit.edu/classes/865.15/classes/measurement/hybrid-position-force.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 manipulation 문제를 이해하기 위해 읽는다. 본문은 The slow progress is due partly to a lack of rugged, reliable sensors of sufficient precision and versatility.를 문제로 두고, Note that the method we propose here does not prescribe particular feedback control laws for the regulation of errors.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Craig2.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** 91103 Hybrid Position/Force Control of Manipulators1 A new conceptually simple approach to controlling compliant motions of a robot manipulator is presented.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** The "hybrid" technique described combines force and torque information with positional data to satisfy simultaneous position and force trajectory constraints specified in a convenient task ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Analysis, simulation, and experiments are used to evaluate the controller's ability to execute trajectories using feedback from a force sensing wrist and from position sensors ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** The results show that the method achieves stable, accurate control of force and position trajectories for a variety of test conditions.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** The slow progress is due partly to a lack of rugged, reliable sensors of sufficient precision and versatility.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** But perhaps more important is the lack of adequate controller architectures and computing techniques needed to take advantage of such sensory information, where it available.

## Core Idea

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Note that the method we propose here does not prescribe particular feedback control laws for the regulation of errors.
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** The transformation form (C) to the joints of the manipulator is such that, for the general case, control of one manipulator joint involves every dimension ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Such techniques are just now being developed.
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** The present control methodology was designed to address this low-level control problem.
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** N [Vx] rotation matrix from [H] to {C) 0 -V, o -v[ v, o V = vector from the origin of (C) to the origin ...
- **p. 5 / Body text (section boundary not confidently recovered) - extractive body cue:** The model includes a simplified static friction term plus the Coulomb force: r-sgn(<7,.)[min(Ti];,lT,-l)] L-sgn(<7i)[Tc,i] where: TS = static friction constant TC = Coulomb friction constant ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** The first two of these techniques are limited by the accuracy and availability of manipulator models that compensate for the complicated inertial, frictional, and gravitational ...
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** Also acting on the hand is reaction force fx produced through contact with an environmental surface.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The actuator control signal for the /'th joint has N components - one for each force controlled degree of freedom in [C], and one for each position controlled degree of freedom: (2) ... | RGB-D/point cloud, object state와 contact/task observation | p. 3 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)) |
| State/latent | actuator, control, signal, joint, components, force, controlled, degree, freedom, position, where, torque | object geometry, affordance, contact mode 또는 end-effector state | p. 3 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)) |
| Output/action | A number of methods for obtaining force information exist: motor currents may be measured or programmed, [6, 11], motor output torques may be measured [7], and wrist or hand mounted sensors may ... | grasp, pose, force 또는 end-effector trajectory | p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)) |
| Objective/outcome | Manipulators of greater precision can be achieved only at the expense of size, weight, and cost. | task completion, contact success, pose/force error와 generalization | p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)) |

## Main Claims and Actual Contribution

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Note that the method we propose here does not prescribe particular feedback control laws for the regulation of errors.
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** The transformation form (C) to the joints of the manipulator is such that, for the general case, control of one manipulator joint involves every dimension ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Such techniques are just now being developed.
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** The present control methodology was designed to address this low-level control problem.
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** To improve thermal immunity, gauges mounted on opposite faces are operated as voltage divider pairs [9J.
- **p. 5 / Body text (section boundary not confidently recovered) - extractive body cue:** Force control was achieved by combining proportional-integral (PI) control with a saturation-type feedback limiter and a simple feed forward term.
- **p. 6 / Body text (section boundary not confidently recovered) - extractive body cue:** Therefore, stability is more easily achieved.
- **p. 7 / Body text (section boundary not confidently recovered) - extractive body cue:** These changes resulted in improved force response -less overshoot and better stability - but did not affect the position servo perceptibly.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 4 (Body text (section boundary not confidently recovered)), p. 5 (Body text (section boundary not confidently recovered)) |
| Embodiment/environment | 5 Model used for simulation of hybrid control task 1 1 l-Kwwt -Acosfa,)] w2 = TT \-~K^w7. +Asin(<?i)l M3 Reaction surface model: fx=K,.(Cx CXf) Cx = ^cosfa,) + /sinfa,) (7) (8) (9) ... | hardware/simulator version and reset protocol | p. 5 (Body text (section boundary not confidently recovered)), p. 7 (Body text (section boundary not confidently recovered)) |
| Dataset/benchmark | It is an N degree of freedom Cartesian system defined with respect to the task geometry. | role, split, size and leakage | p. 5 (Body text (section boundary not confidently recovered)), p. 7 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)) |
| Metric | As the manipulator moves, irregularities in the reaction surface and small errors in the accuracy of the position servo will look like surface motion to the force controller. | definition, denominator, direction and uncertainty | p. 7 (Body text (section boundary not confidently recovered)), p. 4 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)) |
| Baseline/ablation | Without this term the system was stable only when heavily overdamped. | fair input/data/compute/action matching | p. 6 (Body text (section boundary not confidently recovered)), p. 6 (Body text (section boundary not confidently recovered)), p. 6 (Body text (section boundary not confidently recovered)) |

## Explicit Limitations and Failure Boundary

- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** A rigid X-Y table under precise numeric control was used to provide reaction forces and disturbance motions to the manipulator hand during testing.
- **p. 6 / Body text (section boundary not confidently recovered) - extractive body cue:** As motion begins force control degrades somewhat, although contact with the reaction surface is never lost.
- **p. 6 / Body text (section boundary not confidently recovered) - extractive body cue:** The upper two curves show response to the artificial constraints while the lower curve shows the position disturbance. error in the steady state was < ...
- **p. 7 / Body text (section boundary not confidently recovered) - extractive body cue:** Our ramp disturbance data suggest adequate force control is possible under such circumstances.
- **p. 7 / Body text (section boundary not confidently recovered) - extractive body cue:** Although some error in position occurs along the position trajectory, the force step produces no noticeable disturbance in position.

## Why Read It

Planning and control의 manipulation 문제를 이해하기 위해 읽는다. 본문은 The slow progress is due partly to a lack of rugged, reliable sensors of sufficient precision and versatility.를 문제로 두고, Note that the method we propose here does not prescribe particular feedback control laws for the regulation of errors.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)), p. 4 (Body text (section boundary not confidently recovered)) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** The slow progress is due partly to a lack of rugged, reliable sensors of sufficient precision and versatility. (p. 1, Body text (section boundary not confidently recovered)).
- **Actual contribution:** Note that the method we propose here does not prescribe particular feedback control laws for the regulation of errors. (p. 1, Body text (section boundary not confidently recovered)).
- **Evaluation boundary:** Comparison with previous results [1 and unpublished] shows that use of force feed-forward gives faithful trajectory control with relatively low force feedback gains. (p. 6, Body text (section boundary not confidently recovered)).
- **Explicit failure boundary:** Therefore manual dexterity remains quite low and continues to limit application opportunities and growth. (p. 1, Body text (section boundary not confidently recovered)).
