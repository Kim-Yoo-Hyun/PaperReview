# Evaluation - SSCNet: Semantic Scene Completion from a Single Depth Image

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1611.08974; PDF retrieval source: https://arxiv.org/pdf/1611.08974. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5.1. Experimental results), p. 8 (5.1. Experimental results), p. 6 (5.1. Experimental results), p. 7 (5.1. Experimental results), p. 7 (5.1. Experimental results), p. 12 (Figure/Table caption)): Increasing the receptive field gives the network a opportunity to capture richer contextual information and significantly improve the network performance from 38.0% to 44.3%.

## Evaluation Body Digest

- **p. 6 / 5. Evaluation - extractive PDF cue:** The SUNCG test set consists of 500 depth images rendered from 184 scenes that are not in the training set.
- **p. 6 / 5. Evaluation - extractive PDF cue:** For the semantic scene completion task, we evaluate the IoU of each object classes on both the observed and occluded voxels.
- **p. 7 / 5.1. Experimental results - extractive PDF cue:** We examine to what extent the supervision of object semantics benefits the scene completion task.
- **p. 7 / 5.1. Experimental results - extractive PDF cue:** We evaluate on the rendered NYU benchmark with the same test images used by Firman at al.
- **p. 8 / 5.1. Experimental results - extractive PDF cue:** The following rows show the evaluation on semantic scene completion task.
- **p. 8 / 5.1. Experimental results - extractive PDF cue:** We see a performance gain by using additional synthetic data especially for the semantic scene completion task having an 10.3% improvement in IoU.
- **p. 6 / 5. Evaluation - extractive PDF cue:** As our evaluation metric, we use the voxel-level intersection over union (IoU) of predicted voxel method training prec. recall IoU Zheng et al.
- **p. 8 / 5.1. Experimental results - extractive PDF cue:** We observe that removing the view dependency by using the accurate TSDF gives a 2.4% improvement in IoU.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Evaluation (p. 6); 5.1. Experimental results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.1. Experimental results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Increasing the receptive field gives the network a opportunity to capture richer contextual information and significantly improve the network performance from 38.0% to 44.3%. | p. 8 (5.1. Experimental results) |
| 5.1. Experimental results | EMPIRICAL / SOURCE-REPORTED EVALUATION | We see a performance gain by using additional synthetic data especially for the semantic scene completion task having an 10.3% improvement in IoU. | p. 8 (5.1. Experimental results) |
| 5.1. Experimental results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Therefore, they can achieve perfect alignments by finding the exact mesh model in a small database. | p. 6 (5.1. Experimental results) |
| 5.1. Experimental results | EMPIRICAL / SOURCE-REPORTED EVALUATION | This result validates the idea that it is beneficial to understand object semantics in order to achieve better scene completion. | p. 7 (5.1. Experimental results) |
| 5.1. Experimental results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Even when only evaluating on the visible surface, the model trained with the added supervision of the scene completion task outperforms the model trained ... | p. 7 (5.1. Experimental results) |

## Dataset / Benchmark Role

