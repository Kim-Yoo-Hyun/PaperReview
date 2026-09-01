# Evaluation - ST4R-Splat: Spatio-Temporal Referring Segmentation in 4D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Meng_ST4R-Splat_Spatio-Temporal_Referring_Segmentation_in_4D_Gaussian_Splatting_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Meng_ST4R-Splat_Spatio-Temporal_Referring_Segmentation_in_4D_Gaussian_Splatting_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Results), p. 6 (4.2. Results), p. 7 (4.2. Results), p. 7 (4.2. Results), p. 8 (4.2. Results), p. 8 (4.2. Results)): ST4RSplat achieves an average accuracy of 83.44% and vIoU 17603

## Evaluation Body Digest

- **p. 6 / 4.1. Setup - extractive PDF cue:** To adapt it to our dynamic 4D benchmark as a strong baseline for timeagnostic queries, we train the model utilizing the exact same instance masks ...
- **p. 6 / 4.1. Setup - extractive PDF cue:** We extend the HyperNeRF [27] dataset for the evaluation of STRS-4DGS task.
- **p. 7 / 4.2. Results - extractive PDF cue:** Quantitative comparisons on the HyperNeRF dataset.
- **p. 7 / 4.2. Results - extractive PDF cue:** 2 presents examples from two scenes, visualizing the activation heatmaps and the resulting segmentation masks (red contours) with non-target regions grayed out.
- **p. 8 / 4.2. Results - extractive PDF cue:** The performance is evaluated using the mIoU metric for time-agnostic queries on the HyperNeRF dataset.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** To validate the effectiveness of our design choices, we conduct ablation studies on our extended HyperNeRF dataset, as summarized in Table 2.
- **p. 6 / 4.1. Setup - extractive PDF cue:** To comprehensively assess both temporal accuracy and segmentation quality, we adopt the vIoU metric, defined as vIoU = 1 /Su/ P t∈Si IoU(ˆst, st), where ...
- **p. 6 / 4.1. Setup - extractive PDF cue:** For time-sensitive referring queries, we assess temporal performance using an accuracy metric, defined as Acc = ncorrect/nall, where ncorrect represents the number of correctly predicted ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.2. Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | ST4RSplat achieves an average accuracy of 83.44% and vIoU 17603 | p. 6 (4.2. Results) |
| 4.2. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method achieves an average mIoU of 77.67%, demonstrating exceptional segmentation performance. | p. 6 (4.2. Results) |
| 4.2. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Best results are highlighted in bold. of 57.98%, substantially outperforming 4DLangSplat. | p. 7 (4.2. Results) |
| 4.2. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Qualitative comparison of time-agnostic referring querying results between 4DLangSplat [22] and our method. | p. 7 (4.2. Results) |
| 4.2. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | The performance is evaluated using the mIoU metric for time-agnostic queries on the HyperNeRF dataset. | p. 8 (4.2. Results) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Setup - extractive PDF cue:** To adapt it to our dynamic 4D benchmark as a strong baseline for timeagnostic queries, we train the model utilizing the exact same instance masks ...
- **p. 6 / 4.1. Setup - extractive PDF cue:** We extend the HyperNeRF [27] dataset for the evaluation of STRS-4DGS task.
- **p. 7 / 4.2. Results - extractive PDF cue:** Quantitative comparisons on the HyperNeRF dataset.
- **p. 7 / 4.2. Results - extractive PDF cue:** 2 presents examples from two scenes, visualizing the activation heatmaps and the resulting segmentation masks (red contours) with non-target regions grayed out.
- **p. 8 / 4.2. Results - extractive PDF cue:** The performance is evaluated using the mIoU metric for time-agnostic queries on the HyperNeRF dataset.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** To validate the effectiveness of our design choices, we conduct ablation studies on our extended HyperNeRF dataset, as summarized in Table 2.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 1. Overview of the ST4R-Splat framework. It mainly consists of three main components: (I) MLLM-based object captioning for generating decoupled textual supervision, (II) an ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 2. Qualitative comparison of time-agnostic referring querying results between 4DLangSplat [22] and our method. For both methods, we visualize the activation heatmaps and the ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative comparisons on the HyperNeRF dataset. We report (a) time-agnostic referring querying (mIoU in %) and (b) time- sensitive referring querying (Acc and ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative comparison of time-sensitive query results in novel viewpoints between 4DLangSplat [22] and our method. Our method accurately resolves these spatial relations and ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2. Ablation study of different components in our ST4R-Splat framework. The performance is evaluated using the mIoU metric for time-agnostic queries on the HyperNeRF ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To adapt it to our dynamic 4D benchmark as a strong baseline for timeagnostic queries, we train the model utilizing the exact same instance ... | embodiment, simulator version and control stack | p. 6 (4.1. Setup), p. 6 (4.1. Setup) |
| Task/environment | We extend the HyperNeRF [27] dataset for the evaluation of STRS-4DGS task. | reset, timeout, object/scene variation | p. 6 (4.1. Setup), p. 7 (4.2. Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.2. Overview), p. 3 (3.1. Preliminaries) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| To comprehensively assess both temporal accuracy and segmentation quality, we adopt the vIoU metric, defined as vIoU = 1 /Su/ P t∈Si IoU(ˆst, st), ... | definition/direction/unit from same section | p. 6 (4.1. Setup) |
| For time-sensitive referring queries, we assess temporal performance using an accuracy metric, defined as Acc = ncorrect/nall, where ncorrect represents the number of correctly ... | definition/direction/unit from same section | p. 6 (4.1. Setup) |
| To isolate the temporal querying performance and eliminate errors from the initial spatial localization stage, we provide 4DLangSplat with groundtruth object masks as the ... | definition/direction/unit from same section | p. 8 (4.2. Results) |
| It fails to effectively obtain features representing the temporal state, resulting in a substantial drop in accuracy (51.92% Acc). | definition/direction/unit from same section | p. 8 (4.2. Results) |
| Figure 1. Overview of the ST4R-Splat framework. It mainly consists of three main components: (I) MLLM-based object captioning for generating decoupled textual supervision, (II) ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Consequently, we adapt state-of-the-art approaches from closely related domains to establish strong baselines: • ReferSplat [9]: The current state-of-the-art for referring segmentation in 3D ... | comparison identity and matched condition | p. 6 (4.1. Setup) |
| To adapt it to our dynamic 4D benchmark as a strong baseline for timeagnostic queries, we train the model utilizing the exact same instance ... | comparison identity and matched condition | p. 6 (4.1. Setup) |
| Best results are highlighted in bold. of 57.98%, substantially outperforming 4DLangSplat. | comparison identity and matched condition | p. 7 (4.2. Results) |
| Quantitative comparisons on the HyperNeRF dataset. | comparison identity and matched condition | p. 7 (4.2. Results) |
| Ablation study of different components in our ST4R-Splat framework. | comparison identity and matched condition | p. 8 (4.2. Results) |
| Qualitative comparison of time-sensitive query results in novel viewpoints between 4DLangSplat [22] and our method. | comparison identity and matched condition | p. 8 (4.2. Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To validate the effectiveness of our design choices, we conduct ablation studies on our extended HyperNeRF dataset, as summarized in Table 2. | component/input/data sensitivity | p. 8 (4.3. Ablation Studies) |
| Ablation study of different components in our ST4R-Splat framework. | component/input/data sensitivity | p. 8 (4.2. Results) |
| Figure 1. Overview of the ST4R-Splat framework. It mainly consists of three main components: (I) MLLM-based object captioning for generating decoupled textual supervision, (II) ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our main contributions are as follows: • We introduce the novel task of STRS-4DGS (SpatioTemporal Referring Segmentation in 4D Gaussian Splatting) and ... | ST4RSplat achieves an average accuracy of 83.44% and vIoU 17603 | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Results), p. 6 (4.2. Results), p. 7 (4.2. Results), p. 7 (4.2. Results), p. 8 (4.2. Results), p. 8 (4.2. Results) |
| Primary metric/result | Our method achieves an average mIoU of 77.67%, demonstrating exceptional segmentation performance. | numeric claim only at cited anchor | p. 6 (4.2. Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Setup - extractive PDF cue:** For evaluation, we provide 52 time-agnostic referring queries and 8 time-sensitive referring queries for 26 objects in 6 different scenes.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 4DLangSplat often fails to parse complex spatial relations within referring expressions. | p. 7 (4.2. Results) |
| body limitation/failure cue | It fails to effectively obtain features representing the temporal state, resulting in a substantial drop in accuracy (51.92% Acc). | p. 8 (4.2. Results) |
| body limitation/failure cue | To tackle this, we proposed ST4RSplat, which incorporates an Instance-Aware 4D Referring Field for robust spatial grounding and an Instance-Level Temporal State Mapping module ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 1. Overview of the ST4R-Splat framework. It mainly consists of three main components: (I) MLLM-based object captioning for generating decoupled textual supervision, (II) ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | For robust object segmentation and tracking, we use the Unipixel [25] model along with the Grounded-SAM-2 [24, 30] model. | p. 6 (4.1. Setup) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 3.5), we use the e5-mistral-7b [34] model to encode the time-aware state captions. | p. 6 (4.1. Setup) |
| Following the established practice in referring segmentation [9], we use the BERT [5] model to encode text embeddings for the instance-aware 4D gaussian referring ... | p. 6 (4.1. Setup) |
| This results in a pre-computed cache of state features: Ck = {ck,t / t ∈[0, T]}. | p. 5 (3.5. Instance-Level Temporal State Modeling) |
| We generate and encode time-aware state captions for each instance ok across all timestamps t. | p. 5 (3.5. Instance-Level Temporal State Modeling) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.2. Results - extractive PDF cue:** 4DLangSplat often fails to parse complex spatial relations within referring expressions.
- **p. 8 / 4.2. Results - extractive PDF cue:** It fails to effectively obtain features representing the temporal state, resulting in a substantial drop in accuracy (51.92% Acc).
- **p. 8 / 5. Conclusion - extractive PDF cue:** To tackle this, we proposed ST4RSplat, which incorporates an Instance-Aware 4D Referring Field for robust spatial grounding and an Instance-Level Temporal State Mapping module for ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 1. Overview of the ST4R-Splat framework. It mainly consists of three main components: (I) MLLM-based object captioning for generating decoupled textual supervision, (II) an ...
- **p. 6 / 4.1. Setup - extractive PDF cue:** For robust object segmentation and tracking, we use the Unipixel [25] model along with the Grounded-SAM-2 [24, 30] model.

- **PDF anchors reviewed:** datasets p. 6 (4.1. Setup), p. 6 (4.1. Setup), p. 7 (4.2. Results), p. 7 (4.2. Results), p. 8 (4.2. Results), p. 8 (4.3. Ablation Studies), metrics p. 6 (4.1. Setup), p. 6 (4.1. Setup), p. 8 (4.2. Results), p. 8 (4.2. Results), p. 4 (Figure/Table caption), baselines p. 6 (4.1. Setup), p. 6 (4.1. Setup), p. 7 (4.2. Results), p. 7 (4.2. Results), p. 8 (4.2. Results), p. 8 (4.2. Results), results p. 6 (4.2. Results), p. 6 (4.2. Results), p. 7 (4.2. Results), p. 7 (4.2. Results), p. 8 (4.2. Results), p. 8 (4.2. Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
