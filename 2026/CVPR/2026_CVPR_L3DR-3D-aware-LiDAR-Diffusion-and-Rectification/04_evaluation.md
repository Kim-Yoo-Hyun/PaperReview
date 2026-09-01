# Evaluation - L3DR: 3D-aware LiDAR Diffusion and Rectification

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_L3DR_3D-aware_LiDAR_Diffusion_and_Rectification_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_L3DR_3D-aware_LiDAR_Diffusion_and_Rectification_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.2. Experiment Setup), p. 7 (5.2. Experiment Setup), p. 8 (5.3. Other Results), p. 8 (5.3. Other Results), p. 4 (3.2. Theoretical Analysis), p. 4 (3.3. Empirical Analysis)): We conclude that L3DR significantly improves conditional generation capability compared to the baselines.

## Evaluation Body Digest

- **p. 6 / 5.2. Experiment Setup - extractive PDF cue:** All datasets are split into trainvalidation-test according to official recommendations.
- **p. 6 / 5.2. Experiment Setup - extractive PDF cue:** We train and evaluate our method on SemanticKITTI [1, 10], KITTI360 [20], nuScenes [4], and Waymo Open Dataset [40].
- **p. 7 / 5.2. Experiment Setup - extractive PDF cue:** L3DR exhibits consistent improvements on all datasets, improving all metrics by an average of 11.6% and 7.0% on nuScenes and Waymo conditional generation, respectively.
- **p. 7 / 5.2. Experiment Setup - extractive PDF cue:** We conclude that L3DR is widely applicable and sets new state-of-the-arts on the nuScenes and Waymo semanticconditioned generation tasks.
- **p. 3 / 3.2. Theoretical Analysis - extractive PDF cue:** Therefore, DDIM outputs are smooth, with softly transitioned object boundaries.
- **p. 4 / 3.3. Empirical Analysis - extractive PDF cue:** We conclude that 3D models generate sharper object borders than 2D models, thus being preferable for rectification of 2D image diffusion results.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Visualization of two types of errors in RRN training data. While the generated point clouds (colored) approximate the GT (gray) in most of ...
- **p. 7 / 5.3. Other Results - extractive PDF cue:** The best overall performance attributes to SPUNET with Welsch loss and semantic-map input.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.1. Main Results (p. 6); 5.2. Experiment Setup (p. 6); 5.3. Other Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Experiment Setup | EMPIRICAL / SOURCE-REPORTED EVALUATION | We conclude that L3DR significantly improves conditional generation capability compared to the baselines. | p. 7 (5.2. Experiment Setup) |
| 5.2. Experiment Setup | EMPIRICAL / SOURCE-REPORTED EVALUATION | Meanwhile, L3DR with semantic-map input improves generation quality consistently, providing further 10.2% average performance boost on all metrics upon raw L3DR. | p. 7 (5.2. Experiment Setup) |
| 5.3. Other Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Red regions highlight the the improvements from the diffusiongenerated (i.e., denoised) data to our rectified data. | p. 8 (5.3. Other Results) |
| 5.3. Other Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | We conclude that the L3DR framework can greatly improve generation quality with negligible additional parameter and inference cost. | p. 8 (5.3. Other Results) |
| 3.2. Theoretical Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | In the residual regression training stage, such data pairs are employed to train a 3D network to remove RV artifacts present in the residuals ... | p. 4 (3.2. Theoretical Analysis) |

## Dataset / Benchmark Role

