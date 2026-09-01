# Evaluation - CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Tian_CCL-LGS_Contrastive_Codebook_Learning_for_3D_Language_Gaussian_Splatting_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Tian_CCL-LGS_Contrastive_Codebook_Learning_for_3D_Language_Gaussian_Splatting_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.1. Experiments on LERF), p. 7 (4.1. Experiments on LERF), p. 8 (4.2. Experiments on 3D-OVS), p. 7 (4.1. Experiments on LERF), p. 8 (4.2. Experiments on 3D-OVS), p. 1 (Figure/Table caption)): We observed that our method achieved an IoU result of 65.6 in 3D semantic segmentation, ranking either first or second across all four scenes, outperforming the state-ofthe-art 3D Vision-Language GS ...

## Evaluation Body Digest

- **p. 6 / 4. Experiments - extractive PDF cue:** The dataset's real-world imaging conditions, including severe occlusions and motion blur, make it particularly suited for testing segmentation robustness in complex environments.
- **p. 6 / 4. Experiments - extractive PDF cue:** To assess the effectiveness of our approach, we conduct experiments on two benchmark datasets using the mean Intersection over Union (mIoU) metric.
- **p. 7 / 4.1. Experiments on LERF - extractive PDF cue:** Evaluations are conducted on four LERF scenes.
- **p. 7 / 4.1. Experiments on LERF - extractive PDF cue:** Segmentation results on the figurines (top) and kitchen (bottom) scenes.
- **p. 8 / 4.2. Experiments on 3D-OVS - extractive PDF cue:** Qualitative comparison on 3D-OVS dataset.
- **p. 8 / 4.2. Experiments on 3D-OVS - extractive PDF cue:** Quantitative experiments results on 3D-OVS dataset.
- **p. 6 / 4. Experiments - extractive PDF cue:** Note that the Room scene contains a significant annotation error; thus, we exclude it from quantitative evaluation and provide qualitative results only in the supplementary ...
- **p. 6 / 4.1. Experiments on LERF - extractive PDF cue:** We observed that our method achieved an IoU result of 65.6 in 3D semantic segmentation, ranking either first or second across all four scenes, outperforming ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6); 4.1. Experiments on LERF (p. 6); 4.2. Experiments on 3D-OVS (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Experiments on LERF | EMPIRICAL / REAL-ROBOT OR HARDWARE | We observed that our method achieved an IoU result of 65.6 in 3D semantic segmentation, ranking either first or second across all four scenes, ... | p. 6 (4.1. Experiments on LERF) |
| 4.1. Experiments on LERF | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method achieves consistent multi-view segmentation and accurately captures challenging objects like the cabinet, outperforming prior approaches. glass of water kamaboko RGB GT Ours ... | p. 7 (4.1. Experiments on LERF) |
| 4.2. Experiments on 3D-OVS | EMPIRICAL / REAL-ROBOT OR HARDWARE | While our approach achieves comparable performance, it underperforms 3D VL-GS. | p. 8 (4.2. Experiments on 3D-OVS) |
| 4.1. Experiments on LERF | EMPIRICAL / REAL-ROBOT OR HARDWARE | This demonstrates that CCL improves alignment between extracted features and semantic ground truth during 2D supervision. | p. 7 (4.1. Experiments on LERF) |
| 4.2. Experiments on 3D-OVS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In these two scenes, our method clearly outperforms the other two methods. | p. 8 (4.2. Experiments on 3D-OVS) |

## Dataset / Benchmark Role

- **p. 6 / 4. Experiments - extractive PDF cue:** The dataset's real-world imaging conditions, including severe occlusions and motion blur, make it particularly suited for testing segmentation robustness in complex environments.
- **p. 6 / 4. Experiments - extractive PDF cue:** To assess the effectiveness of our approach, we conduct experiments on two benchmark datasets using the mean Intersection over Union (mIoU) metric.
- **p. 7 / 4.1. Experiments on LERF - extractive PDF cue:** Evaluations are conducted on four LERF scenes.
- **p. 7 / 4.1. Experiments on LERF - extractive PDF cue:** Segmentation results on the figurines (top) and kitchen (bottom) scenes.
- **p. 8 / 4.2. Experiments on 3D-OVS - extractive PDF cue:** Qualitative comparison on 3D-OVS dataset.
- **p. 8 / 4.2. Experiments on 3D-OVS - extractive PDF cue:** Quantitative experiments results on 3D-OVS dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Quantitative comparison of our method and LangSplat under three challenging scenarios: Occlusion, Image Blur, and View- Dependent Variations. The results clearly demonstrate the ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. The framework of our CCL-LGS. Top: Instance tracker responsible for mask association. Middle: CCL module that constructs consistent 2D semantic supervision. For multi-view ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Tab. 1. We observed that our method achieved an IoU result of 65.6 in 3D semantic segmentation, ranking either first or second across all four ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative experiments results on LERF dataset. The best result is bolded, and the second-best result is underlined.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Ablation study on LERF dataset. "tea in glass" "ottolenghi" "miffy" Ground Truth 2D Feature w/ CCL Module 2D Feature
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative comparison of 2D feature maps with and without CCL module. Visualization Results. Fig. 4 illustrates segmentation re- sults for two scenes: figurines ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Segmentation results on the figurines (top) and kitchen (bottom) scenes. Our method achieves consistent multi-view segmentation and accurately captures challenging objects like the ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Qualitative comparison of different loss configurations. The pull loss improves intra-class consistency (e.g., for "glass of water"), while the push loss reduces false ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset's real-world imaging conditions, including severe occlusions and motion blur, make it particularly suited for testing segmentation robustness in complex environments. | embodiment, simulator version and control stack | p. 6 (4. Experiments), p. 6 (4. Experiments) |
| Task/environment | To assess the effectiveness of our approach, we conduct experiments on two benchmark datasets using the mean Intersection over Union (mIoU) metric. | reset, timeout, object/scene variation | p. 6 (4. Experiments), p. 7 (4.1. Experiments on LERF) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.2. Two-Level Semantic Feature Extraction), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.2. Two-Level Semantic Feature Extraction), p. 4 (3.2. Two-Level Semantic Feature Extraction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Note that the Room scene contains a significant annotation error; thus, we exclude it from quantitative evaluation and provide qualitative results only in the ... | definition/direction/unit from same section | p. 6 (4. Experiments) |
| We observed that our method achieved an IoU result of 65.6 in 3D semantic segmentation, ranking either first or second across all four scenes, ... | definition/direction/unit from same section | p. 6 (4.1. Experiments on LERF) |
| Figure 1. Quantitative comparison of our method and LangSplat under three challenging scenarios: Occlusion, Image Blur, and View- Dependent Variations. The results clearly demonstrate ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| 2, both losses are essential for optimal performance-removing either causes noticeable degradation, though all variants still surpass the baseline. | definition/direction/unit from same section | p. 7 (4.1. Experiments on LERF) |
| Qualitative comparison of different loss configurations. | definition/direction/unit from same section | p. 7 (4.1. Experiments on LERF) |
| While our approach achieves comparable performance, it underperforms 3D VL-GS. | definition/direction/unit from same section | p. 8 (4.2. Experiments on 3D-OVS) |
| Among the compared methods, our method produces the most accurate segmentation maps, further demonstrating the effectiveness of our CCL-LGS. | definition/direction/unit from same section | p. 8 (4.2. Experiments on 3D-OVS) |
| Figure 2. The framework of our CCL-LGS. Top: Instance tracker responsible for mask association. Middle: CCL module that constructs consistent 2D semantic supervision. For ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method achieves consistent multi-view segmentation and accurately captures challenging objects like the cabinet, outperforming prior approaches. glass of water kamaboko RGB GT Ours ... | comparison identity and matched condition | p. 7 (4.1. Experiments on LERF) |
| Figure 5. Qualitative comparison of different loss configurations. The pull loss improves intra-class consistency (e.g., for "glass of water"), while the push loss reduces ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 1. Quantitative comparison of our method and LangSplat under three challenging scenarios: Occlusion, Image Blur, and View- Dependent Variations. The results clearly demonstrate ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Baseline 46.8 57.1 60.8 61.0 56.4 baseline(w/ pull loss) 48.0 58.0 70.1 62.0 59.5 baseline(w/ push loss) 55.1 61.0 66.0 59.3 60.4 Ours 62.3 ... | comparison identity and matched condition | p. 6 (4.1. Experiments on LERF) |
| We observed that our method achieved an IoU result of 65.6 in 3D semantic segmentation, ranking either first or second across all four scenes, ... | comparison identity and matched condition | p. 6 (4.1. Experiments on LERF) |
| In these two scenes, our method clearly outperforms the other two methods. | comparison identity and matched condition | p. 8 (4.2. Experiments on 3D-OVS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To validate the effectiveness of our Contrastive Codebook Learning (CCL) module, we conduct experiments, including visual analysis of 2D supervision features and ablation studies ... | component/input/data sensitivity | p. 6 (4.1. Experiments on LERF) |
| Figure 5. Qualitative comparison of different loss configurations. The pull loss improves intra-class consistency (e.g., for "glass of water"), while the push loss reduces ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| 2, both losses are essential for optimal performance-removing either causes noticeable degradation, though all variants still surpass the baseline. | component/input/data sensitivity | p. 7 (4.1. Experiments on LERF) |
| Qualitative comparison of 2D feature maps with and without CCL module. | component/input/data sensitivity | p. 6 (4.1. Experiments on LERF) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contributions of our work can be summarized as follows: • We propose a novel framework, CCL-LGS, which integrates view-consistent semantic supervision to ... | We observed that our method achieved an IoU result of 65.6 in 3D semantic segmentation, ranking either first or second across all four scenes, ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.1. Experiments on LERF), p. 7 (4.1. Experiments on LERF), p. 8 (4.2. Experiments on 3D-OVS), p. 7 (4.1. Experiments on LERF), p. 8 (4.2. Experiments on 3D-OVS), p. 1 (Figure/Table caption) |
| Primary metric/result | Our method achieves consistent multi-view segmentation and accurately captures challenging objects like the cabinet, outperforming prior approaches. glass of water kamaboko RGB GT Ours ... | numeric claim only at cited anchor | p. 7 (4.1. Experiments on LERF) |

- Numeric sentences retained from the body:
- **p. 4 / 3.2. Two-Level Semantic Feature Extraction - extractive PDF cue:** In our method, a uniform 32×32 point prompt is provided to SAM to generate three types of masks corresponding to the semantic scales of subparts, ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations remain due to inherent capabilities of SAM and SAM2, as imperfect masks still affect results. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Future work will refine masks for greater robustness. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 1. Quantitative comparison of our method and LangSplat under three challenging scenarios: Occlusion, Image Blur, and View- Dependent Variations. The results clearly demonstrate ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | The dataset's real-world imaging conditions, including severe occlusions and motion blur, make it particularly suited for testing segmentation robustness in complex environments. | p. 6 (4. Experiments) |
| body limitation/failure cue | In the kitchen scene, we specifically focus on the cabinet, a challenging object that other methods frequently fail to segment correctly. | p. 6 (4.1. Experiments on LERF) |
| body limitation/failure cue | Combining both ensures robust, discriminative 3D semantic segmentation in challenging scenes. | p. 7 (4.1. Experiments on LERF) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The training is performed over 30,000 iterations using the Adam optimizer [10], with a learning rate of 0.001 and beta parameters set to (0.9, ... | p. 6 (4. Experiments) |
| To validate the effectiveness of our Contrastive Codebook Learning (CCL) module, we conduct experiments, including visual analysis of 2D supervision features and ablation studies ... | p. 6 (4.1. Experiments on LERF) |
| The baseline uses codebook-based feature compression to produce 2D semantic supervision for 3D segmentation. | p. 7 (4.1. Experiments on LERF) |
| Although LangSplat [20] extracts object-level features with clear boundaries by generating masks for subparts, parts, and whole objects, its dependence on multiple models increases ... | p. 4 (3.2. Two-Level Semantic Feature Extraction) |
| 3.2), then perform mask association and contrastive codebook learning to organize and refine these features (Sec. | p. 3 (3. Method) |
| Images are rasterized by splatting Gaussians onto each pixel v in the scene and performing α-blending to compute the final color C(v), as defined ... | p. 3 (3. Method) |
| SAM Sub-Part Whole-Part 1 2 N Codebook Instance Tracker Rasterizer 𝓛𝓛𝒄𝒄𝒄𝒄 ෢ 𝑮𝑮𝑮𝑮Feature Map Frozen Tracker CLIP Multi-view Captures with Anything Masks by SAM ... | p. 4 (3.2. Two-Level Semantic Feature Extraction) |
| The codebook serves as latent feature prototypes that structure the feature space for contrastive learning. | p. 5 (3.3. Contrastive Codebook Learning) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** Limitations remain due to inherent capabilities of SAM and SAM2, as imperfect masks still affect results.
- **p. 8 / 5. Conclusion - extractive PDF cue:** Future work will refine masks for greater robustness.
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Quantitative comparison of our method and LangSplat under three challenging scenarios: Occlusion, Image Blur, and View- Dependent Variations. The results clearly demonstrate the ...
- **p. 6 / 4. Experiments - extractive PDF cue:** The dataset's real-world imaging conditions, including severe occlusions and motion blur, make it particularly suited for testing segmentation robustness in complex environments.
- **p. 6 / 4.1. Experiments on LERF - extractive PDF cue:** In the kitchen scene, we specifically focus on the cabinet, a challenging object that other methods frequently fail to segment correctly.
- **p. 7 / 4.1. Experiments on LERF - extractive PDF cue:** Combining both ensures robust, discriminative 3D semantic segmentation in challenging scenes.

- **PDF anchors reviewed:** datasets p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (4.1. Experiments on LERF), p. 7 (4.1. Experiments on LERF), p. 8 (4.2. Experiments on 3D-OVS), p. 8 (4.2. Experiments on 3D-OVS), metrics p. 6 (4. Experiments), p. 6 (4.1. Experiments on LERF), p. 1 (Figure/Table caption), p. 7 (4.1. Experiments on LERF), p. 7 (4.1. Experiments on LERF), p. 8 (4.2. Experiments on 3D-OVS), baselines p. 7 (4.1. Experiments on LERF), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 6 (4.1. Experiments on LERF), p. 6 (4.1. Experiments on LERF), p. 8 (4.2. Experiments on 3D-OVS), results p. 6 (4.1. Experiments on LERF), p. 7 (4.1. Experiments on LERF), p. 8 (4.2. Experiments on 3D-OVS), p. 7 (4.1. Experiments on LERF), p. 8 (4.2. Experiments on 3D-OVS), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
