# Evaluation - DiSCO-3D : Discovering and Segmenting Sub-Concepts from Open-vocabulary Queries in NeRF

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Petit_DiSCO-3D__Discovering_and_Segmenting_Sub-Concepts_from_Open-vocabulary_Queries_in_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Petit_DiSCO-3D__Discovering_and_Segmenting_Sub-Concepts_from_Open-vocabulary_Queries_in_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2.1. Evaluated methods), p. 7 (4.2.3. Ablations studies), p. 5 (4.1. Implementation and evaluation details), p. 7 (4.2.2. Results), p. 5 (4. Experimental evaluations), p. 6 (4.2.2. Results)): Notice that the only difference between DiSCO-3D and those baselines relies on the fact that DiSCO-3D achieves USS and OVSeg jointly whereas the latters achieve it successively.

## Evaluation Body Digest

- **p. 7 / 4.2.2. Results - extractive body cue:** We also display some qualitative examples in Figure 3 across various scenes (both indoor and outdoor from various datasets [12, 21, 33]), feature fields (LeRF ...
- **p. 6 / 4.1. Implementation and evaluation details - extractive body cue:** Segmentation quality is evaluated by first matching discovered sub-concepts to the dataset-defined sub-concepts (we match predictions with all of the scene's classes) using embeddings distances.
- **p. 7 / 4.2.2. Results - extractive body cue:** However, the benchmark is still far from being saturated, showing the difficulty of the task and the room for future improvements.
- **p. 5 / 4. Experimental evaluations - extractive body cue:** After introducing some implementation and evaluation details in subsection 4.1, we first present evaluations on the novel Open-Vocabulary Sub-concepts Discovery problem with a dedicated benchmark ...
- **p. 6 / 4.1. Implementation and evaluation details - extractive body cue:** We introduce an extension of the Replica [33] dataset for Open-Vocabulary Sub-concepts Discovery.
- **p. 7 / 4.2.3. Ablations studies - extractive body cue:** First, we observe that the complete model's performance remains stable in both segmentation accuracy and the numFF Method PCLIP Hungarian PQ ↑ mIoU ↑ mAcc ...
- **p. 6 / 4.1. Implementation and evaluation details - extractive body cue:** This enables comparison with the groundtruth query segmentation to compute classic segmentation metrics: Mean Accuracy (mAcc) and mean Intersection over Union (mIoU).
- **p. 7 / 4.2.3. Ablations studies - extractive body cue:** As illustrated in Figure 4, this 24% is usually related to sub-concepts with close semantic (e.g. "blanket" and "comforter") or ambiguous annotations (e.g. the armchair ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experimental evaluations (p. 5); 4.1. Implementation and evaluation details (p. 5); 4.2.2. Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2.1. Evaluated methods | EMPIRICAL / SOURCE-REPORTED EVALUATION | Notice that the only difference between DiSCO-3D and those baselines relies on the fact that DiSCO-3D achieves USS and OVSeg jointly whereas the latters ... | p. 6 (4.2.1. Evaluated methods) |
| 4.2.3. Ablations studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | To evaluate the ability of the produced CLIP prototypes to achieve semantic matching, we evaluate the OV-SD performance by replacing the prototypes matching by ... | p. 7 (4.2.3. Ablations studies) |
| 4.1. Implementation and evaluation details | EMPIRICAL / SOURCE-REPORTED EVALUATION | We implemented our method in the Nerfstudio [34] framework and every evaluation is based on the same Nerfacto model, a grid-based NeRF method coupled ... | p. 5 (4.1. Implementation and evaluation details) |
| 4.2.2. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | However, the benchmark is still far from being saturated, showing the difficulty of the task and the room for future improvements. | p. 7 (4.2.2. Results) |
| 4. Experimental evaluations | EMPIRICAL / SOURCE-REPORTED EVALUATION | Then, we successively propose experiments for the edge cases of Open-Vocabulary Segmentation and Unsupervised Semantic Segmentation in subsection 4.3. | p. 5 (4. Experimental evaluations) |

## Dataset / Benchmark Role

- **p. 7 / 4.2.2. Results - extractive body cue:** We also display some qualitative examples in Figure 3 across various scenes (both indoor and outdoor from various datasets [12, 21, 33]), feature fields (LeRF ...
- **p. 6 / 4.1. Implementation and evaluation details - extractive body cue:** Segmentation quality is evaluated by first matching discovered sub-concepts to the dataset-defined sub-concepts (we match predictions with all of the scene's classes) using embeddings distances.
- **p. 7 / 4.2.2. Results - extractive body cue:** However, the benchmark is still far from being saturated, showing the difficulty of the task and the room for future improvements.
- **p. 5 / 4. Experimental evaluations - extractive body cue:** After introducing some implementation and evaluation details in subsection 4.1, we first present evaluations on the novel Open-Vocabulary Sub-concepts Discovery problem with a dedicated benchmark ...
- **p. 6 / 4.1. Implementation and evaluation details - extractive body cue:** We introduce an extension of the Replica [33] dataset for Open-Vocabulary Sub-concepts Discovery.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We introduce the 3D Open-Vocabulary Sub-concepts Discovery (OV-SD) paradigm, which aims to provide a 3D semantic segmentation adapted to both the scene (semantic ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of DiSCO-3D for a LeRF Feature Field. DiSCO-3D inputs pairs of features from 3D samples into a projector net- work learnt to ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. To ensure stability during training, we apply an Exponential Moving Average (EMA) across epochs, result- ing in the following update process for all ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. DiSCO-3D Qualitative Evaluation for OV-SD. We present results for various queries, scenes (which originate from [12, 21, 33]) and feature fields (LeRF in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Quantitative Evaluation for OV-SD. Additional metrics can be found in sup. mat. "FF" stands for feature field. Lproto Nadd 0 2 5 10
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Ablative on # of Prototypes (N = NGT +Nadd). These are done in the Hungarian Matching paradigm and with LeRF. The last column ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Linking Sub-concepts to a posteriori Textual Classes. The queries of the left and right images are respectively "Sleep" and "Furniture". By comparing each ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. DiSCO-3D Quantitative Evaluation for OV-Seg. form of OV-SD where each query asks for a single sub- concept, and to USS, which can be ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We also display some qualitative examples in Figure 3 across various scenes (both indoor and outdoor from various datasets [12, 21, 33]), feature fields ... | embodiment, simulator version and control stack | p. 7 (4.2.2. Results), p. 6 (4.1. Implementation and evaluation details) |
| Task/environment | Segmentation quality is evaluated by first matching discovered sub-concepts to the dataset-defined sub-concepts (we match predictions with all of the scene's classes) using embeddings ... | reset, timeout, object/scene variation | p. 6 (4.1. Implementation and evaluation details), p. 7 (4.2.2. Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 8 (4.3.2. Unsupervised Semantic Segmentation), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.1. Problem Statement and Overview), p. 3 (3.2. Preliminaries) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| First, we observe that the complete model's performance remains stable in both segmentation accuracy and the numFF Method PCLIP Hungarian PQ ↑ mIoU ↑ ... | definition/direction/unit from same section | p. 7 (4.2.3. Ablations studies) |
| This enables comparison with the groundtruth query segmentation to compute classic segmentation metrics: Mean Accuracy (mAcc) and mean Intersection over Union (mIoU). | definition/direction/unit from same section | p. 6 (4.1. Implementation and evaluation details) |
| As illustrated in Figure 4, this 24% is usually related to sub-concepts with close semantic (e.g. "blanket" and "comforter") or ambiguous annotations (e.g. the ... | definition/direction/unit from same section | p. 7 (4.2.3. Ablations studies) |
| Then, we successively propose experiments for the edge cases of Open-Vocabulary Segmentation and Unsupervised Semantic Segmentation in subsection 4.3. | definition/direction/unit from same section | p. 5 (4. Experimental evaluations) |
| We notice that using DiSCO-3D always overperforms the naive baselines, which demonstrates the interest of performing jointly USS and OVSeg. | definition/direction/unit from same section | p. 6 (4.2.2. Results) |
| Figure 2. Overview of DiSCO-3D for a LeRF Feature Field. DiSCO-3D inputs pairs of features from 3D samples into a projector net- work learnt ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| All quantitative experiments, including DiSCO3D and the comparative baselines, use the same pre-trained Nerfacto models and feature fields as input. | comparison identity and matched condition | p. 5 (4.1. Implementation and evaluation details) |
| Additional details on hyperparameters, evaluation protocols and baselines can be found in the supplementary materials, as well as ablative experiments and analysis on DiSCO's ... | comparison identity and matched condition | p. 5 (4. Experimental evaluations) |
| We also create two additional naive baselines by replacing the USS part by K-Means. | comparison identity and matched condition | p. 6 (4.2.1. Evaluated methods) |
| Both of these baselines share the DiSCO-3D architecture and the input feature fields. | comparison identity and matched condition | p. 6 (4.2.1. Evaluated methods) |
| Finally, we observe that the difference of performances between DiSCO and the baselines is not related to the use of CLIP prototypes. | comparison identity and matched condition | p. 7 (4.2.3. Ablations studies) |
| We also notice that replacing our USS with K-Means in the naive baselines outputs mostly worse performances, highlighting the interest of our architecture choices. | comparison identity and matched condition | p. 7 (4.2.3. Ablations studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Sensitivity to Number of Prototypes and influence of Lproto. | component/input/data sensitivity | p. 7 (4.2.3. Ablations studies) |
| Finally, the last column, corresponding to our main experiment with a fixed N = 10, shows that performance is maintained without requiring prior knowledge ... | component/input/data sensitivity | p. 7 (4.2.3. Ablations studies) |
| Table 3. DiSCO-3D Quantitative Evaluation for OV-Seg. form of OV-SD where each query asks for a single sub- concept, and to USS, which can ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Although we present our method using a pre-trained LeRF as input, DiSCO-3D is compatible with a wide range of feature fields (and their combinations) ... | Notice that the only difference between DiSCO-3D and those baselines relies on the fact that DiSCO-3D achieves USS and OVSeg jointly whereas the latters ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2.1. Evaluated methods), p. 7 (4.2.3. Ablations studies), p. 5 (4.1. Implementation and evaluation details), p. 7 (4.2.2. Results), p. 5 (4. Experimental evaluations), p. 6 (4.2.2. Results) |
| Primary metric/result | To evaluate the ability of the produced CLIP prototypes to achieve semantic matching, we evaluate the OV-SD performance by replacing the prototypes matching by ... | numeric claim only at cited anchor | p. 7 (4.2.3. Ablations studies) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Implementation and evaluation details - extractive body cue:** All our experiments were run on the same single RTX 4090 GPU.
- **p. 5 / 4.1. Implementation and evaluation details - extractive body cue:** They run for 100 epochs each, at approximately 20ms per epoch 20047
- **p. 6 / 4.1. Implementation and evaluation details - extractive body cue:** (resulting in ∼2s optimization per query, which can be considered fast enough for most practical applications; see sup. mat. for further discussions on DiSCO's speed).
- **p. 6 / 4.2.1. Evaluated methods - extractive body cue:** All the methods use the same hyperparameters and especially, we fix the number of prototypes N = 10 for all queries (as no concept query ...
- **p. 7 / 4.2.3. Ablations studies - extractive body cue:** Lproto Nadd 0 2 5 10 20 N = 10 ✗ Used Nadd -0.07 1.33 1.98 2.62 3.02 2.60 PQ ↑ 8.56 9.49 9.72 9.71 ...
- **p. 7 / 4.2.3. Ablations studies - extractive body cue:** Finally, the last column, corresponding to our main experiment with a fixed N = 10, shows that performance is maintained without requiring prior knowledge of ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Additional details on hyperparameters, evaluation protocols and baselines can be found in the supplementary materials, as well as ablative experiments and analysis on DiSCO's ... | p. 5 (4. Experimental evaluations) |
| body limitation/failure cue | The last column refers to the main experiment where the number of prototypes is fixed and does not depend on NGT . | p. 7 (4.2.3. Ablations studies) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All our experiments were run on the same single RTX 4090 GPU. | p. 5 (4.1. Implementation and evaluation details) |
| They run for 100 epochs each, at approximately 20ms per epoch 20047 | p. 5 (4.1. Implementation and evaluation details) |
| This enables comparison with the groundtruth query segmentation to compute classic segmentation metrics: Mean Accuracy (mAcc) and mean Intersection over Union (mIoU). | p. 6 (4.1. Implementation and evaluation details) |
| All the methods use the same hyperparameters and especially, we fix the number of prototypes N = 10 for all queries (as no concept ... | p. 6 (4.2.1. Evaluated methods) |
| In practice, we compute that approximately 76% of the matching remains unchanged, while 24% is reassigned to a new ground-truth sub-concept. | p. 7 (4.2.3. Ablations studies) |
| By comparing each CLIP prototype to Replica's semantic classes encoded with CLIP, DiSCO-3D is able to choose the most relevant class to describe each ... | p. 7 (4.3. Edge Cases) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 4. Experimental evaluations - extractive body cue:** Additional details on hyperparameters, evaluation protocols and baselines can be found in the supplementary materials, as well as ablative experiments and analysis on DiSCO's limitations.
- **p. 7 / 4.2.3. Ablations studies - extractive body cue:** The last column refers to the main experiment where the number of prototypes is fixed and does not depend on NGT .

- **Evidence anchors reviewed:** datasets p. 7 (4.2.2. Results), p. 6 (4.1. Implementation and evaluation details), p. 7 (4.2.2. Results), p. 5 (4. Experimental evaluations), p. 6 (4.1. Implementation and evaluation details), metrics p. 7 (4.2.3. Ablations studies), p. 6 (4.1. Implementation and evaluation details), p. 7 (4.2.3. Ablations studies), p. 5 (4. Experimental evaluations), p. 6 (4.2.2. Results), p. 3 (Figure/Table caption), baselines p. 5 (4.1. Implementation and evaluation details), p. 5 (4. Experimental evaluations), p. 6 (4.2.1. Evaluated methods), p. 6 (4.2.1. Evaluated methods), p. 7 (4.2.3. Ablations studies), p. 7 (4.2.3. Ablations studies), results p. 6 (4.2.1. Evaluated methods), p. 7 (4.2.3. Ablations studies), p. 5 (4.1. Implementation and evaluation details), p. 7 (4.2.2. Results), p. 5 (4. Experimental evaluations), p. 6 (4.2.2. Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
