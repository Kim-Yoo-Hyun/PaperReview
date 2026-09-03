# Evaluation - Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Deng_Boost_3D_Reconstruction_using_Diffusion-based_Monocular_Camera_Calibration_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Deng_Boost_3D_Reconstruction_using_Diffusion-based_Monocular_Camera_Calibration_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (7.7. The Importance of Principal Point Evaluation), p. 5 (7.8. The Importance of camera image in metric), p. 2 (6.3. More implementation details and discussions), p. 2 (6.3. More implementation details and discussions), p. 3 (7.6. Single view 3D reconstuction), p. 3 (7.6. Single view 3D reconstuction)): Despite targeting metric depth, we achieve performance comparable to SoTA affine-invariant depth methods.

## Evaluation Body Digest

- **p. 1 / 6.2. Metric depth prediction - extractive body cue:** Dataset Images Scene Intrinsic Training Set NuScenes [7] 28k Outdoor Calibrated KITTI [11] 18 k Outdoor Calibrated CityScapes [11] 23k Outdoor Calibrated NYUv2 [44] 6k ...
- **p. 1 / 6.2. Metric depth prediction - extractive body cue:** Dataset Images Scene Acquisition Training Set Hypersim [52] 54k Indoor Synthetic Virtual KITTI [6] 20k Outdoor Synthetic Taskonomy [87] 40M Indoor RGB-D TartanAir [74] 305k ...
- **p. 4 / 7.7. The Importance of Principal Point Evaluation - extractive body cue:** NuScenes KITTI CityScapes NYUv2 eb 0.051 0.021 0.055 0.050 ˆeb 0.007 0.014 0.011 0.009 ensure more robust estimation and support future broader applications and datasets ...
- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** Method Waymo RGBD ScanNet MVS Scenes11 Average ef eb ef eb ef eb ef eb ef eb ef eb Ours-small 0.138 0.033 0.051 0.012 0.084 ...
- **p. 3 / 7.6. Single view 3D reconstuction - extractive body cue:** We present the predicted metric depth in both outdoor and indoor scenes.
- **p. 3 / 7.6. Single view 3D reconstuction - extractive body cue:** Nuscenes DIODE(Outdoor) DIODE(Outdoor) Eth3D NYUv2 DIODE(Indoor) VOID RGB GT Ours UniDepth Metric3D m Figure 9.
- **p. 4 / 7.7. The Importance of Principal Point Evaluation - extractive body cue:** Quantitative Comparison on 5 Zero-shot Affine-invariant Depth Benchmarks.
- **p. 5 / 7.8. The Importance of camera image in metric - extractive body cue:** Metrology of in-the-wild scenes for UniDepth.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 6. Implementation Details (p. 1); 6.3. More implementation details and discussions (p. 1); 7. More experimental Results (p. 2); 7.7. The Importance of Principal Point Evaluation (p. 3).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 7.7. The Importance of Principal Point Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Despite targeting metric depth, we achieve performance comparable to SoTA affine-invariant depth methods. | p. 4 (7.7. The Importance of Principal Point Evaluation) |
| 7.8. The Importance of camera image in metric | EMPIRICAL / SOURCE-REPORTED EVALUATION | With intrinsic cues, our method achieves more accurate and better-aligned reconstructions. results on three additional datasets in Tab.12, complementing the findings in Tab.5. | p. 5 (7.8. The Importance of camera image in metric) |
| 6.3. More implementation details and discussions | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results demonstrate that Dust3r achieves more accurate reconstruction when equipped with our estimated intrinsics. | p. 2 (6.3. More implementation details and discussions) |
| 6.3. More implementation details and discussions | EMPIRICAL / SOURCE-REPORTED EVALUATION | Then we employ single-step diffusion at timestamp T to generate depth latent code ˆzd, which is then decoded into predicted metric depth ˆd. ground ... | p. 2 (6.3. More implementation details and discussions) |
| 7.6. Single view 3D reconstuction | EMPIRICAL / SOURCE-REPORTED EVALUATION | Zero-Shot Metric Depth Estimation Results. | p. 3 (7.6. Single view 3D reconstuction) |

## Dataset / Benchmark Role

