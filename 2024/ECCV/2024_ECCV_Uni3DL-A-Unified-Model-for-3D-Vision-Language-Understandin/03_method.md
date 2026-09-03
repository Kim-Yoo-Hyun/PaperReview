# Method - Uni3DL: A Unified Model for 3D Vision-Language Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3330_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03330.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 12 (11 Method), p. 14 (11 Method), p. 11 (11 Method), p. 11 (11 Method), p. 12 (11 Method), p. 13 (11 Method)): Ablation experiments are conducted by training separate models from scratch for various tasks, including ScanNet (v2) semantic segmentation, S3DIS

## Method Body Digest

- **p. 12 / 11 Method - extractive body cue:** Ablation experiments are conducted by training separate models from scratch for various tasks, including ScanNet (v2) semantic segmentation, S3DIS
- **p. 14 / 11 Method - extractive body cue:** Ours + alt. means our model with alternative training.
- **p. 11 / 11 Method - extractive body cue:** 4.5 3D Captioning From Table 3, our Uni3DL model outperforms existing methods in 3D captioning on the Cap3D Objaverse dataset.
- **p. 11 / 11 Method - extractive body cue:** Note that Swin3D† uses extra training data (Structure3D [74]). localization because minor boundary inaccuracies in segmentation masks minimally impact segmentation IOU, but can significantly alter ...
- **p. 12 / 11 Method - extractive body cue:** 4.8 Ablation Study Effect of Pretraining.
- **p. 13 / 11 Method - extractive body cue:** We show results of the baseline method trained from scratch and our finetuned model.
- **p. 13 / 11 Method - extractive body cue:** In Table 5, we keep grounded segmentation while evaluating the significance of remaining pretraining tasks.
- **p. 3 / 1 Introduction - extractive body cue:** Its versatile architecture allows for the processing of both point clouds and text inputs, generating diverse outputs including masks, classes, and texts.

## Design Rationale

- **p. 3 / 1 Introduction - extractive body cue:** Our contributions are summarized as: - We present Uni3DL, a unified model tailored for 3D vision and language comprehension.
- **p. 3 / 1 Introduction - extractive body cue:** Uni3DL starts with a 3D encoder to extract point features and a text encoder to extract text features, followed by a carefully designed query transformer ...
- **p. 11 / 11 Method - extractive body cue:** On the BLEU-1 [44] and ROUGE-L [36] scores, our method beats precious STOA methods by a large margin (more than 20%).

## Source Evidence Cues

