# Evaluation - BEVDepth: Acquisition of Reliable Depth for Multi-view 3D Object Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2206.10092; PDF retrieval source: https://arxiv.org/pdf/2206.10092. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5 Experiment), p. 6 (5 Experiment), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 3 (Figure/Table caption)): In the end, Depth Refinement Module improves 0.8% mAP.

## Evaluation Body Digest

- **p. 6 / 5 Experiment - extractive PDF cue:** There are 1000 scenarios in the dataset, which are divided into 700, 150, and 150 scenes for training, validation, and testing, respectively.
- **p. 6 / 5 Experiment - extractive PDF cue:** 5.1 Experimental Setup Dataset and Metrics nuScenes (Caesar et al.
- **p. 6 / 5 Experiment - extractive PDF cue:** For 3D detection task, we report nuScenes Detection Score (NDS), mean Average Precision (mAP), as well as five True Positive (TP) metrics including mean Average ...
- **p. 6 / 5 Experiment - extractive PDF cue:** In this part, we ablate the effect of using these two different losses in DepthNet (see Table 5), and find that different depth losses barely ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Testing detectors' robustness to image sizes. We use 256 × 704 for training. mAP on nuScenes are reported. best-predicted pixel for each object. ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4: Framework of BEVDepth. Image backbone extracts image feature from multi-view images. Depth net takes Image feature as input, generates context and depth, and ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 8: Comparison on the nuScenes test set. L denotes LiDAR and C denotes camera. BEVDepth uses pretrained VovNet as backbone. the resolution of the ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Depth estimation results in Lift-splat detector and BEVDepth. Dashed boxes highlight the regions that Lift-splat detector makes "relatively" accurate depth predictions in, usually ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5 Experiment (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | In the end, Depth Refinement Module improves 0.8% mAP. | p. 6 (5 Experiment) |
| 5 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | 5.2 Ablation Study Component Analysis As shown in Table 4, our vanilla BEVDepth achieves 28.2% mAP and 32.7% NDS. | p. 6 (5 Experiment) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 2: Testing detectors' robustness to image sizes. We use 256 × 704 for training. mAP on nuScenes are reported. best-predicted pixel for each ... | p. 4 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 8: Comparison on the nuScenes test set. L denotes LiDAR and C denotes camera. BEVDepth uses pretrained VovNet as backbone. the resolution of ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1: Depth estimation results in Lift-splat detector and BEVDepth. Dashed boxes highlight the regions that Lift-splat detector makes "relatively" accurate depth predictions in, ... | p. 2 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 5 Experiment - extractive PDF cue:** There are 1000 scenarios in the dataset, which are divided into 700, 150, and 150 scenes for training, validation, and testing, respectively.
- **p. 6 / 5 Experiment - extractive PDF cue:** 5.1 Experimental Setup Dataset and Metrics nuScenes (Caesar et al.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Depth estimation results in Lift-splat detector and BEVDepth. Dashed boxes highlight the regions that Lift-splat detector makes "relatively" accurate depth predictions in, usually ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 1: Evaluation of depth prediction on the nuScenes val set. "soft" and "hard" denote gaussian and one-hot random- ization along depth dimension, respectively. odepth2 ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 2: Evaluation of depth prediction on the nuScenes val set. DL denotes Depth Loss. All foreground points are taken for evaluation. 3.2 Making Lift-splat ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Testing detectors' robustness to image sizes. We use 256 × 704 for training. mAP on nuScenes are reported. best-predicted pixel for each object. ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3: Compared to the Base Detector (left), the En- hanced Detector (right) retains more structure information during feature unprojection and thus can provide precise ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 3: Classification on the nuScenes val set. We use the classification heatmap for evaluation, th denotes the thresh- old of heatmap. Enhanced Detector performs ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4: Framework of BEVDepth. Image backbone extracts image feature from multi-view images. Depth net takes Image feature as input, generates context and depth, and ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 4: Ablation study of Depth Loss, Camera-awareness and Depth Refinement Module on the nuScenes val set. DL, CA, DR and MF denotes Depth Loss, ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | There are 1000 scenarios in the dataset, which are divided into 700, 150, and 150 scenes for training, validation, and testing, respectively. | embodiment, simulator version and control stack | p. 6 (5 Experiment), p. 6 (5 Experiment) |
| Task/environment | 5.1 Experimental Setup Dataset and Metrics nuScenes (Caesar et al. | reset, timeout, object/scene variation | p. 6 (5 Experiment) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 1 (Abstract) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (Abstract), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For 3D detection task, we report nuScenes Detection Score (NDS), mean Average Precision (mAP), as well as five True Positive (TP) metrics including mean ... | definition/direction/unit from same section | p. 6 (5 Experiment) |
| In this part, we ablate the effect of using these two different losses in DepthNet (see Table 5), and find that different depth losses ... | definition/direction/unit from same section | p. 6 (5 Experiment) |
| Figure 2: Testing detectors' robustness to image sizes. We use 256 × 704 for training. mAP on nuScenes are reported. best-predicted pixel for each ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 4: Framework of BEVDepth. Image backbone extracts image feature from multi-view images. Depth net takes Image feature as input, generates context and depth, ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 8: Comparison on the nuScenes test set. L denotes LiDAR and C denotes camera. BEVDepth uses pretrained VovNet as backbone. the resolution of ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 1: Depth estimation results in Lift-splat detector and BEVDepth. Dashed boxes highlight the regions that Lift-splat detector makes "relatively" accurate depth predictions in, ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Table 2: Evaluation of depth prediction on the nuScenes val set. DL denotes Depth Loss. All foreground points are taken for evaluation. 3.2 Making ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Overall, our BEVDepth improves 4.0% mAP and 4.0% NDS compared to its baseline, showing the effectiveness of our innovations. | comparison identity and matched condition | p. 6 (5 Experiment) |
| When compared to other methods, BEVDepth is trained for 20 epochs with CBGS. | comparison identity and matched condition | p. 6 (5 Experiment) |
| Figure 3: Compared to the Base Detector (left), the En- hanced Detector (right) retains more structure information during feature unprojection and thus can provide ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |
| Table 3: Classification on the nuScenes val set. We use the classification heatmap for evaluation, th denotes the thresh- old of heatmap. Enhanced Detector ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |
| Table 8: Comparison on the nuScenes test set. L denotes LiDAR and C denotes camera. BEVDepth uses pretrained VovNet as backbone. the resolution of ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For the ablation study, all experiments are trained for 24 epochs without using CBGS strategy (Zhu et al. | component/input/data sensitivity | p. 6 (5 Experiment) |
| 5.2 Ablation Study Component Analysis As shown in Table 4, our vanilla BEVDepth achieves 28.2% mAP and 32.7% NDS. | component/input/data sensitivity | p. 6 (5 Experiment) |
| Table 8: Comparison on the nuScenes test set. L denotes LiDAR and C denotes camera. BEVDepth uses pretrained VovNet as backbone. the resolution of ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Therefore, in this work, we introduce BEVDepth, a new multi-view 3D detector that leverages depth supervision derives from point clouds to guide depth learning. | In the end, Depth Refinement Module improves 0.8% mAP. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5 Experiment), p. 6 (5 Experiment), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 3 (Figure/Table caption) |
| Primary metric/result | 5.2 Ablation Study Component Analysis As shown in Table 4, our vanilla BEVDepth achieves 28.2% mAP and 32.7% NDS. | numeric claim only at cited anchor | p. 6 (5 Experiment) |

- Numeric sentences retained from the body:
- **p. 6 / 5 Experiment - extractive PDF cue:** There are 1000 scenarios in the dataset, which are divided into 700, 150, and 150 scenes for training, validation, and testing, respectively.
- **p. 6 / 5 Experiment - extractive PDF cue:** 2016) as the image backbone and the image size is processed to 256×704.
- **p. 6 / 5 Experiment - extractive PDF cue:** For the ablation study, all experiments are trained for 24 epochs without using CBGS strategy (Zhu et al.
- **p. 6 / 5 Experiment - extractive PDF cue:** When compared to other methods, BEVDepth is trained for 20 epochs with CBGS.
- **p. 6 / 5 Experiment - extractive PDF cue:** CD × W mAP↑ mATE↓ mAOE↓ NDS↑ - 0.314 0.706 0.647 0.357 1×3 0.315 0.703 0.650 0.357 3×1 0.320 0.695 0.624 0.369 3×3 0.322 0.707 ...
- **p. 6 / 5 Experiment - extractive PDF cue:** Method Resolution mAP↑ NDS↑ FCOS3D 900×1600 0.295 0.372 DETR3D 900×1600 0.303 0.374 BEVDet-R50 256×704 0.286 0.372 BEVDet-Tiny 512×1408 0.349 0.417 PETR-R50-DCN 384×1056 0.313 0.381 PETR-R101-DCN ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | If the 2.5D projection of a certain point cloud does not fall into the ith view, we simply discard it. | p. 5 (2 Related Work) |
| body limitation/failure cue | Benefiting from the decoupled nature of LSS (Philion and Fidler 2020), the camera-aware depth prediction module is isolated from the detection head and thus ... | p. 5 (2 Related Work) |
| body limitation/failure cue | See Table 6, when we use 1×3 conv on CD ×W dimension, the information does not exchange along the depth axis, and | p. 6 (5 Experiment) |
| body limitation/failure cue | Such a phenomenon implies that the model without depth loss has a higher risk of over-fitting, and thus it may also be sensitive to ... | p. 4 (2 Related Work) |
| body limitation/failure cue | Figure 2: Testing detectors' robustness to image sizes. We use 256 × 704 for training. mAP on nuScenes are reported. best-predicted pixel for each ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use AdamW (Loshchilov and Hutter 2017) as an optimizer with a learning rate set to 2e-4 and batch size set to 64. | p. 6 (5 Experiment) |
| When compared to other methods, BEVDepth is trained for 20 epochs with CBGS. | p. 6 (5 Experiment) |
| Meanwhile, we innovatively propose to encode camera intrinsics and extrinsics into a depth learning module so that the detector is robust to various camera ... | p. 1 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 2 Related Work - extractive PDF cue:** If the 2.5D projection of a certain point cloud does not fall into the ith view, we simply discard it.
- **p. 5 / 2 Related Work - extractive PDF cue:** Benefiting from the decoupled nature of LSS (Philion and Fidler 2020), the camera-aware depth prediction module is isolated from the detection head and thus the ...
- **p. 6 / 5 Experiment - extractive PDF cue:** See Table 6, when we use 1×3 conv on CD ×W dimension, the information does not exchange along the depth axis, and
- **p. 4 / 2 Related Work - extractive PDF cue:** Such a phenomenon implies that the model without depth loss has a higher risk of over-fitting, and thus it may also be sensitive to the ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Testing detectors' robustness to image sizes. We use 256 × 704 for training. mAP on nuScenes are reported. best-predicted pixel for each object. ...

- **PDF anchors reviewed:** datasets p. 6 (5 Experiment), p. 6 (5 Experiment), metrics p. 6 (5 Experiment), p. 6 (5 Experiment), p. 4 (Figure/Table caption), p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), baselines p. 6 (5 Experiment), p. 6 (5 Experiment), p. 4 (Figure/Table caption), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), results p. 6 (5 Experiment), p. 6 (5 Experiment), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), p. 2 (Figure/Table caption), p. 3 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
