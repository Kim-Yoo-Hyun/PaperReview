# Method - BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2205.13542; PDF retrieval source: https://arxiv.org/pdf/2205.13542. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (III. METHOD), p. 2 (III. METHOD)): Given different sensory inputs, we first apply modality-specific encoders to extract their features.

## Method Body Digest

- **p. 2 / III. METHOD - extractive PDF cue:** Given different sensory inputs, we first apply modality-specific encoders to extract their features.
- **p. 2 / III. METHOD - extractive PDF cue:** We then apply the convolution-based BEV encoder to the unified BEV features to alleviate the local misalignment between different features.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** (in BEV) BEV Map Segmentation 3D Object Detection LiDAR Features Fused BEV Features LiDAR Point Cloud Multi-View RGB Images Task-Specific Heads … Flatten (along z-axis) ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** BEVFusion sets the new state-of-the-art 3D object detection performance on both nuScenes and Waymo benchmarks.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** We maintain both geometric structure and semantic density (see Figure 1c) and naturally support most 3D perception tasks (since their output space can be naturally ...
- **p. 3 / III. METHOD - extractive PDF cue:** log scale (a) Camera-to-BEV transformation (b) Efficient BEV pooling (c) Improvement breakdown Depth Grid Association Feat.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Then, we propose a specialized kernel with precomputation and interval reduction to eliminate this bottleneck, achieving more than 40× speedup.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** In this paper, we propose BEVFusion to unify multi-modal features in a shared bird's-eye view (BEV) representation space for task-agnostic learning.

## Source Evidence Cues

- **p. 2 / III. METHOD - extractive PDF cue:** Given different sensory inputs, we first apply modality-specific encoders to extract their features.
- **p. 2 / III. METHOD - extractive PDF cue:** We then apply the convolution-based BEV encoder to the unified BEV features to alleviate the local misalignment between different features.
- **Detected method headings:** III. METHOD (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Given different sensory inputs, we first apply modality-specific encoders to extract their features. | p. 2 (III. METHOD), p. 2 (III. METHOD) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We then apply the convolution-based BEV encoder to the unified BEV features to alleviate the local misalignment between different features. | p. 2 (III. METHOD) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Given different sensory inputs, we first apply modality-specific encoders to extract their features. | p. 2 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, different, sensory, inputs, first, apply, modality-specific, encoders, extract, features, BEV, Map, Segmentation, Object | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Given, different, sensory, inputs, first, apply, modality-specific, encoders, extract, features | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Then, specialized, kernel, precomputation, interval, reduction, eliminate, bottleneck, achieving, more | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / III. METHOD - extractive PDF cue:** Given different sensory inputs, we first apply modality-specific encoders to extract their features.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** (in BEV) BEV Map Segmentation 3D Object Detection LiDAR Features Fused BEV Features LiDAR Point Cloud Multi-View RGB Images Task-Specific Heads … Flatten (along z-axis) ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** BEVFusion sets the new state-of-the-art 3D object detection performance on both nuScenes and Waymo benchmarks.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** We maintain both geometric structure and semantic density (see Figure 1c) and naturally support most 3D perception tasks (since their output space can be naturally ...
- **p. 3 / III. METHOD - extractive PDF cue:** log scale (a) Camera-to-BEV transformation (b) Efficient BEV pooling (c) Improvement breakdown Depth Grid Association Feat.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | As in Table I, BEVFusion achieves state-of-the-art results on the nuScenes detection benchmark, with close-to-real-time (8.4 FPS) inference speed on a desktop ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Our framework can be easily extended to support other types of sensors (such as radars and event-based cameras) and other 3D perception ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | As in Table I, BEVFusion achieves state-of-the-art results on the nuScenes detection benchmark, with close-to-real-time (8.4 FPS) inference speed on a desktop ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** We also measure the single-inference #MACs and latency on an RTX3090 GPU for all opensource methods.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** As in Table I, BEVFusion achieves state-of-the-art results on the nuScenes detection benchmark, with close-to-real-time (8.4 FPS) inference speed on a desktop GPU.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Given, different, sensory, inputs, first, apply, modality-specific, encoders, extract, features, then, convolution-based, BEV, encoder, unified, alleviate, local, misalignment, between, Map.
- **Relevant PDF headings:** III. METHOD (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We evaluate our method on nuScenes [59] and Waymo [60], which are large-scale datasets for 3D perception with >40k annotated scenes. | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Semantic / temporal fusion | Fig. 4: BEVFusion outperforms state-of-the-art single- and multi-modality detectors under different LiDAR sparsity, object sizes and object distances, especially under more challenging ... | p. 6 (Figure/Table caption), p. 5 (IV. EXPERIMENTS) |
| Robot query / planning handoff | Consequently, BEVFusion can achieve the same performance with much smaller resolution for the camera inputs, resulting in significantly lower MACs. | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** We use a single model without any test-time augmentation for both val and test results.
- **p. 3 / A C - extractive PDF cue:** On the one hand, the LiDARto-BEV projection flattens the sparse LiDAR features along the height dimension, thus does not create geometric distortion in Figure 1a.
- **p. 4 / A C - extractive PDF cue:** Our method could potentially benefit from more accurate depth estimation (e.g., supervising the view transformer with groundtruth depth [42], [53]), which we leave for future ...
- **p. 4 / A C - extractive PDF cue:** This kernel removes the dependency between outputs (thus does not require multi-level tree reduction) and avoids writing the partial sums to the DRAM, reducing the ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** IV: BEVFusion is robust under different lighting and weather conditions, significantly boosting the performance single-modality models under challenging rainy(+10.7) and nighttime(+12.8) scenes.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (III. METHOD), p. 2 (III. METHOD), objective 본문 anchor 없음, temporal p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 1 (Abstract), p. 1 (Abstract), p. 3 (A C).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
