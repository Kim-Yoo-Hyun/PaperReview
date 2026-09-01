# Problem - BeliefMapNav: 3D Voxel-Based Belief Map for Zero-Shot Object Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (29 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=7AMriz7I3K; PDF retrieval source: https://openreview.net/pdf/0723f863304fd597c9e6e38242914d49584b6776.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction)): Training-based methods typically require large amounts of data and have difficulty generalizing due to limited environmental diversity [19, 26], while zero-shot methods offer flexibility and adaptability to novel environments, but ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Zero-shot object navigation (ZSON) allows robots to find target objects in unfamiliar environments using natural language instructions, without relying on pre-built maps or task-specific training.
- **p. 1 / Abstract - extractive PDF cue:** Recent general-purpose models, such as large language models (LLMs) and vision-language models (VLMs), equip agents with semantic reasoning abilities to estimate target object locations in ...
- **p. 1 / Abstract - extractive PDF cue:** However, these models often greedily select the next goal without maintaining a global understanding of the environment and are fundamentally limited in the spatial reasoning ...
- **p. 1 / Abstract - extractive PDF cue:** To overcome these limitations, we propose a novel 3D voxel-based belief map that estimates the target's prior presence distribution within a voxelized 3D space.
- **p. 1 / Abstract - extractive PDF cue:** This approach enables agents to integrate semantic priors from LLMs and visual embeddings with hierarchical spatial structure, alongside real-time observations, to build a comprehensive 3D ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Training-based methods typically require large amounts of data and have difficulty generalizing due to limited environmental diversity [19, 26], while zero-shot methods offer flexibility and ...
- **p. 2 / 1 Introduction - extractive PDF cue:** However, both LLMs and VLMs face limitations in spatial understanding and reasoning [15], which significantly affect target location prediction accuracy.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Training-based methods typically require large amounts of data and have difficulty generalizing due to limited environmental diversity [19, 26], while zero-shot methods ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | At each timestep, the system takes as input the current RGB-D observation It, the agent's pose st, and the text-specified target c, ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | timestep, system, takes, input, current, RGB-D, observation, agent, pose, text-specified | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | fusion, enables, more, dynamic, accurate, estimation, belief, detecting | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: timestep, system, takes, input, current, RGB-D, observation, agent, pose, text-specified | p. 3 (3 Method), p. 4 (3 Method), p. 6 (3 Method) |
| Decision / output variable | path/waypoint/velocity; body terms: contributions, mainly, summarized, follows, BeliefMapNav, efficient, zero-shot, object | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: objective, improves, search, efficiency, minimizing, exploration, cost, optimized | p. 7 (3 Method), p. 7 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 9 (3 Method), p. 4 (3 Method), p. 5 (3 Method) |
| Success / guarantee | goal reach with collision-free execution | p. 9 (3 Method), p. 2 (Figure/Table caption), p. 5 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** However, both LLMs and VLMs face limitations in spatial understanding and reasoning [15], which significantly affect target location prediction accuracy.
- **p. 2 / 1 Introduction - extractive PDF cue:** Together, in existing works, the lack of semantic cues and spatial reasoning leads to inaccurate and imprecise target object position estimation.
- **p. 3 / 1 Introduction - extractive PDF cue:** As a result, the generated maps lack the precision needed to accurately localize target objects.
- **p. 1 / 1 Introduction - extractive PDF cue:** To enable ZSON, prior works have progressed along two main directions.

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): The contributions of our method are mainly summarized as follows: 1) We propose BeliefMapNav, an efficient zero-shot object navigation system that accurately predicts target location through fine-grained belief estimation in ...

- **p. 2 / 1 Introduction - extractive PDF cue:** To enable more precise and accurate predictions of the target object's location within 3D space, we propose a novel 3D voxel-based belief map that considers ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Zero-shot object navigation (ZSON) enables robots to locate targets in novel environments through natural language instructions (e.g., "find the red sofa"), eliminating reliance on pre-mapped ...
- **p. 2 / 1 Introduction - extractive PDF cue:** To further enhance search efficiency, we introduce BeliefMapNav, an efficient zero-shot object navigation system based on path sequence optimization over the belief map.
- **p. 3 / 1 Introduction - extractive PDF cue:** In contrast, our method constructs a multi-level, spatially-aligned semantic map that supports accurate target object localization estimation.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Across all datasets, the performance limitations of the local planner in [7] lead to significant degradation, especially in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Second, there are a lot of mesh "holes" in MP3D, which allow the agent to see through obstacles, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 26 | Figure 8: The proportion of different causes of failure in the HM3D dataset. A.6 Baselines We evaluate our ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 22 | For each semantic level, if the voxel does not contain an existing feature, we directly store the current ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), interface p. 3 (3 Method), p. 4 (3 Method), p. 6 (3 Method), p. 2 (1 Introduction), objective p. 7 (3 Method), p. 7 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
