# Method - BEVDepth: Acquisition of Reliable Depth for Multi-view 3D Object Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2206.10092; PDF retrieval source: https://arxiv.org/pdf/2206.10092. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (1 Introduction), p. 1 (1 Introduction)): They first "lift" multi-view features to 3D frustums using estimated depth, then "splat" frustums onto a reference plane, usually being a plane in Bird's-Eye-View (BEV).

## Method Body Digest

- **p. 1 / 1 Introduction - extractive PDF cue:** They first "lift" multi-view features to 3D frustums using estimated depth, then "splat" frustums onto a reference plane, usually being a plane in Bird's-Eye-View (BEV).
- **p. 1 / 1 Introduction - extractive PDF cue:** Based on this observation, we point out that the depth learning mechanism in existing Lift-splat brings three deficiencies: • Inaccurate Depth Since the depth prediction ...
- **p. 1 / 1 Introduction - extractive PDF cue:** While LiDAR-based methods have demonstrated their ability to deliver trustworthy 3D detection results, multi-view camera-based methods have recently attracted increasing attention because of their lower ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Input Image Lift-splat BEVDepth Figure 1: Depth estimation results in Lift-splat detector and BEVDepth.
- **p. 1 / Abstract - extractive PDF cue:** Our work is based on a key observation - depth estimation in recent approaches is surprisingly inadequate given the fact that depth is essential to ...
- **p. 1 / Abstract - extractive PDF cue:** Aided by customized Efficient Voxel Pooling and multi-frame mechanism, BEVDepth achieves the new stateof-the-art 60.9% NDS on the challenging nuScenes test set while maintaining high ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Dashed boxes highlight the regions that Lift-splat detector makes "relatively" accurate depth predictions in, usually being the attaching regions between objects and the ground.

## Design Rationale

- **p. 1 / 1 Introduction - extractive PDF cue:** Therefore, in this work, we introduce BEVDepth, a new multi-view 3D detector that leverages depth supervision derives from point clouds to guide depth learning.
- **p. 1 / 1 Introduction - extractive PDF cue:** The BEV representation is non-trivial since it not only enables an end-to-end training scheme of a multiple input cameras system but also provides a unified ...

## Source Evidence Cues

