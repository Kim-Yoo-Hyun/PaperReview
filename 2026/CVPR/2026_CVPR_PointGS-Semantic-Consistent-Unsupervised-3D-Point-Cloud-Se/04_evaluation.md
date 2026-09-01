# Evaluation - PointGS: Semantic-Consistent Unsupervised 3D Point Cloud Segmentation with 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Song_PointGS_Semantic-Consistent_Unsupervised_3D_Point_Cloud_Segmentation_with_3D_Gaussian_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Song_PointGS_Semantic-Consistent_Unsupervised_3D_Point_Cloud_Segmentation_with_3D_Gaussian_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. 3D Unsupervised Semantic Segmentation), p. 8 (4.4. Parameter Sensitivity Experiment), p. 6 (4.2. 3D Unsupervised Semantic Segmentation), p. 7 (4.2. 3D Unsupervised Semantic Segmentation), p. 7 (4.3. Ablation Experiment), p. 8 (4.4. Parameter Sensitivity Experiment)): Relative to the state-of-theart LogoSP, we achieve a 0.9% improvement in mIoU.

## Evaluation Body Digest

- **p. 6 / 4.1. Experiment Details - extractive PDF cue:** S3DIS contains 271 scenes with 13 classes.
- **p. 6 / 4.1. Experiment Details - extractive PDF cue:** Dataset and Implementation Details: We evaluate our method on two large-scale indoor datasets: ScanNet-v2 [8] and S3DIS [2].
- **p. 7 / 4.2. 3D Unsupervised Semantic Segmentation - extractive PDF cue:** Additionally, qualitative experiments conducted on the S3DIS Area 5 dataset, as depicted in Fig.
- **p. 7 / 4.3. Ablation Experiment - extractive PDF cue:** To showcase the effectiveness of each module, we conduct four groups of experiments on the S3DIS[2] Area 5 dataset: (1) the baseline projection approach proposed ...
- **p. 8 / 4.4. Parameter Sensitivity Experiment - extractive PDF cue:** This parameter needs to be adjusted according to different scenes.
- **p. 8 / 4.4. Parameter Sensitivity Experiment - extractive PDF cue:** 6 favors surround (49.3% mIoU) over tiled (45.9%), as the circular path ensures uniform scene encapsulation, reducing blind spots in indoor scenes.
- **p. 6 / 4.1. Experiment Details - extractive PDF cue:** For evaluation metrics, we report the standard mean Intersection-over-Union (mIoU), overall accuracy (oAcc) and mean accuracy (mAcc) across all classes.
- **p. 8 / 4.4. Parameter Sensitivity Experiment - extractive PDF cue:** Although it can improve the segmentation accuracy of smaller items, it sacrifices the semantic consistency of larger items.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experiment Details (p. 6); 4.3. Ablation Experiment (p. 7); 4.4. Parameter Sensitivity Experiment (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. 3D Unsupervised Semantic Segmentation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Relative to the state-of-theart LogoSP, we achieve a 0.9% improvement in mIoU. | p. 6 (4.2. 3D Unsupervised Semantic Segmentation) |
| 4.4. Parameter Sensitivity Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | Although it can improve the segmentation accuracy of smaller items, it sacrifices the semantic consistency of larger items. | p. 8 (4.4. Parameter Sensitivity Experiment) |
| 4.2. 3D Unsupervised Semantic Segmentation | EMPIRICAL / SOURCE-REPORTED EVALUATION | In the absence of any human annotations or pre-training on point cloud data, our method outperforms the majority of these baselines. | p. 6 (4.2. 3D Unsupervised Semantic Segmentation) |
| 4.2. 3D Unsupervised Semantic Segmentation | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in the table, our approach surpasses the best baseline, achieving +2.8 mIoU improvement. | p. 7 (4.2. 3D Unsupervised Semantic Segmentation) |
| 4.3. Ablation Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | The significantly enhanced performance indicates the necessity of 2-Step ICP for the 3D-GS method. | p. 7 (4.3. Ablation Experiment) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experiment Details - extractive PDF cue:** S3DIS contains 271 scenes with 13 classes.
- **p. 6 / 4.1. Experiment Details - extractive PDF cue:** Dataset and Implementation Details: We evaluate our method on two large-scale indoor datasets: ScanNet-v2 [8] and S3DIS [2].
- **p. 7 / 4.2. 3D Unsupervised Semantic Segmentation - extractive PDF cue:** Additionally, qualitative experiments conducted on the S3DIS Area 5 dataset, as depicted in Fig.
- **p. 7 / 4.3. Ablation Experiment - extractive PDF cue:** To showcase the effectiveness of each module, we conduct four groups of experiments on the S3DIS[2] Area 5 dataset: (1) the baseline projection approach proposed ...
- **p. 8 / 4.4. Parameter Sensitivity Experiment - extractive PDF cue:** This parameter needs to be adjusted according to different scenes.
- **p. 8 / 4.4. Parameter Sensitivity Experiment - extractive PDF cue:** 6 favors surround (49.3% mIoU) over tiled (45.9%), as the circular path ensures uniform scene encapsulation, reducing blind spots in indoor scenes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. In the conference room scene, the upper part of the figure shows that the sparse point cloud causes the foreground points and background ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. The pipeline of our method. Given an indoor point cloud, we first generate multi-view projections and apply Gaussian splatting. Then, the rendered images ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative comparison of unsupervised segmentation on the S3DIS validation set. Each color represents one semantic class. For better understanding, we show some of ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison of unsupervised segmentation on the ScanNet-v2 validation set. Unsupervised Methods mIoU(%) PC-HC [13] 4.63 PiCIE [7]
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison of unsupervised segmentation on the S3DIS validation set (Area 5). Unsupervised Methods mIoU(%) oAcc(%) mAcc(%) PC-HC [13] 9.3
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Impact of varying the number of projection views (V ) on S3DIS Area 5. V S3DIS (mIoU%) 50 35.9 75 42.2
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Impact of varying angular intervals on S3DIS Area 5. ∆elev (◦) ∆azim (◦) S3DIS (mIoU%) 0.1 5.5 48.6 0.3
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 5. Ablation experiments of PointGS on the S3DIS Area5. 3D-GS 2-Step ICP Affinity Feature Multi-View Consistency Check mIoU

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | S3DIS contains 271 scenes with 13 classes. | embodiment, simulator version and control stack | p. 6 (4.1. Experiment Details), p. 6 (4.1. Experiment Details) |
| Task/environment | Dataset and Implementation Details: We evaluate our method on two large-scale indoor datasets: ScanNet-v2 [8] and S3DIS [2]. | reset, timeout, object/scene variation | p. 6 (4.1. Experiment Details), p. 7 (4.2. 3D Unsupervised Semantic Segmentation) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 4 (3.2. Preliminary) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.2. Preliminary), p. 6 (3.5. Gaussian-to-Point Cloud Alignment) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For evaluation metrics, we report the standard mean Intersection-over-Union (mIoU), overall accuracy (oAcc) and mean accuracy (mAcc) across all classes. | definition/direction/unit from same section | p. 6 (4.1. Experiment Details) |
| Although it can improve the segmentation accuracy of smaller items, it sacrifices the semantic consistency of larger items. | definition/direction/unit from same section | p. 8 (4.4. Parameter Sensitivity Experiment) |
| Figure 2. The pipeline of our method. Given an indoor point cloud, we first generate multi-view projections and apply Gaussian splatting. Then, the rendered ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| To evaluate the performance of the unsupervised method, we establish evaluation practices from prior studies. | definition/direction/unit from same section | p. 6 (4.1. Experiment Details) |
| The significantly enhanced performance indicates the necessity of 2-Step ICP for the 3D-GS method. | definition/direction/unit from same section | p. 7 (4.3. Ablation Experiment) |
| Impact of varying angular intervals on S3DIS Area 5. ∆elev (◦) ∆azim (◦) S3DIS (mIoU%) 0.1 5.5 48.6 0.3 6.5 49.1 0.5 7.5 49.3 ... | definition/direction/unit from same section | p. 7 (4.3. Ablation Experiment) |
| It can be seen that the segmentation performance reaches its optimum when the Scale Gate is 0.4. | definition/direction/unit from same section | p. 8 (4.4. Parameter Sensitivity Experiment) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In the absence of any human annotations or pre-training on point cloud data, our method outperforms the majority of these baselines. | comparison identity and matched condition | p. 6 (4.2. 3D Unsupervised Semantic Segmentation) |
| 5, our full model clearly outperforms the baseline on all of the evaluation metrics, benefiting from the 2-Step ICP, Affinity Feature, and Multi-View Consistency ... | comparison identity and matched condition | p. 7 (4.3. Ablation Experiment) |
| 3.3, (2) adding 3D-GS to the baseline without alignment. | comparison identity and matched condition | p. 7 (4.3. Ablation Experiment) |
| 1, We compare our approach with prior unsupervised 3D point cloud segmentation methods, including PC-HC [13], PointDC [6], U3DS3 [20], and LogoSP [46], as ... | comparison identity and matched condition | p. 6 (4.2. 3D Unsupervised Semantic Segmentation) |
| Comparison of projection distribution types on S3DIS Area 5. | comparison identity and matched condition | p. 8 (4.4. Parameter Sensitivity Experiment) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To showcase the effectiveness of each module, we conduct four groups of experiments on the S3DIS[2] Area 5 dataset: (1) the baseline projection approach ... | component/input/data sensitivity | p. 7 (4.3. Ablation Experiment) |
| Label Matching and Metric: As our approach operates in an unsupervised manner, without prior knowledge of the ground truth labels, the resulting clusters may ... | component/input/data sensitivity | p. 6 (4.1. Experiment Details) |
| Ablation experiments of PointGS on the S3DIS Area5. | component/input/data sensitivity | p. 7 (4.3. Ablation Experiment) |
| Scale Gate S3DIS (mIoU%) 0.2 46.6 0.3 48.5 0.4 49.3 0.5 47.7 0.6 35.1 We further analyze SAM-specific parameters: cluster selection epsilon (ϵ) for ... | component/input/data sensitivity | p. 8 (4.4. Parameter Sensitivity Experiment) |
| A smaller Scale Gate value will amplify the channels in the features corresponding to fine-grained segmentation (such as object components). | component/input/data sensitivity | p. 8 (4.4. Parameter Sensitivity Experiment) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as follows: • We leverage Gaussian Splatting as a unified intermediate representation for unsupervised point cloud segmentation, effectively bridging ... | Relative to the state-of-theart LogoSP, we achieve a 0.9% improvement in mIoU. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. 3D Unsupervised Semantic Segmentation), p. 8 (4.4. Parameter Sensitivity Experiment), p. 6 (4.2. 3D Unsupervised Semantic Segmentation), p. 7 (4.2. 3D Unsupervised Semantic Segmentation), p. 7 (4.3. Ablation Experiment), p. 8 (4.4. Parameter Sensitivity Experiment) |
| Primary metric/result | Although it can improve the segmentation accuracy of smaller items, it sacrifices the semantic consistency of larger items. | numeric claim only at cited anchor | p. 8 (4.4. Parameter Sensitivity Experiment) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experiment Details - extractive PDF cue:** S3DIS contains 271 scenes with 13 classes.
- **p. 6 / 4.1. Experiment Details - extractive PDF cue:** To test the generality of our method, we do not use the official multi-view images from either dataset and rely solely on RGB information from ...
- **p. 6 / 4.1. Experiment Details - extractive PDF cue:** Efficiency is measured on a single NVIDIA RTX 3090 GPU.
- **p. 6 / 4.1. Experiment Details - extractive PDF cue:** The vanilla 3D-GS performs 43.27 iterations per second, and SAM processes images at 0.35 frames per second.
- **p. 5 / 3.5. Gaussian-to-Point Cloud Alignment - extractive PDF cue:** Let PG = {(pn, lG n )}N n=1 denote the aligned Gaussian centers with labels, and let PO = {bm}M m=1 denote the original point ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This alignment enables a robust measurement of semantic consistency between the inferred partitions and the reference annotations, while mitigating the impact of label permutations ... | p. 6 (4.1. Experiment Details) |
| body limitation/failure cue | Scale Gate S3DIS (mIoU%) 0.2 46.6 0.3 48.5 0.4 49.3 0.5 47.7 0.6 35.1 We further analyze SAM-specific parameters: cluster selection epsilon (ϵ) for ... | p. 8 (4.4. Parameter Sensitivity Experiment) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Efficiency is measured on a single NVIDIA RTX 3090 GPU. | p. 6 (4.1. Experiment Details) |
| To balance efficiency and quality, we run 3D-GS for 10,000 iterations per scene. | p. 6 (4.1. Experiment Details) |
| We perform parameter sensitivity analysis on key projection hyperparameters-the number of views (V ), angular intervals in elevation (∆elev) and azimuth (∆azim), and distribution ... | p. 7 (4.4. Parameter Sensitivity Experiment) |
| A key advantage is differentiable rasterization, which projects 3D Gaussians to 2D image planes and computes pixel colors via alpha compositing (depth-sorted blending of ... | p. 3 (3.2. Preliminary) |
| It computes the scale sM of a 2D mask M in a view-consistent manner by projecting M into 3D space using camera intrinsics and ... | p. 3 (3.2. Preliminary) |
| For supervision, we compute pixel correspondences from sorted masks based on their 3D scales sM (v) j . | p. 5 (3.4. Semantic Information Distillation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.1. Experiment Details - extractive PDF cue:** This alignment enables a robust measurement of semantic consistency between the inferred partitions and the reference annotations, while mitigating the impact of label permutations in ...
- **p. 8 / 4.4. Parameter Sensitivity Experiment - extractive PDF cue:** Scale Gate S3DIS (mIoU%) 0.2 46.6 0.3 48.5 0.4 49.3 0.5 47.7 0.6 35.1 We further analyze SAM-specific parameters: cluster selection epsilon (ϵ) for boundary ...

- **PDF anchors reviewed:** datasets p. 6 (4.1. Experiment Details), p. 6 (4.1. Experiment Details), p. 7 (4.2. 3D Unsupervised Semantic Segmentation), p. 7 (4.3. Ablation Experiment), p. 8 (4.4. Parameter Sensitivity Experiment), p. 8 (4.4. Parameter Sensitivity Experiment), metrics p. 6 (4.1. Experiment Details), p. 8 (4.4. Parameter Sensitivity Experiment), p. 4 (Figure/Table caption), p. 6 (4.1. Experiment Details), p. 7 (4.3. Ablation Experiment), p. 7 (4.3. Ablation Experiment), baselines p. 6 (4.2. 3D Unsupervised Semantic Segmentation), p. 7 (4.3. Ablation Experiment), p. 7 (4.3. Ablation Experiment), p. 6 (4.2. 3D Unsupervised Semantic Segmentation), p. 8 (4.4. Parameter Sensitivity Experiment), results p. 6 (4.2. 3D Unsupervised Semantic Segmentation), p. 8 (4.4. Parameter Sensitivity Experiment), p. 6 (4.2. 3D Unsupervised Semantic Segmentation), p. 7 (4.2. 3D Unsupervised Semantic Segmentation), p. 7 (4.3. Ablation Experiment), p. 8 (4.4. Parameter Sensitivity Experiment).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
