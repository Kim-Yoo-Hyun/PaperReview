# Method - MeshLLM: Empowering Large Language Models to Progressively Understand and Generate 3D Mesh

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (3 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh)): SamPart3D is pretrained on Objaverse [2] with a 3D backbone network designed to extract visual features.

## Method Body Digest

- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** SamPart3D is pretrained on Objaverse [2] with a 3D backbone network designed to extract visual features.
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** This ensures compliance with the token length constraints of large language models, effectively expanding the scale of trainable data.
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** This strategy provides more accurate semantic information for mesh parts but is time-consuming and incurs API query costs.
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** For mesh-derived dense point clouds, FPS begins with a random point and iteratively chooses the farthest point to yield N center points.
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** We begin by densely sampling point clouds from the mesh and then apply farthest point sampling (FPS) and KNN to identify central points and point ...

## Design Rationale

- **p. 2 / 2.2. Training Strategy Analysis - extractive body cue:** In MeshLLM, we introduce a progressive training strategy that begins with KNN-based Primitive-Mesh samples, followed by Semantic-based Primitive-Mesh samples, and concludes with training on specific ...
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** SamPart3D is pretrained on Objaverse [2] with a 3D backbone network designed to extract visual features.

## Source Evidence Cues

- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** SamPart3D is pretrained on Objaverse [2] with a 3D backbone network designed to extract visual features.
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** This ensures compliance with the token length constraints of large language models, effectively expanding the scale of trainable data.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | SamPart3D is pretrained on Objaverse [2] with a 3D backbone network designed to extract visual features. | p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | This ensures compliance with the token length constraints of large language models, effectively expanding the scale of trainable data. | p. 1 (1.1. Construction of Primitive-Mesh) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | SamPart3D is pretrained on Objaverse [2] with a 3D backbone network designed to extract visual features. | p. 1 (1.1. Construction of Primitive-Mesh) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** This strategy provides more accurate semantic information for mesh parts but is time-consuming and incurs API query costs.
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** This ensures compliance with the token length constraints of large language models, effectively expanding the scale of trainable data.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.2. Metric Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | mesh-derived, dense, point, clouds, FPS, begins, random, iteratively, chooses, farthest, yield, center, points, begin | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | mesh-derived, dense, point, clouds, FPS, begins, random, iteratively, chooses, farthest | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | MeshLLM, introduce, progressive, training, strategy, begins, KNN-based, Primitive-Mesh, samples, followed | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | strategy, provides, more, accurate, semantic, information, mesh, parts, time-consuming, incurs | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** For mesh-derived dense point clouds, FPS begins with a random point and iteratively chooses the farthest point to yield N center points.
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** We begin by densely sampling point clouds from the mesh and then apply farthest point sampling (FPS) and KNN to identify central points and point ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | For mesh-derived dense point clouds, FPS begins with a random point and iteratively chooses the farthest point to yield N center points. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We begin by densely sampling point clouds from the mesh and then apply farthest point sampling (FPS) and KNN to identify central ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** SamPart3D is pretrained on Objaverse [2] with a 3D backbone network designed to extract visual features.
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** This ensures compliance with the token length constraints of large language models, effectively expanding the scale of trainable data.
- **p. 1 / 2.1. Shape Novelty Analysis - extractive body cue:** We compute the Chamfer Distance between samples to identify the three most similar training meshes to the generated meshes for comparison.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** SamPart3D, pretrained, Objaverse, backbone, network, designed, extract, visual, features, ensures, compliance, token, length, constraints, large, language, models, effectively, expanding, scale.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We utilize 128 A800 GPUs and spent over three days constructing this dataset. | p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh) |
| Semantic / temporal fusion | And NX in the 1-NNA metric is a point cloud that is closest to X in both the generated and reference dataset, ... | p. 1 (1.2. Metric Details), p. 1 (2.1. Shape Novelty Analysis) |
| Robot query / planning handoff | Table 1. Effect of the training order. MeshLLMR refers to the reversed training order, where the Semantic-based Primitive-Mesh is trained first, followed ... | p. 3 (Figure/Table caption), p. 1 (1.1. Construction of Primitive-Mesh) |

## Failure and Ablation Link

- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. Effect of the training order. MeshLLMR refers to the reversed training order, where the Semantic-based Primitive-Mesh is trained first, followed by the KNN-based ...
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** SamPart3D is pretrained on Objaverse [2] with a 3D backbone network designed to extract visual features.
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** To obtain semantic labels for each part, we render multiview images and annotate the corresponding 2D regions for each segmented 3D component.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Failure case. The limited semantic dataset size reduces text-geometry alignment for more fine-grained generations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh), objective p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh), temporal p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
