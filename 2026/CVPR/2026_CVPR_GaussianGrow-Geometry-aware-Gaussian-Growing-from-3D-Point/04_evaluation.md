# Evaluation - GaussianGrow: Geometry-aware Gaussian Growing from 3D Point Clouds with Text Guidance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_GaussianGrow_Geometry-aware_Gaussian_Growing_from_3D_Point_Clouds_with_Text_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_GaussianGrow_Geometry-aware_Gaussian_Growing_from_3D_Point_Clouds_with_Text_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. Text-to-3D Generation), p. 7 (4.2. Text-to-3D Generation), p. 6 (4. Experiments), p. 6 (4.1. Text-Guided Visual Synthesis), p. 8 (4.4. Ablation Study), p. 8 (4.4. Ablation Study)): Moreover, applying the geometry of LGM to GaussianGrow also achieves significantly better performance by replacing the appearance of LGM with GaussianGrow.

## Evaluation Body Digest

- **p. 7 / 4.3. Point to Gaussian Generation - extractive body cue:** To demonstrate robustness with real-world data, we also utilized the DeepFashion3D dataset 18974
- **p. 7 / 4.2. Text-to-3D Generation - extractive body cue:** For quantitative evaluation, we conduct comprehensive experiments on the T3Bench benchmark [11], which provides a diverse collection of text prompts covering various object categories and ...
- **p. 6 / 4. Experiments - extractive body cue:** Quantitative comparison on the Objaverse dataset.
- **p. 6 / 4.1. Text-Guided Visual Synthesis - extractive body cue:** We benchmark GaussianGrow against state-of-the-art text-guided 3D appearance generation methods, including Texture [38], Text2Tex [5], Paint3D [57], SyncMVD [25] and GAP [61].
- **p. 8 / 4.3. Point to Gaussian Generation - extractive body cue:** We benchmark GaussianGrow against two leading methods: DreamGaussian [44] and TriplaneGaussian [68].
- **p. 8 / 4.3. Point to Gaussian Generation - extractive body cue:** Visual comparison with DreamGaussian and TriplaneGaussian on the task of Point-to-Gaussian.
- **p. 6 / 4.1. Text-Guided Visual Synthesis - extractive body cue:** For quantitative evaluation, we employ three complementary metrics: Fr´echet Inception Distance (FID) [19] and Kernel Inception Distance (KID ×10-3) [3] to assess image quality, while ...
- **p. 7 / 4.2. Text-to-3D Generation - extractive body cue:** We measure performance using three complementary metrics: CLIP similarity for semantic alignment, CLIP R-Precision for textimage correspondence, and ImageReward [36, 51] for perceptual quality assessment.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Text-to-3D Generation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Moreover, applying the geometry of LGM to GaussianGrow also achieves significantly better performance by replacing the appearance of LGM with GaussianGrow. | p. 7 (4.2. Text-to-3D Generation) |
| 4.2. Text-to-3D Generation | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results demonstrate that GaussianGrow significantly outperforms previous methods in terms of appearance generation, and a stronger geometric setting leads to better generation quality. | p. 7 (4.2. Text-to-3D Generation) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | In this section, we present a comprehensive evaluation of GaussianGrow's performance across multiple scenarios. | p. 6 (4. Experiments) |
| 4.1. Text-Guided Visual Synthesis | EMPIRICAL / REAL-ROBOT OR HARDWARE | For quantitative evaluation, we employ three complementary metrics: Fr´echet Inception Distance (FID) [19] and Kernel Inception Distance (KID ×10-3) [3] to assess image quality, ... | p. 6 (4.1. Text-Guided Visual Synthesis) |
| 4.4. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | Ablation results for key components of GaussianGrow. | p. 8 (4.4. Ablation Study) |

## Dataset / Benchmark Role

