# Evaluation - EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite Towards Embodied AI

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.1. Fundamental 3D Perception Benchmarks), p. 3 (Figure/Table caption), p. 7 (5.1. Fundamental 3D Perception Benchmarks), p. 8 (5.2. Language-Grounded Benchmark), p. 8 (5.1. Fundamental 3D Perception Benchmarks), p. 2 (Dataset)): Substituting this with our decoder design markedly improves performance.

## Evaluation Body Digest

- **p. 2 / Dataset - extractive body cue:** To bridge this divide, we introduce a multi-modal, egocentric 3D perception dataset and benchmark for holistic 3D scene understanding, termed EmbodiedScan, aimed at facilitating real-world ...
- **p. 2 / Dataset - extractive body cue:** Comparison with other 3D indoor scene datasets. "Cats" refers to the categories with box annotations for the 3D detection benchmark.
- **p. 4 / 3.3. Statistics - extractive body cue:** We remove four categories, {wall, ceiling, floor, object} in our 3D detection benchmark and divide the remaining 284 categories into three splits, {head, common, tail} ...
- **p. 6 / 5. Benchmark - extractive body cue:** Scenebased benchmarks mean the samples are based on different scenes, covering continuous and multi-view perception.
- **p. 6 / 5. Benchmark - extractive body cue:** Detailed splits will be discussed in each benchmark.
- **p. 7 / 5. Benchmark - extractive body cue:** Continuous and multi-view occupancy prediction benchmark (split by the double line). "refri." means "refrigerator".
- **p. 8 / 5.2. Language-Grounded Benchmark - extractive body cue:** Data sample splits align with previous benchmarks' 3D scan splits.
- **p. 3 / 3.1. Data Collection & Processing - extractive body cue:** Considering there have been readily available 3D indoor scene scans from existing datasets, we start with integrating those providing ego-centric RGB-D captures with the corresponding ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** Dataset (p. 2); 3. Dataset (p. 3); 5. Benchmark (p. 6); 5.1. Fundamental 3D Perception Benchmarks (p. 7); 5.2. Language-Grounded Benchmark (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.1. Fundamental 3D Perception Benchmarks | BENCHMARK / DATASET | Substituting this with our decoder design markedly improves performance. | p. 7 (5.1. Fundamental 3D Perception Benchmarks) |
| Figure/Table caption | BENCHMARK / DATASET | Figure 3. EmbodiedScan annotation and statistics. (a) UI for 3D box annotation. We select keyframes and generate their SAM masks with corresponding axis-aligned boxes. ... | p. 3 (Figure/Table caption) |
| 5.1. Fundamental 3D Perception Benchmarks | BENCHMARK / DATASET | Nevertheless, all models have substantial potential for improvement, demonstrating the challenges of this new dataset and setup. | p. 7 (5.1. Fundamental 3D Perception Benchmarks) |
| 5.2. Language-Grounded Benchmark | BENCHMARK / DATASET | Our baseline outperforms all due to the strong multi-modal encoder. | p. 8 (5.2. Language-Grounded Benchmark) |
| 5.1. Fundamental 3D Perception Benchmarks | BENCHMARK / DATASET | Similarly, our method outperforms others, providing a solid baseline for future studies. | p. 8 (5.1. Fundamental 3D Perception Benchmarks) |

## Dataset / Benchmark Role

- **p. 2 / Dataset - extractive body cue:** To bridge this divide, we introduce a multi-modal, egocentric 3D perception dataset and benchmark for holistic 3D scene understanding, termed EmbodiedScan, aimed at facilitating real-world ...
- **p. 2 / Dataset - extractive body cue:** Comparison with other 3D indoor scene datasets. "Cats" refers to the categories with box annotations for the 3D detection benchmark.
- **p. 4 / 3.3. Statistics - extractive body cue:** We remove four categories, {wall, ceiling, floor, object} in our 3D detection benchmark and divide the remaining 284 categories into three splits, {head, common, tail} ...
- **p. 6 / 5. Benchmark - extractive body cue:** Scenebased benchmarks mean the samples are based on different scenes, covering continuous and multi-view perception.
- **p. 6 / 5. Benchmark - extractive body cue:** Detailed splits will be discussed in each benchmark.
- **p. 7 / 5. Benchmark - extractive body cue:** Continuous and multi-view occupancy prediction benchmark (split by the double line). "refri." means "refrigerator".
- **p. 8 / 5.2. Language-Grounded Benchmark - extractive body cue:** Data sample splits align with previous benchmarks' 3D scan splits.
- **p. 3 / 3.1. Data Collection & Processing - extractive body cue:** Considering there have been readily available 3D indoor scene scans from existing datasets, we start with integrating those providing ego-centric RGB-D captures with the corresponding ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. EmbodiedScan provides a multi-modal, ego-centric 3D perception dataset with massive real-scanned data and rich annotations for indoor scenes. It benchmarks language-grounded holistic 3D ...
- **p. 2 / Figure/Table caption - extractive body cue:** Table 1. Comparison with other 3D indoor scene datasets. "Cats" refers to the categories with box annotations for the 3D detection benchmark. EmbodiedScan features more ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Dataset composition. Embodied- Scan is composed of three data sources and has similar scans, images, objects, and cate- gories in each of them. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. EmbodiedScan annotation and statistics. (a) UI for 3D box annotation. We select keyframes and generate their SAM masks with corresponding axis-aligned boxes. With ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Embodied Perceptron accepts RGB-D sequence with any number of views along with texts as multi-modal input. It uses classical encoders to extract features ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Continuous and multi-view 3D object detection benchmark on EmbodiedScan (split by the double line). Methods Input Large-Vocabulary Head Common Tail AP25
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Continuous and multi-view occupancy prediction benchmark (split by the double line). "refri." means "refrigerator". Methods Input mIOU empty floor wall chair
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Monocular 3D object detection benchmark on EmbodiedScan. Methods Input

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To bridge this divide, we introduce a multi-modal, egocentric 3D perception dataset and benchmark for holistic 3D scene understanding, termed EmbodiedScan, aimed at facilitating ... | embodiment, simulator version and control stack | p. 2 (Dataset), p. 2 (Dataset) |
| Task/environment | Comparison with other 3D indoor scene datasets. "Cats" refers to the categories with box annotations for the 3D detection benchmark. | reset, timeout, object/scene variation | p. 2 (Dataset), p. 4 (3.3. Statistics) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 4 (4. Embodied Perceptron), p. 1 (1. Introduction) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 1 (Abstract), p. 4 (3.1. Data Collection & Processing) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For metrics, we use the 3D IoU-based average precision (AP) with thresholds of 0.25 and 0.5 for 3D detection and visual grounding. | definition/direction/unit from same section | p. 6 (5. Benchmark) |
| This benchmark offers comprehensive results including mIoU and IoU for common classes. | definition/direction/unit from same section | p. 7 (5.1. Fundamental 3D Perception Benchmarks) |
| Detailed analysis further underscores the value of EmbodiedScan and highlights the primary challenges posed by this new setup. | definition/direction/unit from same section | p. 2 (Dataset) |
| 6), implying that the accuracy of reconstructed point clouds is superior to raw depth maps. | definition/direction/unit from same section | p. 8 (5.3. Analysis) |
| We also provide average recall (AR) for reference. | definition/direction/unit from same section | p. 6 (5. Benchmark) |
| Their performance slightly lags behind our camera-only baseline. | definition/direction/unit from same section | p. 7 (5.1. Fundamental 3D Perception Benchmarks) |
| 4), observing a larger AP-AR gap for top methods because of difficulties predicting accurate 3D boxes from partial views. | definition/direction/unit from same section | p. 8 (5.1. Fundamental 3D Perception Benchmarks) |
| Semantic occupancy necessitates accurate boundaries across semantic regions without considering object pose or recalling all the objects, so the original point cloud segmentation annotations ... | definition/direction/unit from same section | p. 4 (3.2. Annotation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our baseline outperforms all due to the strong multi-modal encoder. | comparison identity and matched condition | p. 8 (5.2. Language-Grounded Benchmark) |
| Similarly, our method outperforms others, providing a solid baseline for future studies. | comparison identity and matched condition | p. 8 (5.1. Fundamental 3D Perception Benchmarks) |
| Built upon this dataset, we devise a baseline framework for ego-centric 3D perception, Embodied Perceptron. | comparison identity and matched condition | p. 2 (Dataset) |
| Experimental results validate the effectiveness of our baseline model on EmbodiedScan and demonstrate its generalization ability in the wild. | comparison identity and matched condition | p. 2 (Dataset) |
| Due to the space limitation, please refer to the appendix for implementation details of different baselines, and more quantitative and qualitative results including an ... | comparison identity and matched condition | p. 6 (5. Benchmark) |
| Their performance slightly lags behind our camera-only baseline. | comparison identity and matched condition | p. 7 (5.1. Fundamental 3D Perception Benchmarks) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We remove four categories, {wall, ceiling, floor, object} in our 3D detection benchmark and divide the remaining 284 categories into three splits, {head, common, ... | component/input/data sensitivity | p. 4 (3.3. Statistics) |
| Semantic occupancy necessitates accurate boundaries across semantic regions without considering object pose or recalling all the objects, so the original point cloud segmentation annotations ... | component/input/data sensitivity | p. 4 (3.2. Annotation) |
| If a category lacks instances, it is removed when calculating mAP and mIoU. | component/input/data sensitivity | p. 7 (5.1. Fundamental 3D Perception Benchmarks) |
| Variants of our baselines exhibit a performance trend akin to embodied benchmarks. | component/input/data sensitivity | p. 7 (5.1. Fundamental 3D Perception Benchmarks) |
| Ablation with conventional settings. | component/input/data sensitivity | p. 8 (5.1. Fundamental 3D Perception Benchmarks) |
| As an initial step, this setup takes multi-view RGB-D images as input without considering differing prompt timestamps. | component/input/data sensitivity | p. 8 (5.2. Language-Grounded Benchmark) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Building upon this database, we introduce a baseline framework named Embodied Perceptron. | Substituting this with our decoder design markedly improves performance. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.1. Fundamental 3D Perception Benchmarks), p. 3 (Figure/Table caption), p. 7 (5.1. Fundamental 3D Perception Benchmarks), p. 8 (5.2. Language-Grounded Benchmark), p. 8 (5.1. Fundamental 3D Perception Benchmarks), p. 2 (Dataset) |
| Primary metric/result | Figure 3. EmbodiedScan annotation and statistics. (a) UI for 3D box annotation. We select keyframes and generate their SAM masks with corresponding axis-aligned boxes. ... | numeric claim only at cited anchor | p. 3 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 4 / 3.1. Data Collection & Processing - extractive body cue:** As for different sampling rates of images in ScanNet and 3RScan videos, we sample one keyframe per 10 frames for ScanNet and keep all the ...
- **p. 7 / 5.1. Fundamental 3D Perception Benchmarks - extractive body cue:** Here, N = 10 during training with random view sampling, while in evaluation, N = 50 with fixed views.
- **p. 8 / 5.1. Fundamental 3D Perception Benchmarks - extractive body cue:** Train Val Overall Head Common Tail Render Render 22.11 33.01 16.44 6.74 Render Real 18.72 27.02 14.85 6.25 Real Real 21.98 32.91 17.18 5.05 frame ...
- **p. 4 / 3.1. Data Collection & Processing - extractive body cue:** As for different sampling rates of images in ScanNet and 3RScan videos, we sample one keyframe per 10 frames for ScanNet and keep all the ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | On the other hand, since we cannot trivially obtain the reconstruction of a new environment, models trained with scene-level input are not directly applicable ... | p. 2 (Dataset) |
| body limitation/failure cue | Figure 2. Dataset composition. Embodied- Scan is composed of three data sources and has similar scans, images, objects, and cate- gories in each of ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | 3a) to address limitations in existing 3D box annotations, i.e., lack of orientation and small object annotations. | p. 4 (3.2. Annotation) |
| body limitation/failure cue | Generated language prompts following SR3D fall into five types of spatial object-to-object relations: Horizontal Proximity, Vertical Proximity, Support, Allocentric, and Between. | p. 4 (3.3. Statistics) |
| body limitation/failure cue | Due to the space limitation, please refer to the appendix for implementation details of different baselines, and more quantitative and qualitative results including an ... | p. 6 (5. Benchmark) |
| body limitation/failure cue | Unlike continuous settings, multi-view 3D perception does not predefine the order of views but provides all views to the model for scene-level results. | p. 7 (5.1. Fundamental 3D Perception Benchmarks) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Specifically, we use one of three groups of decoded predictions, {3D centers, 3D sizes, and Euler angles}, while setting the other two with ground ... | p. 6 (4.2. Sparse & Dense Decoder) |
| In the realm of computer vision and robotics, embodied agents are expected to explore their environment and carry out human instructions. | p. 1 (Abstract) |
| Nonetheless, subtle but significant discrepancies exist between this expectation and research problems examined within the computer vision community. | p. 1 (1. Introduction) |
| It accepts RGB-D sequences and texts as inputs and manifests scalability to any number of views input with encoders shared across different tasks. | p. 2 (Dataset) |
| With the encoded 2D and 3D features, we employ dense fusion and isomorphic multilevel fusion across them guided by the perspective projection to produce ... | p. 2 (Dataset) |
| For the sparse case, we use multi-level features as seeds instead of a single dense feature map to predict 3D objects. | p. 5 (4.1. Multi-Modal 3D Encoder) |
| In practice, these two ResNets produce 4 levels of features, for both point clouds and images, denoted as isomorphic multi-modality encoders. | p. 5 (4.1. Multi-Modal 3D Encoder) |
| Sparse Decoder for 3D Boxes Prediction. | p. 6 (4.2. Sparse & Dense Decoder) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Dataset - extractive body cue:** On the other hand, since we cannot trivially obtain the reconstruction of a new environment, models trained with scene-level input are not directly applicable in ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Dataset composition. Embodied- Scan is composed of three data sources and has similar scans, images, objects, and cate- gories in each of them. ...
- **p. 4 / 3.2. Annotation - extractive body cue:** 3a) to address limitations in existing 3D box annotations, i.e., lack of orientation and small object annotations.
- **p. 4 / 3.3. Statistics - extractive body cue:** Generated language prompts following SR3D fall into five types of spatial object-to-object relations: Horizontal Proximity, Vertical Proximity, Support, Allocentric, and Between.
- **p. 6 / 5. Benchmark - extractive body cue:** Due to the space limitation, please refer to the appendix for implementation details of different baselines, and more quantitative and qualitative results including an "in-the-wild" ...
- **p. 7 / 5.1. Fundamental 3D Perception Benchmarks - extractive body cue:** Unlike continuous settings, multi-view 3D perception does not predefine the order of views but provides all views to the model for scene-level results.

- **Evidence anchors reviewed:** datasets p. 2 (Dataset), p. 2 (Dataset), p. 4 (3.3. Statistics), p. 6 (5. Benchmark), p. 6 (5. Benchmark), p. 7 (5. Benchmark), metrics p. 6 (5. Benchmark), p. 7 (5.1. Fundamental 3D Perception Benchmarks), p. 2 (Dataset), p. 8 (5.3. Analysis), p. 6 (5. Benchmark), p. 7 (5.1. Fundamental 3D Perception Benchmarks), baselines p. 8 (5.2. Language-Grounded Benchmark), p. 8 (5.1. Fundamental 3D Perception Benchmarks), p. 2 (Dataset), p. 2 (Dataset), p. 6 (5. Benchmark), p. 7 (5.1. Fundamental 3D Perception Benchmarks), results p. 7 (5.1. Fundamental 3D Perception Benchmarks), p. 3 (Figure/Table caption), p. 7 (5.1. Fundamental 3D Perception Benchmarks), p. 8 (5.2. Language-Grounded Benchmark), p. 8 (5.1. Fundamental 3D Perception Benchmarks), p. 2 (Dataset).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
