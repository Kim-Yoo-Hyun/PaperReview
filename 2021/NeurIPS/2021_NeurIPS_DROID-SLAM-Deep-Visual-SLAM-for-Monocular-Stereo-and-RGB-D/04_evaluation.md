# Evaluation - DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2108.10869; PDF retrieval source: https://arxiv.org/pdf/2108.10869. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (4 Experiments)): On most sequences, we outperform existing methods by an order-of-magnitude and achieve 8x lower average error than TartanVO [54] and 20x lower than DeepV2D [48].

## Evaluation Body Digest

- **p. 8 / 4 Experiments - extractive body cue:** TUM-RGBD [44] The RGBD dataset consists of indoor scenes captured with handheld camera.
- **p. 8 / 4 Experiments - extractive body cue:** The EuRoC dataset consists of video captured from sensor on-board a micro aerial vehicle (MAV) and is a widely used benchmark to evaluate SLAM systems.
- **p. 9 / 4 Experiments - extractive body cue:** Method AUC (train) AUC (test) BundleFusion [11] 84.10 33.84 ElasticFusion [57] 89.06 34.02 RFusion [56] 17.37 51.94 DVO-SLAM [20] 193.89 71.83 ORB-SLAM2 [32] 156.10 104.28 ...
- **p. 9 / 4 Experiments - extractive body cue:** (Left) Our method, which is trained only on the synthetic TartanAir dataset, ranks 1st on both the train and test splits.
- **p. 7 / 4 Experiments - extractive body cue:** We experiment on a diverse set of datasets and sensor modalities.
- **p. 7 / 4 Experiments - extractive body cue:** Our network is trained entirely on monocular video from the synthetic TartanAir dataset [55].
- **p. 7 / 4 Experiments - extractive body cue:** Following prior work, we evaluate the accuracy of the camera trajectory [31, 15, 42], primarily using Absolute Trajectory Error (ATE) [44].
- **p. 8 / 4 Experiments - extractive body cue:** The score is computed using normalized relative pose error for all possible sequences of length {5, 10, 15, ..., 40} meters, see competition page for ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4 Experiments (p. 7); A Additional Results (p. 13).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | On most sequences, we outperform existing methods by an order-of-magnitude and achieve 8x lower average error than TartanVO [54] and 20x lower than DeepV2D ... | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | In the monocular setting, we achieve an average ATE of 2.2cm, reducing error by 82% among methods with zero failures, and by 43% over ... | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Method AUC (train) AUC (test) BundleFusion [11] 84.10 33.84 ElasticFusion [57] 89.06 34.02 RFusion [56] 17.37 51.94 DVO-SLAM [20] 193.89 71.83 ORB-SLAM2 [32] 156.10 ... | p. 9 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 4: Generalization results on the RGB-D ETH3D-SLAM benchmark. (Left) Our method, which is trained only on the synthetic TartanAir dataset, ranks 1st on ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1: DROID-SLAM can operate on monocular, stereo, and RGB-D video. It builds a dense 3D map of the environment while simultaneously localizing the ... | p. 2 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiments - extractive body cue:** TUM-RGBD [44] The RGBD dataset consists of indoor scenes captured with handheld camera.
- **p. 8 / 4 Experiments - extractive body cue:** The EuRoC dataset consists of video captured from sensor on-board a micro aerial vehicle (MAV) and is a widely used benchmark to evaluate SLAM systems.
- **p. 9 / 4 Experiments - extractive body cue:** Method AUC (train) AUC (test) BundleFusion [11] 84.10 33.84 ElasticFusion [57] 89.06 34.02 RFusion [56] 17.37 51.94 DVO-SLAM [20] 193.89 71.83 ORB-SLAM2 [32] 156.10 104.28 ...
- **p. 9 / 4 Experiments - extractive body cue:** (Left) Our method, which is trained only on the synthetic TartanAir dataset, ranks 1st on both the train and test splits.
- **p. 7 / 4 Experiments - extractive body cue:** We experiment on a diverse set of datasets and sensor modalities.
- **p. 7 / 4 Experiments - extractive body cue:** Our network is trained entirely on monocular video from the synthetic TartanAir dataset [55].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: DROID-SLAM can operate on monocular, stereo, and RGB-D video. It builds a dense 3D map of the environment while simultaneously localizing the camera ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Illustration of the update operator. The operator acts on edges in the frame graph, predicting flow revisions which are mapped to depth and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: DROID-SLAM can generalize to new datasets. In order, we show results from Tanks & Temples [21], ScanNet [10], Sintel [3], and ETH-3D [42]; ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Results on the TartanAir monocular benchmark. 7
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Results on the TartanAir test set, compared with the top 3 submission to the ECCV 2020 SLAM competition. The score is computed using ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Monocular SLAM on the EuRoC datasets, ATE[m]. † denotes visual odometry methods. In the monocular setting, we achieve an average ATE of 2.2cm, ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: ATE on the TUM-RGBD benchmark. All methods are provided mono. video, 1except DeepTAM which uses RGB-D and 2TartanVO which uses ground truth to ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Generalization results on the RGB-D ETH3D-SLAM benchmark. (Left) Our method, which is trained only on the synthetic TartanAir dataset, ranks 1st on both ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | TUM-RGBD [44] The RGBD dataset consists of indoor scenes captured with handheld camera. | embodiment, simulator version and control stack | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Task/environment | The EuRoC dataset consists of video captured from sensor on-board a micro aerial vehicle (MAV) and is a widely used benchmark to evaluate SLAM ... | reset, timeout, object/scene variation | p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (3 Approach), p. 5 (3 Approach) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 5 (3 Approach), p. 3 (3 Approach) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Following prior work, we evaluate the accuracy of the camera trajectory [31, 15, 42], primarily using Absolute Trajectory Error (ATE) [44]. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| The score is computed using normalized relative pose error for all possible sequences of length {5, 10, 15, ..., 40} meters, see competition page ... | definition/direction/unit from same section | p. 8 (4 Experiments) |
| 1 demonstrates both the robustness of our method (no catastrophic failures) and accuracy (very low drift). | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Figure 1: DROID-SLAM can operate on monocular, stereo, and RGB-D video. It builds a dense 3D map of the environment while simultaneously localizing the ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 6: (Left) we show the performance of the system with different inputs (monocular vs. stereo) and whether global optimization is performed in addition ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| Figure 4: Generalization results on the RGB-D ETH3D-SLAM benchmark. (Left) Our method, which is trained only on the synthetic TartanAir dataset, ranks 1st on ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| On the test set, we successfully track 30/32 RGB-D, improving over the next best of 19/32. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Figure 2: Illustration of the update operator. The operator acts on edges in the frame graph, predicting flow revisions which are mapped to depth ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We retrain DeepV2D [48] on TartanAir as a baseline. | comparison identity and matched condition | p. 8 (4 Experiments) |
| We find that recent deep learning approaches [9, 48, 54] perform poorly on the EuRoC dataset compared to classical SLAM systems. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Table 5: Stereo SLAM on the EuRoC datasets, ATE[m]. We provide stereo results on the EuRoC dataset[2] in Tab. 5 using our network trained ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| Figure 1: DROID-SLAM can operate on monocular, stereo, and RGB-D video. It builds a dense 3D map of the environment while simultaneously localizing the ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Following prior work, we evaluate the accuracy of the camera trajectory [31, 15, 42], primarily using Absolute Trajectory Error (ATE) [44]. | comparison identity and matched condition | p. 7 (4 Experiments) |
| Without any finetuning, our method ranks 1st on both the train and test splits. | comparison identity and matched condition | p. 9 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Without any finetuning, our method ranks 1st on both the train and test splits. | component/input/data sensitivity | p. 9 (4 Experiments) |
| Table 5: Stereo SLAM on the EuRoC datasets, ATE[m]. We provide stereo results on the EuRoC dataset[2] in Tab. 5 using our network trained ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| Figure 6: (Left) we show the performance of the system with different inputs (monocular vs. stereo) and whether global optimization is performed in addition ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| Figure 2: Illustration of the update operator. The operator acts on edges in the frame graph, predicting flow revisions which are mapped to depth ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work we introduce DROID-SLAM, a new SLAM system based on deep learning. | On most sequences, we outperform existing methods by an order-of-magnitude and achieve 8x lower average error than TartanVO [54] and 20x lower than DeepV2D ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (4 Experiments) |
| Primary metric/result | In the monocular setting, we achieve an average ATE of 2.2cm, reducing error by 82% among methods with zero failures, and by 43% over ... | numeric claim only at cited anchor | p. 8 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive body cue:** We train our network for 250k steps with a batch size of 4, resolution 384 × 512, and 7 frame clips, and unroll 15 update ...
- **p. 7 / 4 Experiments - extractive body cue:** Training takes 1 week on 4 RTX-3090 GPUs.
- **p. 7 / 4 Experiments - extractive body cue:** Monocular MH000 MH001 MH002 MH003 MH004 MH005 MH006 MH007 Avg ORB-SLAM [31] 1.30 0.04 2.37 2.45 X X 21.47 2.73 - DeepV2D [48] 6.15 2.12 ...
- **p. 8 / 4 Experiments - extractive body cue:** On most sequences, we outperform existing methods by an order-of-magnitude and achieve 8x lower average error than TartanVO [54] and 20x lower than DeepV2D [48].
- **p. 8 / 4 Experiments - extractive body cue:** The score is computed using normalized relative pose error for all possible sequences of length {5, 10, 15, ..., 40} meters, see competition page for ...
- **p. 8 / 4 Experiments - extractive body cue:** Our method, on the other hand, runs 16x faster and achieves an error 62% lower on the monocular benchmark and 60% lower on the stereo ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 1 demonstrates both the robustness of our method (no catastrophic failures) and accuracy (very low drift). | p. 8 (4 Experiments) |
| body limitation/failure cue | Figure 1: DROID-SLAM can operate on monocular, stereo, and RGB-D video. It builds a dense 3D map of the environment while simultaneously localizing the ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | In the monocular setting, we achieve an average ATE of 2.2cm, reducing error by 82% among methods with zero failures, and by 43% over ... | p. 8 (4 Experiments) |
| body limitation/failure cue | While memory and resource requirements are currently the biggest limitation of our system, we believe these can be drastically reduced by culling redundant computation ... | p. 9 (4 Experiments) |
| body limitation/failure cue | DROID-SLAM is accurate, robust, and versatile and can be used on monocular, stereo, and RGB-D video. | p. 9 (5 Conclusion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train our network for 250k steps with a batch size of 4, resolution 384 × 512, and 7 frame clips, and unroll 15 ... | p. 7 (4 Experiments) |
| The score is computed using normalized relative pose error for all possible sequences of length {5, 10, 15, ..., 40} meters, see competition page ... | p. 8 (4 Experiments) |
| Tracking and local BA is run on the first GPU, while global BA and loop closure is run on the second. | p. 9 (4 Experiments) |
| The SLAM frontend can be run on GPUs with 8GB of memory. | p. 9 (4 Experiments) |
| Once 12 frames have been accumulated, we initialize a frame graph by creating an edges between keyframes which are within 3 timesteps apart, then ... | p. 6 (3 Approach) |
| At inference time, we use a custom CUDA kernel which takes advantage of the block-sparse structure of the problem, then perform sparse Cholesky decomposition ... | p. 7 (3 Approach) |
| After each pose or depth update, we can recompute 3 | p. 3 (3 Approach) |
| The operator is applied to each correlation volume in the pyramid and the final feature vector is computed by concatenating the results at each ... | p. 4 (3 Approach) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4 Experiments - extractive body cue:** 1 demonstrates both the robustness of our method (no catastrophic failures) and accuracy (very low drift).
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: DROID-SLAM can operate on monocular, stereo, and RGB-D video. It builds a dense 3D map of the environment while simultaneously localizing the camera ...
- **p. 8 / 4 Experiments - extractive body cue:** In the monocular setting, we achieve an average ATE of 2.2cm, reducing error by 82% among methods with zero failures, and by 43% over ORB-SLAM3 ...
- **p. 9 / 4 Experiments - extractive body cue:** While memory and resource requirements are currently the biggest limitation of our system, we believe these can be drastically reduced by culling redundant computation and ...
- **p. 9 / 5 Conclusion - extractive body cue:** DROID-SLAM is accurate, robust, and versatile and can be used on monocular, stereo, and RGB-D video.

- **Evidence anchors reviewed:** datasets p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), metrics p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 2 (Figure/Table caption), p. 13 (Figure/Table caption), p. 9 (Figure/Table caption), baselines p. 8 (4 Experiments), p. 8 (4 Experiments), p. 13 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (4 Experiments), p. 9 (4 Experiments), results p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (Figure/Table caption), p. 2 (Figure/Table caption), p. 7 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 2: Results on the TartanAir test set, compared with the top 3 submission to the ECCV 2020 SLAM competition. The score is computed using normalized relative pose error for ... (p. 8, Figure/Table caption).
- **Metric evidence:** Following prior work, we evaluate the accuracy of the camera trajectory [31, 15, 42], primarily using Absolute Trajectory Error (ATE) [44]. (p. 7, 4 Experiments).
- **Baseline/ablation evidence:** Following prior work, we evaluate the accuracy of the camera trajectory [31, 15, 42], primarily using Absolute Trajectory Error (ATE) [44]. (p. 7, 4 Experiments).
- **Failure/negative evidence:** We find that the SLAM system is unstable and prone to failure if the DBA is not used during training. (p. 13, 8 Keyframes).
