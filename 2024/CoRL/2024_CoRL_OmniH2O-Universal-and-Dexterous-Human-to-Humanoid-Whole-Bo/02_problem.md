# Problem - OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=oL1WEZQal8; PDF retrieval source: https://arxiv.org/pdf/2406.08858. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 2 (1 Introduction), p. 5 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): However, due to the delay and inaccuracy of RGB-based pose estimation and the requirement for global linear velocity estimation, H2O [3] requires MoCap during test time, only supports simple mobility ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We present OmniH2O (Omni Human-to-Humanoid), a learning-based system for whole-body humanoid teleoperation and autonomy.
- **p. 1 / Abstract - extractive body cue:** Using kinematic pose as a universal control interface, OmniH2O enables various ways for a human to control a full-sized humanoid with dexterous hands, including using ...
- **p. 1 / Abstract - extractive body cue:** OmniH2O also enables full autonomy by learning from teleoperated demonstrations or integrating with frontier models such as GPT-4o.
- **p. 1 / Abstract - extractive body cue:** OmniH2O demonstrates versatility and dexterity in various real-world whole-body tasks through teleoperation or autonomy, such as playing multiple sports, moving and manipulating objects, and interacting ...
- **p. 1 / Abstract - extractive body cue:** We develop an RL-based sim-to-real pipeline, which involves large-scale retargeting and augmentation of human motion datasets, learning a real-world deployable policy with sparse sensor input ...
- **p. 3 / 1 Introduction - extractive body cue:** However, due to the delay and inaccuracy of RGB-based pose estimation and the requirement for global linear velocity estimation, H2O [3] requires MoCap during test ...
- **p. 2 / 1 Introduction - extractive body cue:** Controlling humanoid robots is a long-standing robotic problem due to their high degree-of-freedom (DoF) and lack of self-stabilization [16, 17].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, due to the delay and inaccuracy of RGB-based pose estimation and the requirement for global linear velocity estimation, H2O [3] requires ... | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | We design our learning from demonstration policy to be πLfD(ˆpSparse-lfd t:t+ϕ /It), where πLfD outputs ϕ frames of motion goals given the ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF body |
| State / latent | design, learning, demonstration, policy, LfD, pSparse-lfd, where, outputs, frames, motion | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | proprioception, student, policy, sp-real, dt-25, root, t-25, gt-25 | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: design, learning, demonstration, policy, LfD, pSparse-lfd, where, outputs, frames, motion | p. 8 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction) |
| Decision / output variable | joint/whole-body action; body terms: conclusion, contributions, follows, pipeline, train, robust, humanoid, control | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: apply, Proximal, Policy, Optimization, algorithm, PPO, maximize, cumulative | p. 5 (1 Introduction), p. 2 (1 Introduction), p. 8 (1 Introduction), p. 8 (1 Introduction), p. 4 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (1 Introduction), p. 5 (1 Introduction), p. 1 (Abstract) |
| Success / guarantee | motion/task success and recovery | p. 8 (1 Introduction), p. 8 (1 Introduction), p. 21 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive body cue:** Controlling humanoid robots is a long-standing robotic problem due to their high degree-of-freedom (DoF) and lack of self-stabilization [16, 17].
- **p. 5 / 1 Introduction - extractive body cue:** In simulation, we evaluate on the retargeted AMASS dataset with augmented motions ˆ Q (14k sequences); in real-world, we test on 20 standing sequences due ...
- **p. 2 / 1 Introduction - extractive body cue:** However, whole-body control of a full-sized humanoid robot is challenging [6], with many existing works focusing only on the lower body [7, 8, 9, 10, ...
- **p. 3 / 1 Introduction - extractive body cue:** One major challenge within the robotics community is the limited number of publicly available datasets compared to those for language and vision tasks [40].

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction), p. 7 (1 Introduction)): In conclusion, our contributions are as follows: (1) We propose a pipeline to train a robust humanoid control policy that supports whole-body dexterous loco-manipulation with a universal interface that enables ...

- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose OmniH2O, a learning-based system for whole-body humanoid teleoperation and autonomy.
- **p. 4 / 1 Introduction - extractive body cue:** To encourage standing still and taking large steps during locomotion, we propose a key reward function max feet height for each step.
- **p. 3 / 1 Introduction - extractive body cue:** By contrast, OmniH2O enables high-precision dexterous loco-manipulation indoors and in the wild.
- **p. 7 / 1 Introduction - extractive body cue:** By linking πOmniH2O with a pretrained text to motion generative model (MDM) [57], it enables controlling the humanoid via verbal instructions.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Another limitation is safety; although the OmniH2O policy has shown great robustness, we do not have guarantees or ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | 5 Limitations and Future Work Summary. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | 2 Unable to finish the real-world test due to falling on the ground. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | OmniH2O demonstrates great robustness under disturbances and unstructured terrains. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 8 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction), p. 6 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (1 Introduction), p. 2 (1 Introduction), p. 5 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), interface p. 8 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction), p. 6 (1 Introduction), objective p. 5 (1 Introduction), p. 2 (1 Introduction), p. 8 (1 Introduction), p. 8 (1 Introduction), p. 4 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (25 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Controlling humanoid robots is a long-standing robotic problem due to their high degree-of-freedom (DoF) and lack of self-stabilization [16, 17]. (p. 2, 1 Introduction).
- **Formulation-changing contribution:** In conclusion, our contributions are as follows: (1) We propose a pipeline to train a robust humanoid control policy that supports whole-body dexterous loco-manipulation with a universal interface that enables ... (p. 2, 1 Introduction).
- **Assumption/failure evidence:** Another limitation is safety; although the OmniH2O policy has shown great robustness, we do not have guarantees or safety checks for extreme disturbances or out-of-distribution motion goals (e.g., large discontinuity ... (p. 8, 1 Introduction).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
