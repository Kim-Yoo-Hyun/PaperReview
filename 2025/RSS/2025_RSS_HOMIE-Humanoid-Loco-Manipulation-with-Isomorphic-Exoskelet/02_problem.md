# Problem - HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p070.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p070.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (A. Teleoperation Systems), p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 3 (B. Whole-body Loco-Manipulation)): However, due to limitations in the accuracy, inference speed, and difficulty in handling occlusions of pose estimation, such approaches cannot guarantee rapid and accurate pose acquisition.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Generalizable humanoid loco-manipulation poses significant challenges, requiring coordinated whole-body control and precise, contact
- **p. 1 / Abstract - extractive body cue:** this paper introduces HOMIE, a semi-autonomous teleoperation and its affordability, with a price of just $500.
- **p. 1 / Abstract - extractive body cue:** The system is fully system that combines a reinforcement learning poliey for body open-source, demos and code can be found in our websit control mapped ...
- **p. 1 / Abstract - extractive body cue:** m-sensing gloves for hand control, forming I.
- **p. 1 / Abstract - extractive body cue:** ‘arm control, and mot ‘8 uniled cockpit to freely operate humas data flywheel.
- **p. 2 / A. Teleoperation Systems - extractive body cue:** However, due to limitations in the accuracy, inference speed, and difficulty in handling occlusions of pose estimation, such approaches cannot guarantee rapid and accurate pose ...
- **p. 1 / Abstract - extractive body cue:** However, the field currently faces a significant

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, due to limitations in the accuracy, inference speed, and difficulty in handling occlusions of pose estimation, such approaches cannot guarantee rapid ... | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | 1) Training Settings: ‘The observations of one step are defined as O, = [Cry tes dts des de» ei], Where Cy is ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF body |
| State / latent | Training, Settings, observations, step, defined, Cry, Where, command, body, angular | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | RL-based, training, framework, features, three, core, techrniques, upper-body | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: Training, Settings, observations, step, defined, Cry, Where, command, body, angular | p. 4 (B. Humanoid Whole-body Control), p. 4 (B. Humanoid Whole-body Control), p. 2 (Abstract) |
| Decision / output variable | joint/whole-body action; body terms: introduce, training, settings, three, techniques, framework, section, Unlike | p. 4 (B. Humanoid Whole-body Control), p. 2 (Abstract), p. 2 (Abstract) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: Given, symmetry, loss, reach, values, order, without, constraints | p. 7 (A. Humanoid Whole-body Control), p. 4 (B. Humanoid Whole-body Control), p. 5 (1 2001p), p. 5 (1 2001p), p. 6 (C. Hardware System Design), p. 7 (A. Humanoid Whole-body Control) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (A. Teleoperation Systems), p. 3 (A. Teleoperation Systems), p. 3 (A. Teleoperation Systems) |
| Success / guarantee | motion/task success and recovery | p. 8 (A. Humanoid Whole-body Control), p. 8 (A. Humanoid Whole-body Control), p. 7 (A. Humanoid Whole-body Control) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / Abstract - extractive body cue:** However, the field currently faces a significant
- **p. 1 / Abstract - extractive body cue:** Generalizable humanoid loco-manipulation poses significant challenges, requiring coordinated whole-body control and precise, contact
- **p. 2 / Abstract - extractive body cue:** dichotomy: reinforcement learning (RL)-trained locomotion policies excel at environmental adaptation but lack the interfaces needed for real-time, precise teleoperation [1, 2, 3, 4, 5, 6].
- **p. 3 / B. Whole-body Loco-Manipulation - extractive body cue:** Despite achieving impressive results, these methods still face several common limitations.

## What the Paper Changes

PDF body contribution framing (p. 4 (B. Humanoid Whole-body Control), p. 2 (Abstract), p. 2 (Abstract), p. 4 (A. System Overview), p. 3 (A. Teleoperation Systems)): We introduce the training settings and three key techniques of our framework in this section

- **p. 2 / Abstract - extractive body cue:** Unlike previous whole-body contro! methods that depend on motion priors derived from MoCap data [12], our framework eliminates this dependency, resulting in a more cfficient ...
- **p. 2 / Abstract - extractive body cue:** In responce, we introduce HOMIE, a semi-autonomous humanoid teleoperation system that integrates a RL policy for body control mapped to a pedal, an isomorphic exoskeleton ...
- **p. 4 / A. System Overview - extractive body cue:** 2, HOMIE consists of low-level policy Toco and an exoskeleton-based hardware system.
- **p. 3 / A. Teleoperation Systems - extractive body cue:** HOMIE is designed to combine all the advantages mentioned above, integrating isomorphic exoskeleton arms with a pair of novel motionsensing gloves.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Thus, our curriculum approach leads to better performance compared to rand, Although w/o cur does not use a ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | We design two additional algorithms w/o knee, which does not USE rinee described in Eq. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Infact, het ultimately does not achieve faster ‘convergence in height tracking compared to ours. | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Fig. 1: HOMIE empowers the humanoid robot to execute various loco-manipulation tasks in the real world. (2): Squatting ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (B. Humanoid Whole-body Control), p. 4 (B. Humanoid Whole-body Control), p. 2 (Abstract), p. 5 (C. Hardware System Design). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (A. Teleoperation Systems), p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 3 (B. Whole-body Loco-Manipulation), interface p. 4 (B. Humanoid Whole-body Control), p. 4 (B. Humanoid Whole-body Control), p. 2 (Abstract), p. 5 (C. Hardware System Design), objective p. 7 (A. Humanoid Whole-body Control), p. 4 (B. Humanoid Whole-body Control), p. 5 (1 2001p), p. 5 (1 2001p), p. 6 (C. Hardware System Design), p. 7 (A. Humanoid Whole-body Control).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, due to limitations in the accuracy, inference speed, and difficulty in handling occlusions of pose estimation, such approaches cannot guarantee rapid and accurate pose acquisition. (p. 2, A. Teleoperation Systems).
- **Formulation-changing contribution:** HOMIE is designed to combine all the advantages mentioned above, integrating isomorphic exoskeleton arms with a pair of novel motionsensing gloves. (p. 3, A. Teleoperation Systems).
- **Assumption/failure evidence:** However, due to limitations in the accuracy, inference speed, and difficulty in handling occlusions of pose estimation, such approaches cannot guarantee rapid and accurate pose acquisition. (p. 2, A. Teleoperation Systems).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
