# Evaluation - Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Jun-Seong_Dr._Splat_Directly_Referring_3D_Gaussian_Splatting_via_Direct_Language_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.2. 3D object localization), p. 8 (4.4. Ablation study), p. 7 (4. Experiments), p. 7 (4.1. 3D object selection), p. 5 (Figure/Table caption), p. 5 (Figure/Table caption)): Even with the 3D space search method, OpenGaussian [37], our model consistently demonstrates superior performance and achieves higher accuracy in localization.

## Evaluation Body Digest

- **p. 6 / 4. Experiments - extractive body cue:** 4.1), we use the LERF [17] dataset annotated by LangSplat [30], which consists of several multi-view images of 3D scenes containing long-tail objects and includes ...
- **p. 7 / 4. Experiments - extractive body cue:** ScanNet is a large-scale benchmark that provides data on indoor scenes, including calibrated RGBD images and 3D point clouds with ground-truth semantic labels.
- **p. 6 / 4. Experiments - extractive body cue:** 4.3 task, we employ the ScanNet [4] dataset.
- **p. 7 / 4.1. 3D object selection - extractive body cue:** The results demonstrate that our method performs better object selection in most scenes, showing an improvement of over 0.5 in mIoU and more than 4.5 ...
- **p. 8 / 4.2. 3D object localization - extractive body cue:** We report the 3D localization performance on the Scannet dataset in Table 2a.
- **p. 8 / 4.4. Ablation study - extractive body cue:** We conduct an ablation study using the ScanNet dataset on different hyper-parameters of Dr.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6. Limitations of point-based IoU measurement. This figure shows the effect of removing the top and bottom 30% of Gaussians according to the proposed ...
- **p. 7 / 4.2. 3D object localization - extractive body cue:** With the obtained significant scores d = [d1, d2, ..., dN], we compute weighted IoU of 3D Gaussians to approximate volumes.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. 3D object localization | EMPIRICAL / SOURCE-REPORTED EVALUATION | Even with the 3D space search method, OpenGaussian [37], our model consistently demonstrates superior performance and achieves higher accuracy in localization. | p. 8 (4.2. 3D object localization) |
| 4.4. Ablation study | EMPIRICAL / SOURCE-REPORTED EVALUATION | We observe that increasing the aggregating number of Gaussians per ray improves localization performance; however, it results in higher memory consumption and the number ... | p. 8 (4.4. Ablation study) |
| 4. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Note that, not specifically designed for segmentation, it achieves high performance as a result of language-based Gaussian updates. | p. 7 (4. Experiments) |
| 4.1. 3D object selection | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results demonstrate that our method performs better object selection in most scenes, showing an improvement of over 0.5 in mIoU and more than ... | p. 7 (4.1. 3D object selection) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 6. Limitations of point-based IoU measurement. This figure shows the effect of removing the top and bottom 30% of Gaussians according to the ... | p. 5 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4. Experiments - extractive body cue:** 4.1), we use the LERF [17] dataset annotated by LangSplat [30], which consists of several multi-view images of 3D scenes containing long-tail objects and includes ...
- **p. 7 / 4. Experiments - extractive body cue:** ScanNet is a large-scale benchmark that provides data on indoor scenes, including calibrated RGBD images and 3D point clouds with ground-truth semantic labels.
- **p. 6 / 4. Experiments - extractive body cue:** 4.3 task, we employ the ScanNet [4] dataset.
- **p. 7 / 4.1. 3D object selection - extractive body cue:** The results demonstrate that our method performs better object selection in most scenes, showing an improvement of over 0.5 in mIoU and more than 4.5 ...
- **p. 8 / 4.2. 3D object localization - extractive body cue:** We report the 3D localization performance on the Scannet dataset in Table 2a.
- **p. 8 / 4.4. Ablation study - extractive body cue:** We conduct an ablation study using the ScanNet dataset on different hyper-parameters of Dr.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Comparison of 2D (left) vs. our direct 3D search (right) for open-vocabulary 3D scene understanding. The 2D approach relies on multiview rendering, incurring ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Visualization of discrepancy in rendered 2D features and 3D features. Color indicates a cosine similarity score between query features from a text query ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Overview of Dr. Splat. (a) In the preprocessing stage, we compute optimized 3D Gaussians [16] and Product Quantization (PQ) codebook construction. (b) During ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Feature registration process in Dr. Splat. (a) We first map per-pixel CLIP embeddings {f map} to Gaussians. Here, we only map dominant k ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. 3D object selection results on the LeRF-OVS dataset [17]. To measure 3D object selection performance, we calculate 2D segmentation accuracy on rendering of ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative results of the object selection on the LeRF-OVS dataset [17]. We visualize rendering of selected 3D Gaussians for LangSplat [30], OpenGaussian [37], ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6. Limitations of point-based IoU measurement. This figure shows the effect of removing the top and bottom 30% of Gaussians according to the proposed ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Quantitative comparison in the ScanNet dataset [4]. Left: Localization prediction is defined as 3D regions with a text similarity score above threshold. Right: ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.1), we use the LERF [17] dataset annotated by LangSplat [30], which consists of several multi-view images of 3D scenes containing long-tail objects and ... | embodiment, simulator version and control stack | p. 6 (4. Experiments), p. 7 (4. Experiments) |
| Task/environment | ScanNet is a large-scale benchmark that provides data on indoor scenes, including calibrated RGBD images and 3D point clouds with ground-truth semantic labels. | reset, timeout, object/scene variation | p. 7 (4. Experiments), p. 6 (4. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 6 (3.3. Text-query based 3D localization), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.1. Feature registration process), p. 4 (3.1. Feature registration process) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 6. Limitations of point-based IoU measurement. This figure shows the effect of removing the top and bottom 30% of Gaussians according to the ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| With the obtained significant scores d = [d1, d2, ..., dN], we compute weighted IoU of 3D Gaussians to approximate volumes. | definition/direction/unit from same section | p. 7 (4.2. 3D object localization) |
| Given the ground truth, we measure IoU considering the spatial significance of each Gaussian and define a significant score di for each Gaussian θi ... | definition/direction/unit from same section | p. 7 (4.2. 3D object localization) |
| weight to the Gaussians with higher significant scores, when measuring IoU. | definition/direction/unit from same section | p. 8 (4.2. 3D object localization) |
| Even with the 3D space search method, OpenGaussian [37], our model consistently demonstrates superior performance and achieves higher accuracy in localization. | definition/direction/unit from same section | p. 8 (4.2. 3D object localization) |
| Table 1. 3D object selection results on the LeRF-OVS dataset [17]. To measure 3D object selection performance, we calculate 2D segmentation accuracy on rendering ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 2. Quantitative comparison in the ScanNet dataset [4]. Left: Localization prediction is defined as 3D regions with a text similarity score above threshold. ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 2. Visualization of discrepancy in rendered 2D features and 3D features. Color indicates a cosine similarity score between query features from a text ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The results demonstrate that our method performs better object selection in most scenes, showing an improvement of over 0.5 in mIoU and more than ... | comparison identity and matched condition | p. 7 (4.1. 3D object selection) |
| To study the various aspects of our method, we introduce baseline methods modified from rasterizationbased ones [30, 34], for direct 3D referring operation, denoted ... | comparison identity and matched condition | p. 7 (4. Experiments) |
| While OpenGaussian performs positionbased clustering, our model demonstrates comparable performance, surpassing the baseline as the Top-k value increases. | comparison identity and matched condition | p. 8 (4.3. 3D semantic segmentation) |
| Ablation study on (a) PQ and (b) Top-k Gaussians. | comparison identity and matched condition | p. 8 (4.4. Ablation study) |
| Figure 1. Comparison of 2D (left) vs. our direct 3D search (right) for open-vocabulary 3D scene understanding. The 2D approach relies on multiview rendering, ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Table 2. Quantitative comparison in the ScanNet dataset [4]. Left: Localization prediction is defined as 3D regions with a text similarity score above threshold. ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 6. Limitations of point-based IoU measurement. This figure shows the effect of removing the top and bottom 30% of Gaussians according to the ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| 2, without modification, global search over a whole scene is quite demanding. | component/input/data sensitivity | p. 7 (4. Experiments) |
| Ablation study on (a) PQ and (b) Top-k Gaussians. | component/input/data sensitivity | p. 8 (4.4. Ablation study) |
| We conduct an ablation study using the ScanNet dataset on different hyper-parameters of Dr. | component/input/data sensitivity | p. 8 (4.4. Ablation study) |
| Splat (ours) model on the same RGB-pretrained 3DGS. | component/input/data sensitivity | p. 7 (4. Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Splat, direct registration and referencing of language-aligned features in 3D Gaussians, bypassing intermediate rendering and preserving feature accuracy. • We introduce the PQ encoding ... | Even with the 3D space search method, OpenGaussian [37], our model consistently demonstrates superior performance and achieves higher accuracy in localization. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.2. 3D object localization), p. 8 (4.4. Ablation study), p. 7 (4. Experiments), p. 7 (4.1. 3D object selection), p. 5 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Primary metric/result | We observe that increasing the aggregating number of Gaussians per ray improves localization performance; however, it results in higher memory consumption and the number ... | numeric claim only at cited anchor | p. 8 (4.4. Ablation study) |

