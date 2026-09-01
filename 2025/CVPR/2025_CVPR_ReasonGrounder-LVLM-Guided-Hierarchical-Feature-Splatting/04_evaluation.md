# Evaluation - ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Liu_ReasonGrounder_LVLM-Guided_Hierarchical_Feature_Splatting_for_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_ReasonGrounder_LVLM-Guided_Hierarchical_Feature_Splatting_for_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding), p. 8 (4.2. Evaluation on 3D Reasoning), p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding), p. 7 (4.2. Evaluation on 3D Reasoning), p. 8 (4.2. Evaluation on 3D Reasoning), p. 5 (4. Experiments)): Our results show that ReasonGrounder outperforms 2D-based methods like ODISE [35] and OV-Seg [25], and significantly surpasses 3D-based methods, including Method bed bench room sofa lawn overall LSeg [22] 56.0 ...

## Evaluation Body Digest

- **p. 5 / 4. Experiments - extractive PDF cue:** This paper introduces a novel dataset, ReasoningGD, which includes over 10K scenes of varying complexity and more than 263 types of common objects, with around ...
- **p. 7 / 4.2. Evaluation on 3D Reasoning - extractive PDF cue:** The ReasoningGD dataset introduced here includes scenes with amodal binary mask annotations, accurately representing the full shape of occluded objects from different views.
- **p. 7 / 4.2. Evaluation on 3D Reasoning - extractive PDF cue:** To test robustness, we selected five challenging scenes with small proportions, including multi-hierarchical structures and similar objects, along with ten text queries per scene from ...
- **p. 5 / 4. Experiments - extractive PDF cue:** The LERF dataset consists of 13 scenes, including in-the-wild scenarios and posed long-tail scenes.
- **p. 6 / 4.1. Evaluation on Open-set 3D Visual Grounding - extractive PDF cue:** Quantitative results of mean IoU (%) across various scenes in the LERF, 3D-OVS, and ReasoningGD datasets, including both scene-specific scores and overall performance.
- **p. 6 / 4.1. Evaluation on Open-set 3D Visual Grounding - extractive PDF cue:** Dataset Scene LERF ramen figurines teatime kitchen - overall 53.8 49.5 67.9 49.6 - 55.2 3D-OVS bed bench room sofa lawn overall 93.1 94.8 92.9 ...
- **p. 8 / 4.2. Evaluation on 3D Reasoning - extractive PDF cue:** The ReasoningGD dataset provides complete masks of occluded objects as ground truth, enabling quantitative evaluation. sonGrounder's evaluation on the LERF and ReasoningGD datasets in Figure ...
- **p. 8 / 4.2. Evaluation on 3D Reasoning - extractive PDF cue:** Qualitative results of amodal perception of novel views on the LERF and proposed ReasoningGD datasets.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Evaluation on Open-set 3D Visual Grounding (p. 6); 4.2. Evaluation on 3D Reasoning (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Evaluation on Open-set 3D Visual Grounding | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our results show that ReasonGrounder outperforms 2D-based methods like ODISE [35] and OV-Seg [25], and significantly surpasses 3D-based methods, including Method bed bench room ... | p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding) |
| 4.2. Evaluation on 3D Reasoning | EMPIRICAL / SOURCE-REPORTED EVALUATION | These results demonstrate that ReasonGrounder successfully achieves amodal perception, accurately localizing complete objects regardless of the occlusion level. | p. 8 (4.2. Evaluation on 3D Reasoning) |
| 4.1. Evaluation on Open-set 3D Visual Grounding | EMPIRICAL / SOURCE-REPORTED EVALUATION | Quantitative results of mean IoU (%) across various scenes in the LERF, 3D-OVS, and ReasoningGD datasets, including both scene-specific scores and overall performance. | p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding) |
| 4.2. Evaluation on 3D Reasoning | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 5, our method outperforms in all edge cases. | p. 7 (4.2. Evaluation on 3D Reasoning) |
| 4.2. Evaluation on 3D Reasoning | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our ReasonGrounder achieves accurate 3D localization, even when the object is partially visible or fully occluded in novel views. | p. 8 (4.2. Evaluation on 3D Reasoning) |

## Dataset / Benchmark Role

