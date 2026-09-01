# Evaluation - UniGS: Unified Language-Image-3D Pretraining with Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=6U2KI1dpfl; PDF retrieval source: https://openreview.net/pdf/a89f593acd0d100b23f75744f408665a3c531fbc.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (Figure/Table caption), p. 7 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 8 (Figure/Table caption)): Table 5: Zero-shot classification with point clouds on ABO. Avg. denotes mean average classifica- tion accuracy. Results illustrate that properly converting point clouds into 3DGS format can improve performance. As ...

## Evaluation Body Digest

- **p. 15 / B.2 DETAILS OF TRAINING AND EVALUATION - extractive PDF cue:** As for the scene recognition task on the SUN RGBD dataset, UniGS follows the basic evaluation pattern to directly train 50 epochs on the training ...
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** Due to the lack of real-world data in the pre-training dataset, the Top1 accuracy of MVImgNet is relatively low.
- **p. 14 / B.1 DETAILS OF ENSEMBLE DATASETS - extractive PDF cue:** All datasets can be successfully prepared on 6×RTX4090 GPU within 2 days, where 15 scenes can be optimized simultaneously on each GPU.
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** We leverage the SUN RGBD dataset (Song et al., 2015) as the scene data and classify objects into 37 categories following the setting of (Song ...
- **p. 15 / B.2 DETAILS OF TRAINING AND EVALUATION - extractive PDF cue:** UniGS will be further fine-tuned for 50 epochs on the training set to alleviate the impact of the text domain across different datasets.
- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** For the retrieval task, we randomly sample 1000 items to form the test set, and use the rest as training set.
- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** Following Section 3.5, we collect 146000, 7929, 3483, and 61871 objects, optimized for Objaverse (including Objaverse-LVIS for evaluation only ), ABO, MVImgNet, and SUN RGBD ...
- **p. 14 / B IMPLEMENTATION DETAILS - extractive PDF cue:** (2015) datasets; as well as the training and evaluation details on the Text-driven retrieval, Zero-shot classification, and scene recognition tasks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EXPERIMENT (p. 6); B IMPLEMENTATION DETAILS (p. 14); B.1 DETAILS OF ENSEMBLE DATASETS (p. 14); B.2 DETAILS OF TRAINING AND EVALUATION (p. 14).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 5: Zero-shot classification with point clouds on ABO. Avg. denotes mean average classifica- tion accuracy. Results illustrate that properly converting point clouds into ... | p. 9 (Figure/Table caption) |
| 4 EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 1, UniGS outperforms the current state-of-the-art approaches across all datasets and improves the Top 1 retrieval accuracy of CLIP2 and ... | p. 7 (4 EXPERIMENT) |
| 4 EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | On the contrary, training directly from scratch can better learn the feature information of 3DGS, revealing that incorrect model design can hinder subsequent learning ... | p. 10 (4 EXPERIMENT) |
| 4 EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | The performance under different data and model scales demonstrates that scaling up the training data and model size of UniGS can significantly improve the ... | p. 10 (4 EXPERIMENT) |
| 4 EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | (2023) and UniGS significantly outperform SOTA methods, emphasizing the effectiveness of 3DGS representation and proposed Gaussian-aware Guidance. | p. 9 (4 EXPERIMENT) |

## Dataset / Benchmark Role

- **p. 15 / B.2 DETAILS OF TRAINING AND EVALUATION - extractive PDF cue:** As for the scene recognition task on the SUN RGBD dataset, UniGS follows the basic evaluation pattern to directly train 50 epochs on the training ...
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** Due to the lack of real-world data in the pre-training dataset, the Top1 accuracy of MVImgNet is relatively low.
- **p. 14 / B.1 DETAILS OF ENSEMBLE DATASETS - extractive PDF cue:** All datasets can be successfully prepared on 6×RTX4090 GPU within 2 days, where 15 scenes can be optimized simultaneously on each GPU.
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** We leverage the SUN RGBD dataset (Song et al., 2015) as the scene data and classify objects into 37 categories following the setting of (Song ...
- **p. 15 / B.2 DETAILS OF TRAINING AND EVALUATION - extractive PDF cue:** UniGS will be further fine-tuned for 50 epochs on the training set to alleviate the impact of the text domain across different datasets.
- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** For the retrieval task, we randomly sample 1000 items to form the test set, and use the rest as training set.
- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** Following Section 3.5, we collect 146000, 7929, 3483, and 61871 objects, optimized for Objaverse (including Objaverse-LVIS for evaluation only ), ABO, MVImgNet, and SUN RGBD ...
- **p. 14 / B IMPLEMENTATION DETAILS - extractive PDF cue:** (2015) datasets; as well as the training and evaluation details on the Text-driven retrieval, Zero-shot classification, and scene recognition tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Left: information gap in different 3D representations. Middle: our UniGS, a novel unified text-image-3D pre-training framework, leverages 3DGS as the 3D representation. Right: ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: The overview of UniGS. UniGS is an innovative, unified, and scalable 3D pretraining framework designed for 3D representation learning. It offers versatile pipelines ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Model overview of UniGS. Let µ, c, α, s, R denote the location, color, opacity, scale, and rotation attribute of 3DGS. (a) Given ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Top1, Top5 and Top10 Text-3D retrieval accuracy. Avg.: the mean average retrieval accuracy. * denotes training from scratch. Implementation Details. Following Section 3.5, ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Zero-shot classification. Avg.: the mean average classification accuracy. * denotes training from scratch.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Recognition on SUN RGBD (dataset with point clouds). Avg.: the mean average Top1 accuracy across all categories. * denotes training from scratch. 13.6% ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 4: Summary of the experimental results on Objaverse-LVIS zero-shot classification. Avg.: the mean average classification accuracy. All methods are trained from scratch. Training Initialization ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 5: Zero-shot classification with point clouds on ABO. Avg. denotes mean average classifica- tion accuracy. Results illustrate that properly converting point clouds into 3DGS ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | As for the scene recognition task on the SUN RGBD dataset, UniGS follows the basic evaluation pattern to directly train 50 epochs on the ... | embodiment, simulator version and control stack | p. 15 (B.2 DETAILS OF TRAINING AND EVALUATION), p. 9 (4 EXPERIMENT) |
| Task/environment | Due to the lack of real-world data in the pre-training dataset, the Top1 accuracy of MVImgNet is relatively low. | reset, timeout, object/scene variation | p. 9 (4 EXPERIMENT), p. 14 (B.1 DETAILS OF ENSEMBLE DATASETS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 4 (3 METHODOLOGY) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 5: Zero-shot classification with point clouds on ABO. Avg. denotes mean average classifica- tion accuracy. Results illustrate that properly converting point clouds into ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| We report Top1, Top5, and Top10 accuracy. | definition/direction/unit from same section | p. 7 (4 EXPERIMENT) |
| Avg.: the mean average retrieval accuracy. * denotes training from scratch. | definition/direction/unit from same section | p. 7 (4 EXPERIMENT) |
| Avg.: the mean average Top1 accuracy across all categories. | definition/direction/unit from same section | p. 10 (4 EXPERIMENT) |
| Avg.: the mean average Top1 zero-shot classification accuracy on ABO. • Comparisons between Exp1., Exp2., and Exp3. show that the convolution-based model, i.e. | definition/direction/unit from same section | p. 10 (4 EXPERIMENT) |
| The accuracy of Text-driven retrieval on Objaverse under three optimization pipelines. | definition/direction/unit from same section | p. 15 (B.2 DETAILS OF TRAINING AND EVALUATION) |
| The accuracy of Zero-shot classification on ABO under three optimization pipelines. items, respectively. | definition/direction/unit from same section | p. 15 (B.2 DETAILS OF TRAINING AND EVALUATION) |
| Table 11: Zero-shot classification on Objaverse with other 3DGS-driven methods. Avg. denotes mean average classification accuracy. Results illustrate the ability of UniGS to migrate ... | definition/direction/unit from same section | p. 17 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown in Table 1, UniGS outperforms the current state-of-the-art approaches across all datasets and improves the Top 1 retrieval accuracy of CLIP2 and ... | comparison identity and matched condition | p. 7 (4 EXPERIMENT) |
| However, UniGS outperforms all the baselines on all datasets, revealing the power of 3DGS representations and the effectiveness of UniGS. | comparison identity and matched condition | p. 9 (4 EXPERIMENT) |
| 4.2 COMPARISONS TO STATE-OF-THE-ART To demonstrate the effectiveness of our proposed method, we evaluate UniGS on the Text-3D retrieval, zero-shot classification, and scene understanding ... | comparison identity and matched condition | p. 7 (4 EXPERIMENT) |
| (2023) and UniGS significantly outperform SOTA methods, emphasizing the effectiveness of 3DGS representation and proposed Gaussian-aware Guidance. | comparison identity and matched condition | p. 9 (4 EXPERIMENT) |
| As for the baseline model, we further report the performance of the original Uni3D model trained with point clouds and the altered version trained ... | comparison identity and matched condition | p. 6 (4 EXPERIMENT) |
| Table 9: Comparisons to state-of-the-art methods with the same data on Objaverse-LVIS zero- shot classification. Avg.: the mean average classification accuracy. Methods Source Backbone ... | comparison identity and matched condition | p. 16 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We summarize all the experiments and conduct an ablation study on whether to leverage the 3DGS feature, ViT pattern, Pretrained weight (Pre.), Parallel structure ... | component/input/data sensitivity | p. 9 (4 EXPERIMENT) |
| Uni3D, can successfully model feature relationships. • Comparisons between Exp3., Exp4., and Exp7. show that loading pretrained weights has certain advantages, but without careful ... | component/input/data sensitivity | p. 10 (4 EXPERIMENT) |
| We further conduct detailed and comprehensive ablation studies to reveal the impact and power of our design for cross-modal learning. | component/input/data sensitivity | p. 6 (4 EXPERIMENT) |
| We evaluate the zero-shot classification performance of UniGS on Objaverse-Lvis, ABO, and MVImgNet without accessing their training sets. | component/input/data sensitivity | p. 8 (4 EXPERIMENT) |
| Ablation study on the proposed modules of UniGS. | component/input/data sensitivity | p. 9 (4 EXPERIMENT) |
| Published as a conference paper at ICLR 2025 Figure 4: Additional ablation study of the quality of 3DGS on the Text-driven retrieval task. | component/input/data sensitivity | p. 15 (B.2 DETAILS OF TRAINING AND EVALUATION) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions can be summarized as follows: • We propose UniGS, a novel unified text-image-3D pre-training framework, which leverages 3DGS as the 3D representation ... | Table 5: Zero-shot classification with point clouds on ABO. Avg. denotes mean average classifica- tion accuracy. Results illustrate that properly converting point clouds into ... | PDF body cue; verify exact table/figure and matched conditions | p. 9 (Figure/Table caption), p. 7 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 8 (Figure/Table caption) |
| Primary metric/result | As shown in Table 1, UniGS outperforms the current state-of-the-art approaches across all datasets and improves the Top 1 retrieval accuracy of CLIP2 and ... | numeric claim only at cited anchor | p. 7 (4 EXPERIMENT) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** Following Section 3.5, we collect 146000, 7929, 3483, and 61871 objects, optimized for Objaverse (including Objaverse-LVIS for evaluation only ), ABO, MVImgNet, and SUN RGBD ...
- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** We train UniGS with a learning rate of 1e-4 for 15 epochs for the retrieval task and 50 epochs for the zero-shot classification and scene ...
- **p. 14 / B.1 DETAILS OF ENSEMBLE DATASETS - extractive PDF cue:** All datasets can be successfully prepared on 6×RTX4090 GPU within 2 days, where 15 scenes can be optimized simultaneously on each GPU.
- **p. 14 / B.2 DETAILS OF TRAINING AND EVALUATION - extractive PDF cue:** In terms of time consumption, the whole training process on Objaverse costs 12.5 hours with 6×RTX4090 GPU, where UniGS is trained for 15 epochs on ...
- **p. 14 / B.2 DETAILS OF TRAINING AND EVALUATION - extractive PDF cue:** After training 15 epochs on Objaverse, UniGS is directly evaluated on the entire Objaverse-Lvis, ABO, and MVimgnet datasets.
- **p. 15 / B.2 DETAILS OF TRAINING AND EVALUATION - extractive PDF cue:** UniGS will be further fine-tuned for 50 epochs on the training set to alleviate the impact of the text domain across different datasets.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations: Despite the robust and effective performance of UniGS for 3D representation learning and downstream applications, its current version lacks performance validation of out-door ... | p. 10 (5 CONCLUSION) |
| body limitation/failure cue | Moreover, at least one image with a camera pose is required for the optimization of 3DGS, and how to further consider a camera-pose-free approach ... | p. 10 (5 CONCLUSION) |
| body limitation/failure cue | Note that the saving interval should not be a multiplier of the opacity reset interval, otherwise the retained results may become unstable. | p. 14 (B.1 DETAILS OF ENSEMBLE DATASETS) |
| body limitation/failure cue | Note that 3DGS does not necessarily exist on the surface of objects, so there is a certain difference between point clouds and the 3D ... | p. 6 (4 EXPERIMENT) |
| body limitation/failure cue | Moreover, the success of UniGS in SUN RGBD shows the robustness of 3DGS representation to the number of multi-view images. | p. 9 (4 EXPERIMENT) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train UniGS with a learning rate of 1e-4 for 15 epochs for the retrieval task and 50 epochs for the zero-shot classification and ... | p. 7 (4 EXPERIMENT) |
| In terms of time consumption, the whole training process on Objaverse costs 12.5 hours with 6×RTX4090 GPU, where UniGS is trained for 15 epochs ... | p. 14 (B.2 DETAILS OF TRAINING AND EVALUATION) |
| Next, 3DGS encoded by UniGS is used to compute similarity and calculate Topk accuracy across texts of all the items in the testing set. | p. 15 (B.2 DETAILS OF TRAINING AND EVALUATION) |
| We leverage the activation function tanh(·) to convert the features of 3DGS to the range [-1,1] and set the batch size of training and ... | p. 14 (B.2 DETAILS OF TRAINING AND EVALUATION) |
| This highlights UniGS's potential to inherit capabilities of the point cloud encoder and that it can directly be applied to 3D point clouds. | p. 9 (4 EXPERIMENT) |
| UniGS will be further fine-tuned for 50 epochs on the training set to alleviate the impact of the text domain across different datasets. | p. 15 (B.2 DETAILS OF TRAINING AND EVALUATION) |
| Let N denotes the batch size and τ the temperature coefficient, the Language-3DGS Alignment training objective L(T, G) can be described as: L(T, G) ... | p. 4 (3 METHODOLOGY) |
| Given a text-image-3DGS triplet, {XT , XI, XG}, text features, f T ∈RCT , image features, f I ∈RCI, and 3DGS features, f G ... | p. 4 (3 METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 5 CONCLUSION - extractive PDF cue:** Limitations: Despite the robust and effective performance of UniGS for 3D representation learning and downstream applications, its current version lacks performance validation of out-door scenarios ...
- **p. 10 / 5 CONCLUSION - extractive PDF cue:** Moreover, at least one image with a camera pose is required for the optimization of 3DGS, and how to further consider a camera-pose-free approach (e.g., ...
- **p. 14 / B.1 DETAILS OF ENSEMBLE DATASETS - extractive PDF cue:** Note that the saving interval should not be a multiplier of the opacity reset interval, otherwise the retained results may become unstable.
- **p. 6 / 4 EXPERIMENT - extractive PDF cue:** Note that 3DGS does not necessarily exist on the surface of objects, so there is a certain difference between point clouds and the 3D location ...
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** Moreover, the success of UniGS in SUN RGBD shows the robustness of 3DGS representation to the number of multi-view images.

- **PDF anchors reviewed:** datasets p. 15 (B.2 DETAILS OF TRAINING AND EVALUATION), p. 9 (4 EXPERIMENT), p. 14 (B.1 DETAILS OF ENSEMBLE DATASETS), p. 9 (4 EXPERIMENT), p. 15 (B.2 DETAILS OF TRAINING AND EVALUATION), p. 7 (4 EXPERIMENT), metrics p. 9 (Figure/Table caption), p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 15 (B.2 DETAILS OF TRAINING AND EVALUATION), baselines p. 7 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 7 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 6 (4 EXPERIMENT), p. 16 (Figure/Table caption), results p. 9 (Figure/Table caption), p. 7 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 10 (4 EXPERIMENT), p. 9 (4 EXPERIMENT), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
