# From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (34 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=yngvAamNQi.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/245158. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Vision-Language Model, Robotics, 3D Vision
- Official paper: https://openreview.net/forum?id=yngvAamNQi
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/245158
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (34 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 FSD unlocks visual aids reasoning and generation through Spatial RelationshipFocused CoT, demonstrating exceptional generalization capabilities that enable zero-shot robot manipulation and achieving remarkable performance across multipl ...를 문제로 두고, To this end, we propose FSD (From Seeing to Doing), a novel framework that generates these visual intermediate representations through structured spatial reasoning (Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Achieving generalization in robotic manipulation remains a critical challenge, particularly for unseen scenarios and novel tasks.
- **p. 1 / ABSTRACT - extractive body cue:** Current Vision-Language-Action (VLA) models, while building on top of general Vision-Language Models (VLMs), still fall short of achieving robust zero-shot performance due to the scarcity ...
- **p. 1 / ABSTRACT - extractive body cue:** To address these limitations, we propose FSD (From Seeing to Doing), a novel vision-language model that generates intermediate representations through spatial relationship reasoning, providing fine-grained ...
- **p. 1 / ABSTRACT - extractive body cue:** Our approach combines a hierarchical data construction pipeline for training with a self-consistency mechanism that aligns spatial coordinates with visual signals.
- **p. 1 / ABSTRACT - extractive body cue:** Through extensive experiments, we comprehensively validated FSD's capabilities in both "seeing" and "doing", achieving outstanding performance across 8 benchmarks for general spatial reasoning and embodied ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** FSD unlocks visual aids reasoning and generation through Spatial RelationshipFocused CoT, demonstrating exceptional generalization capabilities that enable zero-shot robot manipulation and achieving remarkable performance across ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** We attribute the limited generalization in existing VLA-based systems to two fundamental challenges: data scarcity and heterogeneity.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, we propose FSD (From Seeing to Doing), a novel framework that generates these visual intermediate representations through structured spatial reasoning (Fig.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions include: 1) A novel paradigm where VLM reasoning generates versatile visual aids, enabling either direct open-loop control or serving as the high-level planner ...
- **p. 4 / 4. How to avoid collisions? - extractive body cue:** Based on these considerations, we introduce Spatial Relationship-Focused Visual Chain-of-thought (SrCoT).
- **p. 4 / 4. How to avoid collisions? - extractive body cue:** While VLMs struggle to directly map future actions to image coordinates, our method leverages known object relationships as reference points for multi-hop analysis, simplifying the ...
- **p. 5 / 4. How to avoid collisions? - extractive body cue:** Therefore, we propose a self-consistency mechanism to further align FSD capabilities in 5
- **p. 6 / 4. How to avoid collisions? - extractive body cue:** The training process unfolds in two stages: General Spatial Reasoning Enhancement: In the first stage, we use our Level 1-3 data to cultivate the model's ...
- **p. 5 / 4. How to avoid collisions? - extractive body cue:** For visual trace generation (Level 5 Dataset), we employ a two-stage approach: first applying self-supervised keypoint extraction (Huang et al., 2024) to identify grasp points ...
- **p. 6 / 4. How to avoid collisions? - extractive body cue:** FSD's architecture features a frozen CLIP-ViT-L (Gao et al., 2024) image encoder and a Vicuna-13B (Zheng et al., 2023b) LLM, which are connected by a ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A driving force behind robotics research is the pursuit of generalization: creating agents capable of versatile action across diverse robotic platforms, extending beyond familiar tasks, objects, and environments while adapting to dynami ... | image/video, language instruction, proprioception과 history | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| State/latent | driving, force, behind, robotics, research, pursuit, generalization, creating, agents, capable, versatile, action | language-grounded task state와 action-policy context | p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 6 (4. How to avoid collisions?) |
| Output/action | End-to-end VLAs (Black et al., 2024; Brohan et al., 2023) attempt a direct mapping from multimodal inputs to low-level actions, but the disconnect between pre-trained cyberspace data and physical action modalities can ... | continuous action, pose 또는 action chunk | p. 1 (1 INTRODUCTION), p. 6 (4. How to avoid collisions?), p. 4 (4. How to avoid collisions?) |
| Objective/outcome | Subsequently, we optimize the path trajectory using gradient descent-based interpolation, generating complete motion trajectories in SE(3) space, enabling the robotic arm to follow the 3D visual trajectory. | instruction following, task success, generalization과 latency | p. 6 (4. How to avoid collisions?), p. 4 (4. How to avoid collisions?), p. 5 (4. How to avoid collisions?) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To this end, we propose FSD (From Seeing to Doing), a novel framework that generates these visual intermediate representations through structured spatial reasoning (Fig.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions include: 1) A novel paradigm where VLM reasoning generates versatile visual aids, enabling either direct open-loop control or serving as the high-level planner ...
- **p. 4 / 4. How to avoid collisions? - extractive body cue:** Based on these considerations, we introduce Spatial Relationship-Focused Visual Chain-of-thought (SrCoT).
- **p. 4 / 4. How to avoid collisions? - extractive body cue:** While VLMs struggle to directly map future actions to image coordinates, our method leverages known object relationships as reference points for multi-hop analysis, simplifying the ...
- **p. 5 / 4. How to avoid collisions? - extractive body cue:** Therefore, we propose a self-consistency mechanism to further align FSD capabilities in 5
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** Type Model Put Spoon on Towel Put Carrot on Plate Stack Green Block on Yellow Block Put Eggplant in Yellow Basket Avg End-to-end VLA Octo ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** Under zero-shot conditions, FSD achieved 72% success rate, outperforming the strongest baseline by more than 30%.
- **p. 8 / 6 EXPERIMENTS - extractive body cue:** 1, FSD achieves a leading average rank of 1.3 across 15 tasks from spatial benchmarks, significantly outperforming other 13B open-source models and rivaling the closed-source ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |
| Embodiment/environment | For Doing, we conducted zero-shot manipulation experiments in both SimplerEnv (Li et al., 2024c) simulation and real-world xArm robotic platforms to assess its practical generalization performance. | hardware/simulator version and reset protocol | p. 7 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |
| Dataset/benchmark | Use 2D points to mark the manipulated object-centric waypoints to guide the robot to successfully complete the task. | role, split, size and leakage | p. 7 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 7 (6 EXPERIMENTS) |
| Metric | Specifically, FSD achieves 61.82% accuracy on VABench-P, over 3x higher than RoboPoint (19.09%) and attains significantly lower error rates with a better LLM Score on VABench-V. | definition, denominator, direction and uncertainty | p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |
| Baseline/ablation | 3, FSD significantly outperforms all baselines in generating precise spatial affordances and visual traces. | fair input/data/compute/action matching | p. 8 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS), p. 9 (6 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 7 CONCLUSION - extractive body cue:** More limitations and future works are in App.J.
- **p. 34 / Figure/Table caption - extractive body cue:** Figure 17: Visual comparison demonstrating the effectiveness of Self-Consistency Alignment. It is worth noting that without self-consistent alignment, the model's textual reasoning process is logically ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Overview of FSD. FSD unlocks visual aids reasoning and generation through Spatial Relationship- Focused CoT, demonstrating exceptional generalization capabilities that enable zero-shot robot ...
- **p. 10 / 7 CONCLUSION - extractive body cue:** We acknowledge limitations, such as the reliance on 2D trajectory generation and constraints from training data quality.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Inspired by the process of human reasoning, FSD uses a spatial relationship graph as an anchor to derive a visual chain-of-thought reasoning process ...
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** The primary cause of MOKA failures stems from the cascading errors of multiple submodules.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: FSD screens data from large-scale embodied datasets, generates ground truth spatial relationship graph. We finally collected 300K data for 10+ embodiments with 5-level ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 FSD unlocks visual aids reasoning and generation through Spatial RelationshipFocused CoT, demonstrating exceptional generalization capabilities that enable zero-shot robot manipulation and achieving remarkable performance across multipl ...를 문제로 두고, To this end, we propose FSD (From Seeing to Doing), a novel framework that generates these visual intermediate representations through structured spatial reasoning (Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 6 (4. How to avoid collisions?), p. 5 (4. How to avoid collisions?) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
