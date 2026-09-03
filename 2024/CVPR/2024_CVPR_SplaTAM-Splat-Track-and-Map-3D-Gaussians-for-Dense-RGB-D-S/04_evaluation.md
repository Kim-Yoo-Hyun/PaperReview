# Evaluation - SplaTAM: Splat Track & Map 3D Gaussians for Dense RGB-D SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Keetha_SplaTAM_Splat_Track__Map_3D_Gaussians_for_Dense_RGB-D_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Keetha_SplaTAM_Splat_Track__Map_3D_Gaussians_for_Dense_RGB-D_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5. Results & Discussion), p. 6 (5. Results & Discussion), p. 7 (5. Results & Discussion), p. 7 (5. Results & Discussion), p. 8 (5. Results & Discussion), p. 1 (Figure/Table caption)): Compared to prior methods in this category [30, 54], SplaTAM still significantly outperforms, decreasing the trajectory error of the prior SOTA in this category [30] by almost 40%, from 8.92cm ...

## Evaluation Body Digest

- **p. 5 / 4. Experimental Setup - extractive body cue:** Replica [35] is the simplest benchmark as it contains synthetic scenes, highly accurate and complete (synthetic) depth maps, and small displacements between consecutive camera poses.
- **p. 6 / 5. Results & Discussion - extractive body cue:** On the relatively easy synthetic Replica [35] dataset, the de-facto evaluation benchmark, our approach reduces the trajectory error over the prior SOTA-dense baseline [30] by ...
- **p. 5 / 5. Results & Discussion - extractive body cue:** In this section, we first discuss our evaluation results on camera pose estimation for the four benchmark datasets.
- **p. 6 / 5. Results & Discussion - extractive body cue:** Therefore, we set up a novel benchmark for this using the new high-quality ScanNet++ [49] dataset.
- **p. 7 / 5. Results & Discussion - extractive body cue:** With this novel benchmark that is able to correctly evaluate Novel-View Synthesis and SLAM simultaneously, as well as our approach as a strong initial baseline ...
- **p. 7 / 5. Results & Discussion - extractive body cue:** The results for both novel-view and training-view rendering on this ScanNet++ benchmark can be found in Table 3.
- **p. 8 / 5. Results & Discussion - extractive body cue:** Furthermore, SplaTAM can be scaled up to large-scale scenes through efficient representations like OpenVDB [24].
- **p. 7 / 5. Results & Discussion - extractive body cue:** Using only an RGB loss successfully tracks the camera trajectory (although with more than 5x the error as using both).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experimental Setup (p. 5); 5. Results & Discussion (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5. Results & Discussion | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared to prior methods in this category [30, 54], SplaTAM still significantly outperforms, decreasing the trajectory error of the prior SOTA in this category ... | p. 6 (5. Results & Discussion) |
| 5. Results & Discussion | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our approach achieves much better results than the other baselines Vox-Fusion [46] and NICESLAM [54], improving over both by around 10dB in PSNR. | p. 6 (5. Results & Discussion) |
| 5. Results & Discussion | EMPIRICAL / REAL-ROBOT OR HARDWARE | Both the RGB and depth work together to achieve excellent results. | p. 7 (5. Results & Discussion) |
| 5. Results & Discussion | EMPIRICAL / REAL-ROBOT OR HARDWARE | As can be seen, our methods achieve visually excellent results over both scenes for both novel and training views. | p. 7 (5. Results & Discussion) |
| 5. Results & Discussion | EMPIRICAL / REAL-ROBOT OR HARDWARE | Although SplaTAM achieves state-of-the-art performance, we find our method to show some sensitivity to motion blur, large depth noise, and aggressive rotation. | p. 8 (5. Results & Discussion) |

## Dataset / Benchmark Role

- **p. 5 / 4. Experimental Setup - extractive body cue:** Replica [35] is the simplest benchmark as it contains synthetic scenes, highly accurate and complete (synthetic) depth maps, and small displacements between consecutive camera poses.
- **p. 6 / 5. Results & Discussion - extractive body cue:** On the relatively easy synthetic Replica [35] dataset, the de-facto evaluation benchmark, our approach reduces the trajectory error over the prior SOTA-dense baseline [30] by ...
- **p. 5 / 5. Results & Discussion - extractive body cue:** In this section, we first discuss our evaluation results on camera pose estimation for the four benchmark datasets.
- **p. 6 / 5. Results & Discussion - extractive body cue:** Therefore, we set up a novel benchmark for this using the new high-quality ScanNet++ [49] dataset.
- **p. 7 / 5. Results & Discussion - extractive body cue:** With this novel benchmark that is able to correctly evaluate Novel-View Synthesis and SLAM simultaneously, as well as our approach as a strong initial baseline ...
- **p. 7 / 5. Results & Discussion - extractive body cue:** The results for both novel-view and training-view rendering on this ScanNet++ benchmark can be found in Table 3.
- **p. 8 / 5. Results & Discussion - extractive body cue:** Furthermore, SplaTAM can be scaled up to large-scale scenes through efficient representations like OpenVDB [24].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. SplaTAM enables precise camera tracking and high-fidelity reconstruction for dense simultaneous localization and mapping (SLAM) in challenging real-world scenarios. SplaTAM achieves this by ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of SplaTAM. Top-Left: The input to our approach at each timestep is the current RGB-D frame and the 3D Gaussian Map Representation ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Online Camera-Pose Estimation Results on Four Datasets (ATE RMSE ↓[cm]). Our method consistently outperforms all the SOTA-dense baselines on ScanNet++, Replica, and TUM-RGBD, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Quantitative Train View Rendering Performance on Replica [35]. SplaTAM is comparable to the SOTA baseline, Point-SLAM [30] and consistently outperforms the other dense ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Novel & Train View Rendering Performance on Scan- Net++ [49]. SplaTAM provides high-fidelity performance on both training views seen during SLAM and held-out ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Color & Depth Loss Ablation on Replica/Room 0. Velo. Sil. Sil. ATE Dep. L1 PSNR Prop.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Camera Tracking Ablations on Replica/Room 0. depth loss. In Table 4, we ablate the decision to use both and investigate the performance of ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3. Renderings on ScanNet++ [49]. Our method, SplaTAM, renders color & depth for the novel & train views with fidelity comparable to the ground ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Replica [35] is the simplest benchmark as it contains synthetic scenes, highly accurate and complete (synthetic) depth maps, and small displacements between consecutive camera ... | embodiment, simulator version and control stack | p. 5 (4. Experimental Setup), p. 6 (5. Results & Discussion) |
| Task/environment | On the relatively easy synthetic Replica [35] dataset, the de-facto evaluation benchmark, our approach reduces the trajectory error over the prior SOTA-dense baseline [30] ... | reset, timeout, object/scene variation | p. 6 (5. Results & Discussion), p. 5 (5. Results & Discussion) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (3. Method), p. 4 (3. Method) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 3 (3. Method), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Using only an RGB loss successfully tracks the camera trajectory (although with more than 5x the error as using both). | definition/direction/unit from same section | p. 7 (5. Results & Discussion) |
| Setting the silhouette threshold to 0.99 allows the loss to be applied on well-optimized pixels in the map, thereby leading to an important 5x ... | definition/direction/unit from same section | p. 8 (5. Results & Discussion) |
| In contrast, our approach successfully manages to track the camera over both sequences giving an average trajectory error of only 1.2cm. | definition/direction/unit from same section | p. 6 (5. Results & Discussion) |
| Our method obtains an incredibly accurate reconstruction with a depth error of only around 2cm in novel views and 1.3cm in training views. | definition/direction/unit from same section | p. 7 (5. Results & Discussion) |
| For camera pose estimation tracking we use the average absolute trajectory error (ATE RMSE). | definition/direction/unit from same section | p. 5 (4. Experimental Setup) |
| Compared to prior methods in this category [30, 54], SplaTAM still significantly outperforms, decreasing the trajectory error of the prior SOTA in this category ... | definition/direction/unit from same section | p. 6 (5. Results & Discussion) |
| For depth rendering performance we use Depth L1 loss. | definition/direction/unit from same section | p. 5 (4. Experimental Setup) |
| Each iteration of our approach renders a full 1200x980 pixel image (∼1.2 mil pixels) to apply the loss for both tracking and mapping. | definition/direction/unit from same section | p. 8 (5. Results & Discussion) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The main baseline method we compare to is Point-SLAM [30], the previous state-of-the-art (SOTA) method for dense radiance-field-based SLAM. | comparison identity and matched condition | p. 5 (4. Experimental Setup) |
| Our method consistently outperforms all the SOTA-dense baselines on ScanNet++, Replica, and TUM-RGBD, while providing competitive performance on Orig-ScanNet [5]. | comparison identity and matched condition | p. 6 (5. Results & Discussion) |
| Compared to prior methods in this category [30, 54], SplaTAM still significantly outperforms, decreasing the trajectory error of the prior SOTA in this category ... | comparison identity and matched condition | p. 6 (5. Results & Discussion) |
| SplaTAM is comparable to the SOTA baseline, Point-SLAM [30] and consistently outperforms the other dense SLAM methods by a large margin. | comparison identity and matched condition | p. 7 (5. Results & Discussion) |
| Furthermore, for all comparisons to prior baselines, we present results as the average of 3 seeds (0-2) and use seed 0 for the ablations. | comparison identity and matched condition | p. 5 (4. Experimental Setup) |
| Figure 1. SplaTAM enables precise camera tracking and high-fidelity reconstruction for dense simultaneous localization and mapping (SLAM) in challenging real-world scenarios. SplaTAM achieves this ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Furthermore, for all comparisons to prior baselines, we present results as the average of 3 seeds (0-2) and use seed 0 for the ablations. | component/input/data sensitivity | p. 5 (4. Experimental Setup) |
| Finally, we discuss pipeline ablations and provide a runtime comparison. | component/input/data sensitivity | p. 5 (5. Results & Discussion) |
| On ScanNet++ [49], both SOTA SLAM approaches Point-SLAM [30] and ORB-SLAM3 [3] (RGB-D variant) completely fail to correctly track the camera pose due to ... | component/input/data sensitivity | p. 6 (5. Results & Discussion) |
| Color & Depth Loss Ablation on Replica/Room 0. | component/input/data sensitivity | p. 7 (5. Results & Discussion) |
| Camera Tracking Ablations on Replica/Room 0. depth loss. | component/input/data sensitivity | p. 7 (5. Results & Discussion) |
| Silhouette is critical as without it tracking completely fails. | component/input/data sensitivity | p. 8 (5. Results & Discussion) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We show across all our experiments on simulated and real data that our approach, SplaTAM, achieves state-of-the-art results compared to all previous approaches for ... | Compared to prior methods in this category [30, 54], SplaTAM still significantly outperforms, decreasing the trajectory error of the prior SOTA in this category ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5. Results & Discussion), p. 6 (5. Results & Discussion), p. 7 (5. Results & Discussion), p. 7 (5. Results & Discussion), p. 8 (5. Results & Discussion), p. 1 (Figure/Table caption) |
| Primary metric/result | Our approach achieves much better results than the other baselines Vox-Fusion [46] and NICESLAM [54], improving over both by around 10dB in PSNR. | numeric claim only at cited anchor | p. 6 (5. Results & Discussion) |

