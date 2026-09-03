# Evaluation - 3D Weakly Supervised Semantic Segmentation with 2D Vision-Language Guidance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9223_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09223.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (Figure/Table caption), p. 12 (Figure/Table caption), p. 13 (Figure/Table caption), p. 14 (Figure/Table caption)): Table 1: Performance comparison on the S3DIS dataset. "Sup." indicates the type of supervision. "100%" represents full annotation. "scene." denotes scene-level annotation.

## Evaluation Body Digest

- **p. 9 / 4 Experiments - extractive body cue:** We adopt the default train-val split setting, where there are 1201 training scenes and 312 validation scenes.
- **p. 9 / 4 Experiments - extractive body cue:** ScanNet [10] has 1513 training scenes and 100 test scenes with 20 classes.
- **p. 9 / 4 Experiments - extractive body cue:** We reduce the learning rate by a multiplying factor of 0.7 every 20 epochs for a total of 80 epochs.
- **p. 9 / 4 Experiments - extractive body cue:** 3.2, we use Adam optimizer with batch size of 16 and set an initial learning rate of 0.003 for the model.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 2: The proposed pseudo label generation procedure. We first leverage the text encoder εtext of Openseg to get embeddings of the full category labels ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 1: Performance comparison on the S3DIS dataset. "Sup." indicates the type of supervision. "100%" represents full annotation. "scene." denotes scene-level annotation.
- **p. 12 / Figure/Table caption - extractive body cue:** Table 4: Performance comparisons of the generalization capability. Domain mIoU mAcc S3DIS ->ScanNet 13.4 23.0 ScanNet ->S3DIS 33.3 50.9 labels to supervised 3D model. Meanwhile, ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 5: Performance comparisons with different 3D backbones and ESS module back- bones on the S3DIS dataset. Module Backbone mIoU 3D MinkowskiNet14A 44.5 MinkowskiNet18A 45.3

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 9).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 1: Performance comparison on the S3DIS dataset. "Sup." indicates the type of supervision. "100%" represents full annotation. "scene." denotes scene-level annotation. | p. 10 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 4: Performance comparisons of the generalization capability. Domain mIoU mAcc S3DIS ->ScanNet 13.4 23.0 ScanNet ->S3DIS 33.3 50.9 labels to supervised 3D model. ... | p. 12 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 5: Performance comparisons with different 3D backbones and ESS module back- bones on the S3DIS dataset. Module Backbone mIoU 3D MinkowskiNet14A 44.5 MinkowskiNet18A ... | p. 13 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Fig. 4: Qualitative results on the S3DIS dataset of baseline and our 3DSS-VLG. From left to right: input point clouds, ground truth, baseline results, ... | p. 14 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 9 / 4 Experiments - extractive body cue:** We adopt the default train-val split setting, where there are 1201 training scenes and 312 validation scenes.
- **p. 9 / 4 Experiments - extractive body cue:** ScanNet [10] has 1513 training scenes and 100 test scenes with 20 classes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Comparison of different approaches. (a) The conventional 3D WSSS approach adopts the coarse-grained CAM method in a global manner and is supervised by ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 2: The proposed pseudo label generation procedure. We first leverage the text encoder εtext of Openseg to get embeddings of the full category labels ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 3: The proposed training procedure of our proposed 3DSS-VLG. Here, it is mainly divided into two stages: (a) Embeddings Specialization Stage and (b) Embeddings ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 1: Performance comparison on the S3DIS dataset. "Sup." indicates the type of supervision. "100%" represents full annotation. "scene." denotes scene-level annotation.
- **p. 11 / Figure/Table caption - extractive body cue:** Table 2: Performance comparison on the ScanNet test set and validation set. "Sup." indicates the type of supervision. "100%" represents full annotation. "subcloud." and "scene." ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 3: Ablation studies of the 3DSS-VLG components on S3DIS dataset. ESGS Filtering ESS mIoU (a) 37.7 (b) ✓ 38.2 (c)
- **p. 12 / Figure/Table caption - extractive body cue:** Table 4: Performance comparisons of the generalization capability. Domain mIoU mAcc S3DIS ->ScanNet 13.4 23.0 ScanNet ->S3DIS 33.3 50.9 labels to supervised 3D model. Meanwhile, ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 5: Performance comparisons with different 3D backbones and ESS module back- bones on the S3DIS dataset. Module Backbone mIoU 3D MinkowskiNet14A 44.5 MinkowskiNet18A 45.3

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We adopt the default train-val split setting, where there are 1201 training scenes and 312 validation scenes. | embodiment, simulator version and control stack | p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Task/environment | ScanNet [10] has 1513 training scenes and 100 test scenes with 20 classes. | reset, timeout, object/scene variation | p. 9 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (X. Xu et al), p. 3 (X. Xu et al) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (X. Xu et al), p. 6 (X. Xu et al) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We reduce the learning rate by a multiplying factor of 0.7 every 20 epochs for a total of 80 epochs. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| 3.2, we use Adam optimizer with batch size of 16 and set an initial learning rate of 0.003 for the model. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Fig. 2: The proposed pseudo label generation procedure. We first leverage the text encoder εtext of Openseg to get embeddings of the full category ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 1: Performance comparison on the S3DIS dataset. "Sup." indicates the type of supervision. "100%" represents full annotation. "scene." denotes scene-level annotation. | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Table 4: Performance comparisons of the generalization capability. Domain mIoU mAcc S3DIS ->ScanNet 13.4 23.0 ScanNet ->S3DIS 33.3 50.9 labels to supervised 3D model. ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Table 5: Performance comparisons with different 3D backbones and ESS module back- bones on the S3DIS dataset. Module Backbone mIoU 3D MinkowskiNet14A 44.5 MinkowskiNet18A ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The competing methods are then presented and compared. | comparison identity and matched condition | p. 9 (4 Experiments) |
| Fig. 4: Qualitative results on the S3DIS dataset of baseline and our 3DSS-VLG. From left to right: input point clouds, ground truth, baseline results, ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |
| Finally, ablation studies are provided to further demonstrate the necessity and effectiveness of each component of our framework. | comparison identity and matched condition | p. 9 (4 Experiments) |
| Fig. 1: Comparison of different approaches. (a) The conventional 3D WSSS approach adopts the coarse-grained CAM method in a global manner and is supervised ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Table 1: Performance comparison on the S3DIS dataset. "Sup." indicates the type of supervision. "100%" represents full annotation. "scene." denotes scene-level annotation. | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| Table 3: Ablation studies of the 3DSS-VLG components on S3DIS dataset. ESGS Filtering ESS mIoU (a) 37.7 (b) ✓ 38.2 (c) | comparison identity and matched condition | p. 12 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Finally, ablation studies are provided to further demonstrate the necessity and effectiveness of each component of our framework. | component/input/data sensitivity | p. 9 (4 Experiments) |
| Table 3: Ablation studies of the 3DSS-VLG components on S3DIS dataset. ESGS Filtering ESS mIoU (a) 37.7 (b) ✓ 38.2 (c) | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| Fig. 2: The proposed pseudo label generation procedure. We first leverage the text encoder εtext of Openseg to get embeddings of the full category ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, the main contributions of this paper are as follows: - We propose a weakly supervised method 3DSS-VLG for 3D WSSS, which takes ... | Table 1: Performance comparison on the S3DIS dataset. "Sup." indicates the type of supervision. "100%" represents full annotation. "scene." denotes scene-level annotation. | PDF body cue; verify exact table/figure and matched conditions | p. 10 (Figure/Table caption), p. 12 (Figure/Table caption), p. 13 (Figure/Table caption), p. 14 (Figure/Table caption) |
| Primary metric/result | Table 4: Performance comparisons of the generalization capability. Domain mIoU mAcc S3DIS ->ScanNet 13.4 23.0 ScanNet ->S3DIS 33.3 50.9 labels to supervised 3D model. ... | numeric claim only at cited anchor | p. 12 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 9 / 4 Experiments - extractive body cue:** We reduce the learning rate by a multiplying factor of 0.7 every 20 epochs for a total of 80 epochs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 3.2, we use Adam optimizer with batch size of 16 and set an initial learning rate of 0.003 for the model. | p. 9 (4 Experiments) |
| We reduce the learning rate by a multiplying factor of 0.7 every 20 epochs for a total of 80 epochs. | p. 9 (4 Experiments) |
| 3D Weakly Supervised Semantic Segmentation with 2D Vision-Language Guidance Xiaoxu Xu1, Yitian Yuan2 , Jinlong Li3 , Qiudan Zhang1 , Zequn Jie2 , Lin ... | p. 1 (Body text (section not recovered)) |
| We first process these multi-view images using the image encoder of the pretrained off-the-shelf 2D OVSS model such as Openseg [12] to get the ... | p. 3 (X. Xu et al) |
| We first leverage the text encoder εtext of Openseg to get embeddings of the full category labels FC, and leverage the 2D image encoder ... | p. 6 (X. Xu et al) |
| 2, we first implement dense 2D embeddings extraction for each RGB image via the frozen visual encoder of Openseg [12], and back-project them onto ... | p. 6 (X. Xu et al) |
| Similarly, we also freeze the text encoder and directly load the pretrained Openseg parameters. | p. 7 (X. Xu et al) |
| We take the text encoder of Openseg to exact text embeddings FC ∈RK×d of full category labels, where K denoted the number of categories. | p. 7 (X. Xu et al) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not recovered

- **Evidence anchors reviewed:** datasets p. 9 (4 Experiments), p. 9 (4 Experiments), metrics p. 9 (4 Experiments), p. 9 (4 Experiments), p. 6 (Figure/Table caption), p. 10 (Figure/Table caption), p. 12 (Figure/Table caption), p. 13 (Figure/Table caption), baselines p. 9 (4 Experiments), p. 14 (Figure/Table caption), p. 9 (4 Experiments), p. 2 (Figure/Table caption), p. 10 (Figure/Table caption), p. 12 (Figure/Table caption), results p. 10 (Figure/Table caption), p. 12 (Figure/Table caption), p. 13 (Figure/Table caption), p. 14 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
