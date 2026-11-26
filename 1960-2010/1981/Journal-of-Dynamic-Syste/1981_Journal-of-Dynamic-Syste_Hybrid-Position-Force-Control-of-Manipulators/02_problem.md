# Problem - Hybrid Position/Force Control of Manipulators

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://api.crossref.org/works/10.1115/1.3139652; PDF retrieval source: https://fab.cba.mit.edu/classes/865.15/classes/measurement/hybrid-position-force.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered))): The slow progress is due partly to a lack of rugged, reliable sensors of sufficient precision and versatility.

## PDF Body Digest

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Craig2.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** 91103 Hybrid Position/Force Control of Manipulators1 A new conceptually simple approach to controlling compliant motions of a robot manipulator is presented.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** The "hybrid" technique described combines force and torque information with positional data to satisfy simultaneous position and force trajectory constraints specified in a convenient task ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Analysis, simulation, and experiments are used to evaluate the controller's ability to execute trajectories using feedback from a force sensing wrist and from position sensors ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** The results show that the method achieves stable, accurate control of force and position trajectories for a variety of test conditions.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** The slow progress is due partly to a lack of rugged, reliable sensors of sufficient precision and versatility.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** But perhaps more important is the lack of adequate controller architectures and computing techniques needed to take advantage of such sensory information, where it available.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The slow progress is due partly to a lack of rugged, reliable sensors of sufficient precision and versatility. | 실물 팔과 모의 접촉면의 힘·위치 추종 | body wording is the source claim |
| Observation / input | The actuator control signal for the /'th joint has N components - one for each force controlled degree of freedom in [C], ... | 관절 위치·접촉력·지정한 힘과 위치 궤적 | exact sensor/frame/preprocessing from PDF body |
| State / latent | actuator, control, signal, joint, components, force, controlled, degree, freedom, position | 작업 좌표계와 축별 힘·위치 제약 | notation and tensor shape require body check |
| Output / action | Analysis, simulation, experiments, evaluate, controller, ability, execute, trajectories | 결합한 위치·힘 서보 명령 | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | 접촉 중 힘과 위치의 추종 응답 | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | 관절 위치·접촉력·지정한 힘과 위치 궤적; body terms: actuator, control, signal, joint, components, force, controlled, degree, freedom, position | p. 3 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)) |
| Decision / output variable | 결합한 위치·힘 서보 명령; body terms: Note, here, does, prescribe, particular, feedback, control, laws | p. 1 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)) |
| Objective / loss / cost | 접촉 중 힘과 위치의 추종 응답; cue terms: Manipulators, greater, precision, achieved, only, expense, size, weight | p. 5 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)) |
| Success / guarantee | completion, contact success and robustness | p. 7 (Body text (section boundary not confidently recovered)), p. 4 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** But perhaps more important is the lack of adequate controller architectures and computing techniques needed to take advantage of such sensory information, where it available.
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** In general, for each task configuration a generalized surface can be defined in a constraint space having N degrees of freedom, with position constraints along ...
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** These constraints also occur along the tangents and normals to the generalized surface, but, unlike natural constraints, artificial force constraints are specified along surface normals, ...
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** The present control methodology was designed to address this low-level control problem.

## What the Paper Changes

PDF body contribution framing (p. 1 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered))): Note that the method we propose here does not prescribe particular feedback control laws for the regulation of errors.

- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** The transformation form (C) to the joints of the manipulator is such that, for the general case, control of one manipulator joint involves every dimension ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Such techniques are just now being developed.
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** The present control methodology was designed to address this low-level control problem.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 4 | A rigid X-Y table under precise numeric control was used to provide reaction forces and disturbance motions to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | As motion begins force control degrades somewhat, although contact with the reaction surface is never lost. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The upper two curves show response to the artificial constraints while the lower curve shows the position disturbance. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Our ramp disturbance data suggest adequate force control is possible under such circumstances. | reported limitation/failure wording; scope must be verified |

## Position in the Robotics Loop

관절 위치·접촉력·지정한 힘과 위치 궤적 → 작업 좌표계와 축별 힘·위치 제약 → 결합한 위치·힘 서보 명령. [원문 근거](./01_overview.md#observation-state-and-output-interface)

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)), interface p. 3 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)), objective p. 5 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)).

[공통 검토 기준](../../../../research/READING_STATUS.md#note-checks)

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** The slow progress is due partly to a lack of rugged, reliable sensors of sufficient precision and versatility. (p. 1, Body text (section boundary not confidently recovered)).
- **Formulation-changing contribution:** Note that the method we propose here does not prescribe particular feedback control laws for the regulation of errors. (p. 1, Body text (section boundary not confidently recovered)).
- **Assumption/failure evidence:** Therefore manual dexterity remains quite low and continues to limit application opportunities and growth. (p. 1, Body text (section boundary not confidently recovered)).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
