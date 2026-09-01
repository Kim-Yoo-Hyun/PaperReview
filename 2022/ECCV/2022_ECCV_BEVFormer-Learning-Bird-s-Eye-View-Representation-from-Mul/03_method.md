# Method - BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2203.17270; PDF retrieval source: https://arxiv.org/pdf/2203.17270. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 16 (A.3 Task Heads), p. 16 (A.3 Task Heads)): Following [47], we use 900 object queries and keep 300 predicted boxes with highest confidence scores during inference.

## Method Body Digest

- **p. 16 / A.3 Task Heads - extractive PDF cue:** Following [47], we use 900 object queries and keep 300 predicted boxes with highest confidence scores during inference.
- **p. 16 / A.3 Task Heads - extractive PDF cue:** Map Query BEV Feature 𝐵𝑡 Mask Result Multi-Head Attention Add & Norm Feed Forward Refined Query Add & Norm Query Next Layer Attention Maps Figure ...
- **p. 16 / A.3 Task Heads - extractive PDF cue:** Only L1 loss and L1 cost are used during training phase.
- **p. 16 / A.4 Spatial Cross-Attention - extractive PDF cue:** However, the computational cost of this straightforward way is unaffordable.
- **p. 2 / 1 Introduction - extractive PDF cue:** Our main contributions are as follows: • We propose BEVFormer, a spatiotemporal transformer encoder that projects multi-camera and/or timestamp input to BEV representations.
- **p. 2 / 1 Introduction - extractive PDF cue:** For the human visual perception system, temporal information plays a crucial role in inferring the motion state of objects and identifying occluded objects, and many ...
- **p. 3 / 1 Introduction - extractive PDF cue:** For the map segmentation task, we also achieve the state-ofthe-art performance, more than 5.0 points higher than Lift-Splat [32] on the most challenging lane segmentation.
- **p. 3 / 1 Introduction - extractive PDF cue:** • We designed learnable BEV queries along with a spatial cross-attention layer and a temporal self-attention layer to lookup spatial features from cross cameras and ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** Our main contributions are as follows: • We propose BEVFormer, a spatiotemporal transformer encoder that projects multi-camera and/or timestamp input to BEV representations.
- **p. 2 / 1 Introduction - extractive PDF cue:** To this end, we present a transformer-based bird's-eye-view (BEV) encoder, termed BEVFormer, which can effectively aggregate spatiotemporal features from multi-view cameras and history BEV features.
- **p. 3 / 1 Introduction - extractive PDF cue:** • We designed learnable BEV queries along with a spatial cross-attention layer and a temporal self-attention layer to lookup spatial features from cross cameras and ...

## Source Evidence Cues

