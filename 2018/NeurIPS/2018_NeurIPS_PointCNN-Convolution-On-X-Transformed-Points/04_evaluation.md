# Evaluation - PointCNN: Convolution On X-Transformed Points

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1801.07791; PDF retrieval source: https://arxiv.org/pdf/1801.07791. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 14 (Figure/Table caption), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (Figure/Table caption)): Table 3: Segmentation result comparisons on the S3DIS [2] Area 5 in overall accuracy (OA, %), micro-averaged accuracy (mAcc, %), micro-averaged IoU (mIoU, %) and per-class IoU (%). 4 Detailed ...

## Evaluation Body Digest

- **p. 6 / 4 Experiments - extractive PDF cue:** Material Section 2, and the PointCNN architectures for the tasks on these datasets can be found in Supp.
- **p. 6 / 4 Experiments - extractive PDF cue:** We conducted an extensive evaluation of PointCNN for shape classification on six datasets (ModelNet40 [52], ScanNet [9], TU-Berlin [11], Quick Draw [15], MNIST, CIFAR10), and ...
- **p. 7 / 4 Experiments - extractive PDF cue:** We evaluate PointCNN on the segmentation of ShapeNet Parts, S3DIS, and ScanNet datasets, and summarize the results in Table 2.
- **p. 7 / 4 Experiments - extractive PDF cue:** It is interesting to study whether architectural elements from Sketch-a-Net can be adopted and integrated into PointCNN to improve its performance on the sketch datasets.
- **p. 8 / 4 Experiments - extractive PDF cue:** To verify this, we show T-SNE visualization of Fo, F∗and FX of 15 randomly picked representative points from the ModelNet40 dataset in Figure 5, each ...
- **p. 7 / 4 Experiments - extractive PDF cue:** ShapeNet Parts S3DIS ScanNet pIoU mpIoU mIoU OA SyncSpecCNN [55] 84.74 82.0 - - Pd-Network [22] 85.49 82.7 - - SSCN [12] 85.98 83.3 - ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Table 3: Segmentation result comparisons on the S3DIS [2] Area 5 in overall accuracy (OA, %), micro-averaged accuracy (mAcc, %), micro-averaged IoU (mIoU, %) and ...
- **p. 7 / 4 Experiments - extractive PDF cue:** Note that the part averaged IoU metric for ShapeNet Parts is the one used in [56].

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 3: Segmentation result comparisons on the S3DIS [2] Area 5 in overall accuracy (OA, %), micro-averaged accuracy (mAcc, %), micro-averaged IoU (mIoU, %) ... | p. 14 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | PointCNN outperforms PointNet++ on both datasets, with a more prominent advantage on Quick Draw (25M data samples), which is significantly larger than TU-Berlin (0.02M ... | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Note that PointCNN achieved top performance on both ModelNet40 and ScanNet. | p. 6 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | For MNIST data, PointCNN achieved comparable performance with other methods, indicating its effective learning of the digits' shape information. | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | With the qualitative visualization and quantitative investigation, we conclude that though the "concentration" is far from reaching a point, the improvement is significant, and ... | p. 8 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 4 Experiments - extractive PDF cue:** Material Section 2, and the PointCNN architectures for the tasks on these datasets can be found in Supp.
- **p. 6 / 4 Experiments - extractive PDF cue:** We conducted an extensive evaluation of PointCNN for shape classification on six datasets (ModelNet40 [52], ScanNet [9], TU-Berlin [11], Quick Draw [15], MNIST, CIFAR10), and ...
- **p. 7 / 4 Experiments - extractive PDF cue:** We evaluate PointCNN on the segmentation of ShapeNet Parts, S3DIS, and ScanNet datasets, and summarize the results in Table 2.
- **p. 7 / 4 Experiments - extractive PDF cue:** It is interesting to study whether architectural elements from Sketch-a-Net can be adopted and integrated into PointCNN to improve its performance on the sketch datasets.
- **p. 8 / 4 Experiments - extractive PDF cue:** To verify this, we show T-SNE visualization of Fo, F∗and FX of 15 randomly picked representative points from the ModelNet40 dataset in Figure 5, each ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Convolution input from regular grids (i) and point clouds (ii-iv). In (i), each grid cell is associated with a feature. In (ii-iv), the ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: Hierarchical convolution on regular grids (upper) and point clouds (lower). In reg- ular grids, convolutions are recursively applied on local grid patches, which ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3: The process for converting point coordinates to features. Neighboring points are transformed to the local coordinate systems of the representative points (a and ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4: PointCNN architecture for classification (a and b) and segmentation (c), where N and C denote the output representative point number and feature dimen- ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: Comparisons of mean per-class accuracy (mA) and overall accuracy (OA) (%) on ModelNet40 [52] and Scan- Net [9]. The reported perfor- mances are ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: Segmentation comparisons on ShapeNet Parts in part-averaged IoU (pIoU, %) and mean per- class pIoU (mpIoU, %), S3DIS in mean per-class IoU (mIoU, ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3: Sketch classification results.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4: Image classification results. 4.2 Ablation Experiments and Visualizations Ablation test of the core X-Conv operator. To verify the effectiveness of the X-transformation, we ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Material Section 2, and the PointCNN architectures for the tasks on these datasets can be found in Supp. | embodiment, simulator version and control stack | p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Task/environment | We conducted an extensive evaluation of PointCNN for shape classification on six datasets (ModelNet40 [52], ScanNet [9], TU-Berlin [11], Quick Draw [15], MNIST, CIFAR10), ... | reset, timeout, object/scene variation | p. 6 (4 Experiments), p. 7 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1 Introduction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| ShapeNet Parts S3DIS ScanNet pIoU mpIoU mIoU OA SyncSpecCNN [55] 84.74 82.0 - - Pd-Network [22] 85.49 82.7 - - SSCN [12] 85.98 83.3 ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Table 3: Segmentation result comparisons on the S3DIS [2] Area 5 in overall accuracy (OA, %), micro-averaged accuracy (mAcc, %), micro-averaged IoU (mIoU, %) ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| Note that the part averaged IoU metric for ShapeNet Parts is the one used in [56]. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| PointCNN w/o X w/o X-W w/o X-D Core Layers X-Conv×4 Conv×4 Conv×4 Conv×5 # Parameter 0.6M 0.54M 0.63M 0.61M Accuracy (%) 92.2 90.7 90.8 ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Table 1: Comparisons of mean per-class accuracy (mA) and overall accuracy (OA) (%) on ModelNet40 [52] and Scan- Net [9]. The reported perfor- mances ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Note that PointCNN achieved top performance on both ModelNet40 and ScanNet. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| With these comparisons, we conclude that X-Conv is the key to the performance of PointCNN. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Figure 3: The process for converting point coordinates to features. Neighboring points are transformed to the local coordinate systems of the representative points (a ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We note that PointCNN outperforms all the compared methods, including SSCN [12], SPGraph [24] and SGPN [49], which are specialized segmentation networks with state-of-the-art ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| Table 4: Image classification results. 4.2 Ablation Experiments and Visualizations Ablation test of the core X-Conv operator. To verify the effectiveness of the X-transformation, ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 5: T-SNE visualization of features without (a/Fo), before (b/F∗) and after (c/FX ) X- transformation. the decrease in depth caused by the removal ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| PointCNN w/o X w/o X-W w/o X-D Core Layers X-Conv×4 Conv×4 Conv×4 Conv×5 # Parameter 0.6M 0.54M 0.63M 0.61M Accuracy (%) 92.2 90.7 90.8 ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| Table 1: Comparisons of mean per-class accuracy (mA) and overall accuracy (OA) (%) on ModelNet40 [52] and Scan- Net [9]. The reported perfor- mances ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 1: Segmentation result comparisons on ShapeNet Parts [54] in part-averaged IoU (pIoU, %) , mean per-class pIoU (mpIoU, %) and per-class pIoU (%). | comparison identity and matched condition | p. 14 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 4: Image classification results. 4.2 Ablation Experiments and Visualizations Ablation test of the core X-Conv operator. To verify the effectiveness of the X-transformation, ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Figure 5: T-SNE visualization of features without (a/Fo), before (b/F∗) and after (c/FX ) X- transformation. the decrease in depth caused by the removal ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| PointCNN w/o X w/o X-W w/o X-D Core Layers X-Conv×4 Conv×4 Conv×4 Conv×5 # Parameter 0.6M 0.54M 0.63M 0.61M Accuracy (%) 92.2 90.7 90.8 ... | component/input/data sensitivity | p. 8 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we propose to learn a K × K X-transformation for the coordinates of K input points (p1, p2, ..., pK), with ... | Table 3: Segmentation result comparisons on the S3DIS [2] Area 5 in overall accuracy (OA, %), micro-averaged accuracy (mAcc, %), micro-averaged IoU (mIoU, %) ... | PDF body cue; verify exact table/figure and matched conditions | p. 14 (Figure/Table caption), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (Figure/Table caption) |
| Primary metric/result | PointCNN outperforms PointNet++ on both datasets, with a more prominent advantage on Quick Draw (25M data samples), which is significantly larger than TU-Berlin (0.02M ... | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 8 / 4 Experiments - extractive PDF cue:** Methods PointNet [33] PointNet++ [35] 3DmFV-Net [4] DGCNN [50] SpecGCN [46] PCNN [3] PointCNN Parameters 3.48M 1.48M 45.77M 1.84M 2.05M 8.2M 0.6M FLOPs Training 43.82B ...
- **p. 2 / 1 Introduction - extractive PDF cue:** 1b, where the Xs are 4×4 matrices, as K = 4 in this figure.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Together with the lack of "shape" information, PointNet++ fails completely on this task. | p. 7 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| As shown in Table 6, we summarize our running statistics based with the model for classification with batch size 16, 1024 input points on ... | p. 8 (4 Experiments) |
| We implemented PointCNN in tensorflow [1], and use ADAM optimizer [21] with an initial learning rate 0.01 for the training of our models. | p. 8 (4 Experiments) |
| Based on this, if the convolution operator is directly applied, the output features for the three cases could be computed as depicted in Eq. | p. 2 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4 Experiments - extractive PDF cue:** Together with the lack of "shape" information, PointNet++ fails completely on this task.

- **PDF anchors reviewed:** datasets p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), metrics p. 7 (4 Experiments), p. 14 (Figure/Table caption), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 6 (Figure/Table caption), p. 6 (4 Experiments), baselines p. 7 (4 Experiments), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (4 Experiments), p. 6 (Figure/Table caption), p. 14 (Figure/Table caption), results p. 14 (Figure/Table caption), p. 7 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
