# Evaluation - nuScenes: A Multimodal Dataset for Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1903.11027; PDF retrieval source: https://arxiv.org/pdf/1903.11027. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.1. Baselines), p. 7 (4.2. Analysis), p. 8 (4.2. Analysis), p. 8 (4.2. Analysis), p. 4 (2. The nuScenes dataset), p. 4 (2. The nuScenes dataset)): submissions, MonoDIS [70] was the best, significantly outperforming our image baseline and even some lidar based methods.

## Evaluation Body Digest

- **p. 6 / 4. Experiments - extractive body cue:** In this section we present object detection and tracking experiments on the nuScenes dataset, analyze their characteristics and suggest avenues for future research.
- **p. 3 / 1.2. Related datasets - extractive body cue:** The Lyft L5 dataset [45] is most similar to nuScenes.
- **p. 3 / Dataset - extractive body cue:** (‡) The current Waymo Open dataset size is comparable to nuScenes, but at a 5x higher annotation frequency.
- **p. 5 / 2. The nuScenes dataset - extractive body cue:** Due to the finegrained classes in nuScenes, the dataset shows severe class imbalance with a ratio of 1:10k for the least and most common class ...
- **p. 7 / 4.2. Analysis - extractive body cue:** The case for a large benchmark dataset.
- **p. 7 / 4.2. Analysis - extractive body cue:** One of the contributions of nuScenes is the dataset size, and in particular the increase compared to KITTI (Table 1).
- **p. 8 / 4.2. Analysis - extractive body cue:** Object detection results on the test set of nuScenes.
- **p. 5 / 2. The nuScenes dataset - extractive body cue:** Our dataset has 23 categories including different vehicles, types of pedestrians, mobility devices and other objects (Figure 8-SM).

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** Dataset (p. 3); 1.2. Related datasets (p. 3); 2. The nuScenes dataset (p. 3); 4. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Baselines | BENCHMARK / DATASET | submissions, MonoDIS [70] was the best, significantly outperforming our image baseline and even some lidar based methods. | p. 7 (4.1. Baselines) |
| 4.2. Analysis | BENCHMARK / DATASET | Multiple lidar sweeps improve performance. | p. 7 (4.2. Analysis) |
| 4.2. Analysis | BENCHMARK / DATASET | An important question for AVs is which sensors are required to achieve the best detection performance. | p. 8 (4.2. Analysis) |
| 4.2. Analysis | BENCHMARK / DATASET | Weng and Kitani [77] presented a simple baseline that achieved stateof-the-art 3d tracking results using powerful detections on KITTI. | p. 8 (4.2. Analysis) |
| 2. The nuScenes dataset | BENCHMARK / DATASET | This method is very robust and we achieve localization errors of ≤10cm. | p. 4 (2. The nuScenes dataset) |

## Dataset / Benchmark Role