- **p. 16 / A.3 Task Heads - extractive PDF cue:** Following [47], we use 900 object queries and keep 300 predicted boxes with highest confidence scores during inference.
- **p. 16 / A.3 Task Heads - extractive PDF cue:** Map Query BEV Feature 𝐵𝑡 Mask Result Multi-Head Attention Add & Norm Feed Forward Refined Query Add & Norm Query Next Layer Attention Maps Figure ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Following [47], we use 900 object queries and keep 300 predicted boxes with highest confidence scores during inference. | p. 16 (A.3 Task Heads), p. 16 (A.3 Task Heads) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Map Query BEV Feature 𝐵𝑡 Mask Result Multi-Head Attention Add & Norm Feed Forward Refined Query Add & Norm Query Next Layer ... | p. 16 (A.3 Task Heads) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Following [47], we use 900 object queries and keep 300 predicted boxes with highest confidence scores during inference. | p. 16 (A.3 Task Heads) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 16 / A.3 Task Heads - extractive PDF cue:** Only L1 loss and L1 cost are used during training phase.
- **p. 16 / A.4 Spatial Cross-Attention - extractive PDF cue:** However, the computational cost of this straightforward way is unaffordable.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 16 (A.3 Task Heads).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | main, contributions, follows, BEVFormer, spatiotemporal, transformer, encoder, projects, multi-camera, and/or, timestamp, input, BEV, representations | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | main, contributions, follows, BEVFormer, spatiotemporal, transformer, encoder, projects, multi-camera, and/or | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | main, contributions, follows, BEVFormer, spatiotemporal, transformer, encoder, projects, multi-camera, and/or | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Only, loss, cost, during, training, phase, However, computational, straightforward, unaffordable | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive PDF cue:** Our main contributions are as follows: • We propose BEVFormer, a spatiotemporal transformer encoder that projects multi-camera and/or timestamp input to BEV representations.
- **p. 2 / 1 Introduction - extractive PDF cue:** For the human visual perception system, temporal information plays a crucial role in inferring the motion state of objects and identifying occluded objects, and many ...
- **p. 3 / 1 Introduction - extractive PDF cue:** For the map segmentation task, we also achieve the state-ofthe-art performance, more than 5.0 points higher than Lift-Splat [32] on the most challenging lane segmentation.
- **p. 3 / 1 Introduction - extractive PDF cue:** • We designed learnable BEV queries along with a spatial cross-attention layer and a temporal self-attention layer to lookup spatial features from cross cameras and ...
- **p. 16 / A Implementation Details - extractive PDF cue:** In this section, we provide more implementation details of the proposed method and experiments.
- **p. 16 / A.3 Task Heads - extractive PDF cue:** Map Query BEV Feature 𝐵𝑡 Mask Result Multi-Head Attention Add & Norm Feed Forward Refined Query Add & Norm Query Next Layer Attention Maps Figure ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Note that the five images at each frame provided by Waymo have only about 252° horizontal FOV, but the provided annotated labels ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We also adapt BEVFormer into a static model called BEVFormer-S via adjusting the temporal self-attention into a vanilla self-attention without using history ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | We also adapt BEVFormer into a static model called BEVFormer-S via adjusting the temporal self-attention into a vanilla self-attention without using history ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Following previous methods [47, 56], we train all models with 24 epochs, a batch size of 1 (containing 6 view images) per ... | hardware, batch and throughput |

## Training vs Inference

- **p. 16 / A.3 Task Heads - extractive PDF cue:** Following [47], we use 900 object queries and keep 300 predicted boxes with highest confidence scores during inference.
- **p. 16 / A.1 Traning Strategy - extractive PDF cue:** Following previous methods [47, 56], we train all models with 24 epochs, a batch size of 1 (containing 6 view images) per GPU, a learning ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Following, object, queries, keep, predicted, boxes, highest, confidence, scores, during, inference, Map, Query, BEV, Feature, Mask, Result, Multi-Head, Attention, Add.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The nuScenes dataset [4] contains 1000 scenes of roughly 20s duration each, and the key samples are annotated at 2Hz. | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Semantic / temporal fusion | Our method outperforms previous best method DETR3D [47] over 9.2 points on val set (51.7% NDS vs. | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Robot query / planning handoff | Figure 3: The detection results of subsets with different visibilities. We divide the nuScenes val set into four subsets based on the ... | p. 10 (Figure/Table caption), p. 11 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / 4 Experiments - extractive PDF cue:** To eliminate the effect of task heads and compare other BEV generating methods fairly, we use VPN [30] and Lift-Splat [32] to replace our BEVFormer ...
- **p. 7 / 4 Experiments - extractive PDF cue:** On the test set, our model achieves 56.9% NDS without bells and whistles, 9.0 points 7
- **p. 18 / Figure/Table caption - extractive PDF cue:** Table 8: Ablation Experiments on nuScenes val set. "A." indicates aligning history BEV fea- tures with ego-motion. "R." indicates randomly sampling 4 frames from 5 ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 5: The detection results of different methods with various BEV encoders on nuScenes val set. "Memory" is the consumed GPU memory during training. *: ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 4: 3D detection and map segmentation results on nuScenes val set. Comparison of training segmentation and detection tasks jointly or not. *: We use ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: 3D detection results on nuScenes test set. ∗notes that VoVNet-99 (V2-99) [21] was pre-trained on the depth estimation task with extra data [31]. ...
- **p. 9 / C R101 - extractive PDF cue:** However, the jointly trained model does not perform as well as individually trained models for road and lane segmentation, which is a common phenomenon called ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 16 (A.3 Task Heads), p. 16 (A.3 Task Heads), objective p. 16 (A.3 Task Heads), p. 16 (A.4 Spatial Cross-Attention), temporal p. 7 (4 Experiments), p. 7 (4 Experiments), p. 4 (2 Related Work), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
