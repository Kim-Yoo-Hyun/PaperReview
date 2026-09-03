# Evaluation - SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reconstruction and High-Quality Mesh Rendering

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Guedon_SuGaR_Surface-Aligned_Gaussian_Splatting_for_Efficient_3D_Mesh_Reconstruction_and_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Guedon_SuGaR_Surface-Aligned_Gaussian_Splatting_for_Efficient_3D_Mesh_Reconstruction_and_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.2. Real-Time Rendering of Real Scenes), p. 7 (5.2. Real-Time Rendering of Real Scenes), p. 8 (5.4. Mesh Rendering Ablation), p. 8 (5.4. Mesh Rendering Ablation), p. 1 (Figure/Table caption)): Even though SuGaR focuses on aligning 3D Gaussians for reconstructing a high quality mesh during the first stage of its optimization, it significantly outperforms the state of the art methods ...

## Evaluation Body Digest

- **p. 7 / 5.2. Real-Time Rendering of Real Scenes - extractive body cue:** For evaluating our model, we follow the approach from the original 3D Gaussian Splatting paper [15] and compare the performance of several variations of our ...
- **p. 7 / 5.2. Real-Time Rendering of Real Scenes - extractive body cue:** Results on the Mip-NeRF360 dataset are given in Table 1.
- **p. 8 / 5.4. Mesh Rendering Ablation - extractive body cue:** Quantitative evaluation of rendering quality on the Mip-NeRF360 dataset [2].
- **p. 8 / 5.4. Mesh Rendering Ablation - extractive body cue:** Ablation for different mesh extraction methods on the Mip-NeRF360 dataset [2] after applying our regularization term.
- **p. 7 / 5.1. Implementation details - extractive body cue:** We perform Poisson reconstruction with depth 10 and apply mesh simplification using quadric error metrics [9] to decrease the resolution of the meshes.
- **p. 8 / 5.4. Mesh Rendering Ablation - extractive body cue:** Even though rendering with surface-aligned Gaussians provides better performance, rendering our meshes with traditional UV textures still produces satisfying results, which further illustrates the quality ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. Efficiently estimating ˆf(p) of the SDF of the sur- face generated from Gaussians. We render depth maps of the Gaussians, sample points p ...
- **p. 7 / 5.2. Real-Time Rendering of Real Scenes - extractive body cue:** Two main reasons explain this performance.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 7); 5.1. Implementation details (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Real-Time Rendering of Real Scenes | SYSTEM / EVALUATION SCOPE UNRESOLVED | Even though SuGaR focuses on aligning 3D Gaussians for reconstructing a high quality mesh during the first stage of its optimization, it significantly outperforms ... | p. 7 (5.2. Real-Time Rendering of Real Scenes) |
| 5.2. Real-Time Rendering of Real Scenes | SYSTEM / EVALUATION SCOPE UNRESOLVED | This performance is remarkable as SuGaR is able to extract a mesh significantly faster than other methods. | p. 7 (5.2. Real-Time Rendering of Real Scenes) |
| 5.4. Mesh Rendering Ablation | SYSTEM / EVALUATION SCOPE UNRESOLVED | Using 3D Gaussians bound to the mesh greatly improves rendering quality, even though it contains less parameters than the UV texture. | p. 8 (5.4. Mesh Rendering Ablation) |
| 5.4. Mesh Rendering Ablation | SYSTEM / EVALUATION SCOPE UNRESOLVED | Even though rendering with surface-aligned Gaussians provides better performance, rendering our meshes with traditional UV textures still produces satisfying results, which further illustrates the ... | p. 8 (5.4. Mesh Rendering Ablation) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 1. We introduce a method that extracts accurate and editable meshes from 3D Gaussian Splatting representations within minutes on a single GPU. The ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 5.2. Real-Time Rendering of Real Scenes - extractive body cue:** For evaluating our model, we follow the approach from the original 3D Gaussian Splatting paper [15] and compare the performance of several variations of our ...
- **p. 7 / 5.2. Real-Time Rendering of Real Scenes - extractive body cue:** Results on the Mip-NeRF360 dataset are given in Table 1.
- **p. 8 / 5.4. Mesh Rendering Ablation - extractive body cue:** Quantitative evaluation of rendering quality on the Mip-NeRF360 dataset [2].
- **p. 8 / 5.4. Mesh Rendering Ablation - extractive body cue:** Ablation for different mesh extraction methods on the Mip-NeRF360 dataset [2] after applying our regularization term.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We introduce a method that extracts accurate and editable meshes from 3D Gaussian Splatting representations within minutes on a single GPU. The meshes ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Our algorithm can extract a highly detailed mesh from any 3D Gaussian Splatting scene [15] within minutes on a single GPU (top: Renderings ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 3. Extracting a mesh from Gaussians. Without regular- ization, the Gaussians have no special arrangement after optimiza- tion, which makes extracting a mesh very ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Examples of (a) renderings and (b) reconstructed meshes with SuGaR. The (c) normal maps help visualize the geometry. nally be approximated by density ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. Efficiently estimating ˆf(p) of the SDF of the sur- face generated from Gaussians. We render depth maps of the Gaussians, sample points p ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. Sampling points on a level set for Poisson reconstruc- tion. Left: We sample points on the depth maps of the Gaussians and refine ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 7. Joint refinement of mesh and Gaussians. Left: We bind Gaussians to the triangles of the mesh. Depending on the number of triangles in ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1. Quantitative evaluation of rendering quality on the Mip-NeRF360 dataset [2]. SuGaR is best among the methods that recover a mesh, and still performs ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For evaluating our model, we follow the approach from the original 3D Gaussian Splatting paper [15] and compare the performance of several variations of ... | embodiment, simulator version and control stack | p. 7 (5.2. Real-Time Rendering of Real Scenes), p. 7 (5.2. Real-Time Rendering of Real Scenes) |
| Task/environment | Results on the Mip-NeRF360 dataset are given in Table 1. | reset, timeout, object/scene variation | p. 7 (5.2. Real-Time Rendering of Real Scenes), p. 8 (5.4. Mesh Rendering Ablation) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (4.1. Aligning the Gaussians with the Surface), p. 5 (4.1. Aligning the Gaussians with the Surface) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (4.2. Efficient Mesh Extraction), p. 6 (4.2. Efficient Mesh Extraction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We perform Poisson reconstruction with depth 10 and apply mesh simplification using quadric error metrics [9] to decrease the resolution of the meshes. | definition/direction/unit from same section | p. 7 (5.1. Implementation details) |
| Even though rendering with surface-aligned Gaussians provides better performance, rendering our meshes with traditional UV textures still produces satisfying results, which further illustrates the ... | definition/direction/unit from same section | p. 8 (5.4. Mesh Rendering Ablation) |
| Figure 5. Efficiently estimating ˆf(p) of the SDF of the sur- face generated from Gaussians. We render depth maps of the Gaussians, sample points ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Two main reasons explain this performance. | definition/direction/unit from same section | p. 7 (5.2. Real-Time Rendering of Real Scenes) |
| Then, we illustrate the benefits of using Gaussians aligned on the surface as a texturing tool for rendering meshes. | definition/direction/unit from same section | p. 8 (5.4. Mesh Rendering Ablation) |
| Figure 1. We introduce a method that extracts accurate and editable meshes from 3D Gaussian Splatting representations within minutes on a single GPU. The ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Moreover, SuGaR even reaches performance similar to state-of-the-art models for rendering quality [2, 15] on some of the scenes used for evaluation. | comparison identity and matched condition | p. 7 (5.2. Real-Time Rendering of Real Scenes) |
| We compare to several baselines, some of them focusing only on Novel View Synthesis [2, 15, 23, 41] and others relying on a reconstructed ... | comparison identity and matched condition | p. 7 (5.2. Real-Time Rendering of Real Scenes) |
| SuGaR is best among the methods that recover a mesh, and still performs well compared to NeRF methods and vanilla 3D Gaussian Splatting. | comparison identity and matched condition | p. 8 (5.4. Mesh Rendering Ablation) |
| Qualitative comparisons are provided in the supplementary material. | comparison identity and matched condition | p. 8 (5.4. Mesh Rendering Ablation) |
| Figure 6. Sampling points on a level set for Poisson reconstruc- tion. Left: We sample points on the depth maps of the Gaussians and ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 2. Our algorithm can extract a highly detailed mesh from any 3D Gaussian Splatting scene [15] within minutes on a single GPU (top: ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For all experiments except the ablation presented in Table 2, we extract the λ-level set of the density function for λ = 0.3. | component/input/data sensitivity | p. 7 (5.1. Implementation details) |
| For all scenes, we start by optimizing a Gaussian Splatting with no regularization for 7,000 iterations to let the 3D Gaussians position themselves without ... | component/input/data sensitivity | p. 7 (5.1. Implementation details) |
| Ablation for different mesh extraction methods on the Mip-NeRF360 dataset [2] after applying our regularization term. | component/input/data sensitivity | p. 8 (5.4. Mesh Rendering Ablation) |
| Figure 2. Our algorithm can extract a highly detailed mesh from any 3D Gaussian Splatting scene [15] within minutes on a single GPU (top: ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Figure 3. Extracting a mesh from Gaussians. Without regular- ization, the Gaussians have no special arrangement after optimiza- tion, which makes extracting a mesh ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Figure 6. Sampling points on a level set for Poisson reconstruc- tion. Left: We sample points on the depth maps of the Gaussians and ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present our SuGaR in this section: • First, we detail our loss term that enforces the alignment of the 3D Gaussians with the ... | Even though SuGaR focuses on aligning 3D Gaussians for reconstructing a high quality mesh during the first stage of its optimization, it significantly outperforms ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.2. Real-Time Rendering of Real Scenes), p. 7 (5.2. Real-Time Rendering of Real Scenes), p. 8 (5.4. Mesh Rendering Ablation), p. 8 (5.4. Mesh Rendering Ablation), p. 1 (Figure/Table caption) |
| Primary metric/result | This performance is remarkable as SuGaR is able to extract a mesh significantly faster than other methods. | numeric claim only at cited anchor | p. 7 (5.2. Real-Time Rendering of Real Scenes) |

- Numeric sentences retained from the body:
- **p. 7 / 5.2. Real-Time Rendering of Real Scenes - extractive body cue:** Following [15], we select the same sets of 2 scenes from Tanks&Temples (Truck and Train) and 2 scenes from DeepBlending (Playroom and Dr.
- **p. 7 / 5.2. Real-Time Rendering of Real Scenes - extractive body cue:** However, due to licensing issues and the unavailability of the scenes Flowers and Treehill, we perform the evaluation of all methods only on 7 scenes ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | SuGaR does not come without limitations: Gaussians do tend to "cheat" on the geometry and depth by creating cavities to reproduce specular effects, instead ... | p. 8 (6. Conclusion) |
| body limitation/failure cue | Figure 3. Extracting a mesh from Gaussians. Without regular- ization, the Gaussians have no special arrangement after optimiza- tion, which makes extracting a mesh ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Figure 6. Sampling points on a level set for Poisson reconstruc- tion. Left: We sample points on the depth maps of the Gaussians and ... | p. 6 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All our models are optimized on a single GPU Nvidia Tesla V100 SXM2 32 Go. | p. 7 (5.1. Implementation details) |
| We compute the standard metrics PSNR, SSIM and LPIPS [44] to evaluate the quality of SuGaR's rendering using our extracted meshes and their bound ... | p. 7 (5.2. Real-Time Rendering of Real Scenes) |
| By minimizing the difference between this SDF and the actual SDF computed for the Gaussians, we encourage the Gaussians to have these properties. | p. 4 (4.1. Aligning the Gaussians with the Surface) |
| For a given Gaussian Splatting scene, we start by considering the corresponding density function d : R3 →R+, computed as the sum of the ... | p. 4 (4.1. Aligning the Gaussians with the Surface) |
| Since a zero-level set is entirely determined by an unsigned distance function, we actually do not need to compute the sign of the SDFs ... | p. 5 (4.1. Aligning the Gaussians with the Surface) |
| Then, we compute the density values di = d(p + tiv) from Eq. | p. 6 (4.2. Efficient Mesh Extraction) |
| (10), we sample 3D points on a level set of the density computed from the Gaussians. | p. 6 (4.2. Efficient Mesh Extraction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive body cue:** SuGaR does not come without limitations: Gaussians do tend to "cheat" on the geometry and depth by creating cavities to reproduce specular effects, instead of ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 3. Extracting a mesh from Gaussians. Without regular- ization, the Gaussians have no special arrangement after optimiza- tion, which makes extracting a mesh very ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. Sampling points on a level set for Poisson reconstruc- tion. Left: We sample points on the depth maps of the Gaussians and refine ...

- **Evidence anchors reviewed:** datasets p. 7 (5.2. Real-Time Rendering of Real Scenes), p. 7 (5.2. Real-Time Rendering of Real Scenes), p. 8 (5.4. Mesh Rendering Ablation), p. 8 (5.4. Mesh Rendering Ablation), metrics p. 7 (5.1. Implementation details), p. 8 (5.4. Mesh Rendering Ablation), p. 5 (Figure/Table caption), p. 7 (5.2. Real-Time Rendering of Real Scenes), p. 8 (5.4. Mesh Rendering Ablation), p. 1 (Figure/Table caption), baselines p. 7 (5.2. Real-Time Rendering of Real Scenes), p. 7 (5.2. Real-Time Rendering of Real Scenes), p. 8 (5.4. Mesh Rendering Ablation), p. 8 (5.4. Mesh Rendering Ablation), p. 6 (Figure/Table caption), p. 2 (Figure/Table caption), results p. 7 (5.2. Real-Time Rendering of Real Scenes), p. 7 (5.2. Real-Time Rendering of Real Scenes), p. 8 (5.4. Mesh Rendering Ablation), p. 8 (5.4. Mesh Rendering Ablation), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
