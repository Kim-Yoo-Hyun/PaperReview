# Evaluation - Gau-Occ: Geometry-Completed Gaussians for Multi-Modal 3D Occupancy Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Lv_Gau-Occ_Geometry-Completed_Gaussians_for_Multi-Modal_3D_Occupancy_Prediction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Lv_Gau-Occ_Geometry-Completed_Gaussians_for_Multi-Modal_3D_Occupancy_Prediction_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.2. Quantitative Results), p. 5 (4.2. Quantitative Results), p. 8 (4.4. Ablation Study), p. 6 (4.2. Quantitative Results), p. 6 (4.2. Quantitative Results), p. 7 (4.4. Ablation Study)): Across modalities, LiDARonly approaches generally outperform camera-only methods due to geometric cues, and multi-modal systems further improve performance.

## Evaluation Body Digest

- **p. 5 / 4.1. Datasets and Metrics - extractive body cue:** We evaluate Gau-Occ on three widely adopted benchmarks: SurroundOcc-nuScenes [2, 46], Occ3DnuScenes [40], and KITTI-360 [28].
- **p. 6 / 4.2. Quantitative Results - extractive body cue:** Quantitative comparison on Occ3D-nuScenes validation set.
- **p. 7 / 4.3. Qualitative Comparison - extractive body cue:** Qualitative results on the Occ3D-nuScenes validation set.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Ablation on the SurroundOcc-nuScenes validation set.
- **p. 5 / 4.2. Quantitative Results - extractive body cue:** Results on the validation split are reported in Tab.
- **p. 6 / 4.2. Quantitative Results - extractive body cue:** Multimodal baselines are scarce on this dataset.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** IoU↑ mIoU↑ 1 P DS + RS 41.5 29.6 2 PD(P) DS + RS 43.1 31.9 3 P′ RS 43.9 32.4 4 P′ DS + ...
- **p. 7 / 4.4. Ablation Study - extractive body cue:** This approach balances structural concentration with broad scene coverage, enabling better reconstruction of far-range and easily overlooked object, such as drivable surfaces and cars.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Datasets and Metrics (p. 5); 4.2. Quantitative Results (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Quantitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Across modalities, LiDARonly approaches generally outperform camera-only methods due to geometric cues, and multi-modal systems further improve performance. | p. 5 (4.2. Quantitative Results) |
| 4.2. Quantitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Gau-Occ achieves a new state of the art with 55.1 mIoU, surpassing DAOcc by +0.8, SDGOcc by +3.4, and even outperforming radar-augmented OccFusion by ... | p. 5 (4.2. Quantitative Results) |
| 4.4. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | The full GAF configuration (Row 4) achieves optimal results, validating the necessity of both geometry-guided sampling and refinement in building a robust multi-modal representation. | p. 8 (4.4. Ablation Study) |
| 4.2. Quantitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown, Gau-Occ outperforms the strongest LiDAR-only baseline, L2COcc [43], by +1.3 IoU and +0.6 mIoU. | p. 6 (4.2. Quantitative Results) |
| 4.2. Quantitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Under this challenging single-camera setting, our method shows notable improvements on moving vehicles (car, truck) and large structures (road, building), demonstrating its capability for ... | p. 6 (4.2. Quantitative Results) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Datasets and Metrics - extractive body cue:** We evaluate Gau-Occ on three widely adopted benchmarks: SurroundOcc-nuScenes [2, 46], Occ3DnuScenes [40], and KITTI-360 [28].
- **p. 6 / 4.2. Quantitative Results - extractive body cue:** Quantitative comparison on Occ3D-nuScenes validation set.
- **p. 7 / 4.3. Qualitative Comparison - extractive body cue:** Qualitative results on the Occ3D-nuScenes validation set.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Ablation on the SurroundOcc-nuScenes validation set.
- **p. 5 / 4.2. Quantitative Results - extractive body cue:** Results on the validation split are reported in Tab.
- **p. 6 / 4.2. Quantitative Results - extractive body cue:** Multimodal baselines are scarce on this dataset.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** IoU↑ mIoU↑ 1 P DS + RS 41.5 29.6 2 PD(P) DS + RS 43.1 31.9 3 P′ RS 43.9 32.4 4 P′ DS + ...
- **p. 7 / 4.4. Ablation Study - extractive body cue:** This approach balances structural concentration with broad scene coverage, enabling better reconstruction of far-range and easily overlooked object, such as drivable surfaces and cars.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1. Overview of Gau-Occ. Sparse LiDAR scans are first completed by a pretrained LiDAR Completion Diffuser (LCD) to recover occluded geometry. The completed points ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Hybrid Gaussian initialization. Left: raw sparse Li- DAR input. Middle: completed point cloud P′ from LCD. Right: initialized Gaussian centers derived from P′, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Schematic of geometry-aware image token resampling and modulation. N = V × L × N off is the total number of samples. As ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparison on SurroundOcc-nuScenes validation set. The best results are in bold, second best are underlined.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Quantitative comparison on Occ3D-nuScenes validation set. The best results are in bold, second best are underlined.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative results on the SurroundOcc-nuScenes validation set. Top: multi-view images (left), LiDAR input (center), and predicted image-view occupancy (right). Bottom: predicted 3D Gaussians, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative results on the Occ3D-nuScenes validation set. Top: predicted occupancy. Bottom: ground-truth. introducing holes in ground or object regions. These obser- vations support ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Qualitative comparison between Gaussianformer-2 [16], DAOcc [49] and Gau-Occ on the SurroundOcc-nuScenes validation set.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate Gau-Occ on three widely adopted benchmarks: SurroundOcc-nuScenes [2, 46], Occ3DnuScenes [40], and KITTI-360 [28]. | embodiment, simulator version and control stack | p. 5 (4.1. Datasets and Metrics), p. 6 (4.2. Quantitative Results) |
| Task/environment | Quantitative comparison on Occ3D-nuScenes validation set. | reset, timeout, object/scene variation | p. 6 (4.2. Quantitative Results), p. 7 (4.3. Qualitative Comparison) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (3.1. 3D Semantic Gaussian Scene Representation), p. 4 (3.2. LiDAR Completion Diffuser (LCD)) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.2. LiDAR Completion Diffuser (LCD)), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 7, replacing the completed point cloud P′ with the raw input P leads to notable performance drops in both IoU and mIoU. | definition/direction/unit from same section | p. 7 (4.4. Ablation Study) |
| For quantitative analysis, the Intersection over Union (IoU) and mean IoU (mIoU) are used as evaluation metrics, consistent with previous work [3]. | definition/direction/unit from same section | p. 5 (4.1. Datasets and Metrics) |
| Gau-Occ establishes a new state-ofthe-art, surpassing the previous best multi-modal method (DAOcc [49]) by significant margins of +1.5 IoU and +0.6 mIoU. | definition/direction/unit from same section | p. 5 (4.2. Quantitative Results) |
| As shown, Gau-Occ outperforms the strongest LiDAR-only baseline, L2COcc [43], by +1.3 IoU and +0.6 mIoU. | definition/direction/unit from same section | p. 6 (4.2. Quantitative Results) |
| This also causes a slight accuracy drop, attributed to token redundancy. | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| IoU↑ mIoU↑ 1 P DS + RS 41.5 29.6 2 PD(P) DS + RS 43.1 31.9 3 P′ RS 43.9 32.4 4 P′ DS ... | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| On KITTI-360, under challenging singlecamera + LiDAR setting, Gau-Occ maps both large layouts and small instances accurately, demonstrating robustness to sparse viewpoints and effective ... | definition/direction/unit from same section | p. 6 (4.3. Qualitative Comparison) |
| On Point Cloud Completion and Gaussian Initialization. | definition/direction/unit from same section | p. 7 (4.4. Ablation Study) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown, Gau-Occ outperforms the strongest LiDAR-only baseline, L2COcc [43], by +1.3 IoU and +0.6 mIoU. | comparison identity and matched condition | p. 6 (4.2. Quantitative Results) |
| 6 provides comparisons with state-of-the-art counterparts, i.e. | comparison identity and matched condition | p. 6 (4.3. Qualitative Comparison) |
| Gau-Occ achieves a new state of the art with 55.1 mIoU, surpassing DAOcc by +0.8, SDGOcc by +3.4, and even outperforming radar-augmented OccFusion by ... | comparison identity and matched condition | p. 5 (4.2. Quantitative Results) |
| Across modalities, LiDARonly approaches generally outperform camera-only methods due to geometric cues, and multi-modal systems further improve performance. | comparison identity and matched condition | p. 5 (4.2. Quantitative Results) |
| Compared to diffusionbased alternatives such as LiDPM [32] (omitted for brevity), our lightweight pre-trained module provides superior geometric priors. | comparison identity and matched condition | p. 7 (4.4. Ablation Study) |
| Furthermore, the hybrid initialization strategy combining DS (density-based selection) and RS (random sampling) consistently outperforms the use of vanilla RS alone. | comparison identity and matched condition | p. 7 (4.4. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We further conduct a comprehensive ablation study on the GAF module, focusing on two core components governing cross-modal fusion: (1) GGS (Geometry-Guided Sampling), which ... | component/input/data sensitivity | p. 7 (4.4. Ablation Study) |
| Visualization of ablations on GAF components. sistency during fusion. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| IoU↑ mIoU↑ 1 P DS + RS 41.5 29.6 2 PD(P) DS + RS 43.1 31.9 3 P′ RS 43.9 32.4 4 P′ DS ... | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| While DAOcc benefits from detection-level supervision, the proposed Gau-Occ attains superior accuracy without additional priors, highlighting advantage of geometrycomplete Gaussian anchors and structure-aware fusion. | component/input/data sensitivity | p. 5 (4.2. Quantitative Results) |
| For example, in Case 1, Gau-Occ is the only method that reconstructs lower building outlines and terrain surfaces cleanly; in Case 2, it recovers ... | component/input/data sensitivity | p. 6 (4.3. Qualitative Comparison) |
| Figure 1. Overview of Gau-Occ. Sparse LiDAR scans are first completed by a pretrained LiDAR Completion Diffuser (LCD) to recover occluded geometry. The completed ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are: • We propose Gau-Occ, a compact Gaussian-based framework that unifies LiDAR and multi-view images for 3D semantic occupancy prediction. ... | Across modalities, LiDARonly approaches generally outperform camera-only methods due to geometric cues, and multi-modal systems further improve performance. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.2. Quantitative Results), p. 5 (4.2. Quantitative Results), p. 8 (4.4. Ablation Study), p. 6 (4.2. Quantitative Results), p. 6 (4.2. Quantitative Results), p. 7 (4.4. Ablation Study) |
| Primary metric/result | Gau-Occ achieves a new state of the art with 55.1 mIoU, surpassing DAOcc by +0.8, SDGOcc by +3.4, and even outperforming radar-augmented OccFusion by ... | numeric claim only at cited anchor | p. 5 (4.2. Quantitative Results) |

