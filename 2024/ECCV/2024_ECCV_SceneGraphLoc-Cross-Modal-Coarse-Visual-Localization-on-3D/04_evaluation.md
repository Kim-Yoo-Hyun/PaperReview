# Evaluation - SceneGraphLoc: Cross-Modal Coarse Visual Localization on 3D Scene Graphs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1255_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01255.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 12 (4 Experiments), p. 13 (4 Experiments), p. 12 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments)): SceneGraphLoc, even when excluding the image modality (I), outperforms other cross-modal strategies significantly.

## Evaluation Body Digest

- **p. 11 / 4 Experiments - extractive body cue:** The 3RScan dataset [123] comprises 1335 annotated indoor scenes, representing 432 distinct rooms, with 1178 scenes (385 rooms) allocated for training and 157 (47 rooms) ...
- **p. 12 / 4 Experiments - extractive body cue:** To evaluate the generalization ability of our methods in real-world applications when scene graph annotations are not available, we conduct further experiments in the ScanNet ...
- **p. 13 / 4 Experiments - extractive body cue:** SceneGraphLoc 13 Table 3: Average time (ms) of obtaining the query image embedding (teq) and of the retrieval from 10, 50, and all scenes from ...
- **p. 11 / 4 Experiments - extractive body cue:** SceneGraphLoc 11 Table 1: Retrieval recall on the test set of 3RScan dataset [123] (%; target scene ranked within the top 1, 3, and 5 ...
- **p. 12 / 4 Experiments - extractive body cue:** The inferiority is because both methods learn shared embedding between entire scenes and query images of totally different objects due to viewpoint differences.
- **p. 13 / 4 Experiments - extractive body cue:** We partly attribute this performance gap to the lack of object attributes in the dataset and the inaccurate instance segmentation predicted by [130].
- **p. 10 / 4 Experiments - extractive body cue:** Both methods were fine-tuned on our dataset for accurate comparison.
- **p. 10 / 4 Experiments - extractive body cue:** No existing methods directly tackle our task, but several recent advancements provide relevant baselines.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4 Experiments (p. 10).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | SceneGraphLoc, even when excluding the image modality (I), outperforms other cross-modal strategies significantly. | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | LidarCLIP shows a small improvement in accuracy. | p. 13 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Incorporating images significantly enhances its performance, positioning it close to that of image-based approaches but with three orders of magnitude smaller storage requirements. | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | These methods offer advanced performance but demand significant storage for image descriptors and exhibit slower inference times. | p. 10 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | To evaluate the accuracy of a method, we focus on the recall of scene selection. | p. 11 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 11 / 4 Experiments - extractive body cue:** The 3RScan dataset [123] comprises 1335 annotated indoor scenes, representing 432 distinct rooms, with 1178 scenes (385 rooms) allocated for training and 157 (47 rooms) ...
- **p. 12 / 4 Experiments - extractive body cue:** To evaluate the generalization ability of our methods in real-world applications when scene graph annotations are not available, we conduct further experiments in the ScanNet ...
- **p. 13 / 4 Experiments - extractive body cue:** SceneGraphLoc 13 Table 3: Average time (ms) of obtaining the query image embedding (teq) and of the retrieval from 10, 50, and all scenes from ...
- **p. 11 / 4 Experiments - extractive body cue:** SceneGraphLoc 11 Table 1: Retrieval recall on the test set of 3RScan dataset [123] (%; target scene ranked within the top 1, 3, and 5 ...
- **p. 12 / 4 Experiments - extractive body cue:** The inferiority is because both methods learn shared embedding between entire scenes and query images of totally different objects due to viewpoint differences.
- **p. 13 / 4 Experiments - extractive body cue:** We partly attribute this performance gap to the lack of object attributes in the dataset and the inaccurate instance segmentation predicted by [130].
- **p. 10 / 4 Experiments - extractive body cue:** Both methods were fine-tuned on our dataset for accurate comparison.
- **p. 10 / 4 Experiments - extractive body cue:** No existing methods directly tackle our task, but several recent advancements provide relevant baselines.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: SceneGraphLoc addresses the novel problem of localizing a query image in a database of 3D scenes represented as compact multi-modal 3D scene graphs. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Overview. The training phase is represented by orange arrows, while blue arrows denote the inference phase. During training, a query image and its ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: The embedding of im- age modality I for each object. The image crops of a pillow are shown as an example. This section ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 4: The same scene at different time steps t. We use contrastive learning to learn a joint embedding space for the scene graph nodes ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 5: Qualitative Result of object-association-based scene retrieval from the 3RScan dataset [123]. The two left images show the ground truth (left) and predicted (right) ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 1: Retrieval recall on the test set of 3RScan dataset [123] (%; target scene ranked within the top 1, 3, and 5 of the ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 2: Retrieval recall in the temporal scenario on the test set of ScanNet dataset [21] (%; target scene ranked within the top 1, 3, ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 3: Average time (ms) of obtaining the query image embedding (teq) and of the retrieval from 10, 50, and all scenes from the 3RScan ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The 3RScan dataset [123] comprises 1335 annotated indoor scenes, representing 432 distinct rooms, with 1178 scenes (385 rooms) allocated for training and 157 (47 ... | embodiment, simulator version and control stack | p. 11 (4 Experiments), p. 12 (4 Experiments) |
| Task/environment | To evaluate the generalization ability of our methods in real-world applications when scene graph annotations are not available, we conduct further experiments in the ... | reset, timeout, object/scene variation | p. 12 (4 Experiments), p. 13 (4 Experiments) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered)) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 3 (1 Introduction), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| To evaluate the accuracy of a method, we focus on the recall of scene selection. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| Although LidarCLIP exhibits marginally better accuracy, it remains inferior to alternative methods. | definition/direction/unit from same section | p. 12 (4 Experiments) |
| LidarCLIP shows a small improvement in accuracy. | definition/direction/unit from same section | p. 13 (4 Experiments) |
| OpenMask3D attains an accuracy comparable to our proposed method without incorporating the image modality. | definition/direction/unit from same section | p. 13 (4 Experiments) |
| SceneGraphLoc 11 Table 1: Retrieval recall on the test set of 3RScan dataset [123] (%; target scene ranked within the top 1, 3, and ... | definition/direction/unit from same section | p. 11 (4 Experiments) |
| Both methods were fine-tuned on our dataset for accurate comparison. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| These methods offer advanced performance but demand significant storage for image descriptors and exhibit slower inference times. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| SceneGraphLoc, even when excluding the image modality (I), outperforms other cross-modal strategies significantly. | definition/direction/unit from same section | p. 12 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For comparison with state-of-the-art visual localization methods requiring large image databases, we included CVNet [63] and AnyLoc [55]. | comparison identity and matched condition | p. 10 (4 Experiments) |
| No existing methods directly tackle our task, but several recent advancements provide relevant baselines. | comparison identity and matched condition | p. 10 (4 Experiments) |
| SceneGraphLoc, even when excluding the image modality (I), outperforms other cross-modal strategies significantly. | comparison identity and matched condition | p. 12 (4 Experiments) |
| Although there remains a gap in accuracy compared with methods that use extensive image collections as maps (such as CVNet and AnyLoc), SceneGraphLoc benefits ... | comparison identity and matched condition | p. 13 (4 Experiments) |
| Also, the storage of SceneGraphLoc with and without images is the same due to its design of distilling knowledge into fixed-sized embeddings. | comparison identity and matched condition | p. 12 (4 Experiments) |
| For a fair comparison, all the methods only use the same selected images for training and evaluation. | comparison identity and matched condition | p. 13 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Also, the storage of SceneGraphLoc with and without images is the same due to its design of distilling knowledge into fixed-sized embeddings. | component/input/data sensitivity | p. 12 (4 Experiments) |
| OpenMask3D attains an accuracy comparable to our proposed method without incorporating the image modality. | component/input/data sensitivity | p. 13 (4 Experiments) |
| Table 4: Ablation study performed on the val. split of 3RScan [123], analysing map modalities (P - point cloud, I - image, A - ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Both methods were fine-tuned on our dataset for accurate comparison. | component/input/data sensitivity | p. 10 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This method enables the creation of small, efficient databases and significantly accelerates the coarse localization process. | SceneGraphLoc, even when excluding the image modality (I), outperforms other cross-modal strategies significantly. | PDF body cue; verify exact table/figure and matched conditions | p. 12 (4 Experiments), p. 13 (4 Experiments), p. 12 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments) |
| Primary metric/result | LidarCLIP shows a small improvement in accuracy. | numeric claim only at cited anchor | p. 13 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 11 / 4 Experiments - extractive body cue:** The 3RScan dataset [123] comprises 1335 annotated indoor scenes, representing 432 distinct rooms, with 1178 scenes (385 rooms) allocated for training and 157 (47 rooms) ...
- **p. 11 / 4 Experiments - extractive body cue:** Thus, we reorganized the original validation set, allocating 34 scenes (17 rooms) for validation and 123 scenes (30 rooms) for testing.
- **p. 11 / 4 Experiments - extractive body cue:** During testing, we examine all 123 scenes of 30 rooms within the test set, selecting query images from each scene.
- **p. 11 / 4 Experiments - extractive body cue:** Furthermore, we evaluate scene selection through two settings N = 50 and N = 10.
- **p. 13 / 4 Experiments - extractive body cue:** We divide the official validation set, which includes 312 scenes, into two distinct subsets: the first 100 scenes form our validation set, while the remaining ...
- **p. 13 / 4 Experiments - extractive body cue:** The results are in Table 2 for scenarios selecting the target room from subsets of 10, 50, and the entire set of 210 scenes.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| These methods offer advanced performance but demand significant storage for image descriptors and exhibit slower inference times. | p. 10 (4 Experiments) |
| Additionally, we will report the inference time and storage requirements. | p. 11 (4 Experiments) |
| For our proposed method, this entails passing the point cloud, images, metadata, and relationships through the 3D scene graph encoder outlined in Section 3.1. | p. 10 (4 Experiments) |
| For image-based methods like CVNet and AnyLoc, embeddings for all images in the database are precomputed. | p. 11 (4 Experiments) |
| Given the absence of scene graph annotations in ScanNet, we run the SceneGraphFusion [130] on the RGBD sequences of scans for 3D reconstruction and ... | p. 12 (4 Experiments) |
| Coarse visual localization, or place recognition, is a fundamental component in computer vision and robotics applications, defined as the task of identifying the approximate ... | p. 1 (1 Introduction) |
| This capability is crucial for estimating the state of robots and is widely utilized in autonomous, unmanned aerial, terrestrial, and underwater vehicles, as well ... | p. 2 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not recovered

- **Evidence anchors reviewed:** datasets p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), metrics p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 13 (4 Experiments), p. 11 (4 Experiments), p. 10 (4 Experiments), baselines p. 10 (4 Experiments), p. 10 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), results p. 12 (4 Experiments), p. 13 (4 Experiments), p. 12 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
