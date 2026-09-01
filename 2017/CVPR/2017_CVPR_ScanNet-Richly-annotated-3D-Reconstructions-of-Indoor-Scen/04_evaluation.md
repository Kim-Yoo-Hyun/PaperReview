# Evaluation - ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1702.04405; PDF retrieval source: https://arxiv.org/pdf/1702.04405. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.1. 3D Object Classification), p. 20 (Figure/Table caption), p. 2 (Dataset), p. 3 (3.1. RGB-D Scanning), p. 7 (5.1. 3D Object Classification), p. 8 (5.2. Semantic Voxel Labeling)): On the other hand, training on ScanNet translates well to testing on SceneNN; as a result, the test results on SceneNN are significantly improved by using the training data from ...

## Evaluation Body Digest

- **p. 3 / 3. Dataset Acquisition Framework - extractive PDF cue:** Our main goal driving the design of our framework was to allow untrained users to capture semantically labeled surfaces of indoor scenes with commodity hardware.
- **p. 5 / 4. ScanNet Dataset - extractive PDF cue:** 5 plots the distribution of scanned scenes over different types of real-world spaces.
- **p. 6 / 5. Tasks and Benchmarks - extractive PDF cue:** We use these tasks to demonstrate that ScanNet enables the use of deep learning methods for 3D scene understanding tasks with supervised training, and compare ...
- **p. 6 / 5.1. 3D Object Classification - extractive PDF cue:** With the availability of large-scale synthetic 3D datasets such as [91, 6] and recent advances in 3D deep learnScans Instances #Train #Test #Train #Test Object ...
- **p. 7 / 5.1. 3D Object Classification - extractive PDF cue:** Second, although the relatively small SceneNN dataset is able to learn within its own dataset to a reasonable degree, it does not generalize to the ...
- **p. 2 / Dataset - extractive PDF cue:** Overview of RGB-D datasets for 3D reconstruction and semantic scene understanding.
- **p. 2 / Dataset - extractive PDF cue:** Overall, the contributions of this paper are: • A large 3D dataset containing 1513 RGB-D scans of over 707 unique indoor environments with estimated camera ...
- **p. 7 / 5.1. 3D Object Classification - extractive PDF cue:** Synthetic Test Sets Real Test Sets Training Set ShapeNet ShapeNet Partial SceneNN ScanNet ShapeNet 92.5 37.6 68.2 39.5 ShapeNet Partial 88.5 92.1 72.7 45.7 SceneNN ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** Dataset (p. 2); 3. Dataset Acquisition Framework (p. 3); 4. ScanNet Dataset (p. 5); 5. Tasks and Benchmarks (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.1. 3D Object Classification | BENCHMARK / DATASET | On the other hand, training on ScanNet translates well to testing on SceneNN; as a result, the test results on SceneNN are significantly improved ... | p. 7 (5.1. 3D Object Classification) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 15. Comparison of calibration results. In the top row, we show results of calibration on a flat wall. As the distance increases the ... | p. 20 (Figure/Table caption) |
| Dataset | BENCHMARK / DATASET | We also provide CAD model placements for a subset of the scans. • A design for efficient 3D data capture and annotation suitable for ... | p. 2 (Dataset) |
| 3.1. RGB-D Scanning | BENCHMARK / DATASET | We find that this calibration procedure is easy for users and results in improved data and consequently enhanced reconstruction quality. | p. 3 (3.1. RGB-D Scanning) |
| 5.1. 3D Object Classification | BENCHMARK / DATASET | Interestingly enough, these results can be slightly improved when mixing training data of ScanNet with partial scans of ShapeNet (last row). | p. 7 (5.1. 3D Object Classification) |

## Dataset / Benchmark Role

- **p. 3 / 3. Dataset Acquisition Framework - extractive PDF cue:** Our main goal driving the design of our framework was to allow untrained users to capture semantically labeled surfaces of indoor scenes with commodity hardware.
- **p. 5 / 4. ScanNet Dataset - extractive PDF cue:** 5 plots the distribution of scanned scenes over different types of real-world spaces.
- **p. 6 / 5. Tasks and Benchmarks - extractive PDF cue:** We use these tasks to demonstrate that ScanNet enables the use of deep learning methods for 3D scene understanding tasks with supervised training, and compare ...
- **p. 6 / 5.1. 3D Object Classification - extractive PDF cue:** With the availability of large-scale synthetic 3D datasets such as [91, 6] and recent advances in 3D deep learnScans Instances #Train #Test #Train #Test Object ...
- **p. 7 / 5.1. 3D Object Classification - extractive PDF cue:** Second, although the relatively small SceneNN dataset is able to learn within its own dataset to a reasonable degree, it does not generalize to the ...
- **p. 2 / Dataset - extractive PDF cue:** Overview of RGB-D datasets for 3D reconstruction and semantic scene understanding.
- **p. 2 / Dataset - extractive PDF cue:** Overall, the contributions of this paper are: • A large 3D dataset containing 1513 RGB-D scans of over 707 unique indoor environments with estimated camera ...
- **p. 7 / 5.1. 3D Object Classification - extractive PDF cue:** Synthetic Test Sets Real Test Sets Training Set ShapeNet ShapeNet Partial SceneNN ScanNet ShapeNet 92.5 37.6 68.2 39.5 ShapeNet Partial 88.5 92.1 72.7 45.7 SceneNN ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Example reconstructed spaces in ScanNet annotated with instance-level object category labels through our crowdsourced annotation framework. ciently providing (dense) annotations in 3D is ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Table 1. Overview of RGB-D datasets for 3D reconstruction and semantic scene understanding. Note that in addition to the 1513 scans in ScanNet, we also ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of our RGB-D reconstruction and semantic annotation framework. Left: a novice user uses a handheld RGB-D device with our scanning interface to ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Our web-based crowdsourcing interface for annotating a scene with instance-level object category labels. The right panel lists object instances already annotated in the ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Crowdsourcing interface for aligning CAD models to objects in a reconstruction. Objects can be clicked to initiate an assisted search for CAD models ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 2. Summary statistics for ScanNet compared to the most similar existing dataset (SceneNN [32]). ScanNet has an order of magnitude more scans, with 3D ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Distribution of the scans in ScanNet organized by type. our crowdsourcing task. In total, we deployed 3,391 anno- tation tasks to annotate all ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Train/Test split for object classification and dense voxel prediction tasks. Note that the number of instances does not in- clude the rotation augmentation. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our main goal driving the design of our framework was to allow untrained users to capture semantically labeled surfaces of indoor scenes with commodity ... | embodiment, simulator version and control stack | p. 3 (3. Dataset Acquisition Framework), p. 5 (4. ScanNet Dataset) |
| Task/environment | 5 plots the distribution of scanned scenes over different types of real-world spaces. | reset, timeout, object/scene variation | p. 5 (4. ScanNet Dataset), p. 6 (5. Tasks and Benchmarks) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 4 (3.2. Surface Reconstruction), p. 4 (3.2. Surface Reconstruction) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 1 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Percentages indicate average instance accuracy of retrieved model to query region. | definition/direction/unit from same section | p. 7 (5.1. 3D Object Classification) |
| Percentages give the classification accuracy over all models in each test set (average instance accuracy). | definition/direction/unit from same section | p. 7 (5.1. 3D Object Classification) |
| Dense pixel classification accuracy on NYU2 [58]. | definition/direction/unit from same section | p. 8 (5.2. Semantic Voxel Labeling) |
| Semantic voxel label prediction accuracy on ScanNet test scenes. before the CRF regularization. | definition/direction/unit from same section | p. 8 (5.2. Semantic Voxel Labeling) |
| We use these tasks to demonstrate that ScanNet enables the use of deep learning methods for 3D scene understanding tasks with supervised training, and ... | definition/direction/unit from same section | p. 6 (5. Tasks and Benchmarks) |
| In order to establish a clean snapshot to construct the ScanNet dataset reported in this paper, we automatically discard scan sequences that are short, ... | definition/direction/unit from same section | p. 4 (3.2. Surface Reconstruction) |
| Naturally, training with the corresponding synthetic counterparts of ShapeNet provides the best performance, as data characteristics are shared. | definition/direction/unit from same section | p. 6 (5.1. 3D Object Classification) |
| To conform with the goal for an automated and scalable framework, we choose methods that favor robustness and processing speed such that uploaded recordings ... | definition/direction/unit from same section | p. 4 (3.2. Surface Reconstruction) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Summary statistics for ScanNet compared to the most similar existing dataset (SceneNN [32]). | comparison identity and matched condition | p. 5 (3.3. Semantic Annotation) |
| As a baseline evaluation, we run the 3D CNN approach of Qi et al. | comparison identity and matched condition | p. 6 (5.1. 3D Object Classification) |
| We are able to outperform previous methods which are trained on limited sets of real-world data using our volumetric classification network. | comparison identity and matched condition | p. 7 (5.2. Semantic Voxel Labeling) |
| Prior work has focused mostly on controlled lab conditions with more accurate equipment to inform calibration for commodity sensors (e.g., Wang et al. | comparison identity and matched condition | p. 3 (3.1. RGB-D Scanning) |
| This is in contrast to much prior work that uses 2D polygon annotations on RGB or RGB-D images, or 3D bounding box annotations. | comparison identity and matched condition | p. 4 (3.3. Semantic Annotation) |
| This task of predicting a semantic class for each visible 3D voxel has been addressed by some prior work, but using handcrafted features to ... | comparison identity and matched condition | p. 7 (5.2. Semantic Voxel Labeling) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Without the turntable rotation animation, many workers only annotated from the initial view and never used camera controls despite the provided instructions. | component/input/data sensitivity | p. 5 (3.3. Semantic Annotation) |
| Earlier experiments without this constraint resulted in two undesirable behaviors: cheating by painting many surfaces with a few labels, and labeling of multiple object ... | component/input/data sensitivity | p. 5 (3.3. Semantic Annotation) |
| For object classification, we follow the network architecture of the 3D Network-in-Network of [66], without the multi-orientation pooling step. | component/input/data sensitivity | p. 6 (5.1. 3D Object Classification) |
| Table 8. Total counts of annotated object instances of the 50 largest categories in ScanNet (left), and in SceneNN [32] (right), the most similar ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| SceneNet trains on a large synthetic dataset and fine-tunes on NYU2. | component/input/data sensitivity | p. 8 (5.2. Semantic Voxel Labeling) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we introduce ScanNet, a dataset of richlyannotated RGB-D scans of real-world environments containing 2.5M RGB-D images in 1513 scans acquired in ... | On the other hand, training on ScanNet translates well to testing on SceneNN; as a result, the test results on SceneNN are significantly improved ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.1. 3D Object Classification), p. 20 (Figure/Table caption), p. 2 (Dataset), p. 3 (3.1. RGB-D Scanning), p. 7 (5.1. 3D Object Classification), p. 8 (5.2. Semantic Voxel Labeling) |
| Primary metric/result | Figure 15. Comparison of calibration results. In the top row, we show results of calibration on a flat wall. As the distance increases the ... | numeric claim only at cited anchor | p. 20 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 2 / Dataset - extractive PDF cue:** Size Labels Annotation Tool Reconstruction CAD Models NYU v2 [58] 464 scans 1449 frames 2D LabelMe-style [69] none some [25] TUM [81] 47 scans none ...
- **p. 3 / 3.1. RGB-D Scanning - extractive PDF cue:** The iPad RGB camera data is temporally synchronized with the depth sensor via hardware, providing synchronized depth and color capture at 30 Hz.
- **p. 6 / 5.1. 3D Object Classification - extractive PDF cue:** [66], we use an SGD solver with learning rate 0.01 and momentum 0.9, decaying the learning rate by half every 20 epochs, and training the ...
- **p. 6 / 5.1. 3D Object Classification - extractive PDF cue:** We augment training samples with 12 instances of different rotations (including both elevation and tilt), resulting in a total training set of 111, 660 samples.
- **p. 7 / 5.2. Semantic Voxel Labeling - extractive PDF cue:** In addition, we extract 18, 750 sample volumes for testing, which are also augmented by 8 rotations each (i.e., 150, 000 test samples) from 312 ...
- **p. 7 / 5.2. Semantic Voxel Labeling - extractive PDF cue:** We have 20 object class labels plus 1 class for free space.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1. Example reconstructed spaces in ScanNet annotated with instance-level object category labels through our crowdsourced annotation framework. ciently providing (dense) annotations in 3D ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | We demonstrated that the richlyannotated scan data collected so far in ScanNet is useful in achieving state-of-the-art performance on several 3D scene understanding tasks; ... | p. 8 (6. Conclusion) |
| body limitation/failure cue | This feature was critical for providing intuition to users who are not familiar with the constraints and limitations of 3D reconstruction algorithms. | p. 3 (3.1. RGB-D Scanning) |
| body limitation/failure cue | The main limitation of this interface is due to the mismatch between the corpus of available CAD models and the objects observed in the ... | p. 5 (3.3. Semantic Annotation) |
| body limitation/failure cue | A promising way to alleviate this limitation is to algorithmically suggest candidate retrieved and aligned CAD models such that workers can perform an easier ... | p. 5 (3.3. Semantic Annotation) |
| body limitation/failure cue | When training data is synthetic and test is performed on real data, there is also a significant discrepancy of test performance, as data characteristics, ... | p. 6 (5.1. 3D Object Classification) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| [66], we use an SGD solver with learning rate 0.01 and momentum 0.9, decaying the learning rate by half every 20 epochs, and training ... | p. 6 (5.1. 3D Object Classification) |
| There is a spectrum of choices for RGB-D sensor hardware. | p. 3 (3.1. RGB-D Scanning) |
| The iPad RGB camera data is temporally synchronized with the depth sensor via hardware, providing synchronized depth and color capture at 30 Hz. | p. 3 (3.1. RGB-D Scanning) |
| For each input scan, we first run BundleFusion [12] at a voxel resolution of 1 cm3. | p. 4 (3.2. Surface Reconstruction) |
| RGB data is encoded with the H.264 codec with a high bitrate of 15 Mbps to prevent encoding artifacts. | p. 4 (3.1. RGB-D Scanning) |
| As a baseline evaluation, we run the 3D CNN approach of Qi et al. | p. 6 (5.1. 3D Object Classification) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Example reconstructed spaces in ScanNet annotated with instance-level object category labels through our crowdsourced annotation framework. ciently providing (dense) annotations in 3D is ...
- **p. 8 / 6. Conclusion - extractive PDF cue:** We demonstrated that the richlyannotated scan data collected so far in ScanNet is useful in achieving state-of-the-art performance on several 3D scene understanding tasks; we ...
- **p. 3 / 3.1. RGB-D Scanning - extractive PDF cue:** This feature was critical for providing intuition to users who are not familiar with the constraints and limitations of 3D reconstruction algorithms.
- **p. 5 / 3.3. Semantic Annotation - extractive PDF cue:** The main limitation of this interface is due to the mismatch between the corpus of available CAD models and the objects observed in the ScanNet ...
- **p. 5 / 3.3. Semantic Annotation - extractive PDF cue:** A promising way to alleviate this limitation is to algorithmically suggest candidate retrieved and aligned CAD models such that workers can perform an easier verification ...
- **p. 6 / 5.1. 3D Object Classification - extractive PDF cue:** When training data is synthetic and test is performed on real data, there is also a significant discrepancy of test performance, as data characteristics, such ...

- **PDF anchors reviewed:** datasets p. 3 (3. Dataset Acquisition Framework), p. 5 (4. ScanNet Dataset), p. 6 (5. Tasks and Benchmarks), p. 6 (5.1. 3D Object Classification), p. 7 (5.1. 3D Object Classification), p. 2 (Dataset), metrics p. 7 (5.1. 3D Object Classification), p. 7 (5.1. 3D Object Classification), p. 8 (5.2. Semantic Voxel Labeling), p. 8 (5.2. Semantic Voxel Labeling), p. 6 (5. Tasks and Benchmarks), p. 4 (3.2. Surface Reconstruction), baselines p. 5 (3.3. Semantic Annotation), p. 6 (5.1. 3D Object Classification), p. 7 (5.2. Semantic Voxel Labeling), p. 3 (3.1. RGB-D Scanning), p. 4 (3.3. Semantic Annotation), p. 7 (5.2. Semantic Voxel Labeling), results p. 7 (5.1. 3D Object Classification), p. 20 (Figure/Table caption), p. 2 (Dataset), p. 3 (3.1. RGB-D Scanning), p. 7 (5.1. 3D Object Classification), p. 8 (5.2. Semantic Voxel Labeling).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
