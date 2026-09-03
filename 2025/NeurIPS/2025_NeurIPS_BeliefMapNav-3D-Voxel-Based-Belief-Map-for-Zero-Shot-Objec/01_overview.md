# BeliefMapNav: 3D Voxel-Based Belief Map for Zero-Shot Object Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=7AMriz7I3K.
> PDF retrieval source: https://arxiv.org/pdf/2506.06487.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, Navigation
- Official paper: https://openreview.net/forum?id=7AMriz7I3K
- Full-text retrieval: https://arxiv.org/pdf/2506.06487.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Training-based methods typically require large amounts of data and have difficulty generalizing due to limited environmental diversity [17, 18], while zero-shot methods offer flexibility and adaptability to novel environments, but are c ...를 문제로 두고, The contributions of our method are mainly summarized as follows: 1)We propose BeliefMapNav, an efficient zero-shot object navigation system that accurately predicts target location through fine-grained belief estimation in a 3D voxel-b ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Zero-shot object navigation (ZSON) allows robots to find target objects in unfamiliar environments using natural language instructions, without relying on pre-built maps or task-specific training.
- **p. 1 / Abstract - extractive body cue:** Recent general-purpose models, such as large language models (LLMs) and vision-language models (VLMs), equip agents with semantic reasoning abilities to estimate target object locations in ...
- **p. 1 / Abstract - extractive body cue:** However, these models often greedily select the next goal without maintaining a global understanding of the environment and are fundamentally limited in the spatial reasoning ...
- **p. 1 / Abstract - extractive body cue:** To overcome these limitations, we propose a novel 3D voxel-based belief map that estimates the target's prior presence distribution within a voxelized 3D space.
- **p. 1 / Abstract - extractive body cue:** This approach enables agents to integrate semantic priors from LLMs and visual embeddings with hierarchical spatial structure, alongside real-time observations, to build a comprehensive 3D ...
- **p. 3 / 1 Introduction - extractive body cue:** Training-based methods typically require large amounts of data and have difficulty generalizing due to limited environmental diversity [17, 18], while zero-shot methods offer flexibility and ...
- **p. 2 / 1 Introduction - extractive body cue:** However, both LLMs and VLMs face limitations in spatial understanding and reasoning [15], which significantly affect target location prediction accuracy.

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** The contributions of our method are mainly summarized as follows: 1)We propose BeliefMapNav, an efficient zero-shot object navigation system that accurately predicts target location through ...
- **p. 2 / 1 Introduction - extractive body cue:** To enable more precise and accurate predictions of the target object's location within 3D space, we propose a novel 3D voxel-based belief map that considers ...
- **p. 1 / 1 Introduction - extractive body cue:** Zero-shot object navigation(ZSON) enables robots to locate targets in novel environments through natural language instructions (e.g., "find the red sofa"), eliminating reliance on pre-mapped scenes ...
- **p. 2 / 1 Introduction - extractive body cue:** To further enhance search efficiency, we introduce BeliefMapNav, an efficient zero-shot object navigation system based on path sequence optimization over the belief map.
- **p. 3 / 1 Introduction - extractive body cue:** In contrast, our method constructs a multi-level, spatially-aligned semantic map that supports accurate target object localization estimation.
- **p. 3 / 3 Method - extractive body cue:** At each timestep, the system takes as input the current RGB-D observation It, the agent's pose st, and the text-specified target c, and outputs a ...
- **p. 4 / 3 Method - extractive body cue:** The observation-based belief planning module selects the next goal based on this belief and outputs navigation actions.
- **p. 5 / 3 Method - extractive body cue:** We use CLIP [33] to extract visual features vk h,w for each patch and each patch P k h,w is processed by the Segment Anything ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | At each timestep, the system takes as input the current RGB-D observation It, the agent's pose st, and the text-specified target c, and outputs a navigation action at ∈A from the discrete ... | camera/depth stream, pose, map와 language goal | p. 3 (3 Method), p. 4 (3 Method) |
| State/latent | timestep, system, takes, input, current, RGB-D, observation, agent, pose, text-specified, target, outputs | robot pose, free-space/semantic map와 local goal | p. 3 (3 Method), p. 4 (3 Method), p. 6 (3 Method) |
| Output/action | The observation-based belief planning module selects the next goal based on this belief and outputs navigation actions. | collision-free trajectory 또는 velocity command | p. 4 (3 Method), p. 6 (3 Method), p. 2 (1 Introduction) |
| Objective/outcome | The proposed objective improves search efficiency by minimizing exploration cost with A*-optimized paths and prioritizing high-belief frontiers via observation-weighted costs. | goal reach, safety, localization error와 replanning latency | p. 7 (3 Method), p. 7 (3 Method), p. 4 (3 Method) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** The contributions of our method are mainly summarized as follows: 1)We propose BeliefMapNav, an efficient zero-shot object navigation system that accurately predicts target location through ...
- **p. 2 / 1 Introduction - extractive body cue:** To enable more precise and accurate predictions of the target object's location within 3D space, we propose a novel 3D voxel-based belief map that considers ...
- **p. 1 / 1 Introduction - extractive body cue:** Zero-shot object navigation(ZSON) enables robots to locate targets in novel environments through natural language instructions (e.g., "find the red sofa"), eliminating reliance on pre-mapped scenes ...
- **p. 2 / 1 Introduction - extractive body cue:** To further enhance search efficiency, we introduce BeliefMapNav, an efficient zero-shot object navigation system based on path sequence optimization over the belief map.
- **p. 3 / 1 Introduction - extractive body cue:** In contrast, our method constructs a multi-level, spatially-aligned semantic map that supports accurate target object localization estimation.
- **p. 8 / 3 Method - extractive body cue:** On the HM3D dataset, our method improves SPL by 46.4% compared to the zero-shot method InstructNav [9], which achieves the highest SR.
- **p. 8 / 3 Method - extractive body cue:** However, on the HSSD dataset, performance significantly improves because the synthetic scenes avoid the issues present in MP3D and HM3D.
- **p. 9 / 3 Method - extractive body cue:** Results indicate that incorporating more semantic levels generally improves SR.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 8 (3 Method), p. 8 (3 Method) |
| Embodiment/environment | HSSD, a synthetic dataset with scenes based on real house layouts, contains 40 validation scenes, 1,248 navigation episodes, and 6 object categories. | hardware/simulator version and reset protocol | p. 7 (3 Method), p. 7 (3 Method) |
| Dataset/benchmark | However, on the HSSD dataset, performance significantly improves because the synthetic scenes avoid the issues present in MP3D and HM3D. | role, split, size and leakage | p. 7 (3 Method), p. 7 (3 Method), p. 8 (3 Method), p. 15 (A.3 Prompting) |
| Metric | Evaluation Metrics: We use two standard metrics: Success Rate (SR) and Success weighted by Path Length (SPL). | definition, denominator, direction and uncertainty | p. 7 (3 Method), p. 8 (3 Method), p. 9 (3 Method) |
| Baseline/ablation | As shown in Table 1, our method outperforms all existing zero-shot baselines, achieving significant improvements across multiple benchmarks. | fair input/data/compute/action matching | p. 8 (3 Method), p. 8 (3 Method), p. 18 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 3 Method - extractive body cue:** Baseline summaries and HM3D failure analyses appear in Appendix A.6 and A.7, respectively.
- **p. 8 / 3 Method - extractive body cue:** Across all datasets, the performance limitations of the local planner in [7] lead to significant degradation, especially in narrow areas.
- **p. 8 / 3 Method - extractive body cue:** Second, a lot of mesh "holes" in MP3D, which allow the agent to see through obstacles, causing it to mistakenly prioritize these holes as targets, ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 8: The proportion of different causes of failure in the HM3D dataset. A.6 Baselines We evaluate our approach in comparison with a range (ZSGN) ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: The search process: BeliefMapNav plans frontier paths by minimizing the expected search distance based on the 3D voxel-based belief map, ensuring efficient and ...
- **p. 14 / A.2 Adaptive hierarchical feature selection - extractive body cue:** For each semantic level, if the voxel does not contain an existing feature, we directly store the current feature and its associated confidence score.
- **p. 7 / 3 Method - extractive body cue:** Combining geometric path costs and belief weights, it reduces noise impact on navigation stability.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Training-based methods typically require large amounts of data and have difficulty generalizing due to limited environmental diversity [17, 18], while zero-shot methods offer flexibility and adaptability to novel environments, but are c ...를 문제로 두고, The contributions of our method are mainly summarized as follows: 1)We propose BeliefMapNav, an efficient zero-shot object navigation system that accurately predicts target location through fine-grained belief estimation in a 3D voxel-b ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 3 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
