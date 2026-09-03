# Evaluation - PointContrast: Unsupervised Pre-training for 3D Point Cloud Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2007.10985; PDF retrieval source: https://arxiv.org/pdf/2007.10985. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 2 (1 Introduction), p. 1 (body section not recovered), p. 2 (1 Introduction), p. 10 (Figure/Table caption), p. 12 (Figure/Table caption), p. 24 (Figure/Table caption)): Our contributions can be summarized as follows: - We evaluate, for the first time, the transferability of learned representation in 3D point clouds to high-level scene understanding. - Our results ...

## Evaluation Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions can be summarized as follows: - We evaluate, for the first time, the transferability of learned representation in 3D point clouds to high-level ...
- **p. 1 / body section not recovered - extractive body cue:** To this end, we select a suite of diverse datasets and tasks to measure the effect of unsupervised pre-training on a large source set of ...
- **p. 1 / body section not recovered - extractive body cue:** Our findings are extremely encouraging: using a unified triplet of architecture, source dataset, and contrastive loss for pre-training, we achieve improvement over recent best results ...
- **p. 2 / 1 Introduction - extractive body cue:** Next, we choose a broad set of target datasets and downstream tasks that includes: semantic segmentation on S3DIS [2], ScanNetV2 [11], ShapeNetPart [77] and Synthia ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 2: ShapeNet classification. Top: classification accuracy with limited labeled training data for finetuning. Bottom: classification accuracy on the least represented classes in the data ...
- **p. 23 / Figure/Table caption - extractive body cue:** Table 10: Synthia4D segmentation test results Per-category IOU performance. optimizer with an initial learning rate 0.8. We use Polynomial LR scheduler with a power factor ...
- **p. 23 / Figure/Table caption - extractive body cue:** Table 11: ScanNet segmentation results on val set Per-category IOU performance. H ScanNet and SUN RGB-D Detection Details For the 3D object detection experiments, we ...
- **p. 22 / Figure/Table caption - extractive body cue:** Table 9: Stanford Area 5 Test (Fold 1). Per-category IOU performance. F Synthia4D Segmentation Experimental Details Here we provide training details for Synthia4D semantic segmentation ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** B Visualization of the ScanNet Point Cloud Pair Dataset (p. 20).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 1 Introduction | SYSTEM / EVALUATION SCOPE UNRESOLVED | Our contributions can be summarized as follows: - We evaluate, for the first time, the transferability of learned representation in 3D point clouds to ... | p. 2 (1 Introduction) |
| 2 Stanford University | SYSTEM / EVALUATION SCOPE UNRESOLVED | Our findings are extremely encouraging: using a unified triplet of architecture, source dataset, and contrastive loss for pre-training, we achieve improvement over recent best ... | p. 1 (body section not recovered) |
| 1 Introduction | SYSTEM / EVALUATION SCOPE UNRESOLVED | Remarkably, our results indicate improved performance across all datasets and tasks (See Table 1 for a summary of the results). | p. 2 (1 Introduction) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 2: ShapeNet classification. Top: classification accuracy with limited labeled training data for finetuning. Bottom: classification accuracy on the least represented classes in the ... | p. 10 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 6: Segmentation results on the 4D Synthia test set. All networks here are SR-UNet with 3D kernels, trained on individual 3D frames without ... | p. 12 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions can be summarized as follows: - We evaluate, for the first time, the transferability of learned representation in 3D point clouds to high-level ...
- **p. 1 / body section not recovered - extractive body cue:** To this end, we select a suite of diverse datasets and tasks to measure the effect of unsupervised pre-training on a large source set of ...
- **p. 1 / body section not recovered - extractive body cue:** Our findings are extremely encouraging: using a unified triplet of architecture, source dataset, and contrastive loss for pre-training, we achieve improvement over recent best results ...
- **p. 2 / 1 Introduction - extractive body cue:** Next, we choose a broad set of target datasets and downstream tasks that includes: semantic segmentation on S3DIS [2], ScanNetV2 [11], ShapeNetPart [77] and Synthia ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 1: Training from scratch vs. fine-tuning with ShapeNet pre-trained weights. understand the limitations of existing practice (pre-training on ShapeNet) in 3D deep learning (Section ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2: PointContrast: Pretext task for 3D pre-training. 𝐱! 𝐱" 𝑇! 𝑇" Sparse Res-U-Net 𝐟! 𝐟"
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1: Summary of downstream fine-tuning tasks. Compared to the baseline learning paradigm of training from scratch, which is dominant in 3D deep learning, our ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 2: ShapeNet classification. Top: classification accuracy with limited labeled training data for finetuning. Bottom: classification accuracy on the least represented classes in the data ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 3: ShapeNet part segmentation. Replacing the backbone architecture with SR-UNet already boosts performance. PointContrast pre-training further adds a sig- nificant gain, and outshines where ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 4: Stanford Area 5 Test (Fold 1) (S3DIS). Replacing the backbone network with SR-UNet improves upon prior art. Using PointContrast adds further significant boost ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 5: SUN RGB-D detection results. PointContrast demonstrates a substan- tial boost compared to training from scratch. We observe a larger improvement in localization as ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 6: Segmentation results on the 4D Synthia test set. All networks here are SR-UNet with 3D kernels, trained on individual 3D frames without temporal ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our contributions can be summarized as follows: - We evaluate, for the first time, the transferability of learned representation in 3D point clouds to ... | embodiment, simulator version and control stack | p. 2 (1 Introduction), p. 1 (body section not recovered) |
| Task/environment | To this end, we select a suite of diverse datasets and tasks to measure the effect of unsupervised pre-training on a large source set ... | reset, timeout, object/scene variation | p. 1 (body section not recovered), p. 1 (body section not recovered) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (body section not recovered), p. 1 (body section not recovered) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2: ShapeNet classification. Top: classification accuracy with limited labeled training data for finetuning. Bottom: classification accuracy on the least represented classes in the ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Table 10: Synthia4D segmentation test results Per-category IOU performance. optimizer with an initial learning rate 0.8. We use Polynomial LR scheduler with a power ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| Table 11: ScanNet segmentation results on val set Per-category IOU performance. H ScanNet and SUN RGB-D Detection Details For the 3D object detection experiments, ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| Table 9: Stanford Area 5 Test (Fold 1). Per-category IOU performance. F Synthia4D Segmentation Experimental Details Here we provide training details for Synthia4D semantic ... | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| ImageNet classification) can help boost performance once fine-tuned on the usually much smaller target set, has been key to the success of many applications. | definition/direction/unit from same section | p. 1 (1 Introduction) |
| Table 1: Summary of downstream fine-tuning tasks. Compared to the baseline learning paradigm of training from scratch, which is dominant in 3D deep learning, ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 5: SUN RGB-D detection results. PointContrast demonstrates a substan- tial boost compared to training from scratch. We observe a larger improvement in localization ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Table 6: Segmentation results on the 4D Synthia test set. All networks here are SR-UNet with 3D kernels, trained on individual 3D frames without ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 1: Summary of downstream fine-tuning tasks. Compared to the baseline learning paradigm of training from scratch, which is dominant in 3D deep learning, ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Table 6: Segmentation results on the 4D Synthia test set. All networks here are SR-UNet with 3D kernels, trained on individual 3D frames without ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |
| Table 8: 3D object detection results on ScanNet validation set. Similarly to in- domain segmentation task, here as well PointContrast boost performance on detection, ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| However, it still falls behind compared to its 2D counterpart as evidently, in all 3D scene understanding tasks, adhoc training from scratch on the ... | comparison identity and matched condition | p. 2 (1 Introduction) |
| Our contributions can be summarized as follows: - We evaluate, for the first time, the transferability of learned representation in 3D point clouds to ... | comparison identity and matched condition | p. 2 (1 Introduction) |
| Table 5: SUN RGB-D detection results. PointContrast demonstrates a substan- tial boost compared to training from scratch. We observe a larger improvement in localization ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 9: Stanford Area 5 Test (Fold 1). Per-category IOU performance. F Synthia4D Segmentation Experimental Details Here we provide training details for Synthia4D semantic ... | component/input/data sensitivity | p. 22 (Figure/Table caption) |
| To this end, we select a suite of diverse datasets and tasks to measure the effect of unsupervised pre-training on a large source set ... | component/input/data sensitivity | p. 1 (body section not recovered) |
| Table 6: Segmentation results on the 4D Synthia test set. All networks here are SR-UNet with 3D kernels, trained on individual 3D frames without ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| ImageNet classification) can help boost performance once fine-tuned on the usually much smaller target set, has been key to the success of many applications. | component/input/data sensitivity | p. 1 (1 Introduction) |
| The purpose of this work is to move the needle by initiating research on unsupervised pre-training with supervised fine-tuning in deep learning for 3D ... | component/input/data sensitivity | p. 2 (1 Introduction) |
| Specifically, we choose ScanNet [11] as our source set on which the pretraining takes place, and utilize a sparse residual U-Net [51, 9] as ... | component/input/data sensitivity | p. 2 (1 Introduction) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions can be summarized as follows: - We evaluate, for the first time, the transferability of learned representation in 3D point clouds to ... | Our contributions can be summarized as follows: - We evaluate, for the first time, the transferability of learned representation in 3D point clouds to ... | PDF body cue; verify exact table/figure and matched conditions | p. 2 (1 Introduction), p. 1 (body section not recovered), p. 2 (1 Introduction), p. 10 (Figure/Table caption), p. 12 (Figure/Table caption), p. 24 (Figure/Table caption) |
| Primary metric/result | Our findings are extremely encouraging: using a unified triplet of architecture, source dataset, and contrastive loss for pre-training, we achieve improvement over recent best ... | numeric claim only at cited anchor | p. 1 (body section not recovered) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, it still falls behind compared to its 2D counterpart as evidently, in all 3D scene understanding tasks, adhoc training from scratch on the ... | p. 2 (1 Introduction) |
| body limitation/failure cue | Fig. 1: Training from scratch vs. fine-tuning with ShapeNet pre-trained weights. understand the limitations of existing practice (pre-training on ShapeNet) in 3D deep learning ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | This suggests that potentially many of the 3D datasets could fall into the "breakdown regime"[24] where network pre-training is essential for good performance. | p. 14 (2 Related work) |
| body limitation/failure cue | Although typically the source dataset for pre-training and the target dataset for fine-tuning are different, because of the specific multi-view contrastive learning pipeline for ... | p. 13 (2 Related work) |
| body limitation/failure cue | This calls for an architectural modification as the SR-UNet architecture does not directly output bounding box coordinates. | p. 11 (2 Related work) |
| body limitation/failure cue | Table 8: 3D object detection results on ScanNet validation set. Similarly to in- domain segmentation task, here as well PointContrast boost performance on detection, ... | p. 13 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| no implementation/reproducibility sentence selected | verify appendix and code/project |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / 1 Introduction - extractive body cue:** However, it still falls behind compared to its 2D counterpart as evidently, in all 3D scene understanding tasks, adhoc training from scratch on the target ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 1: Training from scratch vs. fine-tuning with ShapeNet pre-trained weights. understand the limitations of existing practice (pre-training on ShapeNet) in 3D deep learning (Section ...
- **p. 14 / 2 Related work - extractive body cue:** This suggests that potentially many of the 3D datasets could fall into the "breakdown regime"[24] where network pre-training is essential for good performance.
- **p. 13 / 2 Related work - extractive body cue:** Although typically the source dataset for pre-training and the target dataset for fine-tuning are different, because of the specific multi-view contrastive learning pipeline for pre-training, ...
- **p. 11 / 2 Related work - extractive body cue:** This calls for an architectural modification as the SR-UNet architecture does not directly output bounding box coordinates.
- **p. 13 / Figure/Table caption - extractive body cue:** Table 8: 3D object detection results on ScanNet validation set. Similarly to in- domain segmentation task, here as well PointContrast boost performance on detection, setting ...

- **Evidence anchors reviewed:** datasets p. 2 (1 Introduction), p. 1 (body section not recovered), p. 1 (body section not recovered), p. 2 (1 Introduction), metrics p. 10 (Figure/Table caption), p. 23 (Figure/Table caption), p. 23 (Figure/Table caption), p. 22 (Figure/Table caption), p. 1 (1 Introduction), p. 5 (Figure/Table caption), baselines p. 5 (Figure/Table caption), p. 12 (Figure/Table caption), p. 13 (Figure/Table caption), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 12 (Figure/Table caption), results p. 2 (1 Introduction), p. 1 (body section not recovered), p. 2 (1 Introduction), p. 10 (Figure/Table caption), p. 12 (Figure/Table caption), p. 24 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
