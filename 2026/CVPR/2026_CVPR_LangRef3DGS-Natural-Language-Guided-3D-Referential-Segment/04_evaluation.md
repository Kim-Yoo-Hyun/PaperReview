# Evaluation - LangRef3DGS: Natural Language-Guided 3D Referential Segmentation from Partial Observations via 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Ye_LangRef3DGS_Natural_Language-Guided_3D_Referential_Segmentation_from_Partial_Observations_via_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Ye_LangRef3DGS_Natural_Language-Guided_3D_Referential_Segmentation_from_Partial_Observations_via_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5.2.1. Quantitative Results), p. 6 (5.2.2. Qualitative Results), p. 7 (5.3. Ablation and Analysis), p. 7 (5.3. Ablation and Analysis), p. 8 (5.3. Ablation and Analysis), p. 8 (5.3. Ablation and Analysis)): Although our model improves performance in the dense-view setting, the relative gains become substantially larger under incompleteness.

## Evaluation Body Digest

- **p. 8 / 5.3. Ablation and Analysis - extractive body cue:** Qualitative results on four scenes from the LERF-OVS dataset under the partial-view setting, where 20% of RGB-D frames are removed.
- **p. 6 / 5.1. Experiment settings - extractive body cue:** To evaluate our framework across both object-centric and scene-level language-guided segmentation, we follow the dataset-specific protocols of LERF-Mask and LERF-OVS.
- **p. 6 / 5.1. Experiment settings - extractive body cue:** LERF-Mask focuses on objectcentric indoor scenes with clear boundaries, while LERFOVS introduces complex layouts, occlusions, and multiple referring expressions, enabling evaluation under ambiguous or partial ...
- **p. 7 / 5.3. Ablation and Analysis - extractive body cue:** Our method consistently outperforms existing approaches across both benchmarks.
- **p. 7 / 5.2.2. Qualitative Results - extractive body cue:** Performance comparison on the LERF-OVS dataset under the dense-view setting, where all RGB-D frames are available.
- **p. 8 / 5.3. Ablation and Analysis - extractive body cue:** 10% 60.5 81.2 20% 57.3 78.6 30% 54.0 75.5 40% 50.8 72.3 ness of our framework under partial observations, we analyze model performance on the ...
- **p. 7 / 5.3. Ablation and Analysis - extractive body cue:** Progressively adding these components, the ablation study provides a clear analysis of how each module influences our method's overall segmentation accuracy and robustness.
- **p. 7 / 5.3. Ablation and Analysis - extractive body cue:** Specifically, Table 4 presents the performance obtained when the Dirichlet Process (DP), Gradient LowRank (GLR), and Contrastive Graph Semantic Loss (CGSL) modules are gradually integrated ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.1. Experiment settings (p. 6); 5.2. Results (p. 6); 5.2.1. Quantitative Results (p. 6); 5.2.2. Qualitative Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2.1. Quantitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Although our model improves performance in the dense-view setting, the relative gains become substantially larger under incompleteness. | p. 6 (5.2.1. Quantitative Results) |
| 5.2.2. Qualitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Compared with prior methods, our results exhibit cleaner boundaries, fewer fragmented regions, and improved alignment with textual prompts. | p. 6 (5.2.2. Qualitative Results) |
| 5.3. Ablation and Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | GLR constraints further improve performance to 54.1/75.2, fostering stable, low-rank semantic representations. | p. 7 (5.3. Ablation and Analysis) |
| 5.3. Ablation and Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method consistently outperforms existing approaches across both benchmarks. | p. 7 (5.3. Ablation and Analysis) |
| 5.3. Ablation and Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | Modules are added progressively to the baseline, and results are reported in terms of mean Intersection-over-Union (mIoU) and mean Accuracy (mAcc). | p. 8 (5.3. Ablation and Analysis) |

## Dataset / Benchmark Role

