# Method - Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2401.10891; PDF retrieval source: https://arxiv.org/pdf/2401.10891. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (Method), p. 5 (Method), p. 6 (4.3. Fine-tuned to Metric Depth Estimation), p. 7 (Method), p. 7 (Method), p. 6 (4.3. Fine-tuned to Metric Depth Estimation)): Thus, it is not beneficial to exhaustively enforce our depth model to produce exactly the same features as the frozen encoder.

## Method Body Digest

- **p. 5 / Method - extractive body cue:** Thus, it is not beneficial to exhaustively enforce our depth model to produce exactly the same features as the frozen encoder.
- **p. 5 / Method - extractive body cue:** The feature alignment loss is formulated as: \ma t h c a l {L } _{f eat} = 1 - \frac {1}{HW}\sum _{i=1}^{HW}\cos (f_i, f'_i), ...
- **p. 6 / 4.3. Fine-tuned to Metric Depth Estimation - extractive body cue:** In this part, we use our ViT-L encoder for fine-tuning.
- **p. 7 / Method - extractive body cue:** We use Mask2Former as our segmentation model. since the labeled images are already sufficient.
- **p. 7 / Method - extractive body cue:** Following ZoeDepth, we use the model trained on NYUv2 for indoor generalization, while use the model trained on KITTI for outdoor evaluation.
- **p. 6 / 4.3. Fine-tuned to Metric Depth Estimation - extractive body cue:** We initialize the encoder of downstream MDE models with our pre-trained encoder parameters and leave the decoder randomly initialized.
- **p. 8 / Method - extractive body cue:** Since our finally produced encoder (from large-scale MDE training) is finetuned from DINOv2 [43], we compare our encoder with the original DINOv2 encoder in Table ...
- **p. 5 / Method - extractive body cue:** Best, second best results. depth model with an auxiliary feature alignment loss.

## Design Rationale

- **p. 5 / Method - extractive body cue:** This allows our method to enjoy both the semantic-aware representation from DINOv2 and the part-level discriminative representation from depth supervision.
- **p. 2 / 1. Introduction - extractive body cue:** To address the dilemma, we propose to challenge the student model with a more difficult optimization target when learning the pseudo labels.
- **p. 2 / 1. Introduction - extractive body cue:** Therefore, considering the excellent performance of DINOv2 in semantic-related tasks, we propose to maintain the rich semantic priors from it with a simple feature alignment ...

## Source Evidence Cues

- **p. 5 / Method - extractive body cue:** Thus, it is not beneficial to exhaustively enforce our depth model to produce exactly the same features as the frozen encoder.
- **p. 5 / Method - extractive body cue:** The feature alignment loss is formulated as: \ma t h c a l {L } _{f eat} = 1 - \frac {1}{HW}\sum _{i=1}^{HW}\cos (f_i, f'_i), ...
- **p. 6 / 4.3. Fine-tuned to Metric Depth Estimation - extractive body cue:** In this part, we use our ViT-L encoder for fine-tuning.
- **p. 7 / Method - extractive body cue:** We use Mask2Former as our segmentation model. since the labeled images are already sufficient.
- **p. 7 / Method - extractive body cue:** Following ZoeDepth, we use the model trained on NYUv2 for indoor generalization, while use the model trained on KITTI for outdoor evaluation.
- **p. 6 / 4.3. Fine-tuned to Metric Depth Estimation - extractive body cue:** We initialize the encoder of downstream MDE models with our pre-trained encoder parameters and leave the decoder randomly initialized.
- **p. 8 / Method - extractive body cue:** Since our finally produced encoder (from large-scale MDE training) is finetuned from DINOv2 [43], we compare our encoder with the original DINOv2 encoder in Table ...
- **Detected method headings:** Method (p. 5); Method (p. 6); Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Thus, it is not beneficial to exhaustively enforce our depth model to produce exactly the same features as the frozen encoder. | p. 5 (Method), p. 5 (Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The feature alignment loss is formulated as: \ma t h c a l {L } _{f eat} = 1 - \frac {1}{HW}\sum ... | p. 5 (Method), p. 6 (4.3. Fine-tuned to Metric Depth Estimation) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | In this part, we use our ViT-L encoder for fine-tuning. | p. 6 (4.3. Fine-tuned to Metric Depth Estimation), p. 7 (Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / Method - extractive body cue:** Best, second best results. depth model with an auxiliary feature alignment loss.
- **p. 5 / Method - extractive body cue:** Finally, our overall loss is an average combination of the three losses Ll, Lu, and Lfeat.
- **p. 6 / 4.4. Fine-tuned to Semantic Segmentation - extractive body cue:** In our method, we design our MDE model to inherit the rich semantic priors from a pre-trained encoder via a simple feature alignment constraint.
- **p. 7 / Method - extractive body cue:** Effectiveness of 1) challenging the student model when learning unlabeled images, and 2) semantic constraint.
- **p. 7 / Method - extractive body cue:** Moreover, with our used semantic constraint Lfeat, the power of unlabeled images can be further amplified for the depth estimation task.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (Method), p. 5 (Method), p. 6 (4.4. Fine-tuned to Semantic Segmentation), p. 7 (Method), p. 7 (Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Meantime, ControlNet, synthesize, images, depth, Similar, observations, hold, ADE20K, dataset, Table, goal, build, foundation | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Meantime, ControlNet, synthesize, images, depth, Similar, observations, hold, ADE20K, dataset | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | allows, enjoy, semantic-aware, representation, DINOv2, part-level, discriminative, depth, supervision, address | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Best, second, depth, model, auxiliary, feature, alignment, loss, Finally, overall | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 8 / Method - extractive body cue:** Meantime, we use ControlNet to synthesize new images from the depth map.
- **p. 6 / 4.4. Fine-tuned to Semantic Segmentation - extractive body cue:** Similar observations hold on the ADE20K dataset [89] in Table 8.
- **p. 1 / 1. Introduction - extractive body cue:** In this work, our goal is to build a foundation model for MDE capable of producing high-quality depth information for any images under any circumstances.
- **p. 2 / 1. Introduction - extractive body cue:** labeled images from depth sensors, our used monocular unlabeled images exhibit three advantages: (i) (simple and cheap to acquire) Monocular images exist almost everywhere, thus ...
- **p. 5 / Method - extractive body cue:** Thus, it is not beneficial to exhaustively enforce our depth model to produce exactly the same features as the frozen encoder.
- **p. 6 / Method - extractive body cue:** We highlight best, second best results, as well as most discriminative metrics. ∗: Reproduced by us. benchmarks KITTI and NYUv2, although MiDaS v3.1 uses the ...
- **p. 7 / Method - extractive body cue:** Moreover, with our used semantic constraint Lfeat, the power of unlabeled images can be further amplified for the depth estimation task.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We only apply horizontal flipping as our data augmentation for labeled images. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We do not follow some works [19] to project the online feature f into a new space for alignment, because a randomly ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The batch size is 16 and the model is trained for 5 epochs. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4.3. Fine-tuned to Metric Depth Estimation - extractive body cue:** In this part, we use our ViT-L encoder for fine-tuning.
- **p. 7 / Method - extractive body cue:** Following ZoeDepth, we use the model trained on NYUv2 for indoor generalization, while use the model trained on KITTI for outdoor evaluation.
- **p. 6 / 4.3. Fine-tuned to Metric Depth Estimation - extractive body cue:** We initialize the encoder of downstream MDE models with our pre-trained encoder parameters and leave the decoder randomly initialized.
- **p. 8 / Method - extractive body cue:** Since our finally produced encoder (from large-scale MDE training) is finetuned from DINOv2 [43], we compare our encoder with the original DINOv2 encoder in Table ...
- **p. 5 / 4.1. Implementation Details - extractive body cue:** In both stages, the base learning rate of the pre-trained encoder is set as 5e-6, while the randomly initialized decoder uses a 10× larger learning ...
- **p. 9 / 6. More Implementation Details - extractive body cue:** The batch size is 16 and the model is trained for 5 epochs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Thus, beneficial, exhaustively, enforce, depth, model, produce, exactly, same, features, frozen, encoder, feature, alignment, loss, formulated, frac, where, measures, cosine.
- **Relevant PDF headings:** Method (p. 5); Method (p. 6); Method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Moreover, our ViT-S model, whose scale is less than 1/10 of the MiDaS model, even outperforms MiDaS on several unseen datasets, including ... | p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 5 (4.2. Zero-Shot Relative Depth Estimation) |
| Semantic / temporal fusion | Moreover, our ViT-S model, whose scale is less than 1/10 of the MiDaS model, even outperforms MiDaS on several unseen datasets, including ... | p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 8 (Figure/Table caption) |
| Robot query / planning handoff | Moreover, our ViT-S model, whose scale is less than 1/10 of the MiDaS model, even outperforms MiDaS on several unseen datasets, including ... | p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 5 (4.2. Zero-Shot Relative Depth Estimation) |

## Failure and Ablation Link

- **p. 5 / 4.1. Implementation Details - extractive body cue:** All labeled datasets are simply combined together without re-sampling.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Fine-tuning and evaluating on NYUv2 [55] with our pre-trained MDE encoder. We highlight best, second best results, as well as most discriminative metrics. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 4. Fine-tuning and evaluating on KITTI [18] with our pre-trained MDE encoder. ∗: Reproduced by us. coder with metric depth information from NYUv2 [55] ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 9. Ablation studies of: 1) challenging the student with strong perturbations (S) when learning unlabeled images, and 2) semantic constraint (Lfeat). Limited by space, ...
- **p. 9 / 6. More Implementation Details - extractive body cue:** The model is trained for 160K iterations on ADE20K and 80K iterations on Cityscapes both with batch size 16, without any COCO [36] or Mapillary ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 12. Ablation studies on different values of the tolerance margin α for the feature alignment loss Lfeat. Limited by space, we only report the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Our pipeline. Solid line: flow of labeled images, dotted line: unlabeled images. We especially highlight the value of large-scale unlabeled images. The S ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (Method), p. 5 (Method), p. 6 (4.3. Fine-tuned to Metric Depth Estimation), p. 7 (Method), p. 7 (Method), p. 6 (4.3. Fine-tuned to Metric Depth Estimation), objective p. 5 (Method), p. 5 (Method), p. 6 (4.4. Fine-tuned to Semantic Segmentation), p. 7 (Method), p. 7 (Method), temporal p. 5 (4.1. Implementation Details), p. 5 (Method), p. 6 (4.3. Fine-tuned to Metric Depth Estimation), p. 2 (2. Related Work), p. 2 (1. Introduction), p. 4 (3.2. Unleashing the Power of Unlabeled Images).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
