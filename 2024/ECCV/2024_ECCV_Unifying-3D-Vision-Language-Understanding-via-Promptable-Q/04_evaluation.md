# Evaluation - Unifying 3D Vision-Language Understanding via Promptable Queries

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6043_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06043.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (4 Experiments), p. 11 (4 Experiments), p. 13 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 9 (4 Experiments)): Furthermore, on the Multi3DRefer benchmark, our model outperforms others in the ST (single target) and MT (multiple targets) categories and achieves the highest average score of 50.1%.

## Evaluation Body Digest

- **p. 9 / 4 Experiments - extractive PDF cue:** To further demonstrate the capability of PQ3D, we also transfer it to an embodied agent for object navigation using the ObjNav task from CortexBench [42] ...
- **p. 8 / 4 Experiments - extractive PDF cue:** 1 shows a summary of the datasets used for the multitask training of PQ3D.
- **p. 8 / 4 Experiments - extractive PDF cue:** Notably, we combine eight datasets for training, including about 662K training samples for various tasks.
- **p. 9 / 4 Experiments - extractive PDF cue:** Dataset Task Prompt Heads Size ScanNet200 [52] instance segmentation category mask,grounding 240K ScanRefer [6] visual grounding sentence grounding 37K Nr3D [2] visual grounding sentence grounding ...
- **p. 11 / 4 Experiments - extractive PDF cue:** Importantly, the performance of PQ3D trained on multiple tasks and datasets exceeds that of PQ3D trained on a single task and dataset, showcasing the effectiveness ...
- **p. 10 / 4 Experiments - extractive PDF cue:** Zhu et al. of-distribution dataset Replica [55].
- **p. 10 / 4 Experiments - extractive PDF cue:** These findings imply a notable capability of PQ3D for effective transfer to different datasets.
- **p. 11 / 4 Experiments - extractive PDF cue:** The notation "PQ3D (sg.)" indicates a model trained on a single dataset rather than through unified joint training.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Furthermore, on the Multi3DRefer benchmark, our model outperforms others in the ST (single target) and MT (multiple targets) categories and achieves the highest average ... | p. 10 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | The proposed PQ3D provides global 3D features to the navigation agent that can improve the baseline VC-1 by a significant margin, achieving a 22.9% ... | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | When both image and point features are absent, the PQ3D outperforms the specific-tuned model, demonstrating the improved generalization ability through training with multiple representations. | p. 13 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results suggest that a 4-layer decoder outperforms both 2-layer and 6-layer ones on all tasks. | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 8, we can observe that PQ3D achieves comparable performance with the model trained with specific scene features when the image feature is excluded. | p. 13 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 9 / 4 Experiments - extractive PDF cue:** To further demonstrate the capability of PQ3D, we also transfer it to an embodied agent for object navigation using the ObjNav task from CortexBench [42] ...
- **p. 8 / 4 Experiments - extractive PDF cue:** 1 shows a summary of the datasets used for the multitask training of PQ3D.
- **p. 8 / 4 Experiments - extractive PDF cue:** Notably, we combine eight datasets for training, including about 662K training samples for various tasks.
- **p. 9 / 4 Experiments - extractive PDF cue:** Dataset Task Prompt Heads Size ScanNet200 [52] instance segmentation category mask,grounding 240K ScanRefer [6] visual grounding sentence grounding 37K Nr3D [2] visual grounding sentence grounding ...
- **p. 11 / 4 Experiments - extractive PDF cue:** Importantly, the performance of PQ3D trained on multiple tasks and datasets exceeds that of PQ3D trained on a single task and dataset, showcasing the effectiveness ...
- **p. 10 / 4 Experiments - extractive PDF cue:** Zhu et al. of-distribution dataset Replica [55].
- **p. 10 / 4 Experiments - extractive PDF cue:** These findings imply a notable capability of PQ3D for effective transfer to different datasets.
- **p. 11 / 4 Experiments - extractive PDF cue:** The notation "PQ3D (sg.)" indicates a model trained on a single dataset rather than through unified joint training.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: PQ3D is a unified model for 3D vision-language understanding, capable of taking various prompts (object categories, referring sentences, images, locations) to perform a ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Fig. 2: Comparison between PQ3D and other models. (a) When comparing PQ3D to other state-of-the-art (SOTA) methods, PQ3D demonstrates superior performance on most tasks. (b) ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 3: The model architecture of PQ3D, which consists of Task Prompt Encoding, 3D Scene Encoding, and Prompt-guided Query Learning modules. In prompt encoding, task ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 1: Datasets for unified training. The size of ScanNet200 is #scenes (1202)× #categories (200).
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 2: Instance Segmentation results on the ScanNet200 validation set and zero-shot performance on Replica. The Average Precision (AP) is averaged over an overlapping range, ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 3: Grounding accuracy (%) on 3D visual grounding benchmarks. The results of ScanRefer and Multi3DRefer are reported under IoU@0.5. The results of Nr3D and ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 4: Answer accuracy on ScanQA. Each entry denotes "test w/ object" and "test w/o object". EM@1 refers to the top 1 exact match accuracy, ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 5: Answer accuracy on SQA3D under question types.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To further demonstrate the capability of PQ3D, we also transfer it to an embodied agent for object navigation using the ObjNav task from CortexBench ... | embodiment, simulator version and control stack | p. 9 (4 Experiments), p. 8 (4 Experiments) |
| Task/environment | 1 shows a summary of the datasets used for the multitask training of PQ3D. | reset, timeout, object/scene variation | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 6 (3 Method), p. 8 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 8 (3 Method), p. 6 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The proposed PQ3D provides global 3D features to the navigation agent that can improve the baseline VC-1 by a significant margin, achieving a 22.9% ... | definition/direction/unit from same section | p. 11 (4 Experiments) |
| Table 4: Answer accuracy on ScanQA. Each entry denotes "test w/ object" and "test w/o object". EM@1 refers to the top 1 exact match ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| Model Success ↑SPL ↑Soft-SPL ↑ VC-1 (ViT-B) [42] 57.1 0.31 0.41 PQ3D 80.0 0.50 0.60 PQ3D w/o GPS∗ 75.0 0.45 0.50 4.3 Ablation study ... | definition/direction/unit from same section | p. 12 (4 Experiments) |
| Table 2: Instance Segmentation results on the ScanNet200 validation set and zero-shot performance on Replica. The Average Precision (AP) is averaged over an overlapping ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| 3 provides an assessment of grounding accuracy for various methods on four benchmarks: ScanRefer, Nr3D, Sr3D, and Multi3DRefer. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| 2, PQ3D demonstrates SOTA performance for instance segmentation tasks on ScanNet200. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Table 5: Answer accuracy on SQA3D under question types. | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| The loss balance weights λmask, λgen are set to 1, and λgrd is set to 10. | definition/direction/unit from same section | p. 9 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| On the ScanRefer, Nr3D, and Sr3D benchmarks, our model outperforms SOTA by 5.4%, 2.3%, and 3.3%, respectively. | comparison identity and matched condition | p. 10 (4 Experiments) |
| Fig. 2: Comparison between PQ3D and other models. (a) When comparing PQ3D to other state-of-the-art (SOTA) methods, PQ3D demonstrates superior performance on most tasks. ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |
| Our model consistently outperforms the other methods in most categories. | comparison identity and matched condition | p. 10 (4 Experiments) |
| Dense Captioning For the dense captioning task, PQ3D outperforms all other models in the CIDEr, METEOR, and ROUGE metrics. | comparison identity and matched condition | p. 11 (4 Experiments) |
| The proposed PQ3D provides global 3D features to the navigation agent that can improve the baseline VC-1 by a significant margin, achieving a 22.9% ... | comparison identity and matched condition | p. 11 (4 Experiments) |
| The results suggest that a 4-layer decoder outperforms both 2-layer and 6-layer ones on all tasks. | comparison identity and matched condition | p. 12 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 7: Results on ObjNav from CortexBench [42]. Note we reproduce the result of "VC-1 (ViT-B)" ourselves due to the slight mismatch we have ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| Table 8: Ablation study of scene features. Each entry denotes PQ3D "trained with specific scene features" and "trained with all features but some removed ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| 4: Ablation study of query decoder depth. | component/input/data sensitivity | p. 12 (4 Experiments) |
| Voxel Point Image Refer QA Caption ✓ 46.1 / 47.1 43.7 / 44.2 67.8 / 68.1 ✓ ✓ 49.2 / 49.4 45.4 / 45.8 ... | component/input/data sensitivity | p. 13 (4 Experiments) |
| Vacuum or sweep the floor to remove any dirt or debris. | component/input/data sensitivity | p. 14 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this section, we present PQ3D, which consists of three main modules: Task Prompt Encoding, 3D Scene Encoding, and Prompt-guided Query Learning, as depicted ... | Furthermore, on the Multi3DRefer benchmark, our model outperforms others in the ST (single target) and MT (multiple targets) categories and achieves the highest average ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (4 Experiments), p. 11 (4 Experiments), p. 13 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 9 (4 Experiments) |
| Primary metric/result | The proposed PQ3D provides global 3D features to the navigation agent that can improve the baseline VC-1 by a significant margin, achieving a 22.9% ... | numeric claim only at cited anchor | p. 11 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 9 / 4 Experiments - extractive PDF cue:** In the first stage, we train the model with instance segmentation alone on ScanNet200 for 800 epochs.
- **p. 5 / 3 Method - extractive PDF cue:** 3.1 Task Prompt Encoding In various 3D-VL tasks, a task prompt can be of diverse formats, including object categories, referring sentences, questions, 3D bounding boxes, ...
- **p. 7 / 3 Method - extractive PDF cue:** For each segment, we sample 1,024 points, normalize their coordinates into a unit sphere and then feed them into a pre-trained PointNet++ backbone [46, 47] ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, our model trained only on the Multi3DRefer dataset "PQ3D (sg.)" exhibits better performance in the ZT and MT metric, but falls short of ... | p. 10 (4 Experiments) |
| body limitation/failure cue | As our model utilizes the CLIP text encoder, it may face limitations in understanding long sentences. | p. 11 (4 Experiments) |
| body limitation/failure cue | Different from 3D-VisTA, our model does not use a classification head for QA, which causes a performance drop in EM metric. | p. 10 (4 Experiments) |
| body limitation/failure cue | 5 Conclusions and Future Works In conclusion, our proposed PQ3D addresses the challenges in 3D vision-language learning (3D-VL) by offering a unified approach that ... | p. 14 (4. Adjust the temperature or settings of the heater) |
| body limitation/failure cue | However, our model's performance with tail classes is relatively less robust due to biases in the CLIP text encoder, which is analyzed in the ... | p. 9 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We utilize the AdamW optimizer with a learning rate of 1e-4, batch size of 16, β1 = 0.9, and β2 = 0.98. | p. 9 (4 Experiments) |
| In our implementation, We compute the average coordinate across all points within each segment as its 3D location, which is further encoded by an ... | p. 7 (3 Method) |
| We set the hidden dimension D to 768, and query decoder layer N to 4. | p. 9 (4 Experiments) |
| As our model utilizes the CLIP text encoder, it may face limitations in understanding long sentences. | p. 11 (4 Experiments) |
| 4: Ablation study of query decoder depth. | p. 12 (4 Experiments) |
| Consequently, we choose a 4-layer query decoder for PQ3D. | p. 12 (4 Experiments) |
| We encode the textual and visual prompts by the pre-trained CLIP | p. 5 (3 Method) |
| The encoded task prompt is denoted as t ∈RT ×D, T is the number of prompt tokens, and D is the hidden dimension. | p. 6 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 4 Experiments - extractive PDF cue:** However, our model trained only on the Multi3DRefer dataset "PQ3D (sg.)" exhibits better performance in the ZT and MT metric, but falls short of the ...
- **p. 11 / 4 Experiments - extractive PDF cue:** As our model utilizes the CLIP text encoder, it may face limitations in understanding long sentences.
- **p. 10 / 4 Experiments - extractive PDF cue:** Different from 3D-VisTA, our model does not use a classification head for QA, which causes a performance drop in EM metric.
- **p. 14 / 4. Adjust the temperature or settings of the heater - extractive PDF cue:** 5 Conclusions and Future Works In conclusion, our proposed PQ3D addresses the challenges in 3D vision-language learning (3D-VL) by offering a unified approach that integrates ...
- **p. 9 / 4 Experiments - extractive PDF cue:** However, our model's performance with tail classes is relatively less robust due to biases in the CLIP text encoder, which is analyzed in the appendix.

- **PDF anchors reviewed:** datasets p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 11 (4 Experiments), p. 10 (4 Experiments), metrics p. 11 (4 Experiments), p. 11 (Figure/Table caption), p. 12 (4 Experiments), p. 10 (Figure/Table caption), p. 10 (4 Experiments), p. 9 (4 Experiments), baselines p. 10 (4 Experiments), p. 4 (Figure/Table caption), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), results p. 10 (4 Experiments), p. 11 (4 Experiments), p. 13 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 9 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