- Numeric sentences retained from the body:
- **p. 5 / 4. Experimental Setup - extractive body cue:** Furthermore, for all comparisons to prior baselines, we present results as the average of 3 seeds (0-2) and use seed 0 for the ablations.
- **p. 6 / 5. Results & Discussion - extractive body cue:** R0 R1 R2 Of0 Of1 Of2 Of3 Of4 DROID-SLAM [39] 0.38 0.53 0.38 0.45 0.35 0.24 0.36 0.33 0.43 Vox-Fusion [46] 3.09 1.37 4.70 1.47 ...
- **p. 6 / 5. Results & Discussion - extractive body cue:** Kintinuous [42] 4.84 3.70 7.10 7.50 2.90 3.00 ElasticFusion [43] 6.91 2.53 6.83 21.49 1.17 2.52 ORB-SLAM2 [23] 1.98 1.60 2.20 4.70 0.40 1.00 NICE-SLAM ...
- **p. 6 / 5. Results & Discussion - extractive body cue:** 0000 0059 0106 0169 0181 0207 Vox-Fusion [46] 26.90 68.84 24.18 8.41 27.28 23.30 9.41 NICE-SLAM [54] 10.70 12.00 14.00 7.90 10.90 13.40 6.20 Point-SLAM ...
- **p. 7 / 5. Results & Discussion - extractive body cue:** R0 R1 R2 Of0 Of1 Of2 Of3 Of4 Vox-Fusion [46] PSNR ↑24.41 22.39 22.36 23.92 27.79 29.83 20.33 23.47 25.21 SSIM ↑0.80 0.68 0.75 0.80 ...
- **p. 7 / 5. Results & Discussion - extractive body cue:** Using only an RGB loss successfully tracks the camera trajectory (although with more than 5x the error as using both).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 3. Renderings on ScanNet++ [49]. Our method, SplaTAM, renders color & depth for the novel & train views with fidelity comparable to the ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Figure 1. SplaTAM enables precise camera tracking and high-fidelity reconstruction for dense simultaneous localization and mapping (SLAM) in challenging real-world scenarios. SplaTAM achieves this ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | However, all current SLAM benchmarks don't have a hold-out set of images separate from the camera trajectory that the SLAM algorithm estimates, so they ... | p. 6 (5. Results & Discussion) |
| body limitation/failure cue | In contrast, Point-SLAM [30] fails at camera-pose tracking and overfits to the training views, and isn't able to successfully render novel views at all. | p. 7 (5. Results & Discussion) |
| body limitation/failure cue | Since Point-SLAM [30] fails to successfully estimate the camera poses and build a good map, it also completely fails on the task of novel-view ... | p. 7 (5. Results & Discussion) |
| body limitation/failure cue | Silhouette is critical as without it tracking completely fails. | p. 8 (5. Results & Discussion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Furthermore, for all comparisons to prior baselines, we present results as the average of 3 seeds (0-2) and use seed 0 for the ablations. | p. 5 (4. Experimental Setup) |
| In practice, to keep the batch size manageable, a selected subset of keyframes that overlap with the most recent frame are optimized. | p. 4 (3. Method) |
| Given a new RGB-D frame t + 1, our SLAM system performs the following steps (see Fig. | p. 4 (3. Method) |
| Finally, we discuss pipeline ablations and provide a runtime comparison. | p. 5 (5. Results & Discussion) |
| Runtime on Replica/R0 using a RTX 3080 Ti. ing. | p. 8 (5. Results & Discussion) |
| In Table 6, we compare our runtime to NICE-SLAM [54] and Point-SLAM [30] on a Nvidia RTX 3080 Ti. | p. 8 (5. Results & Discussion) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3. Renderings on ScanNet++ [49]. Our method, SplaTAM, renders color & depth for the novel & train views with fidelity comparable to the ground ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. SplaTAM enables precise camera tracking and high-fidelity reconstruction for dense simultaneous localization and mapping (SLAM) in challenging real-world scenarios. SplaTAM achieves this by ...
- **p. 6 / 5. Results & Discussion - extractive body cue:** However, all current SLAM benchmarks don't have a hold-out set of images separate from the camera trajectory that the SLAM algorithm estimates, so they cannot ...
- **p. 7 / 5. Results & Discussion - extractive body cue:** In contrast, Point-SLAM [30] fails at camera-pose tracking and overfits to the training views, and isn't able to successfully render novel views at all.
- **p. 7 / 5. Results & Discussion - extractive body cue:** Since Point-SLAM [30] fails to successfully estimate the camera poses and build a good map, it also completely fails on the task of novel-view synthesis.
- **p. 8 / 5. Results & Discussion - extractive body cue:** Silhouette is critical as without it tracking completely fails.

- **Evidence anchors reviewed:** datasets p. 5 (4. Experimental Setup), p. 6 (5. Results & Discussion), p. 5 (5. Results & Discussion), p. 6 (5. Results & Discussion), p. 7 (5. Results & Discussion), p. 7 (5. Results & Discussion), metrics p. 7 (5. Results & Discussion), p. 8 (5. Results & Discussion), p. 6 (5. Results & Discussion), p. 7 (5. Results & Discussion), p. 5 (4. Experimental Setup), p. 6 (5. Results & Discussion), baselines p. 5 (4. Experimental Setup), p. 6 (5. Results & Discussion), p. 6 (5. Results & Discussion), p. 7 (5. Results & Discussion), p. 5 (4. Experimental Setup), p. 1 (Figure/Table caption), results p. 6 (5. Results & Discussion), p. 6 (5. Results & Discussion), p. 7 (5. Results & Discussion), p. 7 (5. Results & Discussion), p. 8 (5. Results & Discussion), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
