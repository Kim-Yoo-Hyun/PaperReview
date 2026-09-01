# Method - QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=eZNdkwJYbN; PDF retrieval source: https://openreview.net/pdf/cc6e0a2d054469a238a6da05b30dce8f439f11f3.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 16 (C Additional Implementation Details), p. 16 (C Additional Implementation Details)): To clarify, we take the QuadricFormer with N superquadrics as an example and describe the process as follows: Initial Training: We first train a QuadricFormer with B=4 quadric-encoder blocks and ...

## Method Body Digest

- **p. 16 / C Additional Implementation Details - extractive PDF cue:** To clarify, we take the QuadricFormer with N superquadrics as an example and describe the process as follows: Initial Training: We first train a QuadricFormer ...
- **p. 16 / C Additional Implementation Details - extractive PDF cue:** To address this, we introduce the prunning-and-splitting module: · We divide all superquadrics in Q into two groups based on the product of their scales: ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Extensive experiments on the nuScenes and KITTI-360 dataset demonstrate that our QuadricFormer achieves state-of-the-art performance with superior efficiency.
- **p. 2 / 1 Introduction - extractive PDF cue:** This imposes a strong ellipsoidal shape prior to Gaussians and severely constrains their capacity to model diverse geometries.

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we propose an efficient and expressive object-centric 3D representation using superquadrics [1] as scene primitives.
- **p. 2 / 1 Introduction - extractive PDF cue:** Building on this representation, we introduce QuadricFormer, a superquadric-based framework for efficient 3D semantic occupancy prediction.
- **p. 16 / C Additional Implementation Details - extractive PDF cue:** To address this, we introduce the prunning-and-splitting module: · We divide all superquadrics in Q into two groups based on the product of their scales: ...

## Source Evidence Cues

- **p. 16 / C Additional Implementation Details - extractive PDF cue:** To clarify, we take the QuadricFormer with N superquadrics as an example and describe the process as follows: Initial Training: We first train a QuadricFormer ...
- **p. 16 / C Additional Implementation Details - extractive PDF cue:** To address this, we introduce the prunning-and-splitting module: · We divide all superquadrics in Q into two groups based on the product of their scales: ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To clarify, we take the QuadricFormer with N superquadrics as an example and describe the process as follows: Initial Training: We first ... | p. 16 (C Additional Implementation Details), p. 16 (C Additional Implementation Details) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To address this, we introduce the prunning-and-splitting module: · We divide all superquadrics in Q into two groups based on the product ... | p. 16 (C Additional Implementation Details) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To clarify, we take the QuadricFormer with N superquadrics as an example and describe the process as follows: Initial Training: We first ... | p. 16 (C Additional Implementation Details) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Extensive, experiments, nuScenes, KITTI-360, dataset, demonstrate, QuadricFormer, achieves, state-of-the-art, performance, superior, efficiency, imposes, strong | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Extensive, experiments, nuScenes, KITTI-360, dataset, demonstrate, QuadricFormer, achieves, state-of-the-art, performance | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | efficient, expressive, object-centric, representation, superquadrics, scene, primitives, Building, introduce, QuadricFormer | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive PDF cue:** Extensive experiments on the nuScenes and KITTI-360 dataset demonstrate that our QuadricFormer achieves state-of-the-art performance with superior efficiency.
- **p. 2 / 1 Introduction - extractive PDF cue:** This imposes a strong ellipsoidal shape prior to Gaussians and severely constrains their capacity to model diverse geometries.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Each sequence spans a duration of 20 seconds with RGB images captured by 6 surrounding cameras, and the key frames are annotated ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The official split contains 7 sequences for training, 1 for validation, and 1 for testing, corresponding to 8487, 1812, and 2566 key ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | In terms of efficiency, QuadricFormer significantly reduces both latency and memory usage. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Each sequence spans a duration of 20 seconds with RGB images captured by 6 surrounding cameras, and the key frames are annotated ... | hardware, batch and throughput |

## Training vs Inference

- **p. 16 / C Additional Implementation Details - extractive PDF cue:** To clarify, we take the QuadricFormer with N superquadrics as an example and describe the process as follows: Initial Training: We first train a QuadricFormer ...
- **p. 8 / 4 Experiments - extractive PDF cue:** The latency and memory are tested on an NVIDIA 4090 GPU with batch size one during inference, in accordance with Gaussian-based methods [18, 15].
- **p. 8 / 4 Experiments - extractive PDF cue:** For optimization, we train our model using AdamW with weight decay of 0.01, and maximum learning rate of 4 × 10-4, which decays with a ...
- **p. 7 / 4 Experiments - extractive PDF cue:** We employ ResNet101-DCN [13] with FCOS3D checkpoint [42] for nuScenes [3], and ResNet50 [13] pretrained on ImageNet [11] 7
- **p. 16 / C Additional Implementation Details - extractive PDF cue:** At this stage, we load the pretrained model parameters and continue training for 10 more epochs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** clarify, take, QuadricFormer, superquadrics, example, describe, process, follows, Initial, Training, first, train, quadric-encoder, blocks, without, prunning-and-splitting, module, address, introduce, divide.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The dataset is officially split into 700 sequences for training, 150 for validation, and 150 for testing. | p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Semantic / temporal fusion | Compared to other methods, our approach achieves state-of-the-art performance. | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Robot query / planning handoff | The results demonstrate that increasing the crop & split number consistently improves performance. | p. 8 (4 Experiments), p. 7 (4 Experiments) |

## Failure and Ablation Link

- **p. 8 / 4 Experiments - extractive PDF cue:** 4.4 Ablation Study Effect of the ϵ Range.
- **p. 8 / 4 Experiments - extractive PDF cue:** We conduct ablation studies on the effect of the pruningsplitting module, as shown in Table 5.
- **p. 9 / 4 Experiments - extractive PDF cue:** Range of ϵ mIoU IoU (0.01, 2) 20.39 31.13 (0.01, 5) 20.25 30.63 (0.1, 2) 20.51 31.25 (0.1, 5) 19.86 30.65 Table 5: Effect of ...
- **p. 16 / C Additional Implementation Details - extractive PDF cue:** To clarify, we take the QuadricFormer with N superquadrics as an example and describe the process as follows: Initial Training: We first train a QuadricFormer ...
- **p. 7 / 4 Experiments - extractive PDF cue:** We employ ResNet101-DCN [13] with FCOS3D checkpoint [42] for nuScenes [3], and ResNet50 [13] pretrained on ImageNet [11] 7
- **p. 16 / C Additional Implementation Details - extractive PDF cue:** At this stage, we load the pretrained model parameters and continue training for 10 more epochs.
- **p. 9 / 5 Conclusion - extractive PDF cue:** With random initialization, QuadricFormer cannot fully learn accurate superquadric positions, leaving some superquadrics in empty regions and reducing representation efficiency.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 16 (C Additional Implementation Details), p. 16 (C Additional Implementation Details), objective 본문 anchor 없음, temporal p. 6 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments), p. 2 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
