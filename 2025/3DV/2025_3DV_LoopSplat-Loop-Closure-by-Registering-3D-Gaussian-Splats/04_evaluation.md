# Evaluation - LoopSplat: Loop Closure by Registering 3D Gaussian Splats

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=0CNSbBa85A&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 5 (4. Experiments)): Table 2. Tracking Performance on ScanNet++ [93] (ATE RMSE ↓[cm]). LoopSplat achieves the highest accuracy and can robustly deal with the large camera motions in the sequence. computed directly from ...

## Evaluation Body Digest

- **p. 7 / 4.4. Memory and Runtime Analysis - extractive PDF cue:** Additionally, we require the least GPU memory to process a room-sized scene.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 2. Tracking Performance on ScanNet++ [93] (ATE RMSE ↓[cm]). LoopSplat achieves the highest accuracy and can robustly deal with the large camera motions in ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Dense Reconstruction on ScanNet [17] scene0054. LoopSplat demonstrates superior performance in geometric accuracy, robust tracking, and high-quality re-rendering. This is enabled by our ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 5. Reconstruction Performance on Replica [70]. Loop- Splat obtains the second-best F1-score, falling behind only to Loopy-SLAM. It is noteworthy that both the NeRF-based ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Comparison of Mesh Reconstruction on two ScanNet [17] scenes. For the first scene, we highlight shape details with normal shading, showing that LoopSplat ...
- **p. 5 / 4. Experiments - extractive PDF cue:** We evaluate tracking, reconstruction, and rendering performance on synthetic and 5
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 4. Tracking Performance on TUM-RGBD [74] (ATE RMSE ↓[cm]). ∗indicates using ORB-SLAM3 [7] for tracking and loop closure. LoopSplat performs the best among coupled ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 6. Rendering Performance on 3 Datasets. LoopSplat achieves competitive results on synthetic and real-world datasets. Gray indicates evaluation on submaps instead of a global ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2. Tracking Performance on ScanNet++ [93] (ATE RMSE ↓[cm]). LoopSplat achieves the highest accuracy and can robustly deal with the large camera motions ... | p. 5 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 6. Rendering Performance on 3 Datasets. LoopSplat achieves competitive results on synthetic and real-world datasets. Gray indicates evaluation on submaps instead of a ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 3. Tracking Performance on ScanNet [17]. LoopSplat outperforms 3DGS-based systems by a large margin and is on par with the state-of-the-art baselines. real-world ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Tab. 51. LoopSplat outperforms all 3DGS-based baselines attributed to more accurate pose estimates. LoopSplat falls behind Loopy-SLAM [40] and Point-SLAM [63], but note that ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. Dense Reconstruction on ScanNet [17] scene0054. LoopSplat demonstrates superior performance in geometric accuracy, robust tracking, and high-quality re-rendering. This is enabled by ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 4.4. Memory and Runtime Analysis - extractive PDF cue:** Additionally, we require the least GPU memory to process a room-sized scene.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Dense Reconstruction on ScanNet [17] scene0054. LoopSplat demonstrates superior performance in geometric accuracy, robust tracking, and high-quality re-rendering. This is enabled by our ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. LoopSplat Overview. LoopSplat is a coupled RGB-D SLAM system that uses Gaussian splats as a unified scene representation for tracking, mapping, and maintaining ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Tracking Performance on Replica [70] (ATE RMSE ↓[cm]). LC indicates loop closure. The best results are high- lighted as first , second , ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 2. Tracking Performance on ScanNet++ [93] (ATE RMSE ↓[cm]). LoopSplat achieves the highest accuracy and can robustly deal with the large camera motions in ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Tracking Performance on ScanNet [17]. LoopSplat outperforms 3DGS-based systems by a large margin and is on par with the state-of-the-art baselines. real-world datasets, ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 4. Tracking Performance on TUM-RGBD [74] (ATE RMSE ↓[cm]). ∗indicates using ORB-SLAM3 [7] for tracking and loop closure. LoopSplat performs the best among coupled ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3. Comparison of Submap Alignment on ScanNet [17]. We visualize the centers of 3D Gaussians as point clouds. Two submaps are colorized differently. LoopSplat ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Tab. 51. LoopSplat outperforms all 3DGS-based baselines attributed to more accurate pose estimates. LoopSplat falls behind Loopy-SLAM [40] and Point-SLAM [63], but note that the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Additionally, we require the least GPU memory to process a room-sized scene. | embodiment, simulator version and control stack | p. 7 (4.4. Memory and Runtime Analysis) |
| Task/environment | not recovered | reset, timeout, object/scene variation | 본문 anchor 없음 |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 7 (4.3. Rendering), p. 6 (Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 7 (4.2. Reconstruction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2. Tracking Performance on ScanNet++ [93] (ATE RMSE ↓[cm]). LoopSplat achieves the highest accuracy and can robustly deal with the large camera motions ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Figure 1. Dense Reconstruction on ScanNet [17] scene0054. LoopSplat demonstrates superior performance in geometric accuracy, robust tracking, and high-quality re-rendering. This is enabled by ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Table 5. Reconstruction Performance on Replica [70]. Loop- Splat obtains the second-best F1-score, falling behind only to Loopy-SLAM. It is noteworthy that both the ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 4. Comparison of Mesh Reconstruction on two ScanNet [17] scenes. For the first scene, we highlight shape details with normal shading, showing that ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| We evaluate tracking, reconstruction, and rendering performance on synthetic and 5 | definition/direction/unit from same section | p. 5 (4. Experiments) |
| Table 4. Tracking Performance on TUM-RGBD [74] (ATE RMSE ↓[cm]). ∗indicates using ORB-SLAM3 [7] for tracking and loop closure. LoopSplat performs the best among ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 6. Rendering Performance on 3 Datasets. LoopSplat achieves competitive results on synthetic and real-world datasets. Gray indicates evaluation on submaps instead of a ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 8. Ablation Study on 3DGS Registration. The num- bers are computed based on average performance of 8 scenes on Replica [71]. Mul. Opt. ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 3. Tracking Performance on ScanNet [17]. LoopSplat outperforms 3DGS-based systems by a large margin and is on par with the state-of-the-art baselines. real-world ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Here we describe our experimental setup and compare our method to state-of-the-art baselines. | comparison identity and matched condition | p. 5 (4. Experiments) |
| While our per-frame tracking and map optimization time falls behind the fastest baselines, our Gaussian Splattingbased registration significantly shortens the loop edge registration time ... | comparison identity and matched condition | p. 7 (4.4. Memory and Runtime Analysis) |
| Tab. 51. LoopSplat outperforms all 3DGS-based baselines attributed to more accurate pose estimates. LoopSplat falls behind Loopy-SLAM [40] and Point-SLAM [63], but note that ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 7. Runtime and Memory Usage on Replica office 0. Per-frame runtime is calculated as the total optimization time di- vided by the sequence ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Table 8. Ablation Study on 3DGS Registration. The num- bers are computed based on average performance of 8 scenes on Replica [71]. Mul. Opt. ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 8. Ablation Study on 3DGS Registration. The num- bers are computed based on average performance of 8 scenes on Replica [71]. Mul. Opt. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 3. Tracking Performance on ScanNet [17]. LoopSplat outperforms 3DGS-based systems by a large margin and is on par with the state-of-the-art baselines. real-world ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Table 7. Runtime and Memory Usage on Replica office 0. Per-frame runtime is calculated as the total optimization time di- vided by the sequence ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce LoopSplat, a coupled RGB-D SLAM system based on Gaussian Splatting, featuring a novel loop closure module. | Table 2. Tracking Performance on ScanNet++ [93] (ATE RMSE ↓[cm]). LoopSplat achieves the highest accuracy and can robustly deal with the large camera motions ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 5 (4. Experiments) |
| Primary metric/result | Table 6. Rendering Performance on 3 Datasets. LoopSplat achieves competitive results on synthetic and real-world datasets. Gray indicates evaluation on submaps instead of a ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / Method - extractive PDF cue:** Neural Implicit Fields Vox-Fusion [90] 16.6 24.2 8.4 27.3 23.3 9.4 - - - Co-SLAM [83] 7.1 11.1 9.4 5.9 11.8 7.1 - - - ...
- **p. 7 / 4.1. Tracking - extractive PDF cue:** Scene 54 Scene 233 Gaussian-SLAM [95] Ours Ground Truth Figure 3.
- **p. 7 / 4.3. Rendering - extractive PDF cue:** Dataset Replica [70] TUM [74] ScanNet [17] Method PSNR ↑SSIM ↑LPIPS ↓PSNR ↑SSIM ↑LPIPS ↓PSNR ↑SSIM ↑LPIPS ↓ NICE-SLAM [103] 24.42 0.892 0.233 14.86 0.614 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While our per-frame tracking and map optimization time falls behind the fastest baselines, our Gaussian Splattingbased registration significantly shortens the loop edge registration time ... | p. 7 (4.4. Memory and Runtime Analysis) |
| body limitation/failure cue | Table 5. Reconstruction Performance on Replica [70]. Loop- Splat obtains the second-best F1-score, falling behind only to Loopy-SLAM. It is noteworthy that both the ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Figure 4. Comparison of Mesh Reconstruction on two ScanNet [17] scenes. For the first scene, we highlight shape details with normal shading, showing that ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Figure 1. Dense Reconstruction on ScanNet [17] scene0054. LoopSplat demonstrates superior performance in geometric accuracy, robust tracking, and high-quality re-rendering. This is enabled by ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Table 2. Tracking Performance on ScanNet++ [93] (ATE RMSE ↓[cm]). LoopSplat achieves the highest accuracy and can robustly deal with the large camera motions ... | p. 5 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For implementation details, please refer to Supp. | p. 6 (Method) |
| To assess map size, we measure the total memory needed for the map and the peak GPU memory usage. | p. 6 (Method) |
| 7 profiles the runtime and memory usage of LoopSplat. | p. 7 (4.4. Memory and Runtime Analysis) |
| Additionally, we require the least GPU memory to process a room-sized scene. | p. 7 (4.4. Memory and Runtime Analysis) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.4. Memory and Runtime Analysis - extractive PDF cue:** While our per-frame tracking and map optimization time falls behind the fastest baselines, our Gaussian Splattingbased registration significantly shortens the loop edge registration time compared ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 5. Reconstruction Performance on Replica [70]. Loop- Splat obtains the second-best F1-score, falling behind only to Loopy-SLAM. It is noteworthy that both the NeRF-based ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Comparison of Mesh Reconstruction on two ScanNet [17] scenes. For the first scene, we highlight shape details with normal shading, showing that LoopSplat ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Dense Reconstruction on ScanNet [17] scene0054. LoopSplat demonstrates superior performance in geometric accuracy, robust tracking, and high-quality re-rendering. This is enabled by our ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 2. Tracking Performance on ScanNet++ [93] (ATE RMSE ↓[cm]). LoopSplat achieves the highest accuracy and can robustly deal with the large camera motions in ...

- **PDF anchors reviewed:** datasets p. 7 (4.4. Memory and Runtime Analysis), metrics p. 5 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 5 (4. Experiments), p. 6 (Figure/Table caption), baselines p. 6 (Figure/Table caption), p. 5 (4. Experiments), p. 7 (4.4. Memory and Runtime Analysis), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 5 (4. Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
