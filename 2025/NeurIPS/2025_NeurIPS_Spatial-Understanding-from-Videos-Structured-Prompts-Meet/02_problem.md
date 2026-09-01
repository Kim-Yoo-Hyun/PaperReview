# Problem - Spatial Understanding from Videos: Structured Prompts Meet Simulation Data

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=SBYCu5uJJf; PDF retrieval source: https://openreview.net/pdf/3c62afbe7e4670f87d9c26f52fd00d1be34082d5.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction)): However, performing 3D spatial reasoning from scanning videos presents two significant challenges: (1) Spatial Uncertainty.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Visual-spatial understanding, the ability to infer object relationships and layouts from visual input, is fundamental to downstream tasks such as robotic navigation and embodied interaction.
- **p. 1 / Abstract - extractive PDF cue:** However, existing methods face spatial uncertainty and data scarcity, limiting the 3D spatial reasoning capability of pre-trained visionlanguage models (VLMs).
- **p. 1 / Abstract - extractive PDF cue:** To address these challenges, we present a unified framework for enhancing 3D spatial reasoning in pre-trained VLMs without modifying their architecture.
- **p. 1 / Abstract - extractive PDF cue:** This framework combines SpatialMind, a structured prompting strategy that decomposes complex scenes and questions into interpretable reasoning steps, with ScanForgeQA, a scalable question-answering dataset built ...
- **p. 1 / Abstract - extractive PDF cue:** Extensive experiments across multiple benchmarks demonstrate the individual and combined effectiveness of our prompting and fine-tuning strategies, and yield insights that may inspire future research ...
- **p. 1 / 1 Introduction - extractive PDF cue:** However, performing 3D spatial reasoning from scanning videos presents two significant challenges: (1) Spatial Uncertainty.
- **p. 1 / 1 Introduction - extractive PDF cue:** These limitations motivate the pursuit of vision-only solutions that operate on scanning videos or multi-view images of scenes.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, performing 3D spatial reasoning from scanning videos presents two significant challenges: (1) Spatial Uncertainty. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Visual-spatial understanding, the ability to infer object relationships and layouts from visual input, is fundamental to downstream tasks such as robotic navigation ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Visual-spatial, understanding, ability, infer, object, relationships, layouts, visual, input, fundamental | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | contributions, summarized, follows, introduce, SpatialMind, spatial, prompting, strategy | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Visual-spatial, understanding, ability, infer, object, relationships, layouts, visual, input, fundamental | p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Decision / output variable | geometry/map/query r; body terms: contributions, summarized, follows, introduce, SpatialMind, spatial, prompting, strategy | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (A B) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Specifically, adopt, HoloDeck, generation, framework, leverages, LLMs, parse | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (A B), p. 6 (A B), p. 6 (A B) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (5 Experiments), p. 9 (5 Experiments), p. 8 (5 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive PDF cue:** These limitations motivate the pursuit of vision-only solutions that operate on scanning videos or multi-view images of scenes.
- **p. 2 / 1 Introduction - extractive PDF cue:** To address these challenges, we propose a dual approach for enhancing 3D spatial reasoning in pre-trained VLMs, without modifying their underlying architecture.
- **p. 2 / 1 Introduction - extractive PDF cue:** Moreover, these datasets involve scans of real-world scenes, which leads to poor scalability.

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (A B), p. 1 (Abstract), p. 5 (A B)): Our contributions are summarized as follows: • We introduce SpatialMind, a spatial prompting strategy that decomposes spatial reasoning into structured steps, enabling pre-trained VLMs to perform multi-step inference over spatial ...

- **p. 2 / 1 Introduction - extractive PDF cue:** To address these challenges, we propose a dual approach for enhancing 3D spatial reasoning in pre-trained VLMs, without modifying their underlying architecture.
- **p. 5 / A B - extractive PDF cue:** The final dataset consists of 34,116 single-room scenes across six common categories: bedroom, kitchen, bathroom, living room, dining room, and storage room.
- **p. 1 / Abstract - extractive PDF cue:** This framework combines SpatialMind, a structured prompting strategy that decomposes complex scenes and questions into interpretable reasoning steps, with ScanForgeQA, a scalable question-answering dataset built ...
- **p. 5 / A B - extractive PDF cue:** Each scene is scanned using two complementary strategies designed to emulate natural human visual exploration: Orbit Scan.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | For embedding (e.g., fitting an item into a drawer), the object's height must also fall within the bounds ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | In Case (a), Qwen2.5-VL-7B fails to produce the correct directional prediction, likely due to its limited capacity for ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Case (b) involves a simpler spatial reasoning task, however, Qwen2.5-VL-7B still fails, potentially due to insufficient object localization. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | These results validate the robustness of our approach and confirm its applicability across diverse spatial tasks and datasets. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 1 (Abstract), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
