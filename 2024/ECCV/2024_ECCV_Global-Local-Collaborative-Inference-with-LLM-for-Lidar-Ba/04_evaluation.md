# Evaluation - Global-Local Collaborative Inference with LLM for Lidar-Based Open-Vocabulary Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5197_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05197.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 13 (Figure/Table caption), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 14 (Figure/Table caption)): Fig. 4: Visualizations of GLIS. The score of each proposal is the confidence that the proposal is truly a foreground object. These proposals, as well as their confidence scores, are ...

## Evaluation Body Digest

- **p. 11 / 4 Experiments - extractive PDF cue:** SUN RGB-D is a large 3D object detection and scene understanding dataset, which contains 10335 samples with around 800 object classes.
- **p. 10 / 4 Experiments - extractive PDF cue:** 4.1 Datasets and Metrics We conduct experiments on two datasets: ScanNetV2 [7] and SUN RGB-D [38].
- **p. 11 / 4 Experiments - extractive PDF cue:** For a fair comparison, we evaluate our GLIS on the top-20 object classes in ScanNetV2 and SUN RGB-D respectively, following OV-3DET [26].
- **p. 11 / 4 Experiments - extractive PDF cue:** We use the mean Average Precision (mAP) at the IoU threshold of 0.25 to evaluate the detection performance.
- **p. 13 / Figure/Table caption - extractive PDF cue:** Fig. 4: Visualizations of GLIS. The score of each proposal is the confidence that the proposal is truly a foreground object. These proposals, as well ...
- **p. 11 / 4 Experiments - extractive PDF cue:** The base learning rate is set as 1e-4.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 2: The training pipeline of GLIS. local branch, the bounding boxes are extracted by the Background-Aware Ob- ject Localization (BAOL) module, while the object ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Fig. 5: Visualizations of detection results. the LLM's answer, our scheme automatically recognizes the bed as false detec- tion. Subsequently, as the confidence of the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 10).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 4: Visualizations of GLIS. The score of each proposal is the confidence that the proposal is truly a foreground object. These proposals, as ... | p. 13 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our methods also significantly improve the detection precision of many classes, e.g., chair is improved by 10.79%, toilet is improved by 5.81%, and table ... | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1, our proposed GLIS greatly improves the open-vocabulary detection performance on ScanNetV2. | p. 11 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 5: Visualizations of detection results. the LLM's answer, our scheme automatically recognizes the bed as false detec- tion. Subsequently, as the confidence of ... | p. 14 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 11 / 4 Experiments - extractive PDF cue:** SUN RGB-D is a large 3D object detection and scene understanding dataset, which contains 10335 samples with around 800 object classes.
- **p. 10 / 4 Experiments - extractive PDF cue:** 4.1 Datasets and Metrics We conduct experiments on two datasets: ScanNetV2 [7] and SUN RGB-D [38].
- **p. 11 / 4 Experiments - extractive PDF cue:** For a fair comparison, we evaluate our GLIS on the top-20 object classes in ScanNetV2 and SUN RGB-D respectively, following OV-3DET [26].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: (a) The previous 3D OVD paradigm determines the class of an object proposal by comparing its point cloud feature with the class text ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 2: The training pipeline of GLIS. local branch, the bounding boxes are extracted by the Background-Aware Ob- ject Localization (BAOL) module, while the object ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 3: The inference pipeline of GLIS. With the extracted local and global information, we can conduct global- local collaborative inference (GLCI) with LLM and ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 1: Comparisons with other methods on ScanNetV2
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 2: Comparisons with other methods on SUN RGB-D
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 3: Ablation study on ScanNetV2
- **p. 13 / Figure/Table caption - extractive PDF cue:** Fig. 4: Visualizations of GLIS. The score of each proposal is the confidence that the proposal is truly a foreground object. These proposals, as well ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Fig. 5: Visualizations of detection results. the LLM's answer, our scheme automatically recognizes the bed as false detec- tion. Subsequently, as the confidence of the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | SUN RGB-D is a large 3D object detection and scene understanding dataset, which contains 10335 samples with around 800 object classes. | embodiment, simulator version and control stack | p. 11 (4 Experiments), p. 10 (4 Experiments) |
| Task/environment | 4.1 Datasets and Metrics We conduct experiments on two datasets: ScanNetV2 [7] and SUN RGB-D [38]. | reset, timeout, object/scene variation | p. 10 (4 Experiments), p. 11 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 7 (X. Peng et al), p. 3 (X. Peng et al) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (X. Peng et al), p. 2 (X. Peng et al) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We use the mean Average Precision (mAP) at the IoU threshold of 0.25 to evaluate the detection performance. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| Fig. 4: Visualizations of GLIS. The score of each proposal is the confidence that the proposal is truly a foreground object. These proposals, as ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| The base learning rate is set as 1e-4. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| Fig. 2: The training pipeline of GLIS. local branch, the bounding boxes are extracted by the Background-Aware Ob- ject Localization (BAOL) module, while the ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Fig. 5: Visualizations of detection results. the LLM's answer, our scheme automatically recognizes the bed as false detec- tion. Subsequently, as the confidence of ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to previous sota method CoDA [2], mAP 10cls 25 is raised from 28.76% to 30.94% and mAP 20cls 25 is raised from 19.32% ... | comparison identity and matched condition | p. 11 (4 Experiments) |
| We also report the results on top-10 classes for comparison with methods like [25, 56]. | comparison identity and matched condition | p. 11 (4 Experiments) |
| Table 3: Ablation study on ScanNetV2 | comparison identity and matched condition | p. 12 (Figure/Table caption) |
| Table 2: Comparisons with other methods on SUN RGB-D | comparison identity and matched condition | p. 12 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 4: Visualizations of GLIS. The score of each proposal is the confidence that the proposal is truly a foreground object. These proposals, as ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| Table 3: Ablation study on ScanNetV2 | component/input/data sensitivity | p. 12 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are as follows. - We propose a lidar-based open-vocabulary detection method, GLIS, which is the first work to explore the ... | Fig. 4: Visualizations of GLIS. The score of each proposal is the confidence that the proposal is truly a foreground object. These proposals, as ... | PDF body cue; verify exact table/figure and matched conditions | p. 13 (Figure/Table caption), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 14 (Figure/Table caption) |
| Primary metric/result | Our methods also significantly improve the detection precision of many classes, e.g., chair is improved by 10.79%, toilet is improved by 5.81%, and table ... | numeric claim only at cited anchor | p. 11 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 11 / 4 Experiments - extractive PDF cue:** SUN RGB-D is a large 3D object detection and scene understanding dataset, which contains 10335 samples with around 800 object classes.
- **p. 11 / 4 Experiments - extractive PDF cue:** For a fair comparison, we evaluate our GLIS on the top-20 object classes in ScanNetV2 and SUN RGB-D respectively, following OV-3DET [26].
- **p. 11 / 4 Experiments - extractive PDF cue:** The training of phase 1 lasts for 400 epochs with a total batch size of 32 (i.e., a single batch size 4 × 8 GPUs).
- **p. 11 / 4 Experiments - extractive PDF cue:** The training of phase 2 lasts for 50 epochs with a total batch size of 16.
- **p. 3 / X. Peng et al - extractive PDF cue:** Global-Local Collaborative Inference 3 scene-level information.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | These limitations could inspire our future work. | p. 14 (X. Peng et al) |
| body limitation/failure cue | The limitation of GLIS exists due to the noises within the point cloud and the false pseudo labels generated from the 2D image. | p. 14 (X. Peng et al) |
| body limitation/failure cue | This proves that BAOL can overcome the disturbance of noises in point clouds, resulting in better localization for interested objects. | p. 12 (X. Peng et al) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The training of phase 2 lasts for 50 epochs with a total batch size of 16. | p. 11 (4 Experiments) |
| The base learning rate is set as 1e-4. | p. 11 (4 Experiments) |
| As a basic function of machine perception, object detection has attracted much attention within computer vision communities. | p. 1 (1 Introduction) |
| Point Cloud Encoder Text Encoder Desk Cabinet Table … … 0.43 0.37 0.18 If the object is not a desk, what is it probably ... | p. 2 (X. Peng et al) |
| LLM Encoder LLM Global Projector What kind of scene is it mostly like? | p. 6 (X. Peng et al) |
| LLM Encoder predicted bounding boxes Sink, Desk, Desk, Toilet predicted object classes Scene: bathroom Description: There is a toilet and a cabinet. predicted scene ... | p. 6 (X. Peng et al) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / X. Peng et al - extractive PDF cue:** These limitations could inspire our future work.
- **p. 14 / X. Peng et al - extractive PDF cue:** The limitation of GLIS exists due to the noises within the point cloud and the false pseudo labels generated from the 2D image.
- **p. 12 / X. Peng et al - extractive PDF cue:** This proves that BAOL can overcome the disturbance of noises in point clouds, resulting in better localization for interested objects.

- **PDF anchors reviewed:** datasets p. 11 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), metrics p. 11 (4 Experiments), p. 13 (Figure/Table caption), p. 11 (4 Experiments), p. 6 (Figure/Table caption), p. 14 (Figure/Table caption), baselines p. 11 (4 Experiments), p. 11 (4 Experiments), p. 12 (Figure/Table caption), p. 12 (Figure/Table caption), results p. 13 (Figure/Table caption), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 14 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
