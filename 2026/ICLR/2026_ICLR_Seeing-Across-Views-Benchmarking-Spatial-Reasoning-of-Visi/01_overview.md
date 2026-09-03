# Seeing Across Views: Benchmarking Spatial Reasoning of Vision-Language Models in Robotic Scenes

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (50 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=jXDZJAfRZB.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/247464. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Vision-Language Model, Robotics, 3D Vision, Benchmark
- Official paper: https://openreview.net/forum?id=jXDZJAfRZB
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/247464
- Code/Project: not identified
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (50 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 By isolating failure modes in multi-view grounding rather than in isolated perception, MVRoboBench exposes the precise bottlenecks that future embodied AI systems must overcome.를 문제로 두고, To fill this gap, we introduce MV-RoboBench, a benchmark specifically designed to evaluate multiview spatial reasoning in robotic manipulation scenarios.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Vision-language models (VLMs) are essential to Embodied AI, enabling robots to perceive, reason, and act in complex environments.
- **p. 1 / ABSTRACT - extractive body cue:** They also serve as the foundation for the recent Vision-Language-Action (VLA) models.
- **p. 1 / ABSTRACT - extractive body cue:** Yet most evaluations of VLMs focus on single-view settings, leaving their ability to integrate multi-view information underexplored.
- **p. 1 / ABSTRACT - extractive body cue:** At the same time, multi-camera setups are increasingly standard in robotic platforms, as they provide complementary perspectives to mitigate occlusion and depth ambiguity.
- **p. 1 / ABSTRACT - extractive body cue:** Whether VLMs can effectively leverage such multi-view inputs for robotic reasoning therefore remains an open question.
- **p. 10 / 1 INTRODUCTION - extractive body cue:** By isolating failure modes in multi-view grounding rather than in isolated perception, MVRoboBench exposes the precise bottlenecks that future embodied AI systems must overcome.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Singleview inputs are inherently limited by challenges like occlusion, depth ambiguity, and restricted fields of view.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To fill this gap, we introduce MV-RoboBench, a benchmark specifically designed to evaluate multiview spatial reasoning in robotic manipulation scenarios.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 2 MV-ROBOBENCH 2.1 OVERVIEW We introduce MV-RoboBench, a benchmark designed to evaluate the multi-view reasoning capabilities of VLMs in robotic manipulation scenarios.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our key contributions are as follows: • We establish the first benchmark that integrates spatial and robotic reasoning with synchronized multi-view inputs in robotic manipulation ...
- **p. 23 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** This design enables rapid prototyping of spatial arrangements and provides a consistent interface for generating QA items that require reasoning about relative positions and geometric ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** For each subtask, task-specific templates were designed, and trained annotators constructed corresponding five-choice QA pairs from the curated image pairs.
- **p. 25 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** We then describe the four robotic subtasks, which extend spatial reasoning to manipulation scenarios: Action Planning, Step Execution, Trajectory Selection, and Affordance Recognition.
- **p. 32 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** They examine whether models can ground spatial understanding into action decisions, ranging from high-level planning to low-level execution, and from trajectory-level reasoning to grasp affordance ...
- **p. 25 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** The model is then asked to identify which candidate corresponds to the same object as the red box in the reference view.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Top: original inputs from left gripper, head, and right gripper cameras; Bottom: blurry synthesized view from interpolated extrinsics. "text": "Image context: Corresponding estimated depth map. | standardized observation, action, task state와 evaluation split | p. 19 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 10 (1 INTRODUCTION) |
| State/latent | Top, original, inputs, left, gripper, head, right, cameras, Bottom, blurry, synthesized, view | benchmark state/goal와 method decision | p. 19 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 10 (1 INTRODUCTION), p. 18 (C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS) |
| Output/action | Our results suggest that scaling perception alone is insufficient-models require explicit reasoning mechanisms to transform multi-view observations into actionable, embodied understanding. | policy/controller trajectory 또는 measured result | p. 10 (1 INTRODUCTION), p. 18 (C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS), p. 20 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| Objective/outcome | To provide models with explicit geometric constraints, we augmented each view with predicted depth maps. | success metric, robustness, generalization과 reproducibility | p. 18 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 20 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 22 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To fill this gap, we introduce MV-RoboBench, a benchmark specifically designed to evaluate multiview spatial reasoning in robotic manipulation scenarios.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 2 MV-ROBOBENCH 2.1 OVERVIEW We introduce MV-RoboBench, a benchmark designed to evaluate the multi-view reasoning capabilities of VLMs in robotic manipulation scenarios.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our key contributions are as follows: • We establish the first benchmark that integrates spatial and robotic reasoning with synchronized multi-view inputs in robotic manipulation ...
- **p. 23 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** This design enables rapid prototyping of spatial arrangements and provides a consistent interface for generating QA items that require reasoning about relative positions and geometric ...
- **p. 5 / 1 INTRODUCTION - extractive body cue:** For each subtask, task-specific templates were designed, and trained annotators constructed corresponding five-choice QA pairs from the curated image pairs.
- **p. 33 / Figure/Table caption - extractive body cue:** Table 7: Comparison of Single-View vs. Multi-View performance on selected subtasks. The values represent Multi-View accuracy, and values in parentheses indicate the change (∆) compared ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Accuracy of CoT-style augmentations on MV-RoboBench. ∆s and ∆r indicate changes on spatial and robotic tasks relative to the origin baseline. Variants: w ...
- **p. 37 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** This suggests that MV-RoboBench does not merely lower raw accuracy; it exposes non-trivial limitations in current vision-language models' spatial reasoning, and can serve as a ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 33 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Embodiment/environment | F.10 SUMMARY OF BENCHMARK CONSTRUCTION Taken together, the eight subtasks provide a comprehensive evaluation of spatial and robotic reasoning in multi-view environments. | hardware/simulator version and reset protocol | p. 32 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 18 (C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS) |
| Dataset/benchmark | The top row shows the original RGB images; the bottom row shows the corresponding MoGe-2 depth predictions (red indicates closer, blue indicates farther). spatial intelligence exhibited by models in general cognitive benchmarks ... | role, split, size and leakage | p. 32 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 18 (C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS), p. 20 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 21 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| Metric | Table 2: Evaluation on MV-RoboBench under a unified zero-shot prompt. denotes the best score and the second-best within each column. Qwen2.5-vl-72B leads among open-source models, while GPT-5 ranks highest overall but still ... | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 20 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| Baseline/ablation | Table 7: Comparison of Single-View vs. Multi-View performance on selected subtasks. The values represent Multi-View accuracy, and values in parentheses indicate the change (∆) compared to the Single-View baseline. Positive ∆indicates th ... | fair input/data/compute/action matching | p. 33 (Figure/Table caption), p. 33 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 32 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |

## Explicit Limitations and Failure Boundary

- **p. 36 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** GPT-5 often prefers grasp lines or trajectories that look visually neat (e.g., centered on the visible surface) but would be unstable or collision-prone for a ...
- **p. 49 / Figure/Table caption - extractive body cue:** Figure 30: Case Study 2: Instance-Level Correspondence Failure (Qwen2.5-VL-72B). The scene contains multiple instances of the same class (yellow peppers). The model correctly iden- tifies ...
- **p. 36 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** A second common failure mode involves incorrect reasoning about depth, occlusion, and 3D layout.
- **p. 37 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** Overall, these failures indicate that current VLMs still lack robust modeling of robotic affordances and physical constraints, especially when such reasoning must be carried out ...
- **p. 37 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** This suggests that MV-RoboBench does not merely lower raw accuracy; it exposes non-trivial limitations in current vision-language models' spatial reasoning, and can serve as a ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 7: Failure of object-centric synthesis (Trellis). Top: original inputs; Bottom: synthesized views that fail to capture the full scene.
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 8: Failure of LVSM scene interpolation. Top: original inputs from left gripper, head, and right gripper cameras; Bottom: blurry synthesized view from interpolated extrinsics. ...

## Why Read It

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 By isolating failure modes in multi-view grounding rather than in isolated perception, MVRoboBench exposes the precise bottlenecks that future embodied AI systems must overcome.를 문제로 두고, To fill this gap, we introduce MV-RoboBench, a benchmark specifically designed to evaluate multiview spatial reasoning in robotic manipulation scenarios.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 10 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 10 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 25 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
