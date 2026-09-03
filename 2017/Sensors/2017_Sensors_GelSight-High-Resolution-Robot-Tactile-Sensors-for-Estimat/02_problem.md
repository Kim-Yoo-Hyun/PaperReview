# Problem - GelSight: High-Resolution Robot Tactile Sensors for Estimating Geometry and Force

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://publications.ri.cmu.edu/gelsight-high-resolution-robot-tactile-sensors-for-estimating-geometry-and-force/; PDF retrieval source: https://publications.ri.cmu.edu/gelsight-high-resolution-robot-tactile-sensors-for-estimating-geometry-and-force/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): Those tasks, however, are still challenges for robots because they are not yet able to fully apply tactile sensing.

## PDF Body Digest

- **p. 1 / 1. Introduction - extractive body cue:** Tactile sensing is an important mode for both human and robots to perceive the environment.
- **p. 1 / 1. Introduction - extractive body cue:** In the past decades, researchers have developed many different tactile sensors for robots [1-4], and the core part of those tactile sensors is to detect ...
- **p. 1 / 1. Introduction - extractive body cue:** For example, a successfully commercialized sensor is the tactile sensor array from Pressure Profile Systems, which measures the normal pressure distribution over the robot fingertip, ...
- **p. 1 / 1. Introduction - extractive body cue:** The sensor has been applied to multiple commercialized robots, including the PR2 robot, and Barrett hands, and it successfully assisted common robotic tasks, such as ...
- **p. 1 / 1. Introduction - extractive body cue:** With the force measurement from the fingertip tactile sensors, a robot is much less likely to break delicate objects.
- **p. 2 / 1. Introduction - extractive body cue:** Those tasks, however, are still challenges for robots because they are not yet able to fully apply tactile sensing.
- **p. 2 / 1. Introduction - extractive body cue:** When the sensor surface is painted with small black markers, the motion of the markers provides information about both normal force and shear force.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Those tasks, however, are still challenges for robots because they are not yet able to fully apply tactile sensing. | contact-rich manipulation scene | body wording is the source claim |
| Observation / input | Robots need more than force feedback, while the existing sensors do not obtain enough tactile information for the robots. | tactile image/force, vision과 proprioceptive history | exact sensor/frame/preprocessing from PDF body |
| State / latent | Robots, need, more, force, feedback, while, existing, sensors, obtain, enough | contact geometry, force state 또는 latent dynamics | notation and tensor shape require body check |
| Output / action | initial, GelSight, frame, Frm0, when, noting, touch, low-pass | grasp/contact action, force command 또는 object motion | exact unit/frame/decoder require body check |
| Target outcome | slip/contact success and safe interaction | slip/contact success, force/pose error와 robustness | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | visual/tactile/proprioceptive contact history; body terms: Robots, need, more, force, feedback, while, existing, sensors, obtain, enough | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 9 (3.4. Algorithm for Measuring Marker Motion) |
| Decision / output variable | contact-aware action/force; body terms: past, decades, researchers, have, developed, many, different, tactile | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | contact prediction/control error; cue terms: simplified, version, only, record, gradient, entry, space, match | p. 8 (3.3. Algorithm for Measuring Shape), p. 8 (3.3. Algorithm for Measuring Shape) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 8 (3.3. Algorithm for Measuring Shape), p. 8 (3.3. Algorithm for Measuring Shape) |
| Success / guarantee | slip/contact success and safe interaction | p. 17 (5.2. Evaluation of Force Measurement), p. 17 (5.2. Evaluation of Force Measurement), p. 15 (5. Evaluation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** When the sensor surface is painted with small black markers, the motion of the markers provides information about both normal force and shear force.

## What the Paper Changes

PDF body contribution framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): In the past decades, researchers have developed many different tactile sensors for robots [1-4], and the core part of those tactile sensors is to detect the contact and contact force, ...

- **p. 2 / 1. Introduction - extractive body cue:** The first GelSight prototype was developed in 2009 by Johnson and Adelson [7].
- **p. 2 / 1. Introduction - extractive body cue:** We have developed sensors that are compact, yet have resolution far exceeding that of human skin.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | Figure 7. (a) when an indenter pressed on the GelSight surface in normal direction, the force is in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | Figure 8. The change of the marker displacement field with the increase of shear force. The degree of ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | Figure 9. The change of the marker displacement field and rotational angle with the increase of in-plane torque. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 18 | Additionally, it can detect slip by measuring the relative movement of the objects on the sensor. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

tactile writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1. Introduction), p. 2 (1. Introduction), p. 9 (3.4. Algorithm for Measuring Marker Motion), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 2 (1. Introduction), p. 9 (3.4. Algorithm for Measuring Marker Motion), p. 1 (1. Introduction), objective p. 8 (3.3. Algorithm for Measuring Shape), p. 8 (3.3. Algorithm for Measuring Shape).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Those tasks, however, are still challenges for robots because they are not yet able to fully apply tactile sensing. (p. 2, 1. Introduction).
- **Formulation-changing contribution:** Tactile sensing is an important mode for both human and robots to perceive the environment. (p. 1, 1. Introduction).
- **Assumption/failure evidence:** Sensors 2017, 17, 2762 18 of 21 truth qualitatively at all times, but the measurement at some entire contact sequences is worse than the others. (p. 18, 5.2. Evaluation of Force Measurement).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
