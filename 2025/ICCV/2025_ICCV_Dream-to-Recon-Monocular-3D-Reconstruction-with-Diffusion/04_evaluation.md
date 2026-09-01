# Evaluation - Dream-to-Recon: Monocular 3D Reconstruction with Diffusion-Depth Distillation from Single Images

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wulff_Dream-to-Recon_Monocular_3D_Reconstruction_with_Diffusion-Depth_Distillation_from_Single_Images_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wulff_Dream-to-Recon_Monocular_3D_Reconstruction_with_Diffusion-Depth_Distillation_from_Single_Images_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Scene Reconstruction), p. 8 (4.3.2. Occlusion detection in novel views), p. 6 (4.2. Scene Reconstruction), p. 7 (4.3.1. Conditioning of the VCM), p. 7 (4.3.1. Conditioning of the VCM), p. 8 (4.4. Distillation into a Feed-Forward Model)): We contend that, despite being slightly outperformed in quantitative metrics by the directly synthesized geometry, the distilled model is more reliable and significantly faster.

## Evaluation Body Digest

- **p. 5 / 4.1. Setup - extractive PDF cue:** Both datasets contain scenes with complex layouts and possibly dynamic objects.
- **p. 6 / 4.2. Scene Reconstruction - extractive PDF cue:** The distilled scene reconstruction model does not exhibit these issues, as it is trained on a diverse dataset.
- **p. 5 / 4.1. Setup - extractive PDF cue:** We test our method on the challenging KITTI-360 [31] and Waymo [54] self-driving datasets.
- **p. 6 / 4.2. Scene Reconstruction - extractive PDF cue:** In contrast, our synthesized scenes naturally handle such scenarios.
- **p. 8 / 4.3.3. Viewpoint sampling - extractive PDF cue:** We evaluate several pose sampling strategies using our occupancy reconstruction benchmark.
- **p. 7 / 4.3.1. Conditioning of the VCM - extractive PDF cue:** We evaluate different model configurations and training setups.
- **p. 7 / 4.3.1. Conditioning of the VCM - extractive PDF cue:** We present scene reconstructions from several models on KITTI-360 [31] (left) and Waymo [54] (right).
- **p. 8 / 4.4. Distillation into a Feed-Forward Model - extractive PDF cue:** The loss configuration used to distill synthetic data into the scene reconstruction model is critical to its performance.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Scene Reconstruction | SYSTEM / EVALUATION SCOPE UNRESOLVED | We contend that, despite being slightly outperformed in quantitative metrics by the directly synthesized geometry, the distilled model is more reliable and significantly faster. | p. 6 (4.2. Scene Reconstruction) |
| 4.3.2. Occlusion detection in novel views | SYSTEM / EVALUATION SCOPE UNRESOLVED | A camera rig with eight predefined poses and random rotations achieves the best performance. leverages two-way optical flow between the input and novel views ... | p. 8 (4.3.2. Occlusion detection in novel views) |
| 4.2. Scene Reconstruction | SYSTEM / EVALUATION SCOPE UNRESOLVED | We hypothesize that this lack of improvement stems from the strong depth cues already inherent in multi-view data. | p. 6 (4.2. Scene Reconstruction) |
| 4.3.1. Conditioning of the VCM | SYSTEM / EVALUATION SCOPE UNRESOLVED | Despite being trained on single images only, our method achieves accurate reconstructions overall. | p. 7 (4.3.1. Conditioning of the VCM) |
| 4.3.1. Conditioning of the VCM | SYSTEM / EVALUATION SCOPE UNRESOLVED | 2, the full model consistently outperforms the baseline in both color and depth reconstruction metrics on KITTI-360. | p. 7 (4.3.1. Conditioning of the VCM) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Setup - extractive PDF cue:** Both datasets contain scenes with complex layouts and possibly dynamic objects.
- **p. 6 / 4.2. Scene Reconstruction - extractive PDF cue:** The distilled scene reconstruction model does not exhibit these issues, as it is trained on a diverse dataset.
- **p. 5 / 4.1. Setup - extractive PDF cue:** We test our method on the challenging KITTI-360 [31] and Waymo [54] self-driving datasets.
- **p. 6 / 4.2. Scene Reconstruction - extractive PDF cue:** In contrast, our synthesized scenes naturally handle such scenarios.
- **p. 8 / 4.3.3. Viewpoint sampling - extractive PDF cue:** We evaluate several pose sampling strategies using our occupancy reconstruction benchmark.
- **p. 7 / 4.3.1. Conditioning of the VCM - extractive PDF cue:** We evaluate different model configurations and training setups.
- **p. 7 / 4.3.1. Conditioning of the VCM - extractive PDF cue:** We present scene reconstructions from several models on KITTI-360 [31] (left) and Waymo [54] (right).
- **p. 8 / 4.4. Distillation into a Feed-Forward Model - extractive PDF cue:** The loss configuration used to distill synthetic data into the scene reconstruction model is critical to its performance.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Dream-to-Recon. We leverage fine-tuned diffusion models for inpainting and a pre-trained depth predictor to generate high- quality scene geometry from a single image, ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Method overview. a) We train a view completion model (VCM) that inpaints occluded areas and refines warped views. Training uses only a single ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative scene reconstruction. We report cene geometry estimation results using ground-truth derived from accumulated LiDAR scans and semantic annotations on KITTI-360 and Waymo. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative scene reconstruction. We present scene reconstructions from several models on KITTI-360 [31] (left) and Waymo [54] (right). The geometry is discretized into ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Effect of VCM conditioning. We evaluate different model configurations and training setups. VCMsimple receives only masked RGB input. VCMK and VCMK→W denote the ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Effect of VCM conditioning. See Tab. 2.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. Effect of occlusion detection strategies. We compare gradient-based (ours) to optical-flow based occlusion detection, and a combination of both. Occlusions are shown in ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Pose sampling strategies. We evaluate the quality of generated geometry under various pose sampling strategies. A camera rig with eight predefined poses and ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Both datasets contain scenes with complex layouts and possibly dynamic objects. | embodiment, simulator version and control stack | p. 5 (4.1. Setup), p. 6 (4.2. Scene Reconstruction) |
| Task/environment | The distilled scene reconstruction model does not exhibit these issues, as it is trained on a diverse dataset. | reset, timeout, object/scene variation | p. 6 (4.2. Scene Reconstruction), p. 5 (4.1. Setup) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 3 (3.2. Training the View Completion Model), p. 4 (3.2. Training the View Completion Model) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (3.2. Training the View Completion Model) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The accuracy and robustness of our occlusion detection strategy directly influence the effectiveness of refining incomplete novel views using VCM. | definition/direction/unit from same section | p. 7 (4.3.2. Occlusion detection in novel views) |
| We evaluate the overall accuracy of the reconstruction Oacc, as well as the accuracy and recall of the reconstruction in invisible and empty regions ... | definition/direction/unit from same section | p. 6 (4.1. Setup) |
| Here, PSNR measures reconstruction quality of RGB images, and absolute relative error (Abs Rel) is used for depth. | definition/direction/unit from same section | p. 6 (4.1. Setup) |
| The loss configuration used to distill synthetic data into the scene reconstruction model is critical to its performance. | definition/direction/unit from same section | p. 8 (4.4. Distillation into a Feed-Forward Model) |
| Figure 6. Qualitative effect of different loss terms. See Tab. 4. lated variants, our full loss setup achieves competitive Oacc and the highest IEacc. ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| We add batch-normalization layers to the backbone's decoder to stabilize mixed-precision training. | definition/direction/unit from same section | p. 5 (4.1. Setup) |
| Furthermore, we carefully validate our design choices for the view completion model, scene synthesis, and distillation procedure. | definition/direction/unit from same section | p. 5 (4. Experiments) |
| Despite being trained on single images only, our method achieves accurate reconstructions overall. | definition/direction/unit from same section | p. 7 (4.3.1. Conditioning of the VCM) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Here, the state-of-the-art volumetric reconstruction methods Behind the Scenes (BTS) [60] and Know Your Neighbor (KYN) [27] serve as baselines. | comparison identity and matched condition | p. 6 (4.2. Scene Reconstruction) |
| 2, the full model consistently outperforms the baseline in both color and depth reconstruction metrics on KITTI-360. | comparison identity and matched condition | p. 7 (4.3.1. Conditioning of the VCM) |
| Both the synthesized scenes and the distilled model match or surpass baselines, despite not requiring multi-view training data. | comparison identity and matched condition | p. 6 (4.1. Setup) |
| Camera rigs outperform random warp sampling strategies, as their cameras are already defined in sensible poses. | comparison identity and matched condition | p. 8 (4.3.3. Viewpoint sampling) |
| The fused strategy mitigates some of the false positives compared to optical flow alone but still inherits many of its limitations. | comparison identity and matched condition | p. 8 (4.3.2. Occlusion detection in novel views) |
| Figure 2. Method overview. a) We train a view completion model (VCM) that inpaints occluded areas and refines warped views. Training uses only a ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 6. Qualitative effect of different loss terms. See Tab. 4. lated variants, our full loss setup achieves competitive Oacc and the highest IEacc. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We evaluate both configurations on the KITTI-360 dataset (VCMK), and further examine the effect of finetuning on Waymo (VCMK→W). | component/input/data sensitivity | p. 6 (4.3.1. Conditioning of the VCM) |
| Effect of occlusion detection strategies. | component/input/data sensitivity | p. 8 (4.3.2. Occlusion detection in novel views) |
| To this end, we rigorously validate our design choices through a series of ablation studies. | component/input/data sensitivity | p. 6 (4.3. Scene Synthesis using the VCM) |
| Figure 4. Effect of VCM conditioning. See Tab. 2. | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Figure 1. Dream-to-Recon. We leverage fine-tuned diffusion models for inpainting and a pre-trained depth predictor to generate high- quality scene geometry from a single ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Furthermore, we show that our method has unique advantages when it comes to dynamic scenes. | We contend that, despite being slightly outperformed in quantitative metrics by the directly synthesized geometry, the distilled model is more reliable and significantly faster. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Scene Reconstruction), p. 8 (4.3.2. Occlusion detection in novel views), p. 6 (4.2. Scene Reconstruction), p. 7 (4.3.1. Conditioning of the VCM), p. 7 (4.3.1. Conditioning of the VCM), p. 8 (4.4. Distillation into a Feed-Forward Model) |
| Primary metric/result | A camera rig with eight predefined poses and random rotations achieves the best performance. leverages two-way optical flow between the input and novel views ... | numeric claim only at cited anchor | p. 8 (4.3.2. Occlusion detection in novel views) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Setup - extractive PDF cue:** For KITTI-360, we load images at 384×1280 resolution during View Completion Model training and at 192 × 640 resolution otherwise.
- **p. 4 / 3.2. Training the View Completion Model - extractive PDF cue:** 1 ControlNet Denoising U-Net VCM Noise CLIP(Iin) a) View Completion Model Training b) Multi-view and 3D Data Synthesis Predict Depth VCM c) Synthetic Data Distillation ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This failure stems from their use of multi-view data across multiple timesteps, which introduces inconsistency when the object is in motion. | p. 6 (4.2. Scene Reconstruction) |
| body limitation/failure cue | Since depth prediction cannot reason about occluded areas, we do not report the IEacc and IErec metrics. | p. 6 (4.2. Scene Reconstruction) |
| body limitation/failure cue | The fused strategy mitigates some of the false positives compared to optical flow alone but still inherits many of its limitations. | p. 8 (4.3.2. Occlusion detection in novel views) |
| body limitation/failure cue | The accuracy and robustness of our occlusion detection strategy directly influence the effectiveness of refining incomplete novel views using VCM. | p. 7 (4.3.2. Occlusion detection in novel views) |
| body limitation/failure cue | 5, the depth gradient method robustly captures occlusions without requiring extensive post-filtering. | p. 8 (4.3.2. Occlusion detection in novel views) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 1 ControlNet Denoising U-Net VCM Noise CLIP(Iin) a) View Completion Model Training b) Multi-view and 3D Data Synthesis Predict Depth VCM c) Synthetic Data ... | p. 4 (3.2. Training the View Completion Model) |
| We add batch-normalization layers to the backbone's decoder to stabilize mixed-precision training. | p. 5 (4.1. Setup) |
| Legend: ⋆: official checkpoint, †: results as reported in the reference. | p. 6 (4.1. Setup) |
| Both use multi-view supervision from all cameras and multiple time steps. | p. 6 (4.2. Scene Reconstruction) |
| The ray is evaluated at discrete steps x for density σ(x) and color c(x). | p. 4 (3.3. Synthesizing Scene Geometry) |
| We leverage this aspect and compute a depth gradient map using Sobel filters on the inverse depth map, which highlights regions with significant depth ... | p. 5 (3.3. Synthesizing Scene Geometry) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.2. Scene Reconstruction - extractive PDF cue:** This failure stems from their use of multi-view data across multiple timesteps, which introduces inconsistency when the object is in motion.
- **p. 6 / 4.2. Scene Reconstruction - extractive PDF cue:** Since depth prediction cannot reason about occluded areas, we do not report the IEacc and IErec metrics.
- **p. 8 / 4.3.2. Occlusion detection in novel views - extractive PDF cue:** The fused strategy mitigates some of the false positives compared to optical flow alone but still inherits many of its limitations.
- **p. 7 / 4.3.2. Occlusion detection in novel views - extractive PDF cue:** The accuracy and robustness of our occlusion detection strategy directly influence the effectiveness of refining incomplete novel views using VCM.
- **p. 8 / 4.3.2. Occlusion detection in novel views - extractive PDF cue:** 5, the depth gradient method robustly captures occlusions without requiring extensive post-filtering.

- **PDF anchors reviewed:** datasets p. 5 (4.1. Setup), p. 6 (4.2. Scene Reconstruction), p. 5 (4.1. Setup), p. 6 (4.2. Scene Reconstruction), p. 8 (4.3.3. Viewpoint sampling), p. 7 (4.3.1. Conditioning of the VCM), metrics p. 7 (4.3.2. Occlusion detection in novel views), p. 6 (4.1. Setup), p. 6 (4.1. Setup), p. 8 (4.4. Distillation into a Feed-Forward Model), p. 8 (Figure/Table caption), p. 5 (4.1. Setup), baselines p. 6 (4.2. Scene Reconstruction), p. 7 (4.3.1. Conditioning of the VCM), p. 6 (4.1. Setup), p. 8 (4.3.3. Viewpoint sampling), p. 8 (4.3.2. Occlusion detection in novel views), p. 4 (Figure/Table caption), results p. 6 (4.2. Scene Reconstruction), p. 8 (4.3.2. Occlusion detection in novel views), p. 6 (4.2. Scene Reconstruction), p. 7 (4.3.1. Conditioning of the VCM), p. 7 (4.3.1. Conditioning of the VCM), p. 8 (4.4. Distillation into a Feed-Forward Model).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
