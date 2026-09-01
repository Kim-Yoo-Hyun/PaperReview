# Method - Depth Anything V2

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2406.09414; PDF retrieval source: https://arxiv.org/pdf/2406.09414. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 9 (Method), p. 9 (Method), p. 8 (Method), p. 8 (Method), p. 10 (Method), p. 14 (B.7 Benefit of gradient matching loss to fine-grained predictions)): First, same as V1 [89], we follow the ZoeDepth [6] pipeline, but replace its MiDaS [7] encoder with our pre-trained encoder.

## Method Body Digest

- **p. 9 / Method - extractive PDF cue:** First, same as V1 [89], we follow the ZoeDepth [6] pipeline, but replace its MiDaS [7] encoder with our pre-trained encoder.
- **p. 9 / Method - extractive PDF cue:** Different from Depth Anything V1 [89], we further attempt to remove the synthetic images during training student models.
- **p. 8 / Method - extractive PDF cue:** Even our most lightweight model is superior to all other community models.
- **p. 8 / Method - extractive PDF cue:** Similar results (i.e., better model but worse score) are also observed in [7, 28].
- **p. 10 / Method - extractive PDF cue:** We can observe in Table 6 that the model trained with pseudo labels is significantly better than the manual-label counterpart.
- **p. 14 / B.7 Benefit of gradient matching loss to fine-grained predictions - extractive PDF cue:** Unfortunately, we find this loss term fails to bring evident improvement when the model is trained on labeled real datasets.
- **p. 14 / B.7 Benefit of gradient matching loss to fine-grained predictions - extractive PDF cue:** To check this, we further apply and ablate this loss term on synthetic training datasets, whose labels are complete and highly precise.
- **p. 14 / B.7 Benefit of gradient matching loss to fine-grained predictions - extractive PDF cue:** MiDaS [56] proposes a gradient matching loss Lgm to enhance the depth sharpness.

## Design Rationale

- **p. 6 / 1 Introduction - extractive PDF cue:** It consists of three steps: • train a reliable teacher model based on DINOv2-G purely on high-quality synthetic images. • produce precise pseudo depth on ...
- **p. 7 / 1 Introduction - extractive PDF cue:** To address this, we introduce a second pipeline, where we carefully analyze images and manually identify challenging pairs.
- **p. 4 / 1 Introduction - extractive PDF cue:** In the right side of Figure 4c, we show the fine-grained prediction of a MDE model trained on synthetic images.

## Source Evidence Cues

