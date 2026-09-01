# Evaluation - Robust and Efficient 3D Gaussian Splatting for Urban Scene Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Yuan_Robust_and_Efficient_3D_Gaussian_Splatting_for_Urban_Scene_Reconstruction_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Yuan_Robust_and_Efficient_3D_Gaussian_Splatting_for_Urban_Scene_Reconstruction_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.4. Ablation Study), p. 6 (4.2. Results), p. 6 (4.2. Results), p. 7 (4.3. LOD Generation), p. 8 (4.4. Ablation Study), p. 4 (Figure/Table caption)): This model significantly improves all three quality metrics across all scenes.

## Evaluation Body Digest

- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Notably, we also conducted validation using Building scene from Mega-NeRF [42] as well as Residences, Sci-Art and Campus scenes from UrbanScene3D [17], with results provided ...
- **p. 7 / 4.3. LOD Generation - extractive PDF cue:** Quantitative results on three large scene datasets.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** We use three detail levels for these scenes.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** This model significantly improves all three quality metrics across all scenes.
- **p. 7 / 4.3. LOD Generation - extractive PDF cue:** However, increasing B to beyond a certain threshold does not necessarily improve quality, because B only imposes an upper limit, and the scene may not ...
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Scene Rubble JNU-ZH BigCity w/o vis.
- **p. 6 / 4.2. Results - extractive PDF cue:** The only exception is the Rubble scene, where the LPIPS score matches that of CityGaussian.
- **p. 6 / 4.2. Results - extractive PDF cue:** This underscores our method's ability to achieve high-fidelity reconstructions of urban-scale scenes.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experimental Setup (p. 6); 4.2. Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | This model significantly improves all three quality metrics across all scenes. | p. 8 (4.4. Ablation Study) |
| 4.2. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | This underscores our method's ability to achieve high-fidelity reconstructions of urban-scale scenes. | p. 6 (4.2. Results) |
| 4.2. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | For quality-related metrics (SSIM, PSNR, and LPIPS), the results indicate that our method outperforms others. | p. 6 (4.2. Results) |
| 4.3. LOD Generation | EMPIRICAL / SOURCE-REPORTED EVALUATION | However, increasing B to beyond a certain threshold does not necessarily improve quality, because B only imposes an upper limit, and the scene may ... | p. 7 (4.3. LOD Generation) |
| 4.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | The component effectively reduces camera redundancy. ble 4, our camera selection strategy can significantly reduce redundant cameras, thus achieving better results under the same ... | p. 8 (4.4. Ablation Study) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** Notably, we also conducted validation using Building scene from Mega-NeRF [42] as well as Residences, Sci-Art and Campus scenes from UrbanScene3D [17], with results provided ...
- **p. 7 / 4.3. LOD Generation - extractive PDF cue:** Quantitative results on three large scene datasets.
- **p. 6 / 4.1. Experimental Setup - extractive PDF cue:** We use three detail levels for these scenes.
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** This model significantly improves all three quality metrics across all scenes.
- **p. 7 / 4.3. LOD Generation - extractive PDF cue:** However, increasing B to beyond a certain threshold does not necessarily improve quality, because B only imposes an upper limit, and the scene may not ...
- **p. 8 / 4.4. Ablation Study - extractive PDF cue:** Scene Rubble JNU-ZH BigCity w/o vis.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 1. The process of scene and data division. (a) Obtain the 3D point cloud and its corresponding 2D feature points through estimating camera poses ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. In-partition prioritized densification. The red rectan- gle is the partition bounding box, and points represent Gaussians. Point colors indicate gradient thresholds. 𝐵1,ܶ 1, ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Controllable LOD generation and detail level selec- tion. (a) During training, detail levels are progressively generated in a bottom-up manner, guided by resource ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Illustration of the appearance transform. For each image and 3D Gaussian, ℓ(G) represents the Gaussian embedding and ℓ(I) represents the image embedding, respectively. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative results on three large scene datasets. We report SSIM↑, PSNR↑, LPIPS↓, the number of Gaussians (#G, in 106)↓ and FPS↑on test views. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Visualization results. All methods (excluding 3DGS) render in LOD mode. Ours demonstrates better detail preservation and fewer artifacts. ity. However, increasing B to ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Quantitative evaluation of budget B for detail level generation. Adjusting the budget effectively controls resource consumption, but also impacts the quality.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 6. Visualization results of ablation study. Our proposed components effectively suppress the artifacts. eras are assigmend to partitions solely based on spatial lo- cations. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Notably, we also conducted validation using Building scene from Mega-NeRF [42] as well as Residences, Sci-Art and Campus scenes from UrbanScene3D [17], with results ... | embodiment, simulator version and control stack | p. 6 (4.1. Experimental Setup), p. 7 (4.3. LOD Generation) |
| Task/environment | Quantitative results on three large scene datasets. | reset, timeout, object/scene variation | p. 7 (4.3. LOD Generation), p. 6 (4.1. Experimental Setup) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.2.1. Point-based Visibility), p. 4 (3.4. Controllable Level-of-detail) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.5. Quality Enhancements), p. 5 (3.5.1. Appearance Transform Module) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The only exception is the Rubble scene, where the LPIPS score matches that of CityGaussian. | definition/direction/unit from same section | p. 6 (4.2. Results) |
| This underscores our method's ability to achieve high-fidelity reconstructions of urban-scale scenes. | definition/direction/unit from same section | p. 6 (4.2. Results) |
| Ours demonstrates better detail preservation and fewer artifacts. ity. | definition/direction/unit from same section | p. 7 (4.3. LOD Generation) |
| However, as illustrated in Table 5, it markedly accelerates the training process. | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| The 2nd row of Table 3 demonstrates the effect of omitting the appearance transform model. | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| Figure 3. Controllable LOD generation and detail level selec- tion. (a) During training, detail levels are progressively generated in a bottom-up manner, guided by ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to other LOD-enabled methods, our method consistently outperforms previous approaches across all three quality-related metrics. | comparison identity and matched condition | p. 6 (4.2. Results) |
| For quality-related metrics (SSIM, PSNR, and LPIPS), the results indicate that our method outperforms others. | comparison identity and matched condition | p. 6 (4.2. Results) |
| Visualization results of ablation study. | comparison identity and matched condition | p. 7 (4.4. Ablation Study) |
| We conduct ablation experiments to evaluate the impact of different components of our proposed method. | comparison identity and matched condition | p. 7 (4.4. Ablation Study) |
| But without it will lead to severe artifacts, as shown in Figure 6c. | comparison identity and matched condition | p. 8 (4.4. Ablation Study) |
| The 3rd row of Table 3 presents the results without depth regularization. | comparison identity and matched condition | p. 8 (4.4. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 6. Visualization results of ablation study. Our proposed components effectively suppress the artifacts. eras are assigmend to partitions solely based on spatial lo- ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| We conduct ablation experiments to evaluate the impact of different components of our proposed method. | component/input/data sensitivity | p. 7 (4.4. Ablation Study) |
| The 2nd row of Table 3 demonstrates the effect of omitting the appearance transform model. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| The first section of the table compares our method, with the LOD mode disabled, against other methods without LOD mode or with it disabled. | component/input/data sensitivity | p. 6 (4.2. Results) |
| By comparing the results of our method with and without LOD mode, it becomes evident that the number of Gaussians is significantly reduced, leading ... | component/input/data sensitivity | p. 6 (4.2. Results) |
| But without it will lead to severe artifacts, as shown in Figure 6c. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contributions are summarized as follows: • We propose a novel visibility-based data division strategy and in-partition prioritized densification method, to achieve efficient ... | This model significantly improves all three quality metrics across all scenes. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.4. Ablation Study), p. 6 (4.2. Results), p. 6 (4.2. Results), p. 7 (4.3. LOD Generation), p. 8 (4.4. Ablation Study), p. 4 (Figure/Table caption) |
| Primary metric/result | This underscores our method's ability to achieve high-fidelity reconstructions of urban-scale scenes. | numeric claim only at cited anchor | p. 6 (4.2. Results) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Future work could explore incremental switching mechanisms for smoother transitions and improved resource efficiency. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Enhancing robustness to pose inaccuracies is thus an important future direction. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Meanwhile, the FPS does not experience a significant decline and consistently ranks as either the best or second-best, making real-time rendering entirely feasible. | p. 6 (4.2. Results) |
| body limitation/failure cue | However, increasing B to beyond a certain threshold does not necessarily improve quality, because B only imposes an upper limit, and the scene may ... | p. 7 (4.3. LOD Generation) |
| body limitation/failure cue | Meanwhile, the quality experiences only minimal degradation. | p. 6 (4.2. Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Impact of in-partition prioritized densification on training time and the number of Gaussians. | p. 8 (4.4. Ablation Study) |
| All methods were evaluated using a single NVIDIA A100-80G GPU. | p. 6 (4.1. Experimental Setup) |
| Notably, other methods exhibit a lower #G in the BigCity scene, mainly due to our adjustment of their hyperparameters to ensure execution within 80 ... | p. 6 (4.2. Results) |
| As described in [8], the loss function of 3DGS includes the L1 and D-SSIM metrics, computed between the rendered image ˆI and its corresponding ... | p. 3 (3.1. Preliminary) |
| For an unselected image Ii, the 3D point cloud of the scene is projected onto its image plane, and compute its convex hull area ... | p. 3 (3.2.1. Point-based Visibility) |
| This process is entirely end-to-end, eliminating the need for extensive post-processing steps common in compression strategy. | p. 4 (3.4.1. Controllable Detail Level Generation) |
| For the i-th level, upon completion of training, a checkpoint is created, and the budget, interval and downsample factor are changed to Bi+1, Ti+1 ... | p. 4 (3.4.1. Controllable Detail Level Generation) |
| Since normalized embeddings are used, cosine similarity is adopted to compute the loss: Lsim i,j = wi,j | p. 5 (3.5.1. Appearance Transform Module) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** Future work could explore incremental switching mechanisms for smoother transitions and improved resource efficiency.
- **p. 8 / 5. Conclusion - extractive PDF cue:** Enhancing robustness to pose inaccuracies is thus an important future direction.
- **p. 6 / 4.2. Results - extractive PDF cue:** Meanwhile, the FPS does not experience a significant decline and consistently ranks as either the best or second-best, making real-time rendering entirely feasible.
- **p. 7 / 4.3. LOD Generation - extractive PDF cue:** However, increasing B to beyond a certain threshold does not necessarily improve quality, because B only imposes an upper limit, and the scene may not ...
- **p. 6 / 4.2. Results - extractive PDF cue:** Meanwhile, the quality experiences only minimal degradation.

- **PDF anchors reviewed:** datasets p. 6 (4.1. Experimental Setup), p. 7 (4.3. LOD Generation), p. 6 (4.1. Experimental Setup), p. 8 (4.4. Ablation Study), p. 7 (4.3. LOD Generation), p. 8 (4.4. Ablation Study), metrics p. 6 (4.2. Results), p. 6 (4.2. Results), p. 7 (4.3. LOD Generation), p. 8 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), p. 4 (Figure/Table caption), baselines p. 6 (4.2. Results), p. 6 (4.2. Results), p. 7 (4.4. Ablation Study), p. 7 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), results p. 8 (4.4. Ablation Study), p. 6 (4.2. Results), p. 6 (4.2. Results), p. 7 (4.3. LOD Generation), p. 8 (4.4. Ablation Study), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
