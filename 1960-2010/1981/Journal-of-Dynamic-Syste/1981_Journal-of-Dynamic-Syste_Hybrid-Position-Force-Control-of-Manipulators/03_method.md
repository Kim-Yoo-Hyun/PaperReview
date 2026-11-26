# Method - Hybrid Position/Force Control of Manipulators

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://api.crossref.org/works/10.1115/1.3139652; PDF retrieval source: https://fab.cba.mit.edu/classes/865.15/classes/measurement/hybrid-position-force.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (Body text (section boundary not confidently recovered)), p. 5 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 4 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered))): N [Vx] rotation matrix from [H] to {C) 0 -V, o -v[ v, o V = vector from the origin of (C) to the origin of {H}, expressed in (C) ...

## Method Body Digest

- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** N [Vx] rotation matrix from [H] to {C) 0 -V, o -v[ v, o V = vector from the origin of (C) to the origin ...
- **p. 5 / Body text (section boundary not confidently recovered) - extractive body cue:** The model includes a simplified static friction term plus the Coulomb force: r-sgn(<7,.)[min(Ti];,lT,-l)] L-sgn(<7i)[Tc,i] where: TS = static friction constant TC = Coulomb friction constant ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** The first two of these techniques are limited by the accuracy and availability of manipulator models that compensate for the complicated inertial, frictional, and gravitational ...
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** Also acting on the hand is reaction force fx produced through contact with an environmental surface.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** The ability to measure and control contact forces generated at the hand, however, offers a low cost alternative for extending effective precision.
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** That is, each time the user specifies a desired trajectory in either position or force, an artificial constraint is defined.
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** For instance, a hand in contact with a stationary rigid surface is not free to move through that surface (position constraint), and, if the surface ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Manipulators of greater precision can be achieved only at the expense of size, weight, and cost.

## Design Rationale

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Note that the method we propose here does not prescribe particular feedback control laws for the regulation of errors.
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** The transformation form (C) to the joints of the manipulator is such that, for the general case, control of one manipulator joint involves every dimension ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Such techniques are just now being developed.

## Source Evidence Cues

- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** N [Vx] rotation matrix from [H] to {C) 0 -V, o -v[ v, o V = vector from the origin of (C) to the origin ...
- **p. 5 / Body text (section boundary not confidently recovered) - extractive body cue:** The model includes a simplified static friction term plus the Coulomb force: r-sgn(<7,.)[min(Ti];,lT,-l)] L-sgn(<7i)[Tc,i] where: TS = static friction constant TC = Coulomb friction constant ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** The first two of these techniques are limited by the accuracy and availability of manipulator models that compensate for the complicated inertial, frictional, and gravitational ...
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** Also acting on the hand is reaction force fx produced through contact with an environmental surface.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** The ability to measure and control contact forces generated at the hand, however, offers a low cost alternative for extending effective precision.
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** That is, each time the user specifies a desired trajectory in either position or force, an artificial constraint is defined.
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** For instance, a hand in contact with a stationary rigid surface is not free to move through that surface (position constraint), and, if the surface ...
- **Detected method headings:** none reliably recovered

## Pipeline

