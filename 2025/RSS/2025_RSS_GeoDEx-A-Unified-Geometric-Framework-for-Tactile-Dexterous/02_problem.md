# Problem - GeoDEx: A Unified Geometric Framework for Tactile Dexterous and Extrinsic Manipulation under Force Uncertainty

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p057.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p057.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Iyrropucrion), p. 1 (Abstract), p. 2 (B. Utilizing Tactile Readings), p. 3 (B. Utilizing Tactile Readings), p. 2 (B. Utilizing Tactile Readings)): While force sensors can provide accurate force readings, physical limitations associated with ‘embedding the sensors into the robotic hands, as well as lack of high-resolution tactile information limit the use ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Sense of touch that allows robots to detect contact and measure interaction forces enables them to perform ‘challenging tasks such as grasping fragile objects or ...
- **p. 1 / Abstract - extractive body cue:** Tactile sensors in theory can equip the robots with such ‘capabilities.
- **p. 1 / Abstract - extractive body cue:** However, accuracy of the measured forces is not ‘on a par with those of the force sensors due to the potential bration challenges and noise.
- **p. 1 / Abstract - extractive body cue:** This has limited the values these sensors can offer in manipulation applications that require force ‘control.
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce GeoDEx, a unified estimation, planning, and control framework using geometric primitives such a plane, cone and ellipsoid, which enables dexterous ...
- **p. 1 / 1. Iyrropucrion - extractive body cue:** While force sensors can provide accurate force readings, physical limitations associated with ‘embedding the sensors into the robotic hands, as well as lack of high-resolution ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** Most Of the existing works focus on contact force and position planning and validate the method in simulation only [23, 25, 26], [27] performed hardware ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While force sensors can provide accurate force readings, physical limitations associated with ‘embedding the sensors into the robotic hands, as well as ... | contact-rich manipulation scene | body wording is the source claim |
| Observation / input | The interaction between the fingertips and the objects is measured using the tactile fingertips which output normal forces at the contact location. ... | tactile image/force, vision과 proprioceptive history | exact sensor/frame/preprocessing from PDF body |
| State / latent | interaction, between, fingertips, objects, measured, tactile, output, normal, forces, contact | contact geometry, force state 또는 latent dynamics | notation and tensor shape require body check |
| Output / action | Due, sensor, measurement, error, force, estimator, IL-B, improved | grasp/contact action, force command 또는 object motion | exact unit/frame/decoder require body check |
| Target outcome | slip/contact success and safe interaction | slip/contact success, force/pose error와 robustness | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | visual/tactile/proprioceptive contact history; body terms: interaction, between, fingertips, objects, measured, tactile, output, normal, forces, contact | p. 5 (B. Force Estimation), p. 2 (B. Utilizing Tactile Readings), p. 5 (B. Force Estimation) |
| Decision / output variable | contact-aware action/force; body terms: Through, various, experimental, while, relying, direct, inaccurate, noisy | p. 1 (Abstract), p. 2 (B. Utilizing Tactile Readings), p. 1 (Abstract) |
| Objective / loss / cost | contact prediction/control error; cue terms: Force, planning, extrinsic, manipulation, Given, intrinsic, contact, points | p. 2 (B. Utilizing Tactile Readings), p. 3 (B. Utilizing Tactile Readings), p. 3 (B. Utilizing Tactile Readings), p. 4 (B. Force Estimation), p. 4 (B. Force Estimation), p. 5 (B. Force Estimation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (B. Utilizing Tactile Readings), p. 4 (B. Force Estimation), p. 4 (B. Force Estimation) |
| Success / guarantee | slip/contact success and safe interaction | p. 8 (C. Hardware Results), p. 8 (C. Hardware Results), p. 9 (C. Hardware Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / Abstract - extractive body cue:** However, accuracy of the measured forces is not ‘on a par with those of the force sensors due to the potential bration challenges and noise.
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** Most Of the existing works focus on contact force and position planning and validate the method in simulation only [23, 25, 26], [27] performed hardware ...
- **p. 3 / B. Utilizing Tactile Readings - extractive body cue:** When extrinsic contacts are present, we can also assume there is a virtual sensor attached to the contact point that can measure force in the ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** In this section, we will first define the necessary concepts for our theoretical framework, and then use these concepts to address the problems of how ...

## What the Paper Changes

PDF body contribution framing (p. 1 (Abstract), p. 2 (B. Utilizing Tactile Readings), p. 1 (Abstract), p. 2 (B. Utilizing Tactile Readings), p. 3 (B. Force Estimation)): Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, our method enables successful grasping ...

- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** Our framework consists of three major components as shown in Fig.1: a force planner that generates robust plans for
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce GeoDEx, a unified estimation, planning, and control framework using geometric primitives such a plane, cone and ellipsoid, which enables dexterous ...
- **p. 2 / B. Utilizing Tactile Readings - extractive body cue:** We will end by describing the control architecture of our framework.
- **p. 3 / B. Force Estimation - extractive body cue:** Our projection allows changes to normal force magnitude and practically gives similar results as we will show in the experimental section,

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | For these failure cases, the main element at fault was the saturation of the tactile sensors of one ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | We can use this contact location, along with the object parameters to compute the ‘optimal force needed to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | The success rate along with the mean and standard ‘deviation ofthe force error at the contact points for ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | For the remaining failure case, the hysteresis of multiple taxels of the index finger created the illusion of ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

tactile writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (B. Force Estimation), p. 2 (B. Utilizing Tactile Readings), p. 5 (B. Force Estimation), p. 1 (A. State of Tactile Sensors). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Iyrropucrion), p. 1 (Abstract), p. 2 (B. Utilizing Tactile Readings), p. 3 (B. Utilizing Tactile Readings), p. 2 (B. Utilizing Tactile Readings), interface p. 5 (B. Force Estimation), p. 2 (B. Utilizing Tactile Readings), p. 5 (B. Force Estimation), p. 1 (A. State of Tactile Sensors), objective p. 2 (B. Utilizing Tactile Readings), p. 3 (B. Utilizing Tactile Readings), p. 3 (B. Utilizing Tactile Readings), p. 4 (B. Force Estimation), p. 4 (B. Force Estimation), p. 5 (B. Force Estimation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, accuracy of the measured forces is not ‘on a par with those of the force sensors due to the potential bration challenges and noise. (p. 1, Abstract).
- **Formulation-changing contribution:** Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, our method enables successful grasping ... (p. 1, Abstract).
- **Assumption/failure evidence:** Through various experimental results, we show that while relying on direct inaccurate and noisy force readings from tactile sensors results in unstable or failed manipulation, our method enables successful grasping ... (p. 1, Abstract).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
