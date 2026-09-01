# Evaluation - GroundFlow: A Plug-in Module for Temporal Reasoning on 3D Point Cloud Sequential Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Lin_GroundFlow_A_Plug-in_Module_for_Temporal_Reasoning_on_3D_Point_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Lin_GroundFlow_A_Plug-in_Module_for_Temporal_Reasoning_on_3D_Point_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.3. Comparison on SG3D Benchmark), p. 6 (4.3. Comparison on SG3D Benchmark), p. 7 (4.4. Ablation Study), p. 7 (4.4. Ablation Study), p. 5 (4.1. Dataset and Evaluation Metrics), p. 5 (4.1. Dataset and Evaluation Metrics)): On the other hand, significant performance improvements can be observed when these models are integrated with GroundFlow, as shown in the rows highlighted in orange.

## Evaluation Body Digest

- **p. 5 / 4.1. Dataset and Evaluation Metrics - extractive PDF cue:** The benchmark utilizes real-world scenes from the SceneVerse [26], incorporating indoor scans from 5 different datasets - ScanNet [11], 3RScan [40], MultiScan [31], ARKitScenes [3] ...
- **p. 6 / 4.2. Implementation Details - extractive PDF cue:** Comparisons on SG3D benchmark across five datasets.
- **p. 6 / 4.3. Comparison on SG3D Benchmark - extractive PDF cue:** It is pre-trained on an extensive range of 3D tasks, including object captioning [30, 51], object referring [1, 18, 48], 3D QA [12, 15, 47] ...
- **p. 5 / 4.2. Implementation Details - extractive PDF cue:** The models are trained for 50 epochs with batch size of 32 and evaluated on the last epoch using evaluation split of the SG3D benchmark.
- **p. 7 / 4.4. Ablation Study - extractive PDF cue:** In the SG3D benchmark, the step count of a task ranges from 2 to 10.
- **p. 7 / 4.4. Ablation Study - extractive PDF cue:** To investigate whether GroundFlow can consistently improve task accuracy of the 3DVG methods in more challenging scenarios with a high number of steps, we create ...
- **p. 8 / 4.5. Qualitative Visualization - extractive PDF cue:** T represents the task description, St and Ot denote the step instruction and corresponding referred target object in step t.
- **p. 8 / 4.5. Qualitative Visualization - extractive PDF cue:** In the second example, there are multiple chairs in the scene and the last step instruction, "Walk back to your chair", refers to the chair ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Dataset and Evaluation Metrics (p. 5); 4.2. Implementation Details (p. 5); 4.3. Comparison on SG3D Benchmark (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Comparison on SG3D Benchmark | EMPIRICAL / REAL-ROBOT OR HARDWARE | On the other hand, significant performance improvements can be observed when these models are integrated with GroundFlow, as shown in the rows highlighted in ... | p. 6 (4.3. Comparison on SG3D Benchmark) |
| 4.3. Comparison on SG3D Benchmark | EMPIRICAL / REAL-ROBOT OR HARDWARE | However, the 3DVG methods combined with our proposed GroundFlow module outperform LEO across all five datasets, setting new state-of-the-art performance on SG3D benchmark. | p. 6 (4.3. Comparison on SG3D Benchmark) |
| 4.4. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | To investigate whether GroundFlow can consistently improve task accuracy of the 3DVG methods in more challenging scenarios with a high number of steps, we ... | p. 7 (4.4. Ablation Study) |
| 4.4. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | Improvements after GroundFlow module is integrated in terms of task accuracy of 3D-VisTA and PQ3D across different step count subsets. various settings of short-term ... | p. 7 (4.4. Ablation Study) |
| 4.1. Dataset and Evaluation Metrics | EMPIRICAL / REAL-ROBOT OR HARDWARE | As defined in SG3D benchmark [52], all models' grounding performances is evaluated based on two key metrics: step accuracy (s-acc) and task accuracy (tacc). | p. 5 (4.1. Dataset and Evaluation Metrics) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Dataset and Evaluation Metrics - extractive PDF cue:** The benchmark utilizes real-world scenes from the SceneVerse [26], incorporating indoor scans from 5 different datasets - ScanNet [11], 3RScan [40], MultiScan [31], ARKitScenes [3] ...
- **p. 6 / 4.2. Implementation Details - extractive PDF cue:** Comparisons on SG3D benchmark across five datasets.
- **p. 6 / 4.3. Comparison on SG3D Benchmark - extractive PDF cue:** It is pre-trained on an extensive range of 3D tasks, including object captioning [30, 51], object referring [1, 18, 48], 3D QA [12, 15, 47] ...
- **p. 5 / 4.2. Implementation Details - extractive PDF cue:** The models are trained for 50 epochs with batch size of 32 and evaluated on the last epoch using evaluation split of the SG3D benchmark.
- **p. 7 / 4.4. Ablation Study - extractive PDF cue:** In the SG3D benchmark, the step count of a task ranges from 2 to 10.
- **p. 7 / 4.4. Ablation Study - extractive PDF cue:** To investigate whether GroundFlow can consistently improve task accuracy of the 3DVG methods in more challenging scenarios with a high number of steps, we create ...
- **p. 8 / 4.5. Qualitative Visualization - extractive PDF cue:** T represents the task description, St and Ot denote the step instruction and corresponding referred target object in step t.
- **p. 8 / 4.5. Qualitative Visualization - extractive PDF cue:** In the second example, there are multiple chairs in the scene and the last step instruction, "Walk back to your chair", refers to the chair ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. An example of SG3D task (above) and a comparison be- tween previous visual grounding framework (bottom left) and our recurrent framework (bottom right) ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. The overview of two 3DVG baseline models (blue background) integrated with our proposed plug-in temporal fusion module - GroundFlow (orange background). Unlike baseline ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Detailed illustration of Memory component in Ground- Flow, which enables the module to extract relevant information of both short-term ( ˆJt-1) and long-term ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Comparisons on SG3D benchmark across five datasets. The values for the metrics s-acc (step accuracy) and t-acc (task accuracy) are expressed as percentages ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison of temporal fusion methods for 3D-VisTA and PQ3D. The ∆improvement in the last two columns is relative to the original 3DVG baselines. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Comparison of different short-term and long-term mem- ory settings for 3D-VisTA and PQ3D. Aligned with section 3.2, ˆJm denotes the aggregation of the ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Improvements after GroundFlow module is integrated in terms of task accuracy of 3D-VisTA and PQ3D across different step count subsets. various settings of ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. Visualization results from PQ3D and PQ3D+GroundFlow. T represents the task description, St and Ot denote the step instruction and corresponding referred target object ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The benchmark utilizes real-world scenes from the SceneVerse [26], incorporating indoor scans from 5 different datasets - ScanNet [11], 3RScan [40], MultiScan [31], ARKitScenes ... | embodiment, simulator version and control stack | p. 5 (4.1. Dataset and Evaluation Metrics), p. 6 (4.2. Implementation Details) |
| Task/environment | Comparisons on SG3D benchmark across five datasets. | reset, timeout, object/scene variation | p. 6 (4.2. Implementation Details), p. 6 (4.3. Comparison on SG3D Benchmark) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| To address these limitations, the memory component in GroundFlow computes similarity scores to selectively retrieve and integrate context-specific past information based on its relevance ... | definition/direction/unit from same section | p. 7 (4.4. Ablation Study) |
| As defined in SG3D benchmark [52], all models' grounding performances is evaluated based on two key metrics: step accuracy (s-acc) and task accuracy (tacc). | definition/direction/unit from same section | p. 5 (4.1. Dataset and Evaluation Metrics) |
| Their degraded performance is particularly reflected in their overall task accuracy, with three of the models are falling below 30%. | definition/direction/unit from same section | p. 6 (4.3. Comparison on SG3D Benchmark) |
| Specifically, the overall performance in the SG3D benchmark of 3D-VisTA increases by 3.8% in step accuracy and 6.3% in task accuracy. | definition/direction/unit from same section | p. 6 (4.3. Comparison on SG3D Benchmark) |
| Improvements after GroundFlow module is integrated in terms of task accuracy of 3D-VisTA and PQ3D across different step count subsets. various settings of short-term ... | definition/direction/unit from same section | p. 7 (4.4. Ablation Study) |
| For task accuracy, a sample is considered correct if the predicted sequence of objects for each step matches the ground-truth sequence. | definition/direction/unit from same section | p. 5 (4.1. Dataset and Evaluation Metrics) |
| Unlike PQ3D, which incorrectly selects another chair, PQ3D integrated GroundFlow consistently identifies the correct chair referenced in the first step. | definition/direction/unit from same section | p. 8 (4.5. Qualitative Visualization) |
| These results highlight that the memory component in GroundFlow enables the model to retain important context over time, allowing it to accurately retrieve and ... | definition/direction/unit from same section | p. 8 (4.5. Qualitative Visualization) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| However, the 3DVG methods combined with our proposed GroundFlow module outperform LEO across all five datasets, setting new state-of-the-art performance on SG3D benchmark. | comparison identity and matched condition | p. 6 (4.3. Comparison on SG3D Benchmark) |
| All other training details for the baselines strictly follow the original paper's settings. | comparison identity and matched condition | p. 5 (4.2. Implementation Details) |
| As shown in Table 2, GroundFlow demonstrates more effective improvements compared to classic temporal fusion 28779 | comparison identity and matched condition | p. 6 (4.4. Ablation Study) |
| The ∆improvement in the last two columns is relative to the original 3DVG baselines. methods. | comparison identity and matched condition | p. 7 (4.4. Ablation Study) |
| As shown in Figure 4, the introduction of GroundFlow improves the performance of all subsets with different step counts, with the query-based method PQ3D ... | comparison identity and matched condition | p. 7 (4.4. Ablation Study) |
| Figure 2. The overview of two 3DVG baseline models (blue background) integrated with our proposed plug-in temporal fusion module - GroundFlow (orange background). Unlike ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In Table 3, the performance without one of the memory parts is presented in the first and second rows. | component/input/data sensitivity | p. 7 (4.4. Ablation Study) |
| Figure 3. Detailed illustration of Memory component in Ground- Flow, which enables the module to extract relevant information of both short-term ( ˆJt-1) and ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Furthermore, the state-of-theart 3D large language model, LEO, after fine-tuning on the SG3D benchmark is also compared. | component/input/data sensitivity | p. 6 (4.3. Comparison on SG3D Benchmark) |
| In fine-tuning stage, LEO predicts a special [GRD]t token at each step t, which is concatenated with object tokens and passed to the grounding ... | component/input/data sensitivity | p. 6 (4.3. Comparison on SG3D Benchmark) |
| Improvements after GroundFlow module is integrated in terms of task accuracy of 3D-VisTA and PQ3D across different step count subsets. various settings of short-term ... | component/input/data sensitivity | p. 7 (4.4. Ablation Study) |
| These results highlight that the memory component in GroundFlow enables the model to retain important context over time, allowing it to accurately retrieve and ... | component/input/data sensitivity | p. 8 (4.5. Qualitative Visualization) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, we make the following contributions: • We propose the GroundFlow module with a recurrent framework, which can be integrated into previous 3DVG ... | On the other hand, significant performance improvements can be observed when these models are integrated with GroundFlow, as shown in the rows highlighted in ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.3. Comparison on SG3D Benchmark), p. 6 (4.3. Comparison on SG3D Benchmark), p. 7 (4.4. Ablation Study), p. 7 (4.4. Ablation Study), p. 5 (4.1. Dataset and Evaluation Metrics), p. 5 (4.1. Dataset and Evaluation Metrics) |
| Primary metric/result | However, the 3DVG methods combined with our proposed GroundFlow module outperform LEO across all five datasets, setting new state-of-the-art performance on SG3D benchmark. | numeric claim only at cited anchor | p. 6 (4.3. Comparison on SG3D Benchmark) |

