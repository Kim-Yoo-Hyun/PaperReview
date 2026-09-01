# Problem - Learning Humanoid Standing-up Control across Diverse Postures

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p064.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p064.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): Our proposed RL. framework addresses these limitations by achieving posture adaptivity and real-world deployability without predefined motions, enabling smooth, stable, and robust standing-up across a wide range of laboratory and ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Standing with the potential for Toco-maniputation systems, such as fall recovery.
- **p. 1 / Abstract - extractive PDF cue:** Existing approaches are cither limited to simulations that overlook hardware constraints or rely on predefined ground-specific motion trajectories, failing to ‘up across postures in real~ ...
- **p. 1 / Abstract - extractive PDF cue:** To bridge this gap, we present HOST (Humanoid Standing-up Control), a reinforcement learning framework that learns standing-up control from scratch, enabling robust sim= to-real transfer ...
- **p. 1 / Abstract - extractive PDF cue:** raining on diverse simulated ter ensure successful real-world deployment, we constrain the motion with smoothness regularization and implicit motion speed bound to alleviate oscillatory and ...
- **p. 1 / Abstract - extractive PDF cue:** After simulation-based training, the learned control
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Our proposed RL. framework addresses these limitations by achieving posture adaptivity and real-world deployability without predefined motions, enabling smooth, stable, and robust standing-up across a ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** ‘TABLE I: Comparison with existing methods on standing-up contol

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Our proposed RL. framework addresses these limitations by achieving posture adaptivity and real-world deployability without predefined motions, enabling smooth, stable, and robust ... | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | postures, PD controllers, observation and action spaces. | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF |
| State / latent | postures, controllers, observation, action, spaces, lower, bounds, vertical, force, bound | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | Curriculum, Setup, adjustment, condition, consistent, vertical, force, action | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: postures, controllers, observation, action, spaces, lower, bounds, vertical, force, bound | p. 13 (B. More Implementation Details), p. 12 (B. More Implementation Details), p. 12 (B. More Implementation Details) |
| Decision / output variable | joint/whole-body action; body terms: enable, postureadaptive, motion, beyond, ground, introduce, multiple, terrains | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 12 (B. More Implementation Details) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: make, following, adjustment, algorithm, more, strict, constraints, joint | p. 13 (B. More Implementation Details) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 12 (B. More Implementation Details), p. 12 (B. More Implementation Details), p. 13 (B. More Implementation Details) |
| Success / guarantee | motion/task success and recovery | p. 6 (B. Main Results), p. 6 (B. Main Results), p. 8 (A. Main Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** ‘TABLE I: Comparison with existing methods on standing-up contol

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 12 (B. More Implementation Details), p. 12 (B. More Implementation Details), p. 13 (B. More Implementation Details)): To enable postureadaptive motion beyond the ground, we introduce multiple terrains for training and a vertical pull force during the initial stages to facilitate exploration, Given the multiple stages of ...

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** We overview the real-world performance of our controllers in Fg. / and summarize our core contributions as follows:
- **p. 12 / B. More Implementation Details - extractive PDF cue:** Our PPO implementation follows the framework outlined in [39]. ‘The actor network consists of 4 3-layer MLP with hidden dimensions [512, 256, 128], while each ...
- **p. 12 / B. More Implementation Details - extractive PDF cue:** We present the complete set of ward functions and their detailed descriptions in Tulble V1 Several regularization reward terms are adapted from prior work [21, ...
- **p. 13 / B. More Implementation Details - extractive PDF cue:** During the hardware deployment, the stiffness of hip and knee joints are amplified to 1.5 times than the simulation ones, similar to G1, We present ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | Without the proposed force curriculum, the robot fails to stand up on all terrains except the platform, as ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | We further tested our controllers on a 15° slippery slope, simulating challenging real-world conditions such as unstable surfaces. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Motion oscillations are observed in all scenes without smoothness regularization, often leading to standing-up failures, In contrast, our ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Our proposed framework, HOST, advances humanoid standing-up control by addressing the limitations of existing methods, which either neglect ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 13 (B. More Implementation Details), p. 12 (B. More Implementation Details), p. 12 (B. More Implementation Details), p. 13 (B. More Implementation Details). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 13 (B. More Implementation Details), p. 12 (B. More Implementation Details), p. 12 (B. More Implementation Details), p. 13 (B. More Implementation Details), objective p. 13 (B. More Implementation Details).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
