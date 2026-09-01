# Method - PointCNN: Convolution On X-Transformed Points

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1801.07791; PDF retrieval source: https://arxiv.org/pdf/1801.07791. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction)): To address these problems, we propose to learn an X-transformation from the input points to simultaneously promote two causes: the first is the weighting of the input features associated with ...

## Method Body Digest

- **p. 1 / Abstract - extractive PDF cue:** To address these problems, we propose to learn an X-transformation from the input points to simultaneously promote two causes: the first is the weighting of ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Nevertheless, PointCNN built with X-Conv is still significantly better than a direct application of typical convolutions on point clouds, and on par or better than ...
- **p. 1 / 1 Introduction - extractive PDF cue:** In (i), each grid cell is associated with a feature.
- **p. 2 / 1 Introduction - extractive PDF cue:** Section 3 contains the details of X-Conv, as well as PointCNN architectures.
- **p. 1 / 1 Introduction - extractive PDF cue:** Work in progress. arXiv:1801.07791v5 [cs.CV] 5 Nov 2018
- **p. 1 / 1 Introduction - extractive PDF cue:** However, for data represented in point cloud form, which is irregular and unordered, the convoralution operator is ill-suited for leveraging spatially-local correlations in the data. ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Suppose the unordered set of the C-dimensional input features is the same F = {fa, fb, fc, fd} ∗Part of the work was done during ...
- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we propose to learn a K × K X-transformation for the coordinates of K input points (p1, p2, ..., pK), with a ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we propose to learn a K × K X-transformation for the coordinates of K input points (p1, p2, ..., pK), with a ...
- **p. 1 / Abstract - extractive PDF cue:** We present a simple and general framework for feature learning from point clouds.
- **p. 1 / Abstract - extractive PDF cue:** To address these problems, we propose to learn an X-transformation from the input points to simultaneously promote two causes: the first is the weighting of ...

## Source Evidence Cues

- **p. 1 / Abstract - extractive PDF cue:** To address these problems, we propose to learn an X-transformation from the input points to simultaneously promote two causes: the first is the weighting of ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Nevertheless, PointCNN built with X-Conv is still significantly better than a direct application of typical convolutions on point clouds, and on par or better than ...
- **p. 1 / 1 Introduction - extractive PDF cue:** In (i), each grid cell is associated with a feature.
- **p. 2 / 1 Introduction - extractive PDF cue:** Section 3 contains the details of X-Conv, as well as PointCNN architectures.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To address these problems, we propose to learn an X-transformation from the input points to simultaneously promote two causes: the first is ... | p. 1 (Abstract), p. 2 (1 Introduction) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Nevertheless, PointCNN built with X-Conv is still significantly better than a direct application of typical convolutions on point clouds, and on par ... | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | In (i), each grid cell is associated with a feature. | p. 1 (1 Introduction), p. 2 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / 1 Introduction - extractive PDF cue:** Work in progress. arXiv:1801.07791v5 [cs.CV] 5 Nov 2018
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Nevertheless, PointCNN, built, X-Conv, still, significantly, better, direct, application, typical, convolutions, point, clouds, state-of-the-art | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Nevertheless, PointCNN, built, X-Conv, still, significantly, better, direct, application, typical | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | learn, X-transformation, coordinates, input, points, multilayer, perceptron, MLP, present, simple | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | progress, arXiv, Nov | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive PDF cue:** Nevertheless, PointCNN built with X-Conv is still significantly better than a direct application of typical convolutions on point clouds, and on par or better than ...
- **p. 1 / 1 Introduction - extractive PDF cue:** However, for data represented in point cloud form, which is irregular and unordered, the convoralution operator is ill-suited for leveraging spatially-local correlations in the data. ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Suppose the unordered set of the C-dimensional input features is the same F = {fa, fb, fc, fd} ∗Part of the work was done during ...
- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we propose to learn a K × K X-transformation for the coordinates of K input points (p1, p2, ..., pK), with a ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Note that a large portion of the 3D models from ModelNet40 are pre-aligned to the common up direction and horizontal facing direction. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | If a random horizontal rotation is not applied on either the training or testing sets, then the relatively consistent horizontal facing direction ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Optimizer, model size, memory usage and timing. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 4 Experiments - extractive PDF cue:** We implemented PointCNN in tensorflow [1], and use ADAM optimizer [21] with an initial learning rate 0.01 for the training of our models.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** address, problems, learn, X-transformation, input, points, simultaneously, promote, causes, first, weighting, features, associated, second, permutation, latent, potentially, canonical, order, Nevertheless.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Material Section 2, and the PointCNN architectures for the tasks on these datasets can be found in Supp. | p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Semantic / temporal fusion | We note that PointCNN outperforms all the compared methods, including SSCN [12], SPGraph [24] and SGPN [49], which are specialized segmentation networks ... | p. 7 (4 Experiments), p. 7 (Figure/Table caption) |
| Robot query / planning handoff | Table 3: Segmentation result comparisons on the S3DIS [2] Area 5 in overall accuracy (OA, %), micro-averaged accuracy (mAcc, %), micro-averaged IoU ... | p. 14 (Figure/Table caption), p. 7 (4 Experiments) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4: Image classification results. 4.2 Ablation Experiments and Visualizations Ablation test of the core X-Conv operator. To verify the effectiveness of the X-transformation, we ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5: T-SNE visualization of features without (a/Fo), before (b/F∗) and after (c/FX ) X- transformation. the decrease in depth caused by the removal of ...
- **p. 8 / 4 Experiments - extractive PDF cue:** PointCNN w/o X w/o X-W w/o X-D Core Layers X-Conv×4 Conv×4 Conv×4 Conv×5 # Parameter 0.6M 0.54M 0.63M 0.61M Accuracy (%) 92.2 90.7 90.8 90.7 ...
- **p. 7 / 4 Experiments - extractive PDF cue:** Together with the lack of "shape" information, PointNet++ fails completely on this task.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), objective p. 1 (1 Introduction), temporal p. 6 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), p. 1 (Abstract), p. 2 (2 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