- Numeric sentences retained from the body:
- **p. 5 / 4.2. Implementation Details - extractive PDF cue:** The models are trained for 50 epochs with batch size of 32 and evaluated on the last epoch using evaluation split of the SG3D benchmark.
- **p. 7 / 4.4. Ablation Study - extractive PDF cue:** Tasks with step counts greater than 7 are combined into one subset, as creating separate subsets for them would result in fewer than 100 tasks, ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Their degraded performance is particularly reflected in their overall task accuracy, with three of the models are falling below 30%. | p. 6 (4.3. Comparison on SG3D Benchmark) |
| body limitation/failure cue | This advantage could stem from the limitations of existing methods: LSTM or GRU tends to forget longterm information. | p. 7 (4.4. Ablation Study) |
| body limitation/failure cue | Since previous step embeddings do not attend to this lost information, it cannot be carried forward to subsequent steps, even if it is essential ... | p. 7 (4.4. Ablation Study) |
| body limitation/failure cue | It is shown that PQ3D fails to correctly choose the target "Telephone", while PQ3D+GroundFlow makes the correct predictions of "Telephone" for both steps. | p. 8 (4.5. Qualitative Visualization) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Due to GPU memory constraints, the batch size for LEO is reduced to 16. | p. 5 (4.2. Implementation Details) |
| The models are trained for 50 epochs with batch size of 32 and evaluated on the last epoch using evaluation split of the SG3D ... | p. 5 (4.2. Implementation Details) |
| Improvements in t-acc over task steps. | p. 7 (4.4. Ablation Study) |
| Therefore, we use ˆJt-1 as short-term memory and ˆJm as long-term memory in our final implementation, leading to the best performance. | p. 7 (4.4. Ablation Study) |
| It is shown that PQ3D fails to correctly choose the target "Telephone", while PQ3D+GroundFlow makes the correct predictions of "Telephone" for both steps. | p. 8 (4.5. Qualitative Visualization) |
| These results highlight that the memory component in GroundFlow enables the model to retain important context over time, allowing it to accurately retrieve and ... | p. 8 (4.5. Qualitative Visualization) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4.3. Comparison on SG3D Benchmark - extractive PDF cue:** Their degraded performance is particularly reflected in their overall task accuracy, with three of the models are falling below 30%.
- **p. 7 / 4.4. Ablation Study - extractive PDF cue:** This advantage could stem from the limitations of existing methods: LSTM or GRU tends to forget longterm information.
- **p. 7 / 4.4. Ablation Study - extractive PDF cue:** Since previous step embeddings do not attend to this lost information, it cannot be carried forward to subsequent steps, even if it is essential for ...
- **p. 8 / 4.5. Qualitative Visualization - extractive PDF cue:** It is shown that PQ3D fails to correctly choose the target "Telephone", while PQ3D+GroundFlow makes the correct predictions of "Telephone" for both steps.

