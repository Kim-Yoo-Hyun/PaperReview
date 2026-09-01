# Evaluation - Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Deng_Boost_3D_Reconstruction_using_Diffusion-based_Monocular_Camera_Calibration_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Deng_Boost_3D_Reconstruction_using_Diffusion-based_Monocular_Camera_Calibration_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.3. Depth Evaluation), p. 7 (4.4. More 3D Vision Tasks), p. 6 (4.2. Camera Intrinsic Evaluation), p. 7 (4.5. Ablation Study), p. 8 (4.5. Ablation Study), p. 8 (4.5. Ablation Study)): Our work significantly outperforms strong baselines such as Metric3D [85] by a large margin, and achieves comparable performance with the SOTA work Unidepth [46].

## Evaluation Body Digest

- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** For camera intrinsic estimation, the training data is sourced from a variety of datasets, including NuScenes [7], KITTI [19], CityScapes [11], NYUv2 [44], SUN3D [78], ...
- **p. 6 / 4.2. Camera Intrinsic Evaluation - extractive PDF cue:** Notably, our method also performs well on the highly challenging Scenes11 dataset [10], which features randomly shaped, moving objects, further demonstrating its robustness in extreme ...
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** We adopt Waymo [67], RGBD [65], ScanNet [13], MVS [16], and Scenes11 [10] datasets for zeroshot testing.
- **p. 6 / 4.2. Camera Intrinsic Evaluation - extractive PDF cue:** Among the methods, Unidepth [46] shows the weakest performance, particularly in real-world, unconstrained scenarios such as the MVS dataset.
- **p. 7 / 4.4. More 3D Vision Tasks - extractive PDF cue:** We present the predicted metric depth in both various scenes.
- **p. 7 / 4.4. More 3D Vision Tasks - extractive PDF cue:** NuScenes Ibims ETH3D RGB GT Ours UniDepth Metric3D m Figure 5.
- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** Our method accurately recovers real-world metrics and demonstrates robustness to variations in focal length. in Tab.
- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** Omitting the camera image representation slightly reduces accuracy and we further justify the importance of the camera image in metric depth estimation with evaluation on ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Setup (p. 5); 4.2. Camera Intrinsic Evaluation (p. 6); 4.3. Depth Evaluation (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Depth Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our work significantly outperforms strong baselines such as Metric3D [85] by a large margin, and achieves comparable performance with the SOTA work Unidepth [46]. | p. 6 (4.3. Depth Evaluation) |
| 4.4. More 3D Vision Tasks | EMPIRICAL / REAL-ROBOT OR HARDWARE | 13 of the supplementary, reconstructions without intrinsic cues exhibit notable distortions and misalignments, whereas incorporating intrinsic cues significantly improves accuracy and alignment. | p. 7 (4.4. More 3D Vision Tasks) |
| 4.2. Camera Intrinsic Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown, our method achieves the highest calibration accuracy. | p. 6 (4.2. Camera Intrinsic Evaluation) |
| 4.5. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | While multi-resolution noise[32] improves performance slightly, it remains suboptimal. | p. 7 (4.5. Ablation Study) |
| 4.5. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method demonstrates superior foreground-background differentiation (e.g., flower) and improved understanding (e.g., wall painting). | p. 8 (4.5. Ablation Study) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** For camera intrinsic estimation, the training data is sourced from a variety of datasets, including NuScenes [7], KITTI [19], CityScapes [11], NYUv2 [44], SUN3D [78], ...
- **p. 6 / 4.2. Camera Intrinsic Evaluation - extractive PDF cue:** Notably, our method also performs well on the highly challenging Scenes11 dataset [10], which features randomly shaped, moving objects, further demonstrating its robustness in extreme ...
- **p. 5 / 4.1. Experimental Setup - extractive PDF cue:** We adopt Waymo [67], RGBD [65], ScanNet [13], MVS [16], and Scenes11 [10] datasets for zeroshot testing.
- **p. 6 / 4.2. Camera Intrinsic Evaluation - extractive PDF cue:** Among the methods, Unidepth [46] shows the weakest performance, particularly in real-world, unconstrained scenarios such as the MVS dataset.
- **p. 7 / 4.4. More 3D Vision Tasks - extractive PDF cue:** We present the predicted metric depth in both various scenes.
- **p. 7 / 4.4. More 3D Vision Tasks - extractive PDF cue:** NuScenes Ibims ETH3D RGB GT Ours UniDepth Metric3D m Figure 5.
- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** Our method accurately recovers real-world metrics and demonstrates robustness to variations in focal length. in Tab.
- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** Omitting the camera image representation slightly reduces accuracy and we further justify the importance of the camera image in metric depth estimation with evaluation on ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1. Images generated using text prompts that specify different focal lengths. images generated by a stable diffusion model [53] using sim- ilar text prompts ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Visualization of incidence map and Camera Image. We show the input RGB image, the incidence map and our proposed Camera Image for reference. ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Error analysis of camera representations. We first use pre-trained VAE to encode and decode each camera representation, and plot the FoV reconstruction errors ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. The overview training framework of DM-Calib. The input image x and the camera image c are first encoded into latent space using a ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Monocular Camera Calibration on Zero-Shot Datasets. We report the calibration errors for both focal length and optical center. †: focuses on focal length ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Zero-Shot Metric Depth Estimation Results. We present the predicted metric depth in both various scenes. Our method provides more detailed results and recovers ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison on Zero-Shot Metric Depth Evaluation. We achieve comparable precision to state-of-the-art models while utilizing less training data.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Relative distance error. We compare the reconstruction performance with and without intrinsic cues. Sofa Car Pavilion StoneWall w/o. cue 1.67

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For camera intrinsic estimation, the training data is sourced from a variety of datasets, including NuScenes [7], KITTI [19], CityScapes [11], NYUv2 [44], SUN3D ... | embodiment, simulator version and control stack | p. 5 (4.1. Experimental Setup), p. 6 (4.2. Camera Intrinsic Evaluation) |
| Task/environment | Notably, our method also performs well on the highly challenging Scenes11 dataset [10], which features randomly shaped, moving objects, further demonstrating its robustness in ... | reset, timeout, object/scene variation | p. 6 (4.2. Camera Intrinsic Evaluation), p. 5 (4.1. Experimental Setup) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.2. Camera Image Representation), p. 4 (3.2. Camera Image Representation) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3. Method), p. 3 (3.1. Preliminaries on Diffusion Model) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Incorporating our camera image representation significantly reduces the error, and the combination of both strategies produces the best results, demonstrating their complementary effectiveness. | definition/direction/unit from same section | p. 7 (4.5. Ablation Study) |
| Table 3. Relative distance error. We compare the reconstruction performance with and without intrinsic cues. Sofa Car Pavilion StoneWall w/o. cue 1.67 | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Compared to Metric3D[85], our method provides more accurate distance estimates across different focal lengths and demonstrates robustness in both outdoor and indoor scenarios (see ... | definition/direction/unit from same section | p. 6 (4.4. More 3D Vision Tasks) |
| For camera intrinsic estimation, we follow the evaluation protocol of [23, 96] using the relative error: 7114 | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| As shown, our method achieves the highest calibration accuracy. | definition/direction/unit from same section | p. 6 (4.2. Camera Intrinsic Evaluation) |
| Omitting the camera image representation slightly reduces accuracy and we further justify the importance of the camera image in metric depth estimation with evaluation ... | definition/direction/unit from same section | p. 8 (4.5. Ablation Study) |
| Our method accurately recovers real-world metrics and demonstrates robustness to variations in focal length. in Tab. | definition/direction/unit from same section | p. 8 (4.5. Ablation Study) |
| Figure 3. Error analysis of camera representations. We first use pre-trained VAE to encode and decode each camera representation, and plot the FoV reconstruction ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our work significantly outperforms strong baselines such as Metric3D [85] by a large margin, and achieves comparable performance with the SOTA work Unidepth [46]. | comparison identity and matched condition | p. 6 (4.3. Depth Evaluation) |
| For metric depth estimation, we compare our method with 4 state-of-the-art methods. | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| We achieve comparable precision to state-of-the-art models while utilizing less training data. | comparison identity and matched condition | p. 7 (4.4. More 3D Vision Tasks) |
| Figure 1. Images generated using text prompts that specify different focal lengths. images generated by a stable diffusion model [53] using sim- ilar text ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Ablation Study on Camera Calibration. | comparison identity and matched condition | p. 7 (4.5. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We evaluate the effectiveness of our proposed camera image representation and multi-resolution noise strategy through an ablation study on the GSV dataset [2], which ... | component/input/data sensitivity | p. 7 (4.5. Ablation Study) |
| [73] on our self-captured images with and without our estimated intrinsics. | component/input/data sensitivity | p. 6 (4.4. More 3D Vision Tasks) |
| Despite being designed for metric depth, our model achieves performance comparable to methods tailored for affine-invariant depth. | component/input/data sensitivity | p. 6 (4.3. Depth Evaluation) |
| Ablation on Metric Depth Estimation. | component/input/data sensitivity | p. 7 (4.5. Ablation Study) |
| Zero-shot qualitative affine-invariant depth results. | component/input/data sensitivity | p. 8 (4.5. Ablation Study) |
| Figure 4. The overview training framework of DM-Calib. The input image x and the camera image c are first encoded into latent space using ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, our main contributions are: • We introduce the Camera Image, a novel image-based representation specifically designed to encode camera intrinsic, optimized to ... | Our work significantly outperforms strong baselines such as Metric3D [85] by a large margin, and achieves comparable performance with the SOTA work Unidepth [46]. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.3. Depth Evaluation), p. 7 (4.4. More 3D Vision Tasks), p. 6 (4.2. Camera Intrinsic Evaluation), p. 7 (4.5. Ablation Study), p. 8 (4.5. Ablation Study), p. 8 (4.5. Ablation Study) |
| Primary metric/result | 13 of the supplementary, reconstructions without intrinsic cues exhibit notable distortions and misalignments, whereas incorporating intrinsic cues significantly improves accuracy and alignment. | numeric claim only at cited anchor | p. 7 (4.4. More 3D Vision Tasks) |

- Numeric sentences retained from the body:
- **p. 7 / 4.4. More 3D Vision Tasks - extractive PDF cue:** Sofa Car Pavilion StoneWall w/o. cue 1.67 0.87 1.03 1.43 w. cue 1.37 0.68 0.68 1.06 points, was reduced by around 20% on four in-the-wild ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Future work could address ultra-wide-angle images by incorporating more diverse training data and improve inference efficiency by developing a few-step diffusion [42] model to ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 4. The overview training framework of DM-Calib. The input image x and the camera image c are first encoded into latent space using ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Compared to Metric3D[85], our method provides more accurate distance estimates across different focal lengths and demonstrates robustness in both outdoor and indoor scenarios (see ... | p. 6 (4.4. More 3D Vision Tasks) |
| body limitation/failure cue | Notably, our method also performs well on the highly challenging Scenes11 dataset [10], which features randomly shaped, moving objects, further demonstrating its robustness in ... | p. 6 (4.2. Camera Intrinsic Evaluation) |
| body limitation/failure cue | While multi-resolution noise[32] improves performance slightly, it remains suboptimal. | p. 7 (4.5. Ablation Study) |
| body limitation/failure cue | Table 4. Ablation on Intrinsic Estimation. Multi-Res. Noise Camera Image Mean Error (◦)↓ Median Error (◦) ↓ ✗ | p. 7 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Ablation NYU-v2 KITTI δ1 ↑ SIlog ↓ A.Rel ↓ δ1 ↑ SIlog ↓ A.Rel ↓ Full Model 85.8 8.17 13.5 89.1 13.3 11.7 w.o ... | p. 7 (4.5. Ablation Study) |
| Additionally, prior methods that froze the VAE decoder during one-step training have shown to be inadequate for metric depth estimation, as demonstrated in our ... | p. 8 (4.5. Ablation Study) |
| 2) to encode camera intrinsics as a detail-preserving color image (see Sec. | p. 3 (3. Method) |
| For any given input image x, the corresponding latent code is generated by the VAE encoder: z = E(x). | p. 3 (3.1. Preliminaries on Diffusion Model) |
| This code is concatenated with zx, serving as the input for the pretrained U-Net. | p. 4 (3.3. Camera Intrinsic Estimation) |
| Multi-resolution noise [32] ϵc is then added to the camera latents zc, forming the noisy code zc T . | p. 4 (3.3. Camera Intrinsic Estimation) |
| Pre-trained Latent Encoder ℰ Add Noise by Timestamp 𝑡𝑡 | p. 5 (3.3. Camera Intrinsic Estimation) |
| Note that both U-Net U and the VAE decoder D are trained to allow predictions in any range. | p. 5 (3.4. Downstream 3D vision tasks) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** Future work could address ultra-wide-angle images by incorporating more diverse training data and improve inference efficiency by developing a few-step diffusion [42] model to further ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. The overview training framework of DM-Calib. The input image x and the camera image c are first encoded into latent space using a ...
- **p. 6 / 4.4. More 3D Vision Tasks - extractive PDF cue:** Compared to Metric3D[85], our method provides more accurate distance estimates across different focal lengths and demonstrates robustness in both outdoor and indoor scenarios (see Fig.
- **p. 6 / 4.2. Camera Intrinsic Evaluation - extractive PDF cue:** Notably, our method also performs well on the highly challenging Scenes11 dataset [10], which features randomly shaped, moving objects, further demonstrating its robustness in extreme ...
- **p. 7 / 4.5. Ablation Study - extractive PDF cue:** While multi-resolution noise[32] improves performance slightly, it remains suboptimal.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation on Intrinsic Estimation. Multi-Res. Noise Camera Image Mean Error (◦)↓ Median Error (◦) ↓ ✗

- **PDF anchors reviewed:** datasets p. 5 (4.1. Experimental Setup), p. 6 (4.2. Camera Intrinsic Evaluation), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Camera Intrinsic Evaluation), p. 7 (4.4. More 3D Vision Tasks), p. 7 (4.4. More 3D Vision Tasks), metrics p. 7 (4.5. Ablation Study), p. 7 (Figure/Table caption), p. 6 (4.4. More 3D Vision Tasks), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Camera Intrinsic Evaluation), p. 8 (4.5. Ablation Study), baselines p. 6 (4.3. Depth Evaluation), p. 6 (4.1. Experimental Setup), p. 7 (4.4. More 3D Vision Tasks), p. 2 (Figure/Table caption), p. 7 (4.5. Ablation Study), results p. 6 (4.3. Depth Evaluation), p. 7 (4.4. More 3D Vision Tasks), p. 6 (4.2. Camera Intrinsic Evaluation), p. 7 (4.5. Ablation Study), p. 8 (4.5. Ablation Study), p. 8 (4.5. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