- **p. 12 / 11 Method - extractive body cue:** Ablation experiments are conducted by training separate models from scratch for various tasks, including ScanNet (v2) semantic segmentation, S3DIS
- **p. 14 / 11 Method - extractive body cue:** Ours + alt. means our model with alternative training.
- **p. 11 / 11 Method - extractive body cue:** 4.5 3D Captioning From Table 3, our Uni3DL model outperforms existing methods in 3D captioning on the Cap3D Objaverse dataset.
- **p. 11 / 11 Method - extractive body cue:** Note that Swin3D† uses extra training data (Structure3D [74]). localization because minor boundary inaccuracies in segmentation masks minimally impact segmentation IOU, but can significantly alter ...
- **p. 12 / 11 Method - extractive body cue:** 4.8 Ablation Study Effect of Pretraining.
- **p. 13 / 11 Method - extractive body cue:** We show results of the baseline method trained from scratch and our finetuned model.
- **p. 13 / 11 Method - extractive body cue:** In Table 5, we keep grounded segmentation while evaluating the significance of remaining pretraining tasks.
- **Detected method headings:** 11 Method (p. 11)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Ablation experiments are conducted by training separate models from scratch for various tasks, including ScanNet (v2) semantic segmentation, S3DIS | p. 12 (11 Method), p. 14 (11 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Ours + alt. means our model with alternative training. | p. 14 (11 Method), p. 11 (11 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 4.5 3D Captioning From Table 3, our Uni3DL model outperforms existing methods in 3D captioning on the Cap3D Objaverse dataset. | p. 11 (11 Method), p. 11 (11 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | versatile, architecture, allows, processing, point, clouds, text, inputs, generating, diverse, outputs, including, masks, classes | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | versatile, architecture, allows, processing, point, clouds, text, inputs, generating, diverse | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, present, Uni3DL, unified, model, tailored, vision, language, comprehension | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1 Introduction - extractive body cue:** Its versatile architecture allows for the processing of both point clouds and text inputs, generating diverse outputs including masks, classes, and texts.
- **p. 2 / 1 Introduction - extractive body cue:** They achieve this by matching projected multiview images with text inputs.
- **p. 12 / 11 Method - extractive body cue:** Input GT Ours Refer: a brown wooden nightstand. it's between the end of the bed and close to the wall.
- **p. 12 / 11 Method - extractive body cue:** Input GT Ours Refer: this is a green toolbox. the green toolbox is in front of a red toolbox on the floor next to a ...
- **p. 3 / 1 Introduction - extractive body cue:** A task router with multiple highly shared functional heads is designed to selectively produce task-specific outputs for diverse 3D vision-only and vision-language tasks.
- **p. 2 / 1 Introduction - extractive body cue:** Point-LLM [63] and 3D-LLM [23] directly operate on raw point clouds and explore Large Language Models (LLMs) for 3D visual understanding tasks, including 3D object ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Achieving a proper balance between these two types of tasks-each characterized by unique data distributions-is crucial in our multi-task training framework. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We hope our benchmark and Uni3DL model will serve as a solid step to ease future research in unified models in the ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The training process spans 50 epochs using the AdamW optimizer [39], taking approximately 20 hours on four NVIDIA A100 GPUs. | hardware, batch and throughput |

## Training vs Inference

- **p. 12 / 11 Method - extractive body cue:** Ablation experiments are conducted by training separate models from scratch for various tasks, including ScanNet (v2) semantic segmentation, S3DIS
- **p. 14 / 11 Method - extractive body cue:** Ours + alt. means our model with alternative training.
- **p. 11 / 11 Method - extractive body cue:** Note that Swin3D† uses extra training data (Structure3D [74]). localization because minor boundary inaccuracies in segmentation masks minimally impact segmentation IOU, but can significantly alter ...
- **p. 12 / 11 Method - extractive body cue:** 4.8 Ablation Study Effect of Pretraining.
- **p. 13 / 11 Method - extractive body cue:** We show results of the baseline method trained from scratch and our finetuned model.
- **p. 13 / 11 Method - extractive body cue:** In Table 5, we keep grounded segmentation while evaluating the significance of remaining pretraining tasks.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Ablation, experiments, conducted, training, separate, models, scratch, various, tasks, including, ScanNet, semantic, segmentation, S3DIS, Ours, means, model, alternative, Captioning, Table.
- **Relevant PDF headings:** 11 Method (p. 11).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Following the official benchmark, we use 1,201 scenes for training, 312 for validation. | p. 9 (4.1 Dataset), p. 9 (4.1 Dataset) |
| Semantic / temporal fusion | Fig. 5: 3D captioning results on Cap3D Objaverse dataset. 4.7 Zero-Shot 3D Object Classification We evaluate the zero-shot 3D classification performance on ... | p. 12 (Figure/Table caption), p. 13 (Figure/Table caption) |
| Robot query / planning handoff | Our method achieves significantly better performance than TGNN method as indicated by instance-average IoU, and accuracy at the IoU thresholds of 0.25 ... | p. 10 (4.1 Dataset), p. 11 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 13 / Figure/Table caption - extractive body cue:** Table 4: Ablation of pertaining. Effect of different pertaining tasks. We further investigate the effect of each pertaining task, including instance/grounded segmentation, 3D captioning, and ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 5: Ablation of pertaining tasks and scene-object task balance. Ours + alt. means our model with alternative training. Scene-object task balance. During the pretraining ...
- **p. 10 / 4.1 Dataset - extractive body cue:** Details about the pretraining and task-specific fine-tuning setups can be found in the supplementary material.
- **p. 11 / Figure/Table caption - extractive body cue:** Table 3: Performance of our Uni3DL on different segmentation and VL tasks. Uni3DL achieves the best performance on 14 out of 17 metrics. ‘SN' denotes ...
- **p. 10 / 4.1 Dataset - extractive body cue:** During pretraining, we employ datasets including ScanNet (v2) instance segmentation, ScanRefer, and Cap3D Objaverse.
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: Comparison of various vision-language models in 3D, highlighting their ca- pabilities across diverse tasks. It specifically indicates the utilization of Multi-View (MV) images ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 12 (11 Method), p. 14 (11 Method), p. 11 (11 Method), p. 11 (11 Method), p. 12 (11 Method), p. 13 (11 Method), objective 본문 anchor 없음, temporal p. 14 (11 Method), p. 2 (Body text (section not recovered)), p. 3 (2 Related Work), p. 4 (2 Related Work), p. 5 (2 Related Work), p. 6 (2 Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
