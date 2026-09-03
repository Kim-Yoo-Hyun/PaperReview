# RobotArena $\infty$: Scalable Robot Benchmarking via Real-to-Sim Translation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=0.875); canonical paper source: https://openreview.net/forum?id=OutljIofvS.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/245501. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Benchmarks and Datasets
- Tier: REFERENCE
- Tags: Robotics, Benchmark
- Official paper: https://openreview.net/forum?id=OutljIofvS
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/245501
- Code/Project: not identified
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=0.875)

## Why This Paper Is Here

Benchmarks and Datasets의 benchmark 문제를 이해하기 위해 읽는다. 본문은 While recent years have witnessed substantial progress in developing more capable and general robot policies, their evaluation remains a persistent challenge and lacks standardization.를 문제로 두고, RobotArena ∞: We introduce RobotArena ∞, a new benchmarking framework that scales robot evaluation by deploying policies in automatically constructed simulated environments and assessing them through automatic VLM score and online human ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** The pursuit of robot generalists, instructable agents capable of performing diverse tasks across diverse environments, demands rigorous and scalable evaluation.
- **p. 1 / ABSTRACT - extractive body cue:** Yet real-world testing of robot policies remains fundamentally constrained: it is laborintensive, slow, unsafe at scale, and difficult to reproduce.
- **p. 1 / ABSTRACT - extractive body cue:** As policies expand in scope and complexity, these barriers only intensify, since defining "success" in robotics often hinges on nuanced human judgments of execution quality.
- **p. 1 / ABSTRACT - extractive body cue:** We introduce RobotArena ∞, a new benchmarking framework that overcomes these challenges by shifting VLA evaluation into large-scale simulated environments augmented with online human feedback.
- **p. 1 / ABSTRACT - extractive body cue:** Leveraging advances in vision-language models, 2D-to-3D generative modeling, and differentiable rendering, our approach automatically converts video demonstrations from widely used robot datasets into simulated counterparts.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** While recent years have witnessed substantial progress in developing more capable and general robot policies, their evaluation remains a persistent challenge and lacks standardization.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Notable examples include the Amazon Picking Challenge Correll et al.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** RobotArena ∞: We introduce RobotArena ∞, a new benchmarking framework that scales robot evaluation by deploying policies in automatically constructed simulated environments and assessing them ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We present key evaluation results that reveal how current robot policies generalize-or fail to-under distribution shifts.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We introduce a fully automated reality-to-simulation translation pipeline built upon VLMs, 2D-to-3D generative models and differentiable rendering.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** RobotArena ∞is inspired by prior efforts to design scalable robot benchmarks, particularly the seminal contributions of BEHAVIOR (Li et al., 2024) and SIMPLER (Li et ...
- **p. 1 / ABSTRACT - extractive body cue:** We introduce RobotArena ∞, a new benchmarking framework that overcomes these challenges by shifting VLA evaluation into large-scale simulated environments augmented with online human feedback.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** First, vision-language-action (VLA) models are highly sensitive to dataset differences: performance drops when they are tested in environments outside their training distribution, indicating that current ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We first automatically translate real videos into corresponding simulation environments, building upon recent advances in vision-language models for scene understanding, 2D-to-3D generative models for asset ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Such manual oversight also raises concerns about consistency and fairness, particularly when baselines and new models are compared under slightly different conditions.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | First, vision-language-action (VLA) models are highly sensitive to dataset differences: performance drops when they are tested in environments outside their training distribution, indicating that current models are not true generalists ... | standardized observation, action, task state와 evaluation split | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| State/latent | First, vision-language-action, VLA, models, highly, sensitive, dataset, differences, performance, drops, when, they | benchmark state/goal와 method decision | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Output/action | We first automatically translate real videos into corresponding simulation environments, building upon recent advances in vision-language models for scene understanding, 2D-to-3D generative models for asset creation, and differentiable ... | policy/controller trajectory 또는 measured result | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (ABSTRACT) |
| Objective/outcome | However, the high cost for both organizers and participants means such events occur infrequently, often no more than once a year. | success metric, robustness, generalization과 reproducibility | p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** RobotArena ∞: We introduce RobotArena ∞, a new benchmarking framework that scales robot evaluation by deploying policies in automatically constructed simulated environments and assessing them ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We present key evaluation results that reveal how current robot policies generalize-or fail to-under distribution shifts.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We introduce a fully automated reality-to-simulation translation pipeline built upon VLMs, 2D-to-3D generative models and differentiable rendering.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** RobotArena ∞is inspired by prior efforts to design scalable robot benchmarks, particularly the seminal contributions of BEHAVIOR (Li et al., 2024) and SIMPLER (Li et ...
- **p. 1 / ABSTRACT - extractive body cue:** We introduce RobotArena ∞, a new benchmarking framework that overcomes these challenges by shifting VLA evaluation into large-scale simulated environments augmented with online human feedback.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 9: Policy evaluation results in RobotArena ∞ versus SIMPLER of Li et al. (2024c). 5.3 ROBOTARENA ∞VERSUS SIMPLER OF LI ET AL. (2024C) In ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: Left: Task progress scores computed by prompting Gemini 2.5 Pro with image frames and synchronized object and robot state sequences. Right: Example task ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 19: Example VLM-generated task evaluation curves on perturbed environments. Top: A successful pick-and-place execution-after the object lift the VLM score climbs steadily and correctly ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Embodiment/environment | The result is a continuously evolving, reproducible, and scalable benchmark for real-world-trained robot manipulation policies, addressing a critical missing capability in today's robotics landscape. | hardware/simulator version and reset protocol | p. 1 (ABSTRACT), p. 1 (ABSTRACT) |
| Dataset/benchmark | BEHAVIOR boasts an impressive manual effort of asset and environment creation, while SIMPLER reconstructs four real-world Bridge scenes and includes hand-designed reward functions. | role, split, size and leakage | p. 1 (ABSTRACT), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Metric | Figure 19: Example VLM-generated task evaluation curves on perturbed environments. Top: A successful pick-and-place execution-after the object lift the VLM score climbs steadily and correctly shows task completion. Bottom: An unsuccessf ... | definition, denominator, direction and uncertainty | p. 24 (Figure/Table caption), p. 22 (Figure/Table caption), p. 24 (Figure/Table caption) |
| Baseline/ablation | Such manual oversight also raises concerns about consistency and fairness, particularly when baselines and new models are compared under slightly different conditions. | fair input/data/compute/action matching | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 2 RELATED WORK - extractive body cue:** Intuitively, this focuses evaluation on the terminal phase of execution, where task completion (or failure) is most evident.
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 19: Example VLM-generated task evaluation curves on perturbed environments. Top: A successful pick-and-place execution-after the object lift the VLM score climbs steadily and correctly ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our benchmark is not without limitations.
- **p. 8 / 2 RELATED WORK - extractive body cue:** For example, in RH20TSim, RoboVLM (19.05%) achieves a substantially higher score than all other models, while X-VLA fails (0.00%).
- **p. 9 / 2 RELATED WORK - extractive body cue:** 6 LIMITATIONS AND FUTURE DIRECTIONS By leveraging recent advances in reality-to-simulation translation and crowdsourced evaluation, RobotArena ∞provides a scalable and extensible robot benchmark.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Second, even within the same environment, performance degrades under perturbations, showing that robustness to distribution shifts remains an open challenge.
- **p. 1 / ABSTRACT - extractive body cue:** Yet real-world testing of robot policies remains fundamentally constrained: it is laborintensive, slow, unsafe at scale, and difficult to reproduce.

## Why Read It

Benchmarks and Datasets의 benchmark 문제를 이해하기 위해 읽는다. 본문은 While recent years have witnessed substantial progress in developing more capable and general robot policies, their evaluation remains a persistent challenge and lacks standardization.를 문제로 두고, RobotArena ∞: We introduce RobotArena ∞, a new benchmarking framework that scales robot evaluation by deploying policies in automatically constructed simulated environments and assessing them through automatic VLM score and online human ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