- **p. 1 / 6.2. Metric depth prediction - extractive body cue:** Dataset Images Scene Intrinsic Training Set NuScenes [7] 28k Outdoor Calibrated KITTI [11] 18 k Outdoor Calibrated CityScapes [11] 23k Outdoor Calibrated NYUv2 [44] 6k ...
- **p. 1 / 6.2. Metric depth prediction - extractive body cue:** Dataset Images Scene Acquisition Training Set Hypersim [52] 54k Indoor Synthetic Virtual KITTI [6] 20k Outdoor Synthetic Taskonomy [87] 40M Indoor RGB-D TartanAir [74] 305k ...
- **p. 4 / 7.7. The Importance of Principal Point Evaluation - extractive body cue:** NuScenes KITTI CityScapes NYUv2 eb 0.051 0.021 0.055 0.050 ˆeb 0.007 0.014 0.011 0.009 ensure more robust estimation and support future broader applications and datasets ...
- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** Method Waymo RGBD ScanNet MVS Scenes11 Average ef eb ef eb ef eb ef eb ef eb ef eb Ours-small 0.138 0.033 0.051 0.012 0.084 ...
- **p. 3 / 7.6. Single view 3D reconstuction - extractive body cue:** We present the predicted metric depth in both outdoor and indoor scenes.
- **p. 3 / 7.6. Single view 3D reconstuction - extractive body cue:** Nuscenes DIODE(Outdoor) DIODE(Outdoor) Eth3D NYUv2 DIODE(Indoor) VOID RGB GT Ours UniDepth Metric3D m Figure 9.
- **p. 4 / 7.7. The Importance of Principal Point Evaluation - extractive body cue:** Quantitative Comparison on 5 Zero-shot Affine-invariant Depth Benchmarks.
- **p. 5 / 7.8. The Importance of camera image in metric - extractive body cue:** Metrology of in-the-wild scenes for UniDepth.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Table 6. Datasets List for camera calibration. List of the training and testing datasets: number of images, scene type, and method of calibration. SfM: Structure-from-Motion.
- **p. 1 / Figure/Table caption - extractive body cue:** Table 7. Datasets List for Metric Depth estimation. List of the training and testing datasets for metric depth estimation: number of images, scene type, and ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 3: Our Camera Image is image-dependent, unlike other camera representations that are not. For other methods, lines can be plotted directly based on different ...
- **p. 1 / Figure/Table caption - extractive body cue:** Tab. 9: We assess the generalization ability across five zero- shot datasets by aligning the predicted depth ˆd to the ground- truth depth d with ...
- **p. 1 / Figure/Table caption - extractive body cue:** Tab. 10: The pose estimation is compared against pseudo
- **p. 2 / Figure/Table caption - extractive body cue:** Table 8. Monocular Camera Calibration on Zero-Shot Datasets. We report the calibration errors for both focal length and optical center. Small means we train our ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 8. The overview of metric depth training pipeline. The encoded image and camera image zx and zc are concatenated and sent to pretrained U-Net. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 9. Zero-Shot Metric Depth Estimation Results. We present the predicted metric depth in both outdoor and indoor scenes. Our method provides more detailed results ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Dataset Images Scene Intrinsic Training Set NuScenes [7] 28k Outdoor Calibrated KITTI [11] 18 k Outdoor Calibrated CityScapes [11] 23k Outdoor Calibrated NYUv2 [44] ... | embodiment, simulator version and control stack | p. 1 (6.2. Metric depth prediction), p. 1 (6.2. Metric depth prediction) |
| Task/environment | Dataset Images Scene Acquisition Training Set Hypersim [52] 54k Indoor Synthetic Virtual KITTI [6] 20k Outdoor Synthetic Taskonomy [87] 40M Indoor RGB-D TartanAir [74] ... | reset, timeout, object/scene variation | p. 1 (6.2. Metric depth prediction), p. 4 (7.7. The Importance of Principal Point Evaluation) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (6.3. More implementation details and discussions), p. 1 (6.2. Metric depth prediction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (6.3. More implementation details and discussions), p. 1 (6.2. Metric depth prediction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Then we employ single-step diffusion at timestamp T to generate depth latent code ˆzd, which is then decoded into predicted metric depth ˆd. ground ... | definition/direction/unit from same section | p. 2 (6.3. More implementation details and discussions) |
| Principal points error We compare the error of principle point estimation when assuming principal point lies at the image center with the error of ... | definition/direction/unit from same section | p. 4 (7.7. The Importance of Principal Point Evaluation) |
| Our method provides more detailed results and recovers accurate metric depths. camera intrinsics and metric depth map. | definition/direction/unit from same section | p. 3 (7.6. Single view 3D reconstuction) |
| We demonstrate the robustness of our intrinsic estimation and depth prediction through in-the-wild single-view 3D reconstructions. | definition/direction/unit from same section | p. 3 (7.6. Single view 3D reconstuction) |
| Our method accurately recovers real-world metrics while demonstrating robustness to variations in focal length. | definition/direction/unit from same section | p. 4 (7.7. The Importance of Principal Point Evaluation) |
| We report the calibration errors for both focal length and optical center. | definition/direction/unit from same section | p. 2 (6.3. More implementation details and discussions) |
| Without the aggregation, the standard deviation is sometimes not negligible, as presented in Tab. | definition/direction/unit from same section | p. 5 (7.9. Test-time ensembling) |
| This significantly minimizes the randomness of the diffusion model, as evidenced by the small standard deviation in Tab. | definition/direction/unit from same section | p. 5 (7.9. Test-time ensembling) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 10: The pose estimation is compared against pseudo | comparison identity and matched condition | p. 1 (6.3. More implementation details and discussions) |
| Notably, our training set includes more data compared to He et al. | comparison identity and matched condition | p. 1 (6.1. Camera intrinsic prediction) |
| The quantitative comparison for relative depth is shown in Tab. | comparison identity and matched condition | p. 2 (7.2. Relative Depth) |
| To validate this, we conduct an ablation study comparing | comparison identity and matched condition | p. 3 (7.7. The Importance of Principal Point Evaluation) |
| Quantitative Comparison on 5 Zero-shot Affine-invariant Depth Benchmarks. | comparison identity and matched condition | p. 4 (7.7. The Importance of Principal Point Evaluation) |
| Despite targeting metric depth, we achieve performance comparable to SoTA affine-invariant depth methods. | comparison identity and matched condition | p. 4 (7.7. The Importance of Principal Point Evaluation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation study on the effectiveness of camera images for metric depth estimation. ibims Diode indoor Diode outdoor w. cam img 88.7 50.1 41.0 w.o ... | component/input/data sensitivity | p. 5 (7.8. The Importance of camera image in metric) |
| Figure 8. The overview of metric depth training pipeline. The encoded image and camera image zx and zc are concatenated and sent to pretrained ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| To validate this, we conduct an ablation study comparing | component/input/data sensitivity | p. 3 (7.7. The Importance of Principal Point Evaluation) |
| Quantitative Comparison on 5 Zero-shot Affine-invariant Depth Benchmarks. | component/input/data sensitivity | p. 4 (7.7. The Importance of Principal Point Evaluation) |
| Despite targeting metric depth, we achieve performance comparable to SoTA affine-invariant depth methods. | component/input/data sensitivity | p. 4 (7.7. The Importance of Principal Point Evaluation) |
| Without the aggregation, the standard deviation is sometimes not negligible, as presented in Tab. | component/input/data sensitivity | p. 5 (7.9. Test-time ensembling) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In contrast, our method is specifically designed to recover camera intrinsics. | Despite targeting metric depth, we achieve performance comparable to SoTA affine-invariant depth methods. | PDF body cue; verify exact table/figure and matched conditions | p. 4 (7.7. The Importance of Principal Point Evaluation), p. 5 (7.8. The Importance of camera image in metric), p. 2 (6.3. More implementation details and discussions), p. 2 (6.3. More implementation details and discussions), p. 3 (7.6. Single view 3D reconstuction), p. 3 (7.6. Single view 3D reconstuction) |
| Primary metric/result | With intrinsic cues, our method achieves more accurate and better-aligned reconstructions. results on three additional datasets in Tab.12, complementing the findings in Tab.5. | numeric claim only at cited anchor | p. 5 (7.8. The Importance of camera image in metric) |

- Numeric sentences retained from the body:
- **p. 6 / 7.9. Test-time ensembling - extractive body cue:** Waymo RGBD ScanNet MVS Scenes11 Average ef 0.115 ± 0.008 0.041 ± 0.002 0.089 ± 0.002 0.087 ± 0.006 0.061 ± 0.006 0.078 ± 0.006 ...
- **p. 6 / 7.9. Test-time ensembling - extractive body cue:** Waymo RGBD ScanNet MVS Scenes11 Average ef 0.115 ± 0.035 0.041 ± 0.010 0.089 ± 0.024 0.087 ± 0.008 0.061 ± 0.009 0.078 ± 0.017 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While it shows some limitations in focal estimation, this leads to slightly less accurate visualizations. | p. 2 (7.3. Metrologie) |
| body limitation/failure cue | This process is less robust and often converges to a local minimum. | p. 2 (6.3. More implementation details and discussions) |
| body limitation/failure cue | We have a significant amount of data where the principal point does not lie at the image center in certain datasets, and our model ... | p. 3 (7.7. The Importance of Principal Point Evaluation) |
| body limitation/failure cue | We demonstrate the robustness of our intrinsic estimation and depth prediction through in-the-wild single-view 3D reconstructions. | p. 3 (7.6. Single view 3D reconstuction) |
| body limitation/failure cue | The camera image (intrinsic information) is essential for robust and accurate metric depth estimation. | p. 4 (7.8. The Importance of camera image in metric) |
| body limitation/failure cue | Our method accurately recovers real-world metrics while demonstrating robustness to variations in focal length. | p. 4 (7.7. The Importance of Principal Point Evaluation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For metric depth estimation, we use the same optimizer and learning rate with a total batch size of 96, and the training process takes ... | p. 1 (6. Implementation Details) |
| To train camera intrinsic estimation model, we employ the AdamW optimizer with a learning rate of 3e-5 and train the model for 30,000 iterations ... | p. 1 (6. Implementation Details) |
| The encoded image and camera image zx and zc are concatenated and sent to pretrained U-Net. | p. 2 (6.3. More implementation details and discussions) |
| Then we employ single-step diffusion at timestamp T to generate depth latent code ˆzd, which is then decoded into predicted metric depth ˆd. ground ... | p. 2 (6.3. More implementation details and discussions) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / 7.3. Metrologie - extractive body cue:** While it shows some limitations in focal estimation, this leads to slightly less accurate visualizations.
- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** This process is less robust and often converges to a local minimum.
- **p. 3 / 7.7. The Importance of Principal Point Evaluation - extractive body cue:** We have a significant amount of data where the principal point does not lie at the image center in certain datasets, and our model effectively ...
- **p. 3 / 7.6. Single view 3D reconstuction - extractive body cue:** We demonstrate the robustness of our intrinsic estimation and depth prediction through in-the-wild single-view 3D reconstructions.
- **p. 4 / 7.8. The Importance of camera image in metric - extractive body cue:** The camera image (intrinsic information) is essential for robust and accurate metric depth estimation.
- **p. 4 / 7.7. The Importance of Principal Point Evaluation - extractive body cue:** Our method accurately recovers real-world metrics while demonstrating robustness to variations in focal length.

- **Evidence anchors reviewed:** datasets p. 1 (6.2. Metric depth prediction), p. 1 (6.2. Metric depth prediction), p. 4 (7.7. The Importance of Principal Point Evaluation), p. 2 (6.3. More implementation details and discussions), p. 3 (7.6. Single view 3D reconstuction), p. 3 (7.6. Single view 3D reconstuction), metrics p. 2 (6.3. More implementation details and discussions), p. 4 (7.7. The Importance of Principal Point Evaluation), p. 3 (7.6. Single view 3D reconstuction), p. 3 (7.6. Single view 3D reconstuction), p. 4 (7.7. The Importance of Principal Point Evaluation), p. 2 (6.3. More implementation details and discussions), baselines p. 1 (6.3. More implementation details and discussions), p. 1 (6.1. Camera intrinsic prediction), p. 2 (7.2. Relative Depth), p. 3 (7.7. The Importance of Principal Point Evaluation), p. 4 (7.7. The Importance of Principal Point Evaluation), p. 4 (7.7. The Importance of Principal Point Evaluation), results p. 4 (7.7. The Importance of Principal Point Evaluation), p. 5 (7.8. The Importance of camera image in metric), p. 2 (6.3. More implementation details and discussions), p. 2 (6.3. More implementation details and discussions), p. 3 (7.6. Single view 3D reconstuction), p. 3 (7.6. Single view 3D reconstuction).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
