# Evaluation - Point Transformer

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2012.09164; PDF retrieval source: https://arxiv.org/pdf/2012.09164. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.1. Semantic Segmentation), p. 5 (4.1. Semantic Segmentation), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption)): Point Transformer also substantially outperforms all prior models under 6-fold cross-validation.

## Evaluation Body Digest

- **p. 5 / 4.1. Semantic Segmentation - extractive PDF cue:** The S3DIS [1] dataset for semantic scene parsing consists of 271 rooms in six areas from three different buildings.
- **p. 5 / 4. Experiments - extractive PDF cue:** For 3D shape classification, we use the widely adopted ModelNet40 dataset [47].
- **p. 5 / 4.1. Semantic Segmentation - extractive PDF cue:** For evaluation metrics, we use mean classwise intersection over union (mIoU), mean of classwise accuracy (mAcc), and overall pointwise accuracy (OA).
- **p. 5 / 4. Experiments - extractive PDF cue:** The initial learning rate is set to 0.05 and is dropped by 10x at epochs 120 and 160.
- **p. 5 / 4.1. Semantic Segmentation - extractive PDF cue:** Point Transformer also substantially outperforms all prior models under 6-fold cross-validation.
- **p. 5 / 4.1. Semantic Segmentation - extractive PDF cue:** The Point Transformer outperforms all prior models according to all metrics in both evaluation modes.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Shape classification results on the ModelNet40 dataset.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Semantic segmentation results on the S3DIS dataset, evaluated on Area 5.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Semantic Segmentation | SYSTEM / EVALUATION SCOPE UNRESOLVED | Point Transformer also substantially outperforms all prior models under 6-fold cross-validation. | p. 5 (4.1. Semantic Segmentation) |
| 4.1. Semantic Segmentation | SYSTEM / EVALUATION SCOPE UNRESOLVED | The Point Transformer outperforms all prior models according to all metrics in both evaluation modes. | p. 5 (4.1. Semantic Segmentation) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 3. Shape classification results on the ModelNet40 dataset. | p. 6 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 1. Semantic segmentation results on the S3DIS dataset, evaluated on Area 5. | p. 6 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 4. Object part segmentation results on the ShapeNetPart | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Semantic Segmentation - extractive PDF cue:** The S3DIS [1] dataset for semantic scene parsing consists of 271 rooms in six areas from three different buildings.
- **p. 5 / 4. Experiments - extractive PDF cue:** For 3D shape classification, we use the widely adopted ModelNet40 dataset [47].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. The Point Transformer can serve as the backbone for var- ious 3D point cloud understanding tasks such as object classifica- tion, object part ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Point transformer networks for semantic segmentation (top) and classification (bottom). linear linear point transformer input: (x, p) output: (y, p) farthest point sampl. ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Detailed structure design for each module.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Semantic segmentation results on the S3DIS dataset, evaluated on Area 5.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Semantic segmentation results on the S3DIS dataset, eval- uated with 6-fold cross-validation. the ground truth. Point Transformer captures detailed se- mantic structure in ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Shape classification results on the ModelNet40 dataset.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 6. The retrieved shapes are very similar to the query, and when they differ, they differ along aspects that we per- ceive as less ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Object part segmentation results on the ShapeNetPart

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The S3DIS [1] dataset for semantic scene parsing consists of 271 rooms in six areas from three different buildings. | embodiment, simulator version and control stack | p. 5 (4.1. Semantic Segmentation), p. 5 (4. Experiments) |
| Task/environment | For 3D shape classification, we use the widely adopted ModelNet40 dataset [47]. | reset, timeout, object/scene variation | p. 5 (4. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3.5. Network Architecture), p. 6 (Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 6 (4.2. Shape Classification) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For evaluation metrics, we use mean classwise intersection over union (mIoU), mean of classwise accuracy (mAcc), and overall pointwise accuracy (OA). | definition/direction/unit from same section | p. 5 (4.1. Semantic Segmentation) |
| The initial learning rate is set to 0.05 and is dropped by 10x at epochs 120 and 160. | definition/direction/unit from same section | p. 5 (4. Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| On Area 5, the Point Transformer attains mIoU/mAcc/OA of 70.4%/76.5%/90.8%, outperforming all prior work by multiple percentage points in each metric. | comparison identity and matched condition | p. 5 (4.1. Semantic Segmentation) |
| Point Transformer also substantially outperforms all prior models under 6-fold cross-validation. | comparison identity and matched condition | p. 5 (4.1. Semantic Segmentation) |
| Table 6. Ablation study: position encoding. Operator mIoU mAcc OA MLP 61.7 68.6 | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 7. Ablation study: form of self-attention operator. Visualization. Object part segmentation results on a num- ber of models are shown in Figure 7. ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 1. The Point Transformer can serve as the backbone for var- ious 3D point cloud understanding tasks such as object classifica- tion, object ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Table 6. Ablation study: position encoding. Operator mIoU mAcc OA MLP 61.7 68.6 | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Table 7. Ablation study: form of self-attention operator. Visualization. Object part segmentation results on a num- ber of models are shown in Figure 7. ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| It consists of 16,880 models from 16 shape categories, with 14,006 3D models for training and 2,874 for testing. | Point Transformer also substantially outperforms all prior models under 6-fold cross-validation. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.1. Semantic Segmentation), p. 5 (4.1. Semantic Segmentation), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | The Point Transformer outperforms all prior models according to all metrics in both evaluation modes. | numeric claim only at cited anchor | p. 5 (4.1. Semantic Segmentation) |

- Numeric sentences retained from the body:
- **p. 5 / 4. Experiments - extractive PDF cue:** For semantic segmentation on S3DIS, we train for 40K iterations with initial learning rate 0.5, dropped by 10x at steps 24K and 32K.
- **p. 5 / 4. Experiments - extractive PDF cue:** For 3D shape classification on ModelNet40 and 3D object part segmentation on ShapeNetPart, we train for 200 epochs.
- **p. 5 / 4. Experiments - extractive PDF cue:** The initial learning rate is set to 0.05 and is dropped by 10x at epochs 120 and 160.
- **p. 6 / 4.2. Shape Classification - extractive PDF cue:** The ModelNet40 [47] dataset contains 12,311 CAD models with 40 object categories.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The initial learning rate is set to 0.05 and is dropped by 10x at epochs 120 and 160. | p. 5 (4. Experiments) |
| For 3D shape classification on ModelNet40 and 3D object part segmentation on ShapeNetPart, we train for 200 epochs. | p. 5 (4. Experiments) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not recovered

- **PDF anchors reviewed:** datasets p. 5 (4.1. Semantic Segmentation), p. 5 (4. Experiments), metrics p. 5 (4.1. Semantic Segmentation), p. 5 (4. Experiments), baselines p. 5 (4.1. Semantic Segmentation), p. 5 (4.1. Semantic Segmentation), p. 7 (Figure/Table caption), p. 7 (Figure/Table caption), results p. 5 (4.1. Semantic Segmentation), p. 5 (4.1. Semantic Segmentation), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
