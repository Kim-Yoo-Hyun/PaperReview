# Evaluation - LIRA: Reasoning Reconstruction via Multimodal Large Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_LIRA_Reasoning_Reconstruction_via_Multimodal_Large_Language_Models_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4.3. Reasoning Reconstruction Results), p. 7 (Figure/Table caption), p. 6 (4.2. Evaluation Metrics), p. 8 (4.7. Qualitative Results)): Table 5. Ablation studies of the three stages of LIRA. struction "Appliances or furniture used to store food" is replaced with "Cabinet, Refrigerator". The generated ex- plicit instruction format is ...

## Evaluation Body Digest

- **p. 5 / 3.4. Benchmark - extractive body cue:** To establish a comprehensive evaluation system suitable for the reasoning reconstruction task, a benchmark ReasonRecon is constructed and the data collection pipeline is shown in ...
- **p. 6 / 3.4. Benchmark - extractive body cue:** Dataset Scene-Instruction Implicit Instruction High-Quality M., M., Z.
- **p. 6 / 3.4. Benchmark - extractive body cue:** The training set and test set are divided into 8: 2.
- **p. 5 / 3.4. Benchmark - extractive body cue:** It uses RGB-D sequences and 3D instance segmentation annotations in the ScanNetV2 dataset [5].
- **p. 6 / 4.2. Evaluation Metrics - extractive body cue:** We evaluate using standard Average Precision (AP) metrics at IoU thresholds of 50% and 25%, and also calculate mean score across IoU thresholds from 50% ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Runtime analysis of reasoning reconstruction. comparison. VLMaps is extended to a 3D map by can- celing top-down projection. LIRA* represents that LIRA uses ...
- **p. 7 / 4.5. Runtime Analysis - extractive body cue:** Compared with other methods, our LIRA-Fast has advantages in both reasoning reconstruction speed and accuracy.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Visualization results of different reasoning reconstruction methods on the ReasonRecon test set. The reconstructed geometric results are augmented with image textures. Single-layered mesh ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3.4. Benchmark (p. 5); 4. Experiments (p. 6); 4.1. Implementation Details (p. 6); 4.2. Evaluation Metrics (p. 6); 4.3. Reasoning Reconstruction Results (p. 6); 4.7. Qualitative Results (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 5. Ablation studies of the three stages of LIRA. struction "Appliances or furniture used to store food" is replaced with "Cabinet, Refrigerator". The ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 6. Visualization results of different reasoning reconstruction methods on the ReasonRecon test set. The reconstructed geometric results are augmented with image textures. Single-layered ... | p. 8 (Figure/Table caption) |
| 4.3. Reasoning Reconstruction Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Some of them are improved to support multi-instance outputs for a fair 1767 | p. 6 (4.3. Reasoning Reconstruction Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 4. Runtime analysis of reasoning reconstruction. comparison. VLMaps is extended to a 3D map by can- celing top-down projection. LIRA* represents that LIRA ... | p. 7 (Figure/Table caption) |
| 4.2. Evaluation Metrics | EMPIRICAL / SOURCE-REPORTED EVALUATION | These metrics evaluate the performance of both geometric reconstruction and instance matching. | p. 6 (4.2. Evaluation Metrics) |

## Dataset / Benchmark Role

- **p. 5 / 3.4. Benchmark - extractive body cue:** To establish a comprehensive evaluation system suitable for the reasoning reconstruction task, a benchmark ReasonRecon is constructed and the data collection pipeline is shown in ...
- **p. 6 / 3.4. Benchmark - extractive body cue:** Dataset Scene-Instruction Implicit Instruction High-Quality M., M., Z.
- **p. 6 / 3.4. Benchmark - extractive body cue:** The training set and test set are divided into 8: 2.
- **p. 5 / 3.4. Benchmark - extractive body cue:** It uses RGB-D sequences and 3D instance segmentation annotations in the ScanNetV2 dataset [5].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Online reasoning reconstruction results of LIRA. It in- puts RGB-D sequences and reconstructs instruction-relevant in- stances and background environment. As the process is ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of LIRA. Stage I: LIRA uses depth maps for geometric reconstruction and applies a MLLM to infer instruction-relevant 2D candidate instance masks ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Architecture of the proposed 2D reasoning segmentation module. Three examples are given (corresponding to the dashed boxes of different colors). Please zoom in ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Illustration of the proposed instance fusion module. Dif- ferent colors represent different instances, and different icons rep- resent instances at different frames. Please ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Illustration of the data collection process. Red dots are projected points. Extended attributes are indicated in orange font.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Comparison of ReasonRecon with related datasets. "M., M., Z." indicates multi-class, multi-target, and zero-target. from a certain viewpoint. Erroneous projected pixels caused by ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Quantitative results of reasoning reconstruction. output types, including multi-class, multi-target, zero-target and single-target outputs. Also, we obtain high-quality 2D segmentation annotations. In addition, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Results of explicit instruction-guided reconstruction.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To establish a comprehensive evaluation system suitable for the reasoning reconstruction task, a benchmark ReasonRecon is constructed and the data collection pipeline is shown ... | embodiment, simulator version and control stack | p. 5 (3.4. Benchmark), p. 6 (3.4. Benchmark) |
| Task/environment | Dataset Scene-Instruction Implicit Instruction High-Quality M., M., Z. | reset, timeout, object/scene variation | p. 6 (3.4. Benchmark), p. 6 (3.4. Benchmark) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3. Method), p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We evaluate using standard Average Precision (AP) metrics at IoU thresholds of 50% and 25%, and also calculate mean score across IoU thresholds from ... | definition/direction/unit from same section | p. 6 (4.2. Evaluation Metrics) |
| Table 4. Runtime analysis of reasoning reconstruction. comparison. VLMaps is extended to a 3D map by can- celing top-down projection. LIRA* represents that LIRA ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Compared with other methods, our LIRA-Fast has advantages in both reasoning reconstruction speed and accuracy. | definition/direction/unit from same section | p. 7 (4.5. Runtime Analysis) |
| Figure 6. Visualization results of different reasoning reconstruction methods on the ReasonRecon test set. The reconstructed geometric results are augmented with image textures. Single-layered ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Human corrections are also incorporated to enhance the quality of these instructions. | definition/direction/unit from same section | p. 6 (3.4. Benchmark) |
| Figure 2. Overview of LIRA. Stage I: LIRA uses depth maps for geometric reconstruction and applies a MLLM to infer instruction-relevant 2D candidate instance ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 1. Online reasoning reconstruction results of LIRA. It in- puts RGB-D sequences and reconstructs instruction-relevant in- stances and background environment. As the process ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 3. Architecture of the proposed 2D reasoning segmentation module. Three examples are given (corresponding to the dashed boxes of different colors). Please zoom ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 4. Runtime analysis of reasoning reconstruction. comparison. VLMaps is extended to a 3D map by can- celing top-down projection. LIRA* represents that LIRA ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Compared with other methods, our LIRA-Fast has advantages in both reasoning reconstruction speed and accuracy. | comparison identity and matched condition | p. 7 (4.5. Runtime Analysis) |
| Figure 6. Visualization results of different reasoning reconstruction methods on the ReasonRecon test set. The reconstructed geometric results are augmented with image textures. Single-layered ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| 6, a visual comparison with existing related works is provided. | comparison identity and matched condition | p. 8 (4.7. Qualitative Results) |
| The comparison of ReasonRecon with related datasets is shown in Tab. | comparison identity and matched condition | p. 6 (3.4. Benchmark) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 5. Ablation studies of the three stages of LIRA. struction "Appliances or furniture used to store food" is replaced with "Cabinet, Refrigerator". The ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our major contributions are as follows: • We introduce the reasoning reconstruction task, which requires online 3D reconstruction guided by implicit and ... | Table 5. Ablation studies of the three stages of LIRA. struction "Appliances or furniture used to store food" is replaced with "Cabinet, Refrigerator". The ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4.3. Reasoning Reconstruction Results), p. 7 (Figure/Table caption), p. 6 (4.2. Evaluation Metrics), p. 8 (4.7. Qualitative Results) |
| Primary metric/result | Figure 6. Visualization results of different reasoning reconstruction methods on the ReasonRecon test set. The reconstructed geometric results are augmented with image textures. Single-layered ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | One limitation is that LIRA exhibits relatively low performance in high-precision reconstruction. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Future work will consider further optimization in 3D space. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Erroneous projected pixels caused by occlusion are filtered out. | p. 6 (3.4. Benchmark) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Loss functions and more implementation details are described in the supplementary material. | p. 6 (4.1. Implementation Details) |
| For a fair comparison, runtime evaluation is performed on a single NVIDIA Tesla A800 GPU. | p. 7 (4.5. Runtime Analysis) |
| The average inference time for each RGB-D keyframe in the FBV is provided. | p. 7 (4.5. Runtime Analysis) |
| Image Encoder Segmentation Foundation Model VLM Vision Encoder Mask Decoder Large Language Model LoRA Vision-Language Model (VLM) Image Embeddings No object. | p. 4 (3.1.1. Incremental Geometric Reconstruction) |
| (3) Then, fimg and ˆhseg (text feature prompt) are input into the mask decoder Fdec of the segmentation foundation model to output the binary ... | p. 4 (3.1.2. 2D Reasoning Segmentation within the FBV) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** One limitation is that LIRA exhibits relatively low performance in high-precision reconstruction.
- **p. 8 / 5. Conclusion - extractive body cue:** Future work will consider further optimization in 3D space.
- **p. 6 / 3.4. Benchmark - extractive body cue:** Erroneous projected pixels caused by occlusion are filtered out.

- **Evidence anchors reviewed:** datasets p. 5 (3.4. Benchmark), p. 6 (3.4. Benchmark), p. 6 (3.4. Benchmark), p. 5 (3.4. Benchmark), metrics p. 6 (4.2. Evaluation Metrics), p. 7 (Figure/Table caption), p. 7 (4.5. Runtime Analysis), p. 8 (Figure/Table caption), p. 6 (3.4. Benchmark), p. 3 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 7 (4.5. Runtime Analysis), p. 8 (Figure/Table caption), p. 8 (4.7. Qualitative Results), p. 6 (3.4. Benchmark), results p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4.3. Reasoning Reconstruction Results), p. 7 (Figure/Table caption), p. 6 (4.2. Evaluation Metrics), p. 8 (4.7. Qualitative Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