- **p. 9 / Method - extractive PDF cue:** First, same as V1 [89], we follow the ZoeDepth [6] pipeline, but replace its MiDaS [7] encoder with our pre-trained encoder.
- **p. 9 / Method - extractive PDF cue:** Different from Depth Anything V1 [89], we further attempt to remove the synthetic images during training student models.
- **p. 8 / Method - extractive PDF cue:** Even our most lightweight model is superior to all other community models.
- **p. 8 / Method - extractive PDF cue:** Similar results (i.e., better model but worse score) are also observed in [7, 28].
- **p. 10 / Method - extractive PDF cue:** We can observe in Table 6 that the model trained with pseudo labels is significantly better than the manual-label counterpart.
- **p. 14 / B.7 Benefit of gradient matching loss to fine-grained predictions - extractive PDF cue:** Unfortunately, we find this loss term fails to bring evident improvement when the model is trained on labeled real datasets.
- **p. 14 / B.7 Benefit of gradient matching loss to fine-grained predictions - extractive PDF cue:** To check this, we further apply and ablate this loss term on synthetic training datasets, whose labels are complete and highly precise.
- **Detected method headings:** Method (p. 8); Method (p. 9)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | First, same as V1 [89], we follow the ZoeDepth [6] pipeline, but replace its MiDaS [7] encoder with our pre-trained encoder. | p. 9 (Method), p. 9 (Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Different from Depth Anything V1 [89], we further attempt to remove the synthetic images during training student models. | p. 9 (Method), p. 8 (Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Even our most lightweight model is superior to all other community models. | p. 8 (Method), p. 8 (Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 14 / B.7 Benefit of gradient matching loss to fine-grained predictions - extractive PDF cue:** MiDaS [56] proposes a gradient matching loss Lgm to enhance the depth sharpness.
- **p. 14 / B.7 Benefit of gradient matching loss to fine-grained predictions - extractive PDF cue:** Image Loss weight 0.5 Loss weight 2.0 Loss weight 4.0 Figure 10: Effect of the gradient matching loss Lgm in terms of fine-grained details.
- **p. 8 / Method - extractive PDF cue:** Despite the advantages, we do not expect DA-2K to replace current benchmarks.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 14 (B.7 Benefit of gradient matching loss to fine-grained predictions), p. 14 (B.7 Benefit of gradient matching loss to fine-grained predictions).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | observation, indeed, similar, SAM, only, releases, pseudo-labeled, masks, Precise, depth, information, favorable, classical, applications | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | observation, indeed, similar, SAM, only, releases, pseudo-labeled, masks, Precise, depth | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | consists, three, steps, train, reliable, teacher, model, DINOv2-G, purely, high-quality | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | MiDaS, proposes, gradient, matching, loss, Lgm, enhance, depth, sharpness, Image | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 9 / Method - extractive PDF cue:** This observation is indeed similar to SAM [33] that only releases its pseudo-labeled masks.
- **p. 2 / 1 Introduction - extractive PDF cue:** Precise depth information is not only favorable in classical applications, such as 3D reconstruction [47, 32, 93], navigation [82], and autonomous driving [80], but is ...
- **p. 8 / Method - extractive PDF cue:** Method Community Models Depth Anything V2 (Ours) Marigold [31] Geowizard [20] DepthFM [25] Depth Anything V1 [89] ViT-S ViT-B ViT-L ViT-G Accuracy (%) 86.8 88.1 ...
- **p. 9 / Method - extractive PDF cue:** Different from Depth Anything V1 [89], we further attempt to remove the synthetic images during training student models.
- **p. 4 / 1 Introduction - extractive PDF cue:** In contrast, some real datasets constructed from web stereo images (e.g., HRWSI [83]) or monocular videos (e.g., MegaDepth [37]), can cover extensive real-world scenes.
- **p. 5 / 1 Introduction - extractive PDF cue:** Unfortunately, as shown in Section B.9, the coarse depth map of real images is destructive to fine-grained prediction.
- **p. 8 / Method - extractive PDF cue:** Finally, we annotate 1K images with 2K pixel pairs in total.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Actually, the smallest model in Depth Anything V1 is used most widely due to its real-time speed. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | 5 Depth Anything V2 5.1 Overall Framework According to all the above analysis, our final pipeline to train Depth Anything V2 is ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / Method - extractive PDF cue:** First, same as V1 [89], we follow the ZoeDepth [6] pipeline, but replace its MiDaS [7] encoder with our pre-trained encoder.
- **p. 9 / Method - extractive PDF cue:** Different from Depth Anything V1 [89], we further attempt to remove the synthetic images during training student models.
- **p. 10 / Method - extractive PDF cue:** We can observe in Table 6 that the model trained with pseudo labels is significantly better than the manual-label counterpart.
- **p. 14 / B.7 Benefit of gradient matching loss to fine-grained predictions - extractive PDF cue:** Unfortunately, we find this loss term fails to bring evident improvement when the model is trained on labeled real datasets.
- **p. 14 / B.7 Benefit of gradient matching loss to fine-grained predictions - extractive PDF cue:** To check this, we further apply and ablate this loss term on synthetic training datasets, whose labels are complete and highly precise.
- **p. 11 / B.1 Fine-tuned to semantic segmentation - extractive PDF cue:** Similar to the practice in metric MDE, we further fine-tune our pre-trained encoder to downstream semantic segmentation task to especially examine its semantic awareness.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** First, same, follow, ZoeDepth, pipeline, replace, MiDaS, encoder, pre-trained, Different, Depth, Anything, further, attempt, remove, synthetic, images, during, training, student.
- **Relevant PDF headings:** Method (p. 8); Method (p. 9).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | As shown in Table 3, on our proposed benchmark with diverse scenes, even our smallest model is significantly better than other heavy ... | p. 8 (7 Experiment), p. 8 (7 Experiment) |
| Semantic / temporal fusion | Figure 1: Depth Anything V2 significantly outperforms V1 [89] in robustness and fine-grained details. Compared with SD-based models [31, 25], it enjoys ... | p. 1 (Figure/Table caption), p. 12 (Dataset) |
| Robot query / planning handoff | We achieve the results without Mapillary [1] or COCO [40] pre-training. our models of various scales consistently achieve the best performance, outperforming ... | p. 12 (Dataset), p. 1 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 8 / 7 Experiment - extractive PDF cue:** Since our model predicts affine-invariant inverse depth, for fairness, we compare with Depth Anything V1 [89] and MiDaS V3.1 [7] on five unseen test datasets.
- **p. 16 / C.2 Comparison with the DIW dataset - extractive PDF cue:** In comparison, our DA-2K is precise, because we exclude many hard-to-decide or controversial pairs. • (better organized) DIW randomly downloads images from Flickr, without carefully ...
- **p. 14 / B.7 Benefit of gradient matching loss to fine-grained predictions - extractive PDF cue:** Image Loss weight 0.5 Loss weight 2.0 Loss weight 4.0 Figure 10: Effect of the gradient matching loss Lgm in terms of fine-grained details.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 7: Depth Anything V2. We first train the most capable teacher on precise synthetic images. Then, to mitigate the distribution shift and limited diversity ...
- **p. 12 / Dataset - extractive PDF cue:** We achieve the results without Mapillary [1] or COCO [40] pre-training. our models of various scales consistently achieve the best performance, outperforming other methods remarkably.
- **p. 14 / B.6 Comparison among various pre-trained encoders - extractive PDF cue:** The success of DINOv2 further reflects the promising future of the data-driven roadmap, since it carefully collects 142M pre-training data without designing fancy algorithms or ...
- **p. 15 / B.9 Harm of real labeled images to fine-grained predictions - extractive PDF cue:** According to the ablation study in Depth Anything V1 [89], HRWSI [83] is the best-performed real training dataset.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 9 (Method), p. 9 (Method), p. 8 (Method), p. 8 (Method), p. 10 (Method), p. 14 (B.7 Benefit of gradient matching loss to fine-grained predictions), objective p. 14 (B.7 Benefit of gradient matching loss to fine-grained predictions), p. 14 (B.7 Benefit of gradient matching loss to fine-grained predictions), p. 8 (Method), temporal p. 5 (1 Introduction), p. 6 (1 Introduction), p. 6 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
