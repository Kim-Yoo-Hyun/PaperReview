# Evaluation - 3D Geometry-Aware Deformable Gaussian Splatting for Dynamic View Synthesis

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Lu_3D_Geometry-Aware_Deformable_Gaussian_Splatting_for_Dynamic_View_Synthesis_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Lu_3D_Geometry-Aware_Deformable_Gaussian_Splatting_for_Dynamic_View_Synthesis_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.5. Ablation Study), p. 7 (4.3. Quantitative Results), p. 7 (4.3. Quantitative Results), p. 3 (Figure/Table caption), p. 8 (4.5. Ablation Study)): Compared with the results (dubbed as "PointNet feat." and "Plane feat.") in Table 4, it can be observed that our method achieves significant performance gains.

## Evaluation Body Digest

- **p. 6 / 4.1. Dataset - extractive PDF cue:** The synthetic dataset D-NeRF [37] contains 8 dynamic scenes, including Hell Warrior, Mutant, Hook, Bouncing Balls, Lego, T-Rex, Stand Up, and Jumping Jacks.
- **p. 6 / 4.1. Dataset - extractive PDF cue:** The real dataset proposed by HyperNeRF [34], including interp-cut-lemon, interp-cut-lemon1, vrigchicken, vrig-3dprinter, misc-split-cookie, and misc-splitcookie.
- **p. 7 / 4.3. Quantitative Results - extractive PDF cue:** We further compare our method with some highly related works on the real scene dataset proposed by [34].
- **p. 7 / 4.3. Quantitative Results - extractive PDF cue:** NeRF, TiNeuVox, NDVG, FDNeRF, and 4D-GS on the DNeRF Dataset.
- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** We conduct ablation studies on the synthetic dataset (800× 800) to verify the effectiveness of our proposed components.
- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** In Table 4, canonical DC shows a performance drop, as the canonical 3D Gaussian alone cannot reflect the over/under reconstruction information at all timestamps for ...
- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** In Table 4, quaternion demonstrates an obvious performance drop, which proves the effectiveness of the 6D representation.
- **p. 6 / 4.2. Implementation Details - extractive PDF cue:** The learning rate of our network takes an exponential decay from 8e-4 to 1.6e-6 with the Adam optimizer.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Dataset (p. 6); 4.2. Implementation Details (p. 6); 4.3. Quantitative Results (p. 6); 4.4. Visualization Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.5. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | Compared with the results (dubbed as "PointNet feat." and "Plane feat.") in Table 4, it can be observed that our method achieves significant performance ... | p. 8 (4.5. Ablation Study) |
| 4.3. Quantitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | On average, our method significantly improves PSNR compared with static Gaussian, 3D-GS. | p. 7 (4.3. Quantitative Results) |
| 4.3. Quantitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | It can be observed that our method achieves good performance compared with other state-of-the-art methods. | p. 7 (4.3. Quantitative Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 2. The pipeline of our proposed 3D geometry-aware deformable Gaussian splitting. In the Gaussian canonical field, we reconstruct a static scene in canonical ... | p. 3 (Figure/Table caption) |
| 4.5. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | The best results are highlighted in bold. | p. 8 (4.5. Ablation Study) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Dataset - extractive PDF cue:** The synthetic dataset D-NeRF [37] contains 8 dynamic scenes, including Hell Warrior, Mutant, Hook, Bouncing Balls, Lego, T-Rex, Stand Up, and Jumping Jacks.
- **p. 6 / 4.1. Dataset - extractive PDF cue:** The real dataset proposed by HyperNeRF [34], including interp-cut-lemon, interp-cut-lemon1, vrigchicken, vrig-3dprinter, misc-split-cookie, and misc-splitcookie.
- **p. 7 / 4.3. Quantitative Results - extractive PDF cue:** We further compare our method with some highly related works on the real scene dataset proposed by [34].
- **p. 7 / 4.3. Quantitative Results - extractive PDF cue:** NeRF, TiNeuVox, NDVG, FDNeRF, and 4D-GS on the DNeRF Dataset.
- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** We conduct ablation studies on the synthetic dataset (800× 800) to verify the effectiveness of our proposed components.
- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** In Table 4, canonical DC shows a performance drop, as the canonical 3D Gaussian alone cannot reflect the over/under reconstruction information at all timestamps for ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Geometric information exploited by different meth- ods. a) Early dynamic NeRF methods such as DNeRF[37] directly encode the coordinate p of the sample ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. The pipeline of our proposed 3D geometry-aware deformable Gaussian splitting. In the Gaussian canonical field, we reconstruct a static scene in canonical space ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2. Given a set of images or monocular video of a dy- namic scene with frames with corresponding time labels and known camera intrinsic ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Our density control is designed for dynamic scenes. We control the densification of Gaussian distributions according to their transformed parameters at timestamp t ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative comparison between our method and competing methods on the D-NeRF dataset. The best results are highlighted in bold. Hell Warrior Mutant Hook ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Quantitative comparison between our method and competing methods on the HyperNeRF dataset.The best results are highlighted in bold. Chicken 3D Printer Broom Peel ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Quantitative comparison on HyperNeRF dataset: Aver- age on Cut Lemon, Chicken, 3D Printer, and Split Cookie. The best results are highlighted in bold.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative comparisons between baselines and our method on the synthetic dataset. NDVG Ours 3D-GS GT Chicken Printer Banana

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The synthetic dataset D-NeRF [37] contains 8 dynamic scenes, including Hell Warrior, Mutant, Hook, Bouncing Balls, Lego, T-Rex, Stand Up, and Jumping Jacks. | embodiment, simulator version and control stack | p. 6 (4.1. Dataset), p. 6 (4.1. Dataset) |
| Task/environment | The real dataset proposed by HyperNeRF [34], including interp-cut-lemon, interp-cut-lemon1, vrigchicken, vrig-3dprinter, misc-split-cookie, and misc-splitcookie. | reset, timeout, object/scene variation | p. 6 (4.1. Dataset), p. 7 (4.3. Quantitative Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.2. Gaussian Canonical Field), p. 3 (3. Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In Table 4, quaternion demonstrates an obvious performance drop, which proves the effectiveness of the 6D representation. | definition/direction/unit from same section | p. 8 (4.5. Ablation Study) |
| The learning rate of our network takes an exponential decay from 8e-4 to 1.6e-6 with the Adam optimizer. | definition/direction/unit from same section | p. 6 (4.2. Implementation Details) |
| Note that the color of the point cloud is generated by 3D coordinates. | definition/direction/unit from same section | p. 7 (4.4. Visualization Results) |
| The quantitative results can demonstrate the effectiveness of the proposed method in real scenes. | definition/direction/unit from same section | p. 7 (4.3. Quantitative Results) |
| To demonstrate the effectiveness of this design, we test our method with geometric branch blocks and leave others unchanged. | definition/direction/unit from same section | p. 8 (4.5. Ablation Study) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| It can be observed that our method achieves good performance compared with other state-of-the-art methods. | comparison identity and matched condition | p. 7 (4.3. Quantitative Results) |
| Qualitative comparisons between baselines and our method on the synthetic dataset. | comparison identity and matched condition | p. 7 (4.3. Quantitative Results) |
| We compare our method with recent state-of-the-art methods in the field, including 3D-GS, D8905 | comparison identity and matched condition | p. 6 (4.3. Quantitative Results) |
| Compared with the results (dubbed as "PointNet feat." and "Plane feat.") in Table 4, it can be observed that our method achieves significant performance ... | comparison identity and matched condition | p. 8 (4.5. Ablation Study) |
| Ablation studys in terms of average PSNR, SSIM, and LPIPS. | comparison identity and matched condition | p. 8 (4.5. Ablation Study) |
| Table 3. Quantitative comparison on HyperNeRF dataset: Aver- age on Cut Lemon, Chicken, 3D Printer, and Split Cookie. The best results are highlighted in ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conduct ablation studies on the synthetic dataset (800× 800) to verify the effectiveness of our proposed components. | component/input/data sensitivity | p. 8 (4.5. Ablation Study) |
| To study the effect of 6D representation of the rotation parameters of the 3D Gaussian, we conduct an experiment that replaces the 6D vector ... | component/input/data sensitivity | p. 8 (4.5. Ablation Study) |
| Figure 2. The pipeline of our proposed 3D geometry-aware deformable Gaussian splitting. In the Gaussian canonical field, we reconstruct a static scene in canonical ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |
| Fig. 2. Given a set of images or monocular video of a dy- namic scene with frames with corresponding time labels and known camera ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are summarized as: • We propose a geometry-aware feature extraction network based on 3D Gaussian distribution to better utilize local geometric ... | Compared with the results (dubbed as "PointNet feat." and "Plane feat.") in Table 4, it can be observed that our method achieves significant performance ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.5. Ablation Study), p. 7 (4.3. Quantitative Results), p. 7 (4.3. Quantitative Results), p. 3 (Figure/Table caption), p. 8 (4.5. Ablation Study) |
| Primary metric/result | On average, our method significantly improves PSNR compared with static Gaussian, 3D-GS. | numeric claim only at cited anchor | p. 7 (4.3. Quantitative Results) |

