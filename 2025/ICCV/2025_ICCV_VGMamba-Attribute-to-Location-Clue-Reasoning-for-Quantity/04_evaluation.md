# Evaluation - VGMamba: Attribute-to-Location Clue Reasoning for Quantity-Agnostic 3D Visual Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_VGMamba_Attribute-to-Location_Clue_Reasoning_for_Quantity-Agnostic_3D_Visual_Grounding_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_VGMamba_Attribute-to-Location_Clue_Reasoning_for_Quantity-Agnostic_3D_Visual_Grounding_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 8 (5.3. Ablation Studies), p. 6 (5.1.3. Baseline Comparison), p. 8 (5.3. Ablation Studies), p. 6 (5.1.3. Baseline Comparison), p. 7 (5.2.3. Baseline Comparison)): Table 4. Ablation study of proposed modules on Multi3DRefer. its intricate and free-form textual descriptions, which in- crease the difficulty of cross-modal alignment. Despite this, our method significantly outperforms alternatives ...

## Evaluation Body Digest

- **p. 5 / 5.1.1. Datasets and Evaluation Metrics - extractive body cue:** The ScanRefer dataset comprises 51,583 natural language descriptions for 11,046 objects across 800 3D scenes from the ScanNet dataset [8].
- **p. 6 / 5.1.1. Datasets and Evaluation Metrics - extractive body cue:** The Nr3D and Sr3D datasets, part of the ReferIt3D benchmark [1], are built upon the ScanNet dataset [8] for 3D visual grounding.
- **p. 5 / 5. Experiments - extractive body cue:** To evaluate the effectiveness of our proposed VGMamba on 3D Visual Grounding tasks with varying numbers of target objects, we conducted experiments on both single-object ...
- **p. 6 / 5.1.1. Datasets and Evaluation Metrics - extractive body cue:** The dataset is divided into two subsets: Unique, where the target object is the only instance of its class within the scene, and Multiple, where ...
- **p. 7 / 5.2.3. Baseline Comparison - extractive body cue:** The top two rows illustrate examples involving multiple target objects in complex scenes.
- **p. 7 / 5.2.1. Datasets and Evaluation Metrics - extractive body cue:** Multi3DRefer is a dataset derived from ScanRefer [3], comprising a total of 61,926 textual descriptions corresponding to 11,609 distinct objects.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** This shows IDM's effectiveness in handling multi-object grounding, enabling precise language-instructed grounding in complex scenes with multiple target objects.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** 5 illustrates the balance between computational complexity (FLOPs), inference speed, and grounding performance on the ScanRefer dataset.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 5); 5.1.1. Datasets and Evaluation Metrics (p. 5); 5.1.2. Implementation Details (p. 6); 5.2.1. Datasets and Evaluation Metrics (p. 7); 5.2.2. Implementation Details (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 4. Ablation study of proposed modules on Multi3DRefer. its intricate and free-form textual descriptions, which in- crease the difficulty of cross-modal alignment. Despite ... | p. 7 (Figure/Table caption) |
| 5.3. Ablation Studies | SYSTEM / EVALUATION SCOPE UNRESOLVED | VGMamba achieves the highest accuracy with significantly lower FLOPs than methods like Chat-Scene, demonstrating superior efficiency. | p. 8 (5.3. Ablation Studies) |
| 5.1.3. Baseline Comparison | SYSTEM / EVALUATION SCOPE UNRESOLVED | 1, with the following key observations: (i) Our method achieves state-of-the-art performance with an overall accuracy of 60.0% at IoU 0.25 and 53.9% at ... | p. 6 (5.1.3. Baseline Comparison) |
| 5.3. Ablation Studies | SYSTEM / EVALUATION SCOPE UNRESOLVED | Comparison of grounding performance between attribute first and location first model. formance gains across all metrics, with a notable increase in the MT case, ... | p. 8 (5.3. Ablation Studies) |
| 5.1.3. Baseline Comparison | SYSTEM / EVALUATION SCOPE UNRESOLVED | VGMamba achieves state-of-the-art performance of 68.3% and 81.3% on both datasets, surpassing prior state-of-the-art methods. | p. 6 (5.1.3. Baseline Comparison) |

## Dataset / Benchmark Role

