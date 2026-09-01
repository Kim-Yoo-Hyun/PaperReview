# Evaluation - Urban-GS: A Unified 3D Gaussian Splatting Framework for Compact and High-Fidelity Aerial-to-Street Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Urban-GS_A_Unified_3D_Gaussian_Splatting_Framework_for_Compact_and_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Urban-GS_A_Unified_3D_Gaussian_Splatting_Framework_for_Compact_and_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5.3. Ablations Study and Analysis), p. 7 (5.2. Experiment Results and Analysis), p. 7 (5.2. Experiment Results and Analysis), p. 1 (Figure/Table caption), p. 8 (5.3. Ablations Study and Analysis), p. 6 (5.1. Experimental Setup)): 5 and 8 show that additional iterations under uniform sampling yield no significant performance improvement, whereas our proposed strategy achieves a more noticeable gain.

## Evaluation Body Digest

- **p. 6 / 5.1. Experimental Setup - extractive PDF cue:** Following Horizon-GS [10], we conduct comprehensive evaluations across 7 scenes containing both aerial and street views, sourced from the UC-GS dataset [40], and Horizon-GS dataset ...
- **p. 7 / 5.1. Experimental Setup - extractive PDF cue:** Qualitive comparisons of Urban-GS against baselines [10, 12, 13] across scenes of Horizon-GS dataset [10].
- **p. 7 / 5.2. Experiment Results and Analysis - extractive PDF cue:** Quantitative comparison on UC-GS dataset [40].
- **p. 8 / 5.3. Ablations Study and Analysis - extractive PDF cue:** We use Elvenruin, Citysample, and Road from the HorizonGS dataset as target cases for analysis, with additional details provided in the supplementary material.
- **p. 8 / 5.3. Ablations Study and Analysis - extractive PDF cue:** It effectively enhances the densification capability of 3DGS in scenes with significant scale variations, leading to a substantial improvement in novel-view rendering quality.
- **p. 6 / 5.1. Experimental Setup - extractive PDF cue:** Horizon-GS, our primary state-ofthe-art comparison, was run using its original, unmodified training settings.
- **p. 6 / 5.1. Experimental Setup - extractive PDF cue:** For the global training stage, we set the learning rate of the mask scores to 0.01 and λm to 0.003, while retaining other parameter settings ...
- **p. 8 / 5.3. Ablations Study and Analysis - extractive PDF cue:** Overall, these performance gaps validate the effectiveness of our analysis that incorporates projection area weighted considerations.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiment (p. 6); 5.1. Experimental Setup (p. 6); 5.2. Experiment Results and Analysis (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.3. Ablations Study and Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | 5 and 8 show that additional iterations under uniform sampling yield no significant performance improvement, whereas our proposed strategy achieves a more noticeable gain. | p. 8 (5.3. Ablations Study and Analysis) |
| 5.2. Experiment Results and Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2, our method outperforms the performance of all baselines on the HorizonGS dataset. | p. 7 (5.2. Experiment Results and Analysis) |
| 5.2. Experiment Results and Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | The above experimental results quantitatively validate that our method achieves superior reconstruction quality and efficiency. | p. 7 (5.2. Experiment Results and Analysis) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1. Urban-GS achieves unified aerial-to-street modeling of urban scenes, supporting drastic viewpoint changes and maintaining fidelity across scales. Compared with the state-of-the-art method ... | p. 1 (Figure/Table caption) |
| 5.3. Ablations Study and Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | Remarkably, under this setting, our method achieves even higher reconstruction quality than MaskGaussian with λm = 0.001, while utilizing fewer anchors. | p. 8 (5.3. Ablations Study and Analysis) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Experimental Setup - extractive PDF cue:** Following Horizon-GS [10], we conduct comprehensive evaluations across 7 scenes containing both aerial and street views, sourced from the UC-GS dataset [40], and Horizon-GS dataset ...
- **p. 7 / 5.1. Experimental Setup - extractive PDF cue:** Qualitive comparisons of Urban-GS against baselines [10, 12, 13] across scenes of Horizon-GS dataset [10].
- **p. 7 / 5.2. Experiment Results and Analysis - extractive PDF cue:** Quantitative comparison on UC-GS dataset [40].
- **p. 8 / 5.3. Ablations Study and Analysis - extractive PDF cue:** We use Elvenruin, Citysample, and Road from the HorizonGS dataset as target cases for analysis, with additional details provided in the supplementary material.
- **p. 8 / 5.3. Ablations Study and Analysis - extractive PDF cue:** It effectively enhances the densification capability of 3DGS in scenes with significant scale variations, leading to a substantial improvement in novel-view rendering quality.
- **p. 6 / 5.1. Experimental Setup - extractive PDF cue:** Horizon-GS, our primary state-ofthe-art comparison, was run using its original, unmodified training settings.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Urban-GS achieves unified aerial-to-street modeling of urban scenes, supporting drastic viewpoint changes and maintaining fidelity across scales. Compared with the state-of-the-art method Horizon-GS ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. The overview pipeline of Urban-GS. Top (Gloabal Training): We start by initializing LOD-structured anchors from SfM- derived points of the aerial-to-street urban scene, ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative comparison across accumulating gradients for densification from aerial views only, street views only and merged views on Colosseum scene [10]. All methods ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Average position gradient (a) and average projection radius (b) for two sets of neural Gaussians over the densification process. Left plots: Analysis of ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Quantitative novel view rendering results comparison on Horizon-GS [10] dataset. The best performance of each part is in bold, while the scecond-best results ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Efficiency comparison between our method and Horizon-GS [10] on the Horizon-GS dataset. stage. For each selected target unstable view vus, we con- struct ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitive comparisons of Urban-GS against baselines [10, 12, 13] across scenes of Horizon-GS dataset [10]. Patches that highlight the visual differences are emphasized ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Qualitative comparisons of our Urban-GS against Horizon-GS [10] on UC-GS dataset [40]. Zoom-in patches high- lighting the visual differences are enclosed by yellow, ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Following Horizon-GS [10], we conduct comprehensive evaluations across 7 scenes containing both aerial and street views, sourced from the UC-GS dataset [40], and Horizon-GS ... | embodiment, simulator version and control stack | p. 6 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup) |
| Task/environment | Qualitive comparisons of Urban-GS against baselines [10, 12, 13] across scenes of Horizon-GS dataset [10]. | reset, timeout, object/scene variation | p. 7 (5.1. Experimental Setup), p. 7 (5.2. Experiment Results and Analysis) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (4.1. Aerial-Street Joint Adaptive Densification), p. 4 (4.1. Aerial-Street Joint Adaptive Densification) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (4.2. Contribution-based Anchor Pruning), p. 5 (4.2. Contribution-based Anchor Pruning) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For the global training stage, we set the learning rate of the mask scores to 0.01 and λm to 0.003, while retaining other parameter ... | definition/direction/unit from same section | p. 6 (5.1. Experimental Setup) |
| Overall, these performance gaps validate the effectiveness of our analysis that incorporates projection area weighted considerations. | definition/direction/unit from same section | p. 8 (5.3. Ablations Study and Analysis) |
| 5 and 8 show that additional iterations under uniform sampling yield no significant performance improvement, whereas our proposed strategy achieves a more noticeable gain. | definition/direction/unit from same section | p. 8 (5.3. Ablations Study and Analysis) |
| In the local optimization stage, we halve the learning rate of the anchors and set τgroup to 0.1. | definition/direction/unit from same section | p. 6 (5.1. Experimental Setup) |
| 2, our method outperforms the performance of all baselines on the HorizonGS dataset. | definition/direction/unit from same section | p. 7 (5.2. Experiment Results and Analysis) |
| Zoom-in patches highlighting the visual differences are enclosed by yellow, red and green boxes for clearer comparison. of gsplat [35] to integrate probabilistic masks ... | definition/direction/unit from same section | p. 7 (5.1. Experimental Setup) |
| Figure 1. Urban-GS achieves unified aerial-to-street modeling of urban scenes, supporting drastic viewpoint changes and maintaining fidelity across scales. Compared with the state-of-the-art method ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. The overview pipeline of Urban-GS. Top (Gloabal Training): We start by initializing LOD-structured anchors from SfM- derived points of the aerial-to-street urban ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 2, our method outperforms the performance of all baselines on the HorizonGS dataset. | comparison identity and matched condition | p. 7 (5.2. Experiment Results and Analysis) |
| These results show that our approach significantly reduces blurring and needle-like artifacts compared to the baseline methods. | comparison identity and matched condition | p. 7 (5.2. Experiment Results and Analysis) |
| Figure 1. Urban-GS achieves unified aerial-to-street modeling of urban scenes, supporting drastic viewpoint changes and maintaining fidelity across scales. Compared with the state-of-the-art method ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| We evaluate all baselines using their officially released code. | comparison identity and matched condition | p. 6 (5.1. Experimental Setup) |
| Following Horizon-GS, for the other baseline methods, we also add depth supervision consistent with our method. | comparison identity and matched condition | p. 6 (5.1. Experimental Setup) |
| Method/Metrics PSNR ↑ SSIM ↑ LPIPS ↓ Anchors ↓ Baseline 25.20 0.797 0.257 2774k + AJAD 25.66 0.820 0.209 9713k + CAP 25.50 0.815 ... | comparison identity and matched condition | p. 8 (5.3. Ablations Study and Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation on main model components. "+" means adding components in addition to all components in the above rows. "AJAD", "CAP", and "GLO" denote our ... | component/input/data sensitivity | p. 8 (5.3. Ablations Study and Analysis) |
| Detailed ablation study on the proposed Global-toLocal Optimization. | component/input/data sensitivity | p. 8 (5.3. Ablations Study and Analysis) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This method resolves densification conflicts, enabling joint contributions and enhancing overall reconstruction fidelity. • A Contribution-based Anchor Pruning method that enables reliable and efficient ... | 5 and 8 show that additional iterations under uniform sampling yield no significant performance improvement, whereas our proposed strategy achieves a more noticeable gain. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5.3. Ablations Study and Analysis), p. 7 (5.2. Experiment Results and Analysis), p. 7 (5.2. Experiment Results and Analysis), p. 1 (Figure/Table caption), p. 8 (5.3. Ablations Study and Analysis), p. 6 (5.1. Experimental Setup) |
| Primary metric/result | 2, our method outperforms the performance of all baselines on the HorizonGS dataset. | numeric claim only at cited anchor | p. 7 (5.2. Experiment Results and Analysis) |

