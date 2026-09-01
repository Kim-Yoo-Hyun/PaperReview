# Evaluation - SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 7 (4.1. Image rendering), p. 8 (4.3. Ablations), p. 8 (4.2. Lidar rendering), p. 6 (3.4. Optimization and implementation), p. 1 (Figure/Table caption)): Figure 4. Removing our rolling shutter modeling compensation leads to inaccurate geometries and inconsistencies in the learning. We measure speed using resolution-agnostic megapixels per second. SplatAD consistently outperforms existing ...

## Evaluation Body Digest

- **p. 6 / 4. Experiments - extractive PDF cue:** Datasets: We perform experiments on PandaSet [41], Argoverse2 [38] and nuScenes [5].
- **p. 7 / 4. Experiments - extractive PDF cue:** Depth ↓ Intensity ↓ Drop acc. ↑ CD ↓ MR/s ↑ PandaSet UniSim 0.08 0.086 - 10.3§ 0.9 NeuRAD 0.01 0.063 96.2 1.9 1.1 PVG ...
- **p. 6 / 4. Experiments - extractive PDF cue:** NVS results for image, over three datasets.
- **p. 7 / 4. Experiments - extractive PDF cue:** Note that all methods are designed for dynamic scenes and use lidar data for supervision.
- **p. 8 / 4.3. Ablations - extractive PDF cue:** Metrics are averaged over all three datasets to avoid any dataset-specific biases.
- **p. 8 / 4.2. Lidar rendering - extractive PDF cue:** NVS results averaged over 10 sequences from PandaSet, nuScenes, and Argoverse2 when removing model components.
- **p. 7 / 4.2. Lidar rendering - extractive PDF cue:** We measure the quality of our lidar point clouds using the same metrics as in [35], i.e., median squared depth error, RMSE intensity error, ray ...
- **p. 8 / 4.2. Lidar rendering - extractive PDF cue:** FDDINOv2 scores when shifting pose of ego vehicle or actors.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3.4. Optimization and implementation (p. 5); 4. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 4. Removing our rolling shutter modeling compensation leads to inaccurate geometries and inconsistencies in the learning. We measure speed using resolution-agnostic megapixels per ... | p. 7 (Figure/Table caption) |
| 4.1. Image rendering | SYSTEM / EVALUATION SCOPE UNRESOLVED | SplatAD achieves SOTA results while rendering ×10 faster than the previous best method. | p. 7 (4.1. Image rendering) |
| 4.3. Ablations | SYSTEM / EVALUATION SCOPE UNRESOLVED | Last, we note that MCMC [16] and EWA antialiasing [47, 52] both improve our performance, with the antialiasing having the largest impact on perceptual ... | p. 8 (4.3. Ablations) |
| 4.2. Lidar rendering | SYSTEM / EVALUATION SCOPE UNRESOLVED | The CNN decoder improves sharpness and is more true to color than the MLP decoder. that we do not report intensity or ray drop ... | p. 8 (4.2. Lidar rendering) |
| 3.4. Optimization and implementation | SYSTEM / EVALUATION SCOPE UNRESOLVED | We chose MCMC partially because we find it to improve far-field rendering quality and partially because it has predictable computation requirements, as it permits ... | p. 6 (3.4. Optimization and implementation) |

## Dataset / Benchmark Role