- **p. 5 / 4. Experiments - extractive PDF cue:** This paper introduces a novel dataset, ReasoningGD, which includes over 10K scenes of varying complexity and more than 263 types of common objects, with around ...
- **p. 7 / 4.2. Evaluation on 3D Reasoning - extractive PDF cue:** The ReasoningGD dataset introduced here includes scenes with amodal binary mask annotations, accurately representing the full shape of occluded objects from different views.
- **p. 7 / 4.2. Evaluation on 3D Reasoning - extractive PDF cue:** To test robustness, we selected five challenging scenes with small proportions, including multi-hierarchical structures and similar objects, along with ten text queries per scene from ...
- **p. 5 / 4. Experiments - extractive PDF cue:** The LERF dataset consists of 13 scenes, including in-the-wild scenarios and posed long-tail scenes.
- **p. 6 / 4.1. Evaluation on Open-set 3D Visual Grounding - extractive PDF cue:** Quantitative results of mean IoU (%) across various scenes in the LERF, 3D-OVS, and ReasoningGD datasets, including both scene-specific scores and overall performance.
- **p. 6 / 4.1. Evaluation on Open-set 3D Visual Grounding - extractive PDF cue:** Dataset Scene LERF ramen figurines teatime kitchen - overall 53.8 49.5 67.9 49.6 - 55.2 3D-OVS bed bench room sofa lawn overall 93.1 94.8 92.9 ...
- **p. 8 / 4.2. Evaluation on 3D Reasoning - extractive PDF cue:** The ReasoningGD dataset provides complete masks of occluded objects as ground truth, enabling quantitative evaluation. sonGrounder's evaluation on the LERF and ReasoningGD datasets in Figure ...
- **p. 8 / 4.2. Evaluation on 3D Reasoning - extractive PDF cue:** Qualitative results of amodal perception of novel views on the LERF and proposed ReasoningGD datasets.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Examples of open-vocabulary 3D visual grounding and reasoning. In a given scene, the user observes from a per- spective with occlusions and asks ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. The framework of our ReasonGrounder. Our ReasonGrounder leverages 3D Gaussian Splatting (3DGS) for efficient high- resolution rendering. It extracts 2D segmentation masks from ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. The pipeline of scale-hierarchical feature Gaussian field. The method extracts 2D masks from SAM and projects them into a 3D field. ReasonGrounder adds ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Localization Accuracy (%) on the LERF dataset for open-vocabulary 3D visual grounding. Our ReasonGrounder employs the same explicit queries as previous approaches.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Mean IoU (%) on LERF for open-vocabulary 3D vi- sual grounding. Our ReasonGrounder employs the same explicit queries as previous state-of-the-art approaches. is ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Mean IoU scores (%) on 3D-OVS dataset for open- vocabulary 3D visual grounding. The first three methods target 2D visual grounding, whereas the ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 4. Quantitative results of mean IoU (%) across vari- ous scenes in the LERF, 3D-OVS, and ReasoningGD datasets, including both scene-specific scores and overall ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative comparisons of open-vocabulary 3D visual grounding. Our ReasonGrounder demonstrates superior accuracy in open-vocabulary 3D localization compared to other state-of-the-art methods. It is ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This paper introduces a novel dataset, ReasoningGD, which includes over 10K scenes of varying complexity and more than 263 types of common objects, with ... | embodiment, simulator version and control stack | p. 5 (4. Experiments), p. 7 (4.2. Evaluation on 3D Reasoning) |
| Task/environment | The ReasoningGD dataset introduced here includes scenes with amodal binary mask annotations, accurately representing the full shape of occluded objects from different views. | reset, timeout, object/scene variation | p. 7 (4.2. Evaluation on 3D Reasoning), p. 7 (4.2. Evaluation on 3D Reasoning) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 6 (Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2. Mean IoU (%) on LERF for open-vocabulary 3D vi- sual grounding. Our ReasonGrounder employs the same explicit queries as previous state-of-the-art approaches. ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| The performance of ReasonGrounder is evaluated using two main metrics: Localization Accuracy [16] and Intersection over Union (IoU). | definition/direction/unit from same section | p. 5 (4. Experiments) |
| Quantitative results of mean IoU (%) across various scenes in the LERF, 3D-OVS, and ReasoningGD datasets, including both scene-specific scores and overall performance. | definition/direction/unit from same section | p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding) |
| Quantitative results of mean IoU scores (%) for amodal perception in novel views using the ReasoningGD dataset. | definition/direction/unit from same section | p. 8 (4.2. Evaluation on 3D Reasoning) |
| Our ReasonGrounder demonstrates superior accuracy in open-vocabulary 3D localization compared to other state-of-the-art methods. | definition/direction/unit from same section | p. 7 (4.2. Evaluation on 3D Reasoning) |
| Table 5. Quantitative results of mean IoU (%) across challenge scenes in the LERF and ReasoningGD datasets. This highlights the robustness of our ReasonGrounder ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Quantitative results from five typical scenes, shown in Table 6, demonstrate that ReasonGrounder excels in amodal perception, successfully localizing target objects even when occluded ... | definition/direction/unit from same section | p. 7 (4.2. Evaluation on 3D Reasoning) |
| Each scene is generated using the Blenderproc [10] toolkit and contains 100 RGB-D images, annotated with object labels, camera poses, and 2D modal and ... | definition/direction/unit from same section | p. 5 (4. Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our ReasonGrounder demonstrates superior accuracy in open-vocabulary 3D localization compared to other state-of-the-art methods. | comparison identity and matched condition | p. 7 (4.2. Evaluation on 3D Reasoning) |
| To further validate the performance of ReasonGrounder, we compare it with other 2D and 3D state-of-the-art methods on the 3D-OVS dataset (Table 3). | comparison identity and matched condition | p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding) |
| We show the superior quality of openvocabulary 3D visual grounding in ReasonGrounder compared to other methods in challenging and realistic 3D scenes. | comparison identity and matched condition | p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding) |
| As shown in Table 5, our method outperforms in all edge cases. | comparison identity and matched condition | p. 7 (4.2. Evaluation on 3D Reasoning) |
| Table 7. Ablation studies. The results are presented for two dif- ferent scenes: the Figurines scene from the LERF dataset and the 001 scene ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 7. Ablation studies. The results are presented for two dif- ferent scenes: the Figurines scene from the LERF dataset and the 001 scene ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Furthermore, we introduce a novel ReasoningGD dataset containing over 10K complex scenes and 263 object types, with a total of approximately 2 million annotations. | Our results show that ReasonGrounder outperforms 2D-based methods like ODISE [35] and OV-Seg [25], and significantly surpasses 3D-based methods, including Method bed bench room ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding), p. 8 (4.2. Evaluation on 3D Reasoning), p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding), p. 7 (4.2. Evaluation on 3D Reasoning), p. 8 (4.2. Evaluation on 3D Reasoning), p. 5 (4. Experiments) |
| Primary metric/result | These results demonstrate that ReasonGrounder successfully achieves amodal perception, accurately localizing complete objects regardless of the occlusion level. | numeric claim only at cited anchor | p. 8 (4.2. Evaluation on 3D Reasoning) |

