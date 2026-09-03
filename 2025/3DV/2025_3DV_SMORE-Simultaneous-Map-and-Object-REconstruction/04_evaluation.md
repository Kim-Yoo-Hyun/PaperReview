# Evaluation - SMORE: Simultaneous Map and Object REconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=1NhnG9BvQB&name=pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 2 (Figure/Table caption), p. 8 (6. Qualitative Results), p. 6 (5.1. Lidar Novel View Synthesis), p. 7 (5.1. Lidar Novel View Synthesis), p. 7 (5.1. Lidar Novel View Synthesis), p. 8 (6. Qualitative Results)): Figure 2. Dynamic object reconstructions using human-annotated bounding-box annotations (top left) tend to be noisy. Optimizing over object pose (top right) improves accuracy, while de-skewing scans to account for dynamic ...

## Evaluation Body Digest

- **p. 5 / 5. Experiments - extractive body cue:** Datasets: All of our experiments are conducted on nuScenes[3] and Argoverse 2.0[42].
- **p. 6 / 5. Experiments - extractive body cue:** Interestingly, our approach is even more effective for recent AV datasets [30, 42] that employ multiple spinning lidars, which are often set to be out-of-phase ...
- **p. 7 / 5.2. Pose Estimation - extractive body cue:** (Left) Each column shows nuScenes and Argoverse object reconstructions using ground truth poses compared to (right) ours.
- **p. 5 / 5. Experiments - extractive body cue:** We focus primarily on nuScenes as its noisy annotations and sparse LiDAR present the greatest challenge to accurate geometry recovery.
- **p. 6 / 5. Experiments - extractive body cue:** Here, we visualize the set of rays captured at a time instant (blue lines) for NuScenes (top) and Argoverse [42] (bottom).
- **p. 8 / 6. Qualitative Results - extractive body cue:** Pose accuracy evaluation on nuScenes (using NuScene's default ATE metric), measured by comparing the bounding box locations predicted by our method to held-out ground truth ...
- **p. 7 / 6. Qualitative Results - extractive body cue:** Visualizations of our foreground reconstructions on nuScenes and Argoverse are shown in Fig.
- **p. 8 / 6. Qualitative Results - extractive body cue:** Background reconstructions from nuScenes and Argoverse are shown in Fig.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 5); 6. Qualitative Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 2. Dynamic object reconstructions using human-annotated bounding-box annotations (top left) tend to be noisy. Optimizing over object pose (top right) improves accuracy, while ... | p. 2 (Figure/Table caption) |
| 6. Qualitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2, we show how accounting for this distortion can significantly improve the reconstructions. | p. 8 (6. Qualitative Results) |
| 5.1. Lidar Novel View Synthesis | EMPIRICAL / SOURCE-REPORTED EVALUATION | We follow [49] and let each method use the test pose that achieves the lowest error. | p. 6 (5.1. Lidar Novel View Synthesis) |
| 5.1. Lidar Novel View Synthesis | EMPIRICAL / SOURCE-REPORTED EVALUATION | 3, we see that SMORE outperforms NeuRAD by order of magnitude in both chamfer distance and median depth error. | p. 7 (5.1. Lidar Novel View Synthesis) |
| 5.1. Lidar Novel View Synthesis | EMPIRICAL / SOURCE-REPORTED EVALUATION | This is the case even when NeuRAD is given the final optimized poses from our method, which we note do outperform the poses found ... | p. 7 (5.1. Lidar Novel View Synthesis) |

## Dataset / Benchmark Role

