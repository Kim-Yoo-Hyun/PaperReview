# Problem - Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_Move_to_Understand_a_3D_Scene_Bridging_Visual_Grounding_and_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_Move_to_Understand_a_3D_Scene_Bridging_Visual_Grounding_and_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): Our approach bridges online exploration with dynamically spatial memory updates for lifelong grounding. ries presents significant challenges, and methods for effectively leveraging such data remain an open problem.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Embodied scene understanding requires not only comprehending visual-spatial information that has been observed but also determining where to explore next in the 3D physical world.
- **p. 1 / Abstract - extractive body cue:** Existing 3D Vision-Language (3D-VL) models primarily focus on grounding objects in static observations from 3D reconstruction, such as meshes and point clouds, but lack the ...
- **p. 1 / Abstract - extractive body cue:** To address this limitation, we introduce Move to Understand (MTU3D), a unified framework that integrates active perception with 3D vision-language learning, enabling embodied agents to ...
- **p. 1 / Abstract - extractive body cue:** This is achieved by three key innovations: 1) Online query-based representation learning, enabling direct spatial memory construction from RGB-D frames, eliminating the need for explicit ...
- **p. 1 / Abstract - extractive body cue:** 2) A unified objective for grounding and exploring, which represents unexplored locations as frontier queries and jointly optimizes object grounding and frontier selection.
- **p. 2 / 1. Introduction - extractive body cue:** Our approach bridges online exploration with dynamically spatial memory updates for lifelong grounding. ries presents significant challenges, and methods for effectively leveraging such data remain ...
- **p. 2 / 1. Introduction - extractive body cue:** In contrast, reinforcement learning (RL)-based embodied agents can explore environments but often struggle with sample inefficiency [71], poor generalization due to limited training data [20, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Our approach bridges online exploration with dynamically spatial memory updates for lifelong grounding. ries presents significant challenges, and methods for effectively leveraging ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | (a) 3D-VL Model (b) End-to-End RL (c) MTU3D (Ours) Full RGB-D Video Time World Visual Grounding Model Explicit Mesh Open loop Single ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | D-VL, Model, End-to-End, MTU3D, Ours, Full, RGB-D, Video, Time, World | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | unified, decision, scores, optimized, binary, cross-entropy, loss, teaching | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: D-VL, Model, End-to-End, MTU3D, Ours, Full, RGB-D, Video, Time, World | p. 2 (1. Introduction), p. 3 (Method), p. 5 (3.4. Vision-Language-Exploration Training) |
| Decision / output variable | path/waypoint/velocity; body terms: main, contributions, summarized, follows, present, MTU3D, bridging, visual | p. 3 (Method), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: unified, decision, scores, optimized, binary, cross-entropy, loss, teaching | p. 3 (Method), p. 5 (3.4. Vision-Language-Exploration Training), p. 5 (3.4. Vision-Language-Exploration Training) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (Method), p. 5 (3.4. Vision-Language-Exploration Training), p. 3 (Method) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (4.2. Quantitative Results), p. 6 (4.1. Experimental setting), p. 7 (4.2. Quantitative Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** In contrast, reinforcement learning (RL)-based embodied agents can explore environments but often struggle with sample inefficiency [71], poor generalization due to limited training data [20, ...

## What the Paper Changes

PDF contribution framing (p. 3 (Method), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (Method)): Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We propose a unified objective that ...

- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose Move to Understand (MTU3D), a unified framework that bridges visual grounding and exploration for versatile embodied navigation as shown ...
- **p. 2 / 1. Introduction - extractive body cue:** Our approach introduces three key innovations:
- **p. 3 / Method - extractive body cue:** When combined with a large vision-language model, serving as its trajectory generator, our approach improves the embodied question answering for LM-SR by 2.4% and LLM-SPL ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| no explicit assumption/failure cue | domain stress test only | not a paper claim |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 3 (Method), p. 5 (3.4. Vision-Language-Exploration Training), p. 3 (Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 3 (Method), p. 5 (3.4. Vision-Language-Exploration Training), p. 3 (Method), objective p. 3 (Method), p. 5 (3.4. Vision-Language-Exploration Training), p. 5 (3.4. Vision-Language-Exploration Training).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
