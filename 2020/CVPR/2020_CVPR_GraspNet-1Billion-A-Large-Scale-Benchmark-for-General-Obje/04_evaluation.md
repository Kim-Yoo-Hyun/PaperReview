# Evaluation - GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1912.13470; PDF retrieval source: https://arxiv.org/pdf/1912.13470. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.1. Ground-Truth Evaluation), p. 4 (3.4. Evaluation), p. 3 (3.3. Data Annotation), p. 4 (3.4. Evaluation), p. 5 (4.1. Ground-Truth Evaluation), p. 3 (3.3. Data Annotation)): Summary of real world success rate of grasping given different grasp score. grasp poses to the camera frame using objects' 6D poses, we paste ArUco code on the objects and ...

## Evaluation Body Digest

- **p. 4 / 3.4. Evaluation - extractive body cue:** Dataset Split For our 170 scenes, we use 100 for training and 70 for testing.
- **p. 4 / 3.4. Evaluation - extractive body cue:** Specifically, we further divide our test sets into 3 categories: 30 scenes with seen objects, 30 with unseen but similar objects and 10 for novel ...
- **p. 5 / 4. Experiments - extractive body cue:** In this section, we conduct robotic experiments to demonstrate that our ground-truth annotations can align well with real-world grasping.
- **p. 2 / 3.2. Data Collection - extractive body cue:** To collect data of clustered scene, we attach the cameras to a robot arm since it can repeat the trajectory precisely
- **p. 2 / 3.1. Overview - extractive body cue:** Previous grasping dataset either focuses on isolated object [11, 17, 7, 26] or only labels one grasp per scene [21, 14].
- **p. 3 / 3.2. Data Collection - extractive body cue:** The robot arm then moves along a fixed trajectory that covers 256 distinct viewpoints on a quarter sphere.
- **p. 3 / 3.2. Data Collection - extractive body cue:** (a) Both the RealSense and Kinect camera are fixed on the end link of a robot arm.
- **p. 5 / 4.1. Ground-Truth Evaluation - extractive body cue:** For robot arm we adopt a Flexiv Rizon arm and for camera we use the Intel RealSense

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 3. GraspNet Dataset (p. 2); Dataset (p. 4); 3.4. Evaluation (p. 4); 4. Experiments (p. 5); 4.1. Ground-Truth Evaluation (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Ground-Truth Evaluation | BENCHMARK / DATASET | Summary of real world success rate of grasping given different grasp score. grasp poses to the camera frame using objects' 6D poses, we paste ... | p. 5 (4.1. Ground-Truth Evaluation) |
| 3.4. Evaluation | BENCHMARK / DATASET | Currently, the Cornell dataset [11] has achieved over 99% accuracy. | p. 4 (3.4. Evaluation) |
| 3.3. Data Annotation | BENCHMARK / DATASET | To achieve that, high quality mesh models are downsampled such that the sampled points (called grasp points) are uniformly distributed in voxel space. | p. 3 (3.3. Data Annotation) |
| 3.4. Evaluation | BENCHMARK / DATASET | It might overestimate the performance of grasping algorithm. | p. 4 (3.4. Evaluation) |
| 4.1. Ground-Truth Evaluation | BENCHMARK / DATASET | We pick 10 objects from our object set and execute grasp poses that has different scores. | p. 5 (4.1. Ground-Truth Evaluation) |

## Dataset / Benchmark Role

- **p. 4 / 3.4. Evaluation - extractive body cue:** Dataset Split For our 170 scenes, we use 100 for training and 70 for testing.
- **p. 4 / 3.4. Evaluation - extractive body cue:** Specifically, we further divide our test sets into 3 categories: 30 scenes with seen objects, 30 with unseen but similar objects and 10 for novel ...
- **p. 5 / 4. Experiments - extractive body cue:** In this section, we conduct robotic experiments to demonstrate that our ground-truth annotations can align well with real-world grasping.
- **p. 2 / 3.2. Data Collection - extractive body cue:** To collect data of clustered scene, we attach the cameras to a robot arm since it can repeat the trajectory precisely
- **p. 2 / 3.1. Overview - extractive body cue:** Previous grasping dataset either focuses on isolated object [11, 17, 7, 26] or only labels one grasp per scene [21, 14].
- **p. 3 / 3.2. Data Collection - extractive body cue:** The robot arm then moves along a fixed trajectory that covers 256 distinct viewpoints on a quarter sphere.
- **p. 3 / 3.2. Data Collection - extractive body cue:** (a) Both the RealSense and Kinect camera are fixed on the end link of a robot arm.
- **p. 5 / 4.1. Ground-Truth Evaluation - extractive body cue:** For robot arm we adopt a Flexiv Rizon arm and for camera we use the Intel RealSense

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Our methodology for building the dataset. We collect data with real-world sensors and annotate grasp poses for every single object by analytic computation. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. The key components of our dataset. RGB-D images are taken using both RealSense camera and Kinect camera from different views. The 6D pose ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. The setting of data collection. (a) Both the RealSense and Kinect camera are fixed on the end link of a robot arm. (b) ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 4. Grasp pose annotation pipeline. The grasp point is firstly sampled from point cloud. Then the grasp view, the in-place ro- tation angle and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1. Summary of the properties of publicly available grasp datasets. "Rect.", "Cam." and "Sim." are short for Rectangle, Camera and Simulation respectively. "-" denotes ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. (a) Visualization of the detected 6D pose the ArUco marker. (b) Object 6D pose and grasp poses inferred from the marker pose. Object ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Summary of real world success rate of grasping given different grasp score. grasp poses to the camera frame using objects' 6D poses, we ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Dataset Split For our 170 scenes, we use 100 for training and 70 for testing. | embodiment, simulator version and control stack | p. 4 (3.4. Evaluation), p. 4 (3.4. Evaluation) |
| Task/environment | Specifically, we further divide our test sets into 3 categories: 30 scenes with seen objects, 30 with unseen but similar objects and 10 for ... | reset, timeout, object/scene variation | p. 4 (3.4. Evaluation), p. 5 (4. Experiments) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 4 (2 Cams) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 3 (3.2. Data Collection), p. 2 (3.1. Overview) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Summary of real world success rate of grasping given different grasp score. grasp poses to the camera frame using objects' 6D poses, we paste ... | definition/direction/unit from same section | p. 5 (4.1. Ground-Truth Evaluation) |
| New Metrics To evaluate the prediction performance of grasp pose, previous methods adopt the rectangle metric that consider a grasp as correct if: i) ... | definition/direction/unit from same section | p. 4 (3.4. Evaluation) |
| Meanwhile, only the top K grasps from each object are considered according to confidence scores and other grasps are omitted. | definition/direction/unit from same section | p. 5 (3.4. Evaluation) |
| Currently, the Cornell dataset [11] has achieved over 99% accuracy. | definition/direction/unit from same section | p. 4 (3.4. Evaluation) |
| Figure 4. Grasp pose annotation pipeline. The grasp point is firstly sampled from point cloud. Then the grasp view, the in-place ro- tation angle ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig 2 illustrates the key components of our dataset. | definition/direction/unit from same section | p. 2 (3.1. Overview) |
| Besides, we also provide accurate object 6D pose annotations, rectangle based grasp poses, object masks and bounding boxes. | definition/direction/unit from same section | p. 2 (3.1. Overview) |
| Hand-eye calibration is conducted before data collection to obtain accurate camera poses. | definition/direction/unit from same section | p. 3 (3.2. Data Collection) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| no baseline sentence selected | not reported | verify comparison table |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig 2 illustrates the key components of our dataset. | component/input/data sensitivity | p. 2 (3.1. Overview) |
| Figure 2. The key components of our dataset. RGB-D images are taken using both RealSense camera and Kinect camera from different views. The 6D ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our methodology for building the dataset. | Summary of real world success rate of grasping given different grasp score. grasp poses to the camera frame using objects' 6D poses, we paste ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.1. Ground-Truth Evaluation), p. 4 (3.4. Evaluation), p. 3 (3.3. Data Annotation), p. 4 (3.4. Evaluation), p. 5 (4.1. Ground-Truth Evaluation), p. 3 (3.3. Data Annotation) |
| Primary metric/result | Currently, the Cornell dataset [11] has achieved over 99% accuracy. | numeric claim only at cited anchor | p. 4 (3.4. Evaluation) |