- Numeric sentences retained from the body:
- **p. 5 / 4. Experiments - extractive PDF cue:** The LERF dataset consists of 13 scenes, including in-the-wild scenarios and posed long-tail scenes.
- **p. 5 / 4. Experiments - extractive PDF cue:** The scenes were captured using the Polycam iPhone app, employing on-board SLAM for camera pose estimation, and feature images with a resolution of 994×738.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 2. Mean IoU (%) on LERF for open-vocabulary 3D vi- sual grounding. Our ReasonGrounder employs the same explicit queries as previous state-of-the-art approaches. ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Figure 1. Examples of open-vocabulary 3D visual grounding and reasoning. In a given scene, the user observes from a per- spective with occlusions and ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | The dataset features multiple object instances with varying levels of occlusion, making it ideal for evaluating the ability in open-vocabulary 3D reasoning, grounding, and ... | p. 5 (4. Experiments) |
| body limitation/failure cue | Existing openvocabulary 3D visual grounding methods struggle with localizing complete objects in novel views with occlusion, limiting their real-world applicability. | p. 7 (4.2. Evaluation on 3D Reasoning) |
| body limitation/failure cue | To test robustness, we selected five challenging scenes with small proportions, including multi-hierarchical structures and similar objects, along with ten text queries per scene ... | p. 7 (4.2. Evaluation on 3D Reasoning) |
| body limitation/failure cue | This highlights the robustness of our ReasonGrounder in complex situations. | p. 8 (4.2. Evaluation on 3D Reasoning) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| no implementation/reproducibility sentence selected | verify appendix and code/project |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Mean IoU (%) on LERF for open-vocabulary 3D vi- sual grounding. Our ReasonGrounder employs the same explicit queries as previous state-of-the-art approaches. is ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Examples of open-vocabulary 3D visual grounding and reasoning. In a given scene, the user observes from a per- spective with occlusions and asks ...
- **p. 5 / 4. Experiments - extractive PDF cue:** The dataset features multiple object instances with varying levels of occlusion, making it ideal for evaluating the ability in open-vocabulary 3D reasoning, grounding, and amodal ...
- **p. 7 / 4.2. Evaluation on 3D Reasoning - extractive PDF cue:** Existing openvocabulary 3D visual grounding methods struggle with localizing complete objects in novel views with occlusion, limiting their real-world applicability.
- **p. 7 / 4.2. Evaluation on 3D Reasoning - extractive PDF cue:** To test robustness, we selected five challenging scenes with small proportions, including multi-hierarchical structures and similar objects, along with ten text queries per scene from ...
- **p. 8 / 4.2. Evaluation on 3D Reasoning - extractive PDF cue:** This highlights the robustness of our ReasonGrounder in complex situations.

- **PDF anchors reviewed:** datasets p. 5 (4. Experiments), p. 7 (4.2. Evaluation on 3D Reasoning), p. 7 (4.2. Evaluation on 3D Reasoning), p. 5 (4. Experiments), p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding), p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding), metrics p. 6 (Figure/Table caption), p. 5 (4. Experiments), p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding), p. 8 (4.2. Evaluation on 3D Reasoning), p. 7 (4.2. Evaluation on 3D Reasoning), p. 8 (Figure/Table caption), baselines p. 7 (4.2. Evaluation on 3D Reasoning), p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding), p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding), p. 7 (4.2. Evaluation on 3D Reasoning), p. 8 (Figure/Table caption), results p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding), p. 8 (4.2. Evaluation on 3D Reasoning), p. 6 (4.1. Evaluation on Open-set 3D Visual Grounding), p. 7 (4.2. Evaluation on 3D Reasoning), p. 8 (4.2. Evaluation on 3D Reasoning), p. 5 (4. Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