- **p. 6 / 4. Experiments - extractive body cue:** In this section we present object detection and tracking experiments on the nuScenes dataset, analyze their characteristics and suggest avenues for future research.
- **p. 3 / 1.2. Related datasets - extractive body cue:** The Lyft L5 dataset [45] is most similar to nuScenes.
- **p. 3 / Dataset - extractive body cue:** (‡) The current Waymo Open dataset size is comparable to nuScenes, but at a 5x higher annotation frequency.
- **p. 5 / 2. The nuScenes dataset - extractive body cue:** Due to the finegrained classes in nuScenes, the dataset shows severe class imbalance with a ratio of 1:10k for the least and most common class ...
- **p. 7 / 4.2. Analysis - extractive body cue:** The case for a large benchmark dataset.
- **p. 7 / 4.2. Analysis - extractive body cue:** One of the contributions of nuScenes is the dataset size, and in particular the increase compared to KITTI (Table 1).
- **p. 8 / 4.2. Analysis - extractive body cue:** Object detection results on the test set of nuScenes.
- **p. 5 / 2. The nuScenes dataset - extractive body cue:** Our dataset has 23 categories including different vehicles, types of pedestrians, mobility devices and other objects (Figure 8-SM).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. An example from the nuScenes dataset. We see 6 dif- ferent camera views, lidar and radar data, as well as the human annotated ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Front camera images collected from clear weather (col 1), nighttime (col 2), rain (col 3) and construction zones (col 4). and blind spots. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. AV dataset comparison. The top part of the table indicates datasets without range data. The middle and lower parts indicate datasets (not publications) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 2. Sensor data in nuScenes. erage of 16km/h). Driving routes are carefully chosen to capture a diverse set of locations (urban, residential, nature and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Semantic map of nuScenes with 11 semantic layers in different colors. To show the path of the ego vehicle we plot each keyframe ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Sensor setup for our data collection platform.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. Spatial data coverage for two nuScenes locations. Colors indicate the number of keyframes with ego vehicle poses within a 100m radius across all ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. Amount of training data vs. mean Average Precision (mAP) on the val set of nuScenes. The dashed black line corre- sponds to the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In this section we present object detection and tracking experiments on the nuScenes dataset, analyze their characteristics and suggest avenues for future research. | embodiment, simulator version and control stack | p. 6 (4. Experiments), p. 3 (1.2. Related datasets) |
| Task/environment | The Lyft L5 dataset [45] is most similar to nuScenes. | reset, timeout, object/scene variation | p. 3 (1.2. Related datasets), p. 3 (Dataset) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 2 (1.1. Contributions) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 3 (1.2. Related datasets), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 7. Detailed detection performance for PointPillars [51] (top) and MonoDIS [70] (bottom) on the test set. AP: average precision averaged over distance thresholds ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| MonoDIS also had larger scale errors with mean IOU 74% vs. | definition/direction/unit from same section | p. 8 (4.2. Analysis) |
| We compare performance of published methods (Table 4) when using our proposed 2m center-distance matching versus the IOU matching used in KITTI. | definition/direction/unit from same section | p. 7 (4.2. Analysis) |
| Method NDS mAP mATE mASE mAOE mAVE mAAE (%) (%) (m) (1-iou) (rad) (m/s) (1-acc) OFT [69]† 21.2 12.6 0.82 0.36 0.85 1.73 0.48 ... | definition/direction/unit from same section | p. 8 (4.2. Analysis) |
| Figure 6. Amount of training data vs. mean Average Precision (mAP) on the val set of nuScenes. The dashed black line corre- sponds to ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| To demonstrate the performance of a leading algorithm on nuScenes, we train a lidaronly 3D object detector, PointPillars [51]. | definition/direction/unit from same section | p. 6 (4.1. Baselines) |
| Figure 16. PointPillars [51] detection performance vs. semantic prior map location on the val set. For the best lidar network (10 li- dar sweeps ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| This method is very robust and we achieve localization errors of ≤10cm. | definition/direction/unit from same section | p. 4 (2. The nuScenes dataset) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| submissions, MonoDIS [70] was the best, significantly outperforming our image baseline and even some lidar based methods. | comparison identity and matched condition | p. 7 (4.1. Baselines) |
| We present a number of baselines with different modalities for detection and tracking. | comparison identity and matched condition | p. 6 (4.1. Baselines) |
| We present several baselines for tracking from camera and lidar data. | comparison identity and matched condition | p. 7 (4.1. Baselines) |
| Compared to the mAP and NDS detection results in Table 4, the ranking is similar. | comparison identity and matched condition | p. 8 (4.2. Analysis) |
| Using the lidar baseline we examine the importance of pre-training when training a detector on nuScenes. | comparison identity and matched condition | p. 8 (4.2. Analysis) |
| It provides 200k 3D boxes over 22 scenes which helped advance the state-of-the-art in 3D object detection. | comparison identity and matched condition | p. 3 (1.2. Related datasets) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For this ablation study we train PointPillars with 6x fewer epochs and a one cycle optimizer schedule [71] to cut down the training time. | component/input/data sensitivity | p. 7 (4.2. Analysis) |
| The top part of the table indicates datasets without range data. | component/input/data sensitivity | p. 3 (Dataset) |
| Other notable multimodal datasets include [15] providing driving behavior labels, [43] providing place categorization labels and [6, 55] providing raw data without semantic labels. | component/input/data sensitivity | p. 3 (1.2. Related datasets) |
| No pretraining means weights are initialized randomly using a uniform distribution as in [38]. | component/input/data sensitivity | p. 8 (4.2. Analysis) |
| ImageNet [21] pretraining [47] uses a backbone that was first trained to accurately classify images. | component/input/data sensitivity | p. 8 (4.2. Analysis) |
| Figure 16. PointPillars [51] detection performance vs. semantic prior map location on the val set. For the best lidar network (10 li- dar sweeps ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our second contribution is new detection and tracking metrics aimed at the AV application. | submissions, MonoDIS [70] was the best, significantly outperforming our image baseline and even some lidar based methods. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.1. Baselines), p. 7 (4.2. Analysis), p. 8 (4.2. Analysis), p. 8 (4.2. Analysis), p. 4 (2. The nuScenes dataset), p. 4 (2. The nuScenes dataset) |
| Primary metric/result | Multiple lidar sweeps improve performance. | numeric claim only at cited anchor | p. 7 (4.2. Analysis) |

- Numeric sentences retained from the body:
- **p. 3 / Dataset - extractive body cue:** (‡) The current Waymo Open dataset size is comparable to nuScenes, but at a 5x higher annotation frequency.
- **p. 3 / 1.2. Related datasets - extractive body cue:** It provides 200k 3D boxes over 22 scenes which helped advance the state-of-the-art in 3D object detection.
- **p. 3 / 1.2. Related datasets - extractive body cue:** Among these datasets, only the Waymo Open dataset [76] provides significantly more annotations, mostly due to the higher annotation frequency (10Hz vs.
- **p. 3 / 1.2. Related datasets - extractive body cue:** A*3D takes an orthogonal approach where a similar number of frames (39k) are selected and annotated from 55 hours of data.
- **p. 3 / 2. The nuScenes dataset - extractive body cue:** From a large body of training data we manually select 84 logs with 15h of driving data (242km travelled at an av4In preliminary analysis we ...
- **p. 3 / 2. The nuScenes dataset - extractive body cue:** A similar conclusion was drawn for H3D [61] where annotations are interpolated from 2Hz to 10Hz.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Future work will add image-level and pointlevel semantic labels and a benchmark for trajectory prediction [63]. | p. 8 (5. Conclusion) |
| body limitation/failure cue | From a large body of training data we manually select 84 logs with 15h of driving data (242km travelled at an av4In preliminary analysis ... | p. 3 (2. The nuScenes dataset) |
| body limitation/failure cue | This method is very robust and we achieve localization errors of ≤10cm. | p. 4 (2. The nuScenes dataset) |
| body limitation/failure cue | As expected, when using IOU matching, small objects like pedestrians and bicycles fail to achieve above 0 AP, making ordering impossible (Figure 7). | p. 7 (4.2. Analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For this ablation study we train PointPillars with 6x fewer epochs and a one cycle optimizer schedule [71] to cut down the training time. | p. 7 (4.2. Analysis) |
| From the detection challenge, we pick the best performing lidar method (Megvii [90]), the fastest reported method at inference time (PointPillars [51]), as well ... | p. 7 (4.1. Baselines) |
| Image based benchmark datasets have driven development in computer vision tasks such as object detection, tracking and segmentation of agents in the environment. | p. 1 (Abstract) |
| All data, code, and information is made available online3. | p. 2 (1.1. Contributions) |
| Third, we publish the devkit, evaluation code, taxonomy, annotator instructions, and database schema for industrywide standardization. | p. 2 (1.1. Contributions) |
| 5The cameras run at 12Hz while the lidar runs at 20Hz. | p. 4 (2. The nuScenes dataset) |
| Using expert annotators and multiple validation steps, we achieve highly accurate annotations. | p. 4 (2. The nuScenes dataset) |
| For each TP metric we compute the mean TP metric (mTP) over all classes: mTP = 1 /C/ X c∈C TPc (2) We omit ... | p. 5 (3.1. Detection) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** Future work will add image-level and pointlevel semantic labels and a benchmark for trajectory prediction [63].
- **p. 3 / 2. The nuScenes dataset - extractive body cue:** From a large body of training data we manually select 84 logs with 15h of driving data (242km travelled at an av4In preliminary analysis we ...
- **p. 4 / 2. The nuScenes dataset - extractive body cue:** This method is very robust and we achieve localization errors of ≤10cm.
- **p. 7 / 4.2. Analysis - extractive body cue:** As expected, when using IOU matching, small objects like pedestrians and bicycles fail to achieve above 0 AP, making ordering impossible (Figure 7).

- **Evidence anchors reviewed:** datasets p. 6 (4. Experiments), p. 3 (1.2. Related datasets), p. 3 (Dataset), p. 5 (2. The nuScenes dataset), p. 7 (4.2. Analysis), p. 7 (4.2. Analysis), metrics p. 15 (Figure/Table caption), p. 8 (4.2. Analysis), p. 7 (4.2. Analysis), p. 8 (4.2. Analysis), p. 7 (Figure/Table caption), p. 6 (4.1. Baselines), baselines p. 7 (4.1. Baselines), p. 6 (4.1. Baselines), p. 7 (4.1. Baselines), p. 8 (4.2. Analysis), p. 8 (4.2. Analysis), p. 3 (1.2. Related datasets), results p. 7 (4.1. Baselines), p. 7 (4.2. Analysis), p. 8 (4.2. Analysis), p. 8 (4.2. Analysis), p. 4 (2. The nuScenes dataset), p. 4 (2. The nuScenes dataset).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
