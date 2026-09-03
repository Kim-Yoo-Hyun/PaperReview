# Spatial Understanding from Videos: Structured Prompts Meet Simulation Data

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=SBYCu5uJJf.
> PDF retrieval source: https://arxiv.org/pdf/2506.03642. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, 3D Vision
- Official paper: https://openreview.net/forum?id=SBYCu5uJJf
- Full-text retrieval: https://arxiv.org/pdf/2506.03642
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, performing 3D spatial reasoning from scanning videos presents two significant challenges: (1) Spatial Uncertainty.를 문제로 두고, Our contributions are summarized as follows: • We introduce SpatialMind, a spatial prompting strategy that decomposes spatial reasoning into structured steps, enabling pre-trained VLMs to perform multi-step inference over spatial relati ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Visual-spatial understanding, the ability to infer object relationships and layouts from visual input, is fundamental to downstream tasks such as robotic navigation and embodied interaction.
- **p. 1 / Abstract - extractive body cue:** However, existing methods face spatial uncertainty and data scarcity, limiting the 3D spatial reasoning capability of pre-trained visionlanguage models (VLMs).
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we present a unified framework for enhancing 3D spatial reasoning in pre-trained VLMs without modifying their architecture.
- **p. 1 / Abstract - extractive body cue:** This framework combines SpatialMind, a structured prompting strategy that decomposes complex scenes and questions into interpretable reasoning steps, with ScanForgeQA, a scalable question-answering dataset built ...
- **p. 1 / Abstract - extractive body cue:** Extensive experiments across multiple benchmarks demonstrate the individual and combined effectiveness of our prompting and fine-tuning strategies, and yield insights that may inspire future research ...
- **p. 1 / 1 Introduction - extractive body cue:** However, performing 3D spatial reasoning from scanning videos presents two significant challenges: (1) Spatial Uncertainty.
- **p. 1 / 1 Introduction - extractive body cue:** Effectively addressing this challenge demands multi-step ∗Corresponding author.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are summarized as follows: • We introduce SpatialMind, a spatial prompting strategy that decomposes spatial reasoning into structured steps, enabling pre-trained VLMs to ...
- **p. 2 / 1 Introduction - extractive body cue:** To address these challenges, we propose a dual approach for enhancing 3D spatial reasoning in pre-trained VLMs, without modifying their underlying architecture.
- **p. 5 / A B - extractive body cue:** The final dataset consists of 34,116 single-room scenes across six common categories: bedroom, kitchen, bathroom, living room, dining room, and storage room.
- **p. 1 / Abstract - extractive body cue:** This framework combines SpatialMind, a structured prompting strategy that decomposes complex scenes and questions into interpretable reasoning steps, with ScanForgeQA, a scalable question-answering dataset built ...
- **p. 5 / A B - extractive body cue:** Each scene is scanned using two complementary strategies designed to emulate natural human visual exploration: Orbit Scan.
- **p. 1 / 1 Introduction - extractive body cue:** In the absence of explicit depth information, models must infer 3D structure from inherently limited 2D observations.
- **p. 1 / 1 Introduction - extractive body cue:** As intelligent systems become increasingly embedded in real-world applications such as autonomous driving [4, 5], robotic navigation [6, 7], and augmented reality [8, 9, 10, ...
- **p. 6 / A B - extractive body cue:** This category targets interobject spatial relationships, requiring models to infer positional and geometric properties such as distance, orientation, and contact.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Visual-spatial understanding, the ability to infer object relationships and layouts from visual input, is fundamental to downstream tasks such as robotic navigation and embodied interaction. | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (Abstract), p. 1 (1 Introduction) |
| State/latent | Visual-spatial, understanding, ability, infer, object, relationships, layouts, visual, input, fundamental, downstream, tasks | geometry, map, object/relationship state | p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Output/action | In the absence of explicit depth information, models must infer 3D structure from inherently limited 2D observations. | point map, pose, scene graph, affordance 또는 query result | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Objective/outcome | Specifically, we adopt HoloDeck [47], a 3D generation framework that leverages LLMs to parse natural language prompts, retrieve matching assets from large-scale 3D object repositories such as Objaverse [48], and optimize their ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (A B), p. 6 (A B), p. 6 (A B) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are summarized as follows: • We introduce SpatialMind, a spatial prompting strategy that decomposes spatial reasoning into structured steps, enabling pre-trained VLMs to ...
- **p. 2 / 1 Introduction - extractive body cue:** To address these challenges, we propose a dual approach for enhancing 3D spatial reasoning in pre-trained VLMs, without modifying their underlying architecture.
- **p. 5 / A B - extractive body cue:** The final dataset consists of 34,116 single-room scenes across six common categories: bedroom, kitchen, bathroom, living room, dining room, and storage room.
- **p. 1 / Abstract - extractive body cue:** This framework combines SpatialMind, a structured prompting strategy that decomposes complex scenes and questions into interpretable reasoning steps, with ScanForgeQA, a scalable question-answering dataset built ...
- **p. 5 / A B - extractive body cue:** Each scene is scanned using two complementary strategies designed to emulate natural human visual exploration: Orbit Scan.
- **p. 8 / 5 Experiments - extractive body cue:** Results show that this strategy achieves improved performance, surpassing the original Qwen2.5-VL-7B baseline, suggesting that spatial fine-tuning can be harmonized with broader capabilities through data ...
- **p. 7 / 5 Experiments - extractive body cue:** Across all models, a consistent trend emerges: the +Des variant outperforms others, followed by +Grid, while +Map yields the least improvement.
- **p. 8 / 5 Experiments - extractive body cue:** The results, reported in the "+Both" row of Table 1, show consistent performance improvements across all evaluated models.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (5 Experiments), p. 7 (5 Experiments) |
| Embodiment/environment | Importantly, both datasets and the VSI-Bench benchmark originate from the same source (i.e., ScanNet [31]), resulting in minimal data discrepancy. | hardware/simulator version and reset protocol | p. 9 (5 Experiments), p. 8 (5 Experiments) |
| Dataset/benchmark | To investigate whether enhancing visualspatial capabilities via fine-tuning adversely impacts a model's general performance, we conducted evaluations on MVBench [52] and Video-MME [53], two broad multi-task video benchmarks. | role, split, size and leakage | p. 9 (5 Experiments), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments) |
| Metric | Method OpenEQA ScanQA SQA3D Acc/Score BLEU-1 EM-1 Qwen2.5-VL-7B 50.1/3.1 32.5 17.2 +SpatialMind 53.7/3.2 33.1 19.8 +ScanForgeQA 56.2/3.3 34.8 23.3 +Both 58.6/3.5 37.9 24.5 Qwen2.5-VL-72B 53.8/3.2 35.4 34.8 +SpatialMind 55.7/3.2 38.0 39. ... | definition, denominator, direction and uncertainty | p. 7 (5 Experiments), p. 9 (5 Experiments), p. 8 (5 Experiments) |
| Baseline/ablation | Our method consistently outperforms the baseline across all settings, with performance further improving as the number of frames and resolution increase. | fair input/data/compute/action matching | p. 9 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 5 Experiments - extractive body cue:** In Case (a), Qwen2.5-VL-7B fails to produce the correct directional prediction, likely due to its limited capacity for 3D spatial reasoning.
- **p. 9 / 5 Experiments - extractive body cue:** Case (b) involves a simpler spatial reasoning task, however, Qwen2.5-VL-7B still fails, potentially due to insufficient object localization.
- **p. 8 / 5 Experiments - extractive body cue:** These results validate the robustness of our approach and confirm its applicability across diverse spatial tasks and datasets.
- **p. 20 / Figure/Table caption - extractive body cue:** Figure 8: Distribution of room types in the ScanForgeQA dataset. are consistent with those reported in our main analysis, further reinforcing the effectiveness and generalizability ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, performing 3D spatial reasoning from scanning videos presents two significant challenges: (1) Spatial Uncertainty.를 문제로 두고, Our contributions are summarized as follows: • We introduce SpatialMind, a spatial prompting strategy that decomposes spatial reasoning into structured steps, enabling pre-trained VLMs to perform multi-step inference over spatial relati ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
