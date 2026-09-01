# Evaluation - Affine-Equivariant Kernel Space Encoding for NeRF Editing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=fAj3MJghc0; PDF retrieval source: https://openreview.net/pdf/048e4b5756022f2faa8898f0f2d379b85079ab58.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5. Experiments), p. 6 (5. Experiments), p. 7 (5. Experiments), p. 8 (5. Experiments), p. 7 (5. Experiments), p. 5 (Figure/Table caption)): These baselines are selected to demonstrate that EKS not only achieves reconstruction quality comparable to or exceeding SOTA methods, while enabling editing with significantly fewer artifacts.

## Evaluation Body Digest

- **p. 6 / 5. Experiments - extractive PDF cue:** Additionally to synthetic data we trained our NeRF model trained on the Mip-NeRF 360 dataset (Barron et al., 2022), comprising five outdoor and four indoor ...
- **p. 7 / 5. Experiments - extractive PDF cue:** These experiments span both synthetic and real-world datasets and include diverse physical phenomena such as rigid body dynamics, soft body deformation, and cloth simulation.
- **p. 6 / 5. Experiments - extractive PDF cue:** Example edits on real-world scenes.
- **p. 7 / 5. Experiments - extractive PDF cue:** Quantitative comparisons (PSNR) on a NeRF-Synthetic dataset showing that EKS gives comparable results with other models on static scenes.
- **p. 8 / 5. Experiments - extractive PDF cue:** Ablation study of EKS reporting PSNR for static reconstruction and edited scenes.
- **p. 8 / 5. Experiments - extractive PDF cue:** Physics simulations with Gaussian Splatting methods.
- **p. 6 / 5. Experiments - extractive PDF cue:** This demonstrates that our approach preserves rendering quality while enabling scene edits.
- **p. 6 / 5. Experiments - extractive PDF cue:** We design our experiments to demonstrate that EKS maintains the reconstruction quality of state-of-the-art (SOTA) methods while enabling complex object modifications.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | These baselines are selected to demonstrate that EKS not only achieves reconstruction quality comparable to or exceeding SOTA methods, while enabling editing with significantly ... | p. 6 (5. Experiments) |
| 5. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | For static scene reconstruction, EKS achieves quality comparable to state-of-the-art editable methods, and in some cases provides the best results among methods that support ... | p. 6 (5. Experiments) |
| 5. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Quantitative comparisons (PSNR) on a (Chen et al., 2023) benchmark showing that EKS achieves best results in editing task. | p. 7 (5. Experiments) |
| 5. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | For static reconstruction, all variants achieve comparable performance, with only minor PSNR differences as shown in Table 3. | p. 8 (5. Experiments) |
| 5. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 2, our method consistently outperforms prior stateof-the-art approaches, including GaMeS, a purely Gaussian Splatting-based editing method. | p. 7 (5. Experiments) |

## Dataset / Benchmark Role

