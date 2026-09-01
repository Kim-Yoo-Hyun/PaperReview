# Evaluation - ORB-SLAM: A Versatile and Accurate Monocular SLAM System

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1502.00956; PDF retrieval source: https://arxiv.org/pdf/1502.00956. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (VIII. EXPERIMENTS), p. 15 (VIII. EXPERIMENTS), p. 15 (VIII. EXPERIMENTS), p. 14 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 11 (VIII. EXPERIMENTS)): In terms of accuracy ORB-SLAM and PTAM are similar in open trajectories, while ORB-SLAM achieves higher accuracy when detecting large loops as in the sequence fr3 nostructure texture near withloop ...

## Evaluation Body Digest

- **p. 9 / VIII. EXPERIMENTS - extractive PDF cue:** We have performed an extensive experimental validation of our system in the large robot sequence of NewCollege [39], evaluating the general performance of the system, ...
- **p. 12 / VIII. EXPERIMENTS - extractive PDF cue:** IEEE TRANSACTIONS ON ROBOTICS 11 TABLE III KEYFRAME LOCALIZATION ERROR COMPARISON IN THE TUM RGB-D BENCHMARK [38] Absolute KeyFrame Trajectory RMSE (cm) ORB-SLAM PTAM LSD-SLAM ...
- **p. 9 / VIII. EXPERIMENTS - extractive PDF cue:** System Performance in the NewCollege Dataset The NewCollege dataset [39] contains a 2.2km sequence from a robot traversing a campus and adjacent parks.
- **p. 11 / VIII. EXPERIMENTS - extractive PDF cue:** Localization Accuracy in the TUM RGB-D Benchmark The TUM RGB-D benchmark [38] is an excellent dataset to evaluate the accuracy of camera localization as it ...
- **p. 13 / VIII. EXPERIMENTS - extractive PDF cue:** Large Scale and Large Loop Closing in the KITTI Dataset The odometry benchmark from the KITTI dataset [40] contains 11 sequences from a car driven ...
- **p. 14 / VIII. EXPERIMENTS - extractive PDF cue:** ORB-SLAM keyframe trajectories in sequences 02, 03, 04 ,06, 08, 09 and 10 from the odometry benchmark of the KITTI dataset.
- **p. 15 / VIII. EXPERIMENTS - extractive PDF cue:** IEEE TRANSACTIONS ON ROBOTICS 14 TABLE V RESULTS OF OUR SYSTEM IN THE KITTI DATASET.
- **p. 13 / VIII. EXPERIMENTS - extractive PDF cue:** Lifelong experiment in a dynamic environment from the TUM RGBD Benchmark. were correctly detected and closed by our system.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** VIII. EXPERIMENTS (p. 9).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| VIII. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | In terms of accuracy ORB-SLAM and PTAM are similar in open trajectories, while ORB-SLAM achieves higher accuracy when detecting large loops as in the ... | p. 11 (VIII. EXPERIMENTS) |
| VIII. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Performing an additional BA after the pose graph optimization slightly improves the accuracy while increasing substantially the time. | p. 15 (VIII. EXPERIMENTS) |
| VIII. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We have noticed that some iterations of full BA slightly improves the accuracy in the trajectories with loops but it has negligible effect in ... | p. 15 (VIII. EXPERIMENTS) |
| VIII. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The output of our system is quite accurate, while it can be slightly improved with some iterations of BA. -100 0 100 200 300 ... | p. 14 (VIII. EXPERIMENTS) |
| VIII. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We have performed an extensive experimental validation of our system in the large robot sequence of NewCollege [39], evaluating the general performance of the ... | p. 9 (VIII. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 9 / VIII. EXPERIMENTS - extractive PDF cue:** We have performed an extensive experimental validation of our system in the large robot sequence of NewCollege [39], evaluating the general performance of the system, ...
- **p. 12 / VIII. EXPERIMENTS - extractive PDF cue:** IEEE TRANSACTIONS ON ROBOTICS 11 TABLE III KEYFRAME LOCALIZATION ERROR COMPARISON IN THE TUM RGB-D BENCHMARK [38] Absolute KeyFrame Trajectory RMSE (cm) ORB-SLAM PTAM LSD-SLAM ...
- **p. 9 / VIII. EXPERIMENTS - extractive PDF cue:** System Performance in the NewCollege Dataset The NewCollege dataset [39] contains a 2.2km sequence from a robot traversing a campus and adjacent parks.
- **p. 11 / VIII. EXPERIMENTS - extractive PDF cue:** Localization Accuracy in the TUM RGB-D Benchmark The TUM RGB-D benchmark [38] is an excellent dataset to evaluate the accuracy of camera localization as it ...
- **p. 13 / VIII. EXPERIMENTS - extractive PDF cue:** Large Scale and Large Loop Closing in the KITTI Dataset The odometry benchmark from the KITTI dataset [40] contains 11 sequences from a car driven ...
- **p. 14 / VIII. EXPERIMENTS - extractive PDF cue:** ORB-SLAM keyframe trajectories in sequences 02, 03, 04 ,06, 08, 09 and 10 from the odometry benchmark of the KITTI dataset.
- **p. 15 / VIII. EXPERIMENTS - extractive PDF cue:** IEEE TRANSACTIONS ON ROBOTICS 14 TABLE V RESULTS OF OUR SYSTEM IN THE KITTI DATASET.
- **p. 13 / VIII. EXPERIMENTS - extractive PDF cue:** Lifelong experiment in a dynamic environment from the TUM RGBD Benchmark. were correctly detected and closed by our system.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 1. ORB-SLAM system overview, showing all the steps performed by the tracking, local mapping and loop closing threads. The main components of the place ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 2. Reconstruction and graphs in the sequence fr3 long office household from the TUM RGB-D Benchmark [38]. • The camera intrinsics, including focal length ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 3. Top: PTAM, middle LSD-SLAM, bottom: ORB-SLAM, some time after initialization in the NewCollege sequence [39]. PTAM and LSD-SLAM initialize a corrupted planar solution ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 4. Example of loop detected in the NewCollege sequence. We draw the inlier correspondences supporting the similarity transformation found. loops and work in large ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 5. Map before and after a loop closure in the NewCollege sequence. The loop closure match is drawn in blue, the trajectory in green, ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Fig. 6. ORB-SLAM reconstruction of the full sequence of NewCollege. The bigger loop on the right is traversed in opposite directions and not visual loop ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Fig. 7. Relocalization experiment in fr2 xyz. Map is initially created during the first 30 seconds of the sequence (KFs). The goal is to relocalize ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Fig. 8. Example of challenging relocalizations (severe scale change, dynamic objects) that our system successfully found in the relocalization experiments. walking xyz, walking halfspehere and ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We have performed an extensive experimental validation of our system in the large robot sequence of NewCollege [39], evaluating the general performance of the ... | embodiment, simulator version and control stack | p. 9 (VIII. EXPERIMENTS), p. 12 (VIII. EXPERIMENTS) |
| Task/environment | IEEE TRANSACTIONS ON ROBOTICS 11 TABLE III KEYFRAME LOCALIZATION ERROR COMPARISON IN THE TUM RGB-D BENCHMARK [38] Absolute KeyFrame Trajectory RMSE (cm) ORB-SLAM PTAM ... | reset, timeout, object/scene variation | p. 12 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 6 (III. SYSTEM OVERVIEW), p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (III. SYSTEM OVERVIEW), p. 5 (III. SYSTEM OVERVIEW) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In the first experiment we build a map with the first 30 seconds of the sequence fr2 xyz and perform global relocalization with every ... | definition/direction/unit from same section | p. 11 (VIII. EXPERIMENTS) |
| We have performed an extensive experimental validation of our system in the large robot sequence of NewCollege [39], evaluating the general performance of the ... | definition/direction/unit from same section | p. 9 (VIII. EXPERIMENTS) |
| Localization Accuracy in the TUM RGB-D Benchmark The TUM RGB-D benchmark [38] is an excellent dataset to evaluate the accuracy of camera localization as ... | definition/direction/unit from same section | p. 11 (VIII. EXPERIMENTS) |
| We have noticed that some iterations of full BA slightly improves the accuracy in the trajectories with loops but it has negligible effect in ... | definition/direction/unit from same section | p. 15 (VIII. EXPERIMENTS) |
| IEEE TRANSACTIONS ON ROBOTICS 11 TABLE III KEYFRAME LOCALIZATION ERROR COMPARISON IN THE TUM RGB-D BENCHMARK [38] Absolute KeyFrame Trajectory RMSE (cm) ORB-SLAM PTAM ... | definition/direction/unit from same section | p. 12 (VIII. EXPERIMENTS) |
| We also provide the dimensions of the maps to put in context the errors. | definition/direction/unit from same section | p. 13 (VIII. EXPERIMENTS) |
| Even after 100 iterations still the error is very high. | definition/direction/unit from same section | p. 15 (VIII. EXPERIMENTS) |
| The whole map after processing the full sequence at its real frame-rate is shown in Fig. | definition/direction/unit from same section | p. 10 (VIII. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We perform the same experiment with PTAM for comparison. | comparison identity and matched condition | p. 11 (VIII. EXPERIMENTS) |
| For comparison we have also executed the novel, direct, semi-dense LSD-SLAM [10] and PTAM [4] in the benchmark. | comparison identity and matched condition | p. 11 (VIII. EXPERIMENTS) |
| IEEE TRANSACTIONS ON ROBOTICS 11 TABLE III KEYFRAME LOCALIZATION ERROR COMPARISON IN THE TUM RGB-D BENCHMARK [38] Absolute KeyFrame Trajectory RMSE (cm) ORB-SLAM PTAM ... | comparison identity and matched condition | p. 12 (VIII. EXPERIMENTS) |
| Qualitative comparisons of our trajectories and the ground truth are shown in Fig. | comparison identity and matched condition | p. 13 (VIII. EXPERIMENTS) |
| Comparison of different loop closing strategies in KITTI 09. | comparison identity and matched condition | p. 15 (VIII. EXPERIMENTS) |
| In table VI we show the keyframe trajectory RMSE and the time spent in the optimization in different cases: without loop closing, if we ... | comparison identity and matched condition | p. 15 (VIII. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In table VI we show the keyframe trajectory RMSE and the time spent in the optimization in different cases: without loop closing, if we ... | component/input/data sensitivity | p. 15 (VIII. EXPERIMENTS) |
| 100 0 100 200 300 x [m] 200 100 0 100 200 300 400 500 600 y [m] Ground truth Estimated (a) Without Loop ... | component/input/data sensitivity | p. 15 (VIII. EXPERIMENTS) |
| Fig. 1. ORB-SLAM system overview, showing all the steps performed by the tracking, local mapping and loop closing threads. The main components of the ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work we build on the main ideas of PTAM, the place recognition work of G´alvez-L´opez and Tard´os [5], the scale-aware loop closing ... | In terms of accuracy ORB-SLAM and PTAM are similar in open trajectories, while ORB-SLAM achieves higher accuracy when detecting large loops as in the ... | PDF body cue; verify exact table/figure and matched conditions | p. 11 (VIII. EXPERIMENTS), p. 15 (VIII. EXPERIMENTS), p. 15 (VIII. EXPERIMENTS), p. 14 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 11 (VIII. EXPERIMENTS) |
| Primary metric/result | Performing an additional BA after the pose graph optimization slightly improves the accuracy while increasing substantially the time. | numeric claim only at cited anchor | p. 15 (VIII. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 9 / VIII. EXPERIMENTS - extractive PDF cue:** The sequence is recorded by a stereo camera at 20 fps and a resolution 512×382.
- **p. 10 / VIII. EXPERIMENTS - extractive PDF cue:** Tracking works at frame-rates around 25-30Hz, being the most demanding task to track the local map.
- **p. 12 / VIII. EXPERIMENTS - extractive PDF cue:** IEEE TRANSACTIONS ON ROBOTICS 11 TABLE III KEYFRAME LOCALIZATION ERROR COMPARISON IN THE TUM RGB-D BENCHMARK [38] Absolute KeyFrame Trajectory RMSE (cm) ORB-SLAM PTAM LSD-SLAM ...
- **p. 13 / VIII. EXPERIMENTS - extractive PDF cue:** 2769 frames to relocalize PTAM 37 0.19 34.9 0.26 1.52 ORB-SLAM 24 0.19 78.4 0.38 1.67 fr3 walking xyz.
- **p. 13 / VIII. EXPERIMENTS - extractive PDF cue:** 859 frames to relocalize PTAM 34 0.83 0.0 - - ORB-SLAM 31 0.82 77.9 1.32 4.95 0 10 20 30 40 50 60 70 80 ...
- **p. 13 / VIII. EXPERIMENTS - extractive PDF cue:** This is a very challenging dataset for monocular vision due to fast rotations, areas with lot of foliage, which make more difficult data association, and ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, direct methods have their own limitations. | p. 16 (IX. CONCLUSIONS AND DISCUSSION) |
| body limitation/failure cue | Future Work The accuracy of our system can still be improved incorporating points at infinity in the tracking. | p. 16 (IX. CONCLUSIONS AND DISCUSSION) |
| body limitation/failure cue | In sequence 08 there are no loops and drift cannot be corrected, which makes clear the need of loop closures to achieve accurate reconstructions. | p. 15 (VIII. EXPERIMENTS) |
| body limitation/failure cue | The big loop on the right does not perfectly align because it was traversed in opposite directions and the place recognizer was not able ... | p. 10 (VIII. EXPERIMENTS) |
| body limitation/failure cue | However, the paper does not give enough details on how those results were obtained, and we have been unable to reproduce them. | p. 11 (VIII. EXPERIMENTS) |
| body limitation/failure cue | During the sequences sitting rpy and walking xyz the map does not grow, because the map created so far explains well the scene. | p. 12 (VIII. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| ORB-SLAM has three main threads, that run in parallel with other tasks from ROS and the operating system, which introduces some randomness in the ... | p. 9 (VIII. EXPERIMENTS) |
| For the benefit of the community, we make the source code public. | p. 2 (Abstract) |
| Demonstration videos and the code can be found in our project webpage1. | p. 3 (B UNDLE ADJUSTMENT (BA) is known to provide ac) |
| 1, incorporates three threads that run in parallel: tracking, local mapping and loop | p. 4 (III. SYSTEM OVERVIEW) |
| They are extremely fast to compute and match, while they have good invariance to viewpoint. | p. 4 (III. SYSTEM OVERVIEW) |
| We explain in detail all local mapping steps in Section VI. | p. 5 (III. SYSTEM OVERVIEW) |
| All the tracking steps are explained in detail in Section V. | p. 5 (III. SYSTEM OVERVIEW) |
| The goal of the map initialization is to compute the relative pose between two frames to triangulate an initial set of map points. | p. 6 (IV. AUTOMATIC MAP INITIALIZATION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 16 / IX. CONCLUSIONS AND DISCUSSION - extractive PDF cue:** However, direct methods have their own limitations.
- **p. 16 / IX. CONCLUSIONS AND DISCUSSION - extractive PDF cue:** Future Work The accuracy of our system can still be improved incorporating points at infinity in the tracking.
- **p. 15 / VIII. EXPERIMENTS - extractive PDF cue:** In sequence 08 there are no loops and drift cannot be corrected, which makes clear the need of loop closures to achieve accurate reconstructions.
- **p. 10 / VIII. EXPERIMENTS - extractive PDF cue:** The big loop on the right does not perfectly align because it was traversed in opposite directions and the place recognizer was not able to ...
- **p. 11 / VIII. EXPERIMENTS - extractive PDF cue:** However, the paper does not give enough details on how those results were obtained, and we have been unable to reproduce them.
- **p. 12 / VIII. EXPERIMENTS - extractive PDF cue:** During the sequences sitting rpy and walking xyz the map does not grow, because the map created so far explains well the scene.

- **PDF anchors reviewed:** datasets p. 9 (VIII. EXPERIMENTS), p. 12 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 11 (VIII. EXPERIMENTS), p. 13 (VIII. EXPERIMENTS), p. 14 (VIII. EXPERIMENTS), metrics p. 11 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 11 (VIII. EXPERIMENTS), p. 15 (VIII. EXPERIMENTS), p. 12 (VIII. EXPERIMENTS), p. 13 (VIII. EXPERIMENTS), baselines p. 11 (VIII. EXPERIMENTS), p. 11 (VIII. EXPERIMENTS), p. 12 (VIII. EXPERIMENTS), p. 13 (VIII. EXPERIMENTS), p. 15 (VIII. EXPERIMENTS), p. 15 (VIII. EXPERIMENTS), results p. 11 (VIII. EXPERIMENTS), p. 15 (VIII. EXPERIMENTS), p. 15 (VIII. EXPERIMENTS), p. 14 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 11 (VIII. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