- **p. 5 / 5.1.1. Datasets and Evaluation Metrics - extractive body cue:** The ScanRefer dataset comprises 51,583 natural language descriptions for 11,046 objects across 800 3D scenes from the ScanNet dataset [8].
- **p. 6 / 5.1.1. Datasets and Evaluation Metrics - extractive body cue:** The Nr3D and Sr3D datasets, part of the ReferIt3D benchmark [1], are built upon the ScanNet dataset [8] for 3D visual grounding.
- **p. 5 / 5. Experiments - extractive body cue:** To evaluate the effectiveness of our proposed VGMamba on 3D Visual Grounding tasks with varying numbers of target objects, we conducted experiments on both single-object ...
- **p. 6 / 5.1.1. Datasets and Evaluation Metrics - extractive body cue:** The dataset is divided into two subsets: Unique, where the target object is the only instance of its class within the scene, and Multiple, where ...
- **p. 7 / 5.2.3. Baseline Comparison - extractive body cue:** The top two rows illustrate examples involving multiple target objects in complex scenes.
- **p. 7 / 5.2.1. Datasets and Evaluation Metrics - extractive body cue:** Multi3DRefer is a dataset derived from ScanRefer [3], comprising a total of 61,926 textual descriptions corresponding to 11,609 distinct objects.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** This shows IDM's effectiveness in handling multi-object grounding, enabling precise language-instructed grounding in complex scenes with multiple target objects.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** 5 illustrates the balance between computational complexity (FLOPs), inference speed, and grounding performance on the ScanRefer dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. To achieve accurate 3D Visual Grounding, we explore two clues. First, we leverage the attribute clue to capture proposal objects. Then, a location ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. VGMamba for quantity-agnostic 3D Visual Grounding. Based on the given language description, we could utilize two clues to localize corresponding objects accurately, i.e., ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. The architecture of Instructive Dual-Mamba (IDM) for conducting multi-modal fusion. where Iglobal ∈Rn×m×d denotes the SSM output. As for the local communication, the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Comparison results on the ScanRefer [3] dataset, in terms of the accuracy evaluated by IoU 0.25 and IoU 0.5. Our proposed VGMamba performs ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Quantitative comparisons on Nr3D and Sr3D dataset. We have highlighted the top-performing three methods in purple.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative examples of the Multi3DRefer dataset. The results illustrate the grounding performance of M3DRef-CLIP (blue box), D-LISA (blue box), and our VGMamba(green box), ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Comparison of F1@0.5 results on the Multi3DRefer [42] validation set, where our method outperforms all baselines. the scene, enabling the model to understand ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Ablation study of proposed modules on Multi3DRefer. its intricate and free-form textual descriptions, which in- crease the difficulty of cross-modal alignment. Despite this, ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The ScanRefer dataset comprises 51,583 natural language descriptions for 11,046 objects across 800 3D scenes from the ScanNet dataset [8]. | embodiment, simulator version and control stack | p. 5 (5.1.1. Datasets and Evaluation Metrics), p. 6 (5.1.1. Datasets and Evaluation Metrics) |
| Task/environment | The Nr3D and Sr3D datasets, part of the ReferIt3D benchmark [1], are built upon the ScanNet dataset [8] for 3D visual grounding. | reset, timeout, object/scene variation | p. 6 (5.1.1. Datasets and Evaluation Metrics), p. 5 (5. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (3. Overview of State Space Models), p. 2 (3. Overview of State Space Models) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3. Overview of State Space Models), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 1, with the following key observations: (i) Our method achieves state-of-the-art performance with an overall accuracy of 60.0% at IoU 0.25 and 53.9% at ... | definition/direction/unit from same section | p. 6 (5.1.3. Baseline Comparison) |
| Adding LM enhances performance, particularly in the MT scenario, where the F1 score increases by 5.3%. | definition/direction/unit from same section | p. 7 (5.3. Ablation Studies) |
| Comparison of grounding performance between attribute first and location first model. formance gains across all metrics, with a notable increase in the MT case, ... | definition/direction/unit from same section | p. 8 (5.3. Ablation Studies) |
| Figure 5. Efficiency-Performance Trade-off on ScanRefer. 46.7%, surpassing the second-best competitor by 3.1%, which highlights its robustness in managing complex scenes with multiple potential ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 1. Comparison results on the ScanRefer [3] dataset, in terms of the accuracy evaluated by IoU 0.25 and IoU 0.5. Our proposed VGMamba ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Following [1], performance is evaluated using accuracy, measuring the proportion of correctly localized target objects. | definition/direction/unit from same section | p. 6 (5.1.1. Datasets and Evaluation Metrics) |
| The final prediction scores, generated by the Instructive Dual-Mamba block, are highlighted in red boxes. | definition/direction/unit from same section | p. 8 (5.4. Interpretability Analysis) |
| Figure 1. To achieve accurate 3D Visual Grounding, we explore two clues. First, we leverage the attribute clue to capture proposal objects. Then, a ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 1, with the following key observations: (i) Our method achieves state-of-the-art performance with an overall accuracy of 60.0% at IoU 0.25 and 53.9% at ... | comparison identity and matched condition | p. 6 (5.1.3. Baseline Comparison) |
| Table 3. Comparison of F1@0.5 results on the Multi3DRefer [42] validation set, where our method outperforms all baselines. the scene, enabling the model to ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Despite this, our method significantly outperforms alternatives that leverage large-scale 3D vision-language pre-training models [13, 44]. | comparison identity and matched condition | p. 7 (5.1.3. Baseline Comparison) |
| VGMamba effectively isolates and identifies the correct object, while baseline models struggle, often mistakenly including distractors in their predictions. | comparison identity and matched condition | p. 7 (5.2.3. Baseline Comparison) |
| One possible explanation is that attribute cues serve as more distinguishing priors compared to location cues, enabling the model to initially identify a larger ... | comparison identity and matched condition | p. 8 (5.3. Ablation Studies) |
| Table 1. Comparison results on the ScanRefer [3] dataset, in terms of the accuracy evaluated by IoU 0.25 and IoU 0.5. Our proposed VGMamba ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To validate the effectiveness of each proposed module within our VGMamba framework, we conduct ablation studies on the Multi3DRefer dataset, as shown in Tab. | component/input/data sensitivity | p. 7 (5.3. Ablation Studies) |
| More ablation results are detailed in supplementary. | component/input/data sensitivity | p. 7 (5.3. Ablation Studies) |
| A black chair without armrests, back to the window. | component/input/data sensitivity | p. 8 (5.3. Ablation Studies) |
| A wooden chair without arms is tucked under the table. | component/input/data sensitivity | p. 8 (5.3. Ablation Studies) |
| Following prior work [42], we employ a pre-trained PointGroup [17] module as the detector, which is fine-tuned on the ScanNet dataset. | component/input/data sensitivity | p. 6 (5.1.2. Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our chief contributions are threefold: • We explore a novel mechanism, i.e., attribute-to-location clue reasoning, for performing 3D visual grounding. • We propose a ... | Table 4. Ablation study of proposed modules on Multi3DRefer. its intricate and free-form textual descriptions, which in- crease the difficulty of cross-modal alignment. Despite ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 8 (5.3. Ablation Studies), p. 6 (5.1.3. Baseline Comparison), p. 8 (5.3. Ablation Studies), p. 6 (5.1.3. Baseline Comparison), p. 7 (5.2.3. Baseline Comparison) |
| Primary metric/result | VGMamba achieves the highest accuracy with significantly lower FLOPs than methods like Chat-Scene, demonstrating superior efficiency. | numeric claim only at cited anchor | p. 8 (5.3. Ablation Studies) |

- Numeric sentences retained from the body:
- **p. 5 / 5.1.1. Datasets and Evaluation Metrics - extractive body cue:** The ScanRefer dataset comprises 51,583 natural language descriptions for 11,046 objects across 800 3D scenes from the ScanNet dataset [8].

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | (iii) Unlike previous methods [13, 44] that show notable performance variations across settings, our VGMamba maintains consistently high accuracy, validating its robust generalization capability ... | p. 6 (5.1.3. Baseline Comparison) |
| body limitation/failure cue | 46.7%, surpassing the second-best competitor by 3.1%, which highlights its robustness in managing complex scenes with multiple potential matches. | p. 7 (5.2.3. Baseline Comparison) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The model is optimized using the AdamW optimizer with a batch size of 4 and a learning rate of 5e-4 with cosine decay scheduling. | p. 6 (5.1.2. Implementation Details) |
| We implement the proposed VGMamba model using PyTorch and train it end-to-end on a single NVIDIA A6000 GPU. | p. 6 (5.1.2. Implementation Details) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 5.1.3. Baseline Comparison - extractive body cue:** (iii) Unlike previous methods [13, 44] that show notable performance variations across settings, our VGMamba maintains consistently high accuracy, validating its robust generalization capability in ...
- **p. 7 / 5.2.3. Baseline Comparison - extractive body cue:** 46.7%, surpassing the second-best competitor by 3.1%, which highlights its robustness in managing complex scenes with multiple potential matches.

- **Evidence anchors reviewed:** datasets p. 5 (5.1.1. Datasets and Evaluation Metrics), p. 6 (5.1.1. Datasets and Evaluation Metrics), p. 5 (5. Experiments), p. 6 (5.1.1. Datasets and Evaluation Metrics), p. 7 (5.2.3. Baseline Comparison), p. 7 (5.2.1. Datasets and Evaluation Metrics), metrics p. 6 (5.1.3. Baseline Comparison), p. 7 (5.3. Ablation Studies), p. 8 (5.3. Ablation Studies), p. 7 (Figure/Table caption), p. 5 (Figure/Table caption), p. 6 (5.1.1. Datasets and Evaluation Metrics), baselines p. 6 (5.1.3. Baseline Comparison), p. 6 (Figure/Table caption), p. 7 (5.1.3. Baseline Comparison), p. 7 (5.2.3. Baseline Comparison), p. 8 (5.3. Ablation Studies), p. 5 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 8 (5.3. Ablation Studies), p. 6 (5.1.3. Baseline Comparison), p. 8 (5.3. Ablation Studies), p. 6 (5.1.3. Baseline Comparison), p. 7 (5.2.3. Baseline Comparison).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
