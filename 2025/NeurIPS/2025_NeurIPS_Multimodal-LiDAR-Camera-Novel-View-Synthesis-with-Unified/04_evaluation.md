# Evaluation - Multimodal LiDAR-Camera Novel View Synthesis with Unified Pose-free Neural Fields

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=GQHUET0V6f; PDF retrieval source: https://openreview.net/pdf/81f57d1abb2e9779707b1274c08b3260d8f44d29.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 9 (5 Experiment), p. 10 (5 Experiment), p. 10 (5 Experiment), p. 7 (Figure/Table caption), p. 4 (Figure/Table caption)): Figure 7: Qualitative NVS results with GT- poses. MUP outperforms single-modal meth- ods i-NGP w/ and w/o point clouds and LiDAR- NeRF. Our method achieves significantly better depth estimation and ...

## Evaluation Body Digest

- **p. 8 / 5 Experiment - extractive PDF cue:** For the NuScenes dataset, it includes six cameras and a LiDAR sensor, with keyframes that are typically used, which are time-synchronized based on timestamps.
- **p. 8 / 5 Experiment - extractive PDF cue:** We conducted experiments on two public autonomous driving datasets: NuScenes [4] and KITTI-360 [15] dataset, each with five representative timesynchronized LiDAR point cloud and image ...
- **p. 9 / 5 Experiment - extractive PDF cue:** As for the registration-first approach, ColoredICP [24] exhibits limited accuracy in large-scale outdoor scenes.
- **p. 9 / 5 Experiment - extractive PDF cue:** Methods LiDAR Metrics Image Metrics CD ↓F-score ↑MAEI ↓PSNR ↑ SSIM ↑ LPIPS ↓ Experiments on KITTI - 360 [15], i-NGP: i-NGP w/ point cloud. ...
- **p. 10 / 5 Experiment - extractive PDF cue:** Additionally, it is not designed to handle dynamic scenes, which is a non-negligible limitation in autonomous driving scenarios.
- **p. 10 / 5 Experiment - extractive PDF cue:** 6 Limitation MUP demonstrates strong performance in pose-free multimodal NVS and pose estimation under challenging large-scale scenes.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4: Consistency constraint. We project rendered images onto other frames by depth obtained from NeRF to compute the photometric error. It's particularly effective for ...
- **p. 8 / 5 Experiment - extractive PDF cue:** Following [36, 55] for point cloud NVS, we adopt CD to assess 3D geometric errors and the F-score with a 5 cm threshold.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5 Experiment (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 7: Qualitative NVS results with GT- poses. MUP outperforms single-modal meth- ods i-NGP w/ and w/o point clouds and LiDAR- NeRF. Our method ... | p. 9 (Figure/Table caption) |
| 5 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method achieves the highest pose estimation accuracy. | p. 9 (5 Experiment) |
| 5 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results indicate that relying solely on NeRF's implicit pose optimization fails to achieve accurate pose estimates and leads to convergence at local optima. | p. 10 (5 Experiment) |
| 5 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | Thus, compared to single-modality methods and i-NGP [21] that with and without point clouds for depth supervision, we achieve highquality NVS and the best ... | p. 10 (5 Experiment) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 5: Qualitative comparison of NVS. We compared MUP with pose-free and registration-first methods. Nope-NeRF and Colored-ICP-assisted fail due to the large-scale scene. BA-Alignmif ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 5 Experiment - extractive PDF cue:** For the NuScenes dataset, it includes six cameras and a LiDAR sensor, with keyframes that are typically used, which are time-synchronized based on timestamps.
- **p. 8 / 5 Experiment - extractive PDF cue:** We conducted experiments on two public autonomous driving datasets: NuScenes [4] and KITTI-360 [15] dataset, each with five representative timesynchronized LiDAR point cloud and image ...
- **p. 9 / 5 Experiment - extractive PDF cue:** As for the registration-first approach, ColoredICP [24] exhibits limited accuracy in large-scale outdoor scenes.
- **p. 9 / 5 Experiment - extractive PDF cue:** Methods LiDAR Metrics Image Metrics CD ↓F-score ↑MAEI ↓PSNR ↑ SSIM ↑ LPIPS ↓ Experiments on KITTI - 360 [15], i-NGP: i-NGP w/ point cloud. ...
- **p. 10 / 5 Experiment - extractive PDF cue:** Additionally, it is not designed to handle dynamic scenes, which is a non-negligible limitation in autonomous driving scenarios.
- **p. 10 / 5 Experiment - extractive PDF cue:** 6 Limitation MUP demonstrates strong performance in pose-free multimodal NVS and pose estimation under challenging large-scale scenes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: NVS results w/ and w/o accurate poses. Compared to continuous LiDAR-Camera Fields, projecting LiDAR point clouds onto images as discrete depth priors fails ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of our proposed MUP. MUP derives pose gradients through both im- plicit global optimization from the Unified Neural LiDAR-Camera Fields and our ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Modality fusion in Hash-grids and geo-MLP. We truncate the gradients of each modal- ity separately in hash grids and geo-MLP. The results show ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4: Consistency constraint. We project rendered images onto other frames by depth obtained from NeRF to compute the photometric error. It's particularly effective for ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Quantitative comparison of NVS in pose-free setting. We conduct experiments under the pose-free setup. The estimated trajectory is aligned with the ground truth ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Qualitative comparison of NVS. We compared MUP with pose-free and registration-first methods. Nope-NeRF and Colored-ICP-assisted fail due to the large-scale scene. BA-Alignmif struggles ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 2: Ablation studies on the MMG mod- ule and image modality under the pose-free setting(top). MMG module plays a pivotal role in pose optimization. ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: Quantitative comparison on NVS with GT-poses. We conducted experiments un- der GT-poses to demonstrate the effectiveness of our method in modal fusion.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For the NuScenes dataset, it includes six cameras and a LiDAR sensor, with keyframes that are typically used, which are time-synchronized based on timestamps. | embodiment, simulator version and control stack | p. 8 (5 Experiment), p. 8 (5 Experiment) |
| Task/environment | We conducted experiments on two public autonomous driving datasets: NuScenes [4] and KITTI-360 [15] dataset, each with five representative timesynchronized LiDAR point cloud and ... | reset, timeout, object/scene variation | p. 8 (5 Experiment), p. 9 (5 Experiment) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (4 Methodology), p. 5 (4 Methodology) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 7 (4 Methodology), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 4: Consistency constraint. We project rendered images onto other frames by depth obtained from NeRF to compute the photometric error. It's particularly effective ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Following [36, 55] for point cloud NVS, we adopt CD to assess 3D geometric errors and the F-score with a 5 cm threshold. | definition/direction/unit from same section | p. 8 (5 Experiment) |
| We also compute mean absolute error (MAE) for intensity in projected range images. | definition/direction/unit from same section | p. 8 (5 Experiment) |
| Our method achieves the highest pose estimation accuracy. | definition/direction/unit from same section | p. 9 (5 Experiment) |
| As for the registration-first approach, ColoredICP [24] exhibits limited accuracy in large-scale outdoor scenes. | definition/direction/unit from same section | p. 9 (5 Experiment) |
| It also introduces complementary information beyond LiDARs perspective, enhancing registration accuracy. | definition/direction/unit from same section | p. 10 (5 Experiment) |
| 6 Limitation MUP demonstrates strong performance in pose-free multimodal NVS and pose estimation under challenging large-scale scenes. | definition/direction/unit from same section | p. 10 (5 Experiment) |
| Figure 5: Qualitative comparison of NVS. We compared MUP with pose-free and registration-first methods. Nope-NeRF and Colored-ICP-assisted fail due to the large-scale scene. BA-Alignmif ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 5: Qualitative comparison of NVS. We compared MUP with pose-free and registration-first methods. Nope-NeRF and Colored-ICP-assisted fail due to the large-scale scene. BA-Alignmif ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| 5.2 Comparison and Ablation in Pose-free Setting Baselines. | comparison identity and matched condition | p. 9 (5 Experiment) |
| Thus, compared to single-modality methods and i-NGP [21] that with and without point clouds for depth supervision, we achieve highquality NVS and the best ... | comparison identity and matched condition | p. 10 (5 Experiment) |
| Figure 1: NVS results w/ and w/o accurate poses. Compared to continuous LiDAR-Camera Fields, projecting LiDAR point clouds onto images as discrete depth priors ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Our method outperforms all approaches in both modalities. | comparison identity and matched condition | p. 9 (5 Experiment) |
| Ablation of MSC2F and Consistency Loss. | comparison identity and matched condition | p. 10 (5 Experiment) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Additionally, to further demonstrate the effectiveness of our multimodal approach, We conduct comparative experiments with the single-modality LiDAR-NeRF [36] and i-NGP [21], where i-NGP ... | component/input/data sensitivity | p. 10 (5 Experiment) |
| Ablation Study in pose-free setting. | component/input/data sensitivity | p. 9 (5 Experiment) |
| All ablation studies are conducted on KITTI-360 [15]. | component/input/data sensitivity | p. 9 (5 Experiment) |
| Ablation of MSC2F and Consistency Loss. | component/input/data sensitivity | p. 10 (5 Experiment) |
| Figure 1: NVS results w/ and w/o accurate poses. Compared to continuous LiDAR-Camera Fields, projecting LiDAR point clouds onto images as discrete depth priors ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| For pose estimation, we follow [3], employing standard odometry metrics: Absolute Trajectory Error (ATE) and Relative Pose Error (RPE), with rotational (RPEr) and translational ... | component/input/data sensitivity | p. 8 (5 Experiment) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our primary contributions can be delineated as follows: (1) We propose MUP, a unified pose-free framework that combines the advantages of two ... | Figure 7: Qualitative NVS results with GT- poses. MUP outperforms single-modal meth- ods i-NGP w/ and w/o point clouds and LiDAR- NeRF. Our method ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 9 (5 Experiment), p. 10 (5 Experiment), p. 10 (5 Experiment), p. 7 (Figure/Table caption), p. 4 (Figure/Table caption) |
| Primary metric/result | Our method achieves the highest pose estimation accuracy. | numeric claim only at cited anchor | p. 9 (5 Experiment) |

- Numeric sentences retained from the body:
- **p. 8 / 5 Experiment - extractive PDF cue:** All experiments were conducted on a single NVIDIA GeForce RTX 3090 GPU.
- **p. 8 / 5 Experiment - extractive PDF cue:** 768 points were uniformly sampled along each ray for two modalities.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We revisit the limitations of single-modality pose-free methods in large-scale scenes. | p. 10 (7 Conclusion) |
| body limitation/failure cue | Figure 1: NVS results w/ and w/o accurate poses. Compared to continuous LiDAR-Camera Fields, projecting LiDAR point clouds onto images as discrete depth priors ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Alignmif [37] cannot be effectively used in ill-conditioned optimization. | p. 9 (5 Experiment) |
| body limitation/failure cue | Additionally, it is not designed to handle dynamic scenes, which is a non-negligible limitation in autonomous driving scenarios. | p. 10 (5 Experiment) |
| body limitation/failure cue | Figure 5: Qualitative comparison of NVS. We compared MUP with pose-free and registration-first methods. Nope-NeRF and Colored-ICP-assisted fail due to the large-scale scene. BA-Alignmif ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Following [47, 16], we perturbed poses of car with additive noise corresponding to a standard deviation of 20 deg in rotation and 3m in ... | p. 8 (5 Experiment) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The learning rates were set as follows: 1 × 10-2, decaying to 1 × 10-4 for NeRF; 1 × 10-3, decaying to 1 × ... | p. 8 (5 Experiment) |
| All experiments were conducted on a single NVIDIA GeForce RTX 3090 GPU. | p. 8 (5 Experiment) |
| This is implemented by adjusting the learning rates of pose parameters across different modalities, as depicted in Eq. | p. 6 (4 Methodology) |
| Pn+1 = Pn -(1 -w)lrGLiDAR -w · lrGCamera, (3) where G is the gradient of the corresponding modality, Pn denotes the pose at the ... | p. 6 (4 Methodology) |
| Finally, the Image-enhanced CD is computed as LICD = ∑ (i,j)∈E CD(i,j). | p. 7 (4 Methodology) |
| Our MMG module directly computes the inter-frame CD and propagates the gradient to the poses, guiding the optimization of the poses during the ill-conditioned ... | p. 7 (4 Methodology) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 7 Conclusion - extractive PDF cue:** We revisit the limitations of single-modality pose-free methods in large-scale scenes.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: NVS results w/ and w/o accurate poses. Compared to continuous LiDAR-Camera Fields, projecting LiDAR point clouds onto images as discrete depth priors fails ...
- **p. 9 / 5 Experiment - extractive PDF cue:** Alignmif [37] cannot be effectively used in ill-conditioned optimization.
- **p. 10 / 5 Experiment - extractive PDF cue:** Additionally, it is not designed to handle dynamic scenes, which is a non-negligible limitation in autonomous driving scenarios.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Qualitative comparison of NVS. We compared MUP with pose-free and registration-first methods. Nope-NeRF and Colored-ICP-assisted fail due to the large-scale scene. BA-Alignmif struggles ...
- **p. 8 / 5 Experiment - extractive PDF cue:** Following [47, 16], we perturbed poses of car with additive noise corresponding to a standard deviation of 20 deg in rotation and 3m in translation.

- **PDF anchors reviewed:** datasets p. 8 (5 Experiment), p. 8 (5 Experiment), p. 9 (5 Experiment), p. 9 (5 Experiment), p. 10 (5 Experiment), p. 10 (5 Experiment), metrics p. 6 (Figure/Table caption), p. 8 (5 Experiment), p. 8 (5 Experiment), p. 9 (5 Experiment), p. 9 (5 Experiment), p. 10 (5 Experiment), baselines p. 7 (Figure/Table caption), p. 9 (5 Experiment), p. 10 (5 Experiment), p. 2 (Figure/Table caption), p. 9 (5 Experiment), p. 10 (5 Experiment), results p. 9 (Figure/Table caption), p. 9 (5 Experiment), p. 10 (5 Experiment), p. 10 (5 Experiment), p. 7 (Figure/Table caption), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
