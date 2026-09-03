# Problem - SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (39 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://research.nvidia.com/labs/dair/publication/sonic2026/; PDF retrieval source: https://research.nvidia.com/labs/dair/publication/sonic2026/. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): These foundation models have shown a consistent pattern: scale unlocks emergent capabilities, generalization, and robustness that smaller models cannot achieve [7-9].

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Despite the rise of billion-parameter foundation models trained across thousands of graphical processing units (GPUs), similar scaling gains have not been shown for humanoid control.
- **p. 1 / Abstract - extractive body cue:** Current neural controllers for humanoids remain modest in size, target a limited set of behaviors, and are trained on a handful of GPUs.
- **p. 1 / Abstract - extractive body cue:** We show that scaling model capacity, data, and compute yields a generalist humanoid controller capable of natural, robust whole-body movements.
- **p. 1 / Abstract - extractive body cue:** We position motion tracking as a scalable task for humanoid control, leveraging dense supervision from diverse motion-capture data to acquire human motion priors without manual ...
- **p. 1 / Abstract - extractive body cue:** We build a foundation model for motion tracking by scaling along three axes: network size (1.2M to 42M parameters), dataset volume (100M+ frames from 700 ...
- **p. 1 / 1. Introduction - extractive body cue:** These foundation models have shown a consistent pattern: scale unlocks emergent capabilities, generalization, and robustness that smaller models cannot achieve [7-9].
- **p. 1 / 1. Introduction - extractive body cue:** Each new capability demands redesigned rewards and objectives, making scaling up difficult.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | These foundation models have shown a consistent pattern: scale unlocks emergent capabilities, generalization, and robustness that smaller models cannot achieve [7-9]. | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | Notably, when the input command is human motion 𝑔ℎ, the encoder-decoder acts as a retargeting pipeline from human to robot motion, and ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF body |
| State / latent | Notably, when, input, command, human, motion, encoder-decoder, acts, retargeting, pipeline | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | context, keyframes, capture, historical, robot, states, joint, positions | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: Notably, when, input, command, human, motion, encoder-decoder, acts, retargeting, pipeline | p. 15 (3.2. Universal Humanoid Motion Tracking), p. 14 (3.2. Universal Humanoid Motion Tracking), p. 16 (3.3. Generative Kinematic Motion Planner) |
| Decision / output variable | joint/whole-body action; body terms: Supersizing, mOtion, tracking, Natural, humanoId, Control, SONIC, framework | p. 3 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: defined, reward, combining, tracking, term, minimizes, root, body-link | p. 16 (3.2. Universal Humanoid Motion Tracking), p. 15 (3.2. Universal Humanoid Motion Tracking), p. 15 (3.2. Universal Humanoid Motion Tracking), p. 16 (3.2. Universal Humanoid Motion Tracking), p. 17 (3.3. Generative Kinematic Motion Planner), p. 17 (3.3. Generative Kinematic Motion Planner) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 17 (3.3. Generative Kinematic Motion Planner), p. 16 (3.2. Universal Humanoid Motion Tracking), p. 15 (3.2. Universal Humanoid Motion Tracking) |
| Success / guarantee | motion/task success and recovery | p. 4 (2.1. Motion Tracking), p. 4 (2.1. Motion Tracking), p. 11 (2.5. Foundation-Model-Driven Loco-manipulation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** Each new capability demands redesigned rewards and objectives, making scaling up difficult.
- **p. 2 / 1. Introduction - extractive body cue:** In this work, we address both challenges by identifying motion tracking as the scalable foundational task for humanoid control.
- **p. 2 / 1. Introduction - extractive body cue:** Even if we identify a scalable objective that can learn diverse behaviors, a second challenge emerges: how do we support the diverse range of real-world ...

## What the Paper Changes

PDF body contribution framing (p. 3 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), p. 2 (1. Introduction), p. 15 (3.2. Universal Humanoid Motion Tracking)): We propose Supersizing mOtion tracking for Natural humanoId Control (SONIC), a framework that enables natural humanoid control across a wide range of applications (Movie S1).

- **p. 2 / 1. Introduction - extractive body cue:** In addition, we show how such a motion tracker can be applied to meaningful downstream tasks, and introduce two key contributions.
- **p. 3 / 1. Introduction - extractive body cue:** Third, we provide a comprehensive evaluation demonstrating humanoid control scaling trends, zero-shot transfer to unseen motions, robust simto-real deployment on physical humanoid robots, and successful ...
- **p. 2 / 1. Introduction - extractive body cue:** SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control Figure 1: SONIC enables diverse humanoid tasks through a universal control policy that handles diverse input ...
- **p. 15 / 3.2. Universal Humanoid Motion Tracking - extractive body cue:** Notably, when the input command is human motion 𝑔ℎ, the encoder-decoder acts as a retargeting pipeline from human to robot motion, and ℒrecon serves as ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | Our metric, similar to [29], captured the physically meaningful failure modes such as falling. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | Limitations include the lack of formal treatment of safety and energy efficiency for extended deployments. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | It also contrasts with task-specific reward engineering (for example, locomotion controllers such as OpenHomie [13]), where each behavior ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | After retargeting to the Unitree G1 using General Motion Retargeting (GMR) [54] and PyRoki [55], we filtered out ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 15 (3.2. Universal Humanoid Motion Tracking), p. 14 (3.2. Universal Humanoid Motion Tracking), p. 16 (3.3. Generative Kinematic Motion Planner), p. 16 (3.2. Universal Humanoid Motion Tracking). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 15 (3.2. Universal Humanoid Motion Tracking), p. 14 (3.2. Universal Humanoid Motion Tracking), p. 16 (3.3. Generative Kinematic Motion Planner), p. 16 (3.2. Universal Humanoid Motion Tracking), objective p. 16 (3.2. Universal Humanoid Motion Tracking), p. 15 (3.2. Universal Humanoid Motion Tracking), p. 15 (3.2. Universal Humanoid Motion Tracking), p. 16 (3.2. Universal Humanoid Motion Tracking), p. 17 (3.3. Generative Kinematic Motion Planner), p. 17 (3.3. Generative Kinematic Motion Planner).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (39 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Each new capability demands redesigned rewards and objectives, making scaling up difficult. (p. 1, 1. Introduction).
- **Formulation-changing contribution:** In addition, we show how such a motion tracker can be applied to meaningful downstream tasks, and introduce two key contributions. (p. 2, 1. Introduction).
- **Assumption/failure evidence:** Our metric, similar to [29], captured the physically meaningful failure modes such as falling. (p. 5, 2.1. Motion Tracking).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
