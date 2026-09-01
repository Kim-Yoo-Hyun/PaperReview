# Evaluation - PlaceIt3D: Language-Guided Object Placement in Real 3D Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5.1.1. Ablations), p. 8 (Figure/Table caption), p. 7 (5.1. Quantitative results), p. 7 (Figure/Table caption), p. 4 (3.2.2. Benchmark metrics), p. 4 (3.2.2. Benchmark metrics)): The inclusion of the anchor prediction head as an auxiliary sub-task also improves performance (row E vs row D).

## Evaluation Body Digest

- **p. 5 / 3.2.3. Benchmark statistics - extractive PDF cue:** PLACEIT3D-dataset-full has ∼4M examples: the 565 scenes x 140 objects x 50 prompts.
- **p. 4 / 3.2.3. Benchmark statistics - extractive PDF cue:** The benchmark contains 3,500 evaluation examples, combining a total of 142 different scenes from ScanNet [15] and 20 different assets from the PartObjaverse-Tiny 6648
- **p. 5 / 3.2.3. Benchmark statistics - extractive PDF cue:** The dataset consists of 100,505 training examples, sourced from 565 distinct ScanNet scenes and 20 unique assets.
- **p. 7 / 5. Experiments - extractive PDF cue:** We validate our method PLACEWIZARD for the task of language-guided object placement on the benchmark described in Section 3.2.
- **p. 4 / 3.2. PLACEIT3D-benchmark - extractive PDF cue:** Each benchmark example consists of a 3D scene mesh, a 3D asset, and a language prompt comprising one or more 3D placement constraints.
- **p. 7 / 5.1. Quantitative results - extractive PDF cue:** In the absence of prior work on language-guided 3D object placement in real scenes, we implemented two baselines by integrating OpenMask3D [46], an open vocabulary ...
- **p. 8 / 5.2. Qualitative Results - extractive PDF cue:** In Figure 4, we show the results of our method PLACEWIZARD on benchmark examples, demonstrating its ability to follow language instructions and satisfy constraints.
- **p. 8 / 5.1.1. Ablations - extractive PDF cue:** The inclusion of the anchor prediction head as an auxiliary sub-task also improves performance (row E vs row D).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3.2. PLACEIT3D-benchmark (p. 4); 3.2.2. Benchmark metrics (p. 4); 3.2.3. Benchmark statistics (p. 4); 5. Experiments (p. 7); 5.1. Quantitative results (p. 7); 5.2. Qualitative Results (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.1.1. Ablations | EMPIRICAL / SOURCE-REPORTED EVALUATION | The inclusion of the anchor prediction head as an auxiliary sub-task also improves performance (row E vs row D). | p. 8 (5.1.1. Ablations) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 4. Qualitative benchmark results. Colored highlights indicate anchors referenced in the textual prompts (predictions are generated entirely from point clouds, with anchor information ... | p. 8 (Figure/Table caption) |
| 5.1. Quantitative results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method, row G, consistently outperforms both baselines across all overall evaluation metrics. | p. 7 (5.1. Quantitative results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 2. Quantitative results: We compare our full method with variations where some components are removed. The results validate our design choices, and they ... | p. 7 (Figure/Table caption) |
| 3.2.2. Benchmark metrics | EMPIRICAL / SOURCE-REPORTED EVALUATION | To evaluate placement performance, we compute metrics that capture constraint validity overall and by subgroup: • Global Constraint Accuracy: The percentage of all constraints ... | p. 4 (3.2.2. Benchmark metrics) |

## Dataset / Benchmark Role

- **p. 5 / 3.2.3. Benchmark statistics - extractive PDF cue:** PLACEIT3D-dataset-full has ∼4M examples: the 565 scenes x 140 objects x 50 prompts.
- **p. 4 / 3.2.3. Benchmark statistics - extractive PDF cue:** The benchmark contains 3,500 evaluation examples, combining a total of 142 different scenes from ScanNet [15] and 20 different assets from the PartObjaverse-Tiny 6648
- **p. 5 / 3.2.3. Benchmark statistics - extractive PDF cue:** The dataset consists of 100,505 training examples, sourced from 565 distinct ScanNet scenes and 20 unique assets.
- **p. 7 / 5. Experiments - extractive PDF cue:** We validate our method PLACEWIZARD for the task of language-guided object placement on the benchmark described in Section 3.2.
- **p. 4 / 3.2. PLACEIT3D-benchmark - extractive PDF cue:** Each benchmark example consists of a 3D scene mesh, a 3D asset, and a language prompt comprising one or more 3D placement constraints.
- **p. 7 / 5.1. Quantitative results - extractive PDF cue:** In the absence of prior work on language-guided 3D object placement in real scenes, we implemented two baselines by integrating OpenMask3D [46], an open vocabulary ...
- **p. 8 / 5.2. Qualitative Results - extractive PDF cue:** In Figure 4, we show the results of our method PLACEWIZARD on benchmark examples, demonstrating its ability to follow language instructions and satisfy constraints.
- **p. 8 / 5.1.1. Ablations - extractive PDF cue:** The inclusion of the anchor prediction head as an auxiliary sub-task also improves performance (row E vs row D).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Language-guided 3D Object Placement in Real 3D Scenes: Given a text prompt, the task is to find a valid placement for an asset, ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. PLACEIT3D-dataset creation. Given a scene and an asset as input (a) the goal is to create a prompt (f) and corresponding mask M ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. PLACEWIZARD overview. A point encoder extracts features from the 3D scene, which are then complemented with positional embeddings. Spatial pooling reduces feature dimensions, ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1. Benchmark statistics for the number and types of lan- guage constraints per sample. Physical plausibility is evaluated in all samples and thus excluded ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Quantitative results: We compare our full method with variations where some components are removed. The results validate our design choices, and they show ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative benchmark results. Colored highlights indicate anchors referenced in the textual prompts (predictions are generated entirely from point clouds, with anchor information provided ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | PLACEIT3D-dataset-full has ∼4M examples: the 565 scenes x 140 objects x 50 prompts. | embodiment, simulator version and control stack | p. 5 (3.2.3. Benchmark statistics), p. 4 (3.2.3. Benchmark statistics) |
| Task/environment | The benchmark contains 3,500 evaluation examples, combining a total of 142 different scenes from ScanNet [15] and 20 different assets from the PartObjaverse-Tiny 6648 | reset, timeout, object/scene variation | p. 4 (3.2.3. Benchmark statistics), p. 5 (3.2.3. Benchmark statistics) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| To evaluate placement performance, we compute metrics that capture constraint validity overall and by subgroup: • Global Constraint Accuracy: The percentage of all constraints ... | definition/direction/unit from same section | p. 4 (3.2.2. Benchmark metrics) |
| Due to its frequent failure to accurately detect floor regions, we substitute in ground truth floor masks, while other anchor objects are selected based ... | definition/direction/unit from same section | p. 7 (5.1. Quantitative results) |
| Finally, the relatively low scores across all methods under the strictest evaluation metric, Complete Placement Success, which requires both physical plausibility and full adherence ... | definition/direction/unit from same section | p. 7 (5.1. Quantitative results) |
| This is a strict metric that reflects the robustness of the placement method under full constraint satisfaction. • Language Adherence Success: The percentage of ... | definition/direction/unit from same section | p. 4 (3.2.2. Benchmark metrics) |
| From Q′ and the input text, the LLM generates a response containing two special tokens, namely [LOC] and [SEG]. | definition/direction/unit from same section | p. 5 (3.2.3. Benchmark statistics) |
| Our method successfully follows language instructions and meets the specified constraints. | definition/direction/unit from same section | p. 8 (5.1.1. Ablations) |
| The bottom-right example demonstrates a failure case where one constraint is not met (highlighted in red). | definition/direction/unit from same section | p. 8 (5.1.1. Ablations) |
| Figure 2. PLACEIT3D-dataset creation. Given a scene and an asset as input (a) the goal is to create a prompt (f) and corresponding mask ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method, row G, consistently outperforms both baselines across all overall evaluation metrics. | comparison identity and matched condition | p. 7 (5.1. Quantitative results) |
| In the absence of prior work on language-guided 3D object placement in real scenes, we implemented two baselines by integrating OpenMask3D [46], an open ... | comparison identity and matched condition | p. 7 (5.1. Quantitative results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We describe the different variants below. | component/input/data sensitivity | p. 7 (5.1.1. Ablations) |
| This variant uses our proposed uniform spatial pooling approach instead of the original superpoints pooling. | component/input/data sensitivity | p. 7 (5.1.1. Ablations) |
| Figure 3. PLACEWIZARD overview. A point encoder extracts features from the 3D scene, which are then complemented with positional embeddings. Spatial pooling reduces feature ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| For the visibility constraint we use the same procedure as the benchmark, but use two approximations for efficiency: the asset is replaced by its ... | component/input/data sensitivity | p. 5 (3.2.3. Benchmark statistics) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To advance research in this area, we make three key contributions, summarized here: • We introduce PLACEIT3D-benchmark for languageguided placement with 3,500 evaluation examples, ... | The inclusion of the anchor prediction head as an auxiliary sub-task also improves performance (row E vs row D). | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5.1.1. Ablations), p. 8 (Figure/Table caption), p. 7 (5.1. Quantitative results), p. 7 (Figure/Table caption), p. 4 (3.2.2. Benchmark metrics), p. 4 (3.2.2. Benchmark metrics) |
| Primary metric/result | Figure 4. Qualitative benchmark results. Colored highlights indicate anchors referenced in the textual prompts (predictions are generated entirely from point clouds, with anchor information ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 3.2.3. Benchmark statistics - extractive PDF cue:** PLACEIT3D-dataset-full has ∼4M examples: the 565 scenes x 140 objects x 50 prompts.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our novel task formulation currently has several limitations. | p. 8 (6. Limitations and Future Work) |
| body limitation/failure cue | Despite these limitations, we believe our work lays the groundwork for further research in this area. | p. 8 (6. Limitations and Future Work) |
| body limitation/failure cue | Due to its frequent failure to accurately detect floor regions, we substitute in ground truth floor masks, while other anchor objects are selected based ... | p. 7 (5.1. Quantitative results) |
| body limitation/failure cue | In contrast, the rule-based system, which leverages both asset and scene meshes, can produce more plausible placements, albeit at the cost of expensive collision ... | p. 7 (5.1. Quantitative results) |
| body limitation/failure cue | This is a strict metric that reflects the robustness of the placement method under full constraint satisfaction. • Language Adherence Success: The percentage of ... | p. 4 (3.2.2. Benchmark metrics) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Implementation details are in the supplemental material. | p. 7 (5. Experiments) |
| We incorporate the asset encoder instead of only providing the asset dimensions in the text prompt to the LLM. | p. 7 (5.1.1. Ablations) |
| Finally, the use of our rotation head combined with passing the asset encoding as input to the decoder gives our final best-performing method (row ... | p. 8 (5.1.1. Ablations) |
| To evaluate placement performance, we compute metrics that capture constraint validity overall and by subgroup: • Global Constraint Accuracy: The percentage of all constraints ... | p. 4 (3.2.2. Benchmark metrics) |
| A point encoder [45] extracts features FX ∈RN×d from the input point cloud, where d is the feature dimension. | p. 5 (3.2.3. Benchmark statistics) |
| We then compute the asset height and footprint and, for each point on a horizontal surface, check if the placement is valid. | p. 5 (3.2.3. Benchmark statistics) |
| Instead, the information useful for placement should be encoded in the embeddings for the special tokens. | p. 6 (4.4. Losses) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Limitations and Future Work - extractive PDF cue:** Our novel task formulation currently has several limitations.
- **p. 8 / 6. Limitations and Future Work - extractive PDF cue:** Despite these limitations, we believe our work lays the groundwork for further research in this area.
- **p. 7 / 5.1. Quantitative results - extractive PDF cue:** Due to its frequent failure to accurately detect floor regions, we substitute in ground truth floor masks, while other anchor objects are selected based on ...
- **p. 7 / 5.1. Quantitative results - extractive PDF cue:** In contrast, the rule-based system, which leverages both asset and scene meshes, can produce more plausible placements, albeit at the cost of expensive collision checks ...
- **p. 4 / 3.2.2. Benchmark metrics - extractive PDF cue:** This is a strict metric that reflects the robustness of the placement method under full constraint satisfaction. • Language Adherence Success: The percentage of placements ...

- **PDF anchors reviewed:** datasets p. 5 (3.2.3. Benchmark statistics), p. 4 (3.2.3. Benchmark statistics), p. 5 (3.2.3. Benchmark statistics), p. 7 (5. Experiments), p. 4 (3.2. PLACEIT3D-benchmark), p. 7 (5.1. Quantitative results), metrics p. 4 (3.2.2. Benchmark metrics), p. 7 (5.1. Quantitative results), p. 7 (5.1. Quantitative results), p. 4 (3.2.2. Benchmark metrics), p. 5 (3.2.3. Benchmark statistics), p. 8 (5.1.1. Ablations), baselines p. 7 (5.1. Quantitative results), p. 7 (5.1. Quantitative results), results p. 8 (5.1.1. Ablations), p. 8 (Figure/Table caption), p. 7 (5.1. Quantitative results), p. 7 (Figure/Table caption), p. 4 (3.2.2. Benchmark metrics), p. 4 (3.2.2. Benchmark metrics).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
