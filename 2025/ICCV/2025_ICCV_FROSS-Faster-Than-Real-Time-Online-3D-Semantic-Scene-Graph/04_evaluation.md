# Evaluation - FROSS: Faster-Than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (5 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 2 (7.3. 2D Scene Graph Generation Performance), p. 2 (Figure/Table caption), p. 1 (7.1. Object and Predicate Performance per Class), p. 1 (7.1. Object and Predicate Performance per Class), p. 3 (Figure/Table caption), p. 3 (8. Statistics of the ReplicaSSG Dataset)): The above observations reveal that the integration of RT-DETR as the object detection backbone results in substantial processing efficiency improvements, with only a slight impact on relationship prediction performance for ...

## Evaluation Body Digest

- **p. 2 / 7.1. Object and Predicate Performance per Class - extractive body cue:** Qualitative results of FROSS on four scenes in the ReplicaSSG dataset.
- **p. 5 / 8. Statistics of the ReplicaSSG Dataset - extractive body cue:** The number of objects present in each scene within the ReplicaSSG dataset.
- **p. 2 / 7.3. 2D Scene Graph Generation Performance - extractive body cue:** For these evaluations, the models tested on ReplicaSSG received training on the Visual Genome dataset, whereas the models tested on the other two datasets used ...
- **p. 1 / 7.1. Object and Predicate Performance per Class - extractive body cue:** In addition, FROSS's per-class object and predicate performance on the proposed ReplicaSSG dataset is presented in Table 8.
- **p. 3 / 8. Statistics of the ReplicaSSG Dataset - extractive body cue:** Evaluation results of two 2D SG generation models across three datasets. ‘RT-DETR+EGTR' represents the EGTR model with RT-DETR as its object detector backbone.
- **p. 4 / 8. Statistics of the ReplicaSSG Dataset - extractive body cue:** The occurrence frequency of each object category in the ReplicaSSG dataset.
- **p. 1 / 7.1. Object and Predicate Performance per Class - extractive body cue:** Despite retaining only the top seven most frequent relationships, the 3DSSG dataset still exhibits an extreme imbalance, with the top two classes occurring at substantially ...
- **p. 3 / 8. Statistics of the ReplicaSSG Dataset - extractive body cue:** Object Recall per Class bag bskt. bed bench bike book botl. bowl box cab. chair clock cntr. cup curt. desk door mean 25.0 50.0 0.0 ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 6. Detailed Evaluation Metric (p. 1); 7. Additional Experimental Results (p. 1); 7.2. Additional Qualitative Results (p. 2); 8. Statistics of the ReplicaSSG Dataset (p. 2).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 7.3. 2D Scene Graph Generation Performance | SYSTEM / EVALUATION SCOPE UNRESOLVED | The above observations reveal that the integration of RT-DETR as the object detection backbone results in substantial processing efficiency improvements, with only a slight ... | p. 2 (7.3. 2D Scene Graph Generation Performance) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 9. For these evaluations, the models tested on Repli- caSSG received training on the Visual Genome dataset, whereas the models tested on the ... | p. 2 (Figure/Table caption) |
| 7.1. Object and Predicate Performance per Class | SYSTEM / EVALUATION SCOPE UNRESOLVED | FROSS's ability to capture complex visual features leads to significantly higher performance in both object recall and mean recall. | p. 1 (7.1. Object and Predicate Performance per Class) |
| 7.1. Object and Predicate Performance per Class | SYSTEM / EVALUATION SCOPE UNRESOLVED | FROSS's predicate performance is significantly affected by class imbalance, excelling in relationship classes such as attached to, build in, and standing on, while performing ... | p. 1 (7.1. Object and Predicate Performance per Class) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 10. Per-class object detection performance in 2D SG generation with RT-DETR (AP@50). | p. 3 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 2 / 7.1. Object and Predicate Performance per Class - extractive body cue:** Qualitative results of FROSS on four scenes in the ReplicaSSG dataset.
- **p. 5 / 8. Statistics of the ReplicaSSG Dataset - extractive body cue:** The number of objects present in each scene within the ReplicaSSG dataset.
- **p. 2 / 7.3. 2D Scene Graph Generation Performance - extractive body cue:** For these evaluations, the models tested on ReplicaSSG received training on the Visual Genome dataset, whereas the models tested on the other two datasets used ...
- **p. 1 / 7.1. Object and Predicate Performance per Class - extractive body cue:** In addition, FROSS's per-class object and predicate performance on the proposed ReplicaSSG dataset is presented in Table 8.
- **p. 3 / 8. Statistics of the ReplicaSSG Dataset - extractive body cue:** Evaluation results of two 2D SG generation models across three datasets. ‘RT-DETR+EGTR' represents the EGTR model with RT-DETR as its object detector backbone.
- **p. 4 / 8. Statistics of the ReplicaSSG Dataset - extractive body cue:** The occurrence frequency of each object category in the ReplicaSSG dataset.
- **p. 1 / 7.1. Object and Predicate Performance per Class - extractive body cue:** Despite retaining only the top seven most frequent relationships, the 3DSSG dataset still exhibits an extreme imbalance, with the top two classes occurring at substantially ...
- **p. 3 / 8. Statistics of the ReplicaSSG Dataset - extractive body cue:** Object Recall per Class bag bskt. bed bench bike book botl. bowl box cab. chair clock cntr. cup curt. desk door mean 25.0 50.0 0.0 ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Table 6. Per-class performance comparison of 3D SSG generation methods on 3DSSG for object recall (%). The best and second-best results are highlighted in red, ...
- **p. 1 / Figure/Table caption - extractive body cue:** Table 7. Per-class performance comparison of 3D SSG generation methods on 3DSSG for predicate recall (%). The best and second-best results are highlighted in red, ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative results of FROSS on four scenes in the ReplicaSSG dataset. Please note that only representative objects are visualized, with misclassified objects marked ...
- **p. 2 / Figure/Table caption - extractive body cue:** Table 9. For these evaluations, the models tested on Repli- caSSG received training on the Visual Genome dataset, whereas the models tested on the other ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 8. Per-class performance comparison of FROSS on the ReplicaSSG dataset for object and predicate recall (%). Object Recall per Class bag bskt. bed bench ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 9. Evaluation results of two 2D SG generation models across three datasets. ‘RT-DETR+EGTR' represents the EGTR model with RT-DETR as its object detector backbone. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 10. Per-class object detection performance in 2D SG generation with RT-DETR (AP@50).
- **p. 3 / Figure/Table caption - extractive body cue:** Table 11. Per-class relationship extraction performance in 2D SG generation with RT-DETR+EGTR (Recall@K).

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Qualitative results of FROSS on four scenes in the ReplicaSSG dataset. | embodiment, simulator version and control stack | p. 2 (7.1. Object and Predicate Performance per Class), p. 5 (8. Statistics of the ReplicaSSG Dataset) |
| Task/environment | The number of objects present in each scene within the ReplicaSSG dataset. | reset, timeout, object/scene variation | p. 5 (8. Statistics of the ReplicaSSG Dataset), p. 2 (7.3. 2D Scene Graph Generation Performance) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 1 (Body text (section not recovered)), p. 2 (8. Statistics of the ReplicaSSG Dataset) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | 본문 anchor 없음 |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Specifically, for a detected triplet in which both the subject and object match ground truth objects, only the predicted class labels for the subject, ... | definition/direction/unit from same section | p. 1 (6. Detailed Evaluation Metric) |
| Per-class performance comparison of 3D SSG generation methods on 3DSSG for object recall (%). | definition/direction/unit from same section | p. 1 (7.1. Object and Predicate Performance per Class) |
| These results further demonstrate FROSS's robustness in diverse scene conditions. | definition/direction/unit from same section | p. 2 (7.2. Additional Qualitative Results) |
| Moreover, both models were optimized and accelerated using TensorRT3. | definition/direction/unit from same section | p. 2 (7.3. 2D Scene Graph Generation Performance) |
| Per-class performance comparison of FROSS on the ReplicaSSG dataset for object and predicate recall (%). | definition/direction/unit from same section | p. 3 (8. Statistics of the ReplicaSSG Dataset) |
| Table 11. Per-class relationship extraction performance in 2D SG generation with RT-DETR+EGTR (Recall@K). | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The per-class performance comparison of FROSS and other baselines is presented in Tables 6 and 7. | comparison identity and matched condition | p. 1 (7.1. Object and Predicate Performance per Class) |
| Per-class performance comparison of 3D SSG generation methods on 3DSSG for object recall (%). | comparison identity and matched condition | p. 1 (7.1. Object and Predicate Performance per Class) |
| Per-class performance comparison of FROSS on the ReplicaSSG dataset for object and predicate recall (%). | comparison identity and matched condition | p. 3 (8. Statistics of the ReplicaSSG Dataset) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The latter replaces the object detection backbone in the original EGTR with RT-DETR [44] object detector. | component/input/data sensitivity | p. 2 (7.3. 2D Scene Graph Generation Performance) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this section, we present the evaluation of two models: the original EGTR [12] 2D SG generation model and our modified version employed in ... | The above observations reveal that the integration of RT-DETR as the object detection backbone results in substantial processing efficiency improvements, with only a slight ... | PDF body cue; verify exact table/figure and matched conditions | p. 2 (7.3. 2D Scene Graph Generation Performance), p. 2 (Figure/Table caption), p. 1 (7.1. Object and Predicate Performance per Class), p. 1 (7.1. Object and Predicate Performance per Class), p. 3 (Figure/Table caption), p. 3 (8. Statistics of the ReplicaSSG Dataset) |
| Primary metric/result | Table 9. For these evaluations, the models tested on Repli- caSSG received training on the Visual Genome dataset, whereas the models tested on the ... | numeric claim only at cited anchor | p. 2 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The only difference is the exclusion of the ‘none' relationship category, as FROSS does not predict it. | p. 1 (6. Detailed Evaluation Metric) |
| body limitation/failure cue | While addressing this issue could potentially enhance FROSS's performance, we leave it as future work, as class imbalance is not the primary focus of ... | p. 1 (7.1. Object and Predicate Performance per Class) |
| body limitation/failure cue | These results further demonstrate FROSS's robustness in diverse scene conditions. | p. 2 (7.2. Additional Qualitative Results) |
| body limitation/failure cue | Misclassified objects are likely caused by occlusions from certain viewpoints or unusual viewing angles. | p. 2 (7.2. Additional Qualitative Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Wu [35] also provided results evaluated under this protocol in their publicly released code. | p. 1 (6. Detailed Evaluation Metric) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / 6. Detailed Evaluation Metric - extractive body cue:** The only difference is the exclusion of the ‘none' relationship category, as FROSS does not predict it.
- **p. 1 / 7.1. Object and Predicate Performance per Class - extractive body cue:** While addressing this issue could potentially enhance FROSS's performance, we leave it as future work, as class imbalance is not the primary focus of this ...
- **p. 2 / 7.2. Additional Qualitative Results - extractive body cue:** These results further demonstrate FROSS's robustness in diverse scene conditions.
- **p. 2 / 7.2. Additional Qualitative Results - extractive body cue:** Misclassified objects are likely caused by occlusions from certain viewpoints or unusual viewing angles.

- **Evidence anchors reviewed:** datasets p. 2 (7.1. Object and Predicate Performance per Class), p. 5 (8. Statistics of the ReplicaSSG Dataset), p. 2 (7.3. 2D Scene Graph Generation Performance), p. 1 (7.1. Object and Predicate Performance per Class), p. 3 (8. Statistics of the ReplicaSSG Dataset), p. 4 (8. Statistics of the ReplicaSSG Dataset), metrics p. 1 (6. Detailed Evaluation Metric), p. 1 (7.1. Object and Predicate Performance per Class), p. 2 (7.2. Additional Qualitative Results), p. 2 (7.3. 2D Scene Graph Generation Performance), p. 3 (8. Statistics of the ReplicaSSG Dataset), p. 3 (Figure/Table caption), baselines p. 1 (7.1. Object and Predicate Performance per Class), p. 1 (7.1. Object and Predicate Performance per Class), p. 3 (8. Statistics of the ReplicaSSG Dataset), results p. 2 (7.3. 2D Scene Graph Generation Performance), p. 2 (Figure/Table caption), p. 1 (7.1. Object and Predicate Performance per Class), p. 1 (7.1. Object and Predicate Performance per Class), p. 3 (Figure/Table caption), p. 3 (8. Statistics of the ReplicaSSG Dataset).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
