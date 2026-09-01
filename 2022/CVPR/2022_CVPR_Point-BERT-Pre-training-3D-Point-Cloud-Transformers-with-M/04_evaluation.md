# Evaluation - Point-BERT: Pre-training 3D Point Cloud Transformers with Masked Point Modeling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2111.14819; PDF retrieval source: https://arxiv.org/pdf/2111.14819. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4.4. Visualization), p. 6 (4.2. Downstream Tasks), p. 6 (4.2. Downstream Tasks), p. 2 (Figure/Table caption), p. 7 (4.2. Downstream Tasks), p. 7 (4.2. Downstream Tasks)): As can be seen, pre-training with our Point-BERT significantly improves the performance of baseline Transformers both in accuracy and speed on both synthetic and real-world datasets.

## Evaluation Body Digest

- **p. 8 / 4.4. Visualization - extractive PDF cue:** We compare the performance of Transformers training from scratch (blue) and pre-training with PointBERT (red) in terms of training loss and validation accuracy on synthetic ...
- **p. 7 / 4.2. Downstream Tasks - extractive PDF cue:** While the superiority is degraded on the real-world dataset ScanObjectNN.
- **p. 8 / 4.4. Visualization - extractive PDF cue:** As can be seen, pre-training with our Point-BERT significantly improves the performance of baseline Transformers both in accuracy and speed on both synthetic and real-world ...
- **p. 5 / 4.1. Pre-training Setups - extractive PDF cue:** ShapeNet [5] is used as our pre-training dataset, which covers over 50,000 unique 3D models from 55 common object categories.
- **p. 7 / 4.2. Downstream Tasks - extractive PDF cue:** Classification results on the ScanObjectNN dataset.
- **p. 6 / 4.2. Downstream Tasks - extractive PDF cue:** Besides the widely used benchmarks, including classification and segmentation, we also study the model's capacity on few-shot learning and transfer learning.
- **p. 5 / 4. Experiments - extractive PDF cue:** Then we evaluate the proposed model with various downstream tasks, including object classification, part segmentation, few-shot learning and transfer learning.
- **p. 6 / 4.2. Downstream Tasks - extractive PDF cue:** In this subsection, we report the experimental results on downstream tasks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 300 dataset (p. 11); 300 dataset (p. 12).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.4. Visualization | EMPIRICAL / REAL-ROBOT OR HARDWARE | As can be seen, pre-training with our Point-BERT significantly improves the performance of baseline Transformers both in accuracy and speed on both synthetic and ... | p. 8 (4.4. Visualization) |
| 4.2. Downstream Tasks | EMPIRICAL / REAL-ROBOT OR HARDWARE | When we increase the density of inputs (4096), our Point-BERT achieves significantly better performance (93.4%) than that with the baseline (91.2%) and OcCo (92.2%). | p. 6 (4.2. Downstream Tasks) |
| 4.2. Downstream Tasks | EMPIRICAL / REAL-ROBOT OR HARDWARE | We also observe that adding more points will not significantly improve the Transformer model without pre-training while Point-BERT models can be consistently improved by ... | p. 6 (4.2. Downstream Tasks) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 2. Masked point clouds reconstruction using our Point-BERT model trained on ShapeNet. We show the reconstruction results of synthetic objects from ShapeNet test ... | p. 2 (Figure/Table caption) |
| 4.2. Downstream Tasks | EMPIRICAL / REAL-ROBOT OR HARDWARE | As for Point-BERT, it achieves SOTA performance on both datasets, which strongly confirms the effectiveness of our method. | p. 7 (4.2. Downstream Tasks) |

## Dataset / Benchmark Role

