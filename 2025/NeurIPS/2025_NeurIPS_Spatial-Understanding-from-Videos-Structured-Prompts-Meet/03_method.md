# Method - Spatial Understanding from Videos: Structured Prompts Meet Simulation Data

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=SBYCu5uJJf; PDF retrieval source: https://openreview.net/pdf/3c62afbe7e4670f87d9c26f52fd00d1be34082d5.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 6 (A B), p. 5 (A B)): To address these challenges, we propose a dual approach for enhancing 3D spatial reasoning in pre-trained VLMs, without modifying their underlying architecture.

## Method Body Digest

- **p. 2 / 1 Introduction - extractive PDF cue:** To address these challenges, we propose a dual approach for enhancing 3D spatial reasoning in pre-trained VLMs, without modifying their underlying architecture.
- **p. 2 / 1 Introduction - extractive PDF cue:** Our contributions are summarized as follows: • We introduce SpatialMind, a spatial prompting strategy that decomposes spatial reasoning into structured steps, enabling pre-trained VLMs to ...
- **p. 1 / 1 Introduction - extractive PDF cue:** In the absence of explicit depth information, models must infer 3D structure from inherently limited 2D observations.
- **p. 1 / 1 Introduction - extractive PDF cue:** As intelligent systems become increasingly embedded in real-world applications such as autonomous driving [4, 5, 6], robotic navigation [7, 8, 9], and augmented reality [10, ...
- **p. 6 / A B - extractive PDF cue:** This category targets interobject spatial relationships, requiring models to infer positional and geometric properties such as distance, orientation, and contact.
- **p. 5 / A B - extractive PDF cue:** We define a circular trajectory centered in the room at a height of approximately 1.5 meters, corresponding to typical adult eye level.
- **p. 6 / A B - extractive PDF cue:** For contact relationships, object dimensions are also considered to determine physical adjacency.
- **p. 5 / A B - extractive PDF cue:** Specifically, we adopt HoloDeck [48], a 3D generation framework that leverages LLMs to parse natural language prompts, retrieve matching assets from large-scale 3D object repositories ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** Our contributions are summarized as follows: • We introduce SpatialMind, a spatial prompting strategy that decomposes spatial reasoning into structured steps, enabling pre-trained VLMs to ...
- **p. 2 / 1 Introduction - extractive PDF cue:** To address these challenges, we propose a dual approach for enhancing 3D spatial reasoning in pre-trained VLMs, without modifying their underlying architecture.
- **p. 5 / A B - extractive PDF cue:** The final dataset consists of 34,116 single-room scenes across six common categories: bedroom, kitchen, bathroom, living room, dining room, and storage room.

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive PDF cue:** To address these challenges, we propose a dual approach for enhancing 3D spatial reasoning in pre-trained VLMs, without modifying their underlying architecture.
- **p. 2 / 1 Introduction - extractive PDF cue:** Our contributions are summarized as follows: • We introduce SpatialMind, a spatial prompting strategy that decomposes spatial reasoning into structured steps, enabling pre-trained VLMs to ...
- **p. 1 / 1 Introduction - extractive PDF cue:** In the absence of explicit depth information, models must infer 3D structure from inherently limited 2D observations.
- **p. 1 / 1 Introduction - extractive PDF cue:** As intelligent systems become increasingly embedded in real-world applications such as autonomous driving [4, 5, 6], robotic navigation [7, 8, 9], and augmented reality [10, ...
- **p. 6 / A B - extractive PDF cue:** This category targets interobject spatial relationships, requiring models to infer positional and geometric properties such as distance, orientation, and contact.
- **p. 5 / A B - extractive PDF cue:** We define a circular trajectory centered in the room at a height of approximately 1.5 meters, corresponding to typical adult eye level.
- **p. 6 / A B - extractive PDF cue:** For contact relationships, object dimensions are also considered to determine physical adjacency.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To address these challenges, we propose a dual approach for enhancing 3D spatial reasoning in pre-trained VLMs, without modifying their underlying architecture. | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Our contributions are summarized as follows: • We introduce SpatialMind, a spatial prompting strategy that decomposes spatial reasoning into structured steps, enabling ... | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | In the absence of explicit depth information, models must infer 3D structure from inherently limited 2D observations. | p. 1 (1 Introduction), p. 1 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / A B - extractive PDF cue:** Specifically, we adopt HoloDeck [48], a 3D generation framework that leverages LLMs to parse natural language prompts, retrieve matching assets from large-scale 3D object repositories ...
- **p. 6 / A B - extractive PDF cue:** Feasibility is determined by comparing object dimensions.
- **p. 6 / A B - extractive PDF cue:** A typical example is operation feasibility ("Considering only object dimensions, is it feasible to place the television on the table?").
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Visual-spatial, understanding, ability, infer, object, relationships, layouts, visual, input, fundamental, downstream, tasks, robotic, navigation | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Visual-spatial, understanding, ability, infer, object, relationships, layouts, visual, input, fundamental | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, follows, introduce, SpatialMind, spatial, prompting, strategy, decomposes, reasoning | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Specifically, adopt, HoloDeck, generation, framework, leverages, LLMs, parse, natural, language | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive PDF cue:** Visual-spatial understanding, the ability to infer object relationships and layouts from visual input, is fundamental to downstream tasks such as robotic navigation and embodied interaction.
- **p. 1 / 1 Introduction - extractive PDF cue:** In the absence of explicit depth information, models must infer 3D structure from inherently limited 2D observations.
- **p. 2 / 1 Introduction - extractive PDF cue:** Our contributions are summarized as follows: • We introduce SpatialMind, a spatial prompting strategy that decomposes spatial reasoning into structured steps, enabling pre-trained VLMs to ...
- **p. 2 / 1 Introduction - extractive PDF cue:** To address these challenges, we propose a dual approach for enhancing 3D spatial reasoning in pre-trained VLMs, without modifying their underlying architecture.
- **p. 5 / A B - extractive PDF cue:** Upon arrival, another 360-degree rotation is performed, again capturing 30 images.
- **p. 5 / A B - extractive PDF cue:** An image is captured every 5 degrees of rotation, resulting in 72 frames per orbit scan.
- **p. 6 / A B - extractive PDF cue:** GPT-4o Qwen2.5-VL-7B Qwen2.5-VL-72B 34.0 40.8 37.2 39.2 39.2 44.0 Base +Map +Grid +Des Figure 3: Effects of different scene expression.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Effectively addressing this challenge demands multi-step logical reasoning across frames to reconstruct coherent spatial layouts. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | This framework combines SpatialMind, a structured prompting strategy that decomposes complex scenes and questions into interpretable reasoning steps, with ScanForgeQA, a scalable ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | 8 16 24 32 Frame 128 256 384 512 Resolution 4 5 6 7 Gain (+Both - Base) 4.5 5.0 5.5 6.0 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive PDF cue:** To address these challenges, we propose a dual approach for enhancing 3D spatial reasoning in pre-trained VLMs, without modifying their underlying architecture.
- **p. 2 / 1 Introduction - extractive PDF cue:** Our contributions are summarized as follows: • We introduce SpatialMind, a spatial prompting strategy that decomposes spatial reasoning into structured steps, enabling pre-trained VLMs to ...
- **p. 1 / Abstract - extractive PDF cue:** This framework combines SpatialMind, a structured prompting strategy that decomposes complex scenes and questions into interpretable reasoning steps, with ScanForgeQA, a scalable question-answering dataset built ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our contributions are summarized as follows: • We introduce SpatialMind, a spatial prompting strategy that decomposes spatial reasoning into structured steps, enabling pre-trained VLMs to ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** address, challenges, dual, enhancing, spatial, reasoning, pre-trained, VLMs, without, modifying, underlying, architecture, contributions, summarized, follows, introduce, SpatialMind, prompting, strategy, decomposes.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Importantly, both datasets and the VSI-Bench benchmark originate from the same source (i.e., ScanNet [31]), resulting in minimal data discrepancy. | p. 9 (5 Experiments), p. 8 (5 Experiments) |
| Semantic / temporal fusion | Our method consistently outperforms the baseline across all settings, with performance further improving as the number of frames and resolution increase. | p. 9 (5 Experiments), p. 7 (5 Experiments) |
| Robot query / planning handoff | Figure 6: Two examples from VSI-Bench comparing predictions from Qwen2.5-VL-7B and Ours. this strategy achieves improved performance, surpassing the original Qwen2.5-VL-7B baseline, ... | p. 9 (Figure/Table caption), p. 8 (5 Experiments) |

## Failure and Ablation Link

- **p. 9 / 5 Experiments - extractive PDF cue:** As shown in Table 4, both variants independently improve spatial reasoning performance, but are less effective than the full combined prompt.
- **p. 9 / 5 Experiments - extractive PDF cue:** 5.2 Ablation Study In this section, we explored the impact of various design choices, including prompting strategies, fine-tuning datasets, frame sampling strategies, and input resolution, ...
- **p. 7 / 5 Experiments - extractive PDF cue:** Across all models, a consistent trend emerges: the +Des variant outperforms others, followed by 7
- **p. 8 / 5 Experiments - extractive PDF cue:** 8 16 24 32 Frame 128 256 384 512 Resolution 4 5 6 7 Gain (+Both - Base) 4.5 5.0 5.5 6.0 6.5 Figure 5: ...
- **p. 25 / Figure/Table caption - extractive PDF cue:** Figure 8: Distribution of room types in the ScanForgeQA dataset. are consistent with those reported in our main analysis, further reinforcing the effectiveness and generalizability ...
- **p. 8 / 5 Experiments - extractive PDF cue:** Does fine-tuning affect performance on other tasks?
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1: Illustration of our SpatailMind prompting strategy. 3 SpatialMind Prompting Strategy As shown in Figure 1, our SpatialMind prompting strategy consists of two main ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 6 (A B), p. 5 (A B), objective p. 5 (A B), p. 6 (A B), p. 6 (A B), temporal p. 1 (1 Introduction), p. 1 (Abstract), p. 8 (5 Experiments), p. 8 (5 Experiments), p. 9 (5 Experiments), p. 9 (5 Experiments).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
