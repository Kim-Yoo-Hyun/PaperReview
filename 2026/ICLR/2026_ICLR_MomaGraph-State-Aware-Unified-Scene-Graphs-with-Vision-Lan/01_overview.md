# MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=3eTr9dGwJv.
> PDF retrieval source: https://openreview.net/pdf/3f888689e829f4172ae97d1dfac5f1b62ddb30c3.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Vision-Language Model, Robotics, 3D Vision, Graph Reasoning
- Official paper: https://openreview.net/forum?id=3eTr9dGwJv
- Full-text retrieval: https://openreview.net/pdf/3f888689e829f4172ae97d1dfac5f1b62ddb30c3.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, existing scene graphs suffer from notable limitations.를 문제로 두고, In summary, our work makes the following key contributions: • We propose MomaGraph, the first scene graph representation that jointly models spatial and functional relationships while incorporating part-level interactive nodes, providin ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Mobile manipulators in households must both navigate and manipulate.
- **p. 1 / ABSTRACT - extractive body cue:** This requires a compact, semantically rich scene representation that captures where objects are, how they function, and which parts are actionable.
- **p. 1 / ABSTRACT - extractive body cue:** Scene graphs are a natural choice, yet prior work often separates spatial and functional relations, treats scenes as static snapshots without object states or temporal ...
- **p. 1 / ABSTRACT - extractive body cue:** To address these limitations, we introduce MomaGraph, a unified scene representation for embodied agents that integrates spatial-functional relationships and part-level interactive elements.
- **p. 1 / ABSTRACT - extractive body cue:** However, advancing such a representation requires both suitable data and rigorous evaluation, which have been largely missing.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, existing scene graphs suffer from notable limitations.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** However, when directly used as task planners, VLMs (Huang et al., 2023; 2024; Ahn et al., 2022; Zheng et al., 2025a; Yang et al., 2025) ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our work makes the following key contributions: • We propose MomaGraph, the first scene graph representation that jointly models spatial and functional relationships ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To achieve this goal, we present MomaGraph, a novel scene representation specifically designed for embodied agents.
- **p. 6 / 4 METHOD - extractive body cue:** To address these limitations, we introduce MomaGraph-Scenes, the first dataset designed to provide a more comprehensive and task-relevant scene representation.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Unlike prior graph-then-plan methods (Dai et al., 2024; Ekpo et al., 2024) that either assume reliable scene graphs or treat graph construction and planning as ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To overcome this gap, we propose the Graph-then-Plan strategy, which first generates task-specific scene graphs as an intermediate structured representation before high-level planning.
- **p. 6 / 4 METHOD - extractive body cue:** After the agent executes an action at and observes the new environment state st+1, the scene graph is refined as: G(t+1) T = U  ...
- **p. 5 / 4 METHOD - extractive body cue:** Reinforcement learning offers a more principled approach by encouraging the model to explore, reason, and iteratively refine its representations through outcome-driven feedback.
- **p. 5 / 4 METHOD - extractive body cue:** 4.2 VLMS LEARN SCENE GRAPH REPRESENTATIONS WITH REINFORCEMENT LEARNING Existing open-source VLMs have demonstrated limited capability in generating accurate taskoriented scene graphs GT from multi-view ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In this work, we do not focus on the agent's interaction policy; instead, our emphasis lies on how to capture and incorporate observed state changes in the environment into the scene graph ... | camera/depth stream, pose, map와 language goal | p. 6 (4 METHOD), p. 5 (4 METHOD) |
| State/latent | focus, agent, interaction, policy, instead, emphasis, lies, capture, incorporate, observed, state, changes | robot pose, free-space/semantic map와 local goal | p. 6 (4 METHOD), p. 5 (4 METHOD), p. 5 (4 METHOD) |
| Output/action | 4.1 MOMAGRAPH DEFINITION Given a single indoor room, the agent receives as input a set of multi-view images {Ii}n i=1 and a natural language instruction T . | collision-free trajectory 또는 velocity command | p. 5 (4 METHOD), p. 5 (4 METHOD), p. 3 (1 INTRODUCTION) |
| Objective/outcome | The objective is to construct an instruction-conditioned, task-oriented scene graph GT = (NT , ET s , ET f ). | goal reach, safety, localization error와 replanning latency | p. 5 (4 METHOD), p. 5 (4 METHOD), p. 6 (4 METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In summary, our work makes the following key contributions: • We propose MomaGraph, the first scene graph representation that jointly models spatial and functional relationships ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To achieve this goal, we present MomaGraph, a novel scene representation specifically designed for embodied agents.
- **p. 6 / 4 METHOD - extractive body cue:** To address these limitations, we introduce MomaGraph-Scenes, the first dataset designed to provide a more comprehensive and task-relevant scene representation.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Unlike prior graph-then-plan methods (Dai et al., 2024; Ekpo et al., 2024) that either assume reliable scene graphs or treat graph construction and planning as ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To overcome this gap, we propose the Graph-then-Plan strategy, which first generates task-specific scene graphs as an intermediate structured representation before high-level planning.
- **p. 11 / 6 EXPERIMENTS - extractive body cue:** As shown in Figure 6, our system achieves an 80% success rate in graph generation, 87.5% success rate in planning (conditioned on correct graphs), and ...
- **p. 22 / Figure/Table caption - extractive body cue:** Table 5: Comparison of our RL-based training with SFT and ICL baselines. Our method achieves substantially better performance on both benchmarks. As shown in Table ...
- **p. 11 / 6 EXPERIMENTS - extractive body cue:** These results demonstrate that MomaGraph remains robust across multiple reasoning and execution stages, achieving a 70% overall success rate on a complex multi-step task.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 11 (6 EXPERIMENTS), p. 22 (Figure/Table caption) |
| Embodiment/environment | To rigorously evaluate spatial-functional reasoning and task planning capabilities, we design a comprehensive multi-choice VQA benchmark based on the scenes and tasks in our dataset. | hardware/simulator version and reset protocol | p. 19 (A.4.1 BENCHMARK DESIGN), p. 17 (A.1.1 REAL-WORLD DATASET SOURCE AND COLLECTION) |
| Dataset/benchmark | Our dataset consists of approximately 1,050 subgraphs and 6278 multi-view RGB images, collected across more than 350 diverse household scenes and encompassing 93 distinct task instructions. | role, split, size and leakage | p. 19 (A.4.1 BENCHMARK DESIGN), p. 17 (A.1.1 REAL-WORLD DATASET SOURCE AND COLLECTION), p. 18 (A.1.4 MULTI-ASPECT STATISTICS OF THE TRAINING DATASET), p. 10 (6 EXPERIMENTS) |
| Metric | This evaluation includes success rates and failure analysis across different stages to validate overall system performance under realistic, sequential conditions (see Figure 6). | definition, denominator, direction and uncertainty | p. 11 (6 EXPERIMENTS), p. 20 (Figure/Table caption), p. 11 (6 EXPERIMENTS) |
| Baseline/ablation | Across all models, the w/ Graph setting consistently outperforms the w/o Graph baseline, demonstrating that explicitly structuring task-oriented scene graphs provides a tangible benefit for downstream planning. | fair input/data/compute/action matching | p. 9 (6 EXPERIMENTS), p. 10 (6 EXPERIMENTS), p. 22 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 11 / Figure/Table caption - extractive body cue:** Figure 6: Quantitative real-robot evaluation. (a) Environment setup of the real-robot experiment. (b) Failure analysis illustrating success/failure rates across different reasoning stages. Task Setup. We ...
- **p. 11 / 7 CONCLUSION - extractive body cue:** This work addresses to the fundamental limitations of existing scene graphs for embodied agents: reliance on a single type of relationship, inability to adapt to ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Direct planning often fails even for strong closed-source models like GPT-5, producing wrong actions or missing key steps, while our Graph-then-Plan approach with ...
- **p. 20 / A.4.1 BENCHMARK DESIGN - extractive body cue:** Moreover, since the benchmark is formulated as a multi-choice VQA task with clearly defined correct answers, it does not require complex evaluation metrics.
- **p. 9 / 6 EXPERIMENTS - extractive body cue:** In contrast, MomaGraph-R1 exhibits a much smaller degradation, preserving strong performance in Tier 3 and Tier 4.
- **p. 10 / 6 EXPERIMENTS - extractive body cue:** Our real-world evaluations show that MomaGraph-R1 delivers robust scene understanding and task planning even in unseen scenarios, while remaining directly compatible with standard mobile humanoid ...
- **p. 22 / Figure/Table caption - extractive body cue:** Table 6: Sensitivity analysis of reward weights (wa, wf, wl) in our DAPO training. The model's performance remains stable across different weight configurations. As shown ...

## Why Read It

VLA and generalist robot policies의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, existing scene graphs suffer from notable limitations.를 문제로 두고, In summary, our work makes the following key contributions: • We propose MomaGraph, the first scene graph representation that jointly models spatial and functional relationships while incorporating part-level interactive nodes, providin ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 6 (4 METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (26 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, existing scene graphs suffer from notable limitations. (p. 2, 1 INTRODUCTION).
- **Actual contribution:** In summary, our work makes the following key contributions: • We propose MomaGraph, the first scene graph representation that jointly models spatial and functional relationships while incorporating part-level interactive nodes, ... (p. 2, 1 INTRODUCTION).
- **Evaluation boundary:** Table 2: Performance comparison on the MomaGraph-Bench. We report accuracy (%) across four tiers (T1-T4) and the overall score, with and without graph-based reasoning. Type Models Params MomaGraph Benchmark Tier ... (p. 9, Figure/Table caption).
- **Explicit failure boundary:** (b) Failure analysis illustrating success/failure rates across different reasoning stages. (p. 11, 6 EXPERIMENTS).