- Numeric sentences retained from the body:
- **p. 6 / 5.1. Experimental Setup - extractive PDF cue:** Following Horizon-GS [10], we conduct comprehensive evaluations across 7 scenes containing both aerial and street views, sourced from the UC-GS dataset [40], and Horizon-GS dataset ...
- **p. 7 / 5.1. Experimental Setup - extractive PDF cue:** The rendering speeds are tested on a RTX 4090 GPU.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2. The overview pipeline of Urban-GS. Top (Gloabal Training): We start by initializing LOD-structured anchors from SfM- derived points of the aerial-to-street urban ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Table 3. Efficiency comparison between our method and Horizon-GS [10] on the Horizon-GS dataset. stage. For each selected target unstable view vus, we con- ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | This limitation is evident in its struggles in the unified aerial-street setting. | p. 8 (5.3. Ablations Study and Analysis) |
| body limitation/failure cue | However, this approach fundamentally fails to account for the contribution variations caused by drastic changes in projection areas. | p. 8 (5.3. Ablations Study and Analysis) |
| body limitation/failure cue | Figure 3. Average position gradient (a) and average projection radius (b) for two sets of neural Gaussians over the densification process. Left plots: Analysis ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In the local optimization stage, we halve the learning rate of the anchors and set τgroup to 0.1. | p. 6 (5.1. Experimental Setup) |
| For the global training stage, we set the learning rate of the mask scores to 0.01 and λm to 0.003, while retaining other parameter ... | p. 6 (5.1. Experimental Setup) |
| Using the default mask learning rate and loss weight (λm = 0.001), our method preserves important anchors more effectively than the supervision strategy in ... | p. 8 (5.3. Ablations Study and Analysis) |
| The rendering speeds are tested on a RTX 4090 GPU. | p. 7 (5.1. Experimental Setup) |
| Further implementation details are provided in the supplementary. | p. 7 (5.1. Experimental Setup) |
| 6, the aggregated contribution wi across the training views can be formulated as: wi = P v∈V /Pv i / · wv i · ... | p. 5 (4.2. Contribution-based Anchor Pruning) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. The overview pipeline of Urban-GS. Top (Gloabal Training): We start by initializing LOD-structured anchors from SfM- derived points of the aerial-to-street urban scene, ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Efficiency comparison between our method and Horizon-GS [10] on the Horizon-GS dataset. stage. For each selected target unstable view vus, we con- struct ...
- **p. 8 / 5.3. Ablations Study and Analysis - extractive PDF cue:** This limitation is evident in its struggles in the unified aerial-street setting.
- **p. 8 / 5.3. Ablations Study and Analysis - extractive PDF cue:** However, this approach fundamentally fails to account for the contribution variations caused by drastic changes in projection areas.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Average position gradient (a) and average projection radius (b) for two sets of neural Gaussians over the densification process. Left plots: Analysis of ...

- **PDF anchors reviewed:** datasets p. 6 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup), p. 7 (5.2. Experiment Results and Analysis), p. 8 (5.3. Ablations Study and Analysis), p. 8 (5.3. Ablations Study and Analysis), p. 6 (5.1. Experimental Setup), metrics p. 6 (5.1. Experimental Setup), p. 8 (5.3. Ablations Study and Analysis), p. 8 (5.3. Ablations Study and Analysis), p. 6 (5.1. Experimental Setup), p. 7 (5.2. Experiment Results and Analysis), p. 7 (5.1. Experimental Setup), baselines p. 7 (5.2. Experiment Results and Analysis), p. 7 (5.2. Experiment Results and Analysis), p. 1 (Figure/Table caption), p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup), p. 8 (5.3. Ablations Study and Analysis), results p. 8 (5.3. Ablations Study and Analysis), p. 7 (5.2. Experiment Results and Analysis), p. 7 (5.2. Experiment Results and Analysis), p. 1 (Figure/Table caption), p. 8 (5.3. Ablations Study and Analysis), p. 6 (5.1. Experimental Setup).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
