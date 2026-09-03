# Problem - NaVILA: Legged Robot Vision-Language-Action Model for Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p018.html; PDF retrieval source: https://arxiv.org/pdf/2412.04453. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): We construct a height map from raw LiDAR point clouds and introduce randomization to bridge the sim-to-real gap.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** This paper proposes to solve the problem of Visionand-Language Navigation with legged robots, which not only provides a flexible way for humans to command but ...
- **p. 1 / Abstract - extractive body cue:** However, it is non-trivial to translate human language
- **p. 1 / Abstract - extractive body cue:** We propose NaVILA, a 2-level framework that unifies a Vision-LanguageAction model (VLA) with locomotion skills.
- **p. 1 / Abstract - extractive body cue:** Instead of directly predicting low-level actions from VLA, NaVILA first generates mid-level actions with spatial information in the form of language, (e.g., "moving forward 75cm"), ...
- **p. 1 / Abstract - extractive body cue:** NaVILA substantially.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We construct a height map from raw LiDAR point clouds and introduce randomization to bridge the sim-to-real gap.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To better simulate the challenges of locomotion navigation in VLN, we introduce a new benchmark, VLN-CE-Isaac, using Isaac Sim.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We construct a height map from raw LiDAR point clouds and introduce randomization to bridge the sim-to-real gap. | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | Inspired by the recent progress on VLM [10, 11] for spatial location and distance reasoning, we propose NaVILA, a twolevel framework for ... | proprioception, terrain/perception observation과 velocity command | exact sensor/frame/preprocessing from PDF body |
| State / latent | Inspired, recent, progress, VLM, spatial, location, distance, reasoning, NaVILA, twolevel | body/contact state, foothold 또는 behavior mode | notation and tensor shape require body check |
| Output / action | advantages, framework, three-fold, decoupling, low-level, execution, VLAs, same | joint target, torque, footstep 또는 locomotion action | exact unit/frame/decoder require body check |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: Inspired, recent, progress, VLM, spatial, location, distance, reasoning, NaVILA, twolevel | p. 2 (I. INTRODUCTION), p. 3 (II. METHOD), p. 2 (I. INTRODUCTION) |
| Decision / output variable | joint action/torque/footstep; body terms: better, simulate, challenges, locomotion, navigation, VLN, introduce, benchmark | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (II. METHOD) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: right, image, preprocessed, height, values, clipped, sensor, constraints | p. 5 (II. METHOD), p. 5 (II. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (II. METHOD), p. 3 (II. METHOD), p. 3 (II. METHOD) |
| Success / guarantee | progress, balance and terrain robustness | p. 6 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS), p. 7 (III. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** To better simulate the challenges of locomotion navigation in VLN, we introduce a new benchmark, VLN-CE-Isaac, using Isaac Sim.

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (II. METHOD), p. 3 (II. METHOD), p. 4 (II. METHOD)): To better simulate the challenges of locomotion navigation in VLN, we introduce a new benchmark, VLN-CE-Isaac, using Isaac Sim.

- **p. 2 / I. INTRODUCTION - extractive body cue:** Inspired by the recent progress on VLM [10, 11] for spatial location and distance reasoning, we propose NaVILA, a twolevel framework for legged robot VLN: ...
- **p. 3 / II. METHOD - extractive body cue:** VILA consists of three main components: a vision encoder, a projector, and an LLM.
- **p. 3 / II. METHOD - extractive body cue:** To address this challenge, we opt for image-based vision-language models in our approach.
- **p. 4 / II. METHOD - extractive body cue:** This flexibility allows us to enhance generalizability for navigation.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | While NaVILA demonstrates strong performance, it fails in some real-world cases (see Appx. | reported limitation/failure wording; scope must be verified |
| body cue at p. 17 | Fig. 12: Obstacle avoidance screenshots. Locomotion policy can ensure collision-free in the face of high grass, certain transparent ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | To overcome this limitation, we introduce a new benchmark VLN-CE-Isaac built on Isaac Sim. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | As shown in Table V, our low-level policy outperforms ROA in all three metrics, particularly achieving a significantly ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (I. INTRODUCTION), p. 3 (II. METHOD), p. 2 (I. INTRODUCTION), p. 5 (II. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 2 (I. INTRODUCTION), p. 3 (II. METHOD), p. 2 (I. INTRODUCTION), p. 5 (II. METHOD), objective p. 5 (II. METHOD), p. 5 (II. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** To better simulate the challenges of locomotion navigation in VLN, we introduce a new benchmark, VLN-CE-Isaac, using Isaac Sim. (p. 2, I. INTRODUCTION).
- **Formulation-changing contribution:** To better simulate the challenges of locomotion navigation in VLN, we introduce a new benchmark, VLN-CE-Isaac, using Isaac Sim. (p. 2, I. INTRODUCTION).
- **Assumption/failure evidence:** While NaVILA demonstrates strong performance, it fails in some real-world cases (see Appx. (p. 9, V. CONCLUSION AND LIMITATIONS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