- **p. 8 / 5.3. Ablation and Analysis - extractive body cue:** Qualitative results on four scenes from the LERF-OVS dataset under the partial-view setting, where 20% of RGB-D frames are removed.
- **p. 6 / 5.1. Experiment settings - extractive body cue:** To evaluate our framework across both object-centric and scene-level language-guided segmentation, we follow the dataset-specific protocols of LERF-Mask and LERF-OVS.
- **p. 6 / 5.1. Experiment settings - extractive body cue:** LERF-Mask focuses on objectcentric indoor scenes with clear boundaries, while LERFOVS introduces complex layouts, occlusions, and multiple referring expressions, enabling evaluation under ambiguous or partial ...
- **p. 7 / 5.3. Ablation and Analysis - extractive body cue:** Our method consistently outperforms existing approaches across both benchmarks.
- **p. 7 / 5.2.2. Qualitative Results - extractive body cue:** Performance comparison on the LERF-OVS dataset under the dense-view setting, where all RGB-D frames are available.
- **p. 8 / 5.3. Ablation and Analysis - extractive body cue:** 10% 60.5 81.2 20% 57.3 78.6 30% 54.0 75.5 40% 50.8 72.3 ness of our framework under partial observations, we analyze model performance on the ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Our proposed LangRef3D3S enables robust language- guided 3D segmentation from partial RGB-D observations. De- spite significant missing data (e.g., the stuffed bear, plate, ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the proposed framework. Our method leverages 3D Gaussian Splatting (3DGS) to construct a semantically continu- ous and differentiable embedding from partial ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Performance comparison on the LERF-Mask dataset under the dense-view setting, where all RGB-D frames are available.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Performance comparison on the LERF-OVS dataset under the dense-view setting, where all RGB-D frames are available.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Comparison on LERF-OVS under 20% view removal. Our method consistently outperforms existing approaches across both benchmarks.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative results on four scenes from the LERF-OVS dataset under the partial-view setting, where 20% of RGB-D frames are removed. Each subfigure shows ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Ablation study on LERF-OVS under 20% view removal. Modules are added progressively to the baseline, and results are re- ported in terms of ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Performance under different levels of partial views on LERF-OVS. A fraction of RGB-D frames is randomly removed during rendering to simulate missing viewpoints. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Qualitative results on four scenes from the LERF-OVS dataset under the partial-view setting, where 20% of RGB-D frames are removed. | embodiment, simulator version and control stack | p. 8 (5.3. Ablation and Analysis), p. 6 (5.1. Experiment settings) |
| Task/environment | To evaluate our framework across both object-centric and scene-level language-guided segmentation, we follow the dataset-specific protocols of LERF-Mask and LERF-OVS. | reset, timeout, object/scene variation | p. 6 (5.1. Experiment settings), p. 6 (5.1. Experiment settings) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 4 (4. Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Progressively adding these components, the ablation study provides a clear analysis of how each module influences our method's overall segmentation accuracy and robustness. | definition/direction/unit from same section | p. 7 (5.3. Ablation and Analysis) |
| Specifically, Table 4 presents the performance obtained when the Dirichlet Process (DP), Gradient LowRank (GLR), and Contrastive Graph Semantic Loss (CGSL) modules are gradually ... | definition/direction/unit from same section | p. 7 (5.3. Ablation and Analysis) |
| Adhering to its protocol, we use mIoU and mAcc to evaluate spatial alignment and per-class semantic accuracy. | definition/direction/unit from same section | p. 6 (5.1. Experiment settings) |
| For LERF-Mask, which emphasizes object-level understanding with dense pixel annotations, we report mean Intersection-over-Union (mIoU) and mean Binary IoU (mBIoU). | definition/direction/unit from same section | p. 6 (5.1. Experiment settings) |
| Nevertheless, our framework maintains stable accuracy across missing-view ratios. | definition/direction/unit from same section | p. 8 (5.3. Ablation and Analysis) |
| Modules are added progressively to the baseline, and results are reported in terms of mean Intersection-over-Union (mIoU) and mean Accuracy (mAcc). | definition/direction/unit from same section | p. 8 (5.3. Ablation and Analysis) |
| Figure 1. Our proposed LangRef3D3S enables robust language- guided 3D segmentation from partial RGB-D observations. De- spite significant missing data (e.g., the stuffed bear, ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 2. Overview of the proposed framework. Our method leverages 3D Gaussian Splatting (3DGS) to construct a semantically continu- ous and differentiable embedding from ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Metrics are averaged across scenes and prompts for fair, consistent comparison with baselines. | comparison identity and matched condition | p. 6 (5.1. Experiment settings) |
| Baseline (without DP/GLR/CGSL) 48.2 69.1 + Dirichlet Process (DP) 51.0 72.4 + Gradient Low-Rank (DP + GLR) 54.1 75.2 + Contrastive Graph Semantic Loss ... | comparison identity and matched condition | p. 8 (5.3. Ablation and Analysis) |
| Table 4. Ablation study on LERF-OVS under 20% view removal. Modules are added progressively to the baseline, and results are re- ported in terms ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Compared with prior methods, our results exhibit cleaner boundaries, fewer fragmented regions, and improved alignment with textual prompts. | comparison identity and matched condition | p. 6 (5.2.2. Qualitative Results) |
| Our method consistently outperforms existing approaches across both benchmarks. | comparison identity and matched condition | p. 7 (5.3. Ablation and Analysis) |
| Additionally, we will include detailed analyses and experiments, such as generalization performance, runtime efficiency, dense-view ablation studies, visual comparisons, and failure case analysis in ... | comparison identity and matched condition | p. 7 (5.2.2. Qualitative Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Overall, the incremental improvements observed across the ablation settings suggest that the three components-DP, GLR, and CGSL-provide complementary effects: DP supports flexible category allocation, ... | component/input/data sensitivity | p. 7 (5.3. Ablation and Analysis) |
| Table 4. Ablation study on LERF-OVS under 20% view removal. Modules are added progressively to the baseline, and results are re- ported in terms ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We conduct a series of ablation experiments on the LERFOVS dataset to thoroughly evaluate the individual contributions of each proposed component within our framework. | component/input/data sensitivity | p. 7 (5.3. Ablation and Analysis) |
| All visualizations use the partialview setting, where RGB-D observations are randomly removed to simulate occlusion or missing viewpoints. | component/input/data sensitivity | p. 6 (5.2.2. Qualitative Results) |
| We vary the ratio of removed frames from 10% to 40%, and summarize results in Table 5. | component/input/data sensitivity | p. 8 (5.3. Ablation and Analysis) |
| Under standard fully observed protocols, our two key components-the Dirichlet Process (DP) for adaptive clustering and the Gradient Low-Rank (GLR) mechanism for semantic refinement-consistently ... | component/input/data sensitivity | p. 6 (5.2.1. Quantitative Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address these challenges, we propose a novel framework built upon the powerful 3D scene representation of 3D Gaussian Splatting (3DGS) [18] that jointly ... | Although our model improves performance in the dense-view setting, the relative gains become substantially larger under incompleteness. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5.2.1. Quantitative Results), p. 6 (5.2.2. Qualitative Results), p. 7 (5.3. Ablation and Analysis), p. 7 (5.3. Ablation and Analysis), p. 8 (5.3. Ablation and Analysis), p. 8 (5.3. Ablation and Analysis) |
| Primary metric/result | Compared with prior methods, our results exhibit cleaner boundaries, fewer fragmented regions, and improved alignment with textual prompts. | numeric claim only at cited anchor | p. 6 (5.2.2. Qualitative Results) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Additionally, we will include detailed analyses and experiments, such as generalization performance, runtime efficiency, dense-view ablation studies, visual comparisons, and failure case analysis in ... | p. 7 (5.2.2. Qualitative Results) |
| body limitation/failure cue | Experiments on LERF-Mask and LERF-OVS demonstrate strong performance in both dense- and partial-view scenarios, with improved robustness to unseen or partially visible objects. | p. 8 (6. Conclusion) |
| body limitation/failure cue | Figure 1. Our proposed LangRef3D3S enables robust language- guided 3D segmentation from partial RGB-D observations. De- spite significant missing data (e.g., the stuffed bear, ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Figure 2. Overview of the proposed framework. Our method leverages 3D Gaussian Splatting (3DGS) to construct a semantically continu- ous and differentiable embedding from ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | All visualizations use the partialview setting, where RGB-D observations are randomly removed to simulate occlusion or missing viewpoints. | p. 6 (5.2.2. Qualitative Results) |
| body limitation/failure cue | Concretely, we achieve an mIoU of 79.6 and mBIoU of 74.9 on LERF-Mask, and an mIoU of 57.3 and mAcc of 78.6 on LERF-OVS, ... | p. 6 (5.2.1. Quantitative Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For brevity, detailed implementation parameters and hardware configurations are deferred to Appendix C. | p. 6 (5.1. Experiment settings) |
| Additionally, we will include detailed analyses and experiments, such as generalization performance, runtime efficiency, dense-view ablation studies, visual comparisons, and failure case analysis in ... | p. 7 (5.2.2. Qualitative Results) |
| The terms λ1 < λ2 are the two smallest distinct eigenvalues of S, and η denotes the learning rate. | p. 5 (4.3. Gradient Low-Rank Mechanism for Semantic) |
| (11), compute its approximate ELBO gain. | p. 4 (4.2. Triggering Novel Candidates via the Dirichlet) |
| The final semantic update rule is thus expressed as: Ft+1 = Ft -η ˜∇FL, (18) where ˜∇FL is periodically recomputed through a truncated singular ... | p. 5 (4.3. Gradient Low-Rank Mechanism for Semantic) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5.2.2. Qualitative Results - extractive body cue:** Additionally, we will include detailed analyses and experiments, such as generalization performance, runtime efficiency, dense-view ablation studies, visual comparisons, and failure case analysis in the ...
- **p. 8 / 6. Conclusion - extractive body cue:** Experiments on LERF-Mask and LERF-OVS demonstrate strong performance in both dense- and partial-view scenarios, with improved robustness to unseen or partially visible objects.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Our proposed LangRef3D3S enables robust language- guided 3D segmentation from partial RGB-D observations. De- spite significant missing data (e.g., the stuffed bear, plate, ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the proposed framework. Our method leverages 3D Gaussian Splatting (3DGS) to construct a semantically continu- ous and differentiable embedding from partial ...
- **p. 6 / 5.2.2. Qualitative Results - extractive body cue:** All visualizations use the partialview setting, where RGB-D observations are randomly removed to simulate occlusion or missing viewpoints.
- **p. 6 / 5.2.1. Quantitative Results - extractive body cue:** Concretely, we achieve an mIoU of 79.6 and mBIoU of 74.9 on LERF-Mask, and an mIoU of 57.3 and mAcc of 78.6 on LERF-OVS, demonstrating ...

- **Evidence anchors reviewed:** datasets p. 8 (5.3. Ablation and Analysis), p. 6 (5.1. Experiment settings), p. 6 (5.1. Experiment settings), p. 7 (5.3. Ablation and Analysis), p. 7 (5.2.2. Qualitative Results), p. 8 (5.3. Ablation and Analysis), metrics p. 7 (5.3. Ablation and Analysis), p. 7 (5.3. Ablation and Analysis), p. 6 (5.1. Experiment settings), p. 6 (5.1. Experiment settings), p. 8 (5.3. Ablation and Analysis), p. 8 (5.3. Ablation and Analysis), baselines p. 6 (5.1. Experiment settings), p. 8 (5.3. Ablation and Analysis), p. 8 (Figure/Table caption), p. 6 (5.2.2. Qualitative Results), p. 7 (5.3. Ablation and Analysis), p. 7 (5.2.2. Qualitative Results), results p. 6 (5.2.1. Quantitative Results), p. 6 (5.2.2. Qualitative Results), p. 7 (5.3. Ablation and Analysis), p. 7 (5.3. Ablation and Analysis), p. 8 (5.3. Ablation and Analysis), p. 8 (5.3. Ablation and Analysis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
