# Evaluation - Detecting Twenty-thousand Classes using Image-level Supervision

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2201.02605; PDF retrieval source: https://arxiv.org/pdf/2201.02605. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 13 (Figure/Table caption), p. 26 (Figure/Table caption), p. 7 (5 Experiments), p. 11 (Figure/Table caption), p. 3 (Figure/Table caption), p. 9 (Figure/Table caption)): Table 5: Detic with different classifiers. We vary the classifier used with Detic and observe that it works well with different choices. While CLIP embeddings give the best performance (* ...

## Evaluation Body Digest

- **p. 7 / 5 Experiments - extractive PDF cue:** We evaluate Detic on the large-vocabulary object detection dataset LVIS [18].
- **p. 7 / 5 Experiments - extractive PDF cue:** The LVIS [18] dataset has object detection and instance segmentation labels for 1203 classes with 100K images.
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: Left: Standard detection requires ground-truth labeled boxes and cannot lever- age image-level labels. Center: Existing prediction-based weakly supervised detection methods [3, 44, 45] ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3: Approach Overview. We mix train on detection data and image-labeled data. When using detection data, our model uses the standard detection losses to ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 3: Open-vocabulary COCO [2]. We compare Detic using the same training data and architecture from OVR-CNN [72]. We report box mAP at IoU threshold ...
- **p. 7 / 5 Experiments - extractive PDF cue:** We use Federated Loss [76] and repeat factor sampling [18].
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 4: Visualization of the assigned boxes during training. We show all boxes with score > 0.5 in blue and the assigned (selected) box in ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Fig. 5: Qualitative results of our 21k-class detector. We show random samples from images containing novel classes in OpenImages (top) and Objects365 (bottom) validation sets. ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 5 Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 5: Detic with different classifiers. We vary the classifier used with Detic and observe that it works well with different choices. While CLIP ... | p. 13 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 15: Detic applied to Deformable-DETR [79]. We report Box mAP on full LVIS. Our method improves Deformable-DETR. outperforms MosaicOS [73] in mAP and ... | p. 26 (Figure/Table caption) |
| 5 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We first establish a strong baseline on LVIS to demonstrate that our improvements are orthogonal to recent advances in object detection. | p. 7 (5 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 3: Open-vocabulary COCO [2]. We compare Detic using the same training data and architecture from OVR-CNN [72]. We report box mAP at IoU ... | p. 11 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 2: Left: Standard detection requires ground-truth labeled boxes and cannot lever- age image-level labels. Center: Existing prediction-based weakly supervised detection methods [3, 44, ... | p. 3 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 5 Experiments - extractive PDF cue:** We evaluate Detic on the large-vocabulary object detection dataset LVIS [18].
- **p. 7 / 5 Experiments - extractive PDF cue:** The LVIS [18] dataset has object detection and instance segmentation labels for 1203 classes with 100K images.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: Top: Typical detection results from a strong open-vocabulary LVIS detector. The detector misses objects of "common" classes. Bottom: Number of images in LVIS, ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: Left: Standard detection requires ground-truth labeled boxes and cannot lever- age image-level labels. Center: Existing prediction-based weakly supervised detection methods [3, 44, 45] ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3: Approach Overview. We mix train on detection data and image-labeled data. When using detection data, our model uses the standard detection losses to ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 1: Prediction-based vs non-prediction-based methods. We show overall and novel-class mAP on open-vocabulary LVIS [17] (with 866 base classes and 337 novel classes) with ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 4: Visualization of the assigned boxes during training. We show all boxes with score > 0.5 in blue and the assigned (selected) box in ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 2: Open-vocabulary LVIS compared to ViLD [17]. We train our model using their training settings and architecture (MaskRCNN-ResNet50, training from scratch). We report mask ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 3: Open-vocabulary COCO [2]. We compare Detic using the same training data and architecture from OVR-CNN [72]. We report box mAP at IoU threshold ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 4: Detecting 21K classes across datasets. We use Detic to train a detector and evaluate it on multiple datasets without retraining. We report the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate Detic on the large-vocabulary object detection dataset LVIS [18]. | embodiment, simulator version and control stack | p. 7 (5 Experiments), p. 7 (5 Experiments) |
| Task/environment | The LVIS [18] dataset has object detection and instance segmentation labels for 1203 classes with 100K images. | reset, timeout, object/scene variation | p. 7 (5 Experiments) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 2 (X. Zhou et al), p. 5 (3 Preliminaries) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (3 Preliminaries), p. 5 (3 Preliminaries) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 2: Left: Standard detection requires ground-truth labeled boxes and cannot lever- age image-level labels. Center: Existing prediction-based weakly supervised detection methods [3, 44, ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 3: Approach Overview. We mix train on detection data and image-labeled data. When using detection data, our model uses the standard detection losses ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 3: Open-vocabulary COCO [2]. We compare Detic using the same training data and architecture from OVR-CNN [72]. We report box mAP at IoU ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| We use Federated Loss [76] and repeat factor sampling [18]. | definition/direction/unit from same section | p. 7 (5 Experiments) |
| Fig. 4: Visualization of the assigned boxes during training. We show all boxes with score > 0.5 in blue and the assigned (selected) box ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Fig. 5: Qualitative results of our 21k-class detector. We show random samples from images containing novel classes in OpenImages (top) and Objects365 (bottom) validation ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| We report mask mAP which is the official metric for LVIS. | definition/direction/unit from same section | p. 7 (5 Experiments) |
| Table 1: Prediction-based vs non-prediction-based methods. We show overall and novel-class mAP on open-vocabulary LVIS [17] (with 866 base classes and 337 novel classes) ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 11: Ablations of the resolution change. We report mask mAP on the open- vocabulary LVIS following the setting of Table 1. Top: ImageNet ... | comparison identity and matched condition | p. 22 (Figure/Table caption) |
| Table 3: Open-vocabulary COCO [2]. We compare Detic using the same training data and architecture from OVR-CNN [72]. We report box mAP at IoU ... | comparison identity and matched condition | p. 11 (Figure/Table caption) |
| Fig. 2: Left: Standard detection requires ground-truth labeled boxes and cannot lever- age image-level labels. Center: Existing prediction-based weakly supervised detection methods [3, 44, ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| Table 1: Prediction-based vs non-prediction-based methods. We show overall and novel-class mAP on open-vocabulary LVIS [17] (with 866 base classes and 337 novel classes) ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Table 4: Detecting 21K classes across datasets. We use Detic to train a detector and evaluate it on multiple datasets without retraining. We report ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |
| Table 15: Detic applied to Deformable-DETR [79]. We report Box mAP on full LVIS. Our method improves Deformable-DETR. outperforms MosaicOS [73] in mAP and ... | comparison identity and matched condition | p. 26 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Following ViLD [17], we remove the labels of 337 rare-class from training and consider them as novel classes in testing. | component/input/data sensitivity | p. 7 (5 Experiments) |
| Notation Definition #Images #Classes LVIS-all The original LVIS dataset [18] 100K 1203 LVIS-base LVIS without rare-class annotations 100K 866 IN-21K The original ImageNet-21K dataset ... | component/input/data sensitivity | p. 7 (5 Experiments) |
| Table 12: Comparison between predicted loss and and max-size loss. (a): comparison under different baselines. (b): comparison in customized metrics. G ViLD baseline details ... | component/input/data sensitivity | p. 24 (Figure/Table caption) |
| Table 10: LVIS baseline evolution. First row: the configuration from the detectron2 model zoo. The following rows change components one by one. Last row: ... | component/input/data sensitivity | p. 21 (Figure/Table caption) |
| Table 1: Prediction-based vs non-prediction-based methods. We show overall and novel-class mAP on open-vocabulary LVIS [17] (with 866 base classes and 337 novel classes) ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Table 2: Open-vocabulary LVIS compared to ViLD [17]. We train our model using their training settings and architecture (MaskRCNN-ResNet50, training from scratch). We report ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This also enables our method to learn detectors for new classes which would have been impossible to predict and assign. | Table 5: Detic with different classifiers. We vary the classifier used with Detic and observe that it works well with different choices. While CLIP ... | PDF body cue; verify exact table/figure and matched conditions | p. 13 (Figure/Table caption), p. 26 (Figure/Table caption), p. 7 (5 Experiments), p. 11 (Figure/Table caption), p. 3 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Primary metric/result | Table 15: Detic applied to Deformable-DETR [79]. We report Box mAP on full LVIS. Our method improves Deformable-DETR. outperforms MosaicOS [73] in mAP and ... | numeric claim only at cited anchor | p. 26 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / 5 Experiments - extractive PDF cue:** We use large scale jittering [15] with input resolution 640×640 and train for a 4× (∼48 LVIS epochs) schedule.
- **p. 2 / X. Zhou et al - extractive PDF cue:** With imagelevel supervision from ImageNet-21K [10], our model trained without novel class detection annotations improves the baseline by 8.3 point and matches the performance of ...
- **p. 3 / X. Zhou et al - extractive PDF cue:** We show that this loss is both simpler and performs better than prior work. outperforms the previous state-of-the-art OVR-CNN [72] by 5 point with the ...
- **p. 5 / 3 Preliminaries - extractive PDF cue:** In our experiments, the proposal network and the bounding box regressors are not the current performance bottleneck, as modern detectors use an over-sufficient number of ...
- **p. 8 / X. Zhou et al - extractive PDF cue:** In our implementation, we use 320×320 for ImageNet and CC and ablate this in Appendix D.
- **p. 8 / X. Zhou et al - extractive PDF cue:** Training our ResNet50 model takes ∼22 hours on 8 V100 GPUs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 2: Left: Standard detection requires ground-truth labeled boxes and cannot lever- age image-level labels. Center: Existing prediction-based weakly supervised detection methods [3, 44, ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | By default, a trained classifier cannot recognize novel classes. | p. 13 (X. Zhou et al) |
| body limitation/failure cue | 6 Limitations and Conclusions We present Detic which is a simple way to use image supervision in largevocabulary object detection. | p. 14 (X. Zhou et al) |
| body limitation/failure cue | We leave incorporating such information for future work. | p. 14 (X. Zhou et al) |
| body limitation/failure cue | Compared to the Box-Supervised baseline (trained on LVIS-all), Detic leverages image-level supervision to train robust detectors. | p. 12 (X. Zhou et al) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use large scale jittering [15] with input resolution 640×640 and train for a 4× (∼48 LVIS epochs) schedule. | p. 7 (5 Experiments) |
| Notation Definition #Images #Classes LVIS-all The original LVIS dataset [18] 100K 1203 LVIS-base LVIS without rare-class annotations 100K 866 IN-21K The original ImageNet-21K dataset ... | p. 7 (5 Experiments) |
| Our method completely side-steps the prediction-based label assignment process by supervising the classification sub-problem alone when using classification data. | p. 2 (X. Zhou et al) |
| Our contributions are summarized below: - We identify issues and propose a simpler alternative to existing weaklysupervised detection techniques in the open-vocabulary setting. - ... | p. 3 (X. Zhou et al) |
| Thus, we only compute the localization losses (RPN loss and bounding box regression loss) on images with ground truth box labels. | p. 5 (3 Preliminaries) |
| Our method side-steps this prediction-and-assignment process entirely and relies on a fixed supervision criteria. | p. 6 (X. Zhou et al) |
| See Appendix E for implementation details. | p. 8 (X. Zhou et al) |
| In our implementation, we use 320×320 for ImageNet and CC and ablate this in Appendix D. | p. 8 (X. Zhou et al) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2: Left: Standard detection requires ground-truth labeled boxes and cannot lever- age image-level labels. Center: Existing prediction-based weakly supervised detection methods [3, 44, 45] ...
- **p. 13 / X. Zhou et al - extractive PDF cue:** By default, a trained classifier cannot recognize novel classes.
- **p. 14 / X. Zhou et al - extractive PDF cue:** 6 Limitations and Conclusions We present Detic which is a simple way to use image supervision in largevocabulary object detection.
- **p. 14 / X. Zhou et al - extractive PDF cue:** We leave incorporating such information for future work.
- **p. 12 / X. Zhou et al - extractive PDF cue:** Compared to the Box-Supervised baseline (trained on LVIS-all), Detic leverages image-level supervision to train robust detectors.

- **PDF anchors reviewed:** datasets p. 7 (5 Experiments), p. 7 (5 Experiments), metrics p. 3 (Figure/Table caption), p. 5 (Figure/Table caption), p. 11 (Figure/Table caption), p. 7 (5 Experiments), p. 10 (Figure/Table caption), p. 12 (Figure/Table caption), baselines p. 22 (Figure/Table caption), p. 11 (Figure/Table caption), p. 3 (Figure/Table caption), p. 9 (Figure/Table caption), p. 12 (Figure/Table caption), p. 26 (Figure/Table caption), results p. 13 (Figure/Table caption), p. 26 (Figure/Table caption), p. 7 (5 Experiments), p. 11 (Figure/Table caption), p. 3 (Figure/Table caption), p. 9 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
