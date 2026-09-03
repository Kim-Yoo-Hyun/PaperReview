# Evaluation - Grounded 3D-Aware Spatial Vision-Language Modeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Cheng_Grounded_3D-Aware_Spatial_Vision-Language_Modeling_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Cheng_Grounded_3D-Aware_Spatial_Vision-Language_Modeling_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (3.2. 3D Object Detection), p. 6 (3.3. Visual Question Answering), p. 7 (3.4. Implicit Grounding CoT), p. 7 (3.4. Implicit Grounding CoT), p. 8 (3.5. Analysis and Ablation Study), p. 5 (Figure/Table caption)): Compared with vision specialists, our model achieves competitive results overall and delivers notably better performance on indoor datasets.

## Evaluation Body Digest

- **p. 7 / 3.5. Analysis and Ablation Study - extractive body cue:** The Omni3D dataset is highly imbalanced [44], with far fewer outdoor training samples compared to indoor scenes.
- **p. 6 / 3.2. 3D Object Detection - extractive body cue:** We evaluate our model on the Omni3D test set, following the benchmark protocol and hyperparameters used in DetAny3D.
- **p. 7 / 3.5. Analysis and Ablation Study - extractive body cue:** It also naturally decomposes the task into two subproblems-2D grounding and 3D inference-where the former benefits from significantly larger amounts of training data across generic ...
- **p. 6 / 3. Experiments - extractive body cue:** 3.1), including the training stages and datasets used.
- **p. 8 / 3.5. Analysis and Ablation Study - extractive body cue:** Results on the MM-GCoT benchmark. "AF" and "GF" correspond to answer-first and grounding-first prompting settings.
- **p. 8 / 3.5. Analysis and Ablation Study - extractive body cue:** ATTRIBUTE JUDGEMENT OBJECT AVERAGE AccA ↑ AccG ↑ Cons. ↑ AccA ↑ AccG ↑ Cons. ↑ AccA ↑ AccG ↑ Cons. ↑ AccA ↑ AccG ...
- **p. 6 / 3.2. 3D Object Detection - extractive body cue:** The Omni3D benchmark reports Average Precision (AP), where predictions are matched to ground-truth using 3D IoU with thresholds ranging from 0.05 to 0.50.
- **p. 7 / 3.4. Implicit Grounding CoT - extractive body cue:** To study this, we evaluate our model on the MMGCoT [63] benchmark, which provides three key metrics: answer accuracy (A-Acc), grounding accuracy (G-Acc), and answer-grounding ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3. Experiments (p. 6); 3.1. Implementation Details (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 3.2. 3D Object Detection | SYSTEM / EVALUATION SCOPE UNRESOLVED | Compared with vision specialists, our model achieves competitive results overall and delivers notably better performance on indoor datasets. | p. 6 (3.2. 3D Object Detection) |
| 3.3. Visual Question Answering | SYSTEM / EVALUATION SCOPE UNRESOLVED | In contrast, Stage 2 finetuning focuses on learning the structure of CoT reasoning, and the results indicate that it does not significantly reduce general ... | p. 6 (3.3. Visual Question Answering) |
| 3.4. Implicit Grounding CoT | SYSTEM / EVALUATION SCOPE UNRESOLVED | We show results in Table 4, where our method outperforms baselines in all these metrics. | p. 7 (3.4. Implicit Grounding CoT) |
| 3.4. Implicit Grounding CoT | SYSTEM / EVALUATION SCOPE UNRESOLVED | In contrast, our model achieves higher performance while performing grounding automatically. | p. 7 (3.4. Implicit Grounding CoT) |
| 3.5. Analysis and Ablation Study | SYSTEM / EVALUATION SCOPE UNRESOLVED | Ablation study on the key components of GR3D-8B. "PT" denotes pretraining, "2D→3D" denotes 2D grounding followed by 3D prediction, and "Cam" denotes using normalized ... | p. 8 (3.5. Analysis and Ablation Study) |

## Dataset / Benchmark Role

- **p. 7 / 3.5. Analysis and Ablation Study - extractive body cue:** The Omni3D dataset is highly imbalanced [44], with far fewer outdoor training samples compared to indoor scenes.
- **p. 6 / 3.2. 3D Object Detection - extractive body cue:** We evaluate our model on the Omni3D test set, following the benchmark protocol and hyperparameters used in DetAny3D.
- **p. 7 / 3.5. Analysis and Ablation Study - extractive body cue:** It also naturally decomposes the task into two subproblems-2D grounding and 3D inference-where the former benefits from significantly larger amounts of training data across generic ...
- **p. 6 / 3. Experiments - extractive body cue:** 3.1), including the training stages and datasets used.
- **p. 8 / 3.5. Analysis and Ablation Study - extractive body cue:** Results on the MM-GCoT benchmark. "AF" and "GF" correspond to answer-first and grounding-first prompting settings.
- **p. 8 / 3.5. Analysis and Ablation Study - extractive body cue:** ATTRIBUTE JUDGEMENT OBJECT AVERAGE AccA ↑ AccG ↑ Cons. ↑ AccA ↑ AccG ↑ Cons. ↑ AccA ↑ AccG ↑ Cons. ↑ AccA ↑ AccG ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. GR3D overview. Top-Left: Spatial CoT enabled by 2D implicit grounding. Top-Middle: Region-prompted 3D grounding predicts camera-relative 3D boxes. Top-Right: Grounded 3D detection performs ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Method overview. GR3D builds on Region-VLMs by adding streaming region insertion for visual Chain-of-Thought reasoning. During CoT, the model repeatedly predicts a region, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Comparison on the Omni3D [32] benchmark between GR3D, vision specialists, and recent VLMs. We report AP15 and mAP for each dataset domain. GR3D ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. 2D detection results on the Omni3D benchmark. We report the mean Average Precision (mAP) for each dataset domain. yond sparse 3D-box labels. (i) ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Results on the BLINK-Depth benchmark for point-level region spatial understanding. Left: comparison with VLM base- lines. Right: visualization of one sample. Our method ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Performance comparison on general visual question answering and spatial reasoning benchmarks.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative results on 3D object detection. Our model produces accurate 3D bounding boxes on in-the-wild samples. whether the grounding genuinely contributes to correct ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Results on the MM-GCoT benchmark. "AF" and "GF" correspond to answer-first and grounding-first prompting settings. AccA, AccG, and Cons. refer to answer accuracy, ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The Omni3D dataset is highly imbalanced [44], with far fewer outdoor training samples compared to indoor scenes. | embodiment, simulator version and control stack | p. 7 (3.5. Analysis and Ablation Study), p. 6 (3.2. 3D Object Detection) |
| Task/environment | We evaluate our model on the Omni3D test set, following the benchmark protocol and hyperparameters used in DetAny3D. | reset, timeout, object/scene variation | p. 6 (3.2. 3D Object Detection), p. 7 (3.5. Analysis and Ablation Study) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (2.2.2. Implicit 2D Grounding), p. 3 (2.1. Foundational Spatial VLM) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The Omni3D benchmark reports Average Precision (AP), where predictions are matched to ground-truth using 3D IoU with thresholds ranging from 0.05 to 0.50. | definition/direction/unit from same section | p. 6 (3.2. 3D Object Detection) |
| To study this, we evaluate our model on the MMGCoT [63] benchmark, which provides three key metrics: answer accuracy (A-Acc), grounding accuracy (G-Acc), and ... | definition/direction/unit from same section | p. 7 (3.4. Implicit Grounding CoT) |
| AccA, AccG, and Cons. refer to answer accuracy, grounding accuracy, and consistency between them. | definition/direction/unit from same section | p. 8 (3.5. Analysis and Ablation Study) |
| Since our method explicitly separates 2D grounding from 3D prediction, we also evaluate 2D grounding performance on the Omni3D benchmark. | definition/direction/unit from same section | p. 6 (3.2. 3D Object Detection) |
| We additionally provide qualitative examples demonstrating that our model can accurately localize tiny regions and successfully handle point-level areas. | definition/direction/unit from same section | p. 7 (3.4. Implicit Grounding CoT) |
| Ablation study on the key components of GR3D-8B. "PT" denotes pretraining, "2D→3D" denotes 2D grounding followed by 3D prediction, and "Cam" denotes using normalized ... | definition/direction/unit from same section | p. 8 (3.5. Analysis and Ablation Study) |
| Table 2. 2D detection results on the Omni3D benchmark. We report the mean Average Precision (mAP) for each dataset domain. yond sparse 3D-box labels. ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Table 1. Comparison on the Omni3D [32] benchmark between GR3D, vision specialists, and recent VLMs. We report AP15 and mAP for each dataset domain. ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 4, where our model outperforms all VLM baselines. | comparison identity and matched condition | p. 6 (3.2. 3D Object Detection) |
| For comparison, we include both vision-specialist baselines (e.g., ImVoxelNet [41], Cube R-CNN [32], OVMono3D [43], and DetAny3D [44]) and VLM-based baselines (e.g., Qwen3VL-4B [45] ... | comparison identity and matched condition | p. 6 (3.2. 3D Object Detection) |
| The Omni3D dataset is highly imbalanced [44], with far fewer outdoor training samples compared to indoor scenes. | comparison identity and matched condition | p. 7 (3.5. Analysis and Ablation Study) |
| Table 1. Comparison on the Omni3D [32] benchmark between GR3D, vision specialists, and recent VLMs. We report AP15 and mAP for each dataset domain. ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Without this normalization, the model may lead to small but noticeable localization offsets in the predicted 3D boxes. | comparison identity and matched condition | p. 7 (3.5. Analysis and Ablation Study) |
| Ablation study on the key components of GR3D-8B. "PT" denotes pretraining, "2D→3D" denotes 2D grounding followed by 3D prediction, and "Cam" denotes using normalized ... | comparison identity and matched condition | p. 8 (3.5. Analysis and Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation study on the key components of GR3D-8B. "PT" denotes pretraining, "2D→3D" denotes 2D grounding followed by 3D prediction, and "Cam" denotes using normalized ... | component/input/data sensitivity | p. 8 (3.5. Analysis and Ablation Study) |
| We further analyze the effect of pointmap reconstruction as an auxiliary task for 3D detection. | component/input/data sensitivity | p. 7 (3.5. Analysis and Ablation Study) |
| 3.5 provides additional analysis and ablation studies of the model's 3D detection performance. | component/input/data sensitivity | p. 6 (3. Experiments) |
| We evaluate two variants of our model: one after spatial pre-training and one after CoT finetuning. | component/input/data sensitivity | p. 6 (3.3. Visual Question Answering) |
| Without this normalization, the model may lead to small but noticeable localization offsets in the predicted 3D boxes. | component/input/data sensitivity | p. 7 (3.5. Analysis and Ablation Study) |
| Figure 3. Results on the BLINK-Depth benchmark for point-level region spatial understanding. Left: comparison with VLM base- lines. Right: visualization of one sample. Our ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce both explicit and implicit forms of grounding, designed to strengthen the spatial reasoning capacity of the vision-language model. | Compared with vision specialists, our model achieves competitive results overall and delivers notably better performance on indoor datasets. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (3.2. 3D Object Detection), p. 6 (3.3. Visual Question Answering), p. 7 (3.4. Implicit Grounding CoT), p. 7 (3.4. Implicit Grounding CoT), p. 8 (3.5. Analysis and Ablation Study), p. 5 (Figure/Table caption) |
| Primary metric/result | In contrast, Stage 2 finetuning focuses on learning the structure of CoT reasoning, and the results indicate that it does not significantly reduce general ... | numeric claim only at cited anchor | p. 6 (3.3. Visual Question Answering) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This makes its 3D predictions unstable under changes in image size. | p. 6 (3.2. 3D Object Detection) |
| body limitation/failure cue | In contrast, Stage 2 finetuning focuses on learning the structure of CoT reasoning, and the results indicate that it does not significantly reduce general ... | p. 6 (3.3. Visual Question Answering) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In this section, we begin by describing the implementation details (Sec. | p. 6 (3. Experiments) |
| During this stage, we freeze the visual encoder and train the remaining modules. | p. 6 (3.1. Implementation Details) |
| The base NVILA encoder extracts dense visual tokens from an RGB image for single-view inputs. | p. 3 (2.1. Foundational Spatial VLM) |
| In addition, we preserve the region-prompt design used in SR-3D: specific image regions can be encoded as individual query tokens by pooling features within ... | p. 3 (2.1. Foundational Spatial VLM) |
| The region's visual features are pooled and encoded into a region token, which is fused into the text stream to guide 3D box prediction. | p. 4 (2.3. Monocular 3D Grounding via Region Prompt) |
| The model first predicts coordinates, then encodes the predicted region to obtain its embedding, which is inserted back into the ongoing sequence before the ... | p. 4 (2.2.2. Implicit 2D Grounding) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 3.2. 3D Object Detection - extractive body cue:** This makes its 3D predictions unstable under changes in image size.
- **p. 6 / 3.3. Visual Question Answering - extractive body cue:** In contrast, Stage 2 finetuning focuses on learning the structure of CoT reasoning, and the results indicate that it does not significantly reduce general VQA ...

- **Evidence anchors reviewed:** datasets p. 7 (3.5. Analysis and Ablation Study), p. 6 (3.2. 3D Object Detection), p. 7 (3.5. Analysis and Ablation Study), p. 6 (3. Experiments), p. 8 (3.5. Analysis and Ablation Study), p. 8 (3.5. Analysis and Ablation Study), metrics p. 6 (3.2. 3D Object Detection), p. 7 (3.4. Implicit Grounding CoT), p. 8 (3.5. Analysis and Ablation Study), p. 6 (3.2. 3D Object Detection), p. 7 (3.4. Implicit Grounding CoT), p. 8 (3.5. Analysis and Ablation Study), baselines p. 6 (3.2. 3D Object Detection), p. 6 (3.2. 3D Object Detection), p. 7 (3.5. Analysis and Ablation Study), p. 5 (Figure/Table caption), p. 7 (3.5. Analysis and Ablation Study), p. 8 (3.5. Analysis and Ablation Study), results p. 6 (3.2. 3D Object Detection), p. 6 (3.3. Visual Question Answering), p. 7 (3.4. Implicit Grounding CoT), p. 7 (3.4. Implicit Grounding CoT), p. 8 (3.5. Analysis and Ablation Study), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
