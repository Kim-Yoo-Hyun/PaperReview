# Evaluation - FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2402.04555; PDF retrieval source: https://arxiv.org/pdf/2402.04555. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (V. EXPERIMENT), p. 5 (V. EXPERIMENT), p. 8 (Figure/Table caption)): Even for those predictable semantic classes, the pretrained Mask R-CNN suffers from the issue of generalization and achieve low AP50 scores.

## Evaluation Body Digest

- **p. 5 / V. EXPERIMENT - extractive body cue:** We chose the public dataset ScanNet and SceneNN to evaluate the semantic mapping quality.
- **p. 5 / V. EXPERIMENT - extractive body cue:** In all the experiments, camera poses are provided by the dataset.
- **p. 6 / V. EXPERIMENT - extractive body cue:** IEEE ROBOTICS AND AUTOMATION LETTERS, VOL.9, NO.3, MARCH 2024
- **p. 5 / V. EXPERIMENT - extractive body cue:** Even for those predictable semantic classes, the pretrained Mask R-CNN suffers from the issue of generalization and achieve low AP50 scores.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6: The visualization shows instance voxel grid map (a) before and (b) after the merge. The inconsistent instance mask is a natural limitation for ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Our system reads a sequence of RGB-D frames. The vision-language foundation models detect objects in open-set labels and high-quality masks. The SLAM modules ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 8: The reconstructed instance map using RAM-Grounded-SAM in ScanNet scene0011, scene0435 and scene0633 (from top to bottom). The falsely predicted semantic classes in (a) ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: GroundingDINO detects a bookshelf and generates multiple open-set label measurements across frames. Our label fusion module predicts its semantic class in NYUv2 label-set ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** V. EXPERIMENT (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENT | EMPIRICAL / SOURCE-REPORTED EVALUATION | Even for those predictable semantic classes, the pretrained Mask R-CNN suffers from the issue of generalization and achieve low AP50 scores. | p. 5 (V. EXPERIMENT) |
| V. EXPERIMENT | EMPIRICAL / SOURCE-REPORTED EVALUATION | In experiment with fine-tune Mask R-CNN, although the mean AP is improved, they still reconstruct a few of semantic classes with 0 AP. | p. 5 (V. EXPERIMENT) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 11: Reconstructions in SceneNN 096. False semantic and over-segmented instances are highlighted in red circles. So far, the system run offline. As shown ... | p. 8 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / V. EXPERIMENT - extractive body cue:** We chose the public dataset ScanNet and SceneNN to evaluate the semantic mapping quality.
- **p. 5 / V. EXPERIMENT - extractive body cue:** In all the experiments, camera poses are provided by the dataset.
- **p. 6 / V. EXPERIMENT - extractive body cue:** IEEE ROBOTICS AND AUTOMATION LETTERS, VOL.9, NO.3, MARCH 2024

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Our system reads a sequence of RGB-D frames. The vision-language foundation models detect objects in open-set labels and high-quality masks. The SLAM modules ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: System overview of FM-Fusion
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: GroundingDINO detects a bookshelf and generates multiple open-set label measurements across frames. Our label fusion module predicts its semantic class in NYUv2 label-set ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: The label likelihood matrix p(yi = om, ∃om ∈qt/Ls = cn) summarized in ScanNet is shown on the left. Each column represents a ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 5: An example of an inconsistent instance mask generated from SAM. In each of the three frames, different areas of the bed are segmented.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6: The visualization shows instance voxel grid map (a) before and (b) after the merge. The inconsistent instance mask is a natural limitation for ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 7: Illustration of the instance-geometry fusion. Geometric points are extracted from the global map. The instance-wise voxel grid map can contain voxel outliers due ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 8: The reconstructed instance map using RAM-Grounded-SAM in ScanNet scene0011, scene0435 and scene0633 (from top to bottom). The falsely predicted semantic classes in (a) ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We chose the public dataset ScanNet and SceneNN to evaluate the semantic mapping quality. | embodiment, simulator version and control stack | p. 5 (V. EXPERIMENT), p. 5 (V. EXPERIMENT) |
| Task/environment | In all the experiments, camera poses are provided by the dataset. | reset, timeout, object/scene variation | p. 5 (V. EXPERIMENT), p. 6 (V. EXPERIMENT) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 6 (6 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Even for those predictable semantic classes, the pretrained Mask R-CNN suffers from the issue of generalization and achieve low AP50 scores. | definition/direction/unit from same section | p. 5 (V. EXPERIMENT) |
| Fig. 6: The visualization shows instance voxel grid map (a) before and (b) after the merge. The inconsistent instance mask is a natural limitation ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 1: Our system reads a sequence of RGB-D frames. The vision-language foundation models detect objects in open-set labels and high-quality masks. The SLAM ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 8: The reconstructed instance map using RAM-Grounded-SAM in ScanNet scene0011, scene0435 and scene0633 (from top to bottom). The falsely predicted semantic classes in ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Fig. 3: GroundingDINO detects a bookshelf and generates multiple open-set label measurements across frames. Our label fusion module predicts its semantic class in NYUv2 ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 5: An example of an inconsistent instance mask generated from SAM. In each of the three frames, different areas of the bed are ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 10: An image of object detection from Ablation-B and our method are shown in (a) and (b). The labels incorporated by text prompt ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 11: Reconstructions in SceneNN 096. False semantic and over-segmented instances are highlighted in red circles. So far, the system run offline. As shown ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compared our method with Kimera 2 and a selfimplemented Fusion++. | comparison identity and matched condition | p. 5 (V. EXPERIMENT) |
| The global TSDF map is integrated for every RGBD frame, while our method and all baselines run in every 10 frames to integrate the ... | comparison identity and matched condition | p. 5 (V. EXPERIMENT) |
| Fig. 10: An image of object detection from Ablation-B and our method are shown in (a) and (b). The labels incorporated by text prompt ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 10: An image of object detection from Ablation-B and our method are shown in (a) and (b). The labels incorporated by text prompt ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Fig. 11: Reconstructions in SceneNN 096. False semantic and over-segmented instances are highlighted in red circles. So far, the system run offline. As shown ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We evaluated a pre-trained Mask R-CNN and a fine-tuned Mask R-CNN. | component/input/data sensitivity | p. 5 (V. EXPERIMENT) |
| The pre-trained one is trained in COCO instance segmentation dataset, while we also fine-tuned it using ScanNet dataset. | component/input/data sensitivity | p. 5 (V. EXPERIMENT) |
| Fig. 8: The reconstructed instance map using RAM-Grounded-SAM in ScanNet scene0011, scene0435 and scene0633 (from top to bottom). The falsely predicted semantic classes in ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method incrementally fuses the object detections from foundation models into an instance-aware semantic map. | Even for those predictable semantic classes, the pretrained Mask R-CNN suffers from the issue of generalization and achieve low AP50 scores. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (V. EXPERIMENT), p. 5 (V. EXPERIMENT), p. 8 (Figure/Table caption) |
| Primary metric/result | In experiment with fine-tune Mask R-CNN, although the mean AP is improved, they still reconstruct a few of semantic classes with 0 AP. | numeric claim only at cited anchor | p. 5 (V. EXPERIMENT) |

- Numeric sentences retained from the body:
- **p. 5 / V. EXPERIMENT - extractive body cue:** The global TSDF map is integrated for every RGBD frame, while our method and all baselines run in every 10 frames to integrate the detected ...
- **p. 5 / V. EXPERIMENT - extractive body cue:** In all the experiments, the RGB-D images are in 640 × 480 dimension and the voxel length is set to be 1.5 cm.
- **p. 5 / V. EXPERIMENT - extractive body cue:** The experiment is run on an Intel-i7 computer with Nvidia RTX-3090 GPU in an offline fashion.
- **p. 7 / 6 Method - extractive body cue:** On the other hand, as illustrated in section III-B, our method maintains a series of labels U t that has been detected in previous 5 ...
- **p. 7 / 6 Method - extractive body cue:** Efficiency Base Scaling Foundation RAM 28.5 ms - Models GroundingDINO 120.7 ms - SAM 464.4 ms - FM-Fusion Projection 307ms 63.4 ms/obj Data Assoc.
- **p. 7 / 6 Method - extractive body cue:** 47.1ms 9.7 ms/obj Integration 71.9ms 14.9 ms/obj Total 1039.6 ms - TABLE IV: Runtime analysis for each frame in ScanNet.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | As shown in Figure 10(a), RAM fails to recognize a table due to the extreme viewpoint, and GroundingDINO cannot detect it either. | p. 7 (6 Method) |
| body limitation/failure cue | Fig. 6: The visualization shows instance voxel grid map (a) before and (b) after the merge. The inconsistent instance mask is a natural limitation ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | We consider those limitations of foundation models. | p. 7 (6 Method) |
| body limitation/failure cue | Compared with the original Fusion++ method, the main difference is that our implemented version does not maintain a foreground probability for each voxel. | p. 5 (V. EXPERIMENT) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The experiment is run on an Intel-i7 computer with Nvidia RTX-3090 GPU in an offline fashion. | p. 5 (V. EXPERIMENT) |
| But we use Cluster-All for convenient implementation. | p. 5 (V. EXPERIMENT) |
| 47.1ms 9.7 ms/obj Integration 71.9ms 14.9 ms/obj Total 1039.6 ms - TABLE IV: Runtime analysis for each frame in ScanNet. | p. 7 (6 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 6 Method - extractive body cue:** As shown in Figure 10(a), RAM fails to recognize a table due to the extreme viewpoint, and GroundingDINO cannot detect it either.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6: The visualization shows instance voxel grid map (a) before and (b) after the merge. The inconsistent instance mask is a natural limitation for ...
- **p. 7 / 6 Method - extractive body cue:** We consider those limitations of foundation models.
- **p. 5 / V. EXPERIMENT - extractive body cue:** Compared with the original Fusion++ method, the main difference is that our implemented version does not maintain a foreground probability for each voxel.

- **Evidence anchors reviewed:** datasets p. 5 (V. EXPERIMENT), p. 5 (V. EXPERIMENT), p. 6 (V. EXPERIMENT), metrics p. 5 (V. EXPERIMENT), p. 5 (Figure/Table caption), p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), p. 3 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 5 (V. EXPERIMENT), p. 5 (V. EXPERIMENT), p. 7 (Figure/Table caption), results p. 5 (V. EXPERIMENT), p. 5 (V. EXPERIMENT), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