- Numeric sentences retained from the body:
- **p. 7 / 4.4. Ablation Study - extractive body cue:** We further conduct a comprehensive ablation study on the GAF module, focusing on two core components governing cross-modal fusion: (1) GGS (Geometry-Guided Sampling), which conditions ...
- **p. 4 / 3.4. Gaussian Anchor Fusion (GAF) - extractive body cue:** The completed LiDAR cloud P′ is voxelized into a sparse grid of size D ×H ×W, keeping at most Tp = 10 points per voxel ...
- **p. 5 / 3.4. Gaussian Anchor Fusion (GAF) - extractive body cue:** 3, instead of applying another attention block, we aggregate them via a geometry-aware VLAD-style [17] resampler using codewords {Cm}M m=1 that act as learnable semantic ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Gau-Occ also achieves clear gains on safety-critical classes such as bus, car, bicycle, and motorcycle, benefiting from precise Geo-VLAD resampling and geometry-aware FiLM modulation ... | p. 5 (4.2. Quantitative Results) |
| body limitation/failure cue | On KITTI-360, under challenging singlecamera + LiDAR setting, Gau-Occ maps both large layouts and small instances accurately, demonstrating robustness to sparse viewpoints and effective ... | p. 6 (4.3. Qualitative Comparison) |
| body limitation/failure cue | These observations support Gau-Occ's geometry-complete representation and its robust multi-modal aggregation pipeline. | p. 7 (4.3. Qualitative Comparison) |
| body limitation/failure cue | The full GAF configuration (Row 4) achieves optimal results, validating the necessity of both geometry-guided sampling and refinement in building a robust multi-modal representation. | p. 8 (4.4. Ablation Study) |
| body limitation/failure cue | Replacing GGS with geometry-agnostic sampling (Row 2) degrades long-range feature association, underscoring the importance of LiDARconditioned offsets in maintaining spatial and semantic conFigure 8. | p. 8 (4.4. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We further conduct a comprehensive ablation study on the GAF module, focusing on two core components governing cross-modal fusion: (1) GGS (Geometry-Guided Sampling), which ... | p. 7 (4.4. Ablation Study) |
| Removing GVR (Row 3) and directly feeding the original, unaggregated tokens Xi to cross-attention leads to markedly higher latency and memory usage, as the ... | p. 8 (4.4. Ablation Study) |
| We propose Gau-Occ, a compact representation of 3D scenes using semantic Gaussians that jointly encode LiDAR geometry and multi-view semantics. | p. 2 (3. Proposed Approach) |
| The completed points are encoded into geometric features to initialize density-aware semantic 3D Gaussians. | p. 3 (3.1. 3D Semantic Gaussian Scene Representation) |
| Finally, fused features [fpc,i; fimg,i] are decoded through a two-layer FFN to update Gaussian attributes: [bµi,bsi,bri,bci] = FFN  [fpc,i; fimg,i]  , (17) The ... | p. 5 (3.4. Gaussian Anchor Fusion (GAF)) |
| 3, instead of applying another attention block, we aggregate them via a geometry-aware VLAD-style [17] resampler using codewords {Cm}M m=1 that act as learnable ... | p. 5 (3.4. Gaussian Anchor Fusion (GAF)) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 4.2. Quantitative Results - extractive body cue:** Gau-Occ also achieves clear gains on safety-critical classes such as bus, car, bicycle, and motorcycle, benefiting from precise Geo-VLAD resampling and geometry-aware FiLM modulation that ...
- **p. 6 / 4.3. Qualitative Comparison - extractive body cue:** On KITTI-360, under challenging singlecamera + LiDAR setting, Gau-Occ maps both large layouts and small instances accurately, demonstrating robustness to sparse viewpoints and effective use ...
- **p. 7 / 4.3. Qualitative Comparison - extractive body cue:** These observations support Gau-Occ's geometry-complete representation and its robust multi-modal aggregation pipeline.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** The full GAF configuration (Row 4) achieves optimal results, validating the necessity of both geometry-guided sampling and refinement in building a robust multi-modal representation.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Replacing GGS with geometry-agnostic sampling (Row 2) degrades long-range feature association, underscoring the importance of LiDARconditioned offsets in maintaining spatial and semantic conFigure 8.

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Datasets and Metrics), p. 6 (4.2. Quantitative Results), p. 7 (4.3. Qualitative Comparison), p. 8 (4.4. Ablation Study), p. 5 (4.2. Quantitative Results), p. 6 (4.2. Quantitative Results), metrics p. 7 (4.4. Ablation Study), p. 5 (4.1. Datasets and Metrics), p. 5 (4.2. Quantitative Results), p. 6 (4.2. Quantitative Results), p. 8 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), baselines p. 6 (4.2. Quantitative Results), p. 6 (4.3. Qualitative Comparison), p. 5 (4.2. Quantitative Results), p. 5 (4.2. Quantitative Results), p. 7 (4.4. Ablation Study), p. 7 (4.4. Ablation Study), results p. 5 (4.2. Quantitative Results), p. 5 (4.2. Quantitative Results), p. 8 (4.4. Ablation Study), p. 6 (4.2. Quantitative Results), p. 6 (4.2. Quantitative Results), p. 7 (4.4. Ablation Study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
