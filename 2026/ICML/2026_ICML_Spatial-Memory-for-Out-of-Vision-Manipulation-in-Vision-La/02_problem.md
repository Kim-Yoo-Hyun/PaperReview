# Problem - Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=5i888dLp8N; PDF retrieval source: https://openreview.net/pdf/95685162fa940bca32702d659b96eebf84138a75.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction)): Without a mechanism to maintain a persistent spatial representation of the scene, the perception-action loop becomes strictly viewdependent: when a target object is not observed, the model lacks the necessary ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We introduce SOMA, the Spatial memory framework for Out-of-Vision Manipulation in VisionLanguage-Action (VLA) models.
- **p. 1 / Abstract - extractive body cue:** Most existing VLAs implicitly assume that task-relevant objects are always visible, leading to brittle and reactive behaviors when targets fall outside the camera's field of ...
- **p. 1 / Abstract - extractive body cue:** SOMA addresses this limitation by equipping VLAs with a persistent, spatial memory constructed from multi-view observations acquired via a movable head camera, enabling reasoning beyond ...
- **p. 1 / Abstract - extractive body cue:** The framework consists of three components: Spatial Memory Construction for aggregating angular-wise observations into a unified spatial-semantic representation by scanning, Dynamic Memory Refinement for maintaining ...
- **p. 1 / Abstract - extractive body cue:** We evaluate SOMA on five self-designed challenging real-world OOV manipulation tasks, including multi-step and dualarm scenarios, where target objects are initially invisible.
- **p. 2 / 1. Introduction - extractive body cue:** Without a mechanism to maintain a persistent spatial representation of the scene, the perception-action loop becomes strictly viewdependent: when a target object is not observed, ...
- **p. 2 / 1. Introduction - extractive body cue:** Addressing this gap requires mechanisms that both acquire spatial evidence beyond the current view and retain it in a persistent scene representation.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Without a mechanism to maintain a persistent spatial representation of the scene, the perception-action loop becomes strictly viewdependent: when a target object ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | These systems typically extend large-scale pre-trained Multimodal Large Language Models (MLLMs) (Bjorck et al., 2025; Yang et al., 2025a) with an action ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | systems, typically, extend, large-scale, pre-trained, Multimodal, Large, Language, Models, MLLMs | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | Dynamic, Memory, Refinement, Instruction, Pick, pink, place, basket | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: systems, typically, extend, large-scale, pre-trained, Multimodal, Large, Language, Models, MLLMs | p. 1 (1. Introduction), p. 3 (3. Method), p. 4 (3.1. Spatial Memory Construction) |
| Decision / output variable | action, pose, option or chunk a; body terms: insights, introduce, SOMA, VLA, framework, out-of-vision, manipulation, equips | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method) |
| Objective / loss / cost | policy/action modeling objective; cue terms: New, observations, head, view, incorporated, update, through, Dynamic | p. 3 (3. Method), p. 4 (3.1. Spatial Memory Construction), p. 4 (3.1. Spatial Memory Construction), p. 5 (3.2. Dynamic Memory Refinement), p. 5 (3.2. Dynamic Memory Refinement) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.1. Spatial Memory Construction), p. 5 (3.2. Dynamic Memory Refinement), p. 5 (3.2. Dynamic Memory Refinement) |
| Success / guarantee | instruction-conditioned task success | p. 18 (Figure/Table caption), p. 7 (4.3. Real World Results), p. 6 (4.1. Benchmarks) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Addressing this gap requires mechanisms that both acquire spatial evidence beyond the current view and retain it in a persistent scene representation.
- **p. 1 / 1. Introduction - extractive body cue:** However, most existing VLAs are developed under fixedview tabletop manipulation setups, typically relying on a single static camera or a third-person viewpoint.
- **p. 1 / 1. Introduction - extractive body cue:** As a result, these models implicitly operate under a view-bound assumption-namely, that the object referenced in the instruction is visible within the robot's current camera ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 1 (1. Introduction), p. 1 (1. Introduction)): Based on these insights, we introduce SOMA, a VLA framework for out-of-vision manipulation that equips the robot with persistent spatial memory for reasoning and action.

- **p. 2 / 1. Introduction - extractive body cue:** In particular, integrating angular-wise observations into a coherent spatial-semantic memory enables globally consistent reasoning and effective manipulation even when task-relevant objects are temporarily out of ...
- **p. 3 / 3. Method - extractive body cue:** By maintaining a globally consistent spatial memory, SOMA enables robust reasoning and manipulation even when task-relevant objects lie outside the current field of view.
- **p. 1 / 1. Introduction - extractive body cue:** However, most existing VLAs are developed under fixedview tabletop manipulation setups, typically relying on a single static camera or a third-person viewpoint.
- **p. 1 / 1. Introduction - extractive body cue:** The development of VLAs have become a central direction in robotic action modeling research (Zhao et al., 2025; Chen et al., 2025c; Kim et al., ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 20 | Table 15. Failure mode analysis on the fully observable RoboCasa Tabletop GR1 simulation (50 sampled failures, 10 per ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 1 | Figure 1. Illustration of the Out-of-Vision (OOV) limitation in existing VLA models. Most VLAs rely on purely reactive ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | We propose SOMA, a spatial memory framework for VisionLanguage-Action models that addresses the fundamental limitation of view-bound perception ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 20 | Table 14. Failure mode analysis on real-world OOV tasks (25 sampled failed episodes, 5 per task). Failures predominantly ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1. Introduction), p. 3 (3. Method), p. 4 (3.1. Spatial Memory Construction), p. 6 (3.3. Contextual Memory Retrieval). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 1 (1. Introduction), p. 3 (3. Method), p. 4 (3.1. Spatial Memory Construction), p. 6 (3.3. Contextual Memory Retrieval), objective p. 3 (3. Method), p. 4 (3.1. Spatial Memory Construction), p. 4 (3.1. Spatial Memory Construction), p. 5 (3.2. Dynamic Memory Refinement), p. 5 (3.2. Dynamic Memory Refinement).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
