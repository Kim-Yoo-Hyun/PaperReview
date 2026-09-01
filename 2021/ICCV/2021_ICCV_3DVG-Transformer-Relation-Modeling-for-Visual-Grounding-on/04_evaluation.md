# Evaluation - 3DVG-Transformer: Relation Modeling for Visual Grounding on Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2021/html/Zhao_3DVG-Transformer_Relation_Modeling_for_Visual_Grounding_on_Point_Clouds_ICCV_2021_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2021/papers/Zhao_3DVG-Transformer_Relation_Modeling_for_Visual_Grounding_on_Point_Clouds_ICCV_2021_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 7 (4.2. Comparisons with the state-of-the-art methods), p. 8 (4.3. Ablation Study and Analysis), p. 8 (4.3. Ablation Study and Analysis), p. 5 (4.1. Datasets and Implementation Details), p. 5 (4.1. Datasets and Implementation Details)): Figure 3. Qualitative results from ScanRefer [6] and our 3DVG-Transformer. The GT boxes are marked in blue. If one predicted box has an IoU score higher than 0.5, this box ...

## Evaluation Body Digest

- **p. 5 / 4.1. Datasets and Implementation Details - extractive PDF cue:** To fully evaluate our method, we compare our method with the baseline methods on both the validation set and the online test set available at ...
- **p. 5 / 4.1. Datasets and Implementation Details - extractive PDF cue:** We evaluate our 3DVG-Transformer on two recent point cloud based visual grounding datasets, including Nr3D/Sr3D from ReferIt3D [7] and ScanRefer [6] . - ScanRefer: ScanRefer ...
- **p. 7 / 4.2. Comparisons with the state-of-the-art methods - extractive PDF cue:** The results of our method under the "2D+3D" setting were also evaluated on the test dataset from the ScanRefer online benchmark under both settings.
- **p. 6 / 4.1. Datasets and Implementation Details - extractive PDF cue:** Comparison of different methods on both Nr3D and Sr3D datasets [7]. "Easy" and "hard" mean whether there are more than 2 instances from the same ...
- **p. 7 / 4.2. Comparisons with the state-of-the-art methods - extractive PDF cue:** These examples demonstrate that our 3DVG-Transformer achieves more reliable 3D object localization results, especially when the scenes are cluttered with multiple similar objects and the ...
- **p. 6 / 4.1. Datasets and Implementation Details - extractive PDF cue:** For the ScanRefer dataset, we train our model in an end-to-end fashion by using the AdamW optimizer [42].
- **p. 8 / 4.3. Ablation Study and Analysis - extractive PDF cue:** We take the Nr3D dataset [7] as an example to compare different choices when fusing the spatial proximity matrix with the attention matrix in this ...
- **p. 8 / 4.3. Ablation Study and Analysis - extractive PDF cue:** Here, we only visualize the attention map of a query object (i.e., "trash can").

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Datasets and Implementation Details (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 3. Qualitative results from ScanRefer [6] and our 3DVG-Transformer. The GT boxes are marked in blue. If one predicted box has an IoU ... | p. 7 (Figure/Table caption) |
| 4.2. Comparisons with the state-of-the-art methods | SYSTEM / EVALUATION SCOPE UNRESOLVED | The proposed 3DVGTransformer achieves the overall accuracy of 40.8% and 51.4% on Nr3D and Sr3D respectively, which outperforms all the baseline methods by a ... | p. 7 (4.2. Comparisons with the state-of-the-art methods) |
| 4.3. Ablation Study and Analysis | SYSTEM / EVALUATION SCOPE UNRESOLVED | As shown in Table 4, the best results are achieved by using our default strategy, while the localization accuracies without using the coordinate-guided attention ... | p. 8 (4.3. Ablation Study and Analysis) |
| 4.3. Ablation Study and Analysis | SYSTEM / EVALUATION SCOPE UNRESOLVED | The results show that the performance is consistently improved after introducing each component, which validates that each proposed module is useful. | p. 8 (4.3. Ablation Study and Analysis) |
| 4.1. Datasets and Implementation Details | SYSTEM / EVALUATION SCOPE UNRESOLVED | The overall accuracy and the accuracies on both"unique" and "multiple" subsets are reported. | p. 5 (4.1. Datasets and Implementation Details) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Datasets and Implementation Details - extractive PDF cue:** To fully evaluate our method, we compare our method with the baseline methods on both the validation set and the online test set available at ...
- **p. 5 / 4.1. Datasets and Implementation Details - extractive PDF cue:** We evaluate our 3DVG-Transformer on two recent point cloud based visual grounding datasets, including Nr3D/Sr3D from ReferIt3D [7] and ScanRefer [6] . - ScanRefer: ScanRefer ...
- **p. 7 / 4.2. Comparisons with the state-of-the-art methods - extractive PDF cue:** The results of our method under the "2D+3D" setting were also evaluated on the test dataset from the ScanRefer online benchmark under both settings.
- **p. 6 / 4.1. Datasets and Implementation Details - extractive PDF cue:** Comparison of different methods on both Nr3D and Sr3D datasets [7]. "Easy" and "hard" mean whether there are more than 2 instances from the same ...
- **p. 7 / 4.2. Comparisons with the state-of-the-art methods - extractive PDF cue:** These examples demonstrate that our 3DVG-Transformer achieves more reliable 3D object localization results, especially when the scenes are cluttered with multiple similar objects and the ...
- **p. 6 / 4.1. Datasets and Implementation Details - extractive PDF cue:** For the ScanRefer dataset, we train our model in an end-to-end fashion by using the AdamW optimizer [42].
- **p. 8 / 4.3. Ablation Study and Analysis - extractive PDF cue:** We take the Nr3D dataset [7] as an example to compare different choices when fusing the spatial proximity matrix with the attention matrix in this ...
- **p. 8 / 4.3. Ablation Study and Analysis - extractive PDF cue:** Here, we only visualize the attention map of a query object (i.e., "trash can").

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1. The pipeline of our 3DVG-Transformer, which includes an object proposal generation module, a language encoding module, and a cross-modal fusion module. The input ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. The network structure of our coordinate-guided contex- tual aggregation module (a), which consists of 2 transformer lay- ers (the multi-level feature fusion module ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison of different methods on the ScanRefer dataset [6], where the results on both "unique" and "multiple" subsets are also reported. We report ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison of different methods on both Nr3D and Sr3D datasets [7]. "Easy" and "hard" mean whether there are more than 2 instances from ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative results from ScanRefer [6] and our 3DVG-Transformer. The GT boxes are marked in blue. If one predicted box has an IoU score ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation study on the ScanRefer validation set [6] under the "2D+3D" setting. We only report the "overall" results in terms of Acc@0.25 and ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Results of our 3DVG-Transformer (i.e. "Add SPM") and two variants (i.e. "w/o SPM" and "Mul SPM") on the Nr3D validation set [7]. Methods ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Visualization of the attention maps by using our method based on the ground-truth bounding boxes (bboxes) from Sr3D [7], in comparison with a ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To fully evaluate our method, we compare our method with the baseline methods on both the validation set and the online test set available ... | embodiment, simulator version and control stack | p. 5 (4.1. Datasets and Implementation Details), p. 5 (4.1. Datasets and Implementation Details) |
| Task/environment | We evaluate our 3DVG-Transformer on two recent point cloud based visual grounding datasets, including Nr3D/Sr3D from ReferIt3D [7] and ScanRefer [6] . - ScanRefer: ... | reset, timeout, object/scene variation | p. 5 (4.1. Datasets and Implementation Details), p. 7 (4.2. Comparisons with the state-of-the-art methods) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.1. Overview), p. 3 (3.2. Relation-enhanced Proposal Generation) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| If one predicted box has an IoU score higher than 0.5, this box is marked in green, otherwise it is marked in red. | definition/direction/unit from same section | p. 7 (4.2. Comparisons with the state-of-the-art methods) |
| The overall accuracy and the accuracies on both"unique" and "multiple" subsets are reported. | definition/direction/unit from same section | p. 5 (4.1. Datasets and Implementation Details) |
| For both datasets, the task is to select which object is the preferred object, which is evaluated by the instancematching accuracy. | definition/direction/unit from same section | p. 5 (4.1. Datasets and Implementation Details) |
| The proposed 3DVGTransformer achieves the overall accuracy of 40.8% and 51.4% on Nr3D and Sr3D respectively, which outperforms all the baseline methods by a ... | definition/direction/unit from same section | p. 7 (4.2. Comparisons with the state-of-the-art methods) |
| Darker/brighter color indicates higher/lower attention score. | definition/direction/unit from same section | p. 8 (4.3. Ablation Study and Analysis) |
| Thanks to our relation modeling capability empowered by the transformer-like structure, our method 3DVG-Transformer achieves the best overall accuracy of Find the dresser that ... | definition/direction/unit from same section | p. 8 (4.3. Ablation Study and Analysis) |
| Figure 1. The pipeline of our 3DVG-Transformer, which includes an object proposal generation module, a language encoding module, and a cross-modal fusion module. The ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| We apply the cosine learning rate decay strategy with a weight decay factor of 1e-5. | definition/direction/unit from same section | p. 6 (4.1. Datasets and Implementation Details) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In Table 1 and Table 2, our 3DVG-Transformer is compared with several baseline methods on both ScanRefer and Nr3D/Sr3D datasets, which include the 2D-based ... | comparison identity and matched condition | p. 6 (4.2. Comparisons with the state-of-the-art methods) |
| Our method outperforms all the baseline methods by remarkable performance gains. | comparison identity and matched condition | p. 7 (4.2. Comparisons with the state-of-the-art methods) |
| The results on the test set also validate that our method significantly outperforms other baseline methods on the "multiple" subset. | comparison identity and matched condition | p. 7 (4.2. Comparisons with the state-of-the-art methods) |
| To fully evaluate our method, we compare our method with the baseline methods on both the validation set and the online test set available ... | comparison identity and matched condition | p. 5 (4.1. Datasets and Implementation Details) |
| 4, we show that our relation modeling scheme can better ground the "dresser" next to the "trash can" according to the relation indicated by ... | comparison identity and matched condition | p. 8 (4.3. Ablation Study and Analysis) |
| The first row is the reported results of the baseline method in ScanRefer [6]. "Ours w/o CCA & MA & aug." means we do ... | comparison identity and matched condition | p. 8 (4.3. Ablation Study and Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We take the ScanRefer validation set [6] as an example to perform a comprehensive ablation study and analyze different components in our 3DVGTransformer. | component/input/data sensitivity | p. 8 (4.3. Ablation Study and Analysis) |
| Ablation study on the ScanRefer validation set [6] under the "2D+3D" setting. | component/input/data sensitivity | p. 7 (4.2. Comparisons with the state-of-the-art methods) |
| Results of our 3DVG-Transformer (i.e. "Add SPM") and two variants (i.e. "w/o SPM" and "Mul SPM") on the Nr3D validation set [7]. | component/input/data sensitivity | p. 8 (4.3. Ablation Study and Analysis) |
| Figure 1. The pipeline of our 3DVG-Transformer, which includes an object proposal generation module, a language encoding module, and a cross-modal fusion module. The ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| 3.1, we present an overview of our method. | Figure 3. Qualitative results from ScanRefer [6] and our 3DVG-Transformer. The GT boxes are marked in blue. If one predicted box has an IoU ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 7 (4.2. Comparisons with the state-of-the-art methods), p. 8 (4.3. Ablation Study and Analysis), p. 8 (4.3. Ablation Study and Analysis), p. 5 (4.1. Datasets and Implementation Details), p. 5 (4.1. Datasets and Implementation Details) |
| Primary metric/result | The proposed 3DVGTransformer achieves the overall accuracy of 40.8% and 51.4% on Nr3D and Sr3D respectively, which outperforms all the baseline methods by a ... | numeric claim only at cited anchor | p. 7 (4.2. Comparisons with the state-of-the-art methods) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Datasets and Implementation Details - extractive PDF cue:** We evaluate our 3DVG-Transformer on two recent point cloud based visual grounding datasets, including Nr3D/Sr3D from ReferIt3D [7] and ScanRefer [6] . - ScanRefer: ScanRefer ...
- **p. 5 / 4.1. Datasets and Implementation Details - extractive PDF cue:** Each scene has an average of 13.81 objects and 64.48 descriptions.
- **p. 5 / 4.1. Datasets and Implementation Details - extractive PDF cue:** We follow the ScanRefer benchmark to split the train/val/test set with 36, 655, 9, 508, and 5, 410 samples, respectively.
- **p. 5 / 4.1. Datasets and Implementation Details - extractive PDF cue:** Specifically, Nr3D contains 41, 503 samples collected by ReferItGame and Sr3D contains 83, 572 samples generated from the synthetic templates.
- **p. 6 / 4.1. Datasets and Implementation Details - extractive PDF cue:** The network is trained for 120, 000 iterations, with a batch size of 8, in which each scene is paired with 8 sentences, thus there ...
- **p. 4 / 3.2. Relation-enhanced Proposal Generation - extractive PDF cue:** 2 layers in our implementation) and then a multi-level feature fusion module.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The failure cases of ScanRefer indicate that this baseline method cannot well model complex relations and distinguish ambiguous objects. | p. 7 (4.2. Comparisons with the state-of-the-art methods) |
| body limitation/failure cue | Figure 2. The network structure of our coordinate-guided contex- tual aggregation module (a), which consists of 2 transformer lay- ers (the multi-level feature fusion ... | p. 4 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We apply the cosine learning rate decay strategy with a weight decay factor of 1e-5. | p. 6 (4.1. Datasets and Implementation Details) |
| The network is trained for 120, 000 iterations, with a batch size of 8, in which each scene is paired with 8 sentences, thus ... | p. 6 (4.1. Datasets and Implementation Details) |
| The language encoding module aims to use the same GRU cell as in ScanRefer [6] to encode the query word embeddings as a set ... | p. 3 (3.1. Overview) |
| 2 layers in our implementation) and then a multi-level feature fusion module. | p. 4 (3.2. Relation-enhanced Proposal Generation) |
| We empirically set k1 = 20 and k2 = 5 in our implementation. | p. 5 (3.2. Relation-enhanced Proposal Generation) |
| In our implementation, we use two pairs of interlaced attention blocks. | p. 5 (3.3. Cross-modal Proposal Disambiguation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.2. Comparisons with the state-of-the-art methods - extractive PDF cue:** The failure cases of ScanRefer indicate that this baseline method cannot well model complex relations and distinguish ambiguous objects.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. The network structure of our coordinate-guided contex- tual aggregation module (a), which consists of 2 transformer lay- ers (the multi-level feature fusion module ...

- **PDF anchors reviewed:** datasets p. 5 (4.1. Datasets and Implementation Details), p. 5 (4.1. Datasets and Implementation Details), p. 7 (4.2. Comparisons with the state-of-the-art methods), p. 6 (4.1. Datasets and Implementation Details), p. 7 (4.2. Comparisons with the state-of-the-art methods), p. 6 (4.1. Datasets and Implementation Details), metrics p. 7 (4.2. Comparisons with the state-of-the-art methods), p. 5 (4.1. Datasets and Implementation Details), p. 5 (4.1. Datasets and Implementation Details), p. 7 (4.2. Comparisons with the state-of-the-art methods), p. 8 (4.3. Ablation Study and Analysis), p. 8 (4.3. Ablation Study and Analysis), baselines p. 6 (4.2. Comparisons with the state-of-the-art methods), p. 7 (4.2. Comparisons with the state-of-the-art methods), p. 7 (4.2. Comparisons with the state-of-the-art methods), p. 5 (4.1. Datasets and Implementation Details), p. 8 (4.3. Ablation Study and Analysis), p. 8 (4.3. Ablation Study and Analysis), results p. 7 (Figure/Table caption), p. 7 (4.2. Comparisons with the state-of-the-art methods), p. 8 (4.3. Ablation Study and Analysis), p. 8 (4.3. Ablation Study and Analysis), p. 5 (4.1. Datasets and Implementation Details), p. 5 (4.1. Datasets and Implementation Details).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