관절 위치·접촉력·지정한 힘과 위치 궤적 → 작업 좌표계와 축별 힘·위치 제약 → 결합한 위치·힘 서보 명령. [방법·평가의 원문 근거](./01_overview.md#observation-state-and-output-interface)

## Objective / Update Rule

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Manipulators of greater precision can be achieved only at the expense of size, weight, and cost.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** The ability to measure and control contact forces generated at the hand, however, offers a low cost alternative for extending effective precision.
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** 1.) IING CRANK C**--ff" f* 'tSr^^ XV NATURAL CONSTRAINTS V .
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** 1 Examples of force control tasks showing the constraint frame /C/, natural constraints, and artificial constraints.
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** Methods for choosing the constraints for a given assembly operation await further research.
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** In this frame N natural constraints and N orthogonal artificial constraints can be specified.
- **Formal bridge:** 관절 위치·접촉력·지정한 힘과 위치 궤적 → 작업 좌표계와 축별 힘·위치 제약 → 결합한 위치·힘 서보 명령.
- **Equation/algorithm anchors:** p. 5 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | actuator, control, signal, joint, components, force, controlled, degree, freedom, position, where, torque, applied, A/y | 관절 위치·접촉력·지정한 힘과 위치 궤적 | body cue; exact tensor/frame verify |
| State/latent | actuator, control, signal, joint, components, force, controlled, degree, freedom, position | 작업 좌표계와 축별 힘·위치 제약 | body cue; notation verify |
| Action/output | Note, here, does, prescribe, particular, feedback, control, laws, regulation, errors | 결합한 위치·힘 서보 명령 | body cue; unit/decoder verify |
| Objective/constraint | Manipulators, greater, precision, achieved, only, expense, size, weight, cost, ability | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** The actuator control signal for the /'th joint has N components - one for each force controlled degree of freedom in [C], and one for ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** A number of methods for obtaining force information exist: motor currents may be measured or programmed, [6, 11], motor output torques may be measured [7], ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Analysis, simulation, and experiments are used to evaluate the controller's ability to execute trajectories using feedback from a force sensing wrist and from position sensors ...
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** The two complementary sets of feedback loops (upper-position, lower-force), each with its own sensory system and control law, are shown here controlling a common plant, ...
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** Our goals were to examine the feasibility of the hybrid method with regard to accuracy, interactions between force and position control and stability.
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** N [Vx] rotation matrix from [H] to {C) 0 -V, o -v[ v, o V = vector from the origin of (C) to the origin ...
- **p. 5 / Body text (section boundary not confidently recovered) - extractive body cue:** [Kpp],[Kpi], and [Kpd\ = proportional, integral, and derivative position feedback gains. iff =U V cFrf the force feed-forward term T„ = the a saturation limited ...
- **Normalized interface:** observation=관절 위치·접촉력·지정한 힘과 위치 궤적; state=작업 좌표계와 축별 힘·위치 제약; output/action=결합한 위치·힘 서보 명령.

## Temporal and Runtime Contract

| Contract | PDF body cue | Unresolved detail |
|---|---|---|
| Horizon | This interpretation was verified by calculating the natural frequency of hand oscillations predicted by the model: j, = ~.JKr+Kw n 2-rr M ... | episode/sequence/action-chunk boundary |
| Rate / latency | An important step toward achieving such control can be taken by providing manipulator hands with sensors that provide information about the progress ... | Hz/fps, inference time and control rate |
| Memory | not stated or recoverable in the selected PDF body | window and reset |
| Compute | This interpretation was verified by calculating the natural frequency of hand oscillations predicted by the model: j, = ~.JKr+Kw n 2-rr M ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** N [Vx] rotation matrix from [H] to {C) 0 -V, o -v[ v, o V = vector from the origin of (C) to the origin ...
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** That is, each time the user specifies a desired trajectory in either position or force, an artificial constraint is defined.
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** For instance, a hand in contact with a stationary rigid surface is not free to move through that surface (position constraint), and, if the surface ...

## Method-Specific Formal Details

- **Body-defined terms:** rotation, matrix, vector, origin, expressed, Error, signals, position, force, found, once, equations, have, been, applied, cXd, addition, error-driven, control, ideal.
- **Relevant PDF headings:** not reliably recovered.

## Evaluation Link

| 평가 근거 | 원문에서 추출한 내용 | 원문 위치 |
|---|---|---|
| 원문 대조 | 5 Model used for simulation of hybrid control task 1 1 l-Kwwt -Acosfa,)] w2 = TT \-~K^w7. +Asin(<?i)l M3 Reaction surface model: ... | p. 5 (Body text (section boundary not confidently recovered)), p. 7 (Body text (section boundary not confidently recovered)) |
| 원문 대조 | Without this term the system was stable only when heavily overdamped. | p. 6 (Body text (section boundary not confidently recovered)), p. 6 (Body text (section boundary not confidently recovered)) |
| 원문 대조 | To improve thermal immunity, gauges mounted on opposite faces are operated as voltage divider pairs [9J. | p. 4 (Body text (section boundary not confidently recovered)), p. 5 (Body text (section boundary not confidently recovered)) |

## Failure and Ablation Link

- **p. 6 / Body text (section boundary not confidently recovered) - extractive body cue:** Without this term the system was stable only when heavily overdamped.
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** Every manipulation task can be broken down into elemental components that are defined by a particular set of contacting surfaces.
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** In these examples [vx,Vy,vz, u xu y, u z] T is the hand's velocity vector, 3 translational and 3 angular components, given in [C\.
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** The actuator control signal for the /'th joint has N components - one for each force controlled degree of freedom in [C], and one for ...
- **p. 5 / Body text (section boundary not confidently recovered) - extractive body cue:** The primary frictional component in the JPL Scheinman arm is due to Coulomb sliding force.
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** A rigid X-Y table under precise numeric control was used to provide reaction forces and disturbance motions to the manipulator hand during testing.
- **p. 6 / Body text (section boundary not confidently recovered) - extractive body cue:** As motion begins force control degrades somewhat, although contact with the reaction surface is never lost.

## Reproduction Checklist

[공통 검토 기준](../../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (Body text (section boundary not confidently recovered)), p. 5 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 4 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), objective p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)), temporal p. 7 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)).

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** N [Vx] rotation matrix from [H] to {C) 0 -V, o -v[ v, o V = vector from the origin of (C) to the origin of {H}, expressed in (C) ... (p. 4, Body text (section boundary not confidently recovered)).
- **Objective/update evidence:** Manipulators of greater precision can be achieved only at the expense of size, weight, and cost. (p. 1, Body text (section boundary not confidently recovered)).
- **Temporal/runtime evidence:** This interpretation was verified by calculating the natural frequency of hand oscillations predicted by the model: j, = ~.JKr+Kw n 2-rr M 3 This evaluates to 280 Hz for the ... (p. 7, Body text (section boundary not confidently recovered)).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
