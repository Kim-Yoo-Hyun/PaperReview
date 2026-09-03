# Evaluation - Triplane Meets Gaussian Splatting: Fast and Generalizable Single-View 3D Reconstruction with Transformers

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Zou_Triplane_Meets_Gaussian_Splatting_Fast_and_Generalizable_Single-View_3D_Reconstruction_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Zou_Triplane_Meets_Gaussian_Splatting_Fast_and_Generalizable_Single-View_3D_Reconstruction_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.5. Runtime Efficiency), p. 7 (4.6. Ablation Study), p. 6 (4.1. Implementation Details), p. 8 (4.6. Ablation Study), p. 8 (4.6. Ablation Study), p. 3 (Figure/Table caption)): We can find that our method has achieved significant improvements in speed for both reconstruction and rendering processes compared to other baselines, benefiting from feed-forward fashion and efficient rasterization.

## Evaluation Body Digest

- **p. 6 / 4.1. Implementation Details - extractive body cue:** Qualitative comparisons of novel view synthesis from reconstructed object between our method and other baselines on the GSO dataset.
- **p. 6 / 4.1. Implementation Details - extractive body cue:** For Evaluation, we adopt the Google Scanned Objects (GSO) dataset [13], which includes a wide variety of high-quality scanned household items, to evaluate the performance ...
- **p. 8 / 4.6. Ablation Study - extractive body cue:** However, for some multiview datasets, obtaining accurate and complete groundtruth 3D models is not an easy task.
- **p. 5 / 4.1. Implementation Details - extractive body cue:** Baselines, Dataset, and Metrics Baselines.
- **p. 7 / 4.3. Single View Reconstruction - extractive body cue:** Quantitative comparison on novel-view synthesis from single images on the GSO dataset, in terms of PSNR, SSIM, LPIPS, and runtime efficiency.
- **p. 7 / 4.3. Single View Reconstruction - extractive body cue:** Quantitative Comparison for single view 3D reconstruction on the GSO dataset, in terms of Chamfer Distance ×10-3, Volume IoU and runtime efficiency.
- **p. 8 / 4.6. Ablation Study - extractive body cue:** In the absence of ground-truth 3D models, we can address this issue by overfitting each object using Gaussian Splatting and leveraging them for pseudo-point-cloud supervision.
- **p. 7 / 4.6. Ablation Study - extractive body cue:** As shown in Table 4, image-based shape codes achieve higher IoU com10330

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Implementation Details (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.5. Runtime Efficiency | SYSTEM / EVALUATION SCOPE UNRESOLVED | We can find that our method has achieved significant improvements in speed for both reconstruction and rendering processes compared to other baselines, benefiting from ... | p. 7 (4.5. Runtime Efficiency) |
| 4.6. Ablation Study | SYSTEM / EVALUATION SCOPE UNRESOLVED | Our TriplaneGaussian, leveraging the projection-aware condition with explicit geometry, excels in producing more detailed texture compared to Triplane-NeRF, as illustrated in the red box ... | p. 7 (4.6. Ablation Study) |
| 4.1. Implementation Details | SYSTEM / EVALUATION SCOPE UNRESOLVED | Our approach achieves both quality and consistency across different novel views. | p. 6 (4.1. Implementation Details) |
| 4.6. Ablation Study | SYSTEM / EVALUATION SCOPE UNRESOLVED | While the projection-aware condition improves rendering quality on the same side as the input view, achieving good texture on the backside remains challenging (see ... | p. 8 (4.6. Ablation Study) |
| 4.6. Ablation Study | SYSTEM / EVALUATION SCOPE UNRESOLVED | Moreover, the projection-aware condition outperforms the other two code methods in terms of CD, suggesting that the local patterns of the image are effectively ... | p. 8 (4.6. Ablation Study) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Implementation Details - extractive body cue:** Qualitative comparisons of novel view synthesis from reconstructed object between our method and other baselines on the GSO dataset.
- **p. 6 / 4.1. Implementation Details - extractive body cue:** For Evaluation, we adopt the Google Scanned Objects (GSO) dataset [13], which includes a wide variety of high-quality scanned household items, to evaluate the performance ...
- **p. 8 / 4.6. Ablation Study - extractive body cue:** However, for some multiview datasets, obtaining accurate and complete groundtruth 3D models is not an easy task.
- **p. 5 / 4.1. Implementation Details - extractive body cue:** Baselines, Dataset, and Metrics Baselines.
- **p. 7 / 4.3. Single View Reconstruction - extractive body cue:** Quantitative comparison on novel-view synthesis from single images on the GSO dataset, in terms of PSNR, SSIM, LPIPS, and runtime efficiency.
- **p. 7 / 4.3. Single View Reconstruction - extractive body cue:** Quantitative Comparison for single view 3D reconstruction on the GSO dataset, in terms of Chamfer Distance ×10-3, Volume IoU and runtime efficiency.
- **p. 8 / 4.6. Ablation Study - extractive body cue:** In the absence of ground-truth 3D models, we can address this issue by overfitting each object using Gaussian Splatting and leveraging them for pseudo-point-cloud supervision.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We propose a method that enables fast reconstruction from a single-view image. We build the 3D representation upon a hybrid Triplane-Gaussian representation by ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. The overview of our framework. Given an image with its camera parameters, we first encode them into a set of latent feature tokens ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative comparisons of novel view synthesis from reconstructed object between our method and other baselines on the GSO dataset. Our approach achieves both ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative comparisons of geometry reconstruction from a single image between our method and other baselines on the GSO dataset. One-2-3-45 [35]. Point-E [45] ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Quantitative Comparison for single view 3D reconstruc- tion on the GSO dataset, in terms of Chamfer Distance ×10-3, Volume IoU and runtime efficiency. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Quantitative comparison on novel-view synthesis from single images on the GSO dataset, in terms of PSNR, SSIM, LPIPS, and runtime efficiency. PSNR ↑ ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Quantitative comparison between different representa- tions for novel view synthesis on GSO.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Quantitative Comparison of different conditions for point cloud up-sampling in geometry reconstruction. P.C. G.E. GT 3D PSNR ↑ SSIM ↑ LPIPS ↓

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Qualitative comparisons of novel view synthesis from reconstructed object between our method and other baselines on the GSO dataset. | embodiment, simulator version and control stack | p. 6 (4.1. Implementation Details), p. 6 (4.1. Implementation Details) |
| Task/environment | For Evaluation, we adopt the Google Scanned Objects (GSO) dataset [13], which includes a wide variety of high-quality scanned household items, to evaluate the ... | reset, timeout, object/scene variation | p. 6 (4.1. Implementation Details), p. 8 (4.6. Ablation Study) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 4 (3.1. Hybrid Triplane-Gaussian) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.2. Reconstruction from Single-View Images), p. 5 (3.2. Reconstruction from Single-View Images) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Quantitative Comparison for single view 3D reconstruction on the GSO dataset, in terms of Chamfer Distance ×10-3, Volume IoU and runtime efficiency. | definition/direction/unit from same section | p. 7 (4.3. Single View Reconstruction) |
| As shown in Table 4, image-based shape codes achieve higher IoU com10330 | definition/direction/unit from same section | p. 7 (4.6. Ablation Study) |
| We find it hard to train our model successfully only by rendering loss after some attempts, so we leverage the 3D supervision from the ... | definition/direction/unit from same section | p. 8 (4.6. Ablation Study) |
| We utilize a pre-trained DINOv2 [46] as our image encoder, which generates 768-dimension feature tokens with a patch size of 14. | definition/direction/unit from same section | p. 5 (4.1. Implementation Details) |
| Initially, we train the point decoder using λc = 10 and λe = 10 only with CD loss and EMD loss, enabling the network ... | definition/direction/unit from same section | p. 5 (4.1. Implementation Details) |
| It directly builds an SDF field by SparseNeuS [39], achieving state-of-the-art performance. | definition/direction/unit from same section | p. 6 (4.1. Implementation Details) |
| Point-E tends to produce holes in the reconstructed meshes due to the sparsity of the generated point cloud. | definition/direction/unit from same section | p. 6 (4.3. Single View Reconstruction) |
| In Figure 5 (right), two examples illustrate its visual effects. | definition/direction/unit from same section | p. 8 (4.6. Ablation Study) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We can find that our method has achieved significant improvements in speed for both reconstruction and rendering processes compared to other baselines, benefiting from ... | comparison identity and matched condition | p. 7 (4.5. Runtime Efficiency) |
| Qualitative comparisons of geometry reconstruction from a single image between our method and other baselines on the GSO dataset. | comparison identity and matched condition | p. 6 (4.1. Implementation Details) |
| Qualitative comparisons of novel view synthesis from reconstructed object between our method and other baselines on the GSO dataset. | comparison identity and matched condition | p. 6 (4.1. Implementation Details) |
| We also evaluate the runtime efficiency of our method in comparison with other baseline approaches. | comparison identity and matched condition | p. 7 (4.5. Runtime Efficiency) |
| Baselines, Dataset, and Metrics Baselines. | comparison identity and matched condition | p. 5 (4.1. Implementation Details) |
| We compare our method with the previous state-of-the-art single-image reconstruction and generation methods. | comparison identity and matched condition | p. 5 (4.1. Implementation Details) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Quantitative effect of projection-aware condition, geometry-aware encoding and ground-truth 3D supervision to novel view synthesis. ble 2 demonstrate the runtime of reconstruction and rendering ... | component/input/data sensitivity | p. 7 (4.5. Runtime Efficiency) |
| Qualitative comparison with 3DG and Triplane-NeRF (left) and qualitative effect of projection-aware condition and geometryaware encoding (right), where the (a-d) are corresponding with (a-d) ... | component/input/data sensitivity | p. 8 (4.6. Ablation Study) |
| We first conduct experiments with two ablation shape code settings to investigate the impact of different shape codes within the point upsampling module, including ... | component/input/data sensitivity | p. 7 (4.6. Ablation Study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our approach consists of two networks for reconstructing the point cloud and triplane from the input image, employing a fully transformer-based architecture for both. | We can find that our method has achieved significant improvements in speed for both reconstruction and rendering processes compared to other baselines, benefiting from ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.5. Runtime Efficiency), p. 7 (4.6. Ablation Study), p. 6 (4.1. Implementation Details), p. 8 (4.6. Ablation Study), p. 8 (4.6. Ablation Study), p. 3 (Figure/Table caption) |
| Primary metric/result | Our TriplaneGaussian, leveraging the projection-aware condition with explicit geometry, excels in producing more detailed texture compared to Triplane-NeRF, as illustrated in the red box ... | numeric claim only at cited anchor | p. 7 (4.6. Ablation Study) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Implementation Details - extractive body cue:** The positional embeddings of the point decoder consist of 2048 tokens with 512 dimensions, corresponding to 2048 points.
- **p. 5 / 4.1. Implementation Details - extractive body cue:** The positional embeddings of the triplane decoder comprise three 32 × 32 tokens, each with 512 dimensions, representing three axis-aligned planes.
- **p. 7 / 4.6. Ablation Study - extractive body cue:** Furthermore, once the 3D Gaussians are decoded, our rendering process demonstrates faster performance compared to Triplane-NeRF (48ms).
- **p. 5 / 3.2. Reconstruction from Single-View Images - extractive body cue:** Due to limited computation and memory resources, we only decode a coarse point cloud with 2048 points in this step.
- **p. 5 / 3.2. Reconstruction from Single-View Images - extractive body cue:** Therefore, we adopt a lifting module with two-step Snowflake point deconvolution (SPD) [73, 74] to densify the point clouds from 2048 points to 16384 points.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | One-2-345 [35] trains a robust multi-view reconstruction model which takes multi-view images generated from a 2D diffusion model (e.g., Zero-1-2-3). | p. 6 (4.1. Implementation Details) |
| body limitation/failure cue | Additionally, by leveraging the transformer architecture and local feature projection, our model exhibits robust generalization to unseen objects while preserving intricate textures. | p. 7 (4.4. Novel View Synthesis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The point decoder and triplane decoder are both 10-layer transformer networks with hidden dimension 512. | p. 5 (4.1. Implementation Details) |
| The positional embeddings of the point decoder consist of 2048 tokens with 512 dimensions, corresponding to 2048 points. | p. 5 (4.1. Implementation Details) |
| As shown in Table 4, image-based shape codes achieve higher IoU com10330 | p. 7 (4.6. Ablation Study) |
| We also evaluate the runtime efficiency of our method in comparison with other baseline approaches. | p. 7 (4.5. Runtime Efficiency) |
| We also assess the impact of the projection-aware condition on the 3D Gaussian Decoder for novel view synthesis. | p. 8 (4.6. Ablation Study) |
| Geometry-aware encoding enables the triplane decoder to predict backside texture with a shape prior, considering that shoes often have a similar texture on both ... | p. 8 (4.6. Ablation Study) |
| The 3D Gaussians' attributes include opacity α, anisotropic covariance (represented by a scale s and rotation q) and spherical harmonics (SH) coefficients sh [28]: ... | p. 4 (3.1. Hybrid Triplane-Gaussian) |
| Subsequently, a triplane decoder takes these points along with the image features and outputs the triplane features. | p. 4 (3. Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.1. Implementation Details - extractive body cue:** One-2-345 [35] trains a robust multi-view reconstruction model which takes multi-view images generated from a 2D diffusion model (e.g., Zero-1-2-3).
- **p. 7 / 4.4. Novel View Synthesis - extractive body cue:** Additionally, by leveraging the transformer architecture and local feature projection, our model exhibits robust generalization to unseen objects while preserving intricate textures.

- **Evidence anchors reviewed:** datasets p. 6 (4.1. Implementation Details), p. 6 (4.1. Implementation Details), p. 8 (4.6. Ablation Study), p. 5 (4.1. Implementation Details), p. 7 (4.3. Single View Reconstruction), p. 7 (4.3. Single View Reconstruction), metrics p. 7 (4.3. Single View Reconstruction), p. 7 (4.6. Ablation Study), p. 8 (4.6. Ablation Study), p. 5 (4.1. Implementation Details), p. 5 (4.1. Implementation Details), p. 6 (4.1. Implementation Details), baselines p. 7 (4.5. Runtime Efficiency), p. 6 (4.1. Implementation Details), p. 6 (4.1. Implementation Details), p. 7 (4.5. Runtime Efficiency), p. 5 (4.1. Implementation Details), p. 5 (4.1. Implementation Details), results p. 7 (4.5. Runtime Efficiency), p. 7 (4.6. Ablation Study), p. 6 (4.1. Implementation Details), p. 8 (4.6. Ablation Study), p. 8 (4.6. Ablation Study), p. 3 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
