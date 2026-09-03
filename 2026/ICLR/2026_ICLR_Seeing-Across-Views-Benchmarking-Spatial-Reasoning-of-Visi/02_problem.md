# Problem - Seeing Across Views: Benchmarking Spatial Reasoning of Vision-Language Models in Robotic Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (50 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=jXDZJAfRZB; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247464. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 10 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 10 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): By isolating failure modes in multi-view grounding rather than in isolated perception, MVRoboBench exposes the precise bottlenecks that future embodied AI systems must overcome.

## PDF Body Digest

- **p. 1 / ABSTRACT - extractive body cue:** Vision-language models (VLMs) are essential to Embodied AI, enabling robots to perceive, reason, and act in complex environments.
- **p. 1 / ABSTRACT - extractive body cue:** They also serve as the foundation for the recent Vision-Language-Action (VLA) models.
- **p. 1 / ABSTRACT - extractive body cue:** Yet most evaluations of VLMs focus on single-view settings, leaving their ability to integrate multi-view information underexplored.
- **p. 1 / ABSTRACT - extractive body cue:** At the same time, multi-camera setups are increasingly standard in robotic platforms, as they provide complementary perspectives to mitigate occlusion and depth ambiguity.
- **p. 1 / ABSTRACT - extractive body cue:** Whether VLMs can effectively leverage such multi-view inputs for robotic reasoning therefore remains an open question.
- **p. 10 / 1 INTRODUCTION - extractive body cue:** By isolating failure modes in multi-view grounding rather than in isolated perception, MVRoboBench exposes the precise bottlenecks that future embodied AI systems must overcome.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Singleview inputs are inherently limited by challenges like occlusion, depth ambiguity, and restricted fields of view.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | By isolating failure modes in multi-view grounding rather than in isolated perception, MVRoboBench exposes the precise bottlenecks that future embodied AI systems ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | Top: original inputs from left gripper, head, and right gripper cameras; Bottom: blurry synthesized view from interpolated extrinsics. "text": "Image context: Corresponding ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF body |
| State / latent | Top, original, inputs, left, gripper, head, right, cameras, Bottom, blurry | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | While, effective, clean, object-level, inputs, they, proved, unsuitable | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: Top, original, inputs, left, gripper, head, right, cameras, Bottom, blurry | p. 19 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 10 (1 INTRODUCTION), p. 18 (C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS) |
| Decision / output variable | method trajectory/action; body terms: fill, introduce, MV-RoboBench, benchmark, specifically, designed, evaluate, multiview | p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: provide, models, explicit, geometric, constraints, augmented, view, predicted | p. 18 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 20 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 22 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 33 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 37 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 29 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 33 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 37 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| Success / guarantee | comparable score and protocol validity | p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 20 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Singleview inputs are inherently limited by challenges like occlusion, depth ambiguity, and restricted fields of view.
- **p. 10 / 1 INTRODUCTION - extractive body cue:** To address these challenges, specialized approaches (Cheng et al., 2024; Ma et al., 2025; Zhou et al., 2025; Fan et al., 2025; Liu et al., ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Multi-view observations, by contrast, offer complementary perspectives that help overcome these limitations.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** These findings highlight the unique challenges of multi-view reasoning in robotics and the need for specialized benchmarks like MV-RoboBench.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 23 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 5 (1 INTRODUCTION)): To fill this gap, we introduce MV-RoboBench, a benchmark specifically designed to evaluate multiview spatial reasoning in robotic manipulation scenarios.

- **p. 3 / 1 INTRODUCTION - extractive body cue:** 2 MV-ROBOBENCH 2.1 OVERVIEW We introduce MV-RoboBench, a benchmark designed to evaluate the multi-view reasoning capabilities of VLMs in robotic manipulation scenarios.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our key contributions are as follows: • We establish the first benchmark that integrates spatial and robotic reasoning with synchronized multi-view inputs in robotic manipulation ...
- **p. 23 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** This design enables rapid prototyping of spatial arrangements and provides a consistent interface for generating QA items that require reasoning about relative positions and geometric ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** For each subtask, task-specific templates were designed, and trained annotators constructed corresponding five-choice QA pairs from the curated image pairs.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 36 | GPT-5 often prefers grasp lines or trajectories that look visually neat (e.g., centered on the visible surface) but ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 49 | Figure 30: Case Study 2: Instance-Level Correspondence Failure (Qwen2.5-VL-72B). The scene contains multiple instances of the same class ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 36 | A second common failure mode involves incorrect reasoning about depth, occlusion, and 3D layout. | reported limitation/failure wording; scope must be verified |
| body cue at p. 37 | Overall, these failures indicate that current VLMs still lack robust modeling of robotic affordances and physical constraints, especially ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 19 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 10 (1 INTRODUCTION), p. 18 (C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS), p. 20 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 10 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 10 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), interface p. 19 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 10 (1 INTRODUCTION), p. 18 (C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS), p. 20 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), objective p. 18 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 20 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 22 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 33 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 37 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
