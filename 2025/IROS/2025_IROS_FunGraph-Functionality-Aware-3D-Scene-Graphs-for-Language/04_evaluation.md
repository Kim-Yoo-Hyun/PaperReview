# Evaluation - FunGraph: Functionality Aware 3D Scene Graphs for Language-Prompted Scene Interaction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2503.07909; PDF retrieval source: https://arxiv.org/pdf/2503.07909. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS)): Given that the measured performance on the different splits of the same datasets are in a similar range, we carefully conclude that our proposed method achieves similar results to SOTA ...

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The train-validation split of the dataset is 80/20, with the split ensuring that train and validation images come from different scenes.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** To this end, we randomly select 10 scenes from the validation dataset: 423070, 423306, 423738, 434892, 435357, 435715, 435724, 442392, 464754, 467330, and associate the ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Given that the measured performance on the different splits of the same datasets are in a similar range, we carefully conclude that our proposed method ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** For each method, the percentage of success (IoU at least 25% and > 0%) is shown for the scenes in our validation sample.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Next, we fine-tune YOLOv11 [44] and RT-DETR [45] on the standard dataset.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Instead, it returns whole object point clouds, which results in low IoU with the ground truth.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Another source of error is not directly related to the method: indeed, the poses P provided in the dataset [5] are not always accurate, generating ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Note that our approach has to cope with inaccurate poses whereas [5] directly segments on the point cloud not affected by these errors.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Given that the measured performance on the different splits of the same datasets are in a similar range, we carefully conclude that our proposed ... | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results, however, show that the return of ConceptGraphs is still less accurate, indicating that the inclusion of functional elements and object-part relations in ... | p. 7 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | To achieve this, we convert our 3D scene graph representation into a JSON format, retaining information about each node's ID, 3D center of mass, ... | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | In the following, we conduct experiments to investigate the accuracy of our trained 2D models and compare them to existing zero-shot detectors. | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Therefore, we first compare the 2D detection performance of our trained models and, in the following section, place this into context with existing 3D ... | p. 5 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The train-validation split of the dataset is 80/20, with the split ensuring that train and validation images come from different scenes.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** To this end, we randomly select 10 scenes from the validation dataset: 423070, 423306, 423738, 434892, 435357, 435715, 435724, 442392, 464754, 467330, and associate the ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Given that the measured performance on the different splits of the same datasets are in a similar range, we carefully conclude that our proposed method ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** For each method, the percentage of success (IoU at least 25% and > 0%) is shown for the scenes in our validation sample.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Next, we fine-tune YOLOv11 [44] and RT-DETR [45] on the standard dataset.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Instead, it returns whole object point clouds, which results in low IoU with the ground truth.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. An example of a generated 3D scene graph and its application. The model represents both object and functional element nodes linked through intra-object ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Implementation of our approach on a mobile manipulator using RGB-D sensing (3D LiDAR not used). The yellow edges in the left picture show ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Overview of our functionality-aware 3D scene graph generation pipeline, which consists of three stages: (1) Detection, where instance segmentation and feature extraction are ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4. Illustration of our context-based label refinement. The VLM is queried to contextualize functional elements with their associated parent objects. The handle on the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The train-validation split of the dataset is 80/20, with the split ensuring that train and validation images come from different scenes. | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Task/environment | To this end, we randomly select 10 scenes from the validation dataset: 423070, 423306, 423738, 434892, 435357, 435715, 435724, 442392, 464754, 467330, and associate ... | reset, timeout, object/scene variation | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 2 (III. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Another source of error is not directly related to the method: indeed, the poses P provided in the dataset [5] are not always accurate, ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Note that our approach has to cope with inaccurate poses whereas [5] directly segments on the point cloud not affected by these errors. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Instead, it returns whole object point clouds, which results in low IoU with the ground truth. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| For each method, the percentage of success (IoU at least 25% and > 0%) is shown for the scenes in our validation sample. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTS) |
| In the following, we conduct experiments to investigate the accuracy of our trained 2D models and compare them to existing zero-shot detectors. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Therefore, we first compare the 2D detection performance of our trained models and, in the following section, place this into context with existing 3D ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Fig. 1. An example of a generated 3D scene graph and its application. The model represents both object and functional element nodes linked through ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As a baseline, we run YOLO-Worldv8.2 [40] and Grounding Dino [41] in a zero-shot fashion. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| We compared this approach to prompting GPT-4o with only the functional element's bounding box annotation (approach "GPT-No-Context") and using CLIP features to classify it ... | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |
| We further validate the scene graph generation and 3D lifting against the current SOTA 3D detectors for functional elements segmentation. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| In Table IV, we report per-scene results and compare them to the SOTA ConceptGraphs [3] that can answer unconstrained language queries on the map. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Note that we retain all functional element detections, even without object associations, to avoid penalizing scores when parent objects are undetected. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Label Refinement Ablation Study As described in Section III-B, the first detection of functional elements only associates them with their affordance label. | comparison identity and matched condition | p. 7 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Further, we compare these models on a variant dataset, which we compute using the slicing-aided hyper inference (SAHI) mechanism [46], and refer to it ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Note that we retain all functional element detections, even without object associations, to avoid penalizing scores when parent objects are undetected. | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| To further emphasize the correlation between 2D detection quality and 3D segmentation performance, we conducted an ablation study to relate the metrics from the ... | component/input/data sensitivity | p. 6 (IV. EXPERIMENTS) |
| Label Refinement Ablation Study As described in Section III-B, the first detection of functional elements only associates them with their affordance label. | component/input/data sensitivity | p. 7 (IV. EXPERIMENTS) |
| Next, we fine-tune YOLOv11 [44] and RT-DETR [45] on the standard dataset. | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Fig. 1. An example of a generated 3D scene graph and its application. The model represents both object and functional element nodes linked through ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| 3 provides an overview of our method. | Given that the measured performance on the different splits of the same datasets are in a similar range, we carefully conclude that our proposed ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Primary metric/result | The results, however, show that the return of ConceptGraphs is still less accurate, indicating that the inclusion of functional elements and object-part relations in ... | numeric claim only at cited anchor | p. 7 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** This splits the images into 640×640 patches, which we then use for training and detection.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** To this end, we randomly select 10 scenes from the validation dataset: 423070, 423306, 423738, 434892, 435357, 435715, 435724, 442392, 464754, 467330, and associate the ...
- **p. 5 / III. METHOD - extractive body cue:** All computations are performed on a machine with an NVIDIA 4090 GPU, 64GB RAM + 64GB SWAP, and an AMD Ryzen 9 7950X Processor.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | It does not rely on segmenting a pre-existing highquality point cloud, which makes it also suitable for robotics applications with affordable RGB-D sensing. | p. 7 (VI. CONCLUSIONS) |
| body limitation/failure cue | Fig. 4. Illustration of our context-based label refinement. The VLM is queried to contextualize functional elements with their associated parent objects. The handle on ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | As is evident from the numbers, ConceptGraphs does not account for the | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | We note that the exact numerical results are difficult to compare, as [5] does not release either the model checkpoints or the full train/test ... | p. 6 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| As a baseline, we run YOLO-Worldv8.2 [40] and Grounding Dino [41] in a zero-shot fashion. | p. 5 (IV. EXPERIMENTS) |
| Further, we compare these models on a variant dataset, which we compute using the slicing-aided hyper inference (SAHI) mechanism [46], and refer to it ... | p. 5 (IV. EXPERIMENTS) |
| We then compute the AP metrics as defined in [5]. | p. 6 (IV. EXPERIMENTS) |
| We note that the exact numerical results are difficult to compare, as [5] does not release either the model checkpoints or the full train/test ... | p. 6 (IV. EXPERIMENTS) |
| Implementation of our approach on a mobile manipulator using RGB-D sensing (3D LiDAR not used). | p. 3 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / VI. CONCLUSIONS - extractive body cue:** It does not rely on segmenting a pre-existing highquality point cloud, which makes it also suitable for robotics applications with affordable RGB-D sensing.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4. Illustration of our context-based label refinement. The VLM is queried to contextualize functional elements with their associated parent objects. The handle on the ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** As is evident from the numbers, ConceptGraphs does not account for the
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We note that the exact numerical results are difficult to compare, as [5] does not release either the model checkpoints or the full train/test split.

- **Evidence anchors reviewed:** datasets p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), metrics p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), baselines p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), results p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
