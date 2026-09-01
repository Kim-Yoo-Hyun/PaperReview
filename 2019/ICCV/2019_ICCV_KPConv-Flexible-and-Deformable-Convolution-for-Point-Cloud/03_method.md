# Method - KPConv: Flexible and Deformable Convolution for Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1904.08889; PDF retrieval source: https://arxiv.org/pdf/1904.08889. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.4. Kernel Point Network Architectures), p. 5 (3.4. Kernel Point Network Architectures)): Skip links are used to pass the features between intermediate layers of the encoder and the decoder.

## Method Body Digest

- **p. 5 / 3.4. Kernel Point Network Architectures - extractive PDF cue:** Skip links are used to pass the features between intermediate layers of the encoder and the decoder.
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive PDF cue:** The encoder part is the same as in KP-CNN, and the decoder part uses nearest upsampling to get the final pointwise features.
- **p. 1 / 1. Introduction - extractive PDF cue:** Input points with a constant scalar feature (in grey) are convolved through a KPConv that is defined by a set of kernel points (in black) ...
- **p. 2 / 1. Introduction - extractive PDF cue:** The kernel weights are thus carried by points, like the input features, and their area of influence is defined by a correlation function.
- **p. 2 / 1. Introduction - extractive PDF cue:** The robustness of our convolution to varying densities is ensured by the combination of radius neighborhoods and regular subsampling of the input cloud [38].
- **p. 1 / 1. Introduction - extractive PDF cue:** Other approaches use multilayer perceptrons (MLP) to process point clouds directly, following the idea proposed by [49, 26].
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive PDF cue:** After the last layer, the features are aggregated by a global average pooling and processed by the fully connected and softmax layers like in an ...
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive PDF cue:** Combining analogy with successful image networks and empirical studies, we designed two network architectures for the classification and the segmentation tasks.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Furthermore, we propose a deformable version of our convolution [7], which consists of learning local shifts applied to the kernel points (see Figure 3).
- **p. 2 / 1. Introduction - extractive PDF cue:** KPConv also consists of a set of local 3D filters, but overcomes previous point convolution limitations as shown in related work.
- **p. 1 / 1. Introduction - extractive PDF cue:** Various approaches have been proposed to handle such data, and can be grouped into different categories that we will develop in the related work section.

## Source Evidence Cues

- **p. 5 / 3.4. Kernel Point Network Architectures - extractive PDF cue:** Skip links are used to pass the features between intermediate layers of the encoder and the decoder.
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive PDF cue:** The encoder part is the same as in KP-CNN, and the decoder part uses nearest upsampling to get the final pointwise features.
- **Detected method headings:** 3.4. Kernel Point Network Architectures (p. 5); Method (p. 15)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Skip links are used to pass the features between intermediate layers of the encoder and the decoder. | p. 5 (3.4. Kernel Point Network Architectures), p. 5 (3.4. Kernel Point Network Architectures) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The encoder part is the same as in KP-CNN, and the decoder part uses nearest upsampling to get the final pointwise features. | p. 5 (3.4. Kernel Point Network Architectures) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Skip links are used to pass the features between intermediate layers of the encoder and the decoder. | p. 5 (3.4. Kernel Point Network Architectures) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Input, points, constant, scalar, feature, grey, convolved, through, KPConv, defined, kernel, black, filter, weights | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Input, points, constant, scalar, feature, grey, convolved, through, KPConv, defined | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Furthermore, deformable, version, convolution, consists, learning, local, shifts, applied, kernel | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive PDF cue:** Input points with a constant scalar feature (in grey) are convolved through a KPConv that is defined by a set of kernel points (in black) ...
- **p. 2 / 1. Introduction - extractive PDF cue:** The kernel weights are thus carried by points, like the input features, and their area of influence is defined by a correlation function.
- **p. 2 / 1. Introduction - extractive PDF cue:** The robustness of our convolution to varying densities is ensured by the combination of radius neighborhoods and regular subsampling of the input cloud [38].
- **p. 1 / 1. Introduction - extractive PDF cue:** Other approaches use multilayer perceptrons (MLP) to process point clouds directly, following the idea proposed by [49, 26].
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive PDF cue:** After the last layer, the features are aggregated by a global average pooling and processed by the fully connected and softmax layers like in an ...
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive PDF cue:** Combining analogy with successful image networks and empirical studies, we designed two network architectures for the classification and the segmentation tasks.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | On average, a ModelNet40 object point cloud comprises 6,800 points in our framework. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Semantic3D is an online benchmark comprising several fixed lidar scans of different outdoor scenes. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | On average, a ModelNet40 object point cloud comprises 6,800 points in our framework. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Skip, links, pass, features, between, intermediate, layers, encoder, decoder, part, same, KP-CNN, uses, nearest, upsampling, final, pointwise, Input, points, constant.
- **Relevant PDF headings:** 3.4. Kernel Point Network Architectures (p. 5); Method (p. 15).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The 3D scenes in these datasets are too big to be segmented as a whole. | p. 6 (4.2. 3D Scene Segmentation), p. 6 (4.2. 3D Scene Segmentation) |
| Semantic / temporal fusion | As shown on Table 1, our networks outperform other state-of-the-art methods using only points (we do not take into account methods using ... | p. 5 (4.1. 3D Shape Classification and Segmentation), p. 6 (4.1. 3D Shape Classification and Segmentation) |
| Robot query / planning handoff | Among these 4 datasets, KPConv deformable kernels improved the results on Paris-Lille-3D and S3DIS while the rigid version was better on Scannet ... | p. 6 (4.2. 3D Scene Segmentation), p. 8 (4.4. Learned Features and Effective Receptive Field) |

## Failure and Ablation Link

- **p. 6 / 4.1. 3D Shape Classification and Segmentation - extractive PDF cue:** For generalizability to real data, we only consider scores obtained without shape normals on ModelNet40 dataset.
- **p. 6 / 4.2. 3D Scene Segmentation - extractive PDF cue:** SubSparseCNN score on Scannet was not reported in their original paper [9], so it is hard to compare without knowing their experimental setup.
- **p. 7 / 4.4. Learned Features and Effective Receptive Field - extractive PDF cue:** Ablation study on Scannet validation set.
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** We conduct an ablation study to support our claim that deformable KPConv has a stronger descriptive power than rigid KPConv.
- **p. 13 / Figure/Table caption - extractive PDF cue:** Figure 11. Illustration of the deformations learned by a KPConv network with or without regularization.
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** We use Scannet dataset (same parameters as before) and use the official validation set, because the test set cannot be used for such evaluations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.4. Kernel Point Network Architectures), p. 5 (3.4. Kernel Point Network Architectures), objective 본문 anchor 없음, temporal p. 5 (4.1. 3D Shape Classification and Segmentation), p. 6 (4.2. 3D Scene Segmentation), p. 6 (4.2. 3D Scene Segmentation), p. 7 (4.2. 3D Scene Segmentation), p. 8 (4.4. Learned Features and Effective Receptive Field).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
