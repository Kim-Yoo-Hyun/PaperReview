# Evaluation - Details Matter for Indoor Open-vocabulary 3D Instance Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Jung_Details_Matter_for_Indoor_Open-vocabulary_3D_Instance_Segmentation_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. Qualitative Results), p. 6 (Figure/Table caption), p. 8 (4.4. Ablation Study), p. 7 (4.2. Quantitative Results), p. 8 (4.4. Ablation Study), p. 6 (4.1. Experimental Setup)): These visual results are consistent with the recall metrics: Open3DIS and OpenYOLO3D achieve the mAR of 43.3% and 47.7%, respectively, whereas our method significantly outperforms both with an mAR of ...

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Replica is a synthetic dataset created from digital replicas of real-world scenes, featuring 48 object classes across 8 different scenes.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** ScanNet200 is a real-world dataset comprising diverse indoor environments with 200 object categories.
- **p. 7 / 4.2. Quantitative Results - extractive PDF cue:** Qualitative comparisons on the ScanNet200 dataset.
- **p. 7 / 4.2. Quantitative Results - extractive PDF cue:** We hypothesize that the domain gap between real-world data and synthetic data from Replica may degrade the performance of Alpha-CLIP.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Class-agnostic evaluation on the ScanNet200 [7]. the ScanNet200 dataset.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Full ablation study on all three datasets can be found in the supplementary materials.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** We measure mean average precision (mAP) and mean average recall (mAR) at IOU thresholds of 25% and 50%.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Additionally, we measure mAP and mAR across IOU thresholds ranging from 50% to 95% with 5% increments.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setup (p. 6); 4.2. Quantitative Results (p. 6); 4.3. Qualitative Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Qualitative Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | These visual results are consistent with the recall metrics: Open3DIS and OpenYOLO3D achieve the mAR of 43.3% and 47.7%, respectively, whereas our method significantly ... | p. 7 (4.3. Qualitative Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. OV-3DIS results on the ScanNet200 validation set [7]. Top-1 evaluation protocol refers to assigning one predicted class per instance mask, and Top-K ... | p. 6 (Figure/Table caption) |
| 4.4. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown, using Alpha-CLIP improves the performance from 27.5 to 30.5 mAP, proving the importance of considering object-centric representation in instance classification. | p. 8 (4.4. Ablation Study) |
| 4.2. Quantitative Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | The resulting 2.3% and 4.3% mAP improvements over OpenYOLO3D demonstrate the effectiveness of our classification method. | p. 7 (4.2. Quantitative Results) |
| 4.4. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 6, applying iterative merging and removing improves AP25 by 5.0%. | p. 8 (4.4. Ablation Study) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Replica is a synthetic dataset created from digital replicas of real-world scenes, featuring 48 object classes across 8 different scenes.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** ScanNet200 is a real-world dataset comprising diverse indoor environments with 200 object categories.
- **p. 7 / 4.2. Quantitative Results - extractive PDF cue:** Qualitative comparisons on the ScanNet200 dataset.
- **p. 7 / 4.2. Quantitative Results - extractive PDF cue:** We hypothesize that the domain gap between real-world data and synthetic data from Replica may degrade the performance of Alpha-CLIP.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Class-agnostic evaluation on the ScanNet200 [7]. the ScanNet200 dataset.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Full ablation study on all three datasets can be found in the supplementary materials.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Examples of open-vocabulary predictions from our method in the ScanNet200 dataset [7]. Our method effectively retrieves instances based on functional descriptions (e.g., drink ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of image-based 3D proposal generation. We first remove overlaps between 2D predictions within each frame and lift them to 3D point cloud ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Matching tracklets with a new observation. We con- duct frame-wise sIOU comparisons between a new observation and each tracked instance in tracklets. If ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Effectiveness of 3D proposal refinement. Red boxes indicate the object of interest, and segments of different colors de- note 3D superpoints. Without refinement, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. Visualization of merged and removed proposals in the ScanNet200 dataset. Overlapping and noisy proposals often emerge after instance tracking. We effectively handle these ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 6. Failure cases of using CLIP for instance classification. CLIP fails when the shape of the object gets distorted or when other objects are ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. OV-3DIS results on the ScanNet200 validation set [7]. Top-1 evaluation protocol refers to assigning one predicted class per instance mask, and Top-K evaluation ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 7. Qualitative comparisons on the ScanNet200 dataset. Black regions indicate empty predictions (no object), while red boxes highlight objects missed by other methods but ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Replica is a synthetic dataset created from digital replicas of real-world scenes, featuring 48 object classes across 8 different scenes. | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Task/environment | ScanNet200 is a real-world dataset comprising diverse indoor environments with 200 object categories. | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Quantitative Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3.2. Open-Vocabulary Instance Classification), p. 4 (3.1. Image-based Proposal Generation) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.1. Image-based Proposal Generation), p. 5 (3.2. Open-Vocabulary Instance Classification) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We measure mean average precision (mAP) and mean average recall (mAR) at IOU thresholds of 25% and 50%. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| Additionally, we measure mAP and mAR across IOU thresholds ranging from 50% to 95% with 5% increments. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| The resulting 2.3% and 4.3% mAP improvements over OpenYOLO3D demonstrate the effectiveness of our classification method. | definition/direction/unit from same section | p. 7 (4.2. Quantitative Results) |
| As shown, using Alpha-CLIP improves the performance from 27.5 to 30.5 mAP, proving the importance of considering object-centric representation in instance classification. | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| Figure 5. Visualization of merged and removed proposals in the ScanNet200 dataset. Overlapping and noisy proposals often emerge after instance tracking. We effectively handle ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| To evaluate the quality of generated proposals, we report class-agnostic AP and AR on 9633 | definition/direction/unit from same section | p. 7 (4.4. Ablation Study) |
| Different Tracklet Matching Strategies. | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| Figure 4. Effectiveness of 3D proposal refinement. Red boxes indicate the object of interest, and segments of different colors de- note 3D superpoints. Without ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As reported in Table 2, our method consistently outperforms the baselines by a large margin in each experiment setting: 2D-only, 3D-only, and 2D+3D. | comparison identity and matched condition | p. 7 (4.2. Quantitative Results) |
| In 2D-only evaluations, our method outperforms previous SoTA methods, SAI3D and Open3DIS, by 8.8% and 7.2% , respectively. | comparison identity and matched condition | p. 7 (4.2. Quantitative Results) |
| As shown in Table 4, our 2Donly method outperforms all image-based approaches, surpassing the previous SoTA by 3.6%. | comparison identity and matched condition | p. 8 (4.4. Ablation Study) |
| We validate our method and baselines on the validation set, reporting performance for each category group (i.e., head, common, tail) as well as the ... | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| However, we note that our method with CLIP still surpasses existing baselines by a large margin (i.e., 3.8% over Open3DIS and 2.8% over OpenYOLO3D). | comparison identity and matched condition | p. 8 (4.4. Ablation Study) |
| Table 1. OV-3DIS results on the ScanNet200 validation set [7]. Top-1 evaluation protocol refers to assigning one predicted class per instance mask, and Top-K ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 4. Effectiveness of 3D proposal refinement. Red boxes indicate the object of interest, and segments of different colors de- note 3D superpoints. Without ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| This is because overlap removal effectively separates masks spanning multiple instances into each instance or partial masks, which later can be merged/removed. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| Figure 5. Visualization of merged and removed proposals in the ScanNet200 dataset. Overlapping and noisy proposals often emerge after instance tracking. We effectively handle ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| For the Replica dataset, we adjust τ merge to 0.7 and disable multiview consensus ratiobased filtering, as Replica is a synthetic dataset without projection ... | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |
| Full ablation study on all three datasets can be found in the supplementary materials. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| Figure 1. Examples of open-vocabulary predictions from our method in the ScanNet200 dataset [7]. Our method effectively retrieves instances based on functional descriptions (e.g., ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as follows: • We carefully combine the existing concepts and refine 3D proposal generation by removing overlaps in 2D predictions ... | These visual results are consistent with the recall metrics: Open3DIS and OpenYOLO3D achieve the mAR of 43.3% and 47.7%, respectively, whereas our method significantly ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. Qualitative Results), p. 6 (Figure/Table caption), p. 8 (4.4. Ablation Study), p. 7 (4.2. Quantitative Results), p. 8 (4.4. Ablation Study), p. 6 (4.1. Experimental Setup) |
| Primary metric/result | Table 1. OV-3DIS results on the ScanNet200 validation set [7]. Top-1 evaluation protocol refers to assigning one predicted class per instance mask, and Top-K ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** ScanNet200 is a real-world dataset comprising diverse indoor environments with 200 object categories.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** It includes 1,201 scenes in the training set and 312 scenes in the validation set.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** S3DIS consists of 271 scenes from 6 different areas, with Area 5 used for our evaluation.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Replica is a synthetic dataset created from digital replicas of real-world scenes, featuring 48 object classes across 8 different scenes.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Method AP AP50 AP25 Tracklet-wise sIOU for Tracking 34.7 54.3 69.6 Frame-wise sIOU for Tracking 35.1 (+0.4) 56.1 (+1.8) 70.5 (+0.9) Table 5.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Improving such limitations remains our future work. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 6. Failure cases of using CLIP for instance classification. CLIP fails when the shape of the object gets distorted or when other objects ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Also, we found that our method fails to improve performance on small objects (e.g., ScanNet++ in the supplementary) but rather remain similar to existing ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | However, it lags behind OpenYOLO3D [2] in terms of mAP, which does not use CLIP for instance classification. | p. 7 (4.2. Quantitative Results) |
| body limitation/failure cue | We hypothesize that the domain gap between real-world data and synthetic data from Replica may degrade the performance of Alpha-CLIP. | p. 7 (4.2. Quantitative Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| OV-3DIS results on S3DIS [1]. †numbers are obtained using their official codes. | p. 7 (4.2. Quantitative Results) |
| 2 illustrates the latter three steps in detail with examples. | p. 3 (3. Method) |
| Our image-based proposal generation is composed of four steps: 2D object grounding, 2D-to-3D lifting, 3D proposal aggregation, and iterative merging/removal. | p. 3 (3. Method) |
| Specifically, we compute the sIOU between the lifted 3D superpoints of the new observation and each tracked instance in each tracklet (see Fig. | p. 4 (3.1. Image-based Proposal Generation) |
| More detailed implementation can refer to supplementary materials. | p. 5 (3.1. Image-based Proposal Generation) |
| For each merging iteration, we compute IOU between a pair of 3D proposals, constructing a cost matrix Cmerge ∈[0, 1]K×K that is a strictly ... | p. 5 (3.1. Image-based Proposal Generation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** Improving such limitations remains our future work.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 6. Failure cases of using CLIP for instance classification. CLIP fails when the shape of the object gets distorted or when other objects are ...
- **p. 8 / 5. Conclusion - extractive PDF cue:** Also, we found that our method fails to improve performance on small objects (e.g., ScanNet++ in the supplementary) but rather remain similar to existing approaches.
- **p. 7 / 4.2. Quantitative Results - extractive PDF cue:** However, it lags behind OpenYOLO3D [2] in terms of mAP, which does not use CLIP for instance classification.
- **p. 7 / 4.2. Quantitative Results - extractive PDF cue:** We hypothesize that the domain gap between real-world data and synthetic data from Replica may degrade the performance of Alpha-CLIP.

- **PDF anchors reviewed:** datasets p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Quantitative Results), p. 7 (4.2. Quantitative Results), p. 8 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), metrics p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (4.2. Quantitative Results), p. 8 (4.4. Ablation Study), p. 5 (Figure/Table caption), p. 7 (4.4. Ablation Study), baselines p. 7 (4.2. Quantitative Results), p. 7 (4.2. Quantitative Results), p. 8 (4.4. Ablation Study), p. 6 (4.1. Experimental Setup), p. 8 (4.4. Ablation Study), p. 6 (Figure/Table caption), results p. 7 (4.3. Qualitative Results), p. 6 (Figure/Table caption), p. 8 (4.4. Ablation Study), p. 7 (4.2. Quantitative Results), p. 8 (4.4. Ablation Study), p. 6 (4.1. Experimental Setup).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