- **p. 8 / 4.4. Visualization - extractive PDF cue:** We compare the performance of Transformers training from scratch (blue) and pre-training with PointBERT (red) in terms of training loss and validation accuracy on synthetic ...
- **p. 7 / 4.2. Downstream Tasks - extractive PDF cue:** While the superiority is degraded on the real-world dataset ScanObjectNN.
- **p. 8 / 4.4. Visualization - extractive PDF cue:** As can be seen, pre-training with our Point-BERT significantly improves the performance of baseline Transformers both in accuracy and speed on both synthetic and real-world ...
- **p. 5 / 4.1. Pre-training Setups - extractive PDF cue:** ShapeNet [5] is used as our pre-training dataset, which covers over 50,000 unique 3D models from 55 common object categories.
- **p. 7 / 4.2. Downstream Tasks - extractive PDF cue:** Classification results on the ScanObjectNN dataset.
- **p. 6 / 4.2. Downstream Tasks - extractive PDF cue:** Besides the widely used benchmarks, including classification and segmentation, we also study the model's capacity on few-shot learning and transfer learning.
- **p. 5 / 4. Experiments - extractive PDF cue:** Then we evaluate the proposed model with various downstream tasks, including object classification, part segmentation, few-shot learning and transfer learning.
- **p. 6 / 4.2. Downstream Tasks - extractive PDF cue:** In this subsection, we report the experimental results on downstream tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Illustration of our main idea. Point-BERT is designed for pre-training of standard point cloud Transformers. By training a dVAE via point cloud reconstruction, ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Masked point clouds reconstruction using our Point-BERT model trained on ShapeNet. We show the reconstruction results of synthetic objects from ShapeNet test set ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. The pipeline of Point-BERT. We first partition the input point cloud into several point patches (sub-clouds). A mini-PointNet [34] is then used to ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Comparisons of Point-BERT with of state-of-the-art models on ModelNet40. We report the classification accuracy (%) and the number of points in the input. ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Few-shot classification results on ModelNet40. We report the average accuracy (%) as well as the standard deviation over 10 independent experiments. 5-way 10-way ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Part segmentation results on the ShapeNetPart dataset. We report the mean IoU across all part categories mIoUC (%) and the mean IoU across ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4. Classification results on the ScanObjectNN dataset. We report the accuracy (%) of three different settings. Methods OBJ-BG OBJ-ONLY PB-T50-RS PointNet [34] 73.3
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 5. Ablation study. We investigate the effects of different designs and report the classification accuracy (%) after fine-tuning on ModelNet40. All models are trained ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We compare the performance of Transformers training from scratch (blue) and pre-training with PointBERT (red) in terms of training loss and validation accuracy on ... | embodiment, simulator version and control stack | p. 8 (4.4. Visualization), p. 7 (4.2. Downstream Tasks) |
| Task/environment | While the superiority is degraded on the real-world dataset ScanObjectNN. | reset, timeout, object/scene variation | p. 7 (4.2. Downstream Tasks), p. 8 (4.4. Visualization) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We compare the performance of Transformers training from scratch (blue) and pre-training with PointBERT (red) in terms of training loss and validation accuracy on ... | definition/direction/unit from same section | p. 8 (4.4. Visualization) |
| We report the average accuracy (%) as well as the standard deviation over 10 independent experiments. | definition/direction/unit from same section | p. 6 (4.2. Downstream Tasks) |
| As can be seen, pre-training with our Point-BERT significantly improves the performance of baseline Transformers both in accuracy and speed on both synthetic and ... | definition/direction/unit from same section | p. 8 (4.4. Visualization) |
| We report the classification accuracy (%) and the number of points in the input. | definition/direction/unit from same section | p. 6 (4.1. Pre-training Setups) |
| We report the accuracy (%) of three different settings. | definition/direction/unit from same section | p. 7 (4.2. Downstream Tasks) |
| We investigate the effects of different designs and report the classification accuracy (%) after fine-tuning on ModelNet40. | definition/direction/unit from same section | p. 7 (4.2. Downstream Tasks) |
| The commonly used ℓ1-style Chamfer Distance loss is employed during the reconstruction procedure. | definition/direction/unit from same section | p. 5 (4.1. Pre-training Setups) |
| The learning rate is set to 0.0005 with a cosine learning schedule with 60,000 steps warming up. | definition/direction/unit from same section | p. 5 (4.1. Pre-training Setups) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Additionally, we compare with a recent pre-training strategy OcCo [52] as a strong baseline of our pre-training method. | comparison identity and matched condition | p. 6 (4.2. Downstream Tasks) |
| Comparisons of Point-BERT with of state-of-the-art models on ModelNet40. | comparison identity and matched condition | p. 6 (4.1. Pre-training Setups) |
| It is clear that our Point-BERT outperforms PointNet, PointNet++, and DGCNN. | comparison identity and matched condition | p. 7 (4.2. Downstream Tasks) |
| Moreover, Point-BERT improves 0.69% and 0.5% mIoU over vanilla Transformers, while OcCo fails to improve baseline performance in part segmentation task. | comparison identity and matched condition | p. 7 (4.2. Downstream Tasks) |
| We denote model A as our baseline, which is the Transformer training from scratch. | comparison identity and matched condition | p. 8 (4.3. Ablation Study) |
| We also visualize the learning curves of our baseline Transformers and the proposed Point-BERT in Figure 5. | comparison identity and matched condition | p. 8 (4.4. Visualization) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 5. Ablation study. We investigate the effects of different designs and report the classification accuracy (%) after fine-tuning on ModelNet40. All models are ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| We also conduct an ablation study for our Point-BERT. | component/input/data sensitivity | p. 5 (4. Experiments) |
| We also observe that adding more points will not significantly improve the Transformer model without pre-training while Point-BERT models can be consistently improved by ... | component/input/data sensitivity | p. 6 (4.2. Downstream Tasks) |
| We follow previous works to conduct experiments on three main variants: OBJ-BG, OBJ-ONLY, and PB-T50-RS. | component/input/data sensitivity | p. 7 (4.2. Downstream Tasks) |
| In this section, we first introduce the setups of our pretraining scheme. | component/input/data sensitivity | p. 5 (4. Experiments) |
| As can be seen, features from different categories can be well separated by our method even before fine-tuning. | component/input/data sensitivity | p. 8 (4.4. Visualization) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Driven by the above analysis, we present Point-BERT, a new scheme for learning point cloud Transformers. | As can be seen, pre-training with our Point-BERT significantly improves the performance of baseline Transformers both in accuracy and speed on both synthetic and ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4.4. Visualization), p. 6 (4.2. Downstream Tasks), p. 6 (4.2. Downstream Tasks), p. 2 (Figure/Table caption), p. 7 (4.2. Downstream Tasks), p. 7 (4.2. Downstream Tasks) |
| Primary metric/result | When we increase the density of inputs (4096), our Point-BERT achieves significantly better performance (93.4%) than that with the baseline (91.2%) and OcCo (92.2%). | numeric claim only at cited anchor | p. 6 (4.2. Downstream Tasks) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Pre-training Setups - extractive PDF cue:** We sample 1024 points from each 3D model and divide them into 64 point patches (subclouds).
- **p. 5 / 4.1. Pre-training Setups - extractive PDF cue:** A lightweight PointNet [34] containing two-layer MLPs is adopted to project each sub-cloud into 64 point embeddings, which are used as input both for dVAE ...
- **p. 5 / 4.1. Pre-training Setups - extractive PDF cue:** We set the weight of KLD loss to 0 in the first 10,000 steps and gradually increased to 0.1 in the following 100,000 steps.
- **p. 5 / 4.1. Pre-training Setups - extractive PDF cue:** The learning rate is set to 0.0005 with a cosine learning schedule with 60,000 steps warming up.
- **p. 6 / 4.1. Pre-training Setups - extractive PDF cue:** PointNet [34] 1k 89.2 PointNet++ [35] 1k 90.5 SO-Net [22] 1k 92.5 PointCNN [23] 1k 92.2 DGCNN [54] 1k 92.9 DensePoint [24] 1k 92.8 RSCNN ...
- **p. 6 / 4.1. Pre-training Setups - extractive PDF cue:** We train dVAE for a total of 150,000 steps with a batch size of 64.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | It is worth noting that the performance of dVAE is susceptible to hyper-parameters, which makes that the configurations of image-based dVAE [37] cannot be ... | p. 5 (4.1. Pre-training Setups) |
| body limitation/failure cue | Moreover, Point-BERT improves 0.69% and 0.5% mIoU over vanilla Transformers, while OcCo fails to improve baseline performance in part segmentation task. | p. 7 (4.2. Downstream Tasks) |
| body limitation/failure cue | While the superiority is degraded on the real-world dataset ScanObjectNN. | p. 7 (4.2. Downstream Tasks) |
| body limitation/failure cue | Thus, randmask makes the task easier than block-mask, and further degrades the reconstruction performance. | p. 8 (4.3. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The learning rate is set to 0.0005 with a cosine learning schedule with 60,000 steps warming up. | p. 5 (4.1. Pre-training Setups) |
| The model is trained for 300 epochs with a batch size of 128. | p. 6 (4.1. Pre-training Setups) |
| We train dVAE for a total of 150,000 steps with a batch size of 64. | p. 6 (4.1. Pre-training Setups) |
| Our decoder is also a DGCNN architecture followed by a FoldingNet [59]. | p. 5 (4.1. Pre-training Setups) |
| Our Transformer encoder can reasonably infer the point tokens of the missing patches. | p. 8 (4.3. Ablation Study) |
| In practice, we reconstruct the local patches through the decoder of dVAE, based on the point tokens predicted by the Transformer encoder. | p. 8 (4.3. Ablation Study) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 4.1. Pre-training Setups - extractive PDF cue:** It is worth noting that the performance of dVAE is susceptible to hyper-parameters, which makes that the configurations of image-based dVAE [37] cannot be directly ...
- **p. 7 / 4.2. Downstream Tasks - extractive PDF cue:** Moreover, Point-BERT improves 0.69% and 0.5% mIoU over vanilla Transformers, while OcCo fails to improve baseline performance in part segmentation task.
- **p. 7 / 4.2. Downstream Tasks - extractive PDF cue:** While the superiority is degraded on the real-world dataset ScanObjectNN.
- **p. 8 / 4.3. Ablation Study - extractive PDF cue:** Thus, randmask makes the task easier than block-mask, and further degrades the reconstruction performance.

- **PDF anchors reviewed:** datasets p. 8 (4.4. Visualization), p. 7 (4.2. Downstream Tasks), p. 8 (4.4. Visualization), p. 5 (4.1. Pre-training Setups), p. 7 (4.2. Downstream Tasks), p. 6 (4.2. Downstream Tasks), metrics p. 8 (4.4. Visualization), p. 6 (4.2. Downstream Tasks), p. 8 (4.4. Visualization), p. 6 (4.1. Pre-training Setups), p. 7 (4.2. Downstream Tasks), p. 7 (4.2. Downstream Tasks), baselines p. 6 (4.2. Downstream Tasks), p. 6 (4.1. Pre-training Setups), p. 7 (4.2. Downstream Tasks), p. 7 (4.2. Downstream Tasks), p. 8 (4.3. Ablation Study), p. 8 (4.4. Visualization), results p. 8 (4.4. Visualization), p. 6 (4.2. Downstream Tasks), p. 6 (4.2. Downstream Tasks), p. 2 (Figure/Table caption), p. 7 (4.2. Downstream Tasks), p. 7 (4.2. Downstream Tasks).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
