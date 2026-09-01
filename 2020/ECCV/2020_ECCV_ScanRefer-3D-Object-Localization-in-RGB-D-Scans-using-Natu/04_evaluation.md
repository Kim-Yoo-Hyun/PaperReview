# Evaluation - ScanRefer: 3D Object Localization in RGB-D Scans using Natural Language

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (35 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1912.08830; PDF retrieval source: https://arxiv.org/pdf/1912.08830. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 14 (6 Experiments), p. 14 (6 Experiments), p. 11 (Figure/Table caption), p. 13 (6 Experiments), p. 13 (6 Experiments), p. 10 (6 Experiments)): The additional 3D information improves performance.

## Evaluation Body Digest

- **p. 5 / 4 Dataset - extractive PDF cue:** 4: Description lengths Number of descriptions 51,583 Number of scenes 800 Number of objects 11,046 Number of objects per scene 13.81 Number of descriptions per ...
- **p. 9 / 6 Experiments - extractive PDF cue:** Following the official ScanNet [9] split, we split our data into train/val/test sets with 36,665, 9,508 and 5,410 samples respectively, ensuring disjoint scenes for each ...
- **p. 6 / 4 Dataset - extractive PDF cue:** 4.2 Dataset Statistics We collected 51,583 descriptions for 800 ScanNet scenes2.
- **p. 4 / 3 dataset - extractive PDF cue:** 3 Task We introduce the task of object localization in 3D scenes using natural language (Fig.
- **p. 4 / 3 dataset - extractive PDF cue:** [2] introduces a new dataset and task that focuses on disambiguating objects from the same category with known localizations.
- **p. 11 / 6 Experiments - extractive PDF cue:** 6.2 Quantitative Analysis We evaluate the performance of our model against baselines on the val and the hidden test split of ScanRefer which serves as ...
- **p. 9 / 6 Experiments - extractive PDF cue:** The test set is hidden and will be reserved for the ScanRefer benchmark.
- **p. 3 / 3 dataset - extractive PDF cue:** Recent work on 3D object detection on volumetric grids [20, 19, 32, 42, 13] has been applied to several 3D RGB-D datasets [58, 9, 4].

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3 dataset (p. 3); 4 Dataset (p. 4); 6 Experiments (p. 9); A Dataset (p. 21); B Additional Implementation Details (p. 25); C.1 Object Detection Results (p. 29); C.2 Training and Evaluation Variance (p. 29).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 6 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | The additional 3D information improves performance. | p. 14 (6 Experiments) |
| 6 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our architecture trained with geometry, multi-view features, and normals (xyz+multiview+ normals+lobjcls) achieves the best performance among all ablations. | p. 14 (6 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 4: Comparison of localization results obtained by our ScanRefer and base- line models. We measure percentage of predictions whose IoU with the ground ... | p. 11 (Figure/Table caption) |
| 6 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | The failure case of OracleRefer suggests that our fusion & localization module can still be improved. | p. 13 (6 Experiments) |
| 6 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | However, the gap between the VoteNetRand and OracleCatRand for the "unique" case shows that 3D object detection still need to be improved. | p. 13 (6 Experiments) |

## Dataset / Benchmark Role

- **p. 5 / 4 Dataset - extractive PDF cue:** 4: Description lengths Number of descriptions 51,583 Number of scenes 800 Number of objects 11,046 Number of objects per scene 13.81 Number of descriptions per ...
- **p. 9 / 6 Experiments - extractive PDF cue:** Following the official ScanNet [9] split, we split our data into train/val/test sets with 36,665, 9,508 and 5,410 samples respectively, ensuring disjoint scenes for each ...
- **p. 6 / 4 Dataset - extractive PDF cue:** 4.2 Dataset Statistics We collected 51,583 descriptions for 800 ScanNet scenes2.
- **p. 4 / 3 dataset - extractive PDF cue:** 3 Task We introduce the task of object localization in 3D scenes using natural language (Fig.
- **p. 4 / 3 dataset - extractive PDF cue:** [2] introduces a new dataset and task that focuses on disambiguating objects from the same category with known localizations.
- **p. 11 / 6 Experiments - extractive PDF cue:** 6.2 Quantitative Analysis We evaluate the performance of our model against baselines on the val and the hidden test split of ScanRefer which serves as ...
- **p. 9 / 6 Experiments - extractive PDF cue:** The test set is hidden and will be reserved for the ScanRefer benchmark.
- **p. 3 / 3 dataset - extractive PDF cue:** Recent work on 3D object detection on volumetric grids [20, 19, 32, 42, 13] has been applied to several 3D RGB-D datasets [58, 9, 4].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: We introduce the task of object localization in 3D scenes using natural language. Given as input a 3D scene and a natural language ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison of referring expression datasets in terms of the number of objects (#objects), number of expressions (#expressions), average lengths of the expressions, data ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 2: Our task: ScanRefer takes as input a 3D scene point cloud and a descrip- tion of an object in the scene, and predicts ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 3: Our data collection pipeline. The annotator writes a description for the focused object in the scene. Then, a verifier selects the objects that ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 4: Description lengths Number of descriptions 51,583 Number of scenes 800 Number of objects 11,046 Number of objects per scene
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 2: ScanRefer dataset statistics. (a) (b) (c) (d) (e)
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 5: Word clouds of terms for (a) object names (b) colors (c) shapes (d) sizes, and (e) spatial relations for the ScanRefer dataset. Bigger ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3: Examples from our dataset illustrating different types of phrases such as attributes (1-8) and parts (5), comparatives (4), superlatives (5), intra-class spatial relations ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4: Description lengths Number of descriptions 51,583 Number of scenes 800 Number of objects 11,046 Number of objects per scene 13.81 Number of descriptions ... | embodiment, simulator version and control stack | p. 5 (4 Dataset), p. 9 (6 Experiments) |
| Task/environment | Following the official ScanNet [9] split, we split our data into train/val/test sets with 36,665, 9,508 and 5,410 samples respectively, ensuring disjoint scenes for ... | reset, timeout, object/scene variation | p. 9 (6 Experiments), p. 6 (4 Dataset) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 6 (5 Method), p. 7 (5 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 7 (5 Method), p. 8 (5 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| To evaluate the performance of our method, we measure the thresholded accuracy where the positive predictions have higher intersection over union (IoU) with the ... | definition/direction/unit from same section | p. 10 (6 Experiments) |
| Fig. 8: Qualitative results from baseline methods and ScanRefer. Predicted boxes are marked green if they have an IoU score higher than 0.5, otherwise ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| We then select the 2D bounding box with the highest confidence score from the bounding box candidates and project it to 3D using the ... | definition/direction/unit from same section | p. 10 (6 Experiments) |
| Table 8: Object detection results measured using mean average precision (mAP) at IOU of 0.5 for the 18 difference classes for [a] VoteNet [49], ... | definition/direction/unit from same section | p. 28 (Figure/Table caption) |
| Table 4: Comparison of localization results obtained by our ScanRefer and base- line models. We measure percentage of predictions whose IoU with the ground ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| Fig. 6: ScanRefer architecture: The PointNet++ [51] backbone takes as input a point cloud and aggregates it to high-level point feature maps, which are ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| However, as the accuracy gap between VoteNetBest and ours (end-to-end) indicates, there is still room for improving | definition/direction/unit from same section | p. 12 (6 Experiments) |
| Table 11: Ablation study with different input lengths. We measure the percent- ages of predictions whose IoU with the ground truth boxes are greater ... | definition/direction/unit from same section | p. 31 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We outperform all baselines by a significant margin. | comparison identity and matched condition | p. 11 (6 Experiments) |
| From the OracleCatRand baseline, we see that information from the description, other than the object category, is necessary to disambiguate between multiple objects (see ... | comparison identity and matched condition | p. 11 (6 Experiments) |
| Fig. 8: Qualitative results from baseline methods and ScanRefer. Predicted boxes are marked green if they have an IoU score higher than 0.5, otherwise ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |
| For the val split, we also include additional experiments on the 2D baselines and a comparison with VoteNetRand. | comparison identity and matched condition | p. 13 (6 Experiments) |
| Architectures with a language to object classifier outperform ones without it. | comparison identity and matched condition | p. 14 (6 Experiments) |
| SCRC & One-stage: 2D image baselines for referring expression comprehension by extending SCRC [23] and One-stage [68] to 3D using back-projection. | comparison identity and matched condition | p. 10 (6 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To show the effectiveness of the extra supervision on input descriptions, we conduct an experiment with the language to object classifier (+lobjcls) and without. | component/input/data sensitivity | p. 14 (6 Experiments) |
| 6.4 Ablation Studies We conduct an ablation study on our model to examine what components and point cloud features contribute to the performance (see ... | component/input/data sensitivity | p. 13 (6 Experiments) |
| Architectures with a language to object classifier outperform ones without it. | component/input/data sensitivity | p. 14 (6 Experiments) |
| Table 5: Ablation study with different features. We measure the percentages of predictions whose IoU with the ground truth boxes are greater than 0.25 ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| As expected, models with the language-based object classifier (rows [g-k]) does not results in better object detection compared to models without such a module ... | component/input/data sensitivity | p. 28 (B.1 Fusion Module) |
| Table 10: Variance between evaluation runs due to the random sampling of points in the VoteNet [49]. We train our model (xyz+multiview+normal+lobjcls) with the ... | component/input/data sensitivity | p. 30 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our architecture consists of two main modules: 1) detection & encoding; 2) fusion & localization (Fig. | The additional 3D information improves performance. | PDF body cue; verify exact table/figure and matched conditions | p. 14 (6 Experiments), p. 14 (6 Experiments), p. 11 (Figure/Table caption), p. 13 (6 Experiments), p. 13 (6 Experiments), p. 10 (6 Experiments) |
| Primary metric/result | Our architecture trained with geometry, multi-view features, and normals (xyz+multiview+ normals+lobjcls) achieves the best performance among all ablations. | numeric claim only at cited anchor | p. 14 (6 Experiments) |

- Numeric sentences retained from the body:
- **p. 4 / 3 dataset - extractive PDF cue:** 3 Task We introduce the task of object localization in 3D scenes using natural language (Fig.
- **p. 6 / 4 Dataset - extractive PDF cue:** On average, there are 13.81 objects, 64.48 descriptions per scene, and 4.67 descriptions per object after filtering (see Tab.
- **p. 9 / 6 Experiments - extractive PDF cue:** Following the official ScanNet [9] split, we split our data into train/val/test sets with 36,665, 9,508 and 5,410 samples respectively, ensuring disjoint scenes for each ...
- **p. 11 / 6 Experiments - extractive PDF cue:** 6.1 Task Difficulty To understand how informative the input description is beyond capturing the object category, we analyze the performance of the methods on "unique" ...
- **p. 6 / 5 Method - extractive PDF cue:** The detection & encoding module encodes the input point cloud and description, and outputs the object proposals and the language embedding, which are fed into ...
- **p. 9 / 5 Method - extractive PDF cue:** For point clouds, we apply rotation about all three axes by a random angle in [-5°, 5°] and randomly translate the point cloud within 0.5 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In contrast, even provided with a pool of ground truth proposals, OracleRefer sometimes still fails to predict correct bounding boxes, while One-stage is limited ... | p. 13 (6 Experiments) |
| body limitation/failure cue | We show examples where our method produced good predictions (blue block) as well as failure cases (orange block). | p. 12 (6 Experiments) |
| body limitation/failure cue | Some failure cases of our method are displayed in the orange block in Fig. | p. 13 (6 Experiments) |
| body limitation/failure cue | Fig. 17: Additional qualitative analysis in the "unique" scenarios where there is only one object from a certain category. Our method is capable of ... | p. 33 (Figure/Table caption) |
| body limitation/failure cue | Fig. 18: Additional qualitative analysis for the "multiple" subset where there are multiple objects with the same category as the target objects. While our ... | p. 34 (Figure/Table caption) |
| body limitation/failure cue | Fig. 1: We introduce the task of object localization in 3D scenes using natural language. Given as input a 3D scene and a natural ... | p. 1 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| At inference time, we sample frames from the scans (using every 20th frame) and predict the target 2D bounding boxes in each frame. | p. 10 (6 Experiments) |
| Implementation Details We implement our architecture using PyTorch and train the model end-to-end using ADAM [29] with a learning rate of 1e-3. | p. 9 (5 Method) |
| Image best viewed in color. we take the average of 5 differently seeded subsamplings (of seed points and vote points) during inference (see supplemental ... | p. 12 (6 Experiments) |
| The detection & encoding module encodes the input point cloud and description, and outputs the object proposals and the language embedding, which are fed ... | p. 6 (5 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 13 / 6 Experiments - extractive PDF cue:** In contrast, even provided with a pool of ground truth proposals, OracleRefer sometimes still fails to predict correct bounding boxes, while One-stage is limited by ...
- **p. 12 / 6 Experiments - extractive PDF cue:** We show examples where our method produced good predictions (blue block) as well as failure cases (orange block).
- **p. 13 / 6 Experiments - extractive PDF cue:** Some failure cases of our method are displayed in the orange block in Fig.
- **p. 33 / Figure/Table caption - extractive PDF cue:** Fig. 17: Additional qualitative analysis in the "unique" scenarios where there is only one object from a certain category. Our method is capable of localizing ...
- **p. 34 / Figure/Table caption - extractive PDF cue:** Fig. 18: Additional qualitative analysis for the "multiple" subset where there are multiple objects with the same category as the target objects. While our methods ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: We introduce the task of object localization in 3D scenes using natural language. Given as input a 3D scene and a natural language ...

- **PDF anchors reviewed:** datasets p. 5 (4 Dataset), p. 9 (6 Experiments), p. 6 (4 Dataset), p. 4 (3 dataset), p. 4 (3 dataset), p. 11 (6 Experiments), metrics p. 10 (6 Experiments), p. 12 (Figure/Table caption), p. 10 (6 Experiments), p. 28 (Figure/Table caption), p. 11 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 11 (6 Experiments), p. 11 (6 Experiments), p. 12 (Figure/Table caption), p. 13 (6 Experiments), p. 14 (6 Experiments), p. 10 (6 Experiments), results p. 14 (6 Experiments), p. 14 (6 Experiments), p. 11 (Figure/Table caption), p. 13 (6 Experiments), p. 13 (6 Experiments), p. 10 (6 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