- **p. 6 / 5. Experiments - extractive PDF cue:** Additionally to synthetic data we trained our NeRF model trained on the Mip-NeRF 360 dataset (Barron et al., 2022), comprising five outdoor and four indoor ...
- **p. 7 / 5. Experiments - extractive PDF cue:** These experiments span both synthetic and real-world datasets and include diverse physical phenomena such as rigid body dynamics, soft body deformation, and cloth simulation.
- **p. 6 / 5. Experiments - extractive PDF cue:** Example edits on real-world scenes.
- **p. 7 / 5. Experiments - extractive PDF cue:** Quantitative comparisons (PSNR) on a NeRF-Synthetic dataset showing that EKS gives comparable results with other models on static scenes.
- **p. 8 / 5. Experiments - extractive PDF cue:** Ablation study of EKS reporting PSNR for static reconstruction and edited scenes.
- **p. 8 / 5. Experiments - extractive PDF cue:** Physics simulations with Gaussian Splatting methods.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. EKS overview. EKS represents positional features using spatially localized anisotropic Gaussian kernels, enabling stable and fine-grained interactive editing while maintaining the high-fidelity rendering ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Physical simulations. From left to right: (1) Rigid body simulation of falling leaves. (2) Soft body simulation of the Lego dozer being squished. ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. Evolution of two physical simulations. From left to right: (1) A rubber duck falling onto a pillow and deforming it. (2) A pirate ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Model overview. Top: During training, a subset of Gaussians is selected using Ray-Traced Gaussian Proximity Search (RT-GPS), which also handles pruning. The nearest ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. KNN Comparisons. Comparison of neighbourhood changes under deformation using Euclidean distance KNN (top) versus our proposed Mahalanobis distance KNN (bottom). Mov- ing points ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 6. The RT-GPS working principle. A light ray passing through the scene is illustrated, along with its intersections with the icosahedrons. The figure highlights ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 7. Example edits on real-world scenes. From left to right: (1) Physics-based simulation, showing an object falling onto a tilted table and bouncing off. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative comparisons (PSNR) on a NeRF-Synthetic dataset showing that EKS gives comparable results with other models on static scenes. For edited scene reconstruction, ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Additionally to synthetic data we trained our NeRF model trained on the Mip-NeRF 360 dataset (Barron et al., 2022), comprising five outdoor and four ... | embodiment, simulator version and control stack | p. 6 (5. Experiments), p. 7 (5. Experiments) |
| Task/environment | These experiments span both synthetic and real-world datasets and include diverse physical phenomena such as rigid body dynamics, soft body deformation, and cloth simulation. | reset, timeout, object/scene variation | p. 7 (5. Experiments), p. 6 (5. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (4. Proposed Method), p. 4 (3. Preliminary) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3. Preliminary), p. 5 (4. Proposed Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| This demonstrates that our approach preserves rendering quality while enabling scene edits. | definition/direction/unit from same section | p. 6 (5. Experiments) |
| We design our experiments to demonstrate that EKS maintains the reconstruction quality of state-of-the-art (SOTA) methods while enabling complex object modifications. | definition/direction/unit from same section | p. 6 (5. Experiments) |
| The results of these simulations are illustrated in Figs 3, 2, 7, and 9. | definition/direction/unit from same section | p. 7 (5. Experiments) |
| These visualizations demonstrate that EKS produces realistic and physically plausible edits across a wide range of scenarios. | definition/direction/unit from same section | p. 7 (5. Experiments) |
| For static reconstruction, all variants achieve comparable performance, with only minor PSNR differences as shown in Table 3. | definition/direction/unit from same section | p. 8 (5. Experiments) |
| Removing view-direction restoration leads to the largest performance drop, as the model fails to recover correct view-dependent appearance after deformation. | definition/direction/unit from same section | p. 8 (5. Experiments) |
| Figure 3. Evolution of two physical simulations. From left to right: (1) A rubber duck falling onto a pillow and deforming it. (2) A ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 4. Model overview. Top: During training, a subset of Gaussians is selected using Ray-Traced Gaussian Proximity Search (RT-GPS), which also handles pruning. The ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We design our experiments to demonstrate that EKS maintains the reconstruction quality of state-of-the-art (SOTA) methods while enabling complex object modifications. | comparison identity and matched condition | p. 6 (5. Experiments) |
| These baselines are selected to demonstrate that EKS not only achieves reconstruction quality comparable to or exceeding SOTA methods, while enabling editing with significantly ... | comparison identity and matched condition | p. 6 (5. Experiments) |
| As shown in Table 2, our method consistently outperforms prior stateof-the-art approaches, including GaMeS, a purely Gaussian Splatting-based editing method. | comparison identity and matched condition | p. 7 (5. Experiments) |
| In addition, we performed simulations following PhysGaussian (Xie et al., 2024) and compared EKS qualitatively against both PhysGaussian and GASP (Borycki et al., 2024). | comparison identity and matched condition | p. 7 (5. Experiments) |
| Using Euclidean KNN introduces artifacts similar to point-based baselines, while removing hash-grid feature distillation has a smaller quantitative impact. | comparison identity and matched condition | p. 8 (5. Experiments) |
| Ablation study of EKS reporting PSNR for static reconstruction and edited scenes. | comparison identity and matched condition | p. 8 (5. Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We evaluate variants that (1) replace RT-GPS with Euclidean KNN (w/o RT-GPS), (2) remove hash-grid feature distillation and use learned per-Gaussian features (w/o Henc), ... | component/input/data sensitivity | p. 8 (5. Experiments) |
| Figure 10. Ablation study. Qualitative comparison showing the effect of individual components on rendering quality. ized, and deformation-aware scene editing. By representing latent features ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| In the Drums scene, the gong is consistently restored without visible holes. | component/input/data sensitivity | p. 7 (5. Experiments) |
| Affine-Equivariant Kernel Space Encoding for NeRF Editing Chair Drums Lego Mic Materials Ship Hotdog Ficus Non Editable INGP 31.97 22.67 33.44 31.38 22.66 28.83 ... | component/input/data sensitivity | p. 7 (5. Experiments) |
| Figure 2. Physical simulations. From left to right: (1) Rigid body simulation of falling leaves. (2) Soft body simulation of the Lego dozer being ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we introduce Affine-Equivariant Kernel Space Encoding (EKS), a novel positional encoding mechanism for NeRFs. | These baselines are selected to demonstrate that EKS not only achieves reconstruction quality comparable to or exceeding SOTA methods, while enabling editing with significantly ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5. Experiments), p. 6 (5. Experiments), p. 7 (5. Experiments), p. 8 (5. Experiments), p. 7 (5. Experiments), p. 5 (Figure/Table caption) |
| Primary metric/result | For static scene reconstruction, EKS achieves quality comparable to state-of-the-art editable methods, and in some cases provides the best results among methods that support ... | numeric claim only at cited anchor | p. 6 (5. Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 5. Experiments - extractive PDF cue:** 25.68 35.49 36.71 29.60 30.88 37.30 33.83 Editable GaMeS 35.73 26.15 35.57 35.67 29.89 30.78 37.58 34.83 RIP-NeRF 34.84 24.89 33.41 34.19 28.31 30.65 35.96 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2. Physical simulations. From left to right: (1) Rigid body simulation of falling leaves. (2) Soft body simulation of the Lego dozer being ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | By representing latent features with anisotropic Gaussian kernels and aggregating them using Mahalanobis-distance-based neighbourhoods, our method preserves local feature structure under affine transformations, addressing ... | p. 8 (6. Conclusions) |
| body limitation/failure cue | Figure 3. Evolution of two physical simulations. From left to right: (1) A rubber duck falling onto a pillow and deforming it. (2) A ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Figure 5. KNN Comparisons. Comparison of neighbourhood changes under deformation using Euclidean distance KNN (top) versus our proposed Mahalanobis distance KNN (bottom). Mov- ing ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | From left to right: (1) Physics-based simulation, showing an object falling onto a tilted table and bouncing off. | p. 6 (5. Experiments) |
| body limitation/failure cue | Whether simulating leaves falling from a plant, squashing a soft object, or draping cloth over complex geometry, our method maintains high rendering fidelity while ... | p. 7 (5. Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In contrast, EKS avoids these artifacts and consistently produces smooth surfaces with high reconstruction quality across all evaluated scenes, as the Gaussians encode latent ... | p. 7 (5. Experiments) |
| The final feature vector is computed as a weighted interpolation of the Gaussian features using a Mahalanobis-distance-based weighting scheme: v (G) = k X ... | p. 5 (4. Proposed Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Physical simulations. From left to right: (1) Rigid body simulation of falling leaves. (2) Soft body simulation of the Lego dozer being squished. ...
- **p. 8 / 6. Conclusions - extractive PDF cue:** By representing latent features with anisotropic Gaussian kernels and aggregating them using Mahalanobis-distance-based neighbourhoods, our method preserves local feature structure under affine transformations, addressing a ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. Evolution of two physical simulations. From left to right: (1) A rubber duck falling onto a pillow and deforming it. (2) A pirate ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 5. KNN Comparisons. Comparison of neighbourhood changes under deformation using Euclidean distance KNN (top) versus our proposed Mahalanobis distance KNN (bottom). Mov- ing points ...
- **p. 6 / 5. Experiments - extractive PDF cue:** From left to right: (1) Physics-based simulation, showing an object falling onto a tilted table and bouncing off.
- **p. 7 / 5. Experiments - extractive PDF cue:** Whether simulating leaves falling from a plant, squashing a soft object, or draping cloth over complex geometry, our method maintains high rendering fidelity while enabling ...

- **PDF anchors reviewed:** datasets p. 6 (5. Experiments), p. 7 (5. Experiments), p. 6 (5. Experiments), p. 7 (5. Experiments), p. 8 (5. Experiments), p. 8 (5. Experiments), metrics p. 6 (5. Experiments), p. 6 (5. Experiments), p. 7 (5. Experiments), p. 7 (5. Experiments), p. 8 (5. Experiments), p. 8 (5. Experiments), baselines p. 6 (5. Experiments), p. 6 (5. Experiments), p. 7 (5. Experiments), p. 7 (5. Experiments), p. 8 (5. Experiments), p. 8 (5. Experiments), results p. 6 (5. Experiments), p. 6 (5. Experiments), p. 7 (5. Experiments), p. 8 (5. Experiments), p. 7 (5. Experiments), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
