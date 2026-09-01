# Evaluation - Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2403.02751; PDF retrieval source: https://arxiv.org/pdf/2403.02751. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (VI. EXPERIMENTS), p. 13 (VI. EXPERIMENTS), p. 11 (VI. EXPERIMENTS), p. 13 (VI. EXPERIMENTS), p. 14 (VI. EXPERIMENTS), p. 16 (Figure/Table caption)): However, Splat-Loc-SIFT achieves a lower success rate, compared to Splat-Loc-Glue, which achieves a perfect success rate.

## Evaluation Body Digest

- **p. 10 / VI. EXPERIMENTS - extractive body cue:** Simulation Results 1) Test Environments: We benchmark Splat-Plan and SplatLoc independently on four different environments: Stonehenge, a fully-synthetic scene, and three real-world scenes Statues, Flightroom, ...
- **p. 10 / VI. EXPERIMENTS - extractive body cue:** We demonstrate the effectiveness of our navigation pipeline for GSplat maps, examining its performance in real-world scenes on hardware and in simulation.
- **p. 11 / VI. EXPERIMENTS - extractive body cue:** In the simulated tests, we represent the robot using balls of various sizes in order to generate interesting trajectories due to the fact that the ...
- **p. 12 / VI. EXPERIMENTS - extractive body cue:** In the hardware tests, we approximate the robot using a sphere with diameter 0.5 m.
- **p. 12 / VI. EXPERIMENTS - extractive body cue:** Unfortunately, because many of these scenes were captured in the real-world, no ground-truth mesh exists.
- **p. 11 / VI. EXPERIMENTS - extractive body cue:** We disable this feature for the hardware Maze scene.
- **p. 13 / VI. EXPERIMENTS - extractive body cue:** 6) Splat-Loc Evaluations: We validate the performance of Splat-Loc in hardware experiments in the Maze scene, showing that Splat-Loc achieves relatively the same level of ...
- **p. 13 / VI. EXPERIMENTS - extractive body cue:** Our hardware tests consist of all combinations of goal locations and control schemes.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** VI. EXPERIMENTS (p. 10).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| VI. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | However, Splat-Loc-SIFT achieves a lower success rate, compared to Splat-Loc-Glue, which achieves a perfect success rate. | p. 11 (VI. EXPERIMENTS) |
| VI. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 6) Splat-Loc Evaluations: We validate the performance of Splat-Loc in hardware experiments in the Maze scene, showing that Splat-Loc achieves relatively the same level ... | p. 13 (VI. EXPERIMENTS) |
| VI. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The GS-Loc algorithm achieves the lowest accuracy and requires the greatest computation time, unlike Colored-ICP, Splat-Loc-SIFT, and Splat-Loc-Glue, which achieve much-higher accuracy with a ... | p. 11 (VI. EXPERIMENTS) |
| VI. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Essentially, all the pose estimators achieve comparable estimation accuracy. | p. 13 (VI. EXPERIMENTS) |
| VI. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Splat-Plan displays competitive non-conservativeness and computation time, while exhibiting superior safety and success rates. | p. 14 (VI. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 10 / VI. EXPERIMENTS - extractive body cue:** Simulation Results 1) Test Environments: We benchmark Splat-Plan and SplatLoc independently on four different environments: Stonehenge, a fully-synthetic scene, and three real-world scenes Statues, Flightroom, ...
- **p. 10 / VI. EXPERIMENTS - extractive body cue:** We demonstrate the effectiveness of our navigation pipeline for GSplat maps, examining its performance in real-world scenes on hardware and in simulation.
- **p. 11 / VI. EXPERIMENTS - extractive body cue:** In the simulated tests, we represent the robot using balls of various sizes in order to generate interesting trajectories due to the fact that the ...
- **p. 12 / VI. EXPERIMENTS - extractive body cue:** In the hardware tests, we approximate the robot using a sphere with diameter 0.5 m.
- **p. 12 / VI. EXPERIMENTS - extractive body cue:** Unfortunately, because many of these scenes were captured in the real-world, no ground-truth mesh exists.
- **p. 11 / VI. EXPERIMENTS - extractive body cue:** We disable this feature for the hardware Maze scene.
- **p. 13 / VI. EXPERIMENTS - extractive body cue:** 6) Splat-Loc Evaluations: We validate the performance of Splat-Loc in hardware experiments in the Maze scene, showing that Splat-Loc achieves relatively the same level of ...
- **p. 13 / VI. EXPERIMENTS - extractive body cue:** Our hardware tests consist of all combinations of goal locations and control schemes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Splat-Nav, consists of a safe planning module, Splat-Plan, and robust localization module, Splat-Loc, both operating on a Gaussian Splatting environment representation. In Splat-Plan ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Visualization of a point cloud from a NeRF and a mesh from a Gaussian Splat in the synthetic scene Stonehenge. The Chamfer Distance ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 3: Splat-Plan, as described by Algorithm 2. Given a GSplat and its corresponding ellipsoidal collision geometry, Splat-Plan generates a binary occupancy grid representing the ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 4: Qualitative results of 100 safe trajectories using Splat-Plan with start (blue) and goal (red) states spread over a circle. We see that the ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 5: A comparison of trajectories generated by Splat-Plan and four variants of SFC [13] for the same 100 start and end locations for each ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 6: A comparison of trajectories generated by Splat-Plan, SFC [13], RRT*, and NeRF-Nav [7]) for the same 100 start and end locations for each ...
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 7: Natural language-specified goal locations in the Maze scene. The rendered RGB image from the GSplat demonstrate good reconstruction of the ground-truth. Additionally, the ...
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 8: Pose estimates of Splat-Nav using motion capture (green), onboard VIO (red), and Splat-Loc (blue). Splat-Loc gives comparable performance without requiring a manual frame ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Simulation Results 1) Test Environments: We benchmark Splat-Plan and SplatLoc independently on four different environments: Stonehenge, a fully-synthetic scene, and three real-world scenes Statues, ... | embodiment, simulator version and control stack | p. 10 (VI. EXPERIMENTS), p. 10 (VI. EXPERIMENTS) |
| Task/environment | We demonstrate the effectiveness of our navigation pipeline for GSplat maps, examining its performance in real-world scenes on hardware and in simulation. | reset, timeout, object/scene variation | p. 10 (VI. EXPERIMENTS), p. 11 (VI. EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 6 (IV. PLANNING WITH SAFE POLYTOPES), p. 1 (I. INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We evaluate the rotation error (R.E.) and translation error (T.E.) with respect to the ground-truth pose, the computation time (C.T.) per frame, and the ... | definition/direction/unit from same section | p. 11 (VI. EXPERIMENTS) |
| We note that all methods had a perfect success rate in this problem. | definition/direction/unit from same section | p. 11 (VI. EXPERIMENTS) |
| Splat-Plan displays competitive non-conservativeness and computation time, while exhibiting superior safety and success rates. | definition/direction/unit from same section | p. 14 (VI. EXPERIMENTS) |
| We note that Splat-Loc achieves rotation errors of about 3 deg and translation errors of about 4 cm, which is comparable to the accuracy ... | definition/direction/unit from same section | p. 13 (VI. EXPERIMENTS) |
| 6) Splat-Loc Evaluations: We validate the performance of Splat-Loc in hardware experiments in the Maze scene, showing that Splat-Loc achieves relatively the same level ... | definition/direction/unit from same section | p. 13 (VI. EXPERIMENTS) |
| 8) Fast Control: We stress test Splat-Plan by increasing vmax until the onboard VIO could no longer track the desired waypoint with enough accuracy ... | definition/direction/unit from same section | p. 15 (VI. EXPERIMENTS) |
| Fig. 9: Ground-truth trajectories of the drone navigating, projected onto the Maze GSplat. The drone is subjected to different goal locations and control schemes. ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Note that the safety violation of all control schemes is relatively small compared to the size of the drone, which allows error in low-level ... | definition/direction/unit from same section | p. 15 (VI. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Furthermore, we perform ablations against variations of the point-cloud planner in order to expose flaws when planning against point clouds compared to the full ... | comparison identity and matched condition | p. 11 (VI. EXPERIMENTS) |
| Lastly, we examine the performance of the pose estimation algorithms in problems with a larger error in the initial estimate of the pose, with ... | comparison identity and matched condition | p. 11 (VI. EXPERIMENTS) |
| Notice that these trajectories are non-conservative compared to the SFC methods (low path lengths and high polytope volume in Figs. | comparison identity and matched condition | p. 12 (VI. EXPERIMENTS) |
| As a result, the rotation and translation errors for this goal location is higher compared to the those of the other goal locations. | comparison identity and matched condition | p. 13 (VI. EXPERIMENTS) |
| Note that the safety violation of all control schemes is relatively small compared to the size of the drone, which allows error in low-level ... | comparison identity and matched condition | p. 15 (VI. EXPERIMENTS) |
| Fig. 2: Visualization of a point cloud from a NeRF and a mesh from a Gaussian Splat in the synthetic scene Stonehenge. The Chamfer ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Number of Gaussians is reported for both dense and sparse variants of the same scene. | component/input/data sensitivity | p. 11 (VI. EXPERIMENTS) |
| Furthermore, we perform ablations against variations of the point-cloud planner in order to expose flaws when planning against point clouds compared to the full ... | component/input/data sensitivity | p. 11 (VI. EXPERIMENTS) |
| To this end, we developed four variants of the Safe Flight Corridor (SFC) [13]. | component/input/data sensitivity | p. 12 (VI. EXPERIMENTS) |
| These variants are all potential solutions to apply SFC to GSplat environments. | component/input/data sensitivity | p. 12 (VI. EXPERIMENTS) |
| Gaussian Splat for the location of these objects using the following text prompts: "keyboard," "beachball," "phonebook" and "microwave," corresponding to these objects, without negative ... | component/input/data sensitivity | p. 13 (VI. EXPERIMENTS) |
| 6) Splat-Loc Evaluations: We validate the performance of Splat-Loc in hardware experiments in the Maze scene, showing that Splat-Loc achieves relatively the same level ... | component/input/data sensitivity | p. 13 (VI. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The key contributions of this paper are as follows: • We develop a fast polytope corridor generation algorithm to enable provably safe planning for ... | However, Splat-Loc-SIFT achieves a lower success rate, compared to Splat-Loc-Glue, which achieves a perfect success rate. | PDF body cue; verify exact table/figure and matched conditions | p. 11 (VI. EXPERIMENTS), p. 13 (VI. EXPERIMENTS), p. 11 (VI. EXPERIMENTS), p. 13 (VI. EXPERIMENTS), p. 14 (VI. EXPERIMENTS), p. 16 (Figure/Table caption) |
| Primary metric/result | 6) Splat-Loc Evaluations: We validate the performance of Splat-Loc in hardware experiments in the Maze scene, showing that Splat-Loc achieves relatively the same level ... | numeric claim only at cited anchor | p. 13 (VI. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 11 / VI. EXPERIMENTS - extractive body cue:** In each scene, we run 10 trials (of 100 frames each) of each pose estimation algorithm.
- **p. 11 / VI. EXPERIMENTS - extractive body cue:** We provide the summary statistics of the error in the pose estimates computed by each algorithm, in addition to the computation time on a trial ...
- **p. 11 / VI. EXPERIMENTS - extractive body cue:** GS-Loc requires a computation time of about 36.15 s per frame, which is about two orders of magnitude slower than the next-slowest method ICP, which ...
- **p. 11 / VI. EXPERIMENTS - extractive body cue:** Colored-ICP, Splat-Loc-SIFT, and Splat-Loc-Glue require less than 100 ms of computation time.
- **p. 11 / VI. EXPERIMENTS - extractive body cue:** Compared to all methods, Splat-Loc-Glue yields pose estimates with the lowest mean rotation and translation error, less than 0.06◦and 4 mm, respectively, and achieves the ...
- **p. 11 / VI. EXPERIMENTS - extractive body cue:** (%) ICP [59] 73.1 ± 45.9 129 ± 75 107 ± 19.2 100 Colored-ICP [58] 0.83 ± 0.37 1.31 ± 0.60 43.3 ± 9.70 100 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Splat-Plan cannot do anything if an obstacle is completely missing from the scene, which is a fundamental limitation of the GSplat map representation. | p. 16 (VIII. LIMITATIONS AND FUTURE WORK) |
| body limitation/failure cue | More importantly, we see that Splat-Plan never fails to return a trajectory, highlighted by the 0 failure rate. | p. 12 (VI. EXPERIMENTS) |
| body limitation/failure cue | Future work will also incorporate IMU data to improve the robustness of the pose estimator, particularly in featureless regions of the scene where the ... | p. 16 (VIII. LIMITATIONS AND FUTURE WORK) |
| body limitation/failure cue | Fig. 1: Splat-Nav, consists of a safe planning module, Splat-Plan, and robust localization module, Splat-Loc, both operating on a Gaussian Splatting environment representation. In ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Splat-Nav consists of a guaranteed-safe planning module Splat-Plan, which allows for real-time planning (> 2 Hz) by leveraging the ellipsoidal representation inherent in GSplats ... | p. 15 (VII. CONCLUSION) |
| body limitation/failure cue | Given a test point x∗and the jth ellipsoid in the collision test set G∗, we can use our collision test (Corollary 2) to derive ... | p. 17 (VIII. LIMITATIONS AND FUTURE WORK) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 3) Implementation: We run the pose estimator and the planner ROS2 nodes on a desktop computer with an Nvidia RTX 4090 GPU and an ... | p. 12 (VI. EXPERIMENTS) |
| In each scene, we run 10 trials (of 100 frames each) of each pose estimation algorithm. | p. 11 (VI. EXPERIMENTS) |
| We provide the summary statistics of the error in the pose estimates computed by each algorithm, in addition to the computation time on a ... | p. 11 (VI. EXPERIMENTS) |
| Note that as SFC does not use GPU, we rewrote the codebase in Pytorch to yield comparable times to Splat-Plan. | p. 12 (VI. EXPERIMENTS) |
| We demonstrate the effectiveness of our navigation pipeline for GSplat maps, examining its performance in real-world scenes on hardware and in simulation. | p. 10 (VI. EXPERIMENTS) |
| Our hardware tests consist of all combinations of goal locations and control schemes. | p. 13 (VI. EXPERIMENTS) |
| However, Splat-Loc failed in one of the closedloop trials with the "keyboard" goal location. | p. 13 (VI. EXPERIMENTS) |
| We noticed that the VIO of the drone would drift in subsequent runs, necessitating the reinitialization of the VIO at the start of every ... | p. 14 (VI. EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 16 / VIII. LIMITATIONS AND FUTURE WORK - extractive body cue:** Splat-Plan cannot do anything if an obstacle is completely missing from the scene, which is a fundamental limitation of the GSplat map representation.
- **p. 12 / VI. EXPERIMENTS - extractive body cue:** More importantly, we see that Splat-Plan never fails to return a trajectory, highlighted by the 0 failure rate.
- **p. 16 / VIII. LIMITATIONS AND FUTURE WORK - extractive body cue:** Future work will also incorporate IMU data to improve the robustness of the pose estimator, particularly in featureless regions of the scene where the PnP-RANSAC ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Splat-Nav, consists of a safe planning module, Splat-Plan, and robust localization module, Splat-Loc, both operating on a Gaussian Splatting environment representation. In Splat-Plan ...
- **p. 15 / VII. CONCLUSION - extractive body cue:** Splat-Nav consists of a guaranteed-safe planning module Splat-Plan, which allows for real-time planning (> 2 Hz) by leveraging the ellipsoidal representation inherent in GSplats for ...
- **p. 17 / VIII. LIMITATIONS AND FUTURE WORK - extractive body cue:** Given a test point x∗and the jth ellipsoid in the collision test set G∗, we can use our collision test (Corollary 2) to derive these ...

- **PDF anchors reviewed:** datasets p. 10 (VI. EXPERIMENTS), p. 10 (VI. EXPERIMENTS), p. 11 (VI. EXPERIMENTS), p. 12 (VI. EXPERIMENTS), p. 12 (VI. EXPERIMENTS), p. 11 (VI. EXPERIMENTS), metrics p. 11 (VI. EXPERIMENTS), p. 11 (VI. EXPERIMENTS), p. 14 (VI. EXPERIMENTS), p. 13 (VI. EXPERIMENTS), p. 13 (VI. EXPERIMENTS), p. 15 (VI. EXPERIMENTS), baselines p. 11 (VI. EXPERIMENTS), p. 11 (VI. EXPERIMENTS), p. 12 (VI. EXPERIMENTS), p. 13 (VI. EXPERIMENTS), p. 15 (VI. EXPERIMENTS), p. 4 (Figure/Table caption), results p. 11 (VI. EXPERIMENTS), p. 13 (VI. EXPERIMENTS), p. 11 (VI. EXPERIMENTS), p. 13 (VI. EXPERIMENTS), p. 14 (VI. EXPERIMENTS), p. 16 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
