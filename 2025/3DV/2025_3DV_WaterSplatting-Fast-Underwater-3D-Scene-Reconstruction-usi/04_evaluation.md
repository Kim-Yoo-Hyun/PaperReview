# Evaluation - WaterSplatting: Fast Underwater 3D Scene Reconstruction using Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=Z9yn9YgNIz&name=pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.1. Results), p. 6 (4.1. Results), p. 7 (4.1. Results), p. 8 (Figure/Table caption), p. 5 (4. Experiments), p. 5 (4.1. Results)): Our rendering without medium and depth maps significantly outperform those from the SeaThru-NeRF, especially in scenes that are farther from the camera.

## Evaluation Body Digest

- **p. 5 / 4. Experiments - extractive body cue:** SeaThru-NeRF Dataset: SeaThru-NeRF Dataset released by [18] contains real-world scenes acquired from four different scenes in sea: IUI3 Red Sea, Curac¸ao, Japanese Gardens Red Sea, ...
- **p. 5 / 4.1. Results - extractive body cue:** First, we evaluated the performance of our method using the standard benchmark dataset, the SeaThru-NeRF Dataset.
- **p. 7 / 4.2. Ablation Study - extractive body cue:** These comparisons are made across validation sets for the SeaThru-NeRF dataset in Table 3.
- **p. 6 / 4.1. Results - extractive body cue:** Quantitative evaluation on the SeaThru-NeRF dataset.
- **p. 7 / 4.1. Results - extractive body cue:** We also achieve higher PSNR values in both scenes.
- **p. 6 / 4.1. Results - extractive body cue:** Underwater scene rendering in the 'Curasao' scene.
- **p. 5 / 4. Experiments - extractive body cue:** We present the alpha blending of depth as the depth map and the rendering without medium to demonstrate the ability to decouple the medium and ...
- **p. 7 / 4.1. Results - extractive body cue:** Our results exhibit better restoring quality and reasonable depth map compared to SeaThru-NeRF-NS' results. to produce a reasonable depth map at greater distances, as indicated ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Results (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our rendering without medium and depth maps significantly outperform those from the SeaThru-NeRF, especially in scenes that are farther from the camera. | p. 7 (4.1. Results) |
| 4.1. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method achieves better rendering quality and preserves finer distant geometric details while reducing the amount of floaters. | p. 6 (4.1. Results) |
| 4.1. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | We also achieve higher PSNR values in both scenes. | p. 7 (4.1. Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6. Ablation Study: loss function alignment. Our proposed LReg-DSSIM improves the reconstruction quality of distant details in dark areas, and the benefit is ... | p. 8 (Figure/Table caption) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | All reported results are averaged over three runs. | p. 5 (4. Experiments) |

## Dataset / Benchmark Role

- **p. 5 / 4. Experiments - extractive body cue:** SeaThru-NeRF Dataset: SeaThru-NeRF Dataset released by [18] contains real-world scenes acquired from four different scenes in sea: IUI3 Red Sea, Curac¸ao, Japanese Gardens Red Sea, ...
- **p. 5 / 4.1. Results - extractive body cue:** First, we evaluated the performance of our method using the standard benchmark dataset, the SeaThru-NeRF Dataset.
- **p. 7 / 4.2. Ablation Study - extractive body cue:** These comparisons are made across validation sets for the SeaThru-NeRF dataset in Table 3.
- **p. 6 / 4.1. Results - extractive body cue:** Quantitative evaluation on the SeaThru-NeRF dataset.
- **p. 7 / 4.1. Results - extractive body cue:** We also achieve higher PSNR values in both scenes.
- **p. 6 / 4.1. Results - extractive body cue:** Underwater scene rendering in the 'Curasao' scene.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Our approach surpasses the performance of state-of-the-art NeRF-based underwater reconstruction methods [18] while offering real-time rendering speed [15].
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Splatting with Medium: We start rendering by casting a ray per pixel and collect the patch-intersected Gaussians along the ray and their color ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Underwater scene rendering in the 'Curasao' scene. From left to right: white-balanced ground-truth image, our result, SeaThru- NeRF's result, 3DGS' result, and Zip-NeRF's ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Underwater scene rendering in the 'IUI3 Red Sea' scene, 'Japanese Gardens Red Sea' scene and 'Panama' scene. We compare our method with SeaThru-NeRF ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative evaluation on the SeaThru-NeRF dataset. We show PSNR↑, SSIM↑, LPIPS↓, Avg. FPS↑, and Avg. Training Time↓. The first , second , and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Simulated scene rendering with the easy foggy scene (upper) and hard foggy scene (lower). We compare our method with SeaThru-NeRF by showing both ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Restoration Performance. (PSNR↑/SSIM↑/LPIPS↓) Dataset/Metric Foggy-Easy Foggy-Hard
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Ablation Study: loss function alignment. Our proposed LReg-DSSIM improves the reconstruction quality of distant details in dark areas, and the benefit is obvious ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | SeaThru-NeRF Dataset: SeaThru-NeRF Dataset released by [18] contains real-world scenes acquired from four different scenes in sea: IUI3 Red Sea, Curac¸ao, Japanese Gardens Red ... | embodiment, simulator version and control stack | p. 5 (4. Experiments), p. 5 (4.1. Results) |
| Task/environment | First, we evaluated the performance of our method using the standard benchmark dataset, the SeaThru-NeRF Dataset. | reset, timeout, object/scene variation | p. 5 (4.1. Results), p. 7 (4.2. Ablation Study) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.2. Splatting with Medium), p. 3 (3.1. Preliminaries) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.2. Splatting with Medium), p. 4 (3.3. Loss Function Alignment) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We present the alpha blending of depth as the depth map and the rendering without medium to demonstrate the ability to decouple the medium ... | definition/direction/unit from same section | p. 5 (4. Experiments) |
| Our results exhibit better restoring quality and reasonable depth map compared to SeaThru-NeRF-NS' results. to produce a reasonable depth map at greater distances, as ... | definition/direction/unit from same section | p. 7 (4.1. Results) |
| Additionally, our depth map reveals much finer details compared to SeaThru-NeRF, which struggles | definition/direction/unit from same section | p. 5 (4.1. Results) |
| Furthermore, under each image, we show the depth maps (for GT the depth map from pre-trained model [42], and highlighted region from the image. | definition/direction/unit from same section | p. 6 (4.1. Results) |
| When used alone, LReg-L1 can also provide better details in far distance. | definition/direction/unit from same section | p. 7 (4.2. Ablation Study) |
| Figure 1. Our approach surpasses the performance of state-of-the-art NeRF-based underwater reconstruction methods [18] while offering real-time rendering speed [15]. | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 6. Ablation Study: loss function alignment. Our proposed LReg-DSSIM improves the reconstruction quality of distant details in dark areas, and the benefit is ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 7. Limitation: simulating distant medium with Gaus- sians. Our method (left) models distant medium with Gaussians. SeaThru-NeRF [18] (right) also struggles with the ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our rendering without medium and depth maps significantly outperform those from the SeaThru-NeRF, especially in scenes that are farther from the camera. | comparison identity and matched condition | p. 7 (4.1. Results) |
| Baseline methods: All methods were trianed on the same set of white-balanced images. | comparison identity and matched condition | p. 5 (4. Experiments) |
| Additionally, our depth map reveals much finer details compared to SeaThru-NeRF, which struggles | comparison identity and matched condition | p. 5 (4.1. Results) |
| Our results exhibit better restoring quality and reasonable depth map compared to SeaThru-NeRF-NS' results. to produce a reasonable depth map at greater distances, as ... | comparison identity and matched condition | p. 7 (4.1. Results) |
| Figure 1. Our approach surpasses the performance of state-of-the-art NeRF-based underwater reconstruction methods [18] while offering real-time rendering speed [15]. | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| For Restoration, we further show the rendered medium without rendering objects. | comparison identity and matched condition | p. 6 (4.1. Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conduct a quantitative analysis on different combination of loss functions, between pixel-wise component {L1, L2, LReg-L1, LReg-L2} and frame-wise {LDSSIM, LReg-DSSIM}, as well ... | component/input/data sensitivity | p. 7 (4.2. Ablation Study) |
| We present the alpha blending of depth as the depth map and the rendering without medium to demonstrate the ability to decouple the medium ... | component/input/data sensitivity | p. 5 (4. Experiments) |
| For Restoration, we further show the rendered medium without rendering objects. | component/input/data sensitivity | p. 6 (4.1. Results) |
| We compare our method with SeaThru-NeRF by showing both the full image and the rendering without the medium. | component/input/data sensitivity | p. 6 (4.1. Results) |
| Our rendering without medium and depth maps significantly outperform those from the SeaThru-NeRF, especially in scenes that are farther from the camera. | component/input/data sensitivity | p. 7 (4.1. Results) |
| Figure 8. Limitation: insufficient supervision. Our method (left) has low-detail visuals in regions not sufficiently covered by train- ing views. SeaThru-NeRF [18] (right) is ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Loss Function Alignment: We propose a novel loss function designed to align 3DGS with human perception of High Dynamic Range (HDR) and low-light scenes. | Our rendering without medium and depth maps significantly outperform those from the SeaThru-NeRF, especially in scenes that are farther from the camera. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.1. Results), p. 6 (4.1. Results), p. 7 (4.1. Results), p. 8 (Figure/Table caption), p. 5 (4. Experiments), p. 5 (4.1. Results) |
| Primary metric/result | Our method achieves better rendering quality and preserves finer distant geometric details while reducing the amount of floaters. | numeric claim only at cited anchor | p. 6 (4.1. Results) |

- Numeric sentences retained from the body:
- **p. 5 / 4. Experiments - extractive body cue:** We also calculate the FPS and total training time using the same RTX 4080 GPU to illustrate the speed difference between baselines and our method.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Although our method achieves good reconstruction quality, there are some limitations to consider. | p. 7 (5. Limitations) |
| body limitation/failure cue | However, in the foreground, our method prunes medium-role primitives well while SeaThru-NeRF cannot prevent the geometrical field from fitting the medium, resulting in wave-like ... | p. 7 (5. Limitations) |
| body limitation/failure cue | Limitation: insufficient supervision. | p. 8 (5. Limitations) |
| body limitation/failure cue | Limitation: simulating distant medium with Gaussians. | p. 8 (5. Limitations) |
| body limitation/failure cue | Both traditional 3DGS and NeRF with a proposal sampler cannot handle semitransparent medium well. | p. 6 (4.1. Results) |
| body limitation/failure cue | However, ZipNeRF training takes orders of magnitude more time than our method and does not offer real-time rendering. | p. 5 (4.1. Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We also calculate the FPS and total training time using the same RTX 4080 GPU to illustrate the speed difference between baselines and our ... | p. 5 (4. Experiments) |
| Implementation Details: Our implementation is based on the reimplemented version of 3DGS released by NeRFStudio [? ]. | p. 5 (4. Experiments) |
| We conduct a quantitative analysis on different combination of loss functions, between pixel-wise component {L1, L2, LReg-L1, LReg-L2} and frame-wise {LDSSIM, LReg-DSSIM}, as well ... | p. 7 (4.2. Ablation Study) |
| We initialize a set of 3D Gaussians via SfM [15] and optimize them with medium properties encoded by a neural network. | p. 3 (3.2. Splatting with Medium) |
| Pixel colors are computed by alpha blending of the sorted intersected Gaussians Gi whose αi are higher than a threshold: C = N X ... | p. 3 (3.1. Preliminaries) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5. Limitations - extractive body cue:** Although our method achieves good reconstruction quality, there are some limitations to consider.
- **p. 7 / 5. Limitations - extractive body cue:** However, in the foreground, our method prunes medium-role primitives well while SeaThru-NeRF cannot prevent the geometrical field from fitting the medium, resulting in wave-like artifacts.
- **p. 8 / 5. Limitations - extractive body cue:** Limitation: insufficient supervision.
- **p. 8 / 5. Limitations - extractive body cue:** Limitation: simulating distant medium with Gaussians.
- **p. 6 / 4.1. Results - extractive body cue:** Both traditional 3DGS and NeRF with a proposal sampler cannot handle semitransparent medium well.
- **p. 5 / 4.1. Results - extractive body cue:** However, ZipNeRF training takes orders of magnitude more time than our method and does not offer real-time rendering.

- **Evidence anchors reviewed:** datasets p. 5 (4. Experiments), p. 5 (4.1. Results), p. 7 (4.2. Ablation Study), p. 6 (4.1. Results), p. 7 (4.1. Results), p. 6 (4.1. Results), metrics p. 5 (4. Experiments), p. 7 (4.1. Results), p. 5 (4.1. Results), p. 6 (4.1. Results), p. 7 (4.2. Ablation Study), p. 1 (Figure/Table caption), baselines p. 7 (4.1. Results), p. 5 (4. Experiments), p. 5 (4.1. Results), p. 7 (4.1. Results), p. 1 (Figure/Table caption), p. 6 (4.1. Results), results p. 7 (4.1. Results), p. 6 (4.1. Results), p. 7 (4.1. Results), p. 8 (Figure/Table caption), p. 5 (4. Experiments), p. 5 (4.1. Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
