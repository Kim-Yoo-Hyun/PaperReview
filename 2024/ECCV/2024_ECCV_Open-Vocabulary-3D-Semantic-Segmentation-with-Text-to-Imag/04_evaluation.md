# Evaluation - Open-Vocabulary 3D Semantic Segmentation with Text-to-Image Diffusion Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4252_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04252.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 12 (Figure/Table caption), p. 9 (4 Experiment), p. 9 (4 Experiment), p. 14 (Figure/Table caption), p. 10 (Figure/Table caption), p. 13 (Figure/Table caption)): Table 3: Performance of different model ablations. We observe that each com- ponent of our model gains consistent improvements.

## Evaluation Body Digest

- **p. 9 / 4 Experiment - extractive body cue:** It splits 61 scenes for training, 11 scenes for validation and 18 for testing.
- **p. 9 / 4 Experiment - extractive body cue:** Matterport3D is a large scale RGB-D dataset containing 10,800 panoramic views from 194,000 RGB-D images of 90 building-scale scenes.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Illustration of open-vocabulary 3D perception methods. LP D and LMD denote point-based distillation loss and mask-based distillation loss. M3D denote a set of ...
- **p. 9 / 4 Experiment - extractive body cue:** We conduct a series of experiments to demonstrate the effectiveness of Diff2Scene on a variety of zero-shot 3D scene understanding benchmarks.
- **p. 9 / 4 Experiment - extractive body cue:** This enables us to evaluate the performance of our method on the long-tail distribution, making ScanNet200 a natural choice as an evaluation dataset.
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 5: Qualitative results from our model and OpenScene on zero-shot vi- sual grounding. Our open-vocabulary semantic understanding model is capable of handling different types ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: Overview of our method. We propose Diff2Scene, an open-vocabulary 3D semantic understanding model. Diff2Scene contains two branches. The 2D branch is de- signed ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 3: Performance of different model ablations. We observe that each com- ponent of our model gains consistent improvements.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiment (p. 9).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 3: Performance of different model ablations. We observe that each com- ponent of our model gains consistent improvements. | p. 12 (Figure/Table caption) |
| 4 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | We train our 3D branch using the images in the training splits and report the results on test split. | p. 9 (4 Experiment) |
| 4 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | This enables us to evaluate the performance of our method on the long-tail distribution, making ScanNet200 a natural choice as an evaluation dataset. | p. 9 (4 Experiment) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 5: Qualitative results from our model and OpenScene on zero-shot vi- sual grounding. Our open-vocabulary semantic understanding model is capable of handling different ... | p. 14 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 1: Comparison to state-of-the-art models. We report mIoU for all benchmarks. Best results in zero-shot, open-vocabulary setting are shown in bold. ScanNet Matterport3D ... | p. 10 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 9 / 4 Experiment - extractive body cue:** It splits 61 scenes for training, 11 scenes for validation and 18 for testing.
- **p. 9 / 4 Experiment - extractive body cue:** Matterport3D is a large scale RGB-D dataset containing 10,800 panoramic views from 194,000 RGB-D images of 90 building-scale scenes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Illustration of open-vocabulary 3D semantic scene understanding. We propose Diff2Scene, a 3D model that performs open-vocabulary semantic segmentation and visual grounding tasks given ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Illustration of open-vocabulary 3D perception methods. LP D and LMD denote point-based distillation loss and mask-based distillation loss. M3D denote a set of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: Overview of our method. We propose Diff2Scene, an open-vocabulary 3D semantic understanding model. Diff2Scene contains two branches. The 2D branch is de- signed ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 1: Comparison to state-of-the-art models. We report mIoU for all benchmarks. Best results in zero-shot, open-vocabulary setting are shown in bold. ScanNet Matterport3D ScanNet200 ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 2: Effectiveness of Different Distillation Settings. We report mIoU of different methods on the Replica [77] dataset. Setting Distillation Type Head Tail All fine-tuned ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 3: Performance of different model ablations. We observe that each com- ponent of our model gains consistent improvements.
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 4: Qualitative results from our model and OpenScene on zero-shot se- mantic segmentation. We visualize the segmentation results on the validation set of ScanNet200 ...
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 5: Qualitative results from our model and OpenScene on zero-shot vi- sual grounding. Our open-vocabulary semantic understanding model is capable of handling different types ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | It splits 61 scenes for training, 11 scenes for validation and 18 for testing. | embodiment, simulator version and control stack | p. 9 (4 Experiment), p. 9 (4 Experiment) |
| Task/environment | Matterport3D is a large scale RGB-D dataset containing 10,800 panoramic views from 194,000 RGB-D images of 90 building-scale scenes. | reset, timeout, object/scene variation | p. 9 (4 Experiment) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (X. Zhu et al), p. 8 (X. Zhu et al) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (1 Introduction), p. 5 (X. Zhu et al) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 2: Illustration of open-vocabulary 3D perception methods. LP D and LMD denote point-based distillation loss and mask-based distillation loss. M3D denote a set ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| We conduct a series of experiments to demonstrate the effectiveness of Diff2Scene on a variety of zero-shot 3D scene understanding benchmarks. | definition/direction/unit from same section | p. 9 (4 Experiment) |
| This enables us to evaluate the performance of our method on the long-tail distribution, making ScanNet200 a natural choice as an evaluation dataset. | definition/direction/unit from same section | p. 9 (4 Experiment) |
| Fig. 5: Qualitative results from our model and OpenScene on zero-shot vi- sual grounding. Our open-vocabulary semantic understanding model is capable of handling different ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| Fig. 3: Overview of our method. We propose Diff2Scene, an open-vocabulary 3D semantic understanding model. Diff2Scene contains two branches. The 2D branch is de- ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 3: Performance of different model ablations. We observe that each com- ponent of our model gains consistent improvements. | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Fig. 4: Qualitative results from our model and OpenScene on zero-shot se- mantic segmentation. We visualize the segmentation results on the validation set of ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 1: Comparison to state-of-the-art models. We report mIoU for all benchmarks. Best results in zero-shot, open-vocabulary setting are shown in bold. ScanNet Matterport3D ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| Fig. 4: Qualitative results from our model and OpenScene on zero-shot se- mantic segmentation. We visualize the segmentation results on the validation set of ... | comparison identity and matched condition | p. 13 (Figure/Table caption) |
| We then perform comprehensive ablation studies to validate our designs. | comparison identity and matched condition | p. 9 (4 Experiment) |
| Except for Replica, point clouds and multi-view images in the training split without ground truth annotations are used for model training. | comparison identity and matched condition | p. 9 (4 Experiment) |
| Fig. 1: Illustration of open-vocabulary 3D semantic scene understanding. We propose Diff2Scene, a 3D model that performs open-vocabulary semantic segmentation and visual grounding tasks ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Table 3: Performance of different model ablations. We observe that each com- ponent of our model gains consistent improvements. | comparison identity and matched condition | p. 12 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We then perform comprehensive ablation studies to validate our designs. | component/input/data sensitivity | p. 9 (4 Experiment) |
| Except for Replica, point clouds and multi-view images in the training split without ground truth annotations are used for model training. | component/input/data sensitivity | p. 9 (4 Experiment) |
| Fig. 1: Illustration of open-vocabulary 3D semantic scene understanding. We propose Diff2Scene, a 3D model that performs open-vocabulary semantic segmentation and visual grounding tasks ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Table 3: Performance of different model ablations. We observe that each com- ponent of our model gains consistent improvements. | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| Table 2: Effectiveness of Different Distillation Settings. We report mIoU of different methods on the Replica [77] dataset. Setting Distillation Type Head Tail All ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| Fig. 4: Qualitative results from our model and OpenScene on zero-shot se- mantic segmentation. We visualize the segmentation results on the validation set of ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, we make the following contributions: - To the best of our knowledge, we are the first to leverage text-image diffusion to perform ... | Table 3: Performance of different model ablations. We observe that each com- ponent of our model gains consistent improvements. | PDF body cue; verify exact table/figure and matched conditions | p. 12 (Figure/Table caption), p. 9 (4 Experiment), p. 9 (4 Experiment), p. 14 (Figure/Table caption), p. 10 (Figure/Table caption), p. 13 (Figure/Table caption) |
| Primary metric/result | We train our 3D branch using the images in the training splits and report the results on test split. | numeric claim only at cited anchor | p. 9 (4 Experiment) |

