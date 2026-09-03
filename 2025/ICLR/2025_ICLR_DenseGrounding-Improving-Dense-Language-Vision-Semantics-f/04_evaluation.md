# Evaluation - DenseGrounding: Improving Dense Language-Vision Semantics for Ego-centric 3D Visual Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=iGafR0hSln; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/114854. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 15 (A.4 ROBUSTNESS ANALYSIS)): The results demonstrate that "LLM+DB(R+L)" achieves the notable over all improvement of 2.45% against naive baseline, confirming the effectiveness of incorporating both object relationships and location data in augmentation process.

## Evaluation Body Digest

- **p. 7 / 5 EXPERIMENTS - extractive body cue:** For benchmarking, the official dataset maintains a non-public test set for the test leaderboard and divides the original training set into new subsets for training ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** This makes the dataset significantly larger and more challenging than previous ones, providing a more rigorous benchmark for 3D visual grounding tasks.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** We evaluate the 3D visual grounding performance of our proposed method, DenseGrounding, and report the results in Table 1, where we compare it against established ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** These qualitative results demonstrate the enhanced performance of DenseGrounding, especially in complex scenes with multiple distractors, solidifying its robustness and precision in real-world applications.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** The table is divided into two sections: the upper half presents models trained on the full training set, while the lower half showcases performance using ...
- **p. 15 / A.4 ROBUSTNESS ANALYSIS - extractive body cue:** As shown in Table 6, our method significantly outperforms the baseline in this zero-shot setting, demonstrating superior robustness and the ability to generalize effectively to ...
- **p. 15 / A.4 ROBUSTNESS ANALYSIS - extractive body cue:** This process is particularly challenging due to differences in camera settings, scene layouts, and object characteristics in visual data across various datasets, which can significantly ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Future research should explore integrating human-agent interaction, allowing the model to query users for clarification, and improving adaptability and robustness in real-world scenarios.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 7); A.1 More Implementation Details (p. 14); A.5 Implementation Details of LSE (p. 14); A.1 MORE IMPLEMENTATION DETAILS (p. 14); A.5 IMPLEMENTATION DETAILS OF LSE (p. 15).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results demonstrate that "LLM+DB(R+L)" achieves the notable over all improvement of 2.45% against naive baseline, confirming the effectiveness of incorporating both object relationships ... | p. 9 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | On the full training set, DenseGrounding achieves a significant improvement of 5.81% over the previous strongest baseline, EmbodiedScan. | p. 8 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 5.4 LIMITATIONS While the DenseGrounding significantly improves the ego-centric 3D visual grounding task performance, it has limitations. | p. 10 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Remarkably, even against this enhanced baseline, DenseGrounding attains a substantial 5.57% improvement in overall accuracy, culminating in a total performance gain of 7.56% over ... | p. 8 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Introducing the augmented data led to a remarkable accuracy improvement of 3.48%, highlighting its significant impact. | p. 9 (5 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / 5 EXPERIMENTS - extractive body cue:** For benchmarking, the official dataset maintains a non-public test set for the test leaderboard and divides the original training set into new subsets for training ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** This makes the dataset significantly larger and more challenging than previous ones, providing a more rigorous benchmark for 3D visual grounding tasks.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** We evaluate the 3D visual grounding performance of our proposed method, DenseGrounding, and report the results in Table 1, where we compare it against established ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** These qualitative results demonstrate the enhanced performance of DenseGrounding, especially in complex scenes with multiple distractors, solidifying its robustness and precision in real-world applications.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** The table is divided into two sections: the upper half presents models trained on the full training set, while the lower half showcases performance using ...
- **p. 15 / A.4 ROBUSTNESS ANALYSIS - extractive body cue:** As shown in Table 6, our method significantly outperforms the baseline in this zero-shot setting, demonstrating superior robustness and the ability to generalize effectively to ...
- **p. 15 / A.4 ROBUSTNESS ANALYSIS - extractive body cue:** This process is particularly challenging due to differences in camera settings, scene layouts, and object characteristics in visual data across various datasets, which can significantly ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Future research should explore integrating human-agent interaction, allowing the model to query users for clarification, and improving adaptability and robustness in real-world scenarios.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: (a) illustrates how limited context due to arbitrary descriptions leads to insufficient lan- guage semantics. (b) highlights the issue of losing fine-grained semantics ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: (a) shows overall framework, while (b) details the Language Semantic Enhancer (LSE) module, and (c) describes the Hierarchical Scene Semantic Enhancer (HSSE) module. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Validation Result: Accuracy performance of the models on the official full validation set. We follow the experimental setting proposed by Wang et al. ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Ablation on LSE. R and L refers to object relationship and object location infor- mation in SIDB, respectively.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Ablation of Proposed Methods. The reported values are Accuracies for predic- tions greater than 25% IoU with groundtruth. LSE HSSE Easy Hard Overall
- **p. 10 / Figure/Table caption - extractive body cue:** Table 4: Ablation on the number of self at- tention layers for HSSE. Lscene Easy Hard Overall 1 40.15
- **p. 10 / Figure/Table caption - extractive body cue:** Table 5: Ablation on the view feature map size after pooling for HSSE. Pooled Size Easy Hard Overall 1 40.61
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 3: Qualitative Analysis. Comparison of Ground Truth, our baseline and DenseGrounding. Ground truth boxes are shown in green, baseline in red, and DenseGrounding's predictions ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For benchmarking, the official dataset maintains a non-public test set for the test leaderboard and divides the original training set into new subsets for ... | embodiment, simulator version and control stack | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Task/environment | This makes the dataset significantly larger and more challenging than previous ones, providing a more rigorous benchmark for 3D visual grounding tasks. | reset, timeout, object/scene variation | p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3 PRELIMINARIES), p. 3 (1 INTRODUCTION) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3 PRELIMINARIES), p. 6 (4 METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Method Data Easy Hard Indep Dep Overall ACC25 ACC25 ACC25 ACC25 ACC25 ScanRefer (Chen et al., 2020) Full 13.78 9.12 13.44 10.77 12.85 BUTD-DETR ... | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| These qualitative results demonstrate the enhanced performance of DenseGrounding, especially in complex scenes with multiple distractors, solidifying its robustness and precision in real-world applications. | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |
| Remarkably, even against this enhanced baseline, DenseGrounding attains a substantial 5.57% improvement in overall accuracy, culminating in a total performance gain of 7.56% over ... | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| These consistent gains across different metrics underscore the robustness and generalizability of our approach in 3D visual grounding tasks. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| The reported values are Accuracies for predictions greater than 25% IoU with groundtruth. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| 5.4 LIMITATIONS While the DenseGrounding significantly improves the ego-centric 3D visual grounding task performance, it has limitations. | definition/direction/unit from same section | p. 10 (5 EXPERIMENTS) |
| Figure 1: (a) illustrates how limited context due to arbitrary descriptions leads to insufficient lan- guage semantics. (b) highlights the issue of losing fine-grained ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 4: Performance of our method on each class in validation set of EmbodiedScan 14 | definition/direction/unit from same section | p. 14 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Remarkably, even against this enhanced baseline, DenseGrounding attains a substantial 5.57% improvement in overall accuracy, culminating in a total performance gain of 7.56% over ... | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| It can be clearly seen that our method outperforms the baseline in correctly identifying the target objects based on ambiguous descriptions. | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| Furthermore, the combined use of LSE and HSSE resulted in a 5.57% accuracy improvement on hard samples compared to the baseline, underscoring our model's ... | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| For inference, our model processes descriptions directly, without any enhancement, aligning with our baseline methods for fair comparison. | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| The results clearly demonstrate that our method consistently outperforms the baseline, especially in scenarios with limited data availability. | comparison identity and matched condition | p. 15 (A.3 ANALYSIS ON LIMITED DATA SCENARIO) |
| As shown in Table 6, our method significantly outperforms the baseline in this zero-shot setting, demonstrating superior robustness and the ability to generalize effectively ... | comparison identity and matched condition | p. 15 (A.4 ROBUSTNESS ANALYSIS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conduct an ablation analysis to assess the effectiveness of each component, as shown in Tab. | component/input/data sensitivity | p. 9 (5 EXPERIMENTS) |
| 4, we conduct an ablation study to determine the optimal number of self-attention layers needed for effective learning of the scenefeature representation. | component/input/data sensitivity | p. 9 (5 EXPERIMENTS) |
| For inference, our model processes descriptions directly, without any enhancement, aligning with our baseline methods for fair comparison. | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |
| The "Dep" and "Indep" metrics further challenge spatial understanding ability by assessing its performance with and without perspective-specific descriptions. | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |
| In real-life applications, vague or ambiguous descriptions from human instructions pose challenges, as the model struggles without the necessary information to resolve ambiguities. | component/input/data sensitivity | p. 10 (5 EXPERIMENTS) |
| Lscene Easy Hard Overall 1 40.15 35.44 39.77 2 40.76 32.70 40.11 3 41.95 34.38 41.34 4 41.06 33.96 40.49 6 40.66 33.23 40.06 ... | component/input/data sensitivity | p. 10 (5 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| As shown in Figure 2, our method consists of three key components: Hierarchical Scene Semantic Enhancer (Sec. | The results demonstrate that "LLM+DB(R+L)" achieves the notable over all improvement of 2.45% against naive baseline, confirming the effectiveness of incorporating both object relationships ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 15 (A.4 ROBUSTNESS ANALYSIS) |
| Primary metric/result | On the full training set, DenseGrounding achieves a significant improvement of 5.81% over the previous strongest baseline, EmbodiedScan. | numeric claim only at cited anchor | p. 8 (5 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** It consists of 5,185 scene scans sourced from well-known datasets such as ScanNet (Dai et al., 2017), 3RScan (Wald et al., 2019), and Matterport3D (Chang ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Due to resource limitations, we reserve the full training dataset for baseline comparisons on the test set and leaderboard submissions to ensure a fair ... | p. 7 (5 EXPERIMENTS) |
| body limitation/failure cue | 5.4 LIMITATIONS While the DenseGrounding significantly improves the ego-centric 3D visual grounding task performance, it has limitations. | p. 10 (5 EXPERIMENTS) |
| body limitation/failure cue | By leveraging LLMs for description enhancement and introducing the HSSE to enhance fine-grained visual semantics, our method significantly improves the accuracy and robustness of ... | p. 10 (6 CONCLUSION) |
| body limitation/failure cue | These consistent gains across different metrics underscore the robustness and generalizability of our approach in 3D visual grounding tasks. | p. 9 (5 EXPERIMENTS) |
| body limitation/failure cue | In cases where the baseline model struggles to disambiguate between multiple similar objects, DenseGrounding successfully detects the correct target by leveraging its enriched textual ... | p. 9 (5 EXPERIMENTS) |
| body limitation/failure cue | Figure 5: Comparison of DenseGrounding and EmbodiedScan on limited data scenario. A.4 ROBUSTNESS ANALYSIS | p. 15 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 4.3, we replace RoBERTA with CLIP (Radford et al., 2021) text encoder as language feature encoders. | p. 8 (5 EXPERIMENTS) |
| Specifically, we use ResNet50 (He et al., 2016) and MinkNet34 (Choy et al., 2019) as the 2D and 3D vision encoders, respectively. | p. 8 (5 EXPERIMENTS) |
| The "Concat Samples" method from EmbodiedScan disambiguate descriptions by concatenating multiple annotations. "LLM" refers to our reimplementation of template-based LLM augmentation used by Viewrefer ... | p. 9 (5 EXPERIMENTS) |
| In this section, we provide the implementation details of the Language Semantic Enhancer (LSE) module, focusing on how the LLM is prompted. | p. 15 (A.5 IMPLEMENTATION DETAILS OF LSE) |
| With the encoded 2D features from each view, HSSE performs view-level semantic aggregation to capture view-level global semantics within each view. | p. 6 (4 METHOD) |
| F v Q = Pool(F v Ref) ∈Rhs×ws×Cs (2) Subsequently, we compute the cross-attention between the pooled queries and the reference feature to aggregate ... | p. 6 (4 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Due to resource limitations, we reserve the full training dataset for baseline comparisons on the test set and leaderboard submissions to ensure a fair and ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** 5.4 LIMITATIONS While the DenseGrounding significantly improves the ego-centric 3D visual grounding task performance, it has limitations.
- **p. 10 / 6 CONCLUSION - extractive body cue:** By leveraging LLMs for description enhancement and introducing the HSSE to enhance fine-grained visual semantics, our method significantly improves the accuracy and robustness of 3D ...
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** These consistent gains across different metrics underscore the robustness and generalizability of our approach in 3D visual grounding tasks.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** In cases where the baseline model struggles to disambiguate between multiple similar objects, DenseGrounding successfully detects the correct target by leveraging its enriched textual descriptions ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 5: Comparison of DenseGrounding and EmbodiedScan on limited data scenario. A.4 ROBUSTNESS ANALYSIS

- **Evidence anchors reviewed:** datasets p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 15 (A.4 ROBUSTNESS ANALYSIS), metrics p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), baselines p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 15 (A.3 ANALYSIS ON LIMITED DATA SCENARIO), p. 15 (A.4 ROBUSTNESS ANALYSIS), results p. 9 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 15 (A.4 ROBUSTNESS ANALYSIS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
