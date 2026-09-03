# Evaluation - Open-Vocabulary Octree-Graph for 3D Scene Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Open-Vocabulary_Octree-Graph_for_3D_Scene_Understanding_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 7 (4.4. Ablation Studies), p. 6 (4.3. Quantitative Comparison), p. 7 (4.4. Ablation Studies), p. 5 (4.2. Dataset and Evaluation Metrics), p. 5 (4.2. Dataset and Evaluation Metrics)): Table 4. Path planning results on HM3DSem. SR denotes success rate (%). s is the threshold within which the distance between the navigation endpoint and the destination is considered successful. ...

## Evaluation Body Digest

- **p. 5 / 4.2. Dataset and Evaluation Metrics - extractive body cue:** For the path planning task, we employ the HM3DSem [46] dataset used in HOV-SG [44], where 8 scenes are selected for evaluation.
- **p. 5 / 4.2. Dataset and Evaluation Metrics - extractive body cue:** For zero-shot 3D instance segmentation, we assess our method on the widely-used ScanNet200 [36] benchmark, including a validation set of 312 scenes with 200 categories.
- **p. 6 / 4.2. Dataset and Evaluation Metrics - extractive body cue:** Text-based object retrieval results on the Sr3D dataset.
- **p. 6 / 4.3. Quantitative Comparison - extractive body cue:** Compared to the existing SoTA 3D scene graph, HOV-SG [44], we achieve +8.9% mIoU and +11.0% mAcc on the Replica dataset.
- **p. 7 / 4.3. Quantitative Comparison - extractive body cue:** For each sense in the HM3DSem [46] dataset, we randomly select 100 pairs of starting points and destinations in navigable areas.
- **p. 8 / 4.4. Ablation Studies - extractive body cue:** This is crucial for real-world deployment.
- **p. 8 / 4.5. Qualitative Analysis - extractive body cue:** We also conduct real-world experiments to further validate the effectiveness of our method.
- **p. 7 / 4.3. Quantitative Comparison - extractive body cue:** HOV-SG [44] can be directly used for path planning, thus it is evaluated and compared with our method in this task.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiment (p. 5); 4.1. Implementation Details (p. 5); 4.2. Dataset and Evaluation Metrics (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4. Path planning results on HM3DSem. SR denotes success rate (%). s is the threshold within which the distance between the navigation endpoint ... | p. 6 (Figure/Table caption) |
| 4.4. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | By contrast, our IFA achieves an improvement of 1.8% mIoU over Row 1. | p. 7 (4.4. Ablation Studies) |
| 4.3. Quantitative Comparison | EMPIRICAL / REAL-ROBOT OR HARDWARE | It can be seen that our method significantly outperforms exMethod SR(s=1.0m) SR(s=0.5m) SR(s=0.25m) HOV-SG [44] 55.25 46.75 32.16 Ours 97.88 96.88 96.38 Table 4. | p. 6 (4.3. Quantitative Comparison) |
| 4.4. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | Row 1 is equipped with our semantic-guided under-segment filtering, and achieves +0.9% mIoU and +1.0% mAcc. | p. 7 (4.4. Ablation Studies) |
| 4.2. Dataset and Evaluation Metrics | EMPIRICAL / REAL-ROBOT OR HARDWARE | Following the mainstream evaluation metrics [44], we assess 3D semantic segmentation results via commonly used mean IoU (mIoU), frequency-weighted mean IoU (F-mIoU), and mean ... | p. 5 (4.2. Dataset and Evaluation Metrics) |

## Dataset / Benchmark Role

- **p. 5 / 4.2. Dataset and Evaluation Metrics - extractive body cue:** For the path planning task, we employ the HM3DSem [46] dataset used in HOV-SG [44], where 8 scenes are selected for evaluation.
- **p. 5 / 4.2. Dataset and Evaluation Metrics - extractive body cue:** For zero-shot 3D instance segmentation, we assess our method on the widely-used ScanNet200 [36] benchmark, including a validation set of 312 scenes with 200 categories.
- **p. 6 / 4.2. Dataset and Evaluation Metrics - extractive body cue:** Text-based object retrieval results on the Sr3D dataset.
- **p. 6 / 4.3. Quantitative Comparison - extractive body cue:** Compared to the existing SoTA 3D scene graph, HOV-SG [44], we achieve +8.9% mIoU and +11.0% mAcc on the Replica dataset.
- **p. 7 / 4.3. Quantitative Comparison - extractive body cue:** For each sense in the HM3DSem [46] dataset, we randomly select 100 pairs of starting points and destinations in navigable areas.
- **p. 8 / 4.4. Ablation Studies - extractive body cue:** This is crucial for real-world deployment.
- **p. 8 / 4.5. Qualitative Analysis - extractive body cue:** We also conduct real-world experiments to further validate the effectiveness of our method.
- **p. 7 / 4.3. Quantitative Comparison - extractive body cue:** HOV-SG [44] can be directly used for path planning, thus it is evaluated and compared with our method in this task.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. (a) A 3D scene. (b) The corresponding semantic 3D map based on point clouds (6.8M). (c) Our Octree-Graph where each object is represented ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of our Octree-Graph. (a) Chronological Group-wise Segment Merging (CGSM). Given posed RGB-D inputs, 2D masks with semantic features are first extracted and ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Illustration of group split and CGSM merging.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Illustration of the nodes and edges in Octree-Graph. where cos(·) denotes cosine similarity, and av i,j is normal- ized via softmax. Intuitively, a ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. Illustration of the construction of the adaptive-octree. The above displays the process, and the below shows an example. 5, an adaptive-octree is constructed ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Zero-shot 3D semantic segmentation results on Replica and ScanNet benchmark.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. 3D instance segmentation results on ScanNet200. sup. means supervised training, z.s. denotes the zero-shot setting.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Text-based object retrieval results on the Sr3D dataset.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For the path planning task, we employ the HM3DSem [46] dataset used in HOV-SG [44], where 8 scenes are selected for evaluation. | embodiment, simulator version and control stack | p. 5 (4.2. Dataset and Evaluation Metrics), p. 5 (4.2. Dataset and Evaluation Metrics) |
| Task/environment | For zero-shot 3D instance segmentation, we assess our method on the widely-used ScanNet200 [36] benchmark, including a validation set of 312 scenes with 200 ... | reset, timeout, object/scene variation | p. 5 (4.2. Dataset and Evaluation Metrics), p. 6 (4.2. Dataset and Evaluation Metrics) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 4 (3.3. Chronological Group-wise Segment Merging) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 4 (3.5. Octree-Graph Construction and Applications) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| SR denotes success rate (%). s is the threshold within which the distance between the navigation endpoint and the destination is considered successful. isting ... | definition/direction/unit from same section | p. 6 (4.3. Quantitative Comparison) |
| Following the mainstream evaluation metrics [44], we assess 3D semantic segmentation results via commonly used mean IoU (mIoU), frequency-weighted mean IoU (F-mIoU), and mean ... | definition/direction/unit from same section | p. 5 (4.2. Dataset and Evaluation Metrics) |
| For 3D instance segmentation, we report the standard Average Precision (AP) at IoU thresholds 25% and 50%, along with the mean of AP from ... | definition/direction/unit from same section | p. 5 (4.2. Dataset and Evaluation Metrics) |
| Ablation study on the segment merging strategy and different temporal intervals for group partitioning of our CGSM. under-segment filtering threshold decay mIoU↑F-IoU↑mAcc↑ ✗ ✗ ... | definition/direction/unit from same section | p. 7 (4.3. Quantitative Comparison) |
| 8 provides a comparison of different spatial representations with respect to storage space and the accuracy of occupancy. | definition/direction/unit from same section | p. 7 (4.4. Ablation Studies) |
| We attribute the performance gain to our accurate semantic object segmentation and the rich relations stored in the Octree-Graph. | definition/direction/unit from same section | p. 6 (4.3. Quantitative Comparison) |
| 7, robots can accurately find the target and successfully navigate to it relying on our Octree-Graph. | definition/direction/unit from same section | p. 8 (4.5. Qualitative Analysis) |
| We can see that our method exhibits more accurate object semantics and fewer incorrect segments than comparison methods. | definition/direction/unit from same section | p. 8 (4.5. Qualitative Analysis) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to the existing SoTA 3D scene graph, HOV-SG [44], we achieve +8.9% mIoU and +11.0% mAcc on the Replica dataset. | comparison identity and matched condition | p. 6 (4.3. Quantitative Comparison) |
| 8 demonstrates the segment merging results of our CGSM and its baseline (i.e., frame-wise sequential merging), where CGSM correctly resolves the over-segmented long table ... | comparison identity and matched condition | p. 8 (4.5. Qualitative Analysis) |
| It can be seen that our method significantly outperforms exMethod SR(s=1.0m) SR(s=0.5m) SR(s=0.25m) HOV-SG [44] 55.25 46.75 32.16 Ours 97.88 96.88 96.38 Table 4. | comparison identity and matched condition | p. 6 (4.3. Quantitative Comparison) |
| Row 0 serves as a fixed-threshold group-wise merging baseline with no extra design. | comparison identity and matched condition | p. 7 (4.4. Ablation Studies) |
| However, at the same depth, the adaptive-octree exhibits a much higher mEOR compared to the octree. | comparison identity and matched condition | p. 7 (4.4. Ablation Studies) |
| To further verify the efficiency of our method, we conduct path planning experiments using A* [9] and Jump Point Search [52] algorithms on the ... | comparison identity and matched condition | p. 8 (4.4. Ablation Studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We compare our method with different SOTA methods in these tasks, and conduct comprehensive ablation studies to investigate several key components, demonstrating the effectiveness ... | component/input/data sensitivity | p. 5 (4. Experiment) |
| Effect of Instance Feature Aggregation. | component/input/data sensitivity | p. 7 (4.4. Ablation Studies) |
| When using supervised 3D models for proposal generation, our method significantly outperforms OpenMask3D [40] and the Open3DIS [29] variant with only the 3D proposals, ... | component/input/data sensitivity | p. 6 (4.3. Quantitative Comparison) |
| Ablation study on path planning efficiency. | component/input/data sensitivity | p. 7 (4.3. Quantitative Comparison) |
| 8 demonstrates the segment merging results of our CGSM and its baseline (i.e., frame-wise sequential merging), where CGSM correctly resolves the over-segmented long table ... | component/input/data sensitivity | p. 8 (4.5. Qualitative Analysis) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as follows. • We propose the Octree-Graph for open-vocabulary 3D scene understanding, which efficiently depicts objects' occupancies, semantics, and relations, ... | Table 4. Path planning results on HM3DSem. SR denotes success rate (%). s is the threshold within which the distance between the navigation endpoint ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 7 (4.4. Ablation Studies), p. 6 (4.3. Quantitative Comparison), p. 7 (4.4. Ablation Studies), p. 5 (4.2. Dataset and Evaluation Metrics), p. 5 (4.2. Dataset and Evaluation Metrics) |
| Primary metric/result | By contrast, our IFA achieves an improvement of 1.8% mIoU over Row 1. | numeric claim only at cited anchor | p. 7 (4.4. Ablation Studies) |

- Numeric sentences retained from the body:
- **p. 5 / 4.2. Dataset and Evaluation Metrics - extractive body cue:** For zero-shot 3D semantic segmentation, we evaluate our method on common scenes following [7, 15, 44], i.e., 8 scenes from Replica [39] dataset and 5 ...
- **p. 5 / 4.2. Dataset and Evaluation Metrics - extractive body cue:** For zero-shot 3D instance segmentation, we assess our method on the widely-used ScanNet200 [36] benchmark, including a validation set of 312 scenes with 200 categories.
- **p. 5 / 4.2. Dataset and Evaluation Metrics - extractive body cue:** For text-based object retrieval, we test our method on Sr3D [1] dataset, and follow the experiment setting of BBQ [23] that subsampled 526 free-form queries ...
- **p. 5 / 4.2. Dataset and Evaluation Metrics - extractive body cue:** For the path planning task, we employ the HM3DSem [46] dataset used in HOV-SG [44], where 8 scenes are selected for evaluation.
- **p. 7 / 4.3. Quantitative Comparison - extractive body cue:** Method Structure Storage↓time↓ A* Octree-Graph 268.41Kb 0.032s A* Point Cloud 71.16Mb 2.154s Jump Point Search Octree-Graph 268.41Kb 0.081s Jump Point Search Point Cloud 71.16Mb 2.153s ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We also analyze the impact of hyper-parameter I, and the results in Rows 3-5 show that our method exhibits robustness to I ranging from ... | p. 7 (4.4. Ablation Studies) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Based on these, we deploy our method on a robotic dog and a drone with NVIDIA Orin NX as onboard computers. | p. 8 (4.5. Qualitative Analysis) |
| Next, each mi is fed into the visual encoder and caption generator to obtain the visual feature f v i and caption feature f ... | p. 3 (3.2. Segment Proposal and Comprehension) |
| Regarding geometric similarity, we compute ϕiou geo(m, n) as the intersection over union of two segments. | p. 4 (3.3. Chronological Group-wise Segment Merging) |
| To merge the left segments, we compute an overall similarity ϕ = ϕiou geo + ϕior geo + ϕv sem + ϕc sem, and ... | p. 4 (3.3. Chronological Group-wise Segment Merging) |
| The size of each node in this adaptive-octree can be computed as follows: dl = (bmax -bmin) /2l, (2) where bmax and bmin are ... | p. 5 (3.5. Octree-Graph Construction and Applications) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4.4. Ablation Studies - extractive body cue:** We also analyze the impact of hyper-parameter I, and the results in Rows 3-5 show that our method exhibits robustness to I ranging from 100 ...

- **Evidence anchors reviewed:** datasets p. 5 (4.2. Dataset and Evaluation Metrics), p. 5 (4.2. Dataset and Evaluation Metrics), p. 6 (4.2. Dataset and Evaluation Metrics), p. 6 (4.3. Quantitative Comparison), p. 7 (4.3. Quantitative Comparison), p. 8 (4.4. Ablation Studies), metrics p. 6 (4.3. Quantitative Comparison), p. 5 (4.2. Dataset and Evaluation Metrics), p. 5 (4.2. Dataset and Evaluation Metrics), p. 7 (4.3. Quantitative Comparison), p. 7 (4.4. Ablation Studies), p. 6 (4.3. Quantitative Comparison), baselines p. 6 (4.3. Quantitative Comparison), p. 8 (4.5. Qualitative Analysis), p. 6 (4.3. Quantitative Comparison), p. 7 (4.4. Ablation Studies), p. 7 (4.4. Ablation Studies), p. 8 (4.4. Ablation Studies), results p. 6 (Figure/Table caption), p. 7 (4.4. Ablation Studies), p. 6 (4.3. Quantitative Comparison), p. 7 (4.4. Ablation Studies), p. 5 (4.2. Dataset and Evaluation Metrics), p. 5 (4.2. Dataset and Evaluation Metrics).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
