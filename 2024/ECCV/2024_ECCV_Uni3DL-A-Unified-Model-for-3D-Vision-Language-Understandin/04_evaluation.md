# Evaluation - Uni3DL: A Unified Model for 3D Vision-Language Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3330_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03330.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (4.1 Dataset), p. 11 (Figure/Table caption), p. 10 (4.1 Dataset), p. 12 (Figure/Table caption), p. 9 (4.1 Dataset), p. 12 (Figure/Table caption)): Our method achieves significantly better performance than TGNN method as indicated by instance-average IoU, and accuracy at the IoU thresholds of 0.25 and 0.5.

## Evaluation Body Digest

- **p. 9 / 4.1 Dataset - extractive body cue:** Following the official benchmark, we use 1,201 scenes for training, 312 for validation.
- **p. 9 / 4.1 Dataset - extractive body cue:** ScanRefer [7] dataset contains 51,583 referring descriptions of 11,046 objects from 800 ScanNet scenes.
- **p. 10 / 4.1 Dataset - extractive body cue:** S3DIS dataset contains 6 large-scale areas with 271 scenes, and 13 semantic categories are annotated.
- **p. 10 / 4.1 Dataset - extractive body cue:** Following previous works, we use 68 scenes in Area 5 for validation and the others for model training.
- **p. 10 / 4.1 Dataset - extractive body cue:** Our method achieves significantly better performance than TGNN method as indicated by instance-average IoU, and accuracy at the IoU thresholds of 0.25 and 0.5.
- **p. 10 / 4.1 Dataset - extractive body cue:** During inference, the top 200 (for S3DIS) and top 500 (for ScanNet (v2)) instances with the highest classification scores are retained for the instance segmentation ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 3: Performance of our Uni3DL on different segmentation and VL tasks. Uni3DL achieves the best performance on 14 out of 17 metrics. ‘SN' denotes ...
- **p. 9 / 4.1 Dataset - extractive body cue:** 3 To ensure a fair comparison with PointLLM, we filter out 200 objects used for benchmark evaluation from our training set and report the performance ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 9); 4.1 Dataset (p. 9).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.1 Dataset | SYSTEM / EVALUATION SCOPE UNRESOLVED | Our method achieves significantly better performance than TGNN method as indicated by instance-average IoU, and accuracy at the IoU thresholds of 0.25 and 0.5. | p. 10 (4.1 Dataset) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 3: Performance of our Uni3DL on different segmentation and VL tasks. Uni3DL achieves the best performance on 14 out of 17 metrics. ‘SN' ... | p. 11 (Figure/Table caption) |
| 4.1 Dataset | SYSTEM / EVALUATION SCOPE UNRESOLVED | From the table, our Uni3DL method achieves better or comparable performance on general segmentation and detection tasks on S3DIS and ScanNet (v2)datasets. | p. 10 (4.1 Dataset) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Fig. 5: 3D captioning results on Cap3D Objaverse dataset. 4.7 Zero-Shot 3D Object Classification We evaluate the zero-shot 3D classification performance on the ModelNet10/40 ... | p. 12 (Figure/Table caption) |
| 4.1 Dataset | SYSTEM / EVALUATION SCOPE UNRESOLVED | 3 To ensure a fair comparison with PointLLM, we filter out 200 objects used for benchmark evaluation from our training set and report the ... | p. 9 (4.1 Dataset) |

## Dataset / Benchmark Role

