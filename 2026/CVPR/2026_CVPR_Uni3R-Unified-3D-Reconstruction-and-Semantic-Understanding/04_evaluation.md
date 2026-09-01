# Evaluation - Uni3R: Unified 3D Reconstruction and Semantic Understanding via Generalizable Gaussian Splatting from Unposed Multi-View Images

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Sun_Uni3R_Unified_3D_Reconstruction_and_Semantic_Understanding_via_Generalizable_Gaussian_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Experiment Results), p. 6 (4.2. Experiment Results), p. 7 (0.724 17.28 13.31 ≈60min), p. 7 (0.724 17.28 13.31 ≈60min), p. 8 (4.3. Analysis and Ablations), p. 8 (Figure/Table caption)): Notably, it achieves superior performance in both novel view synthesis and open-vocabulary segmentation, offering a substantial speed advantage over traditional per-scene optimization methods.

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** We evaluate on 40 unseen ScanNet scenes, and further examine the model's zero-shot generalization on the MipNeRF360 [1] dataset.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Dataset For evaluating both 3D scene and semantic field reconstruction, our model is trained on a combined dataset of ScanNet++ [41] and ScanNet [6], totaling ...
- **p. 7 / 0.724 17.28 13.31 ≈60min - extractive PDF cue:** Quantitative comparisons of novel view synthesis on the RE10k [46] and ACID [22] dataset under 2-views setup.
- **p. 7 / 0.724 17.28 13.31 ≈60min - extractive PDF cue:** 3, Uni3R outperforms pose-dependent methods, such as PixelSplat and MVSplat, by a clear margin (1.7dB), and slightly surpasses baseline model NoPoSplat with a gain of ...
- **p. 8 / 0.724 17.28 13.31 ≈60min - extractive PDF cue:** Comparison with 4 and 8-view settings on the RE10k [46] and ScanNet [6] datasets.
- **p. 8 / 0.724 17.28 13.31 ≈60min - extractive PDF cue:** Zero-shot generalization on Mip-NeRF360 [1] dataset View Nums PSNR↑SSIM↑LPIPS↓mIoU↑Acc↑ rel↓
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 7. Ablation Study on different modules. We evaluate the ablated variants of Uni3R, by recording their rendering quality, segmentation performance and geometric accuracy. Removing ...
- **p. 6 / 4.2. Experiment Results - extractive PDF cue:** The underlying multi-view geometry acts as a spatial filter that ‘votes out' inconsistent 2D errors.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setup (p. 6); 4.2. Experiment Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Experiment Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Notably, it achieves superior performance in both novel view synthesis and open-vocabulary segmentation, offering a substantial speed advantage over traditional per-scene optimization methods. | p. 6 (4.2. Experiment Results) |
| 4.2. Experiment Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | While Uni3R is supervised by LSeg, it outperforms by resolving 2D view-dependent ambiguities through 3D spatial fusion. | p. 6 (4.2. Experiment Results) |
| 0.724 17.28 13.31 ≈60min | EMPIRICAL / SOURCE-REPORTED EVALUATION | Uni3R consistently outperforms all baselines under both 4-view and 8-view settings. | p. 7 (0.724 17.28 13.31 ≈60min) |
| 0.724 17.28 13.31 ≈60min | EMPIRICAL / SOURCE-REPORTED EVALUATION | 3, Uni3R outperforms pose-dependent methods, such as PixelSplat and MVSplat, by a clear margin (1.7dB), and slightly surpasses baseline model NoPoSplat with a gain ... | p. 7 (0.724 17.28 13.31 ≈60min) |
| 4.3. Analysis and Ablations | EMPIRICAL / SOURCE-REPORTED EVALUATION | The scale-invariant constraint contributes to rendering stability across scenes with varying depth ranges, while the intrinsic embedding improves robustness by aligning scenes of varying ... | p. 8 (4.3. Analysis and Ablations) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** We evaluate on 40 unseen ScanNet scenes, and further examine the model's zero-shot generalization on the MipNeRF360 [1] dataset.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Dataset For evaluating both 3D scene and semantic field reconstruction, our model is trained on a combined dataset of ScanNet++ [41] and ScanNet [6], totaling ...
- **p. 7 / 0.724 17.28 13.31 ≈60min - extractive PDF cue:** Quantitative comparisons of novel view synthesis on the RE10k [46] and ACID [22] dataset under 2-views setup.
- **p. 7 / 0.724 17.28 13.31 ≈60min - extractive PDF cue:** 3, Uni3R outperforms pose-dependent methods, such as PixelSplat and MVSplat, by a clear margin (1.7dB), and slightly surpasses baseline model NoPoSplat with a gain of ...
- **p. 8 / 0.724 17.28 13.31 ≈60min - extractive PDF cue:** Comparison with 4 and 8-view settings on the RE10k [46] and ScanNet [6] datasets.
- **p. 8 / 0.724 17.28 13.31 ≈60min - extractive PDF cue:** Zero-shot generalization on Mip-NeRF360 [1] dataset View Nums PSNR↑SSIM↑LPIPS↓mIoU↑Acc↑ rel↓

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Uni3R takes unposed arbitrary multi-view images as input and produces a unified 3D Gaussian scene representation, enabling state-of-the-art performance in view synthesis, semantic ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Architectural overview of the Uni3R pipeline. Uni3R predicts a set of Gaussian primitives with jointly integrated geometry, appearance, and open-vocabulary semantics in a ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative comparison of novel view synthesis on RealEstate10k test set with 8 input images.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative Comparison on ScanNet. We evaluate performance on novel view synthesis, depth estimation, and open-vocabulary semantic segmentation. (*) Unlike LSM, Uni3R is trained ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison with Per-Scene Optimized Methods. Time corresponds to the average reconstruction time per scene. Images GT LSeg Feature 3DGS LSM Uni3R (Ours) Wall
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative Comparison of Novel-View Segmentation on ScanNet. RE10k ACID
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Quantitative comparisons of novel view synthesis on the RE10k [46] and ACID [22] dataset under 2-views setup. Novel-View Synthesis As shown in Tab. ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Comparison with 4 and 8-view settings on the RE10k [46] and ScanNet [6] datasets. 2View 8View

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate on 40 unseen ScanNet scenes, and further examine the model's zero-shot generalization on the MipNeRF360 [1] dataset. | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Task/environment | Dataset For evaluating both 3D scene and semantic field reconstruction, our model is trained on a combined dataset of ScanNet++ [41] and ScanNet [6], ... | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setup), p. 7 (0.724 17.28 13.31 ≈60min) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3.2. Rendering with Open-Vocabulary Semantics), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.1.2. Cross-View Transformer Encoder), p. 5 (3.3. Training Objectives) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 7. Ablation Study on different modules. We evaluate the ablated variants of Uni3R, by recording their rendering quality, segmentation performance and geometric accuracy. ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| The underlying multi-view geometry acts as a spatial filter that ‘votes out' inconsistent 2D errors. | definition/direction/unit from same section | p. 6 (4.2. Experiment Results) |
| When the geometric loss is removed, the model exhibits degraded 3D consistency (higher depth error and lower τ), validating its effectiveness in improving point ... | definition/direction/unit from same section | p. 8 (4.3. Analysis and Ablations) |
| 5, Uni3R demonstrates strong generalization by reconstructing consistent 3D geometry, rendering and semantics from unposed multiview inputs. | definition/direction/unit from same section | p. 6 (4.2. Experiment Results) |
| 3 demonstrates Uni3R consistently produces more detailed and structurally coherent constructions. | definition/direction/unit from same section | p. 7 (0.724 17.28 13.31 ≈60min) |
| Figure 1. Uni3R takes unposed arbitrary multi-view images as input and produces a unified 3D Gaussian scene representation, enabling state-of-the-art performance in view synthesis, ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Architectural overview of the Uni3R pipeline. Uni3R predicts a set of Gaussian primitives with jointly integrated geometry, appearance, and open-vocabulary semantics in ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Uni3R consistently outperforms all baselines under both 4-view and 8-view settings. | comparison identity and matched condition | p. 7 (0.724 17.28 13.31 ≈60min) |
| 3, Uni3R outperforms pose-dependent methods, such as PixelSplat and MVSplat, by a clear margin (1.7dB), and slightly surpasses baseline model NoPoSplat with a gain ... | comparison identity and matched condition | p. 7 (0.724 17.28 13.31 ≈60min) |
| For a fair comparison with the baseline models, we report all quantitative results under 256 × 256. | comparison identity and matched condition | p. 6 (4.1. Experimental Setup) |
| While Uni3R is supervised by LSeg, it outperforms by resolving 2D view-dependent ambiguities through 3D spatial fusion. | comparison identity and matched condition | p. 6 (4.2. Experiment Results) |
| Figure 1. Uni3R takes unposed arbitrary multi-view images as input and produces a unified 3D Gaussian scene representation, enabling state-of-the-art performance in view synthesis, ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| This experiment highlights Uni3R's ability to handle long sequences and wide-baseline configurations, producing high-fidelity and semantically consistent 3D reconstructions in a single feed-forward pass. | comparison identity and matched condition | p. 8 (4.3. Analysis and Ablations) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 7. Ablation Study on different modules. We evaluate the ablated variants of Uni3R, by recording their rendering quality, segmentation performance and geometric accuracy. ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| When the geometric loss is removed, the model exhibits degraded 3D consistency (higher depth error and lower τ), validating its effectiveness in improving point ... | component/input/data sensitivity | p. 8 (4.3. Analysis and Ablations) |
| Table 1. Quantitative Comparison on ScanNet. We evaluate performance on novel view synthesis, depth estimation, and open-vocabulary semantic segmentation. (*) Unlike LSM, Uni3R is ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| We initialize the encoder and decoder with the weights from the pretrained VGGT [36], while the remaining intrinsic layer and Gaussian head are randomly ... | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as follows: • We introduce Uni3R, a novel feed-forward architecture that unifies 3D reconstruction and semantic understanding. | Notably, it achieves superior performance in both novel view synthesis and open-vocabulary segmentation, offering a substantial speed advantage over traditional per-scene optimization methods. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Experiment Results), p. 6 (4.2. Experiment Results), p. 7 (0.724 17.28 13.31 ≈60min), p. 7 (0.724 17.28 13.31 ≈60min), p. 8 (4.3. Analysis and Ablations), p. 8 (Figure/Table caption) |
| Primary metric/result | While Uni3R is supervised by LSeg, it outperforms by resolving 2D view-dependent ambiguities through 3D spatial fusion. | numeric claim only at cited anchor | p. 6 (4.2. Experiment Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Dataset For evaluating both 3D scene and semantic field reconstruction, our model is trained on a combined dataset of ScanNet++ [41] and ScanNet [6], totaling ...
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** All experiments are conducted on 8 × A100 GPUs, taking approximately 22 hours for the training of 2 views, with a batch size of 2.
- **p. 6 / 3.3. Training Objectives - extractive PDF cue:** Time↓ Source View Target View Method SfM Per-Scene mIoU↑Acc.↑ rel↓ τ ↑ mIoU↑Acc.↑PSNR↑SSIM↑LPIPS↓ LSeg N/A N/A 0.4701 0.7891 - - 0.4819 0.7927 - - - ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Thus, Uni3R not only mimics LSeg, but also leverages 3D consistency to produce a denoised, robust semantic prediction. | p. 6 (4.2. Experiment Results) |
| body limitation/failure cue | When the geometric loss is removed, the model exhibits degraded 3D consistency (higher depth error and lower τ), validating its effectiveness in improving point ... | p. 8 (4.3. Analysis and Ablations) |
| body limitation/failure cue | The scale-invariant constraint contributes to rendering stability across scenes with varying depth ranges, while the intrinsic embedding improves robustness by aligning scenes of varying ... | p. 8 (4.3. Analysis and Ablations) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Implementation Details We use DINOv2 [26] as the image encoder, with a patch size of 16, and set the CrossView Transformer layers as L ... | p. 6 (4.1. Experimental Setup) |
| All experiments are conducted on 8 × A100 GPUs, taking approximately 22 hours for the training of 2 views, with a batch size of ... | p. 6 (4.1. Experimental Setup) |
| We extract feature maps ˜F (i) from each input image using the LSeg image encoder. | p. 5 (3.3. Training Objectives) |
| Following NoPoSplat [40], we encode each camera's focal length and principal point with a linear projection. | p. 4 (3.1.1. Intrinsic Embedding) |
| The output latent tokens from the encoder encapsulate a holistic and globally consistent understanding of the 3D scene. | p. 4 (3.1.2. Cross-View Transformer Encoder) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.2. Experiment Results - extractive PDF cue:** Thus, Uni3R not only mimics LSeg, but also leverages 3D consistency to produce a denoised, robust semantic prediction.
- **p. 8 / 4.3. Analysis and Ablations - extractive PDF cue:** When the geometric loss is removed, the model exhibits degraded 3D consistency (higher depth error and lower τ), validating its effectiveness in improving point cloud ...
- **p. 8 / 4.3. Analysis and Ablations - extractive PDF cue:** The scale-invariant constraint contributes to rendering stability across scenes with varying depth ranges, while the intrinsic embedding improves robustness by aligning scenes of varying scales ...

- **PDF anchors reviewed:** datasets p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 7 (0.724 17.28 13.31 ≈60min), p. 7 (0.724 17.28 13.31 ≈60min), p. 8 (0.724 17.28 13.31 ≈60min), p. 8 (0.724 17.28 13.31 ≈60min), metrics p. 8 (Figure/Table caption), p. 6 (4.2. Experiment Results), p. 8 (4.3. Analysis and Ablations), p. 6 (4.2. Experiment Results), p. 7 (0.724 17.28 13.31 ≈60min), p. 1 (Figure/Table caption), baselines p. 7 (0.724 17.28 13.31 ≈60min), p. 7 (0.724 17.28 13.31 ≈60min), p. 6 (4.1. Experimental Setup), p. 6 (4.2. Experiment Results), p. 1 (Figure/Table caption), p. 8 (4.3. Analysis and Ablations), results p. 6 (4.2. Experiment Results), p. 6 (4.2. Experiment Results), p. 7 (0.724 17.28 13.31 ≈60min), p. 7 (0.724 17.28 13.31 ≈60min), p. 8 (4.3. Analysis and Ablations), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
