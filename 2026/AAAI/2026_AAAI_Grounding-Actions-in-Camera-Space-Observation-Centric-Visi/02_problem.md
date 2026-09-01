# Problem - Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ojs.aaai.org/index.php/AAAI/article/view/38947; PDF retrieval source: https://ojs.aaai.org/index.php/AAAI/article/view/38947. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): This implicitly requires the model to reconstruct or reason about consistent 3D actions from limited 2D observationsa fundamentally ill-posed challenge when only single- or dual-view inputs are available.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models frequently encounter challenges in generalizing to real-world environments due to inherent discrepancies between observation and action spaces.
- **p. 1 / Abstract - extractive body cue:** Although training data are collected from diverse camera perspectives, the models typically predict end-effector poses within the robot base coordinate frame, resulting in spatial inconsistencies.
- **p. 1 / Abstract - extractive body cue:** To mitigate this limitation, we introduce the Observation-Centric VLA (OC-VLA) framework, which grounds action predictions directly in the camera observation space.
- **p. 1 / Abstract - extractive body cue:** Leveraging the camera's extrinsic calibration matrix, OC-VLA transforms end-effector poses from the robot base coordinate system into the camera coordinate system, thereby unifying prediction targets ...
- **p. 1 / Abstract - extractive body cue:** This lightweight, plug-and-play strategy ensures robust alignment between perception and action, substantially improving model resilience to camera viewpoint variations.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This implicitly requires the model to reconstruct or reason about consistent 3D actions from limited 2D observationsa fundamentally ill-posed challenge when only single- or dual-view ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Although this paradigm has achieved impressive performance across a variety of benchmarks, it remains fundamentally constrained by the intrinsic limitations of the robotics domain-namely, the ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This implicitly requires the model to reconstruct or reason about consistent 3D actions from limited 2D observationsa fundamentally ill-posed challenge when only ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | OC-VLA transforms the end effector pose whether defined in a discrete or continuous action space from the robot base coordinate to the ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | OC-VLA, transforms, effector, pose, whether, defined, discrete, continuous, action, space | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Following, paradigm, adopt, lightweight, VLA, model, evaluation, demonstrated | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: OC-VLA, transforms, effector, pose, whether, defined, discrete, continuous, action, space | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (III. METHOD) |
| Decision / output variable | action, pose, option or chunk a; body terms: address, issues, novel, paradigm, decouples, end-effector, action, robot | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | policy/action modeling objective; cue terms: Meanwhile, given, end-effector, pose, Pworld, robot, Pcam, TPworld | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Success / guarantee | instruction-conditioned task success | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Although this paradigm has achieved impressive performance across a variety of benchmarks, it remains fundamentally constrained by the intrinsic limitations of the robotics domain-namely, the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** By transforming end-effector actions from the robot base coordinate to the third-person camera coordinate, OC-VLA aligns action predictions with visual observations across diverse viewpoints, enabling ...

## What the Paper Changes

PDF contribution framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD)): To address these issues, we propose a novel paradigm that decouples the end-effector action from the robot base coordinate system and instead predicts actions directly in the third-person camera coordinate ...

- **p. 1 / I. INTRODUCTION - extractive body cue:** Notably, our method exhibits markedly improved adaptability to previously unseen camera viewarXiv:2508.13103v1 [cs.RO] 18 Aug 2025
- **p. 2 / I. INTRODUCTION - extractive body cue:** We introduce the Observation-Centric VLA (OC-VLA) framework.
- **p. 3 / III. METHOD - extractive body cue:** Different from previous end-effector action prediction, the predicted action in our method is in the camera space.
- **p. 3 / III. METHOD - extractive body cue:** Based on the baseline architecture, we implement a variant specifically designed for discrete action prediction or continuous action prediction.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Fig. 5. A qualitative comparison in real-robot experiments. Failures are highlighted with red circles. the same data. This ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | Fig. 1. We introduce the Observation-Centric VLA (OC-VLA) framework. By transforming end-effector actions from the robot base coordinate ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | This diversity makes it an ideal choice for evaluating the generalizability and robustness of our observationcentric action prediction ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | In addition to language and image tokens, we concatenate the current timestep and the noise-perturbed action as inputs ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (III. METHOD), p. 3 (III. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (III. METHOD), p. 3 (III. METHOD), objective p. 3 (III. METHOD), p. 3 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