- **p. 9 / 4.1 Dataset - extractive body cue:** Following the official benchmark, we use 1,201 scenes for training, 312 for validation.
- **p. 9 / 4.1 Dataset - extractive body cue:** ScanRefer [7] dataset contains 51,583 referring descriptions of 11,046 objects from 800 ScanNet scenes.
- **p. 10 / 4.1 Dataset - extractive body cue:** S3DIS dataset contains 6 large-scale areas with 271 scenes, and 13 semantic categories are annotated.
- **p. 10 / 4.1 Dataset - extractive body cue:** Following previous works, we use 68 scenes in Area 5 for validation and the others for model training.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: With a unified architecture, Uni3DL supports diverse 3D vision-language understanding tasks, including semantic segmentation, object detection, instance segmentation, grounded segmentation, captioning, text-3D cross-modal ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: Comparison of various vision-language models in 3D, highlighting their ca- pabilities across diverse tasks. It specifically indicates the utilization of Multi-View (MV) images ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of the Uni3DL Model. The Uni3DL is engineered for multifaceted 3D data tasks, including classification, retrieval, captioning, semantic and instance seg- mentation, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Head compositions of different tasks. Obj-Cls denotes object classification head, Text-Gen denotes text generation head, and Matching denotes text-3D matching. where CE denotes ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 3: Performance of our Uni3DL on different segmentation and VL tasks. Uni3DL achieves the best performance on 14 out of 17 metrics. ‘SN' denotes ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 3: 3D Segmentation results on S3DIS (top) and ScanNet (bottom) datasets. Input GT Ours Refer: a brown wooden nightstand. it's between the end of ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 4: Results of grounded segmentation on the ScanRefer dataset. Grounded masks are shown in green. GT: a small white NASA space
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 5: 3D captioning results on Cap3D Objaverse dataset. 4.7 Zero-Shot 3D Object Classification We evaluate the zero-shot 3D classification performance on the ModelNet10/40 dataset ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Following the official benchmark, we use 1,201 scenes for training, 312 for validation. | embodiment, simulator version and control stack | p. 9 (4.1 Dataset), p. 9 (4.1 Dataset) |
| Task/environment | ScanRefer [7] dataset contains 51,583 referring descriptions of 11,046 objects from 800 ScanNet scenes. | reset, timeout, object/scene variation | p. 9 (4.1 Dataset), p. 10 (4.1 Dataset) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 12 (11 Method), p. 12 (11 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Our method achieves significantly better performance than TGNN method as indicated by instance-average IoU, and accuracy at the IoU thresholds of 0.25 and 0.5. | definition/direction/unit from same section | p. 10 (4.1 Dataset) |
| During inference, the top 200 (for S3DIS) and top 500 (for ScanNet (v2)) instances with the highest classification scores are retained for the instance ... | definition/direction/unit from same section | p. 10 (4.1 Dataset) |
| Table 3: Performance of our Uni3DL on different segmentation and VL tasks. Uni3DL achieves the best performance on 14 out of 17 metrics. ‘SN' ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| 3 To ensure a fair comparison with PointLLM, we filter out 200 objects used for benchmark evaluation from our training set and report the ... | definition/direction/unit from same section | p. 9 (4.1 Dataset) |
| Fig. 5: 3D captioning results on Cap3D Objaverse dataset. 4.7 Zero-Shot 3D Object Classification We evaluate the zero-shot 3D classification performance on the ModelNet10/40 ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Figure 1: With a unified architecture, Uni3DL supports diverse 3D vision-language understanding tasks, including semantic segmentation, object detection, instance segmentation, grounded segmentation, captioning, text-3D ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Table 2: Head compositions of different tasks. Obj-Cls denotes object classification head, Text-Gen denotes text generation head, and Matching denotes text-3D matching. where CE ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 5: 3D captioning results on Cap3D Objaverse dataset. 4.7 Zero-Shot 3D Object Classification We evaluate the zero-shot 3D classification performance on the ModelNet10/40 ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |
| Fig. 6: Instance (Inst.) segmentation results on S3DIS dataset. We show results of the baseline method trained from scratch and our finetuned model. Task ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| 3 To ensure a fair comparison with PointLLM, we filter out 200 objects used for benchmark evaluation from our training set and report the ... | comparison identity and matched condition | p. 9 (4.1 Dataset) |
| It should be noted we report grounded segmentation performance rather than grounded localization to ensure a fair comparison with TGNN. | comparison identity and matched condition | p. 10 (4.1 Dataset) |
| Table 4: Ablation of pertaining. Effect of different pertaining tasks. We further investigate the effect of each pertaining task, including instance/grounded segmentation, 3D captioning, ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| Table 1: Comparison of various vision-language models in 3D, highlighting their ca- pabilities across diverse tasks. It specifically indicates the utilization of Multi-View (MV) ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 4: Ablation of pertaining. Effect of different pertaining tasks. We further investigate the effect of each pertaining task, including instance/grounded segmentation, 3D captioning, ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| Table 5: Ablation of pertaining tasks and scene-object task balance. Ours + alt. means our model with alternative training. Scene-object task balance. During the ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Details about the pretraining and task-specific fine-tuning setups can be found in the supplementary material. | component/input/data sensitivity | p. 10 (4.1 Dataset) |
| Table 3: Performance of our Uni3DL on different segmentation and VL tasks. Uni3DL achieves the best performance on 14 out of 17 metrics. ‘SN' ... | component/input/data sensitivity | p. 11 (Figure/Table caption) |
| During pretraining, we employ datasets including ScanNet (v2) instance segmentation, ScanRefer, and Cap3D Objaverse. | component/input/data sensitivity | p. 10 (4.1 Dataset) |
| Table 1: Comparison of various vision-language models in 3D, highlighting their ca- pabilities across diverse tasks. It specifically indicates the utilization of Multi-View (MV) ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as: - We present Uni3DL, a unified model tailored for 3D vision and language comprehension. | Our method achieves significantly better performance than TGNN method as indicated by instance-average IoU, and accuracy at the IoU thresholds of 0.25 and 0.5. | PDF body cue; verify exact table/figure and matched conditions | p. 10 (4.1 Dataset), p. 11 (Figure/Table caption), p. 10 (4.1 Dataset), p. 12 (Figure/Table caption), p. 9 (4.1 Dataset), p. 12 (Figure/Table caption) |
| Primary metric/result | Table 3: Performance of our Uni3DL on different segmentation and VL tasks. Uni3DL achieves the best performance on 14 out of 17 metrics. ‘SN' ... | numeric claim only at cited anchor | p. 11 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 9 / 4.1 Dataset - extractive body cue:** Following the official benchmark, we use 1,201 scenes for training, 312 for validation.
- **p. 9 / 4.1 Dataset - extractive body cue:** ScanRefer [7] dataset contains 51,583 referring descriptions of 11,046 objects from 800 ScanNet scenes.
- **p. 9 / 4.1 Dataset - extractive body cue:** We use 562 scenes for training and 141 scenes for evaluation.
- **p. 9 / 4.1 Dataset - extractive body cue:** 3 To ensure a fair comparison with PointLLM, we filter out 200 objects used for benchmark evaluation from our training set and report the performance ...
- **p. 10 / 4.1 Dataset - extractive body cue:** S3DIS dataset contains 6 large-scale areas with 271 scenes, and 13 semantic categories are annotated.
- **p. 10 / 4.1 Dataset - extractive body cue:** Following previous works, we use 68 scenes in Area 5 for validation and the others for model training.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 4.2 Implementation Details In this work, we employ 150 latent queries and one additional latent query for scene-level tasks. | p. 10 (4.1 Dataset) |
| The training process spans 50 epochs using the AdamW optimizer [39], taking approximately 20 hours on four NVIDIA A100 GPUs. | p. 10 (4.1 Dataset) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not recovered

- **Evidence anchors reviewed:** datasets p. 9 (4.1 Dataset), p. 9 (4.1 Dataset), p. 10 (4.1 Dataset), p. 10 (4.1 Dataset), metrics p. 10 (4.1 Dataset), p. 10 (4.1 Dataset), p. 11 (Figure/Table caption), p. 9 (4.1 Dataset), p. 12 (Figure/Table caption), p. 1 (Figure/Table caption), baselines p. 12 (Figure/Table caption), p. 13 (Figure/Table caption), p. 9 (4.1 Dataset), p. 10 (4.1 Dataset), p. 13 (Figure/Table caption), p. 4 (Figure/Table caption), results p. 10 (4.1 Dataset), p. 11 (Figure/Table caption), p. 10 (4.1 Dataset), p. 12 (Figure/Table caption), p. 9 (4.1 Dataset), p. 12 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
