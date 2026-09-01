# Evaluation - HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2501.14147; PDF retrieval source: https://arxiv.org/pdf/2501.14147. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS)): HAMMER dramatically outperforms Di-NeRF* which fails to converge to accurate inter-robot alignments.

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** However, ReplicaMultiAgent only contains scenes from simulated environments, and lacks heterogeneous robots/sensing devices and challenging real-world scene conditions (e.g. motion blur, diverse lighting).
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Therefore, to showcase the generalizability of HAMMER and its real-time deployment in real-world environments, we also assess its performance in two different hardware trials with ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Because both MAGiC-SLAM and CP-SLAM are not realtime capable, do not have publicly available code for integration with hardware/ROS, and do not support heterogeneous devices, ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We quantify reconstruction quality based on the average PSNR of each method on the held-out evaluation dataset (Fig.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** First, we compare HAMMER to state-of-the-art baselines [13], [14] by assessing their reconstruction accuracy on the ReplicaMultiAgent dataset [14], [15].
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Experimental Setup 1) Implementation: Unlike other baselines, HAMMER is fully integrated into the ROS2 ecosystem [36] to stream data from all robots to a server, ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: HAMMER takes streaming image and depth data from a heterogeneous team of robots and edge devices (e.g. Aria Glasses [1]), each running on-board ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** 3) as the 3DGS evolves in time during the online map optimization process.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | HAMMER dramatically outperforms Di-NeRF* which fails to converge to accurate inter-robot alignments. | p. 6 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | HAMMER outperforms both baselines on all averaged metrics, and does so at least 25× faster than CPSLAM and 16× faster than MAGiC-SLAM. | p. 6 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 5: Map quality over time for HAMMER and baselines in two scenes. HAMMER outperforms Di-NeRF*, demonstrating the necessity of accurate robot alignment. It ... | p. 7 (Figure/Table caption) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | First, we compare HAMMER to state-of-the-art baselines [13], [14] by assessing their reconstruction accuracy on the ReplicaMultiAgent dataset [14], [15]. | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Therefore, to showcase the generalizability of HAMMER and its real-time deployment in real-world environments, we also assess its performance in two different hardware trials ... | p. 5 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** However, ReplicaMultiAgent only contains scenes from simulated environments, and lacks heterogeneous robots/sensing devices and challenging real-world scene conditions (e.g. motion blur, diverse lighting).
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Therefore, to showcase the generalizability of HAMMER and its real-time deployment in real-world environments, we also assess its performance in two different hardware trials with ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Because both MAGiC-SLAM and CP-SLAM are not realtime capable, do not have publicly available code for integration with hardware/ROS, and do not support heterogeneous devices, ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We quantify reconstruction quality based on the average PSNR of each method on the held-out evaluation dataset (Fig.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: HAMMER takes streaming image and depth data from a heterogeneous team of robots and edge devices (e.g. Aria Glasses [1]), each running on-board ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: HAMMER uses a one-time computation to align a new robot's data stream with the server's map frame. We match images from the unaligned ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Meshes extracted from HAMMER's map during runtime (left) and the final map reconstruction (right). The attribution meshes show the part of the map ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Rendered evaluation images RGB (left) and depth (right) of HAMMER and two baselines across devices. HAMMER is visually and geometrically superior to Di-NeRF*, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Map quality over time for HAMMER and baselines in two scenes. HAMMER outperforms Di-NeRF*, demonstrating the necessity of accurate robot alignment. It also ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Motion plans for robots navigating to language- specified goals with trajectories from Splat-Nav [7]. [2] B. Mildenhall, P. P. Srinivasan, M. Tancik, J. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | However, ReplicaMultiAgent only contains scenes from simulated environments, and lacks heterogeneous robots/sensing devices and challenging real-world scene conditions (e.g. motion blur, diverse lighting). | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Task/environment | Therefore, to showcase the generalizability of HAMMER and its real-time deployment in real-world environments, we also assess its performance in two different hardware trials ... | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (III. METHOD), p. 2 (III. METHOD) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (III. METHOD), p. 2 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| First, we compare HAMMER to state-of-the-art baselines [13], [14] by assessing their reconstruction accuracy on the ReplicaMultiAgent dataset [14], [15]. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Experimental Setup 1) Implementation: Unlike other baselines, HAMMER is fully integrated into the ROS2 ecosystem [36] to stream data from all robots to a ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Fig. 1: HAMMER takes streaming image and depth data from a heterogeneous team of robots and edge devices (e.g. Aria Glasses [1]), each running ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| 3) as the 3DGS evolves in time during the online map optimization process. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Qualitatively, HAMMER demonstrates superior novel-view renders on the evaluation set (Fig. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Fig. 5: Map quality over time for HAMMER and baselines in two scenes. HAMMER outperforms Di-NeRF*, demonstrating the necessity of accurate robot alignment. It ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 2: HAMMER uses a one-time computation to align a new robot's data stream with the server's map frame. We match images from the ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 5: Map quality over time for HAMMER and baselines in two scenes. HAMMER outperforms Di-NeRF*, demonstrating the necessity of accurate robot alignment. It ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| First, we compare HAMMER to state-of-the-art baselines [13], [14] by assessing their reconstruction accuracy on the ReplicaMultiAgent dataset [14], [15]. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| HAMMER outperforms both baselines on all averaged metrics, and does so at least 25× faster than CPSLAM and 16× faster than MAGiC-SLAM. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| HAMMER is visually and geometrically superior to Di-NeRF*, and approaches the quality of the Oracle upper bound baseline. a conference room. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Experimental Setup 1) Implementation: Unlike other baselines, HAMMER is fully integrated into the ROS2 ecosystem [36] to stream data from all robots to a ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |

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
| A server-based architecture allows our method to be used with existing robot and edge device hardware without highpowered GPUs, while leveraging typical communication infrastructure ... | HAMMER dramatically outperforms Di-NeRF* which fails to converge to accurate inter-robot alignments. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Primary metric/result | HAMMER outperforms both baselines on all averaged metrics, and does so at least 25× faster than CPSLAM and 16× faster than MAGiC-SLAM. | numeric claim only at cited anchor | p. 6 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The mapping server is a desktop computer with a NVIDIA RTX 4090 GPU.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** To simulate realtime deployment within the environments, we create 2 minute long ROSBags that stream data at 20Hz.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Onboard the GRs, RGBD images (1280x720) are published onto the network at 10 Hz along with poses estimated onboard using the ZED SDK.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The Arias produce 1440x1440 fisheye RGB images and point clouds at 10 Hz.
- **p. 4 / III. METHOD - extractive body cue:** However, these semantic embeddings can vary up to 1000 dimensions, which is prohibitively expensive to inference and store.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ground-truth images. | p. 6 (IV. EXPERIMENTS) |
| body limitation/failure cue | 3) Pose Refinement: Although the alignment module produces robust estimates of the local-to-world transforms, it cannot account for gradual drift or other temporal noise. | p. 5 (III. METHOD) |
| body limitation/failure cue | HAMMER dramatically outperforms Di-NeRF* which fails to converge to accurate inter-robot alignments. | p. 6 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Because both MAGiC-SLAM and CP-SLAM are not realtime capable, do not have publicly available code for integration with hardware/ROS, and do not support heterogeneous ... | p. 6 (IV. EXPERIMENTS) |
| 5GHz WiFi is used to communicate during hardware trials. | p. 5 (IV. EXPERIMENTS) |
| The mapping server is a desktop computer with a NVIDIA RTX 4090 GPU. | p. 5 (IV. EXPERIMENTS) |
| 2) Hardware Trials: HAMMER is able to successfully construct quality 3DGS maps, visualized in (Fig. | p. 6 (IV. EXPERIMENTS) |
| During runtime, HAMMER rejects alignments where the localized SfM fails to estimate poses for all 2W input images or alignments that have high translation ... | p. 3 (III. METHOD) |
| This computation takes approximately 36 sec. in our implementation. | p. 3 (III. METHOD) |
| However, handling such cases is outside the scope of our implementation of HAMMER. | p. 4 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** 4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ground-truth images.
- **p. 5 / III. METHOD - extractive body cue:** 3) Pose Refinement: Although the alignment module produces robust estimates of the local-to-world transforms, it cannot account for gradual drift or other temporal noise.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** HAMMER dramatically outperforms Di-NeRF* which fails to converge to accurate inter-robot alignments.

- **PDF anchors reviewed:** datasets p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), metrics p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 1 (Figure/Table caption), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), results p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
