# Generalizable Coarse-to-Fine Robot Manipulation via Language-Aligned 3D Keypoints

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=WXFfMLyB6y.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/244660. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, 3D Vision, Imitation Learning
- Official paper: https://openreview.net/forum?id=WXFfMLyB6y
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/244660
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 For simulation, we use GemBench (Garcia et al., 2025), a benchmark specifically designed to assess the generalization ability of multi-task language-conditioned policies across varying difficulty levels.를 문제로 두고, In real-world experiments, our method demonstrate strong generalization ability to novel tasks and object variations with only 10 demonstrations per task.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Hierarchical coarse-to-fine policy, where a coarse branch predicts a region of interest to guide a fine-grained action predictor, has demonstrated significant potential in robotic 3D ...
- **p. 1 / ABSTRACT - extractive body cue:** However, even augmented with pre-trained models, these hierarchical policies still suffer from generalization issues.
- **p. 1 / ABSTRACT - extractive body cue:** To enhance generalization to novel instructions and environment variations, we propose Coarse-to-fine Language-Aligned manipulation Policy (CLAP), a framework that integrates three key components: 1) task ...
- **p. 1 / ABSTRACT - extractive body cue:** Through comprehensive experiments in simulation and on a real robot, we demonstrate its superior generalization capability.
- **p. 1 / ABSTRACT - extractive body cue:** Specifically, on GemBench, a benchmark designed for evaluating generalization, our approach achieves a 12% higher average success rate than the SOTA method while using only ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** For simulation, we use GemBench (Garcia et al., 2025), a benchmark specifically designed to assess the generalization ability of multi-task language-conditioned policies across varying difficulty ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, scaling these methods to a broader range of real-world applications (e.g., industrial, service, or home robotics) requires enhancing both (G1) their generalization to environment ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In real-world experiments, our method demonstrate strong generalization ability to novel tasks and object variations with only 10 demonstrations per task.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these limitations and issues, we propose Coarse-to-fine Language-Aligned manipulation Policy (CLAP), a novel coarse-to-fine 3D manipulation policy.
- **p. 5 / 4 METHOD - extractive body cue:** Our hierarchical policy consists of a coarse task planner and a fine-grained action predictor, as shown in Figure 2.
- **p. 6 / 4 METHOD - extractive body cue:** To mitigate this, we introduce two ideas.
- **p. 6 / 4 METHOD - extractive body cue:** To address this issue, we propose decoupling task planning from keypoint prediction via a two-round inference protocol.
- **p. 6 / 4 METHOD - extractive body cue:** Instead, inspired by Chain-of-Thought reasoning (Mu et al., 2023; Zawalski et al., 2024; Zhao et al., 2025) for robotics, we design a reasoning process by ...
- **p. 7 / 4 METHOD - extractive body cue:** Our feature encoding pipeline consists of three stages to construct a unified 3D-aware and language-aligned representation.
- **p. 5 / 4 METHOD - extractive body cue:** 4.1 COARSE TASK PLANNER Prior coarse-to-fine policies condition all actions within a trajectory on a single high-level task description, limiting compositional generalization.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The fine-grained action predictor takes as input both the step instruction and the multi-view RGB-D images and outputs an action. | image/video, language instruction, proprioception과 history | p. 2 (1 INTRODUCTION), p. 5 (4 METHOD) |
| State/latent | fine-grained, action, predictor, takes, input, step, instruction, multi-view, RGB-D, images, outputs, addition | language-grounded task state와 action-policy context | p. 2 (1 INTRODUCTION), p. 5 (4 METHOD), p. 6 (4 METHOD) |
| Output/action | In addition to task decomposition done at the beginning, at every execution timestep, the VLM fθ is also exploited to predict both the step instruction ℓtk (used as a novel input of ... | continuous action, pose 또는 action chunk | p. 5 (4 METHOD), p. 6 (4 METHOD), p. 4 (3 BACKGROUND) |
| Objective/outcome | Instead, inspired by Chain-of-Thought reasoning (Mu et al., 2023; Zawalski et al., 2024; Zhao et al., 2025) for robotics, we design a reasoning process by training our model to first reason about ... | instruction following, task success, generalization과 latency | p. 6 (4 METHOD), p. 7 (4 METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In real-world experiments, our method demonstrate strong generalization ability to novel tasks and object variations with only 10 demonstrations per task.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these limitations and issues, we propose Coarse-to-fine Language-Aligned manipulation Policy (CLAP), a novel coarse-to-fine 3D manipulation policy.
- **p. 5 / 4 METHOD - extractive body cue:** Our hierarchical policy consists of a coarse task planner and a fine-grained action predictor, as shown in Figure 2.
- **p. 6 / 4 METHOD - extractive body cue:** To mitigate this, we introduce two ideas.
- **p. 6 / 4 METHOD - extractive body cue:** To address this issue, we propose decoupling task planning from keypoint prediction via a two-round inference protocol.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Ablation study of CLAP on GemBench. Here are the average success rates of 4 levels of evaluation tasks from Gembench under different training ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Our method achieves an overall success rate 12% higher than prior 7
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** CLAP achieves 54.8% higher average success rates compared to RVT2 on the evaluation tasks.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 7 (5 EXPERIMENTS) |
| Embodiment/environment | It is LoRA fine-tuned (Hu et al., 2022) with the object keypoint dataset, language plans, and robot trajectories. | hardware/simulator version and reset protocol | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Dataset/benchmark | 5.2 REAL-WORLD EXPERIMENTS Experimental Setting We keep the training settings the same as in the simulation and list key modifications here. | role, split, size and leakage | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Metric | RVT2 CLAP RVT2 CLAP RVT2 CLAP RVT2 CLAP RVT2 CLAP place shape in shape sorter 60% 60% 35% 50% 30% 40% 20% 50% 36.2% 50% put block in cup with same color ... | definition, denominator, direction and uncertainty | p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Baseline/ablation | Table 2: Ablation study of CLAP on GemBench. Here are the average success rates of 4 levels of evaluation tasks from Gembench under different training settings. state-of-the-art method (Li et al., 2025b). ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 16 / A.5 ADDITIONAL ABLATION STUDY - extractive body cue:** Further increasing the number of robot trajectory improves on the in-domain performance (L1) while does not help in the average success rate.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Furthermore, our design leads to substantial performance gain on the most challenging Level-4 tasks, where several baselines methods fail consistently.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 For simulation, we use GemBench (Garcia et al., 2025), a benchmark specifically designed to assess the generalization ability of multi-task language-conditioned policies across varying difficulty levels.를 문제로 두고, In real-world experiments, our method demonstrate strong generalization ability to novel tasks and object variations with only 10 demonstrations per task.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (3 BACKGROUND), p. 5 (4 METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
