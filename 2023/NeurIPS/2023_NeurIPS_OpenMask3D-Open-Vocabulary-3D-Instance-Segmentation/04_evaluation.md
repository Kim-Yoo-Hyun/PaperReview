# Evaluation - OpenMask3D: Open-Vocabulary 3D Instance Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.13631; PDF retrieval source: https://arxiv.org/pdf/2306.13631. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 18 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 6 (4 Experiments), p. 6 (4 Experiments)): Figure 10: Output of SAM, using only 5 randomly sampled points of the mask as input. Here the sampled points (the green points visualized in the image) are concentrated in ...

## Evaluation Body Digest

- **p. 6 / 4 Experiments - extractive body cue:** To assess the generalization capability of our method, we further experiment with the Replica [61] dataset, and evaluate on the office0, office1, office2, office3, office4, ...
- **p. 6 / 4 Experiments - extractive body cue:** We report our ScanNet200 results on the validation set consisting of 312 scenes, and evaluate for the 3D instance segmentation task using the closed vocabulary ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 10: Output of SAM, using only 5 randomly sampled points of the mask as input. Here the sampled points (the green points visualized in ...
- **p. 6 / 4 Experiments - extractive body cue:** AP scores are evaluated at mask overlap thresholds of 50% and 25%, and averaged over the overlap 6
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 11: Illustration of the results from the round which gives the highest confidence score. On the left, we visualize the 5 sampled points which ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 8: Output of SAM, using all of the visible points from the projected 3D mask as input. To address this issue, we explore an ...
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 15: Qualitative results from OpenMask3D. We show open-vocabulary instance segmentation results using arbitrary queries involving object categories that are not present in the ScanNet200 ...
- **p. 6 / 4 Experiments - extractive body cue:** We employ a commonly used 3D instance segmentation metric, average precision (AP).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4 Experiments (p. 6); B Additional results (p. 19); B.2 Evaluation on Replica without RGB-D images (p. 19); C Details on baseline experiments (p. 19).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 10: Output of SAM, using only 5 randomly sampled points of the mask as input. Here the sampled points (the green points visualized ... | p. 18 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 1: 3D instance segmentation results on the ScanNet200 validation set. Metrics are respectively: AP averaged over an overlap range, and AP evaluated at ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 2: 3D instance segmentation results on the Replica [61] dataset. To assess how well our model generalizes to other datasets, we use instance ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 5: 3D instance segmentation results on the ScanNet200 validation set, using oracle masks. We use ground truth instance masks for computing the per-mask ... | p. 9 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Additional results are provided in the Appendix. | p. 6 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 4 Experiments - extractive body cue:** To assess the generalization capability of our method, we further experiment with the Replica [61] dataset, and evaluate on the office0, office1, office2, office3, office4, ...
- **p. 6 / 4 Experiments - extractive body cue:** We report our ScanNet200 results on the validation set consisting of 312 scenes, and evaluate for the 3D instance segmentation task using the closed vocabulary ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Open-Vocabulary 3D Instance Segmentation. Given a 3D scene (top) and free-form user queries (bottom), our OpenMask3D segments object instances and scene parts described ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: An overview of our approach. We propose OpenMask3D, the first open-vocabulary 3D instance segmentation model. Our pipeline consists of four subsequent steps: 1⃝Our ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Mask-Feature Computation Module. For each instance mask, a⃝we first compute the visibility of the instance in each frame, and select top-k views with ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: 3D instance segmentation results on the ScanNet200 validation set. Metrics are respectively: AP averaged over an overlap range, and AP evaluated at 50% ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: 3D instance segmentation results on the Replica [61] dataset. To assess how well our model generalizes to other datasets, we use instance masks ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: 3D instance segmentation results using masks from mask module trained on ScanNet20 annota- tions, evaluated on the ScanNet200 dataset [57]. We identify 53 ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: OpenMask3D Ablation Study. 2D mask and multi-scale crop components. 2D mask refers to whether SAM [36] was employed for computing 2D masks. Results ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 5: 3D instance segmentation results on the ScanNet200 validation set, using oracle masks. We use ground truth instance masks for computing the per-mask features. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To assess the generalization capability of our method, we further experiment with the Replica [61] dataset, and evaluate on the office0, office1, office2, office3, ... | embodiment, simulator version and control stack | p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Task/environment | We report our ScanNet200 results on the validation set consisting of 312 scenes, and evaluate for the 3D instance segmentation task using the closed ... | reset, timeout, object/scene variation | p. 6 (4 Experiments) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (3 Method), p. 6 (3 Method) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 3 (3 Method), p. 4 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 10: Output of SAM, using only 5 randomly sampled points of the mask as input. Here the sampled points (the green points visualized ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| AP scores are evaluated at mask overlap thresholds of 50% and 25%, and averaged over the overlap 6 | definition/direction/unit from same section | p. 6 (4 Experiments) |
| Figure 11: Illustration of the results from the round which gives the highest confidence score. On the left, we visualize the 5 sampled points ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| Figure 8: Output of SAM, using all of the visible points from the projected 3D mask as input. To address this issue, we explore ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| Figure 15: Qualitative results from OpenMask3D. We show open-vocabulary instance segmentation results using arbitrary queries involving object categories that are not present in the ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| We employ a commonly used 3D instance segmentation metric, average precision (AP). | definition/direction/unit from same section | p. 6 (4 Experiments) |
| Table 5: 3D instance segmentation results on the ScanNet200 validation set, using oracle masks. We use ground truth instance masks for computing the per-mask ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Figure 4: Qualitative results from OpenMask3D. Our open-vocabulary instance segmentation approach is capable of handling different types of queries. Novel object classes as well ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 5: 3D instance segmentation results on the ScanNet200 validation set, using oracle masks. We use ground truth instance masks for computing the per-mask ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Table 1: 3D instance segmentation results on the ScanNet200 validation set. Metrics are respectively: AP averaged over an overlap range, and AP evaluated at ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 2: 3D instance segmentation results on the Replica [61] dataset. To assess how well our model generalizes to other datasets, we use instance ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Furthermore, we provide an ablation study for OpenMask3D. | comparison identity and matched condition | p. 6 (4 Experiments) |
| Table 7: Ablation study of the multi-scale cropping hyperparameters on the Replica dataset. We analyze the effect of varying number of levels, and the ... | comparison identity and matched condition | p. 19 (Figure/Table caption) |
| Table 3: 3D instance segmentation results using masks from mask module trained on ScanNet20 annota- tions, evaluated on the ScanNet200 dataset [57]. We identify ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 7: Ablation study of the multi-scale cropping hyperparameters on the Replica dataset. We analyze the effect of varying number of levels, and the ... | component/input/data sensitivity | p. 19 (Figure/Table caption) |
| Furthermore, we provide an ablation study for OpenMask3D. | component/input/data sensitivity | p. 6 (4 Experiments) |
| Table 4: OpenMask3D Ablation Study. 2D mask and multi-scale crop components. 2D mask refers to whether SAM [36] was employed for computing 2D masks. ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Table 3: 3D instance segmentation results using masks from mask module trained on ScanNet20 annota- tions, evaluated on the ScanNet200 dataset [57]. We identify ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 6: Ablation study of the top-k frame selection parameter k. This analysis is conducted on the ScanNet200 validation set. Levels Ratio of Exp. ... | component/input/data sensitivity | p. 19 (Figure/Table caption) |
| Figure 12: Visualization of the Replica RGB images. Original RGB images from the Replica dataset (left), and RGB images rendered from the scene point ... | component/input/data sensitivity | p. 20 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are three-fold: • We introduce the open-vocabulary 3D instance segmentation task in which the object instances that are similar to a given ... | Figure 10: Output of SAM, using only 5 randomly sampled points of the mask as input. Here the sampled points (the green points visualized ... | PDF body cue; verify exact table/figure and matched conditions | p. 18 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Primary metric/result | Table 1: 3D instance segmentation results on the ScanNet200 validation set. Metrics are respectively: AP averaged over an overlap range, and AP evaluated at ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Experiments - extractive body cue:** We report our ScanNet200 results on the validation set consisting of 312 scenes, and evaluate for the 3D instance segmentation task using the closed vocabulary ...
- **p. 4 / 3 Method - extractive body cue:** 3.2.1 Frame selection Obtaining representative images of the proposed object instances is crucial for extracting accurate CLIP features.
- **p. 7 / Model - extractive body cue:** We use posed RGB-depth pairs for both the ScanNet200 and Replica datasets, and we process 1 frame in every 10 frames in the RGB-D sequences.
- **p. 7 / Model - extractive body cue:** In the 2D mask selection algorithm based on SAM [36], we repeat the process for krounds = 10 rounds, and sample ksample = 5 points ...
- **p. 7 / Model - extractive body cue:** Note that once the per-mask features of the scene are computed, objects can be queried in real-time (∼1-2 ms) with arbitrary open-vocabulary queries.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 9: Output of SAM, using only 5 randomly sampled points (visualized as green dots) of the projected 3D mask as input. A.2.4 Why ... | p. 18 (Figure/Table caption) |
| body limitation/failure cue | Table 1: 3D instance segmentation results on the ScanNet200 validation set. Metrics are respectively: AP averaged over an overlap range, and AP evaluated at ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Figure 10: Output of SAM, using only 5 randomly sampled points of the mask as input. Here the sampled points (the green points visualized ... | p. 18 (Figure/Table caption) |
| body limitation/failure cue | Figure 7: Difference between the bounding boxes obtained by tightly cropping around the projected points from the 3D instance mask (left), and the bounding ... | p. 17 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Next, the CLIP encoder is employed to obtain image-embeddings of multi-scale image-crops bounding the computed 2D masks. | p. 3 (3 Method) |
| In b⃝, we compute a 2D object mask in each selected frame, which is used to obtain multi-scale image-crops in order to extract effective ... | p. 5 (3 Method) |
| The computed features are task-agnostic, and can be used for various instance-based tasks by encoding a given text or image-based query, using the same ... | p. 6 (3 Method) |
| In order to compute image features on the mask-crops, we use CLIP [55] visual encoder from the ViT-L/14 model pre-trained at a 336 pixel ... | p. 7 (Model) |
| The mask-feature computation module leverages pre-trained CLIP [55] vision-language model in order to compute meaningful and flexible features for each mask. | p. 3 (3 Method) |
| Here, we explain how we compute these visibility scores. | p. 4 (3 Method) |
| 3, the mask-feature computation module consists of several steps. | p. 4 (3 Method) |
| Here, kview represents another hyperparameter. | p. 5 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 18 / Figure/Table caption - extractive body cue:** Figure 9: Output of SAM, using only 5 randomly sampled points (visualized as green dots) of the projected 3D mask as input. A.2.4 Why do ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: 3D instance segmentation results on the ScanNet200 validation set. Metrics are respectively: AP averaged over an overlap range, and AP evaluated at 50% ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 10: Output of SAM, using only 5 randomly sampled points of the mask as input. Here the sampled points (the green points visualized in ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 7: Difference between the bounding boxes obtained by tightly cropping around the projected points from the 3D instance mask (left), and the bounding box ...

- **Evidence anchors reviewed:** datasets p. 6 (4 Experiments), p. 6 (4 Experiments), metrics p. 18 (Figure/Table caption), p. 6 (4 Experiments), p. 19 (Figure/Table caption), p. 18 (Figure/Table caption), p. 23 (Figure/Table caption), p. 6 (4 Experiments), baselines p. 9 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4 Experiments), p. 19 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 18 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 6 (4 Experiments), p. 6 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
