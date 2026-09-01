# Evaluation - Segment Any 3D Object with Language

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ENv1CeTwxc; PDF retrieval source: https://openreview.net/pdf/49d9ee59e578038d8529a39c19e31d4c61cdc5fe.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (Figure/Table caption), p. 19 (Figure/Table caption), p. 8 (4 EXPERIMENTS)): SOLE outperforms all the OV-3DIS methods and achieves competitive results with the fully-supervised model.

## Evaluation Body Digest

- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** Therefore, despite slightly impairing the performance on benchmark, mask-visual association and mask-caption association are crucial to recognizing free-form language instructions, benefiting the applications in real-world ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** We evaluate SOLE on the popular scene understanding datasets: ScanNetv2 (Dai et al., 2017), ScanNet200 (Rozenberszki et al., 2022) and Replica (Straub et al., 2019) ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Replica (Straub et al., 2019) is a high-quality synthetic dataset annotated with 48 instance categories.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Following (Takmaz et al., 2023), we evaluate on eight scenes in Replica for open-set instance segmentation, including {office0, office1, office2, office3, office4, room0, room1 and ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** All of the studies are evaluated on ScanNetv2 (Dai et al., 2017) dataset.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Furthermore, to verify the generalization ability of SOLE when both domain shift and category shift exist, we compare our framework with all of the mask ...
- **p. 17 / A IMPLEMENTATION DETAILS - extractive PDF cue:** B 3D VISUAL GROUNDING To further verify the effectiveness of SOLE on various language instructions, we conduct experiments on 3D visual grounding benchmark ScanRefer (Chen ...
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** Given the free-form language instruction, "I wanna see outside.", SOLE trained only with f MEA captures the wrong object ((a)), whereas it segments the related ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 7); A IMPLEMENTATION DETAILS (p. 17).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | SOLE outperforms all the OV-3DIS methods and achieves competitive results with the fully-supervised model. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | SOLE outperforms state-of-the-art methods (Nguyen et al., 2024; Takmaz et al., 2023) on five out of the six metrics and achieves comparable performance on ... | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | First, using any of multimodal associations can already achieve significant performance, outperforming previous state-of-the-art method (OpenIns3D (Huang et al., 2023b)) with larger voxel size ... | p. 10 (4 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Tab. 3. Our SOLE outperforms OpenMask3D (Takmaz et al., 2023) and Open3DIS (Nguyen et al., 2024) by a large margin on both base and ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 10: Analysis of the light version of SOLE on ScanNetv2 (Dai et al., 2017). Despite of performance drop, SOLE-light still outperforms mask-training methods ... | p. 19 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** Therefore, despite slightly impairing the performance on benchmark, mask-visual association and mask-caption association are crucial to recognizing free-form language instructions, benefiting the applications in real-world ...
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** We evaluate SOLE on the popular scene understanding datasets: ScanNetv2 (Dai et al., 2017), ScanNet200 (Rozenberszki et al., 2022) and Replica (Straub et al., 2019) ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Replica (Straub et al., 2019) is a high-quality synthetic dataset annotated with 48 instance categories.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Following (Takmaz et al., 2023), we evaluate on eight scenes in Replica for open-set instance segmentation, including {office0, office1, office2, office3, office4, room0, room1 and ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** All of the studies are evaluated on ScanNetv2 (Dai et al., 2017) dataset.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Furthermore, to verify the generalization ability of SOLE when both domain shift and category shift exist, we compare our framework with all of the mask ...
- **p. 17 / A IMPLEMENTATION DETAILS - extractive PDF cue:** B 3D VISUAL GROUNDING To further verify the effectiveness of SOLE on various language instructions, we conduct experiments on 3D visual grounding benchmark ScanRefer (Chen ...
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** Given the free-form language instruction, "I wanna see outside.", SOLE trained only with f MEA captures the wrong object ((a)), whereas it segments the related ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Qualitative results of SOLE with various language instructions. SOLE is highly gen- eralizable and can segment corresponding instances with various language instructions, including ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2: Left (a) : Previous works train class-agnostic mask proposal module with only using mask annotations. In the inference time, generated 3D masks are ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3: Overall framework of SOLE. SOLE is built on transformer-based instance segmentation model with multimodal adaptations. For model architecture, backbone features are integrated with ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4: Three types of multimodal association instance. For each ground truth instance mask, we first pool the per-point CLIP features to obtain Mask-Visual Association ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: The comparison of closed-set 3D instance segmentation setting on ScanNetv2. SOLE is compared with mask-training methods and the fully-supervised counterpart (upper bound). SOLE ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: The comparison of closed-set 3D instance segmentation setting on ScanNet200. SOLE is compared with mask training methods on the overall segmentation performance and ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: The comparison of hierarchical open-set 3D instance segmentation setting on Scan- Netv2 (Dai et al., 2017)→ScanNet200 (Rozenberszki et al., 2022). SOLE is compared ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 4: The comparison of open-set 3D instance segmentation setting on ScanNet200 (Rozen- berszki et al., 2022)→Replica (Straub et al., 2019). SOLE outperforms state-of-the-art meth- ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Therefore, despite slightly impairing the performance on benchmark, mask-visual association and mask-caption association are crucial to recognizing free-form language instructions, benefiting the applications in ... | embodiment, simulator version and control stack | p. 10 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Task/environment | We evaluate SOLE on the popular scene understanding datasets: ScanNetv2 (Dai et al., 2017), ScanNet200 (Rozenberszki et al., 2022) and Replica (Straub et al., ... | reset, timeout, object/scene variation | p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3 METHOD), p. 3 (1 INTRODUCTION) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Average precision (AP) of different IoU thresholds is adopted as the evaluation metric, including AP under 25%, 50% IoU and the average AP from ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| 4, our method further shows superior robustness on more out-of-distribution data from Replica, achieving +9.8% improvement in AP score compared to Open3DIS. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| The best results are in bold while the second best results are underscored. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| 6, reporting the scores of various combinations on ScanNetv2 (Dai et al., 2017) with 4cm voxel size. | definition/direction/unit from same section | p. 10 (4 EXPERIMENTS) |
| This observation shows that mask-visual association and maskcaption association can help semantic learning but impair mask accuracy. | definition/direction/unit from same section | p. 10 (4 EXPERIMENTS) |
| Larger voxel size can save the memory requirements and speed up the model with the loss of precision. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Figure 3: Overall framework of SOLE. SOLE is built on transformer-based instance segmentation model with multimodal adaptations. For model architecture, backbone features are integrated ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Table 11: Analysis of compatibility with previous works on ScanNet200 (Rozenberszki et al., 2022). SOLE shows high compatibility with previous mask training methods, achieving ... | definition/direction/unit from same section | p. 20 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 2: The comparison of closed-set 3D instance segmentation setting on ScanNet200. SOLE is compared with mask training methods on the overall segmentation performance ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| SOLE outperforms state-of-the-art methods (Takmaz et al., 2023; Nguyen et al., 2024) on all the evaluation metrics. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| First, using any of multimodal associations can already achieve significant performance, outperforming previous state-of-the-art method (OpenIns3D (Huang et al., 2023b)) with larger voxel size ... | comparison identity and matched condition | p. 10 (4 EXPERIMENTS) |
| Table 1: The comparison of closed-set 3D instance segmentation setting on ScanNetv2. SOLE is compared with mask-training methods and the fully-supervised counterpart (upper bound). ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 6: K-means clustering of different backbone features. Different colors denote different clusters. OCRand and VoteRand where training is not required, the other four ... | comparison identity and matched condition | p. 18 (Figure/Table caption) |
| Tab. 3. Our SOLE outperforms OpenMask3D (Takmaz et al., 2023) and Open3DIS (Nguyen et al., 2024) by a large margin on both base and ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Finally, we provide two variants of SOLE to further verify our effectiveness. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| Furthermore, we verify that the effectiveness of our framework is not limited to the caption model and NLP tools by conducting experiments without any ... | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| 5, we conduct component analysis on multimodal fusion network, validating the effectiveness of backbone feature ensemble and Cross-Modality Decoder (CMD). | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |
| Figure 6: K-means clustering of different backbone features. Different colors denote different clusters. OCRand and VoteRand where training is not required, the other four ... | component/input/data sensitivity | p. 18 (Figure/Table caption) |
| We analyze the components of multimodal associations (f MVA, f MCA, and f MEA) in Tab. | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |
| Table 8: Analysis on classification probability ensemble. Results are reported on the ScanNetv2 (Dai et al., 2017) dataset in 2cm voxel size. Component AP ... | component/input/data sensitivity | p. 19 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To circumvent this issue, we introduce Cross Modality Decoder (CMD) to incorporate textual information in the decoding process of our framework. | SOLE outperforms all the OV-3DIS methods and achieves competitive results with the fully-supervised model. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (Figure/Table caption), p. 19 (Figure/Table caption), p. 8 (4 EXPERIMENTS) |
| Primary metric/result | SOLE outperforms state-of-the-art methods (Nguyen et al., 2024; Takmaz et al., 2023) on five out of the six metrics and achieves comparable performance on ... | numeric claim only at cited anchor | p. 9 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Method AP AP50 AP25 APhead APcom APtail OpenIns3D (Huang et al., 2023b) 8.8 10.3 14.4 16.0 6.5 4.2 OpenMask3D (Takmaz et al., 2023) 15.4 19.9 ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** The feature backbone extracts point features in 5 scales, while 4 layers of transformer decoder iteratively refine the instance queries.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Our model is trained for 600 epochs with AdamW (Loshchilov & Hutter, 2017) optimizer.
- **p. 17 / A IMPLEMENTATION DETAILS - extractive PDF cue:** For each 3D point cloud scene, we use farthest point sampling (Qi et al., 2017) to get 150 points as object queries.
- **p. 17 / A IMPLEMENTATION DETAILS - extractive PDF cue:** For each 3D point cloud scene, we use farthest point sampling (Qi et al., 2017) to get 150 points as object queries.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2: Left (a) : Previous works train class-agnostic mask proposal module with only using mask annotations. In the inference time, generated 3D masks ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | In contrast, solely using 3D instance backbone feature f b (second row) cannot inherit the generalizable semantic information, resulting in sub-optimal performance. | p. 10 (4 EXPERIMENTS) |
| body limitation/failure cue | Given a free-form language instruction instead of category name, e.g., "I wanna see outside", the model only using mask-entity association cannot segment the correct ... | p. 10 (4 EXPERIMENTS) |
| body limitation/failure cue | 4, our method further shows superior robustness on more out-of-distribution data from Replica, achieving +9.8% improvement in AP score compared to Open3DIS. | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | Both in-distribution ("base") and out-of-distribution ("novel") classes are reported in Tab. | p. 9 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The learning rate is set to 1 × 10-4 with cyclical decay. | p. 8 (4 EXPERIMENTS) |
| Our model is trained for 600 epochs with AdamW (Loshchilov & Hutter, 2017) optimizer. | p. 8 (4 EXPERIMENTS) |
| Additionally, Cross Modality Decoder (CMD) can further enhance the ability to understand language instructions, improving AP by 1.6%. | p. 10 (4 EXPERIMENTS) |
| 5, we conduct component analysis on multimodal fusion network, validating the effectiveness of backbone feature ensemble and Cross-Modality Decoder (CMD). | p. 10 (4 EXPERIMENTS) |
| 3.1) and textual information in the decoder (Sec. | p. 4 (3 METHOD) |
| Specifically, the transformer decoders with mask queries are used to segment instances. | p. 4 (3 METHOD) |
| Finally, incorporated point-wise features with multiple resolutions are fed into cross modality decoder. | p. 5 (3 METHOD) |
| 3.2 CROSS MODALITY DECODER (CMD) Projected 2D CLIP features provide generalizable visual information but the language information is not explicitly integrated, limiting the responsive ... | p. 5 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2: Left (a) : Previous works train class-agnostic mask proposal module with only using mask annotations. In the inference time, generated 3D masks are ...
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** In contrast, solely using 3D instance backbone feature f b (second row) cannot inherit the generalizable semantic information, resulting in sub-optimal performance.
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** Given a free-form language instruction instead of category name, e.g., "I wanna see outside", the model only using mask-entity association cannot segment the correct instance ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** 4, our method further shows superior robustness on more out-of-distribution data from Replica, achieving +9.8% improvement in AP score compared to Open3DIS.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Both in-distribution ("base") and out-of-distribution ("novel") classes are reported in Tab.

- **PDF anchors reviewed:** datasets p. 10 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), metrics p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), baselines p. 8 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 8 (Figure/Table caption), p. 18 (Figure/Table caption), p. 9 (Figure/Table caption), results p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (Figure/Table caption), p. 19 (Figure/Table caption), p. 8 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