- Numeric sentences retained from the body:
- **p. 6 / 4. Experiments - extractive body cue:** 4.3 task, we employ the ScanNet [4] dataset.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | For LangSplat-m, the activations often shows random 3D Gaussians or fail to localize entirely (e.g., see "coffee mug"), highlighting the limitations of rasterization-based methods ... | p. 7 (4.1. 3D object selection) |
| body limitation/failure cue | Figure 6. Limitations of point-based IoU measurement. This figure shows the effect of removing the top and bottom 30% of Gaussians according to the ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Table 1. 3D object selection results on the LeRF-OVS dataset [17]. To measure 3D object selection performance, we calculate 2D segmentation accuracy on rendering ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Figure 7. Qualitative results of 3D object localization. We visualize 3D localization activations (yellow) for "chair" and "desk" in the ScanNet dataset, comparing our ... | p. 6 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We follow the hyperparameter settings favorable to each respective paper. | p. 7 (4. Experiments) |
| This artifacts can be attributed to use of spatial clustering and limited encoder capacity. | p. 7 (4.1. 3D object selection) |
| This gap This CVPR paper is the Open Access version, provided by the Computer Vision Foundation. | p. 1 (1. Introduction) |
| Open-vocabulary 3D scene understanding represents a significant challenge in the field of computer vision, with applications spanning autonomous navigation, robotics, and augmented reality. | p. 1 (1. Introduction) |
| The weights are computed as: w _ { ij} | p. 4 (3.1. Feature registration process) |
| (b) After collecting embeddings, we compute aggregated features (Eq. | p. 4 (3. Dr. Splat) |
| These centroids are learned via clustering, creating a codebook for each subspace. | p. 5 (3.2. Product-Quantized CLIP embeddings) |
| Once the centroids are established, each sub-vector is replaced by the index of the nearest centroid in its respective codebook. | p. 5 (3.2. Product-Quantized CLIP embeddings) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.1. 3D object selection - extractive body cue:** For LangSplat-m, the activations often shows random 3D Gaussians or fail to localize entirely (e.g., see "coffee mug"), highlighting the limitations of rasterization-based methods and ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6. Limitations of point-based IoU measurement. This figure shows the effect of removing the top and bottom 30% of Gaussians according to the proposed ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. 3D object selection results on the LeRF-OVS dataset [17]. To measure 3D object selection performance, we calculate 2D segmentation accuracy on rendering of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 7. Qualitative results of 3D object localization. We visualize 3D localization activations (yellow) for "chair" and "desk" in the ScanNet dataset, comparing our method ...

- **Evidence anchors reviewed:** datasets p. 6 (4. Experiments), p. 7 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.1. 3D object selection), p. 8 (4.2. 3D object localization), p. 8 (4.4. Ablation study), metrics p. 5 (Figure/Table caption), p. 7 (4.2. 3D object localization), p. 7 (4.2. 3D object localization), p. 8 (4.2. 3D object localization), p. 8 (4.2. 3D object localization), p. 5 (Figure/Table caption), baselines p. 7 (4.1. 3D object selection), p. 7 (4. Experiments), p. 8 (4.3. 3D semantic segmentation), p. 8 (4.4. Ablation study), p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), results p. 8 (4.2. 3D object localization), p. 8 (4.4. Ablation study), p. 7 (4. Experiments), p. 7 (4.1. 3D object selection), p. 5 (Figure/Table caption), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