- **PDF anchors reviewed:** datasets p. 5 (4.1. Dataset and Evaluation Metrics), p. 6 (4.2. Implementation Details), p. 6 (4.3. Comparison on SG3D Benchmark), p. 5 (4.2. Implementation Details), p. 7 (4.4. Ablation Study), p. 7 (4.4. Ablation Study), metrics p. 7 (4.4. Ablation Study), p. 5 (4.1. Dataset and Evaluation Metrics), p. 6 (4.3. Comparison on SG3D Benchmark), p. 6 (4.3. Comparison on SG3D Benchmark), p. 7 (4.4. Ablation Study), p. 5 (4.1. Dataset and Evaluation Metrics), baselines p. 6 (4.3. Comparison on SG3D Benchmark), p. 5 (4.2. Implementation Details), p. 6 (4.4. Ablation Study), p. 7 (4.4. Ablation Study), p. 7 (4.4. Ablation Study), p. 3 (Figure/Table caption), results p. 6 (4.3. Comparison on SG3D Benchmark), p. 6 (4.3. Comparison on SG3D Benchmark), p. 7 (4.4. Ablation Study), p. 7 (4.4. Ablation Study), p. 5 (4.1. Dataset and Evaluation Metrics), p. 5 (4.1. Dataset and Evaluation Metrics).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
