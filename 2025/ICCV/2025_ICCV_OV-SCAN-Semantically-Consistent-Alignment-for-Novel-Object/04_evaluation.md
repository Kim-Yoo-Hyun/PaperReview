# Evaluation - OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Chow_OV-SCAN_Semantically_Consistent_Alignment_for_Novel_Object_Discovery_in_Open-Vocabulary_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Chow_OV-SCAN_Semantically_Consistent_Alignment_for_Novel_Object_Discovery_in_Open-Vocabulary_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.3. Ablation Studies), p. 7 (4.2. Main Results), p. 7 (4.2. Main Results), p. 1 (Figure/Table caption), p. 8 (4.3. Ablation Studies), p. 2 (Figure/Table caption)): A simple occlusion filter with a fixed threshold ςocc yields a notable performance gain, while class-based thresholds achieve the highest improvement (+1.7 mAP).

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Our OV-3D object detection experiments are conducted on the nuScenes [2] and KITTI [12] datasets.
- **p. 7 / 4.2. Main Results - extractive PDF cue:** The OV-3D object detection results for topperforming methods on the nuScenes dataset can be seen in Tab.
- **p. 7 / 4.2. Main Results - extractive PDF cue:** SC-NOD generates 319,028 3D annotations for training, a fraction of the 797,179 available in the nuScenes dataset.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** To assess the effectiveness of our adaptive 3D box search in SC-NOD, we evaluate its performance on the nuScenes dataset, comparing it to the greedy ...
- **p. 8 / 4.2. Main Results - extractive PDF cue:** OV-SCAN performs inference on a set of urban scenes identifying a diverse set of objects.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** In our experiments, novel classes (open-set classes) are based on the nuScenes and KITTI class labels.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 3. Sources of Semantic Discrepancies. (a) CLIP sim- ilarity scores for a truck reveal that occlusion cases result in an ambiguous 2D image feature. ...
- **p. 7 / 4.1. Experimental Setup - extractive PDF cue:** For KITTI, we compute APs for three classes using a stricter 3D IoU at a 0.5 matching threshold.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setup (p. 6); 4.2. Main Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | A simple occlusion filter with a fixed threshold ςocc yields a notable performance gain, while class-based thresholds achieve the highest improvement (+1.7 mAP). | p. 8 (4.3. Ablation Studies) |
| 4.2. Main Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Without being given 3D human-annotations, OV-SCAN achieves an AP score above 60 for both car and pedestrian categories. | p. 7 (4.2. Main Results) |
| 4.2. Main Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Furthermore, we show that simply adding camera as an additional input modality to OV-SCAN and then fine-tuning can improve the overall performance. | p. 7 (4.2. Main Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1. Cross-modal Alignment Performance. The red CDF shows the distance distribution between 3D embeddings from a baseline OV-3D detector and 2D CLIP embeddings ... | p. 1 (Figure/Table caption) |
| 4.3. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | 3 shows that our method consistently outperforms the greedy search even with fewer iterations per novel object. | p. 8 (4.3. Ablation Studies) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Our OV-3D object detection experiments are conducted on the nuScenes [2] and KITTI [12] datasets.
- **p. 7 / 4.2. Main Results - extractive PDF cue:** The OV-3D object detection results for topperforming methods on the nuScenes dataset can be seen in Tab.
- **p. 7 / 4.2. Main Results - extractive PDF cue:** SC-NOD generates 319,028 3D annotations for training, a fraction of the 797,179 available in the nuScenes dataset.
- **p. 8 / 4.3. Ablation Studies - extractive PDF cue:** To assess the effectiveness of our adaptive 3D box search in SC-NOD, we evaluate its performance on the nuScenes dataset, comparing it to the greedy ...
- **p. 8 / 4.2. Main Results - extractive PDF cue:** OV-SCAN performs inference on a set of urban scenes identifying a diverse set of objects.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** In our experiments, novel classes (open-set classes) are based on the nuScenes and KITTI class labels.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Cross-modal Alignment Performance. The red CDF shows the distance distribution between 3D embeddings from a baseline OV-3D detector and 2D CLIP embeddings on ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. 3D Annotation Errors. Common 3D annotation errors during box parametrization, including but not limited to, poor L- shape fitting, misinterpreted surfaces, and misaligned ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 3. Sources of Semantic Discrepancies. (a) CLIP sim- ilarity scores for a truck reveal that occlusion cases result in an ambiguous 2D image feature. ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Overall Framework for OV-SCAN. During novel object discovery, SC-NOD associates novel object proposals with cor- responding object clusters, creating cross-modal proposals. SC-NOD performs ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Illustration of the Hierarchical Two-Stage Alignment (H2SA) Head. H2SA first predicts the high-level novel classes, then derives class-based text prompts. H2SA then uses ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Results on nuScenes. We report the overall mAP, NDS, and individual class APs. All classes are novel (i.e., no human annotations are used ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Results on KITTI. We report the overall AP3D@50 for each class at medium difficulty. All classes are novel.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Ablations on Adaptive 3D Box Search. We evaluate performance on nuScenes using different box search methods and varying numbers of search iterations per ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our OV-3D object detection experiments are conducted on the nuScenes [2] and KITTI [12] datasets. | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Main Results) |
| Task/environment | The OV-3D object detection results for topperforming methods on the nuScenes dataset can be seen in Tab. | reset, timeout, object/scene variation | p. 7 (4.2. Main Results), p. 7 (4.2. Main Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 3 (3.1. Notation and Preliminaries) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.1. Notation and Preliminaries), p. 4 (3.1. Notation and Preliminaries) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 3. Sources of Semantic Discrepancies. (a) CLIP sim- ilarity scores for a truck reveal that occlusion cases result in an ambiguous 2D image ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| For KITTI, we compute APs for three classes using a stricter 3D IoU at a 0.5 matching threshold. | definition/direction/unit from same section | p. 7 (4.1. Experimental Setup) |
| Without being given 3D human-annotations, OV-SCAN achieves an AP score above 60 for both car and pedestrian categories. | definition/direction/unit from same section | p. 7 (4.2. Main Results) |
| This simplification results in a performance drop (-5.9 mAP). | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |
| Furthermore, incorporating class-based text prompts to guide cross-modal alignment further enhances performance (+1.7 mAP). | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |
| Figure 2. 3D Annotation Errors. Common 3D annotation errors during box parametrization, including but not limited to, poor L- shape fitting, misinterpreted surfaces, and ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 1. Cross-modal Alignment Performance. The red CDF shows the distance distribution between 3D embeddings from a baseline OV-3D detector and 2D CLIP embeddings ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 5. Illustration of the Hierarchical Two-Stage Alignment (H2SA) Head. H2SA first predicts the high-level novel classes, then derives class-based text prompts. H2SA then ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| OV-SCAN outperforms OV-3DET [25] and ImOV3D [42] in the overall metric, achieving comparable results to ImOV3D [42] in the car category while surpassing both ... | comparison identity and matched condition | p. 7 (4.2. Main Results) |
| To assess the impact of the H2SA head, we introduce a one-step baseline in Tab. | comparison identity and matched condition | p. 8 (4.3. Ablation Studies) |
| 3 shows that our method consistently outperforms the greedy search even with fewer iterations per novel object. | comparison identity and matched condition | p. 8 (4.3. Ablation Studies) |
| Figure 1. Cross-modal Alignment Performance. The red CDF shows the distance distribution between 3D embeddings from a baseline OV-3D detector and 2D CLIP embeddings ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Ablations on Adaptive 3D Box Search. | comparison identity and matched condition | p. 7 (4.1. Experimental Setup) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This variant removes the classification loss term, merges TransFusion-L's class heatmaps into a single class-agnostic heatmap, and replaces the text-guided alignment network with a ... | component/input/data sensitivity | p. 8 (4.3. Ablation Studies) |
| Ablations on Adaptive 3D Box Search. | component/input/data sensitivity | p. 7 (4.1. Experimental Setup) |
| Without being given 3D human-annotations, OV-SCAN achieves an AP score above 60 for both car and pedestrian categories. | component/input/data sensitivity | p. 7 (4.2. Main Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We summarize our main contributions as follows: • We present OV-SCAN, an OV-3D object detector benefiting from improved cross-modal alignment, see Fig. | A simple occlusion filter with a fixed threshold ςocc yields a notable performance gain, while class-based thresholds achieve the highest improvement (+1.7 mAP). | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.3. Ablation Studies), p. 7 (4.2. Main Results), p. 7 (4.2. Main Results), p. 1 (Figure/Table caption), p. 8 (4.3. Ablation Studies), p. 2 (Figure/Table caption) |
| Primary metric/result | Without being given 3D human-annotations, OV-SCAN achieves an AP score above 60 for both car and pedestrian categories. | numeric claim only at cited anchor | p. 7 (4.2. Main Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** OV-SCAN is trained on 8 NVIDIA V100 GPUs with a batch size of four for 20 epochs.
- **p. 5 / 3.2. Semantically Consistent NOD (SC-NOD) - extractive PDF cue:** Specifically, the proportion of pixels occupied by the object within the 2D crop is thresholded by ςocc: %Wcrop x=1 %Hcrop y=1 m(x, y) HcropWcrop ↑ςocc.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The primary limitation of SC-NOD is its limited annotation recovery (Fig. | p. 8 (4.4. Limitations) |
| body limitation/failure cue | These insights motivate future work exploring alternative methods less dependent on 2D proposals and anchor-free box-parameterization strategies. | p. 8 (4.4. Limitations) |
| body limitation/failure cue | Figure 2. 3D Annotation Errors. Common 3D annotation errors during box parametrization, including but not limited to, poor L- shape fitting, misinterpreted surfaces, and ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Figure 3. Sources of Semantic Discrepancies. (a) CLIP sim- ilarity scores for a truck reveal that occlusion cases result in an ambiguous 2D image ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | The remainder of generated annotations are excluded as a result of filtering due to significant occlusion (39%) or insufficient resolution (7%). | p. 7 (4.2. Main Results) |
| body limitation/failure cue | (a) 3D Box Search Cost Weights (b) Resolution Filter (ω1, ω2, ω3, ε) mAP Filter mAP (5.0, 0.0, 0.0, 3.0) 26.1 w/o 30.4 (1.0, ... | p. 7 (4.1. Experimental Setup) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| OV-SCAN is trained on 8 NVIDIA V100 GPUs with a batch size of four for 20 epochs. | p. 6 (4.1. Experimental Setup) |
| OV-SCAN-Fusion is trained for five additional epochs using a cosine annealing schedule initialized at a learning rate of 0.0001. | p. 7 (4.1. Experimental Setup) |
| (a) 3D Box Search Cost Weights (b) Resolution Filter (ω1, ω2, ω3, ε) mAP Filter mAP (5.0, 0.0, 0.0, 3.0) 26.1 w/o 30.4 (1.0, ... | p. 7 (4.1. Experimental Setup) |
| For more details on the implementation, please refer to Sec. | p. 6 (4.1. Experimental Setup) |
| Cross-Modal Target Preparation 2D Image Features 3D Annotations CLIP Image Encoder Adaptive 3D Box Search Predicted Objects Selective Alignment Filter CLIP Image Encoder Adaptive ... | p. 4 (3.1. Notation and Preliminaries) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.4. Limitations - extractive PDF cue:** The primary limitation of SC-NOD is its limited annotation recovery (Fig.
- **p. 8 / 4.4. Limitations - extractive PDF cue:** These insights motivate future work exploring alternative methods less dependent on 2D proposals and anchor-free box-parameterization strategies.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. 3D Annotation Errors. Common 3D annotation errors during box parametrization, including but not limited to, poor L- shape fitting, misinterpreted surfaces, and misaligned ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 3. Sources of Semantic Discrepancies. (a) CLIP sim- ilarity scores for a truck reveal that occlusion cases result in an ambiguous 2D image feature. ...
- **p. 7 / 4.2. Main Results - extractive PDF cue:** The remainder of generated annotations are excluded as a result of filtering due to significant occlusion (39%) or insufficient resolution (7%).
- **p. 7 / 4.1. Experimental Setup - extractive PDF cue:** (a) 3D Box Search Cost Weights (b) Resolution Filter (ω1, ω2, ω3, ε) mAP Filter mAP (5.0, 0.0, 0.0, 3.0) 26.1 w/o 30.4 (1.0, 1.0, ...

- **PDF anchors reviewed:** datasets p. 6 (4.1. Experimental Setup), p. 7 (4.2. Main Results), p. 7 (4.2. Main Results), p. 8 (4.3. Ablation Studies), p. 8 (4.2. Main Results), p. 6 (4.1. Experimental Setup), metrics p. 2 (Figure/Table caption), p. 7 (4.1. Experimental Setup), p. 7 (4.2. Main Results), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), p. 2 (Figure/Table caption), baselines p. 7 (4.2. Main Results), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), p. 1 (Figure/Table caption), p. 7 (4.1. Experimental Setup), results p. 8 (4.3. Ablation Studies), p. 7 (4.2. Main Results), p. 7 (4.2. Main Results), p. 1 (Figure/Table caption), p. 8 (4.3. Ablation Studies), p. 2 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