- **p. 5 / 5. Experiments - extractive body cue:** Datasets: All of our experiments are conducted on nuScenes[3] and Argoverse 2.0[42].
- **p. 6 / 5. Experiments - extractive body cue:** Interestingly, our approach is even more effective for recent AV datasets [30, 42] that employ multiple spinning lidars, which are often set to be out-of-phase ...
- **p. 7 / 5.2. Pose Estimation - extractive body cue:** (Left) Each column shows nuScenes and Argoverse object reconstructions using ground truth poses compared to (right) ours.
- **p. 5 / 5. Experiments - extractive body cue:** We focus primarily on nuScenes as its noisy annotations and sparse LiDAR present the greatest challenge to accurate geometry recovery.
- **p. 6 / 5. Experiments - extractive body cue:** Here, we visualize the set of rays captured at a time instant (blue lines) for NuScenes (top) and Argoverse [42] (bottom).
- **p. 8 / 6. Qualitative Results - extractive body cue:** Pose accuracy evaluation on nuScenes (using NuScene's default ATE metric), measured by comparing the bounding box locations predicted by our method to held-out ground truth ...
- **p. 7 / 6. Qualitative Results - extractive body cue:** Visualizations of our foreground reconstructions on nuScenes and Argoverse are shown in Fig.
- **p. 8 / 6. Qualitative Results - extractive body cue:** Background reconstructions from nuScenes and Argoverse are shown in Fig.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. NuScenes surface reconstruction produced by aggregating LiDAR scans using human-annotated ego-pose and dynamic object bounding boxes (left). We introduce a global optimization that ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Dynamic object reconstructions using human-annotated bounding-box annotations (top left) tend to be noisy. Optimizing over object pose (top right) improves accuracy, while de-skewing ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Depth maps produced by our method (left) as compared to those from a SOTA NeRF-based method[33] (right). In the top row we see ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. (Left) A LiDAR sweep where each point has been col- ored according to which laser it belongs to (hue) and the time within ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. LiDAR is often abstracted as 360-degree sweeps captured with a global shutter, but is actually captured with a continuous rotating shutter from a ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. (Left) Each column shows nuScenes and Argoverse ob- ject reconstructions using ground truth poses compared to (right) ours.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7. Examples of the synthesized point clouds from our method (left) versus NeuRAD [33] (right). Ground truth is shown in blue and the predicted ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1. Evaluation of our method's robustness to actor annotation errors (subsampling or real tracks). We measure reconstruction accuracy using the nearest-neighbor distance between the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Datasets: All of our experiments are conducted on nuScenes[3] and Argoverse 2.0[42]. | embodiment, simulator version and control stack | p. 5 (5. Experiments), p. 6 (5. Experiments) |
| Task/environment | Interestingly, our approach is even more effective for recent AV datasets [30, 42] that employ multiple spinning lidars, which are often set to be ... | reset, timeout, object/scene variation | p. 6 (5. Experiments), p. 7 (5.2. Pose Estimation) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3. Problem Statement), p. 3 (3. Problem Statement) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (4.4. What is a LiDAR sweep?), p. 4 (3. Problem Statement) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report the average distance and two accuracy metrics to characterize the distribution of errors. | definition/direction/unit from same section | p. 8 (6. Qualitative Results) |
| Table 2. Pose accuracy evaluation on nuScenes (using NuScene's default ATE metric), measured by comparing the bounding box locations predicted by our method to ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| We compare our method and NeuRAD[33] on this task by evaluating the chamfer distance and median L2 distance error between the synthesized point cloud ... | definition/direction/unit from same section | p. 6 (5.1. Lidar Novel View Synthesis) |
| 1 further confirm the robustness of our method to input annotation errors. | definition/direction/unit from same section | p. 7 (5.2. Pose Estimation) |
| 3, we see that SMORE outperforms NeuRAD by order of magnitude in both chamfer distance and median depth error. | definition/direction/unit from same section | p. 7 (5.1. Lidar Novel View Synthesis) |
| Figure 2. Dynamic object reconstructions using human-annotated bounding-box annotations (top left) tend to be noisy. Optimizing over object pose (top right) improves accuracy, while ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| We follow [49] and let each method use the test pose that achieves the lowest error. | definition/direction/unit from same section | p. 6 (5.1. Lidar Novel View Synthesis) |
| Figure 1. NuScenes surface reconstruction produced by aggregating LiDAR scans using human-annotated ego-pose and dynamic object bounding boxes (left). We introduce a global optimization ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| However, the comparison is with a state-of-the-art LiDAR odometry method instead of the ground truth since we find odometry is generally superior. | comparison identity and matched condition | p. 8 (6. Qualitative Results) |
| 3, we see that SMORE outperforms NeuRAD by order of magnitude in both chamfer distance and median depth error. | comparison identity and matched condition | p. 7 (5.1. Lidar Novel View Synthesis) |
| (Left) Each column shows nuScenes and Argoverse object reconstructions using ground truth poses compared to (right) ours. | comparison identity and matched condition | p. 7 (5.2. Pose Estimation) |
| Figure 3. Depth maps produced by our method (left) as compared to those from a SOTA NeRF-based method[33] (right). In the top row we ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| Table 3. Our reconstructions sigificantly outperform the state-of- the-art in LiDAR Novel View Synthesis [33] in terms of chamfer distance (m2) and median depth ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 5. LiDAR Novel View Synthesis on more scenes from NuScenes. SMORE consistently outperforms NeuRAD across a variety of scenes by an order of ... | comparison identity and matched condition | p. 12 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| An example of the depth maps produced by our method is shown in Fig. | Figure 2. Dynamic object reconstructions using human-annotated bounding-box annotations (top left) tend to be noisy. Optimizing over object pose (top right) improves accuracy, while ... | PDF body cue; verify exact table/figure and matched conditions | p. 2 (Figure/Table caption), p. 8 (6. Qualitative Results), p. 6 (5.1. Lidar Novel View Synthesis), p. 7 (5.1. Lidar Novel View Synthesis), p. 7 (5.1. Lidar Novel View Synthesis), p. 8 (6. Qualitative Results) |
| Primary metric/result | 2, we show how accounting for this distortion can significantly improve the reconstructions. | numeric claim only at cited anchor | p. 8 (6. Qualitative Results) |

- Numeric sentences retained from the body:
- **p. 6 / 5.1. Lidar Novel View Synthesis - extractive body cue:** Iterations are stopped if the mean registration error for an object falls below 1 centimeter for three consecutive iterations.
- **p. 8 / 6. Qualitative Results - extractive body cue:** NN Dist (m) ↓Acc Relax ↑Acc Strict ↑ NKSR[12] + GT tracks 0.071 0.9 0.76 NKSR[12] + LT3D[27] 0.071 0.9 0.76 Ours + GT tracks ...
- **p. 8 / 6. Qualitative Results - extractive body cue:** Specifically, we compute the percent of points less than 10cm and 5cm for the relaxed and strict metrics, respectively Annotation Rate 1Hz 0.5Hz 0.25Hz Interpolation ...
- **p. 8 / 6. Qualitative Results - extractive body cue:** Pose accuracy evaluation on nuScenes (using NuScene's default ATE metric), measured by comparing the bounding box locations predicted by our method to held-out ground truth ...
- **p. 4 / 4.2. Optimize surfaces - extractive body cue:** First, we use the fact the distance is unaffected by a global rigid transformation to see that D(TM, X) = D(M, T-1X).
- **p. 4 / 4.4. What is a LiDAR sweep? - extractive body cue:** Instead, they rotate continuously and measure depth across 16-128 vertically arranged lasers, typically taking 100ms to complete a 360-degree rotation.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Iterations are stopped if the mean registration error for an object falls below 1 centimeter for three consecutive iterations. | p. 6 (5.1. Lidar Novel View Synthesis) |
| body limitation/failure cue | Figure 1. NuScenes surface reconstruction produced by aggregating LiDAR scans using human-annotated ego-pose and dynamic object bounding boxes (left). We introduce a global optimization ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Interestingly, our approach is even more effective for recent AV datasets [30, 42] that employ multiple spinning lidars, which are often set to be ... | p. 6 (5. Experiments) |
| body limitation/failure cue | For testing, however, the reference implementation does not support optimizing new poses that were not present at train time. | p. 7 (5.1. Lidar Novel View Synthesis) |
| body limitation/failure cue | We focus primarily on nuScenes as its noisy annotations and sparse LiDAR present the greatest challenge to accurate geometry recovery. | p. 5 (5. Experiments) |
| body limitation/failure cue | 1 further confirm the robustness of our method to input annotation errors. | p. 7 (5.2. Pose Estimation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| SMORE Details: We run the SMORE optimization on the training views to obtain reconstructed meshes for objects and the background. | p. 6 (5.1. Lidar Novel View Synthesis) |
| We then run 100 refinement iterations on all objects and background maps, with early stopping criteria to avoid wasted computation. | p. 6 (5.1. Lidar Novel View Synthesis) |
| To test this, we run our method with annotations taken at various sample rates. | p. 7 (5.2. Pose Estimation) |
| We compute this metric over the nine test sequences and filter out objects that follow linear trajectories. | p. 7 (5.2. Pose Estimation) |
| We can now derive the pose and surface optimization steps. | p. 4 (4.1. Decomposition) |
| Specifically, we compute the percent of points less than 10cm and 5cm for the relaxed and strict metrics, respectively Annotation Rate 1Hz 0.5Hz 0.25Hz ... | p. 8 (6. Qualitative Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 5.1. Lidar Novel View Synthesis - extractive body cue:** Iterations are stopped if the mean registration error for an object falls below 1 centimeter for three consecutive iterations.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. NuScenes surface reconstruction produced by aggregating LiDAR scans using human-annotated ego-pose and dynamic object bounding boxes (left). We introduce a global optimization that ...
- **p. 6 / 5. Experiments - extractive body cue:** Interestingly, our approach is even more effective for recent AV datasets [30, 42] that employ multiple spinning lidars, which are often set to be out-of-phase ...
- **p. 7 / 5.1. Lidar Novel View Synthesis - extractive body cue:** For testing, however, the reference implementation does not support optimizing new poses that were not present at train time.
- **p. 5 / 5. Experiments - extractive body cue:** We focus primarily on nuScenes as its noisy annotations and sparse LiDAR present the greatest challenge to accurate geometry recovery.
- **p. 7 / 5.2. Pose Estimation - extractive body cue:** 1 further confirm the robustness of our method to input annotation errors.

- **Evidence anchors reviewed:** datasets p. 5 (5. Experiments), p. 6 (5. Experiments), p. 7 (5.2. Pose Estimation), p. 5 (5. Experiments), p. 6 (5. Experiments), p. 8 (6. Qualitative Results), metrics p. 8 (6. Qualitative Results), p. 8 (Figure/Table caption), p. 6 (5.1. Lidar Novel View Synthesis), p. 7 (5.2. Pose Estimation), p. 7 (5.1. Lidar Novel View Synthesis), p. 2 (Figure/Table caption), baselines p. 8 (6. Qualitative Results), p. 7 (5.1. Lidar Novel View Synthesis), p. 7 (5.2. Pose Estimation), p. 3 (Figure/Table caption), p. 8 (Figure/Table caption), p. 12 (Figure/Table caption), results p. 2 (Figure/Table caption), p. 8 (6. Qualitative Results), p. 6 (5.1. Lidar Novel View Synthesis), p. 7 (5.1. Lidar Novel View Synthesis), p. 7 (5.1. Lidar Novel View Synthesis), p. 8 (6. Qualitative Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