- **p. 6 / 5.2. Experiment Setup - extractive PDF cue:** All datasets are split into trainvalidation-test according to official recommendations.
- **p. 6 / 5.2. Experiment Setup - extractive PDF cue:** We train and evaluate our method on SemanticKITTI [1, 10], KITTI360 [20], nuScenes [4], and Waymo Open Dataset [40].
- **p. 7 / 5.2. Experiment Setup - extractive PDF cue:** L3DR exhibits consistent improvements on all datasets, improving all metrics by an average of 11.6% and 7.0% on nuScenes and Waymo conditional generation, respectively.
- **p. 7 / 5.2. Experiment Setup - extractive PDF cue:** We conclude that L3DR is widely applicable and sets new state-of-the-arts on the nuScenes and Waymo semanticconditioned generation tasks.
- **p. 3 / 3.2. Theoretical Analysis - extractive PDF cue:** Therefore, DDIM outputs are smooth, with softly transitioned object boundaries.
- **p. 4 / 3.3. Empirical Analysis - extractive PDF cue:** We conclude that 3D models generate sharper object borders than 2D models, thus being preferable for rectification of 2D image diffusion results.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. L3DR effectively rectifies LiDAR range-view (RV) diffusion artifacts by selectively ignoring anomalous training regions. (a) Depth bleeding creates fake points between the foreground ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Empirical validation of Theorem 1. The graph shows the distribution of ∥∇x∥for GT, vanilla RV diffusion, and our rectified RV, including the corresponding ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. The training pipeline of the proposed L3DR framework. In the LiDAR diffusion training stage, generated and ground-truth point cloud pairs are collected using ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Visualization of two types of errors in RRN training data. While the generated point clouds (colored) approximate the GT (gray) in most of ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. The inference pipeline of the proposed L3DR. truths, and yet remain imbued with RV artifacts on a limited scale, as depicted in Figure ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Benchmarking of unconditional generation on KITTI360 and semantic-conditioned generation on nuScenes and Waymo. For the semantic-conditioned experiments, RRN takes segmentation map as additional ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison of conditional LiDAR point cloud generation on SemanticKITTI and KITTI360. Gray areas highlight direct comparisons with the baseline, LiDM. ‘Ours-Sem' denotes our ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. Visualization of conditional generation on SemanticKITTI. Cyan regions highlight the improved RV artifacts from the diffusion-generated (i.e., denoised) data to our rectified data, ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | All datasets are split into trainvalidation-test according to official recommendations. | embodiment, simulator version and control stack | p. 6 (5.2. Experiment Setup), p. 6 (5.2. Experiment Setup) |
| Task/environment | We train and evaluate our method on SemanticKITTI [1, 10], KITTI360 [20], nuScenes [4], and Waymo Open Dataset [40]. | reset, timeout, object/scene variation | p. 6 (5.2. Experiment Setup), p. 7 (5.2. Experiment Setup) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (4.2. LiDAR Diffusion Training), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (4.3. Residual Regression Training), p. 4 (4.2. LiDAR Diffusion Training) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 4. Visualization of two types of errors in RRN training data. While the generated point clouds (colored) approximate the GT (gray) in most ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| The best overall performance attributes to SPUNET with Welsch loss and semantic-map input. | definition/direction/unit from same section | p. 7 (5.3. Other Results) |
| As listed in Table 3, applying MSE Loss generally deteriorates performance compared to baseline, with FSVD and FPVD almost doubling from 18.3, 15.3 to ... | definition/direction/unit from same section | p. 7 (5.3. Other Results) |
| Ablation experiment on SemanticKITTI, including RRN backbone structure, loss function, semantic-map input to RRN, and a fair baseline using a 2D image Unet instead ... | definition/direction/unit from same section | p. 8 (5.3. Other Results) |
| Table 1. Benchmarking of unconditional generation on KITTI360 and semantic-conditioned generation on nuScenes and Waymo. For the semantic-conditioned experiments, RRN takes segmentation map as ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 1. L3DR effectively rectifies LiDAR range-view (RV) diffusion artifacts by selectively ignoring anomalous training regions. (a) Depth bleeding creates fake points between the ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| We generate RRN training data by conditional LiDM inference on training set conditions, i.e., segmentation maps, and report the metrics of the last-epoch model ... | definition/direction/unit from same section | p. 6 (5.2. Experiment Setup) |
| Configurations Perceptual Statistical Backbone Loss RRN Sem. | definition/direction/unit from same section | p. 8 (5.3. Other Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We conclude that L3DR significantly improves conditional generation capability compared to the baselines. | comparison identity and matched condition | p. 7 (5.2. Experiment Setup) |
| As listed in Table 3, applying MSE Loss generally deteriorates performance compared to baseline, with FSVD and FPVD almost doubling from 18.3, 15.3 to ... | comparison identity and matched condition | p. 7 (5.3. Other Results) |
| Table 4. Computational overhead on KITTI360. our method introduce very slight computational overhead over the baselines. Time analysis. We provide a simple time comparison ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Ablation experiment on SemanticKITTI, including RRN backbone structure, loss function, semantic-map input to RRN, and a fair baseline using a 2D image Unet instead ... | comparison identity and matched condition | p. 8 (5.3. Other Results) |
| Table 1. Benchmarking of unconditional generation on KITTI360 and semantic-conditioned generation on nuScenes and Waymo. For the semantic-conditioned experiments, RRN takes segmentation map as ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| According to the figure, range view generated images have lower ∥∇x∥compared to the ground truth due to the inherent smoothness of diffusion-generated images. | comparison identity and matched condition | p. 4 (3.3. Empirical Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We remove the dominant ∥∇x∥≤0.3m on planar regions and rare ∥∇x∥≥10m which exceed network ERFs, so that we can compare the remaining geometryrelated gradients. | component/input/data sensitivity | p. 4 (3.3. Empirical Analysis) |
| In the residual regression training stage, such data pairs are employed to train a 3D network to remove RV artifacts present in the residuals ... | component/input/data sensitivity | p. 4 (3.2. Theoretical Analysis) |
| Module ablation and time analysis are listed in Table 3-4. | component/input/data sensitivity | p. 6 (5.1. Main Results) |
| Our diffusion model processes depth values of size without logarithmic scaling. | component/input/data sensitivity | p. 6 (5.2. Experiment Setup) |
| Ablation experiment on SemanticKITTI, including RRN backbone structure, loss function, semantic-map input to RRN, and a fair baseline using a 2D image Unet instead ... | component/input/data sensitivity | p. 8 (5.3. Other Results) |
| We ablate various components of the L3DR framework, including the backbone architecture between SPUNET [7] and PTV3 [46], loss choice, the usage of semantic-map ... | component/input/data sensitivity | p. 7 (5.3. Other Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The contributions of this work can be summarized in three major aspects: • We propose a 3D-aware LiDAR Diffusion and Rectification framework that rectifies ... | We conclude that L3DR significantly improves conditional generation capability compared to the baselines. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.2. Experiment Setup), p. 7 (5.2. Experiment Setup), p. 8 (5.3. Other Results), p. 8 (5.3. Other Results), p. 4 (3.2. Theoretical Analysis), p. 4 (3.3. Empirical Analysis) |
| Primary metric/result | Meanwhile, L3DR with semantic-map input improves generation quality consistently, providing further 10.2% average performance boost on all metrics upon raw L3DR. | numeric claim only at cited anchor | p. 7 (5.2. Experiment Setup) |

- Numeric sentences retained from the body:
- **p. 6 / 5.2. Experiment Setup - extractive PDF cue:** All networks are trained with 4× RTX 4090 24G up to 150 epochs.
- **p. 7 / 5.2. Experiment Setup - extractive PDF cue:** L3DR again achieved better performance compared to the baselines, gaining 15.0(∆15.3%) FPVD, 0.07(∆2.8%) JSD, and an astonishing 1.69 × 10-4(∆46.5%) MMD on SemanticKITTI, and 24.9(∆3.5%) ...
- **p. 8 / 5.3. Other Results - extractive PDF cue:** On an RTX 4090 GPU 24G, the additional time for RRN rectification is 19.65 ms which is negligible compared to LiDM and R2DM sampling processes ...
- **p. 6 / 4.4. Diffusion-agnostic Inference - extractive PDF cue:** Perceptual Distributional Task Method FSVD↓ FPVD↓ JSD↓ MMD×10(-4) ↓ KITTI360 Unconditional LiDARGAN [3] 183.4 168.1 0.272 4.74 LiDARVAE [3] 129.9 105.8 0.237 7.07 ProjectedGAN [36] ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | As a result of Lipschitz continuity throughout the DDIM sampling process, the generated image in theory cannot exhibit arbitrarily sharp spatial transitions. | p. 3 (3.2. Theoretical Analysis) |
| body limitation/failure cue | While 3D models are still generally Lipschitz, the spatial proximity of a point is defined in 3D rather than 2D, adding an additional dimension ... | p. 3 (3.2. Theoretical Analysis) |
| body limitation/failure cue | Figure 6. Visualization of conditional generation on SemanticKITTI. Cyan regions highlight the improved RV artifacts from the diffusion-generated (i.e., denoised) data to our rectified ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | While L3DR does not top the MMD metric, our method still provides a average 7.3% improvement, and is comparable to the bestperforming ProjectedGAN which ... | p. 7 (5.2. Experiment Setup) |
| body limitation/failure cue | Training Seg. w/ noise Generated GT UNet Generated RV & PC RRVP Residuals GT - Gen RVP 3D UNet Welsh Loss Diff. | p. 4 (3.2. Theoretical Analysis) |
| body limitation/failure cue | Figure 4. Visualization of two types of errors in RRN training data. While the generated point clouds (colored) approximate the GT (gray) in most ... | p. 5 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All networks are trained with 4× RTX 4090 24G up to 150 epochs. | p. 6 (5.2. Experiment Setup) |
| Method Network # Params (M) Steps Time (ms) R2DM Eff-UNet 31.10 50 579.83 LiDM VQ-VAE, UNet 257.77 50 557.36 +Ours SPUNET +37.90 +1 +19.65 ... | p. 8 (5.3. Other Results) |
| On an RTX 4090 GPU 24G, the additional time for RRN rectification is 19.65 ms which is negligible compared to LiDM and R2DM sampling ... | p. 8 (5.3. Other Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / 3.2. Theoretical Analysis - extractive PDF cue:** As a result of Lipschitz continuity throughout the DDIM sampling process, the generated image in theory cannot exhibit arbitrarily sharp spatial transitions.
- **p. 3 / 3.2. Theoretical Analysis - extractive PDF cue:** While 3D models are still generally Lipschitz, the spatial proximity of a point is defined in 3D rather than 2D, adding an additional dimension of ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. Visualization of conditional generation on SemanticKITTI. Cyan regions highlight the improved RV artifacts from the diffusion-generated (i.e., denoised) data to our rectified data, ...
- **p. 7 / 5.2. Experiment Setup - extractive PDF cue:** While L3DR does not top the MMD metric, our method still provides a average 7.3% improvement, and is comparable to the bestperforming ProjectedGAN which scores ...
- **p. 4 / 3.2. Theoretical Analysis - extractive PDF cue:** Training Seg. w/ noise Generated GT UNet Generated RV & PC RRVP Residuals GT - Gen RVP 3D UNet Welsh Loss Diff.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Visualization of two types of errors in RRN training data. While the generated point clouds (colored) approximate the GT (gray) in most of ...

- **PDF anchors reviewed:** datasets p. 6 (5.2. Experiment Setup), p. 6 (5.2. Experiment Setup), p. 7 (5.2. Experiment Setup), p. 7 (5.2. Experiment Setup), p. 3 (3.2. Theoretical Analysis), p. 4 (3.3. Empirical Analysis), metrics p. 5 (Figure/Table caption), p. 7 (5.3. Other Results), p. 7 (5.3. Other Results), p. 8 (5.3. Other Results), p. 6 (Figure/Table caption), p. 1 (Figure/Table caption), baselines p. 7 (5.2. Experiment Setup), p. 7 (5.3. Other Results), p. 8 (Figure/Table caption), p. 8 (5.3. Other Results), p. 6 (Figure/Table caption), p. 4 (3.3. Empirical Analysis), results p. 7 (5.2. Experiment Setup), p. 7 (5.2. Experiment Setup), p. 8 (5.3. Other Results), p. 8 (5.3. Other Results), p. 4 (3.2. Theoretical Analysis), p. 4 (3.3. Empirical Analysis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
