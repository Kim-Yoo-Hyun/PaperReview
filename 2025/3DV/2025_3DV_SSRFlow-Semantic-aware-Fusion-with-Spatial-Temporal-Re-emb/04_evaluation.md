# Evaluation - SSRFlow: Semantic-aware Fusion with Spatial Temporal Re-embedding for Real-world Scene Flow

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=9abfUtE6iQ&name=pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 8 (4 Experiments), p. 3 (Figure/Table caption), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments)): Figure 6: Illustration of results on other datasets of our proposed SSRFlow method. Colors mean the same as Figure 5. More visualization results are exhibited in Appendix, Sec F FT3Do ...

## Evaluation Body Digest

- **p. 7 / 4 Experiments - extractive body cue:** (a) FT3Ds (b) KITTIs (c) SF-KITTI (d) LiDAR-KITTI Figure 4: Comparisons of scene flow datasets, including (a) synthetic stereo, (b) real-world stereo, and (c)(d) real-world ...
- **p. 6 / 4 Experiments - extractive body cue:** (2016) and three real-world datasets including Stereo-KITTI Menze et al.
- **p. 8 / 4 Experiments - extractive body cue:** The quantitative results presented in Table 1 indicate that SSRFlow outperforms the other methods by a large margin, especially in real-world datasets.
- **p. 8 / 4 Experiments - extractive body cue:** Furthermore, SSRFlow outperforms Cheng and Ko (2023) by a significant margin, surpassing it by 33% and 40% in terms of EPE3D and Out3D on the ...
- **p. 9 / 4 Experiments - extractive body cue:** Model EPE3D↓Param size (M) Run time (ms) PointPWC 0.0588 7.72M 76ms PointPWC+STR 0.0504 8.02M 81ms PointPWC+STR+GF 0.0402 9.89M 96ms Bi-PointflowNet 0.0282 7.96M 80ms Bi-PointFlow+GF 0.0227 ...
- **p. 6 / 4 Experiments - extractive body cue:** 4.1 Datasets and Data Preprocessing The experiments were performed on four datasets: the synthetic dataset FlyThings3D (FT3D) Mayer et al.
- **p. 7 / 4 Experiments - extractive body cue:** These datasets are preprocessed in two ways Gu et al.
- **p. 9 / 4 Experiments - extractive body cue:** Specifically, SSRFlow reduces EPE3D by 41% and 22% compared to the second place Cheng and Ko (2023) under training on FT3Ds and SF-KITTI datasets, respectively.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 6); B Experiments Settings (p. 13); B.1 Evaluation Metrics (p. 13).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 6: Illustration of results on other datasets of our proposed SSRFlow method. Colors mean the same as Figure 5. More visualization results are ... | p. 8 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The quantitative results presented in Table 1 indicate that SSRFlow outperforms the other methods by a large margin, especially in real-world datasets. | p. 8 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1: Illustration of the proposed network. Firstly, semantic features are hierarchically extracted and sent to GF to achieve global embedding between the two ... | p. 3 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The best results for each dataset are marked in bold. * denotes the methods with an inference time exceeding 250 ms. | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The comprehensive results of the ablation experiments can be found in Table 5, while detailed information is presented in Table 6 and Table 7. | p. 9 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiments - extractive body cue:** (a) FT3Ds (b) KITTIs (c) SF-KITTI (d) LiDAR-KITTI Figure 4: Comparisons of scene flow datasets, including (a) synthetic stereo, (b) real-world stereo, and (c)(d) real-world ...
- **p. 6 / 4 Experiments - extractive body cue:** (2016) and three real-world datasets including Stereo-KITTI Menze et al.
- **p. 8 / 4 Experiments - extractive body cue:** The quantitative results presented in Table 1 indicate that SSRFlow outperforms the other methods by a large margin, especially in real-world datasets.
- **p. 8 / 4 Experiments - extractive body cue:** Furthermore, SSRFlow outperforms Cheng and Ko (2023) by a significant margin, surpassing it by 33% and 40% in terms of EPE3D and Out3D on the ...
- **p. 9 / 4 Experiments - extractive body cue:** Model EPE3D↓Param size (M) Run time (ms) PointPWC 0.0588 7.72M 76ms PointPWC+STR 0.0504 8.02M 81ms PointPWC+STR+GF 0.0402 9.89M 96ms Bi-PointflowNet 0.0282 7.96M 80ms Bi-PointFlow+GF 0.0227 ...
- **p. 6 / 4 Experiments - extractive body cue:** 4.1 Datasets and Data Preprocessing The experiments were performed on four datasets: the synthetic dataset FlyThings3D (FT3D) Mayer et al.
- **p. 7 / 4 Experiments - extractive body cue:** These datasets are preprocessed in two ways Gu et al.
- **p. 9 / 4 Experiments - extractive body cue:** Specifically, SSRFlow reduces EPE3D by 41% and 22% compared to the second place Cheng and Ko (2023) under training on FT3Ds and SF-KITTI datasets, respectively.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1: Illustration of the proposed network. Firstly, semantic features are hierarchically extracted and sent to GF to achieve global embedding between the two point ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Flowchart of global flow embedding. ⊗and ⊕denote multiplication and concatenation, respectively. Specifically, within the DCA module, we employ a cross-attentive mechanism to merge ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: The details of STR module. 2.5 Spatial Temporal Re-embedding After the warping layer, the spatiotemporal relation between the consecutive frames may change. Specifically, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Comparisons of scene flow datasets, including (a) synthetic stereo, (b) real-world stereo, and (c)(d) real-world LiDAR-scanned. Blue and purple denote the source and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Performance comparisons on the FT3Ds and KITTIs datasets. All models in the table are only trained on FT3Ds and no fine-tuning is applied ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. These datasets are preprocessed in two ways Gu et al. (2019); Liu et al. (2019): FT3Ds and KITTIs remove non-corresponding points between consecutive ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Runtime and performance of the methods evaluated on KITTIs.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3: Comparisons on the FT3Do and KITTIo datasets. All methods are trained only on FT3Do. Dataset Method EPE3D↓AS3D↑AR3D↑Out3D↓ FT3Do WM3DSFWang et al. (2022a) 0.0630 ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | (a) FT3Ds (b) KITTIs (c) SF-KITTI (d) LiDAR-KITTI Figure 4: Comparisons of scene flow datasets, including (a) synthetic stereo, (b) real-world stereo, and (c)(d) ... | embodiment, simulator version and control stack | p. 7 (4 Experiments), p. 6 (4 Experiments) |
| Task/environment | (2016) and three real-world datasets including Stereo-KITTI Menze et al. | reset, timeout, object/scene variation | p. 6 (4 Experiments), p. 8 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (2 Methodology), p. 2 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (2 Methodology), p. 4 (2 Methodology) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| After removing the DCA Fusion, the model experienced a substantial decline in accuracy, primarily due to its capability to fuse point features with another ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Figure 9: The differences of ground truth scene flow local consistency under different nearest point search methods. The normalized value is shown in the ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| The AdamW optimizer Loshchilov and Hutter (2017) with β1 = 0.9 and β2 = 0.99 is used for model tuning during the training phase, ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| The experimental results are listed in Table 3, which reveal the good performance of our model even with occlusion. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Further, our model exhibits exceptional generalization performance on the KITTIs dataset, surpassing the second place by 50% on EPE3D. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| 4.4 Ablation Study To investigate the distinct impacts of GF, STR, and DA Losses, a set of ablation experiments are conducted to perform functional ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Figure 2: Flowchart of global flow embedding. ⊗and ⊕denote multiplication and concatenation, respectively. Specifically, within the DCA module, we employ a cross-attentive mechanism to ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Table 2: Runtime and performance of the methods evaluated on KITTIs. | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 6: Illustration of results on other datasets of our proposed SSRFlow method. Colors mean the same as Figure 5. More visualization results are ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| The quantitative results presented in Table 1 indicate that SSRFlow outperforms the other methods by a large margin, especially in real-world datasets. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Specifically, SSRFlow reduces EPE3D by 41% and 22% compared to the second place Cheng and Ko (2023) under training on FT3Ds and SF-KITTI datasets, ... | comparison identity and matched condition | p. 9 (4 Experiments) |
| (2023) 0.0224 376ms MSBRNCheng and Ko (2023) 0.0118 275ms SSRFlow (Ours) 0.0059 101ms Table 3: Comparisons on the FT3Do and KITTIo datasets. | comparison identity and matched condition | p. 7 (4 Experiments) |
| (a) FT3Ds (b) KITTIs (c) SF-KITTI (d) LiDAR-KITTI Figure 4: Comparisons of scene flow datasets, including (a) synthetic stereo, (b) real-world stereo, and (c)(d) ... | comparison identity and matched condition | p. 7 (4 Experiments) |
| The comprehensive results of the ablation experiments can be found in Table 5, while detailed information is presented in Table 6 and Table 7. | comparison identity and matched condition | p. 9 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| More visualization results are exhibited in Appendix, Sec F FT3Do and KITTIo Similar to the above, we train our model on FT3Do and test ... | component/input/data sensitivity | p. 8 (4 Experiments) |
| Lcfs Llfs KNN Radius FT3Ds EPE3D↓ KITTIs EPE3D↓ ✔ ✔ ✔ 0.0171 0.0109 ✔ ✔ ✔ 0.0169 0.0101 ✔ ✔ ✔ 0.0136 0.0082 ✔ ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| (2019): FT3Ds and KITTIs remove non-corresponding points between consecutive frames, while FT3Do and KITTIo retain occluded points using mask labels. | component/input/data sensitivity | p. 7 (4 Experiments) |
| The comprehensive results of the ablation experiments can be found in Table 5, while detailed information is presented in Table 6 and Table 7. | component/input/data sensitivity | p. 9 (4 Experiments) |
| Figure 10: Ablation studies and analysis of adaption losses. From Figure 9 it can be observed that using only KNN introduces noise points that ... | component/input/data sensitivity | p. 15 (Figure/Table caption) |
| All models in the table are only trained on FT3Ds and no fine-tuning is applied when tested on KITTIs. | component/input/data sensitivity | p. 7 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Overall, our contributions are as follows: • Our GF module leverages the dual cross-attentive mechanism to fuse and align the semantic context from both ... | Figure 6: Illustration of results on other datasets of our proposed SSRFlow method. Colors mean the same as Figure 5. More visualization results are ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 8 (4 Experiments), p. 3 (Figure/Table caption), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Primary metric/result | The quantitative results presented in Table 1 indicate that SSRFlow outperforms the other methods by a large margin, especially in real-world datasets. | numeric claim only at cited anchor | p. 8 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive body cue:** The best results for each dataset are marked in bold. * denotes the methods with an inference time exceeding 250 ms.
- **p. 7 / 4 Experiments - extractive body cue:** (2020) 0.0694 76ms Bi-PointFlowCheng and Ko (2022) 0.0307 80ms WM3DSFWang et al.
- **p. 7 / 4 Experiments - extractive body cue:** (2023) 0.0224 376ms MSBRNCheng and Ko (2023) 0.0118 275ms SSRFlow (Ours) 0.0059 101ms Table 3: Comparisons on the FT3Do and KITTIo datasets.
- **p. 7 / 4 Experiments - extractive body cue:** The AdamW optimizer Loshchilov and Hutter (2017) with β1 = 0.9 and β2 = 0.99 is used for model tuning during the training phase, with ...
- **p. 7 / 4 Experiments - extractive body cue:** We train our model in an end-to-end manner for 900 epochs (or reached convergence) with batch size 8.
- **p. 9 / 4 Experiments - extractive body cue:** Model EPE3D↓Param size (M) Run time (ms) PointPWC 0.0588 7.72M 76ms PointPWC+STR 0.0504 8.02M 81ms PointPWC+STR+GF 0.0402 9.89M 96ms Bi-PointflowNet 0.0282 7.96M 80ms Bi-PointFlow+GF 0.0227 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The KNN+Radius search strategy effectively mitigates the influence of noise points resulting from occlusion and sparsity in point clouds, as demonstrated in Sec B.2 ... | p. 6 (2 Methodology) |
| body limitation/failure cue | The experimental results are listed in Table 3, which reveal the good performance of our model even with occlusion. | p. 8 (4 Experiments) |
| body limitation/failure cue | Figure 10: Ablation studies and analysis of adaption losses. From Figure 9 it can be observed that using only KNN introduces noise points that ... | p. 15 (Figure/Table caption) |
| body limitation/failure cue | Figure 11: (a) The occlusion occurs between the source frame and the target frame. In this scenario, red bounding boxes delineate points in the ... | p. 16 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train our model in an end-to-end manner for 900 epochs (or reached convergence) with batch size 8. | p. 7 (4 Experiments) |
| The AdamW optimizer Loshchilov and Hutter (2017) with β1 = 0.9 and β2 = 0.99 is used for model tuning during the training phase, ... | p. 7 (4 Experiments) |
| Specifically, on the FT3Ds dataset, SSRFlow is on par with previous SOTACheng and Ko (2023) while achieving a 63% reduction in inference time, as ... | p. 8 (4 Experiments) |
| Our model code and weights will be released upon publication. | p. 8 (4 Experiments) |
| Secondly, we test the internal and external position encoder of cross-attention in DCA Fusion. | p. 9 (4 Experiments) |
| GF In (a) of Table 7, we provide a detailed list of the importance of the DCA Fusion, location of position encoder, aggregation style, ... | p. 9 (4 Experiments) |
| (4) The external position encoder PE∗instead of internal integration in the DCA module provides explicit position context during global flow embedding. | p. 4 (2 Methodology) |
| Firstly, to establish the relative positional association between each point-pair, a position encoder PE∗in Euclidean space is introduced as follows, where η denotes concatenation. | p. 4 (2 Methodology) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 2 Methodology - extractive body cue:** The KNN+Radius search strategy effectively mitigates the influence of noise points resulting from occlusion and sparsity in point clouds, as demonstrated in Sec B.2 of ...
- **p. 8 / 4 Experiments - extractive body cue:** The experimental results are listed in Table 3, which reveal the good performance of our model even with occlusion.
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 10: Ablation studies and analysis of adaption losses. From Figure 9 it can be observed that using only KNN introduces noise points that do ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 11: (a) The occlusion occurs between the source frame and the target frame. In this scenario, red bounding boxes delineate points in the source ...

- **Evidence anchors reviewed:** datasets p. 7 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 6 (4 Experiments), metrics p. 9 (4 Experiments), p. 14 (Figure/Table caption), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), baselines p. 8 (Figure/Table caption), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), results p. 8 (Figure/Table caption), p. 8 (4 Experiments), p. 3 (Figure/Table caption), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
