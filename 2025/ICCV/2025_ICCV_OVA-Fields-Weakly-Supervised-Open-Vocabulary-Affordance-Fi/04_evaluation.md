# Evaluation - OVA-Fields: Weakly Supervised Open-Vocabulary Affordance Fields for Robot Operational Part Detection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Su_OVA-Fields_Weakly_Supervised_Open-Vocabulary_Affordance_Fields_for_Robot_Operational_Part_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Su_OVA-Fields_Weakly_Supervised_Open-Vocabulary_Affordance_Fields_for_Robot_Operational_Part_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5. Real Robot Experiments), p. 6 (4.3. Ablation Study), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (4.3. Ablation Study), p. 5 (4.2. Numerical and Visual Comparisons)): The case of "grab the cup" reveals that although affordance detection reaches 90% spatial accuracy, the current pipeline achieves a 20% success rate for containers requiring specific approach angles.

## Evaluation Body Digest

- **p. 5 / 4.1. Experiment Settings - extractive body cue:** Our experimental dataset comprises multi-source RGB-D sequences captured using consumer-grade devices (Apple iPad Pro with LiDAR) and benchmark datasets to systematically evaluate cross-environment generalization.
- **p. 5 / 4.1. Experiment Settings - extractive body cue:** The data collection protocol integrates first-person-view captures from two real-world environments (home and lab scenes) with three ScanNet [3] scenes (kitchen, living room, office) and ...
- **p. 6 / 4.3. Ablation Study - extractive body cue:** This shows that the SR module is crucial for improving affordance detection accuracy for detecting smaller items, probably making it better suited for real-world robotic ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** The experiments are conducted based on real-world scenes with many kinds of objects, such as refrigerators, laptops, knives, bottles, cups, microwaves, and so on.
- **p. 8 / 5. Real Robot Experiments - extractive body cue:** Real robot quantitative results. transformation matrix to map all point cloud coordinates to the real-world coordinate system.
- **p. 6 / 4.3. Ablation Study - extractive body cue:** The performance gap demonstrates that the hierarchical integration of semantic and visual features significantly improves affordance detection robustness in real-world environments.
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Our model demonstrates superior localization of actionable regions, particularly in real scenes with small or fine-grained objects.
- **p. 8 / 5. Real Robot Experiments - extractive body cue:** Success rates of the real robot for different objects and semantic complexity levels.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experiment Settings (p. 5); 5. Real Robot Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5. Real Robot Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The case of "grab the cup" reveals that although affordance detection reaches 90% spatial accuracy, the current pipeline achieves a 20% success rate for ... | p. 8 (5. Real Robot Experiments) |
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | The performance gap demonstrates that the hierarchical integration of semantic and visual features significantly improves affordance detection robustness in real-world environments. | p. 6 (4.3. Ablation Study) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2. Performance comparison of various models on the Affordance detection task for different objects. From these two indicators, the OVA-Fields consistently outperforms the ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6. Success rates of the real robot for different objects and semantic complexity levels. Although achieving success 80% in grab pen tasks through ... | p. 8 (Figure/Table caption) |
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | All variants share identical training protocols on the Lab and Home dataset and are evaluated on two metrics: mIoU and instruction grounding accuracy (the ... | p. 7 (4.3. Ablation Study) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experiment Settings - extractive body cue:** Our experimental dataset comprises multi-source RGB-D sequences captured using consumer-grade devices (Apple iPad Pro with LiDAR) and benchmark datasets to systematically evaluate cross-environment generalization.
- **p. 5 / 4.1. Experiment Settings - extractive body cue:** The data collection protocol integrates first-person-view captures from two real-world environments (home and lab scenes) with three ScanNet [3] scenes (kitchen, living room, office) and ...
- **p. 6 / 4.3. Ablation Study - extractive body cue:** This shows that the SR module is crucial for improving affordance detection accuracy for detecting smaller items, probably making it better suited for real-world robotic ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** The experiments are conducted based on real-world scenes with many kinds of objects, such as refrigerators, laptops, knives, bottles, cups, microwaves, and so on.
- **p. 8 / 5. Real Robot Experiments - extractive body cue:** Real robot quantitative results. transformation matrix to map all point cloud coordinates to the real-world coordinate system.
- **p. 6 / 4.3. Ablation Study - extractive body cue:** The performance gap demonstrates that the hierarchical integration of semantic and visual features significantly improves affordance detection robustness in real-world environments.
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Our model demonstrates superior localization of actionable regions, particularly in real scenes with small or fine-grained objects.
- **p. 8 / 5. Real Robot Experiments - extractive body cue:** Success rates of the real robot for different objects and semantic complexity levels.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The OVA-Fields Framework. Our framework directly maps the user's open-vocabulary semantic queries to actionable affordance locations in the complex 3D scenes, allowing robots ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Method Overview. OVA-Fields integrates feature fusion and training in three key steps. First, the Multi-modal Affordance Perception (MAP) module extracts visual and affordance ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Comparison results of different affordance detection models. * denotes adjusted models. Best results are highlighted in bold. Refrigerator Laptop Cup mIoU mPrec mIoU ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Performance comparison of various models on the Affordance detection task for different objects. From these two indicators, the OVA-Fields consistently outperforms the baselines, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Ablation study results. The impact of different compo- nents on the OVA-Fields' performance in Lab and Home scenes. mIoU Instruction Acc. Geo-Only 52.3 ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 4. Effectiveness of dynamic feature arbitration. Our dy- namic weighting shows that static blending fails to handle feature conflicts in open-vocabulary settings. Notably, pure ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative comparison of affordance detection results across various models. The experiments are conducted based on real-world scenes with many kinds of objects, such ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Comparison of the small object processing procedure in the ablation study. a systematic ablation study on the dynamic weight mecha- nism by comparing ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our experimental dataset comprises multi-source RGB-D sequences captured using consumer-grade devices (Apple iPad Pro with LiDAR) and benchmark datasets to systematically evaluate cross-environment generalization. | embodiment, simulator version and control stack | p. 5 (4.1. Experiment Settings), p. 5 (4.1. Experiment Settings) |
| Task/environment | The data collection protocol integrates first-person-view captures from two real-world environments (home and lab scenes) with three ScanNet [3] scenes (kitchen, living room, office) ... | reset, timeout, object/scene variation | p. 5 (4.1. Experiment Settings), p. 6 (4.3. Ablation Study) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 3 (3.2. Spatial Feature Extraction and Feature Fusion), p. 2 (1. Introduction) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 4 (3.2. Spatial Feature Extraction and Feature Fusion), p. 5 (3.3. Query Mapping) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| All variants share identical training protocols on the Lab and Home dataset and are evaluated on two metrics: mIoU and instruction grounding accuracy (the ... | definition/direction/unit from same section | p. 7 (4.3. Ablation Study) |
| The case of "grab the cup" reveals that although affordance detection reaches 90% spatial accuracy, the current pipeline achieves a 20% success rate for ... | definition/direction/unit from same section | p. 8 (5. Real Robot Experiments) |
| 5), achieving a 90% success rate in refrigerator door opening tasks. | definition/direction/unit from same section | p. 8 (5. Real Robot Experiments) |
| 3 demonstrate OVA-Fields' exceptional precision in detecting affordances like refrigerator handles (average contact surface < 0.02m²), while baseline methods fail to achieve comparable accuracy ... | definition/direction/unit from same section | p. 5 (4.2. Numerical and Visual Comparisons) |
| 2, the results demonstrate that integrating semantic embeddings with geometric encoding enhances the model's ability to identify affordances with greater accuracy. | definition/direction/unit from same section | p. 5 (4.2. Numerical and Visual Comparisons) |
| The performance gap demonstrates that the hierarchical integration of semantic and visual features significantly improves affordance detection robustness in real-world environments. | definition/direction/unit from same section | p. 6 (4.3. Ablation Study) |
| This shows that the SR module is crucial for improving affordance detection accuracy for detecting smaller items, probably making it better suited for real-world ... | definition/direction/unit from same section | p. 6 (4.3. Ablation Study) |
| Our model demonstrates superior localization of actionable regions, particularly in real scenes with small or fine-grained objects. | definition/direction/unit from same section | p. 7 (4.3. Ablation Study) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In the context of fine-grained affordance detection, our model consistently outperforms baseline approaches. | comparison identity and matched condition | p. 5 (4.2. Numerical and Visual Comparisons) |
| From these two indicators, the OVA-Fields consistently outperforms the baselines, particularly in fine-grained affordances of small objects such as cups. | comparison identity and matched condition | p. 6 (4.2. Numerical and Visual Comparisons) |
| When processing "Take out some food from the refrigerator", the system identifies fridge handles with 4.7s average response time, significantly outperforming geometric baselines. | comparison identity and matched condition | p. 8 (5. Real Robot Experiments) |
| 1 reveals 3.4× mIoU improvements over the best baseline (52.4% vs. | comparison identity and matched condition | p. 5 (4.2. Numerical and Visual Comparisons) |
| Comparison of the small object processing procedure in the ablation study. a systematic ablation study on the dynamic weight mechanism by comparing four variants ... | comparison identity and matched condition | p. 7 (4.3. Ablation Study) |
| Comparison results of different affordance detection models. * denotes adjusted models. | comparison identity and matched condition | p. 6 (4.2. Numerical and Visual Comparisons) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Comparison of the small object processing procedure in the ablation study. a systematic ablation study on the dynamic weight mechanism by comparing four variants ... | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| To evaluate the effectiveness of our small object handling mechanism, we conduct a comparative experiment by studying the OVAFields' performance with and without the ... | component/input/data sensitivity | p. 6 (4.3. Ablation Study) |
| Table 4. Effectiveness of dynamic feature arbitration. Our dy- namic weighting shows that static blending fails to handle feature conflicts in open-vocabulary settings. Notably, ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| All variants share identical training protocols on the Lab and Home dataset and are evaluated on two metrics: mIoU and instruction grounding accuracy (the ... | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| For ClosedSet Affordance Detection Model (3D AffordanceNet [5], Mask3D [31]), we adjust Mask3D's architectures while preserving its core mechanisms and replace Mask3D's output head ... | component/input/data sensitivity | p. 5 (4.1. Experiment Settings) |
| For Open-Vocabulary Affordance Detection Models (OpenAD [36], OpenMask3D [35], CLIP-Fields [32], OpenScene [26], CLIP-FO3D [45]), we maintain OpenMask3D's and CLIP-Fields's original architectures but unify ... | component/input/data sensitivity | p. 5 (4.1. Experiment Settings) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Here, we introduce our framework, OVA-Fields, which enables accurate affordance detection in 3D scenes based on natural language queries. | The case of "grab the cup" reveals that although affordance detection reaches 90% spatial accuracy, the current pipeline achieves a 20% success rate for ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5. Real Robot Experiments), p. 6 (4.3. Ablation Study), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (4.3. Ablation Study), p. 5 (4.2. Numerical and Visual Comparisons) |
| Primary metric/result | The performance gap demonstrates that the hierarchical integration of semantic and visual features significantly improves affordance detection robustness in real-world environments. | numeric claim only at cited anchor | p. 6 (4.3. Ablation Study) |

- Numeric sentences retained from the body:
- **p. 8 / 5. Real Robot Experiments - extractive body cue:** When processing "Take out some food from the refrigerator", the system identifies fridge handles with 4.7s average response time, significantly outperforming geometric baselines.
- **p. 8 / 5. Real Robot Experiments - extractive body cue:** For ambiguous queries like "I want to cook the chicken", it correctly activates microwave handle affordances within 3.2s, demonstrating 80% intent inference accuracy across 10 ...
- **p. 8 / 5. Real Robot Experiments - extractive body cue:** For example, "Open the refrigerator" (Level 1) achieves 100% success (10/10 trials), while context-dependent instructions like "Find a snack for my lunch" (Level 3) drop ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The key limitations emerge in handling articulated objects (e.g., doors/drawers). | p. 8 (6. Conclusion) |
| body limitation/failure cue | Although grasp positions are reliably detected, the current implementation cannot infer required force application directions or kinematic movement patterns essential for operating hinge-based mechanisms. | p. 8 (6. Conclusion) |
| body limitation/failure cue | This approach demonstrates particular strength in multimodal feature fusion, as 89.3% of failure cases in singlemodality baselines result from either geometric oversimplification or semantic ... | p. 5 (4.2. Numerical and Visual Comparisons) |
| body limitation/failure cue | Our dynamic weighting shows that static blending fails to handle feature conflicts in open-vocabulary settings. | p. 6 (4.3. Ablation Study) |
| body limitation/failure cue | The method maintains robustness under ScanNet's realworld noise conditions, achieving 27.6% precision at 13.2% mIoU compared to CLIP-FO3D's 21.2% precision with 15.3% mIoU. | p. 5 (4.2. Numerical and Visual Comparisons) |
| body limitation/failure cue | Figure 2. Method Overview. OVA-Fields integrates feature fusion and training in three key steps. First, the Multi-modal Affordance Perception (MAP) module extracts visual and ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| OpenScene and CLIPFO3D are adjusted with frozen encoders and retrained projections using our affordance labels. | p. 5 (4.1. Experiment Settings) |
| Ours: Adaptive α computed via wj i . | p. 7 (4.3. Ablation Study) |
| For example, "Open the refrigerator" (Level 1) achieves 100% success (10/10 trials), while context-dependent instructions like "Find a snack for my lunch" (Level 3) ... | p. 8 (5. Real Robot Experiments) |
| The scaled values H are then passed through a sigmoid function to compute the final weight, ensuring balanced training responses across regions. | p. 3 (3.1. Multi-Modal Affordance Perception) |
| Using a pre-trained CLIP model [28], visual embeddings are computed for each bounding box, embedding both object and spatial information into the 3D scene. | p. 3 (3.1. Multi-Modal Affordance Perception) |
| OVA-Fields integrates feature fusion and training in three key steps. | p. 4 (3.2. Spatial Feature Extraction and Feature Fusion) |
| Next, a Multiresolution Hash Encoder [20] and Multi-Head Attention combine spatial coordinates with affordance features into a unified space (Sec. | p. 4 (3.2. Spatial Feature Extraction and Feature Fusion) |
| User queries are encoded into a vector vq using Sentence-BERT. | p. 5 (3.3. Query Mapping) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive body cue:** The key limitations emerge in handling articulated objects (e.g., doors/drawers).
- **p. 8 / 6. Conclusion - extractive body cue:** Although grasp positions are reliably detected, the current implementation cannot infer required force application directions or kinematic movement patterns essential for operating hinge-based mechanisms.
- **p. 5 / 4.2. Numerical and Visual Comparisons - extractive body cue:** This approach demonstrates particular strength in multimodal feature fusion, as 89.3% of failure cases in singlemodality baselines result from either geometric oversimplification or semantic ambiguity.
- **p. 6 / 4.3. Ablation Study - extractive body cue:** Our dynamic weighting shows that static blending fails to handle feature conflicts in open-vocabulary settings.
- **p. 5 / 4.2. Numerical and Visual Comparisons - extractive body cue:** The method maintains robustness under ScanNet's realworld noise conditions, achieving 27.6% precision at 13.2% mIoU compared to CLIP-FO3D's 21.2% precision with 15.3% mIoU.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Method Overview. OVA-Fields integrates feature fusion and training in three key steps. First, the Multi-modal Affordance Perception (MAP) module extracts visual and affordance ...

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Experiment Settings), p. 5 (4.1. Experiment Settings), p. 6 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 8 (5. Real Robot Experiments), p. 6 (4.3. Ablation Study), metrics p. 7 (4.3. Ablation Study), p. 8 (5. Real Robot Experiments), p. 8 (5. Real Robot Experiments), p. 5 (4.2. Numerical and Visual Comparisons), p. 5 (4.2. Numerical and Visual Comparisons), p. 6 (4.3. Ablation Study), baselines p. 5 (4.2. Numerical and Visual Comparisons), p. 6 (4.2. Numerical and Visual Comparisons), p. 8 (5. Real Robot Experiments), p. 5 (4.2. Numerical and Visual Comparisons), p. 7 (4.3. Ablation Study), p. 6 (4.2. Numerical and Visual Comparisons), results p. 8 (5. Real Robot Experiments), p. 6 (4.3. Ablation Study), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (4.3. Ablation Study), p. 5 (4.2. Numerical and Visual Comparisons).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
