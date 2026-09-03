# Evaluation - Point2Graph: An End-To-End Point Cloud-Based 3D Open-Vocabulary Scene Graph for Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2409.10350v1. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS)): In our experimental results, shown in TABLE I, by generating a border-enhanced density map before input to RoomFormer, our approach achieved 12% improvements in AP50 and 3% in mIoU.

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive body cue:** Evaluation for Object Detection and Classication We conducted our experiments on the widely-used ScanNetv2 [45] indoor point cloud dataset, which consists of 312 validation scenes, ...
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive body cue:** 2) Room Classication Evaluation: For room classi- cation, we evaluate our "Snap-Lookup" pipeline on 100 segmented room scenes from the MP3D dataset [35].
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive body cue:** The robot should interpret the human's query and search for the room and object location in the pre-built 3D scene graph hierarchically and navigate to ...
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive body cue:** Since our environment has more than one classroom and our 3D scene graph does not consider further identication for rooms with the same type, it ...
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive body cue:** The "F1" score takes their harmonic mean of Precision and Recall. "mAP" measures the average accuracy of classication across all categories Method B/N AP50 AP25 ...
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive body cue:** Evaluation metrics include Precision, Recall, weighted F1 score, and mean Average Precision (mAP).
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive body cue:** Methods Precision Recall F1 mAP Privileged GPT-3.5-turbo w\ GT object 0.69 0.61 0.61 0.63 GPT-4o w\ GT object 0.68 0.63 0.61 0.63 Unprivileged GPT-3.5-turbo w\ ...
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive body cue:** As baselines, we use two methods: the zero-shot LLM-based room type inference method [29] and the room classication approach from HOV-SG [8], Methods AP50 mIoU ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** IV. EXPERIMENTAL RESULTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTAL RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | In our experimental results, shown in TABLE I, by generating a border-enhanced density map before input to RoomFormer, our approach achieved 12% improvements in ... | p. 5 (IV. EXPERIMENTAL RESULTS) |
| IV. EXPERIMENTAL RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Specically, our method achieves the highest AP50 and | p. 5 (IV. EXPERIMENTAL RESULTS) |
| IV. EXPERIMENTAL RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | This integrated approach effectively captures both global and local contexts, leading to improved precision and generalization across various IoU thresholds. | p. 6 (IV. EXPERIMENTAL RESULTS) |
| IV. EXPERIMENTAL RESULTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The "F1" score takes their harmonic mean of Precision and Recall. "mAP" measures the average accuracy of classication across all categories Method B/N AP50 ... | p. 6 (IV. EXPERIMENTAL RESULTS) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive body cue:** Evaluation for Object Detection and Classication We conducted our experiments on the widely-used ScanNetv2 [45] indoor point cloud dataset, which consists of 312 validation scenes, ...
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive body cue:** 2) Room Classication Evaluation: For room classi- cation, we evaluate our "Snap-Lookup" pipeline on 100 segmented room scenes from the MP3D dataset [35].
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive body cue:** The robot should interpret the human's query and search for the room and object location in the pre-built 3D scene graph hierarchically and navigate to ...
- **p. 6 / IV. EXPERIMENTAL RESULTS - extractive body cue:** Since our environment has more than one classroom and our 3D scene graph does not consider further identication for rooms with the same type, it ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Comparison of our proposed Point2Graph algorithm and the existing 3D scene graph generation algorithm. Compared with existing methods [8], [9], our proposed Point2Graph ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: The overall pipeline of Point2Graph: The system is divided into two levels: the room level and the object level. At the room level, ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: Generation of border-enhanced density map: The process begins by segmenting the point cloud into N layers, each of which is projected into a ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: "Snap" and "Lookup" module in room open-vocabulary classication: (a) In "Snap" module, cameras are positioned evenly at the ellipse shape trajectory facing to ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 5. 1) Object-Level Detection: The room point cloud data is sampled from the segmented room-level geometry informa- tion of the scene. To identify object ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 5: Overview of the 3D open-vocabulary detection pipeline: It consists of two stages: (1) detection and localization using class-agnostic bounding boxes and DBSCAN ltering ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6: Generation of the Voronoi navigation graph: By deducting the projected binary free space map with the eroded map, we can obtain the boundary ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 7: Qualitative result of room segmentation: Room segmentation produced by RoomFormer [28], HOV-SG [8] and our proposed methods on MP3D dataset [35]. Each color ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Evaluation for Object Detection and Classication We conducted our experiments on the widely-used ScanNetv2 [45] indoor point cloud dataset, which consists of 312 validation ... | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS) |
| Task/environment | 2) Room Classication Evaluation: For room classi- cation, we evaluate our "Snap-Lookup" pipeline on 100 segmented room scenes from the MP3D dataset [35]. | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (III. METHODOLOGY), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The "F1" score takes their harmonic mean of Precision and Recall. "mAP" measures the average accuracy of classication across all categories Method B/N AP50 ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTAL RESULTS) |
| Evaluation metrics include Precision, Recall, weighted F1 score, and mean Average Precision (mAP). | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTAL RESULTS) |
| Methods Precision Recall F1 mAP Privileged GPT-3.5-turbo w\ GT object 0.69 0.61 0.61 0.63 GPT-4o w\ GT object 0.68 0.63 0.61 0.63 Unprivileged GPT-3.5-turbo ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTAL RESULTS) |
| As baselines, we use two methods: the zero-shot LLM-based room type inference method [29] and the room classication approach from HOV-SG [8], Methods AP50 ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTAL RESULTS) |
| Fig. 2: The overall pipeline of Point2Graph: The system is divided into two levels: the room level and the object level. At the room ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 1: Comparison of our proposed Point2Graph algorithm and the existing 3D scene graph generation algorithm. Compared with existing methods [8], [9], our proposed ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 3: Generation of border-enhanced density map: The process begins by segmenting the point cloud into N layers, each of which is projected into ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 5. 1) Object-Level Detection: The room point cloud data is sampled from the segmented room-level geometry informa- tion of the scene. To identify ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compared our method to RoomFormer [28], the current SOTA in learning-based algorithms, and the room segmentation techniques employed in HOV-SG [8], the SOTA ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTAL RESULTS) |
| As baselines, we use two methods: the zero-shot LLM-based room type inference method [29] and the room classication approach from HOV-SG [8], Methods AP50 ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTAL RESULTS) |
| Fig. 1: Comparison of our proposed Point2Graph algorithm and the existing 3D scene graph generation algorithm. Compared with existing methods [8], [9], our proposed ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Results are compared on base/novel (B/N) category splits, with an indication of whether methods use RGB-D images ("use RGB-D") "Sofa" "Somewhere to study" Fig. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTAL RESULTS) |
| 0.08 × OpenIns3D [12] -/7 0.28 0.43 × Ours -/7 0.38 0.44 × Mask3D-P-CLIP [44] -/17 0.04 0.14 × OpenIns3D [12] -/17 0.29 0.39 ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENTAL RESULTS) |
| Fig. 5: Overview of the 3D open-vocabulary detection pipeline: It consists of two stages: (1) detection and localization using class-agnostic bounding boxes and DBSCAN ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 5: Overview of the 3D open-vocabulary detection pipeline: It consists of two stages: (1) detection and localization using class-agnostic bounding boxes and DBSCAN ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Generally speaking, our framework consists of a room segmentation and classication module and an object detection and classication module. | In our experimental results, shown in TABLE I, by generating a border-enhanced density map before input to RoomFormer, our approach achieved 12% improvements in ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS) |
| Primary metric/result | Specically, our method achieves the highest AP50 and | numeric claim only at cited anchor | p. 5 (IV. EXPERIMENTAL RESULTS) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive body cue:** Evaluation for Room Segmentation and Classication 1) Room Segmentation Evaluation: We conducted our experiment on the MP3D dataset [35], where all multi-oor scenes were segmented ...
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive body cue:** Excluding those used for ne-tuning the region detector, we selected 43 scenes to serve as the test set for room segmentation.
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive body cue:** Evaluation for Object Detection and Classication We conducted our experiments on the widely-used ScanNetv2 [45] indoor point cloud dataset, which consists of 312 validation scenes, ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** Building on the original training provided by the paper on 3,000 scenes from Structure3D [34], we further ne-tuned the model with 100 scenes from Matterport3D ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Nevertheless, Point2Graph has its limitations. | p. 6 (V. CONCLUSION) |
| body limitation/failure cue | In conclusion, this work presents the Point2Graph framework, which addresses the limitations of current openvocabulary 3D scene graph generation methods by eliminating the need ... | p. 6 (V. CONCLUSION) |
| body limitation/failure cue | Our proposed "Snap-Lookup" pipeline, which incorporates room visual features into type inference, can differentiate between various types of rooms that contain the same objects-something ... | p. 5 (IV. EXPERIMENTAL RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To obtain open-vocabulary features for each room, inspired by the approach in [8], we use the CLIP visual encoder to extract embeddings from the ... | p. 4 (III. METHODOLOGY) |
| Object-Level Detection and Classication After getting the segmentation result for each room, our approach mainly consists of two steps, where the rst step deals ... | p. 4 (III. METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / V. CONCLUSION - extractive body cue:** Nevertheless, Point2Graph has its limitations.
- **p. 6 / V. CONCLUSION - extractive body cue:** In conclusion, this work presents the Point2Graph framework, which addresses the limitations of current openvocabulary 3D scene graph generation methods by eliminating the need for ...
- **p. 5 / IV. EXPERIMENTAL RESULTS - extractive body cue:** Our proposed "Snap-Lookup" pipeline, which incorporates room visual features into type inference, can differentiate between various types of rooms that contain the same objects-something text-only ...

- **Evidence anchors reviewed:** datasets p. 5 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS), metrics p. 6 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 3 (Figure/Table caption), p. 1 (Figure/Table caption), baselines p. 5 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 1 (Figure/Table caption), p. 6 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS), p. 4 (Figure/Table caption), results p. 5 (IV. EXPERIMENTAL RESULTS), p. 5 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS), p. 6 (IV. EXPERIMENTAL RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
