# Evaluation - Segment then Splat: Unified 3D Open-Vocabulary Segmentation via Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ycPVp0577R; PDF retrieval source: https://arxiv.org/pdf/2503.22204.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (Figure/Table caption), p. 8 (4 Experiments), p. 14 (Figure/Table caption), p. 15 (Figure/Table caption)): Similar to the 3DOVS dataset, 2D pixel-based methods produce less precise object boundaries, while our method demonstrates significantly improved results.

## Evaluation Body Digest

- **p. 8 / 4 Experiments - extractive body cue:** (a) Static scenes LERF_OVS 3DOVS Method mIoU↑ Time↓ mIoU↑ Time↓ 2D LangSplat [10] 46.37 62.00 82.49 68.90 LEGaussians [11] 18.79 72.00 52.12 55.90 G-Grouping [36] ...
- **p. 9 / 4 Experiments - extractive body cue:** For scenes with fewer objects (e.g., chickchicken and split-cookie), performance quickly converges after a certain number of supervised objects.
- **p. 10 / 4 Experiments - extractive body cue:** In contrast, scenes with fewer objects (e.g., chickchicken, split-cookie) exhibit a smaller performance gain.
- **p. 7 / 4 Experiments - extractive body cue:** To assess the segmentation performance of our proposed method, we conduct experiments on two static scene datasets (i.e., 3DOVS dataset [37] and LERF_OVS dataset [9]) ...
- **p. 8 / 4 Experiments - extractive body cue:** In each iteration, we sample 1 object per granularity for 3DOVS to compute Lobj and 3 objects per granularity for all the remaining datasets.
- **p. 9 / 4 Experiments - extractive body cue:** In contrast, more complex scenes containing many objects (e.g., ramen and waldo_kitchen) continue to show performance improvements, though at a diminished rate.
- **p. 10 / 4 Experiments - extractive body cue:** Overall, the results validate the effectiveness of the partial mask filtering strategy, particularly in complex scenes with high object density.
- **p. 7 / 4 Experiments - extractive body cue:** For static scenes, we use LangSplat [10], LEGaussians [11] and Gaussian Grouping [36] as the 2D pixel-based baselines.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Similar to the 3DOVS dataset, 2D pixel-based methods produce less precise object boundaries, while our method demonstrates significantly improved results. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | In addition, our method achieves nearly a ten-fold improvement in optimization speed compared to DGD, as learning a dynamic language field is computationally intensive. | p. 9 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 6: Qualitative comparison on dynamic scenes. As our method enforce object-Gaussian correspondence, it applies directly to dynamic scenes and performs well, whereas DGD ... | p. 9 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Notably, 2D pixel-based methods tend to produce relatively ambiguous boundaries, whereas our approach, leveraging the Segment then Splat strategy, achieves significantly clearer object boundaries. | p. 8 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 7: Additional qualitative results on static scenes 7.2 Additional Ablation Study We conduct two additional ablation studies in this section. Object detection stride. ... | p. 14 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiments - extractive body cue:** (a) Static scenes LERF_OVS 3DOVS Method mIoU↑ Time↓ mIoU↑ Time↓ 2D LangSplat [10] 46.37 62.00 82.49 68.90 LEGaussians [11] 18.79 72.00 52.12 55.90 G-Grouping [36] ...
- **p. 9 / 4 Experiments - extractive body cue:** For scenes with fewer objects (e.g., chickchicken and split-cookie), performance quickly converges after a certain number of supervised objects.
- **p. 10 / 4 Experiments - extractive body cue:** In contrast, scenes with fewer objects (e.g., chickchicken, split-cookie) exhibit a smaller performance gain.
- **p. 7 / 4 Experiments - extractive body cue:** To assess the segmentation performance of our proposed method, we conduct experiments on two static scene datasets (i.e., 3DOVS dataset [37] and LERF_OVS dataset [9]) ...
- **p. 8 / 4 Experiments - extractive body cue:** In each iteration, we sample 1 object per granularity for 3DOVS to compute Lobj and 3 objects per granularity for all the remaining datasets.
- **p. 9 / 4 Experiments - extractive body cue:** In contrast, more complex scenes containing many objects (e.g., ramen and waldo_kitchen) continue to show performance improvements, though at a diminished rate.
- **p. 10 / 4 Experiments - extractive body cue:** Overall, the results validate the effectiveness of the partial mask filtering strategy, particularly in complex scenes with high object density.
- **p. 7 / 4 Experiments - extractive body cue:** For static scenes, we use LangSplat [10], LEGaussians [11] and Gaussian Grouping [36] as the 2D pixel-based baselines.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Traditional 3D Open-Vocabulary Segmentation vs. our Segment-then-Splat Pipeline. (a) The traditional Splat-then-Segment pipeline learns a language field alongside the reconstruction of the entire ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Demonstration of Segment then Splat pipeline. We first extracts multi-view masks for each object through a robust tracking module, then object IDs are ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3: A demonstration of how the optimization order af- fects reconstruction. Optimizing small-level objects first pre- serves both small- and middle-level structures, while starting ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative comparison on static scenes. Compared to baseline methods, our approach accurately retrieves the correct object and produces sharper segmentation boundaries. In contrast, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Quantitative segmentation results for static (a) and dynamic (b) scenes. (a) Static scenes LERF_OVS 3DOVS
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5: Comparison between 2D pixel-based segmentation and our 3D segmentation. Unlike 2D pixel-based methods, which are limited by oc- clusions, our approach can retrieve ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 6: Qualitative comparison on dynamic scenes. As our method enforce object-Gaussian correspondence, it applies directly to dynamic scenes and performs well, whereas DGD and ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Ablation studies: (Top) Number of supervised objects per iteration. (Middle) Partial mask filtering. (Bottom) Tracking module ablation. (a) Number of supervised objects per ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | (a) Static scenes LERF_OVS 3DOVS Method mIoU↑ Time↓ mIoU↑ Time↓ 2D LangSplat [10] 46.37 62.00 82.49 68.90 LEGaussians [11] 18.79 72.00 52.12 55.90 G-Grouping ... | embodiment, simulator version and control stack | p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Task/environment | For scenes with fewer objects (e.g., chickchicken and split-cookie), performance quickly converges after a certain number of supervised objects. | reset, timeout, object/scene variation | p. 9 (4 Experiments), p. 10 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 4 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3 Method), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Leveraging ground-truth labels, we adopt two metrics: Object Recall Rate (ORR), defined as ORR = 1 k k X i=1 number of tracked objects ... | definition/direction/unit from same section | p. 10 (4 Experiments) |
| Figure 1: Traditional 3D Open-Vocabulary Segmentation vs. our Segment-then-Splat Pipeline. (a) The traditional Splat-then-Segment pipeline learns a language field alongside the reconstruction of the ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| One thing to be mentioned is that, due to the nature of 3D segmentation and the evaluation used for open-vocabulary segmentation, there is a ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| In contrast, more complex scenes containing many objects (e.g., ramen and waldo_kitchen) continue to show performance improvements, though at a diminished rate. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| In this ablation study, we investigate the impact of the partial mask filtering strategy on segmentation performance as well as reconstruction quality. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| We categorize the baselines into two groups based on their querying strategies: 2D pixel-based segmentation and 3D-based segmentation. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| For the 3D baselines, we choose OpenGaussian[13], and we also adapt LangSplat and LEGaussians for 3D segmentation by selecting Gaussians instead of pixels to ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| For geometric-appearances distance, we set λd to 0.5. | definition/direction/unit from same section | p. 8 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method outperforms all baseline approaches. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Additionally, since our method follows a single-pass reconstruction process and the scene scale is relatively small, our training time is significantly shorter compared to ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| Figure 4: Qualitative comparison on static scenes. Compared to baseline methods, our approach accurately retrieves the correct object and produces sharper segmentation boundaries. In ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| For static scenes, we use LangSplat [10], LEGaussians [11] and Gaussian Grouping [36] as the 2D pixel-based baselines. | comparison identity and matched condition | p. 7 (4 Experiments) |
| In addition, our method achieves nearly a ten-fold improvement in optimization speed compared to DGD, as learning a dynamic language field is computationally intensive. | comparison identity and matched condition | p. 9 (4 Experiments) |
| 4.3 Ablation Study Number of Supervised Objects. | comparison identity and matched condition | p. 9 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conduct an ablation study on each component of our robust object tracking module, as shown in Tab. | component/input/data sensitivity | p. 10 (4 Experiments) |
| Since our method explicitly enforces Gaussian-object correspondence, it can be directly applied to dynamic scenes, achieving good segmentation performance without the Gaussian-object misalignment issue ... | component/input/data sensitivity | p. 8 (4 Experiments) |
| 4.3 Ablation Study Number of Supervised Objects. | component/input/data sensitivity | p. 9 (4 Experiments) |
| In this ablation study, we investigate the impact of the partial mask filtering strategy on segmentation performance as well as reconstruction quality. | component/input/data sensitivity | p. 10 (4 Experiments) |
| Table 3: Effect of stride size on object recall rate (ORR) and runtime. ramen teatime Stride ORR↑ Time↓ ORR↑ Time↓ | component/input/data sensitivity | p. 14 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our key contributions include: • We propose Segment then Splat, a novel paradigm that segments Gaussians into object sets before reconstruction. | Similar to the 3DOVS dataset, 2D pixel-based methods produce less precise object boundaries, while our method demonstrates significantly improved results. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (Figure/Table caption), p. 8 (4 Experiments), p. 14 (Figure/Table caption), p. 15 (Figure/Table caption) |
| Primary metric/result | In addition, our method achieves nearly a ten-fold improvement in optimization speed compared to DGD, as learning a dynamic language field is computationally intensive. | numeric claim only at cited anchor | p. 9 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 8 / 4 Experiments - extractive body cue:** In each iteration, we sample 1 object per granularity for 3DOVS to compute Lobj and 3 objects per granularity for all the remaining datasets.
- **p. 9 / 4 Experiments - extractive body cue:** HyperNeRF Object Queries LSeg DGD Ours Hand Hand Chicken Chicken Object Queries LSeg DGD Ours LSeg DGD Ours Hand Chicken Object Queries T = 1 ...
- **p. 5 / 3 Method - extractive body cue:** 3.3 Object-Specific Gaussian Initialization As our method follows a "segmentation then reconstruction" strategy, we first segment the Gaussians initialized by COLMAP into distinct sets, each ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Another limitation is that our method cannot effectively handle text queries involving relational descriptions across multiple objects, such as "a sheep sitting on the ... | p. 10 (5 Conclusion) |
| body limitation/failure cue | However, this minor failure does not affect the final reconstruction, as sufficient information is retained from other views. | p. 10 (4 Experiments) |
| body limitation/failure cue | Moreover, because DGD does not directly supervise the language embeddings of each Gaussian, Gaussians located far apart may share similar embeddings, further deteriorating segmentation ... | p. 9 (4 Experiments) |
| body limitation/failure cue | Figure 2: Demonstration of Segment then Splat pipeline. We first extracts multi-view masks for each object through a robust tracking module, then object IDs ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | The new object detection stride ∆t in the robust object tracking is set to 10. | p. 8 (4 Experiments) |
| body limitation/failure cue | Unlike 2D pixel-based methods, which are limited by occlusions, our approach can retrieve the complete object even from an occluded view. | p. 8 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Additionally, since our method follows a single-pass reconstruction process and the scene scale is relatively small, our training time is significantly shorter compared to ... | p. 8 (4 Experiments) |
| We omit training time results for LSeg, as it is a zero-shot method requiring no additional optimization. | p. 9 (4 Experiments) |
| To balance training time and performance, we choose three objects for LERF_OVS, Neu3D and HyperNeRF in our experiments. | p. 10 (4 Experiments) |
| All experiments are conducted using a RTX A6000 GPU. | p. 8 (4 Experiments) |
| As our method enforce object-Gaussian correspondence, it applies directly to dynamic scenes and performs well, whereas DGD and LSeg tend to include irrelevant content ... | p. 9 (4 Experiments) |
| The final pixel color is then computed through alpha blending, which integrates the weighted Gaussian colors from front to back: bC = X i∈N ... | p. 4 (3 Method) |
| These strategies transform SAM-based segmentation into a flexible, scene-adaptive tracking pipeline, which serves as the critical foundation for subsequent steps in our methodology. | p. 5 (3 Method) |
| Specifically, we render each reconstructed object into 2D images, compute their Intersectionover-Union (IoU) against the provided masks, and discard masks exhibiting low IoU scores. | p. 6 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 5 Conclusion - extractive body cue:** Another limitation is that our method cannot effectively handle text queries involving relational descriptions across multiple objects, such as "a sheep sitting on the chair ...
- **p. 10 / 4 Experiments - extractive body cue:** However, this minor failure does not affect the final reconstruction, as sufficient information is retained from other views.
- **p. 9 / 4 Experiments - extractive body cue:** Moreover, because DGD does not directly supervise the language embeddings of each Gaussian, Gaussians located far apart may share similar embeddings, further deteriorating segmentation quality.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Demonstration of Segment then Splat pipeline. We first extracts multi-view masks for each object through a robust tracking module, then object IDs are ...
- **p. 8 / 4 Experiments - extractive body cue:** The new object detection stride ∆t in the robust object tracking is set to 10.
- **p. 8 / 4 Experiments - extractive body cue:** Unlike 2D pixel-based methods, which are limited by occlusions, our approach can retrieve the complete object even from an occluded view.

- **Evidence anchors reviewed:** datasets p. 8 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), metrics p. 10 (4 Experiments), p. 2 (Figure/Table caption), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 7 (4 Experiments), baselines p. 8 (4 Experiments), p. 8 (4 Experiments), p. 7 (Figure/Table caption), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), results p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (Figure/Table caption), p. 8 (4 Experiments), p. 14 (Figure/Table caption), p. 15 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
