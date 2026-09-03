# Evaluation - SparseGS: Sparse View Synthesis using 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=O9GMl5UJbe&name=pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. Comparison), p. 3 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (4.3. Ablation Studies)): 1, SparseGS significantly outperforms previous NeRF-based methods and concurrent works, FSGS and DNGaussian, in both 12-view and 24-view settings.

## Evaluation Body Digest

- **p. 7 / 4.2. Comparison - extractive body cue:** The LLFF dataset comprises eight complex forward-facing real scenes, while the DTU dataset includes object-centric scenes with foreground masks.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** We conduct our experiments on three datasets, categorized into two settings: 1) the Mip-NeRF360 [2] dataset, which features seven challenging 360° scenes; 2) the LLFF ...
- **p. 7 / 4.2. Comparison - extractive body cue:** We use the Mip-NeRF360 dataset to evaluate 3D reconstruction of unbounded 360° scenes.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** For the Mip-NeRF360 dataset, we Figure 5.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** Qualitative evaluation on the Mip-NeRF 360 dataset.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** Qualitative evaluation on the forward-facing datasets.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Our proposed pipeline incorporates depth priors, diffusion constraints, and a floater pruning technique to improve few- shot novel view synthesis performance. During training, ...
- **p. 7 / 4.2. Comparison - extractive body cue:** We also provide evaluations on the forward-facing datasets (LLFF and DTU) to demonstrate robustness of our pipeline.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Settings (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Comparison | SYSTEM / EVALUATION SCOPE UNRESOLVED | 1, SparseGS significantly outperforms previous NeRF-based methods and concurrent works, FSGS and DNGaussian, in both 12-view and 24-view settings. | p. 7 (4.2. Comparison) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 2. Our proposed pipeline incorporates depth priors, diffusion constraints, and a floater pruning technique to improve few- shot novel view synthesis performance. During ... | p. 3 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 1. The quality of 3DGS [12] degrades as the number of input views decreases, particularly in unbounded scenes. SparseGS significantly improves novel view ... | p. 1 (Figure/Table caption) |
| 4.3. Ablation Studies | SYSTEM / EVALUATION SCOPE UNRESOLVED | We show the improvements by applying this loss to both alpha-blending and softmax-scaling depth. | p. 7 (4.3. Ablation Studies) |

## Dataset / Benchmark Role

- **p. 7 / 4.2. Comparison - extractive body cue:** The LLFF dataset comprises eight complex forward-facing real scenes, while the DTU dataset includes object-centric scenes with foreground masks.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** We conduct our experiments on three datasets, categorized into two settings: 1) the Mip-NeRF360 [2] dataset, which features seven challenging 360° scenes; 2) the LLFF ...
- **p. 7 / 4.2. Comparison - extractive body cue:** We use the Mip-NeRF360 dataset to evaluate 3D reconstruction of unbounded 360° scenes.
- **p. 6 / 4.1. Experimental Settings - extractive body cue:** For the Mip-NeRF360 dataset, we Figure 5.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** Qualitative evaluation on the Mip-NeRF 360 dataset.
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** Qualitative evaluation on the forward-facing datasets.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The quality of 3DGS [12] degrades as the number of input views decreases, particularly in unbounded scenes. SparseGS significantly improves novel view synthesis ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Our proposed pipeline incorporates depth priors, diffusion constraints, and a floater pruning technique to improve few- shot novel view synthesis performance. During training, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. A Demonstration of the Three Kinds of Depth. The weights wi are shown at the top, with the weights after apply- ing softmax ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Illustration of benefits from the SDS loss. While the scene structure is well preserved, the high-frequency noise in both geometry and texture is ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. The proposed floater pruning technique removes Gaussians at inaccurate depths. An example (a) demonstrates our pruning method: before pruning, there are floaters (blue) ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparison on Mip-NeRF360 dataset for 12/24 input-view settings. ing COLMAP [32, 33]. Specifically, the initial point cloud is output from the multi-view ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Quantitative comparison on forward-facing datasets. Depth PCC PSNR ↑ LPIPS ↓ SSIM ↑ Alpha-blending Softmax-scaling UVR
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Ablation Studies. We ablate our components on the Mip-NeRF360 dataset under 12-view setting. regions, where input coverage is insufficient, NeRF-based methods often produce ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The LLFF dataset comprises eight complex forward-facing real scenes, while the DTU dataset includes object-centric scenes with foreground masks. | embodiment, simulator version and control stack | p. 7 (4.2. Comparison), p. 6 (4.1. Experimental Settings) |
| Task/environment | We conduct our experiments on three datasets, categorized into two settings: 1) the Mip-NeRF360 [2] dataset, which features seven challenging 360° scenes; 2) the ... | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Settings), p. 7 (4.2. Comparison) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 6 (3.3. Unseen Viewpoints Regularization (UVR)) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 2. Our proposed pipeline incorporates depth priors, diffusion constraints, and a floater pruning technique to improve few- shot novel view synthesis performance. During ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| We also provide evaluations on the forward-facing datasets (LLFF and DTU) to demonstrate robustness of our pipeline. | definition/direction/unit from same section | p. 7 (4.2. Comparison) |
| In order to prove robustness of our method, we also evaluate performance with even sparser point clouds output by Structure From Motion (i.e., without ... | definition/direction/unit from same section | p. 7 (4.2. Comparison) |
| The proposed floater pruning technique removes Gaussians at inaccurate depths. | definition/direction/unit from same section | p. 6 (4.1. Experimental Settings) |
| An example (a) demonstrates our pruning method: before pruning, there are floaters (blue) in front of the Gaussians at the object surface (red) and ... | definition/direction/unit from same section | p. 6 (4.1. Experimental Settings) |
| The reference depth map is produced by a monocular depth estimation model. | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |
| Our method is able to reconstruct high-frequency geometry more accurately than state-of-the-art [49]. | definition/direction/unit from same section | p. 8 (4.3. Ablation Studies) |
| Figure 4. Illustration of benefits from the SDS loss. While the scene structure is well preserved, the high-frequency noise in both geometry and texture ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 1, SparseGS significantly outperforms previous NeRF-based methods and concurrent works, FSGS and DNGaussian, in both 12-view and 24-view settings. | comparison identity and matched condition | p. 7 (4.2. Comparison) |
| 3, our softmax-scaling depth rendering method performs better, improving PSNR by 1.37dB compared to 3DGS and significantly enhance the quality of the rendered depth ... | comparison identity and matched condition | p. 7 (4.3. Ablation Studies) |
| Our method is able to reconstruct high-frequency geometry more accurately than state-of-the-art [49]. | comparison identity and matched condition | p. 8 (4.3. Ablation Studies) |
| Figure 7. Ablation studies. The reference depth map is produced by a monocular depth estimation model. Our complete model outputs a cleaner and more ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The proposed floater pruning technique removes Gaussians at inaccurate depths. | component/input/data sensitivity | p. 6 (4.1. Experimental Settings) |
| The pruning method removes all Gaussians on that pixel before the mode and as a result, dmode = dalpha. | component/input/data sensitivity | p. 6 (4.1. Experimental Settings) |
| In order to prove robustness of our method, we also evaluate performance with even sparser point clouds output by Structure From Motion (i.e., without ... | component/input/data sensitivity | p. 7 (4.2. Comparison) |
| Table 3. Ablation Studies. We ablate our components on the Mip-NeRF360 dataset under 12-view setting. regions, where input coverage is insufficient, NeRF-based methods often ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Figure 7. Ablation studies. The reference depth map is produced by a monocular depth estimation model. Our complete model outputs a cleaner and more ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method consists of three key components designed to function cohesively to improve view consistency and depth accuracy in novel view synthesis: a depth ... | 1, SparseGS significantly outperforms previous NeRF-based methods and concurrent works, FSGS and DNGaussian, in both 12-view and 24-view settings. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. Comparison), p. 3 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (4.3. Ablation Studies) |
| Primary metric/result | Figure 2. Our proposed pipeline incorporates depth priors, diffusion constraints, and a floater pruning technique to improve few- shot novel view synthesis performance. During ... | numeric claim only at cited anchor | p. 3 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This limitation actually prompted the introduction of positional encoding [20, 37]. | p. 7 (4.2. Comparison) |
| body limitation/failure cue | In contrast, FSGS excels in preserving fine details due to its densification technique but fails to reconstruct background geometry. | p. 8 (4.3. Ablation Studies) |
| body limitation/failure cue | In regions with little coverage by input views, we leverage Score Distillation Sampling (SDS) and Depth Warping to reduce collapse in geometry and noise ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 1. The quality of 3DGS [12] degrades as the number of input views decreases, particularly in unbounded scenes. SparseGS significantly improves novel view ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Figure 4. Illustration of benefits from the SDS loss. While the scene structure is well preserved, the high-frequency noise in both geometry and texture ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | We also provide evaluations on the forward-facing datasets (LLFF and DTU) to demonstrate robustness of our pipeline. | p. 7 (4.2. Comparison) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In quantitative evaluation from now on, we compute peak signal-to-noise ratio (PSNR), Learned Perceptual Image Patch Similarity (LPIPS) and structural similarity index measure (SSIM) ... | p. 7 (4.2. Comparison) |
| We compute pseudo-ground truth depth maps using pretrained depth estimation models on the training views. | p. 4 (3.2. Patch-based Depth Correlation Loss) |
| Instead, we adopt Pearson correlation across image patches to compute a similarity metric between depth maps. | p. 4 (3.2. Patch-based Depth Correlation Loss) |
| At each iteration, we randomly sample N non-overlapping patches to compute the depth correlation loss as: Ldepth = 1 N N X i 1 ... | p. 5 (3.2. Patch-based Depth Correlation Loss) |
| Then, the renderings at the sampled viewpoints are encoded and decoded by the diffusion model, where the predicted noise is then supervised with our ... | p. 5 (3.3. Unseen Viewpoints Regularization (UVR)) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.2. Comparison - extractive body cue:** This limitation actually prompted the introduction of positional encoding [20, 37].
- **p. 8 / 4.3. Ablation Studies - extractive body cue:** In contrast, FSGS excels in preserving fine details due to its densification technique but fails to reconstruct background geometry.
- **p. 8 / 5. Conclusion - extractive body cue:** In regions with little coverage by input views, we leverage Score Distillation Sampling (SDS) and Depth Warping to reduce collapse in geometry and noise in ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The quality of 3DGS [12] degrades as the number of input views decreases, particularly in unbounded scenes. SparseGS significantly improves novel view synthesis ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Illustration of benefits from the SDS loss. While the scene structure is well preserved, the high-frequency noise in both geometry and texture is ...
- **p. 7 / 4.2. Comparison - extractive body cue:** We also provide evaluations on the forward-facing datasets (LLFF and DTU) to demonstrate robustness of our pipeline.

- **Evidence anchors reviewed:** datasets p. 7 (4.2. Comparison), p. 6 (4.1. Experimental Settings), p. 7 (4.2. Comparison), p. 6 (4.1. Experimental Settings), p. 8 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), metrics p. 3 (Figure/Table caption), p. 7 (4.2. Comparison), p. 7 (4.2. Comparison), p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), p. 8 (4.3. Ablation Studies), baselines p. 7 (4.2. Comparison), p. 7 (4.3. Ablation Studies), p. 8 (4.3. Ablation Studies), p. 8 (Figure/Table caption), results p. 7 (4.2. Comparison), p. 3 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (4.3. Ablation Studies).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
