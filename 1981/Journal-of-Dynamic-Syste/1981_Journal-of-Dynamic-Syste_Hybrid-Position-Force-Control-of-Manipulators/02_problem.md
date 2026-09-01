# Problem - Hybrid Position/Force Control of Manipulators

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1115/1.3139652; PDF retrieval source: https://doi.org/10.1115/1.3139652. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (Front matter), p. 1 (Front matter), p. 2 (Front matter), p. 2 (Front matter), p. 3 (Front matter)): The slow progress is due partly to a lack of rugged, reliable sensors of sufficient precision and versatility.

## PDF Body Digest

- **p. 1 / Front matter - extractive body cue:** Craig2 Jet Propulsion Laboratory, California Institute of Technology Pasadena, Calif.
- **p. 1 / Front matter - extractive body cue:** 91103 Hybrid Position/Force Control of Manipulators1 A new conceptually simple approach to controlling compliant motions of a robot manipulator is presented.
- **p. 1 / Front matter - extractive body cue:** The "hybrid" technique described combines force and torque information with positional data to satisfy simultaneous position and force trajectory constraints specified in a convenient task ...
- **p. 1 / Front matter - extractive body cue:** Analysis, simulation, and experiments are used to evaluate the controller's ability to execute trajectories using feedback from a force sensing wrist and from position sensors ...
- **p. 1 / Front matter - extractive body cue:** The results show that the method achieves stable, accurate control of force and position trajectories for a variety of test conditions.
- **p. 1 / Front matter - extractive body cue:** The slow progress is due partly to a lack of rugged, reliable sensors of sufficient precision and versatility.
- **p. 1 / Front matter - extractive body cue:** But perhaps more important is the lack of adequate controller architectures and computing techniques needed to take advantage of such sensory information, where it available.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The slow progress is due partly to a lack of rugged, reliable sensors of sufficient precision and versatility. | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | The actuator control signal for the /'th joint has N components - one for each force controlled degree of freedom in [C], ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF |
| State / latent | actuator, control, signal, joint, components, force, controlled, degree, freedom, position | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | Analysis, simulation, experiments, evaluate, controller, ability, execute, trajectories | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: actuator, control, signal, joint, components, force, controlled, degree, freedom, position | p. 3 (Front matter), p. 1 (Front matter), p. 1 (Front matter) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: Note, here, does, prescribe, particular, feedback, control, laws | p. 1 (Front matter), p. 3 (Front matter), p. 1 (Front matter) |
| Objective / loss / cost | task/contact/pose objective; cue terms: Manipulators, greater, precision, achieved, only, expense, size, weight | p. 5 (Front matter), p. 1 (Front matter), p. 2 (Front matter), p. 2 (Front matter), p. 3 (Front matter), p. 3 (Front matter) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (Front matter), p. 3 (Front matter), p. 3 (Front matter) |
| Success / guarantee | completion, contact success and robustness | p. 7 (Front matter), p. 4 (Front matter), p. 3 (Front matter) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / Front matter - extractive body cue:** But perhaps more important is the lack of adequate controller architectures and computing techniques needed to take advantage of such sensory information, where it available.
- **p. 2 / Front matter - extractive body cue:** In general, for each task configuration a generalized surface can be defined in a constraint space having N degrees of freedom, with position constraints along ...
- **p. 2 / Front matter - extractive body cue:** These constraints also occur along the tangents and normals to the generalized surface, but, unlike natural constraints, artificial force constraints are specified along surface normals, ...
- **p. 3 / Front matter - extractive body cue:** The present control methodology was designed to address this low-level control problem.

## What the Paper Changes

PDF contribution framing (p. 1 (Front matter), p. 3 (Front matter), p. 1 (Front matter), p. 3 (Front matter)): Note that the method we propose here does not prescribe particular feedback control laws for the regulation of errors.

- **p. 3 / Front matter - extractive body cue:** The transformation form (C) to the joints of the manipulator is such that, for the general case, control of one manipulator joint involves every dimension ...
- **p. 1 / Front matter - extractive body cue:** Such techniques are just now being developed.
- **p. 3 / Front matter - extractive body cue:** The present control methodology was designed to address this low-level control problem.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 4 | A rigid X-Y table under precise numeric control was used to provide reaction forces and disturbance motions to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | As motion begins force control degrades somewhat, although contact with the reaction surface is never lost. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The upper two curves show response to the artificial constraints while the lower curve shows the position disturbance. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Our ramp disturbance data suggest adequate force control is possible under such circumstances. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (Front matter), p. 1 (Front matter), p. 1 (Front matter), p. 3 (Front matter). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (Front matter), p. 1 (Front matter), p. 2 (Front matter), p. 2 (Front matter), p. 3 (Front matter), interface p. 3 (Front matter), p. 1 (Front matter), p. 1 (Front matter), p. 3 (Front matter), objective p. 5 (Front matter), p. 1 (Front matter), p. 2 (Front matter), p. 2 (Front matter), p. 3 (Front matter), p. 3 (Front matter).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