- **p. 6 / 5. Evaluation - extractive PDF cue:** The SUNCG test set consists of 500 depth images rendered from 184 scenes that are not in the training set.
- **p. 6 / 5. Evaluation - extractive PDF cue:** For the semantic scene completion task, we evaluate the IoU of each object classes on both the observed and occluded voxels.
- **p. 7 / 5.1. Experimental results - extractive PDF cue:** We examine to what extent the supervision of object semantics benefits the scene completion task.
- **p. 7 / 5.1. Experimental results - extractive PDF cue:** We evaluate on the rendered NYU benchmark with the same test images used by Firman at al.
- **p. 8 / 5.1. Experimental results - extractive PDF cue:** The following rows show the evaluation on semantic scene completion task.
- **p. 8 / 5.1. Experimental results - extractive PDF cue:** We see a performance gain by using additional synthetic data especially for the semantic scene completion task having an 10.3% improvement in IoU.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Semantic scene completion. (a) Input single-view depth map (b) Visible surface from the depth map; color is for visualiza- tion only. (c) Semantic ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. Given a single-view depth observation of a 3D scene the goal of our SSCNet is to predict both occupancy and object cate- gory ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3. SSCNet: Semantic scene completion network. Taking a single depth map as input, the network predicts occupancy and object labels for each voxel in ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 5. Different encodings for surface (a). The projective TSDF (b) is computed with respect to the camera and is therefore view-dependent. The accurate TSDF ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 4. Comparison of receptive fields and voxel sizes between SSCNet and prior work. (a) Object centric networks such as [34] and [20] scale objects ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 6. Synthesizing Training Data. We collected a large-scale synthetic 3D scene dataset to train our network. For each of the 3D scenes, we select ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Semantic scene completion results on the NYU test set with kinect depth map. the binvox [21] voxelizer which accounts for both surface and ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Scene completion on the rendered NYU test set as [3] labels compared to ground truth labels. For the semantic scene completion task, we ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The SUNCG test set consists of 500 depth images rendered from 184 scenes that are not in the training set. | embodiment, simulator version and control stack | p. 6 (5. Evaluation), p. 6 (5. Evaluation) |
| Task/environment | For the semantic scene completion task, we evaluate the IoU of each object classes on both the observed and occluded voxels. | reset, timeout, object/scene variation | p. 6 (5. Evaluation), p. 7 (5.1. Experimental results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (4.2. Synthetic depth map generation), p. 4 (3.2. Network architecture) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We see a performance gain by using additional synthetic data especially for the semantic scene completion task having an 10.3% improvement in IoU. | definition/direction/unit from same section | p. 8 (5.1. Experimental results) |
| For the semantic scene completion task, we evaluate the IoU of each object classes on both the observed and occluded voxels. | definition/direction/unit from same section | p. 6 (5. Evaluation) |
| As our evaluation metric, we use the voxel-level intersection over union (IoU) of predicted voxel method training prec. recall IoU Zheng et al. | definition/direction/unit from same section | p. 6 (5. Evaluation) |
| We observe that removing the view dependency by using the accurate TSDF gives a 2.4% improvement in IoU. | definition/direction/unit from same section | p. 8 (5.1. Experimental results) |
| Figure 15. Results and error visualization. The first three columns show the input depth map, corresponding color image and visible surface. The fourth and ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |
| We compare the performance of models trained with occupancy and multi-class labeling (see Table 2 [completion] vs. | definition/direction/unit from same section | p. 7 (5.1. Experimental results) |
| To answer this question, we trained a model with a loss only accounting for semantic labels evaluated on the visible surface and compared with ... | definition/direction/unit from same section | p. 7 (5.1. Experimental results) |
| Figure 1. Semantic scene completion. (a) Input single-view depth map (b) Visible surface from the depth map; color is for visualiza- tion only. (c) ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 4. Comparison of receptive fields and voxel sizes between SSCNet and prior work. (a) Object centric networks such as [34] and [20] scale ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |
| Scene completion on the rendered NYU test set as [3] labels compared to ground truth labels. | comparison identity and matched condition | p. 6 (5. Evaluation) |
| Moreover, since our method does not require the model fitting step it is much faster at 7s compared to 127s per image [4]. | comparison identity and matched condition | p. 6 (5.1. Experimental results) |
| Even when only evaluating on the visible surface, the model trained with the added supervision of the scene completion task outperforms the model trained ... | comparison identity and matched condition | p. 7 (5.1. Experimental results) |
| To answer this question, we trained a model with a loss only accounting for semantic labels evaluated on the visible surface and compared with ... | comparison identity and matched condition | p. 7 (5.1. Experimental results) |
| To investigate the effect of using synthetic training data, we compared models trained only with NYU and models pre-trained on SUNCG and then fine-tuned ... | comparison identity and matched condition | p. 8 (5.1. Experimental results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 8. What 3D context does the network learn? The first fig- ure shows the input depth map (a desk) and the following figures ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| To investigate the effect of using synthetic training data, we compared models trained only with NYU and models pre-trained on SUNCG and then fine-tuned ... | component/input/data sensitivity | p. 8 (5.1. Experimental results) |
| Previous work has shown scene completion is possible without 6 | component/input/data sensitivity | p. 6 (5.1. Experimental results) |
| In this section, we evaluate our proposed methods with a comparison to alternative approaches and an ablation study to better understand the proposed model. | component/input/data sensitivity | p. 6 (5. Evaluation) |
| [37] which both predict binary voxel occupancy based on a single depth map without semantic understanding of the scene. | component/input/data sensitivity | p. 7 (5.1. Experimental results) |
| Figure 1. Semantic scene completion. (a) Input single-view depth map (b) Visible surface from the depth map; color is for visualiza- tion only. (c) ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To provide the training data for our network, we introduce SUNCG, a manually created large-scale dataset of synthetic 3D scenes with dense occupancy and ... | Increasing the receptive field gives the network a opportunity to capture richer contextual information and significantly improve the network performance from 38.0% to 44.3%. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5.1. Experimental results), p. 8 (5.1. Experimental results), p. 6 (5.1. Experimental results), p. 7 (5.1. Experimental results), p. 7 (5.1. Experimental results), p. 12 (Figure/Table caption) |
| Primary metric/result | We see a performance gain by using additional synthetic data especially for the semantic scene completion task having an 10.3% improvement in IoU. | numeric claim only at cited anchor | p. 8 (5.1. Experimental results) |

- Numeric sentences retained from the body:
- **p. 6 / 5. Evaluation - extractive PDF cue:** The annotations consist of 33 object meshes in 7 categories, other categories approximated using 3D boxes or planes.
- **p. 6 / 5. Evaluation - extractive PDF cue:** The SUNCG test set consists of 500 depth images rendered from 184 scenes that are not in the training set.
- **p. 6 / 5.1. Experimental results - extractive PDF cue:** Moreover, since our method does not require the model fitting step it is much faster at 7s compared to 127s per image [4].
- **p. 5 / 3.2. Network architecture - extractive PDF cue:** Pre-training SSCNet on the SUNCG training set takes around a week on a Tesla K40 GPU, and fine-tuning on the NYU dataset takes 30 hours.
- **p. 5 / 4. Synthesizing training data - extractive PDF cue:** In the end, we have 49, 884 valid floors, with contain 404, 058 rooms and 5, 697, 217 object instances from 2644 unique object meshes ...
- **p. 5 / 4.3. Volumetric ground truth generation - extractive PDF cue:** Specifically, we first voxelize each object to a 128×128×128 voxel grid.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | While Firman et al. produces good results for many cases, their approach fails when the scene becomes complex. | p. 7 (5.1. Experimental results) |
| body limitation/failure cue | For instance, their algorithm fails to complete half of the bed in the first row of Figure 7, and also fails to complete the ... | p. 7 (5.1. Experimental results) |
| body limitation/failure cue | In contrast, our algorithm is based on only depth and does not use additional mesh model at test time. | p. 6 (5.1. Experimental results) |
| body limitation/failure cue | Moreover, since our method does not require the model fitting step it is much faster at 7s compared to 127s per image [4]. | p. 6 (5.1. Experimental results) |
| body limitation/failure cue | Figure 5. Different encodings for surface (a). The projective TSDF (b) is computed with respect to the camera and is therefore view-dependent. The accurate ... | p. 3 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use the re-implementation of Zheng et al.'s approach from Firman et al., which only provides the completion result. | p. 7 (5.1. Experimental results) |
| Secondly, due to the GPU memory constraints, our network output resolution is lower than that of input volume. | p. 8 (5.1. Experimental results) |
| We encode the 3D scene into a flipped TSDF with grid size 0.02 m, truncation value 0.24 m, resulting in a 240 × 144 ... | p. 4 (3.2. Network architecture) |
| During training, each mini-batch contains one 3D view volume, requiring 11 GB of GPU memory. | p. 5 (3.2. Network architecture) |
| Pre-training SSCNet on the SUNCG training set takes around a week on a Tesla K40 GPU, and fine-tuning on the NYU dataset takes 30 ... | p. 5 (3.2. Network architecture) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5.1. Experimental results - extractive PDF cue:** While Firman et al. produces good results for many cases, their approach fails when the scene becomes complex.
- **p. 7 / 5.1. Experimental results - extractive PDF cue:** For instance, their algorithm fails to complete half of the bed in the first row of Figure 7, and also fails to complete the chairs ...
- **p. 6 / 5.1. Experimental results - extractive PDF cue:** In contrast, our algorithm is based on only depth and does not use additional mesh model at test time.
- **p. 6 / 5.1. Experimental results - extractive PDF cue:** Moreover, since our method does not require the model fitting step it is much faster at 7s compared to 127s per image [4].
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 5. Different encodings for surface (a). The projective TSDF (b) is computed with respect to the camera and is therefore view-dependent. The accurate TSDF ...

- **PDF anchors reviewed:** datasets p. 6 (5. Evaluation), p. 6 (5. Evaluation), p. 7 (5.1. Experimental results), p. 7 (5.1. Experimental results), p. 8 (5.1. Experimental results), p. 8 (5.1. Experimental results), metrics p. 8 (5.1. Experimental results), p. 6 (5. Evaluation), p. 6 (5. Evaluation), p. 8 (5.1. Experimental results), p. 13 (Figure/Table caption), p. 7 (5.1. Experimental results), baselines p. 4 (Figure/Table caption), p. 6 (5. Evaluation), p. 6 (5.1. Experimental results), p. 7 (5.1. Experimental results), p. 7 (5.1. Experimental results), p. 8 (5.1. Experimental results), results p. 8 (5.1. Experimental results), p. 8 (5.1. Experimental results), p. 6 (5.1. Experimental results), p. 7 (5.1. Experimental results), p. 7 (5.1. Experimental results), p. 12 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