- **p. 1 / 1 Introduction - extractive PDF cue:** They first "lift" multi-view features to 3D frustums using estimated depth, then "splat" frustums onto a reference plane, usually being a plane in Bird's-Eye-View (BEV).
- **p. 1 / 1 Introduction - extractive PDF cue:** Based on this observation, we point out that the depth learning mechanism in existing Lift-splat brings three deficiencies: • Inaccurate Depth Since the depth prediction ...
- **Detected method headings:** Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | They first "lift" multi-view features to 3D frustums using estimated depth, then "splat" frustums onto a reference plane, usually being a plane ... | p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Based on this observation, we point out that the depth learning mechanism in existing Lift-splat brings three deficiencies: • Inaccurate Depth Since ... | p. 1 (1 Introduction) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | They first "lift" multi-view features to 3D frustums using estimated depth, then "splat" frustums onto a reference plane, usually being a plane ... | p. 1 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / 1 Introduction - extractive PDF cue:** While LiDAR-based methods have demonstrated their ability to deliver trustworthy 3D detection results, multi-view camera-based methods have recently attracted increasing attention because of their lower ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Based on this observation, we point out that the depth learning mechanism in existing Lift-splat brings three deficiencies: • Inaccurate Depth Since the depth prediction ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 1 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Input, Image, Lift-splat, BEVDepth, Figure, Depth, estimation, detector, observation, recent, approaches, surprisingly, inadequate, given | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Input, Image, Lift-splat, BEVDepth, Figure, Depth, estimation, detector, observation, recent | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Therefore, introduce, BEVDepth, multi-view, detector, leverages, depth, supervision, derives, point | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | While, LiDAR-based, methods, have, demonstrated, ability, deliver, trustworthy, detection, multi-view | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive PDF cue:** Input Image Lift-splat BEVDepth Figure 1: Depth estimation results in Lift-splat detector and BEVDepth.
- **p. 1 / Abstract - extractive PDF cue:** Our work is based on a key observation - depth estimation in recent approaches is surprisingly inadequate given the fact that depth is essential to ...
- **p. 1 / Abstract - extractive PDF cue:** Aided by customized Efficient Voxel Pooling and multi-frame mechanism, BEVDepth achieves the new stateof-the-art 60.9% NDS on the challenging nuScenes test set while maintaining high ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Dashed boxes highlight the regions that Lift-splat detector makes "relatively" accurate depth predictions in, usually being the attaching regions between objects and the ground.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | DL, CA, DR and MF denotes Depth Loss, Camera-awareness, Depth Refinement Module and multi-frame, respectively. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Aided by customized Efficient Voxel Pooling and multi-frame mechanism, BEVDepth achieves the new stateof-the-art 60.9% NDS on the challenging nuScenes test set ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | 2019) uses GRU to reduce memory cost, MVSCRF (Xue et al. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | When compared to other methods, BEVDepth is trained for 20 epochs with CBGS. | hardware, batch and throughput |

## Training vs Inference

- **p. 1 / 1 Introduction - extractive PDF cue:** Based on this observation, we point out that the depth learning mechanism in existing Lift-splat brings three deficiencies: • Inaccurate Depth Since the depth prediction ...
- **p. 6 / 5 Experiment - extractive PDF cue:** When compared to other methods, BEVDepth is trained for 20 epochs with CBGS.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** They, first, lift, multi-view, features, frustums, estimated, depth, then, splat, onto, reference, plane, usually, being, Bird, s-Eye-View, BEV, observation, point.
- **Relevant PDF headings:** Method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | There are 1000 scenarios in the dataset, which are divided into 700, 150, and 150 scenes for training, validation, and testing, respectively. | p. 6 (5 Experiment), p. 6 (5 Experiment) |
| Semantic / temporal fusion | Overall, our BEVDepth improves 4.0% mAP and 4.0% NDS compared to its baseline, showing the effectiveness of our innovations. | p. 6 (5 Experiment), p. 6 (5 Experiment) |
| Robot query / planning handoff | In the end, Depth Refinement Module improves 0.8% mAP. | p. 6 (5 Experiment), p. 6 (5 Experiment) |

## Failure and Ablation Link

- **p. 6 / 5 Experiment - extractive PDF cue:** For the ablation study, all experiments are trained for 24 epochs without using CBGS strategy (Zhu et al.
- **p. 6 / 5 Experiment - extractive PDF cue:** 5.2 Ablation Study Component Analysis As shown in Table 4, our vanilla BEVDepth achieves 28.2% mAP and 32.7% NDS.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 8: Comparison on the nuScenes test set. L denotes LiDAR and C denotes camera. BEVDepth uses pretrained VovNet as backbone. the resolution of the ...
- **p. 5 / 2 Related Work - extractive PDF cue:** If the 2.5D projection of a certain point cloud does not fall into the ith view, we simply discard it.
- **p. 5 / 2 Related Work - extractive PDF cue:** Benefiting from the decoupled nature of LSS (Philion and Fidler 2020), the camera-aware depth prediction module is isolated from the detection head and thus the ...
- **p. 6 / 5 Experiment - extractive PDF cue:** See Table 6, when we use 1×3 conv on CD ×W dimension, the information does not exchange along the depth axis, and
- **p. 4 / 2 Related Work - extractive PDF cue:** Such a phenomenon implies that the model without depth loss has a higher risk of over-fitting, and thus it may also be sensitive to the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (1 Introduction), p. 1 (1 Introduction), objective p. 1 (1 Introduction), p. 1 (1 Introduction), temporal p. 6 (5 Experiment), p. 1 (Abstract), p. 3 (2 Related Work), p. 3 (2 Related Work), p. 5 (2 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