- Numeric sentences retained from the body:
- **p. 9 / 4 Experiment - extractive body cue:** It splits 61 scenes for training, 11 scenes for validation and 18 for testing.
- **p. 9 / 4 Experiment - extractive body cue:** We report the mean intersection over union (mIoU) metric on the validation set consisting of 312 scenes following the split in [62,69,78].

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | There are several limitations of the proposed model. | p. 13 (5 Conclusion) |
| body limitation/failure cue | As Replica does not provide the training data, we perform training on ScanNet and perform evaluation on Replica, following the setting in [79]. | p. 9 (4 Experiment) |
| body limitation/failure cue | Fig. 5: Qualitative results from our model and OpenScene on zero-shot vi- sual grounding. Our open-vocabulary semantic understanding model is capable of handling different ... | p. 14 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Recent progress in computer vision have witnessed the emerging interests in solving semantic understanding tasks in open-vocabulary settings [35,62,67,78, 94]. | p. 2 (1 Introduction) |
| 3D semantic scene understanding, with the task of assigning semantics to every 3D point, plays a fundamental role in many computer vision applications, such ... | p. 2 (1 Introduction) |
| The frozen features extracted from the decoder of the U-Net in the diffusion model are trained with generative objectives, and cannot be directly used ... | p. 3 (1 Introduction) |
| To predict the per-point semantic class, the model first computes the per-mask category logits for both salient and geometric masks. | p. 6 (X. Zhu et al) |
| We first compute the pixel-point correspondence following [62]. | p. 8 (X. Zhu et al) |
| The 3D point cloud is quantized into voxels by averaging the pixels within each voxel to save memory and reduce computes. | p. 8 (X. Zhu et al) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 13 / 5 Conclusion - extractive body cue:** There are several limitations of the proposed model.
- **p. 9 / 4 Experiment - extractive body cue:** As Replica does not provide the training data, we perform training on ScanNet and perform evaluation on Replica, following the setting in [79].
- **p. 14 / Figure/Table caption - extractive body cue:** Fig. 5: Qualitative results from our model and OpenScene on zero-shot vi- sual grounding. Our open-vocabulary semantic understanding model is capable of handling different types ...

- **Evidence anchors reviewed:** datasets p. 9 (4 Experiment), p. 9 (4 Experiment), metrics p. 4 (Figure/Table caption), p. 9 (4 Experiment), p. 9 (4 Experiment), p. 14 (Figure/Table caption), p. 6 (Figure/Table caption), p. 12 (Figure/Table caption), baselines p. 10 (Figure/Table caption), p. 13 (Figure/Table caption), p. 9 (4 Experiment), p. 9 (4 Experiment), p. 1 (Figure/Table caption), p. 12 (Figure/Table caption), results p. 12 (Figure/Table caption), p. 9 (4 Experiment), p. 9 (4 Experiment), p. 14 (Figure/Table caption), p. 10 (Figure/Table caption), p. 13 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
