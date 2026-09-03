# Evaluation - SAGS: Structure-Aware 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/2887_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02887.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 2 (Figure/Table caption), p. 9 (4 Experiments), p. 11 (4 Experiments), p. 13 (Figure/Table caption), p. 8 (4 Experiments)): Fig. 3: Overview of the densification. Given an initial SfM [31] point cloud (left) we estimate the curvature following [25]. Curvature values are presented color-coded on the input COLMAP point ...

## Evaluation Body Digest

- **p. 8 / 4 Experiments - extractive body cue:** To evaluate the proposed method, on par with the 3D-GS [15], we utilized 13 scenes including nine scenes from Mip-NeRF360 [2], two scenes from Tanks&Temples ...
- **p. 10 / 4 Experiments - extractive body cue:** We qualitatively evaluate the proposed and the baseline methods (3D-GS [15] and Scaffold-GS [20]) across six scenes from different datasets.
- **p. 9 / 4 Experiments - extractive body cue:** In particular, we depict the color-coded displacements for the train scene from the Tanks&Temples dataset, where points with color closer to purple indicate small displacements ...
- **p. 11 / 4 Experiments - extractive body cue:** We measured the Gaussians' displacements from their original positions, on the "train" scene from Tanks&Temples [16] dataset, and encoded them in a colormap scale.
- **p. 9 / 4 Experiments - extractive body cue:** 1, we report the average evaluation performance of the proposed and the baseline methods over the three datasets.
- **p. 12 / 4 Experiments - extractive body cue:** Dataset Mip-NeRF360 Tanks&Temples Deep Blending Methods FPS Mem (MB) FPS Mem (MB) FPS Mem (MB) 3D-GS [15] 97 693 123 411 109 676 Scaffold-GS [20] ...
- **p. 11 / 4 Experiments - extractive body cue:** Comparison between the proposed and the Scaffold-GS method on the scene's structure preservation.
- **p. 8 / 4 Experiments - extractive body cue:** We evaluate the proposed SAGS model in terms of rendering quality, structure preservation, and rendering performance.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 3: Overview of the densification. Given an initial SfM [31] point cloud (left) we estimate the curvature following [25]. Curvature values are presented ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 1: Structure-Aware GS (SAGS) leverages the intrinsic structure of the scene and enforces point interaction using graph neural networks outperforming the struc- ture ... | p. 2 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | As can be easily seen, SAGS outperforms 3D-GS and the recently introduced Scaffold-GS method under all datasets and metrics. | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | The proposed method can accurately capture sharp edges and suppress "floater" artifacts that are visible on the Scaffold-GS depth maps. method can not only ... | p. 11 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 7: Comparison with SAGS-Lite. We qualitatively compared the proposed SAGS-Lite model against SAGS and 3DGS. SAGS-Lite can achieve to maintain high quality renderings ... | p. 13 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiments - extractive body cue:** To evaluate the proposed method, on par with the 3D-GS [15], we utilized 13 scenes including nine scenes from Mip-NeRF360 [2], two scenes from Tanks&Temples ...
- **p. 10 / 4 Experiments - extractive body cue:** We qualitatively evaluate the proposed and the baseline methods (3D-GS [15] and Scaffold-GS [20]) across six scenes from different datasets.
- **p. 9 / 4 Experiments - extractive body cue:** In particular, we depict the color-coded displacements for the train scene from the Tanks&Temples dataset, where points with color closer to purple indicate small displacements ...
- **p. 11 / 4 Experiments - extractive body cue:** We measured the Gaussians' displacements from their original positions, on the "train" scene from Tanks&Temples [16] dataset, and encoded them in a colormap scale.
- **p. 9 / 4 Experiments - extractive body cue:** 1, we report the average evaluation performance of the proposed and the baseline methods over the three datasets.
- **p. 12 / 4 Experiments - extractive body cue:** Dataset Mip-NeRF360 Tanks&Temples Deep Blending Methods FPS Mem (MB) FPS Mem (MB) FPS Mem (MB) 3D-GS [15] 97 693 123 411 109 676 Scaffold-GS [20] ...
- **p. 11 / 4 Experiments - extractive body cue:** Comparison between the proposed and the Scaffold-GS method on the scene's structure preservation.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Structure-Aware GS (SAGS) leverages the intrinsic structure of the scene and enforces point interaction using graph neural networks outperforming the struc- ture agnostic ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of the proposed method. Given a point cloud obtained from COLMAP [31], we initially apply a curvature-based densification step to populate under-represented ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3. Leveraging the mid-point densification step, we can train a lightweight
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: Overview of the densification. Given an initial SfM [31] point cloud (left) we estimate the curvature following [25]. Curvature values are presented color-coded ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 1: Quantitative comparison between the proposed and the baseline methods on Mip-NeRF360 [2], Tanks&Temples [16] and Deep Blending [13] datasets.
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 4: Qualitative comparison. We qualitatively evaluate the proposed and the baseline methods (3D-GS [15] and Scaffold-GS [20]) across six scenes from different datasets. We ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 5: Color Coded Gaussian Displacements. We measured the Gaussians' dis- placements from their original positions, on the "train" scene from Tanks&Temples [16] dataset, and ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 6: Depth Structural Preservation. Comparison between the proposed and the Scaffold-GS method on the scene's structure preservation. The proposed method can accurately capture sharp ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To evaluate the proposed method, on par with the 3D-GS [15], we utilized 13 scenes including nine scenes from Mip-NeRF360 [2], two scenes from ... | embodiment, simulator version and control stack | p. 8 (4 Experiments), p. 10 (4 Experiments) |
| Task/environment | We qualitatively evaluate the proposed and the baseline methods (3D-GS [15] and Scaffold-GS [20]) across six scenes from different datasets. | reset, timeout, object/scene variation | p. 10 (4 Experiments), p. 9 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 7 (3 Method), p. 5 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (3 Method), p. 7 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We evaluate the proposed SAGS model in terms of rendering quality, structure preservation, and rendering performance. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| 5, we illustrate the displacements of points, in a color-coded format, on top of their original positions. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| 1, we report the average evaluation performance of the proposed and the baseline methods over the three datasets. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Furthermore, Scaffold-GS method falls short in accurately representing flat surfaces, as can be seen in the walls and the table, | definition/direction/unit from same section | p. 11 (4 Experiments) |
| The proposed method can accurately capture sharp edges and suppress "floater" artifacts that are visible on the Scaffold-GS depth maps. method can not only ... | definition/direction/unit from same section | p. 11 (4 Experiments) |
| Fig. 1: Structure-Aware GS (SAGS) leverages the intrinsic structure of the scene and enforces point interaction using graph neural networks outperforming the struc- ture ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Fig. 2: Overview of the proposed method. Given a point cloud obtained from COLMAP [31], we initially apply a curvature-based densification step to populate ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Fig. 3: Overview of the densification. Given an initial SfM [31] point cloud (left) we estimate the curvature following [25]. Curvature values are presented ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compared the proposed method with NeRF- and 3D-GS-based state-of-the-art works in novel-view synthesis, including the Mip-NeRF360 [2], Plenoxels [10], iNGP [23], 3D-GS [15] ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| The proposed method consistently captures more structural and high-frequency details while minimizing floaters and artifacts compared to the baseline methods. | comparison identity and matched condition | p. 10 (4 Experiments) |
| 1, we report the average evaluation performance of the proposed and the baseline methods over the three datasets. | comparison identity and matched condition | p. 9 (4 Experiments) |
| As can be easily seen, SAGS outperforms 3D-GS and the recently introduced Scaffold-GS method under all datasets and metrics. | comparison identity and matched condition | p. 9 (4 Experiments) |
| We qualitatively evaluate the proposed and the baseline methods (3D-GS [15] and Scaffold-GS [20]) across six scenes from different datasets. | comparison identity and matched condition | p. 10 (4 Experiments) |
| We also report the storage reduction of each model compared to original 3D-GS method [15]. | comparison identity and matched condition | p. 12 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This is caused by the unstructured nature of the Gaussian optimization that attempts to minimize only the rendering constraints without any structural guidance. | component/input/data sensitivity | p. 11 (4 Experiments) |
| Table 3: Ablation study on the components of SAGS. The ablation was per- formed on the Deep Blending and the Tanks&Temples datasets. Scene Deep ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| Fig. 8: Ablation study on the components of SAGS. We perform a series of ablation experiments on the Deep Blending and the Tanks&Temples datasets ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Fig. 3: Overview of the densification. Given an initial SfM [31] point cloud (left) we estimate the curvature following [25]. Curvature values are presented ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To sum up, our contributions can be summarized as follows: - We introduce the first structure-aware 3D Gaussian Splatting method that leverages both local ... | Fig. 3: Overview of the densification. Given an initial SfM [31] point cloud (left) we estimate the curvature following [25]. Curvature values are presented ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 2 (Figure/Table caption), p. 9 (4 Experiments), p. 11 (4 Experiments), p. 13 (Figure/Table caption), p. 8 (4 Experiments) |
| Primary metric/result | Fig. 1: Structure-Aware GS (SAGS) leverages the intrinsic structure of the scene and enforces point interaction using graph neural networks outperforming the struc- ture ... | numeric claim only at cited anchor | p. 2 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 8 / 4 Experiments - extractive body cue:** To evaluate the proposed method, on par with the 3D-GS [15], we utilized 13 scenes including nine scenes from Mip-NeRF360 [2], two scenes from Tanks&Temples ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Using the proposed structure-aware encoder, we manage to tackle the structure preservation limitations of previous 3D-GS methods and constrain the point displacements close to ... | p. 9 (4 Experiments) |
| body limitation/failure cue | Furthermore, Scaffold-GS method falls short in accurately representing flat surfaces, as can be seen in the walls and the table, | p. 11 (4 Experiments) |
| body limitation/failure cue | Both the 3D-GS and Scaffold-GS methodologies depend on a rudimentary point optimization approach, that neglects the local topology and fails to guide the Gaussians ... | p. 11 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 5, we illustrate the displacements of points, in a color-coded format, on top of their original positions. | p. 9 (4 Experiments) |
| Using the proposed structure-aware encoder, we manage to tackle the structure preservation limitations of previous 3D-GS methods and constrain the point displacements close to ... | p. 9 (4 Experiments) |
| We measured the Gaussians' displacements from their original positions, on the "train" scene from Tanks&Temples [16] dataset, and encoded them in a colormap scale. | p. 11 (4 Experiments) |
| The proposed method can be divided into three main components: a) the curvatureaware densification, b) the structure-aware encoder, and c) the refinement layer. | p. 5 (3 Method) |
| Using a set of small MLPs we decode the structural features to 3D Gaussian attributes, i.e., color c, opacity α, covariance Σ and point ... | p. 5 (3 Method) |
| To further enhance our encoder with global structural information of the scene, we included a global feature that is | p. 6 (3 Method) |
| Curvature values are presented color-coded on the input COLMAP point cloud (middle) where colors with minimum curvature are closer to the purple color. | p. 6 (3 Method) |
| To encode Gaussian positions we selected the high-performing multi-resolution hash encoding [23] given its lightweight nature and its ability to expressively encode complex scenes. | p. 7 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4 Experiments - extractive body cue:** Using the proposed structure-aware encoder, we manage to tackle the structure preservation limitations of previous 3D-GS methods and constrain the point displacements close to their ...
- **p. 11 / 4 Experiments - extractive body cue:** Furthermore, Scaffold-GS method falls short in accurately representing flat surfaces, as can be seen in the walls and the table,
- **p. 11 / 4 Experiments - extractive body cue:** Both the 3D-GS and Scaffold-GS methodologies depend on a rudimentary point optimization approach, that neglects the local topology and fails to guide the Gaussians in ...

- **Evidence anchors reviewed:** datasets p. 8 (4 Experiments), p. 10 (4 Experiments), p. 9 (4 Experiments), p. 11 (4 Experiments), p. 9 (4 Experiments), p. 12 (4 Experiments), metrics p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 2 (Figure/Table caption), baselines p. 8 (4 Experiments), p. 10 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments), p. 12 (4 Experiments), results p. 6 (Figure/Table caption), p. 2 (Figure/Table caption), p. 9 (4 Experiments), p. 11 (4 Experiments), p. 13 (Figure/Table caption), p. 8 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