- Numeric sentences retained from the body:
- **p. 2 / 3.2. Data Collection - extractive body cue:** We select 32 objects that are suitable for grasping from the YCB dataset [4], 13 adversarial objects from DexNet 2.0 [17] and collect 43 objects ...
- **p. 3 / 3.2. Data Collection - extractive body cue:** For each cluster scene, we randomly pick around 10 objects from our whole set and place them in a clustered manner.
- **p. 4 / 3.4. Evaluation - extractive body cue:** Dataset Split For our 170 scenes, we use 100 for training and 70 for testing.
- **p. 4 / 3.4. Evaluation - extractive body cue:** Specifically, we further divide our test sets into 3 categories: 30 scenes with seen objects, 30 with unseen but similar objects and 10 for novel ...
- **p. 5 / 3.4. Evaluation - extractive body cue:** In evaluation, we set thd = 1 cm, thα = 5 degree and K = 10.
- **p. 5 / 4.1. Ground-Truth Evaluation - extractive body cue:** Object s=1 s=0.5 s=0.1 Object s=1 s=0.5 s=0.1 Banana 98% 67% 21% Apple 97% 65% 16% Peeler 95% 59% 9% Dragon 96% 60% 9% Mug ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The previous method that pre-computed ground truth for evaluating grasping, no matter collected by human annotation [11] or simulation [7], cannot cover all feasible ... | p. 5 (3.5. Discussion) |
| body limitation/failure cue | Such evaluation method does not assume the representation of the grasp pose, thus is general in practice. | p. 5 (3.5. Discussion) |
| body limitation/failure cue | Collision detection is also conducted to avoid the collision between grasps and background or other object. where Pj i is the 6D pose of ... | p. 3 (3.3. Data Annotation) |
| body limitation/failure cue | The 6D poses will then be propagated to the remaining frames by: Pj i = cam-1 i cam0Pj 0, (1) Gripper Depth Sampling Grasp ... | p. 3 (3.3. Data Annotation) |
| body limitation/failure cue | Figure 1. Our methodology for building the dataset. We collect data with real-world sensors and annotate grasp poses for every single object by analytic ... | p. 1 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To avoid dominated by similar grasp poses or grasp poses from single object, we run a pose-NMS before eval | p. 4 (3.4. Evaluation) |
| Summary of real world success rate of grasping given different grasp score. grasp poses to the camera frame using objects' 6D poses, we paste ... | p. 5 (4.1. Ground-Truth Evaluation) |
| Our dataset, source code and models will be made publicly available. | p. 1 (Abstract) |
| Object grasping is critical for many applications, which is also a challenging computer vision problem. | p. 1 (Abstract) |
| The result is computed based on physical rules, which is robust. | p. 4 (2 Cams) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 3.5. Discussion - extractive body cue:** The previous method that pre-computed ground truth for evaluating grasping, no matter collected by human annotation [11] or simulation [7], cannot cover all feasible solution.
- **p. 5 / 3.5. Discussion - extractive body cue:** Such evaluation method does not assume the representation of the grasp pose, thus is general in practice.
- **p. 3 / 3.3. Data Annotation - extractive body cue:** Collision detection is also conducted to avoid the collision between grasps and background or other object. where Pj i is the 6D pose of object ...
- **p. 3 / 3.3. Data Annotation - extractive body cue:** The 6D poses will then be propagated to the remaining frames by: Pj i = cam-1 i cam0Pj 0, (1) Gripper Depth Sampling Grasp View ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Our methodology for building the dataset. We collect data with real-world sensors and annotate grasp poses for every single object by analytic computation. ...

- **PDF anchors reviewed:** datasets p. 4 (3.4. Evaluation), p. 4 (3.4. Evaluation), p. 5 (4. Experiments), p. 2 (3.2. Data Collection), p. 2 (3.1. Overview), p. 3 (3.2. Data Collection), metrics p. 5 (4.1. Ground-Truth Evaluation), p. 4 (3.4. Evaluation), p. 5 (3.4. Evaluation), p. 4 (3.4. Evaluation), p. 3 (Figure/Table caption), p. 2 (3.1. Overview), baselines 본문 anchor 없음, results p. 5 (4.1. Ground-Truth Evaluation), p. 4 (3.4. Evaluation), p. 3 (3.3. Data Annotation), p. 4 (3.4. Evaluation), p. 5 (4.1. Ground-Truth Evaluation), p. 3 (3.3. Data Annotation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