- Numeric sentences retained from the body:
- **p. 6 / 4.2. Implementation Details - extractive PDF cue:** Then 5 layers MLP with width 256 and skip connection is used for a decoder.
- **p. 6 / 4.2. Implementation Details - extractive PDF cue:** For the D-NeRF dataset, which does not provide point clouds, we randomly initialize 150000 points.
- **p. 6 / 4.2. Implementation Details - extractive PDF cue:** All the experiments are tested on a single RTX 4090 GPU.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We addressed the limitations of existing approaches from two perspectives: 1) we introduced 3D sparse convolution to extract local structural information effectively and efficiently ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Since 3D-DS cannot model dynamic scenes, the quality of the point cloud is poor. | p. 7 (4.4. Visualization Results) |
| body limitation/failure cue | Since it inherently cannot model the deformation of the dynamic scene, 3D-GS performs poorly in dynamic view synthesis. | p. 7 (4.3. Quantitative Results) |
| body limitation/failure cue | In Table 4, canonical DC shows a performance drop, as the canonical 3D Gaussian alone cannot reflect the over/under reconstruction information at all timestamps ... | p. 8 (4.5. Ablation Study) |
| body limitation/failure cue | For the D-NeRF dataset, which does not provide point clouds, we randomly initialize 150000 points. | p. 6 (4.2. Implementation Details) |
| body limitation/failure cue | Following previous works [21], we report three evaluation metrics, including Peak Signal-to-Noise Ratio (PSNR), Structural Similarity (SSIM), and Learned Perceptual Image Patch Similarity (LPIPS) ... | p. 6 (4.1. Dataset) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The learning rate of our network takes an exponential decay from 8e-4 to 1.6e-6 with the Adam optimizer. | p. 6 (4.2. Implementation Details) |
| The computational costs are: training time around 2h (avg. on D-NeRF dataset), render FPS 12 (fixed viewpoint), model size (34MB points cloud + 14MB ... | p. 7 (4.3. Quantitative Results) |
| Our implementation is based on 3D-GS [21]. | p. 6 (4.2. Implementation Details) |
| 3.3, we propose a 3D geometry-aware deformation field to learn transformations for given time steps, which transform our canonical 3D Gaussian distributions to corresponding ... | p. 3 (3. Method) |
| \ m ath bf {C}=\sum _{i=1}^N \mathbf {T}_i\alpha _i\mathbf {c}_i, (4) where αi represents the density of the Gaussian point computed by a Gaussian ... | p. 4 (3.1. Preliminary) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** We addressed the limitations of existing approaches from two perspectives: 1) we introduced 3D sparse convolution to extract local structural information effectively and efficiently for ...
- **p. 7 / 4.4. Visualization Results - extractive PDF cue:** Since 3D-DS cannot model dynamic scenes, the quality of the point cloud is poor.
- **p. 7 / 4.3. Quantitative Results - extractive PDF cue:** Since it inherently cannot model the deformation of the dynamic scene, 3D-GS performs poorly in dynamic view synthesis.
- **p. 8 / 4.5. Ablation Study - extractive PDF cue:** In Table 4, canonical DC shows a performance drop, as the canonical 3D Gaussian alone cannot reflect the over/under reconstruction information at all timestamps for ...
- **p. 6 / 4.2. Implementation Details - extractive PDF cue:** For the D-NeRF dataset, which does not provide point clouds, we randomly initialize 150000 points.
- **p. 6 / 4.1. Dataset - extractive PDF cue:** Following previous works [21], we report three evaluation metrics, including Peak Signal-to-Noise Ratio (PSNR), Structural Similarity (SSIM), and Learned Perceptual Image Patch Similarity (LPIPS) [66].

- **PDF anchors reviewed:** datasets p. 6 (4.1. Dataset), p. 6 (4.1. Dataset), p. 7 (4.3. Quantitative Results), p. 7 (4.3. Quantitative Results), p. 8 (4.5. Ablation Study), p. 8 (4.5. Ablation Study), metrics p. 8 (4.5. Ablation Study), p. 6 (4.2. Implementation Details), p. 7 (4.4. Visualization Results), p. 7 (4.3. Quantitative Results), p. 8 (4.5. Ablation Study), baselines p. 7 (4.3. Quantitative Results), p. 7 (4.3. Quantitative Results), p. 6 (4.3. Quantitative Results), p. 8 (4.5. Ablation Study), p. 8 (4.5. Ablation Study), p. 6 (Figure/Table caption), results p. 8 (4.5. Ablation Study), p. 7 (4.3. Quantitative Results), p. 7 (4.3. Quantitative Results), p. 3 (Figure/Table caption), p. 8 (4.5. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
