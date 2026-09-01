# Evaluation - OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhai_OnlinePG_Online_Open-Vocabulary_Panoptic_Mapping_with_3D_Gaussian_Splatting_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. Ablation Studies), p. 6 (4.2. Main Experiments), p. 6 (4.2. Main Experiments), p. 7 (4.2. Main Experiments), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies)): Compared to single-cue clustering, multi-cue clustering achieves 8 to 18 PRQ improvement with only ∼40 33275

## Evaluation Body Digest

- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** Following [50, 58], we take the commonly-used 8 scenes {room0-2,office0-4} for Replica dataset.
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** The two datasets both contain high-quality RGB-D sequences of various indoor scenes and 3D instance-level semantic annotations.
- **p. 7 / 4.2. Main Experiments - extractive PDF cue:** For Scene0645 in the ScanNetV2 dataset, our method takes an average of 410 ms to perform rendering optimization for 5 keyframes with 20 iterations, 350 ...
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** Qualitative 3D Semantic Segmentation Comparison of ScanNetV2 Dataset.
- **p. 6 / 4.2. Main Experiments - extractive PDF cue:** 1, our method achieves the best 3D semantic segmentation results among online approaches on the mIoU and mAcc metrics of two datasets.
- **p. 7 / 4.2. Main Experiments - extractive PDF cue:** 1, compared to the performance gap in 3D semantic segmentation, we further narrow the gap with offline baselines in 3D panoptic segmentation performance, even surpassing ...
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** The results are evaluated on ScanNetV2 dataset.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** Ablation studies of different matching strategies for global map fusion on ScanNetV2 dataset.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Settings (p. 5); 4.2. Main Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | Compared to single-cue clustering, multi-cue clustering achieves 8 to 18 PRQ improvement with only ∼40 33275 | p. 7 (4.3. Ablation Studies) |
| 4.2. Main Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1, our method achieves the best 3D semantic segmentation results among online approaches on the mIoU and mAcc metrics of two datasets. | p. 6 (4.2. Main Experiments) |
| 4.2. Main Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Compared to O2V-Mapping [42] and OnlineAnySeg [41], by maintaining and updating voxellevel spatial language feature grid F, we can achieve more fine-grained 3D scene ... | p. 6 (4.2. Main Experiments) |
| 4.2. Main Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method can achieve more consistent segmentation results among online approaches. | p. 7 (4.2. Main Experiments) |
| 4.3. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | Comparing #2 and #3, we can know that our spatial attribute module can improve the open-vocabulary scene understanding performance of our system. | p. 8 (4.3. Ablation Studies) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** Following [50, 58], we take the commonly-used 8 scenes {room0-2,office0-4} for Replica dataset.
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** The two datasets both contain high-quality RGB-D sequences of various indoor scenes and 3D instance-level semantic annotations.
- **p. 7 / 4.2. Main Experiments - extractive PDF cue:** For Scene0645 in the ScanNetV2 dataset, our method takes an average of 410 ms to perform rendering optimization for 5 keyframes with 20 iterations, 350 ...
- **p. 6 / 4.1. Experimental Settings - extractive PDF cue:** Qualitative 3D Semantic Segmentation Comparison of ScanNetV2 Dataset.
- **p. 6 / 4.2. Main Experiments - extractive PDF cue:** 1, our method achieves the best 3D semantic segmentation results among online approaches on the mIoU and mAcc metrics of two datasets.
- **p. 7 / 4.2. Main Experiments - extractive PDF cue:** 1, compared to the performance gap in 3D semantic segmentation, we further narrow the gap with offline baselines in 3D panoptic segmentation performance, even surpassing ...
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** The results are evaluated on ScanNetV2 dataset.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** Ablation studies of different matching strategies for global map fusion on ScanNetV2 dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Illustration of OnlinePG, which integrates geometric reconstruction and open-vocabulary panoptic perception built upon 3D Gaussian Splatting. Given the posed video stream and 2D ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of the proposed approach. Our system performs online open-vocabulary panoptic mapping from RGB-D streams using a local-to-global paradigm. (a) Maintaining a sliding ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. 3D Semantic and Panoptic Segmentation Results on ScanNetV2 and Replica Datasets. ∗indicates the baseline results are taken from [58] which use the 3D ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative 3D Semantic Segmentation Comparison of ScanNetV2 Dataset. Our approach outperforms recent online ap- proaches, O2V-Mapping [42] and OnlineAnySeg [41], by a large ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative Results of Open-Vocabulary Query. We use different colors to distinguish different instances found in the query. Compared to OnlineAnySeg [41], our approach ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. Left: ablation studies of using different segments clus- tering cues for local map construction. Right: ablation studies of using different feature grid resolutions. ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2. Ablation studies of different matching strategies for global map fusion on ScanNetV2 dataset. Settings PRQ (T) PRQ (S) #1 NN Match 24.67
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation studies of our system components. The results are evaluated on ScanNetV2 dataset. Settings mIoU PRQ (T) PRQ (S) #1 w/o. Segment Clustering ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Following [50, 58], we take the commonly-used 8 scenes {room0-2,office0-4} for Replica dataset. | embodiment, simulator version and control stack | p. 5 (4.1. Experimental Settings), p. 5 (4.1. Experimental Settings) |
| Task/environment | The two datasets both contain high-quality RGB-D sequences of various indoor scenes and 3D instance-level semantic annotations. | reset, timeout, object/scene variation | p. 5 (4.1. Experimental Settings), p. 7 (4.2. Main Experiments) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (3.2. Local Consistent Map Construction), p. 1 (1. Introduction) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 3 (3.2. Local Consistent Map Construction), p. 4 (3.2. Local Consistent Map Construction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 2, we show the performance of different matching strategies for fusing local map from the sliding window into global map. #1 represents using the ... | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |
| For open-vocabulary panoptic mapping evaluation, we adopt four widely-used metrics: 3D point-level mean Intersection over Union (mIoU), mean Accuracy (mAcc), and 3D Panoptic Reconstruction ... | definition/direction/unit from same section | p. 5 (4.1. Experimental Settings) |
| The results are evaluated on ScanNetV2 dataset. ms additional latency, demonstrating a favorable accuracyefficiency trade-off. | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |
| The performance also validates the effectiveness of our localto-global online reconstruction system, which consolidates the 2D inconsistency and obtains robust 3D panoptic map. | definition/direction/unit from same section | p. 7 (4.2. Main Experiments) |
| Segment clustering and local-to-global map fusion are performed every 7 keyframes. | definition/direction/unit from same section | p. 5 (4.1. Experimental Settings) |
| So, we mark their PRQ performance in gray. | definition/direction/unit from same section | p. 6 (4.1. Experimental Settings) |
| Compared with the offline SOTA PanoGS [58], our approach still exists a small performance gap. mentation approach [44] (trained on ScanNetV2 [5]) to obtain ... | definition/direction/unit from same section | p. 6 (4.1. Experimental Settings) |
| In contrast, our clusteringbased approach can obtain accurate instance-level information for objects with the same semantics. | definition/direction/unit from same section | p. 7 (4.2. Main Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 3. Qualitative 3D Semantic Segmentation Comparison of ScanNetV2 Dataset. Our approach outperforms recent online ap- proaches, O2V-Mapping [42] and OnlineAnySeg [41], by a ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Compared to the best current offline method, OnlineAnySeg [41], we outperformed by ∼13.8 and ∼11.5 in mIoU and mAcc. metrics, respectively. | comparison identity and matched condition | p. 7 (4.2. Main Experiments) |
| 1, compared to the performance gap in 3D semantic segmentation, we further narrow the gap with offline baselines in 3D panoptic segmentation performance, even ... | comparison identity and matched condition | p. 7 (4.2. Main Experiments) |
| 3D Semantic and Panoptic Segmentation Results on ScanNetV2 and Replica Datasets. ∗indicates the baseline results are taken from [58] which use the 3D instance ... | comparison identity and matched condition | p. 6 (4.1. Experimental Settings) |
| Unlike offline baselines [33, 50, 58] that use ground truth point clouds as input, our method reconstructs the scene from RGB-D streams. | comparison identity and matched condition | p. 5 (4.1. Experimental Settings) |
| Since the baselines [31, 33, 50] marked with ∗ cannot obtain 3D panoptic results, we use the performance reported in [58], which uses a ... | comparison identity and matched condition | p. 5 (4.1. Experimental Settings) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Additionally, we perform a detailed ablation study to validate the effect of each design in our system. | component/input/data sensitivity | p. 5 (4. Experiments) |
| Ablation studies of our system components. | component/input/data sensitivity | p. 8 (4.3. Ablation Studies) |
| Right: ablation studies of using different feature grid resolutions. | component/input/data sensitivity | p. 8 (4.3. Ablation Studies) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Overall, the technical contributions of our approach are summarized as follows: • We propose an online open-vocabulary panoptic mapping framework that unifies geometric reconstruction ... | Compared to single-cue clustering, multi-cue clustering achieves 8 to 18 PRQ improvement with only ∼40 33275 | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. Ablation Studies), p. 6 (4.2. Main Experiments), p. 6 (4.2. Main Experiments), p. 7 (4.2. Main Experiments), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies) |
| Primary metric/result | 1, our method achieves the best 3D semantic segmentation results among online approaches on the mIoU and mAcc metrics of two datasets. | numeric claim only at cited anchor | p. 6 (4.2. Main Experiments) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** Following [50, 58], we take the commonly-used 8 scenes {room0-2,office0-4} for Replica dataset.
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** We sample a keyframe every 20 frames and maintain a sliding window of size 12.
- **p. 7 / 4.2. Main Experiments - extractive PDF cue:** We evaluate the runtime performance of OnlinePG on a desktop computer equipped with an AMD Ryzen 9 7950X CPU and an NVIDIA RTX 4090 GPU.
- **p. 7 / 4.2. Main Experiments - extractive PDF cue:** For Scene0645 in the ScanNetV2 dataset, our method takes an average of 410 ms to perform rendering optimization for 5 keyframes with 20 iterations, 350 ...
- **p. 7 / 4.2. Main Experiments - extractive PDF cue:** Since clustering and fusion process multiple keyframes per sliding window movement (frequency much lower than framerate), our system achieves 18 FPS on simple scenes and ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations: (1) Our method currently cannot reconstruct dynamic objects. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Our future work will explore feed-forward approaches [20, 46, 47] that eliminate these requirements for fully pose-free and depth-free openvocabulary reconstruction. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Since the baselines [31, 33, 50] marked with ∗ cannot obtain 3D panoptic results, we use the performance reported in [58], which uses a ... | p. 5 (4.1. Experimental Settings) |
| body limitation/failure cue | While OnlineAnySeg can handle simple queries (e.g., "television"), it fails on some fine-grained and multi-instance queries (e.g., "pillow", "toilet paper", "bag") due to inaccurate ... | p. 7 (4.2. Main Experiments) |
| body limitation/failure cue | Since some offline baselines (LangSplat [33], OpenGaussian [50], OpenScene [31]) marked with ∗cannot inherently output 3D instances, PanoGS [58] provides supervised instance annotations [44] ... | p. 7 (4.2. Main Experiments) |
| body limitation/failure cue | Figure 1. Illustration of OnlinePG, which integrates geometric reconstruction and open-vocabulary panoptic perception built upon 3D Gaussian Splatting. Given the posed video stream and ... | p. 1 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We evaluate the runtime performance of OnlinePG on a desktop computer equipped with an AMD Ryzen 9 7950X CPU and an NVIDIA RTX 4090 ... | p. 7 (4.2. Main Experiments) |
| The hyperparameters are set as: α = 0.9, λ1 = 1.5, λ2 = 0.8. | p. 5 (4.1. Experimental Settings) |
| More detailed runtime analyses are provided in our Supp. | p. 7 (4.2. Main Experiments) |
| After clustering the 3D Gaussian segments, we voxelize the 3D space to efficiently compute and update spatial attributes. | p. 4 (3.2. Local Consistent Map Construction) |
| The semantic cue is then computed as the cosine similarity between language features: X(Si, Sj) = zi · zj/(//zi// · //zj//). | p. 4 (3.2. Local Consistent Map Construction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** Limitations: (1) Our method currently cannot reconstruct dynamic objects.
- **p. 8 / 5. Conclusion - extractive PDF cue:** Our future work will explore feed-forward approaches [20, 46, 47] that eliminate these requirements for fully pose-free and depth-free openvocabulary reconstruction.
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** Since the baselines [31, 33, 50] marked with ∗ cannot obtain 3D panoptic results, we use the performance reported in [58], which uses a supervised ...
- **p. 7 / 4.2. Main Experiments - extractive PDF cue:** While OnlineAnySeg can handle simple queries (e.g., "television"), it fails on some fine-grained and multi-instance queries (e.g., "pillow", "toilet paper", "bag") due to inaccurate 3D ...
- **p. 7 / 4.2. Main Experiments - extractive PDF cue:** Since some offline baselines (LangSplat [33], OpenGaussian [50], OpenScene [31]) marked with ∗cannot inherently output 3D instances, PanoGS [58] provides supervised instance annotations [44] for ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Illustration of OnlinePG, which integrates geometric reconstruction and open-vocabulary panoptic perception built upon 3D Gaussian Splatting. Given the posed video stream and 2D ...

- **PDF anchors reviewed:** datasets p. 5 (4.1. Experimental Settings), p. 5 (4.1. Experimental Settings), p. 7 (4.2. Main Experiments), p. 6 (4.1. Experimental Settings), p. 6 (4.2. Main Experiments), p. 7 (4.2. Main Experiments), metrics p. 8 (4.3. Ablation Studies), p. 5 (4.1. Experimental Settings), p. 8 (4.3. Ablation Studies), p. 7 (4.2. Main Experiments), p. 5 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), baselines p. 6 (Figure/Table caption), p. 7 (4.2. Main Experiments), p. 7 (4.2. Main Experiments), p. 6 (4.1. Experimental Settings), p. 5 (4.1. Experimental Settings), p. 5 (4.1. Experimental Settings), results p. 7 (4.3. Ablation Studies), p. 6 (4.2. Main Experiments), p. 6 (4.2. Main Experiments), p. 7 (4.2. Main Experiments), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
