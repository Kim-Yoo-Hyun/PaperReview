# Problem - VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/He_VIRAL_Visual_Sim-to-Real_at_Scale_for_Humanoid_Loco-Manipulation_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/He_VIRAL_Visual_Sim-to-Real_at_Scale_for_Humanoid_Loco-Manipulation_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): Yet, despite rapid progress in hardware and control, current humanoids have delivered limited real, sustained productivity outside of carefully engineered demos [21].

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** A key barrier to the real-world deployment of humanoid robots is the lack of autonomous loco-manipulation skills.
- **p. 1 / Abstract - extractive body cue:** We introduce VIRAL, a visual sim-to-real framework that learns humanoid loco-manipulation entirely in simulation and deploys it zero-shot to real hardware.
- **p. 1 / Abstract - extractive body cue:** VIRAL follows a teacher-student design: a privileged RL teacher, operating on full state, learns long-horizon loco-manipulation using a delta action space and reference state initialization.
- **p. 1 / Abstract - extractive body cue:** A vision-based student policy is then distilled from the teacher via large-scale simulation with tiled rendering, trained with a mixture of online DAgger and behavior ...
- **p. 1 / Abstract - extractive body cue:** We find that compute scale is critical: scaling simulation to tens of GPUs (up to 64) makes both teacher and student training reliable, while low-compute ...
- **p. 1 / 1. Introduction - extractive body cue:** Yet, despite rapid progress in hardware and control, current humanoids have delivered limited real, sustained productivity outside of carefully engineered demos [21].
- **p. 2 / 1. Introduction - extractive body cue:** In other words, if we treat humanoid mobile manipulation as "just another data problem," the required scale may be prohibitively expensive in practice.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Yet, despite rapid progress in hardware and control, current humanoids have delivered limited real, sustained productivity outside of carefully engineered demos [21]. | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | Phase 1: In simulation, a privileged RL teacher policy ωteacher receives full-state proprioception and exteroception of the task information and outputs WBC ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF body |
| State / latent | Phase, simulation, privileged, teacher, policy, receives, full-state, proprioception, exteroception, task | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | Teacher, Action, Privileged, Exteroception, Proprioception, Sim-to-Real, Student, Policy | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: Phase, simulation, privileged, teacher, policy, receives, full-state, proprioception, exteroception, task | p. 2 (1. Introduction), p. 3 (2.1. Key Elements of Teacher Training), p. 2 (1. Introduction) |
| Decision / output variable | joint/whole-body action; body terms: Proprioception, consists, oprop-priv, finger, where, base, linear, angular | p. 3 (2.1. Key Elements of Teacher Training), p. 2 (1. Introduction) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: Therefore, define, four, rewards, Full, reward, definitions, provided | p. 4 (2.2. Key Elements of Student Training), p. 3 (2.1. Key Elements of Teacher Training) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (2.1. Key Elements of Teacher Training), p. 4 (2.1. Key Elements of Teacher Training), p. 4 (2.1. Key Elements of Teacher Training) |
| Success / guarantee | motion/task success and recovery | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 6 (3.1. Robustness) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** In other words, if we treat humanoid mobile manipulation as "just another data problem," the required scale may be prohibitively expensive in practice.
- **p. 2 / 1. Introduction - extractive body cue:** In real-world experiments, VIRAL shows not only the robustness of the high success rate that is near the human expert teleoperation performance, but also generalization ...

## What the Paper Changes

PDF body contribution framing (p. 3 (2.1. Key Elements of Teacher Training), p. 2 (1. Introduction)): Proprioception consists of oprop-priv t = [vt, ωt, gt, at→1, qt, ˙qt, f finger t ] where vt, ωt are base linear and angular velocities, gt is base projected gravity, ...

- **p. 2 / 1. Introduction - extractive body cue:** Our goal is not to propose yet another novel RL or sim-to-real algorithm, but to provide a technical recipe on the full stack required to ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | Note that VIRAL framework does not have designs overfitting to specific WBC policy, and can be extended to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | With a stable and robust WBC policy as an API layer, the action space of VIRAL policy is ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Visual randomization on image, lighting, material, and camera-extrinsics randomization for sim-to-real robustness. | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | The distinction between DAgger and BC lies solely in the source of observations: teacher rollouts provide clean, near-optimal ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1. Introduction), p. 3 (2.1. Key Elements of Teacher Training), p. 2 (1. Introduction), p. 3 (2.1. Key Elements of Teacher Training). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 3 (2.1. Key Elements of Teacher Training), p. 2 (1. Introduction), p. 3 (2.1. Key Elements of Teacher Training), objective p. 4 (2.2. Key Elements of Student Training), p. 3 (2.1. Key Elements of Teacher Training).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** In other words, if we treat humanoid mobile manipulation as "just another data problem," the required scale may be prohibitively expensive in practice. (p. 2, 1. Introduction).
- **Formulation-changing contribution:** Our goal is not to propose yet another novel RL or sim-to-real algorithm, but to provide a technical recipe on the full stack required to make RGBbased humanoid loco-manipulation work ... (p. 2, 1. Introduction).
- **Assumption/failure evidence:** We find that compute scale is critical: scaling simulation to tens of GPUs (up to 64) makes both teacher and student training reliable, while low-compute regimes often fail. (p. 1, Abstract).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