- **p. 7 / 4.3. Point to Gaussian Generation - extractive body cue:** To demonstrate robustness with real-world data, we also utilized the DeepFashion3D dataset 18974
- **p. 7 / 4.2. Text-to-3D Generation - extractive body cue:** For quantitative evaluation, we conduct comprehensive experiments on the T3Bench benchmark [11], which provides a diverse collection of text prompts covering various object categories and ...
- **p. 6 / 4. Experiments - extractive body cue:** Quantitative comparison on the Objaverse dataset.
- **p. 6 / 4.1. Text-Guided Visual Synthesis - extractive body cue:** We benchmark GaussianGrow against state-of-the-art text-guided 3D appearance generation methods, including Texture [38], Text2Tex [5], Paint3D [57], SyncMVD [25] and GAP [61].
- **p. 8 / 4.3. Point to Gaussian Generation - extractive body cue:** We benchmark GaussianGrow against two leading methods: DreamGaussian [44] and TriplaneGaussian [68].
- **p. 8 / 4.3. Point to Gaussian Generation - extractive body cue:** Visual comparison with DreamGaussian and TriplaneGaussian on the task of Point-to-Gaussian.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Left: Diverse shapes generated by GaussianGrow. Right: The Gaussian generation pipeline of GaussianGrow. Reference point clouds can be obtained through large-scale retrieval or ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of GaussianGrow. Stage 1. We leverage depth-aware ControlNet for primary view generation, with a geometry- aware diffusion model for multi-view synthesis. Additional ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. We obtain the additional camera poses by optimizing them to observe largest overlap regions. Gaussian Optimization. Our optimization strategy follows a two-phase approach ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. The effect of Gaussian inpainting. Before Overlap Processing After Overlap Processing
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. The effectiveness of processing overlap regions. certain regions may remain unseen or inadequately cap- tured. Due to the diverse geometric structures of different ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. Visual comparison on the Objaverse dataset shows that GaussianGrow uses point clouds instead of meshes. the depth map Di rendered from vi, the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Spatial Inpainting. Due to noises and uneven density in the raw point cloud data, some points may remain difficult to observe after image ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparison on the Objaverse dataset.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To demonstrate robustness with real-world data, we also utilized the DeepFashion3D dataset 18974 | embodiment, simulator version and control stack | p. 7 (4.3. Point to Gaussian Generation), p. 7 (4.2. Text-to-3D Generation) |
| Task/environment | For quantitative evaluation, we conduct comprehensive experiments on the T3Bench benchmark [11], which provides a diverse collection of text prompts covering various object categories ... | reset, timeout, object/scene variation | p. 7 (4.2. Text-to-3D Generation), p. 6 (4. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.2. Appearance Generation), p. 3 (3.1. Preliminary Preparation) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (3.3. Iterative Inpainting and Refinement), p. 3 (3. Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For quantitative evaluation, we employ three complementary metrics: Fr´echet Inception Distance (FID) [19] and Kernel Inception Distance (KID ×10-3) [3] to assess image quality, ... | definition/direction/unit from same section | p. 6 (4.1. Text-Guided Visual Synthesis) |
| We measure performance using three complementary metrics: CLIP similarity for semantic alignment, CLIP R-Precision for textimage correspondence, and ImageReward [36, 51] for perceptual quality ... | definition/direction/unit from same section | p. 7 (4.2. Text-to-3D Generation) |
| Ours + Uni3D Ours + LGM DiffSplat [21] GVGEN [10] LN3Diff [20] DIRECT-3D [24] 3DTopia [13] LGM [42] GRM [53] ↑CLIP Sim.% 31.55 30.17 ... | definition/direction/unit from same section | p. 7 (4.1. Text-Guided Visual Synthesis) |
| 9, the same point cloud processed with different textual descriptions produces distinct visual styles while maintaining geometric accuracy. | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| Unlike most of these methods, which rely on UV-mapped meshes, GaussianGrow operates directly on point clouds. | definition/direction/unit from same section | p. 6 (4.1. Text-Guided Visual Synthesis) |
| 4 shows that the removal of our image-level inpainting strategy leaves complex regions incomplete. | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| Figure 1. Left: Diverse shapes generated by GaussianGrow. Right: The Gaussian generation pipeline of GaussianGrow. Reference point clouds can be obtained through large-scale retrieval ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Overview of GaussianGrow. Stage 1. We leverage depth-aware ControlNet for primary view generation, with a geometry- aware diffusion model for multi-view synthesis. ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The retrieve-based GaussianGrow "Ours+Uni3D" achieves the best performance across all evaluation metrics, while the generative-based version "Ours+LGM" also achieves comparable performance compared to the ... | comparison identity and matched condition | p. 7 (4.2. Text-to-3D Generation) |
| Ours + Uni3D Ours + LGM DiffSplat [21] GVGEN [10] LN3Diff [20] DIRECT-3D [24] 3DTopia [13] LGM [42] GRM [53] ↑CLIP Sim.% 31.55 30.17 ... | comparison identity and matched condition | p. 7 (4.1. Text-Guided Visual Synthesis) |
| 8, our visual comparisons highlight that GaussianGrow delivers noticeably better visual quality and geometric fidelity than baseline methods. | comparison identity and matched condition | p. 8 (4.3. Point to Gaussian Generation) |
| We benchmark GaussianGrow against state-of-the-art text-guided 3D appearance generation methods, including Texture [38], Text2Tex [5], Paint3D [57], SyncMVD [25] and GAP [61]. | comparison identity and matched condition | p. 6 (4.1. Text-Guided Visual Synthesis) |
| Each baseline required specific adaptations for our experiments. | comparison identity and matched condition | p. 8 (4.3. Point to Gaussian Generation) |
| Quantitative comparison on the Objaverse dataset. | comparison identity and matched condition | p. 6 (4. Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation results for key components of GaussianGrow. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| We evaluate our key components through ablation experiments. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| Finally, we validate our design choices through detailed ablation studies in Sec. | component/input/data sensitivity | p. 6 (4. Experiments) |
| Unlike many competing approaches that require complete mesh representations, GaussianGrow operates directly on point cloud inputs, without additional geometric information. | component/input/data sensitivity | p. 6 (4.1. Text-Guided Visual Synthesis) |
| Figure 4. The effect of Gaussian inpainting. Before Overlap Processing After Overlap Processing | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Figure 2. Overview of GaussianGrow. Stage 1. We leverage depth-aware ControlNet for primary view generation, with a geometry- aware diffusion model for multi-view synthesis. ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions can be summarized as follows: • We propose GaussianGrow, a novel approach that generates 3D Gaussians by learning to grow them from ... | Moreover, applying the geometry of LGM to GaussianGrow also achieves significantly better performance by replacing the appearance of LGM with GaussianGrow. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. Text-to-3D Generation), p. 7 (4.2. Text-to-3D Generation), p. 6 (4. Experiments), p. 6 (4.1. Text-Guided Visual Synthesis), p. 8 (4.4. Ablation Study), p. 8 (4.4. Ablation Study) |
| Primary metric/result | The results demonstrate that GaussianGrow significantly outperforms previous methods in terms of appearance generation, and a stronger geometric setting leads to better generation quality. | numeric claim only at cited anchor | p. 7 (4.2. Text-to-3D Generation) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 4. Spatial Inpainting. Due to noises and uneven density in the raw point cloud data, some points may remain difficult to observe after ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | To demonstrate robustness with real-world data, we also utilized the DeepFashion3D dataset 18974 | p. 7 (4.3. Point to Gaussian Generation) |
| body limitation/failure cue | These scans present challenging characteristics including noise and varying point densities. | p. 8 (4.3. Point to Gaussian Generation) |
| body limitation/failure cue | 4, using only the six cardinal views leads to clear degradation across all metrics, while adding four views focused on key overlap regions yields ... | p. 8 (4.4. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| TriplaneGaussian was adapted by bypassing its point cloud decoder for direct point-to-Gaussian conversion and integrating Stable Diffusion for text guidance. | p. 8 (4.3. Point to Gaussian Generation) |
| We compute normals N = {ni}N i=1 through gradient prediction: ni = ∇fu(pi) ∥∇fu(pi)∥. | p. 3 (3.1. Preliminary Preparation) |
| To extract comprehensive geometric information from the input point cloud, we compute three geometric representation maps: depth, normal, and position maps, each serving a ... | p. 3 (3.1. Preliminary Preparation) |
| We contribute a CUDA-based parallel implementation for speeding up this process, reducing computation time from minutes to seconds. | p. 4 (3.2. Appearance Generation) |
| This targeted approach ensures that the well-optimized Gaussians are not affected at the optimization steps where they are not visible. | p. 5 (3.2. Appearance Generation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Spatial Inpainting. Due to noises and uneven density in the raw point cloud data, some points may remain difficult to observe after image ...
- **p. 7 / 4.3. Point to Gaussian Generation - extractive body cue:** To demonstrate robustness with real-world data, we also utilized the DeepFashion3D dataset 18974
- **p. 8 / 4.3. Point to Gaussian Generation - extractive body cue:** These scans present challenging characteristics including noise and varying point densities.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** 4, using only the six cardinal views leads to clear degradation across all metrics, while adding four views focused on key overlap regions yields the ...

- **Evidence anchors reviewed:** datasets p. 7 (4.3. Point to Gaussian Generation), p. 7 (4.2. Text-to-3D Generation), p. 6 (4. Experiments), p. 6 (4.1. Text-Guided Visual Synthesis), p. 8 (4.3. Point to Gaussian Generation), p. 8 (4.3. Point to Gaussian Generation), metrics p. 6 (4.1. Text-Guided Visual Synthesis), p. 7 (4.2. Text-to-3D Generation), p. 7 (4.1. Text-Guided Visual Synthesis), p. 8 (4.4. Ablation Study), p. 6 (4.1. Text-Guided Visual Synthesis), p. 8 (4.4. Ablation Study), baselines p. 7 (4.2. Text-to-3D Generation), p. 7 (4.1. Text-Guided Visual Synthesis), p. 8 (4.3. Point to Gaussian Generation), p. 6 (4.1. Text-Guided Visual Synthesis), p. 8 (4.3. Point to Gaussian Generation), p. 6 (4. Experiments), results p. 7 (4.2. Text-to-3D Generation), p. 7 (4.2. Text-to-3D Generation), p. 6 (4. Experiments), p. 6 (4.1. Text-Guided Visual Synthesis), p. 8 (4.4. Ablation Study), p. 8 (4.4. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