- **p. 6 / 4. Experiments - extractive PDF cue:** Datasets: We perform experiments on PandaSet [41], Argoverse2 [38] and nuScenes [5].
- **p. 7 / 4. Experiments - extractive PDF cue:** Depth ↓ Intensity ↓ Drop acc. ↑ CD ↓ MR/s ↑ PandaSet UniSim 0.08 0.086 - 10.3§ 0.9 NeuRAD 0.01 0.063 96.2 1.9 1.1 PVG ...
- **p. 6 / 4. Experiments - extractive PDF cue:** NVS results for image, over three datasets.
- **p. 7 / 4. Experiments - extractive PDF cue:** Note that all methods are designed for dynamic scenes and use lidar data for supervision.
- **p. 8 / 4.3. Ablations - extractive PDF cue:** Metrics are averaged over all three datasets to avoid any dataset-specific biases.
- **p. 8 / 4.2. Lidar rendering - extractive PDF cue:** NVS results averaged over 10 sequences from PandaSet, nuScenes, and Argoverse2 when removing model components.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. SplatAD is the first method capable of realistic camera and lidar rendering using 3D Gaussian Splatting. Whereas previous methods are either fast or ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of our proposed method. Given the composition of static and dynamic 3D Gaussians, SplatAD is capable of differentiable rendering of both lidar ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3. Compared to the baselines, SplatAD produces sharp images with a high level of detail. Further, the bottom row highlights the superiority of our ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. NVS results for image, over three datasets. First , second , third . PSNR ↑ SSIM ↑ LPIPS ↓ MP/s ↑
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. NVS results for lidar, over three datasets. §without missing points. First , second , third . Depth ↓ Intensity ↓ Drop acc. ↑ ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Removing our rolling shutter modeling compensation leads to inaccurate geometries and inconsistencies in the learning. We measure speed using resolution-agnostic megapixels per second. ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Reconstruction results for image and lidar point clouds on PandaSet. §without missing points. First , second , third . Image Lidar Efficiency PSNR ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. FDDINOv2 scores when shifting pose of ego vehicle or actors. First , second , third . Ego lane shift Ego vert. shift Actor ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Datasets: We perform experiments on PandaSet [41], Argoverse2 [38] and nuScenes [5]. | embodiment, simulator version and control stack | p. 6 (4. Experiments), p. 7 (4. Experiments) |
| Task/environment | Depth ↓ Intensity ↓ Drop acc. ↑ CD ↓ MR/s ↑ PandaSet UniSim 0.08 0.086 - 10.3§ 0.9 NeuRAD 0.01 0.063 96.2 1.9 1.1 ... | reset, timeout, object/scene variation | p. 7 (4. Experiments), p. 6 (4. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 3 (3. Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (3.4. Optimization and implementation), p. 4 (3.3. Lidar rendering) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We measure the quality of our lidar point clouds using the same metrics as in [35], i.e., median squared depth error, RMSE intensity error, ... | definition/direction/unit from same section | p. 7 (4.2. Lidar rendering) |
| FDDINOv2 scores when shifting pose of ego vehicle or actors. | definition/direction/unit from same section | p. 8 (4.2. Lidar rendering) |
| Removing these components leads to line-of-sight errors, which erroneously can cut through objects. | definition/direction/unit from same section | p. 8 (4.3. Ablations) |
| Projecting lidar points into images for depth supervision, as used by previous 3DGS methods, causes line-of-sight errors and incorrect volume carving due to the ... | definition/direction/unit from same section | p. 6 (3.4. Optimization and implementation) |
| Figure 1. SplatAD is the first method capable of realistic camera and lidar rendering using 3D Gaussian Splatting. Whereas previous methods are either fast ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| To validate the robustness of our method, we evaluate it across multiple popular AD datasets, using the same set of hyperparameters. | definition/direction/unit from same section | p. 6 (4. Experiments) |
| Further, we note that SplatAD's performance on hold-out validation images in Tab. | definition/direction/unit from same section | p. 7 (4.1. Image rendering) |
| LBCE is a binary cross-entropy loss on the predicted ray drop probability, where ground-truth is generated in the same way as for NeuRAD. | definition/direction/unit from same section | p. 5 (3.4. Optimization and implementation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to the baselines, SplatAD produces sharp images with a high level of detail. | comparison identity and matched condition | p. 6 (3.4. Optimization and implementation) |
| See Appendix C for further baseline details. | comparison identity and matched condition | p. 7 (4. Experiments) |
| 4 shows SplatAD's ability to learn meaningful representations for generalization, clearly outperforming other 3DGS methods. | comparison identity and matched condition | p. 7 (4.1. Image rendering) |
| Furthermore, our lidar rendering approach is superior to the naive depth image-based method used for 3DGS baselines, both in terms of speed and quality. | comparison identity and matched condition | p. 8 (4.2. Lidar rendering) |
| The CNN decoder improves sharpness and is more true to color than the MLP decoder. that we do not report intensity or ray drop ... | comparison identity and matched condition | p. 8 (4.2. Lidar rendering) |
| We use [16] as is, without any special treatment of Gaussians assigned to dynamic actors. | comparison identity and matched condition | p. 6 (3.4. Optimization and implementation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Further, some cameras are cropped slightly to remove views of the ego-vehicle, such as the hood and the trunk. | component/input/data sensitivity | p. 6 (4. Experiments) |
| NVS results for lidar, over three datasets. §without missing points. | component/input/data sensitivity | p. 7 (4. Experiments) |
| Reconstruction results for image and lidar point clouds on PandaSet. §without missing points. | component/input/data sensitivity | p. 8 (4.2. Lidar rendering) |
| We validate the effectiveness of key components of our method by measuring their impact on NVS metrics in Tab. | component/input/data sensitivity | p. 8 (4.3. Ablations) |
| Figure 2. Overview of our proposed method. Given the composition of static and dynamic 3D Gaussians, SplatAD is capable of differentiable rendering of both ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| We use [16] as is, without any special treatment of Gaussians assigned to dynamic actors. | component/input/data sensitivity | p. 6 (3.4. Optimization and implementation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, our contributions are as follows: • We propose the first method for efficient lidar rendering using 3D Gaussians, introducing custom CUDA-accelerated algorithms ... | Figure 4. Removing our rolling shutter modeling compensation leads to inaccurate geometries and inconsistencies in the learning. We measure speed using resolution-agnostic megapixels per ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 7 (4.1. Image rendering), p. 8 (4.3. Ablations), p. 8 (4.2. Lidar rendering), p. 6 (3.4. Optimization and implementation), p. 1 (Figure/Table caption) |
| Primary metric/result | SplatAD achieves SOTA results while rendering ×10 faster than the previous best method. | numeric claim only at cited anchor | p. 7 (4.1. Image rendering) |

- Numeric sentences retained from the body:
- **p. 4 / 3.3. Lidar rendering - extractive PDF cue:** Most AD datasets deploy lidars that use several laser diodes (16-128) mounted in a vertical array, where the array of diodes is rotated to capture ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations and future work: SplatAD is currently limited to modeling all dynamic actors as rigid. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Drawing inspiration from recent advances in human reconstruction [18, 20, 26] can provide inspiration how to overcome this limitation in future research. | p. 8 (5. Conclusion) |
| body limitation/failure cue | However, we note that using Inception-v3 features instead does not change the model ranking or our conclusions. | p. 7 (4.1. Image rendering) |
| body limitation/failure cue | To validate the robustness of our method, we evaluate it across multiple popular AD datasets, using the same set of hyperparameters. | p. 6 (4. Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| To validate the robustness of our method, we evaluate it across multiple popular AD datasets, using the same set of hyperparameters. | p. 6 (4. Experiments) |
| Implementation: For efficiency, we implement the forward and backward passes of the rolling shutter compensation and lidar projection and rasterization using custom CUDA kernels. | p. 6 (3.4. Optimization and implementation) |
| We use NeuRAD's official implementation neurad-studio [34] and their version of UniSim, as well as OmniRe's official implementation drivestudio [8] and their implementations of ... | p. 7 (4. Experiments) |
| We also find that using a CNN instead of an MLP for image decoding (c) clearly improves image realism, but at the cost of ... | p. 8 (4.3. Ablations) |
| The CNN decoder improves sharpness and is more true to color than the MLP decoder. that we do not report intensity or ray drop ... | p. 8 (4.2. Lidar rendering) |
| 3.2 and 3.3), and implementation and optimization strategy (Sec. | p. 3 (3. Method) |
| Finally, the rasterized features are decoded into the respective image and lidar point cloud representations. data, with the ability to alter the locations of ... | p. 3 (3. Method) |
| (3) To rasterize a pixel, we α-blend RGB values f rgb i and features fi of the depth-sorted Gaussians intersecting the current tile \la ... | p. 4 (3.2. Camera rendering) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** Limitations and future work: SplatAD is currently limited to modeling all dynamic actors as rigid.
- **p. 8 / 5. Conclusion - extractive PDF cue:** Drawing inspiration from recent advances in human reconstruction [18, 20, 26] can provide inspiration how to overcome this limitation in future research.
- **p. 7 / 4.1. Image rendering - extractive PDF cue:** However, we note that using Inception-v3 features instead does not change the model ranking or our conclusions.
- **p. 6 / 4. Experiments - extractive PDF cue:** To validate the robustness of our method, we evaluate it across multiple popular AD datasets, using the same set of hyperparameters.

- **PDF anchors reviewed:** datasets p. 6 (4. Experiments), p. 7 (4. Experiments), p. 6 (4. Experiments), p. 7 (4. Experiments), p. 8 (4.3. Ablations), p. 8 (4.2. Lidar rendering), metrics p. 7 (4.2. Lidar rendering), p. 8 (4.2. Lidar rendering), p. 8 (4.3. Ablations), p. 6 (3.4. Optimization and implementation), p. 1 (Figure/Table caption), p. 6 (4. Experiments), baselines p. 6 (3.4. Optimization and implementation), p. 7 (4. Experiments), p. 7 (4.1. Image rendering), p. 8 (4.2. Lidar rendering), p. 8 (4.2. Lidar rendering), p. 6 (3.4. Optimization and implementation), results p. 7 (Figure/Table caption), p. 7 (4.1. Image rendering), p. 8 (4.3. Ablations), p. 8 (4.2. Lidar rendering), p. 6 (3.4. Optimization and implementation), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
