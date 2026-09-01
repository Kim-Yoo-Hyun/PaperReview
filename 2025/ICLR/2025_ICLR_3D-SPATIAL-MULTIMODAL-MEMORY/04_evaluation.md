# Evaluation - 3D-SPATIAL MULTIMODAL MEMORY

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=XYdstv3ySl; PDF retrieval source: https://openreview.net/pdf/49718e82c4fa24eac05ec11d26bd767cd526299a.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS)): Our method, M3, outperforms F-Splat while reducing significantly compute than F-3DGS.

## Evaluation Body Digest

- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** To support extensive quantitative and qualitative evaluation, we perform experiments using several existing scene datasets [3; 18; 10] and collected a custom robot dataset (M3-Robot) ...
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** For the M3-Robot dataset, we collect images using two mobile robots.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** After memorizing the scene with M3, the robot is able to locate and grasp any object with text query on decoded CLIP feature.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** The robot can then locate the 3D position of the targeted object with depth information from its depth camera and perform a grasping task.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** We evaluate all the images in the validation sets of the three datasets.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Furthermore, M3 handles overlapping objects exceptionally well, as evident in the Playroom dataset, where complex arrangements are rendered with accurate structural information.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** High-level evaluation metrics, different from low-level ones, focus on evaluating downstream tasks of features.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** To systematically evaluate multi-modal memory, we use evaluation metrics ranging from low/pixel-level to high-level downstream tasks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 6); B M3 LMM BENCHMARK (p. 16); C QUALITATIVE RESULTS (p. 18).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method, M3, outperforms F-Splat while reducing significantly compute than F-3DGS. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The table clearly shows that increasing the number degree will generally improve the performance on all metrics. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4.2 QUANTITATIVE RESULTS Baseline Implementation For quantitative experiments, we compare M3 with two recent distillation-based feature GS methods [26; 51]. | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Published as a conference paper at ICLR 2025 Figure 6: Qualitative results across datasets using M3. | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | M3 demonstrates superior downstream task accuracy with reduced training costs and shows practical utility when deployed on a real robot. | p. 9 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** To support extensive quantitative and qualitative evaluation, we perform experiments using several existing scene datasets [3; 18; 10] and collected a custom robot dataset (M3-Robot) ...
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** For the M3-Robot dataset, we collect images using two mobile robots.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** After memorizing the scene with M3, the robot is able to locate and grasp any object with text query on decoded CLIP feature.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** The robot can then locate the 3D position of the targeted object with depth information from its depth camera and perform a grasping task.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** We evaluate all the images in the validation sets of the three datasets.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Furthermore, M3 handles overlapping objects exceptionally well, as evident in the Playroom dataset, where complex arrangements are rendered with accurate structural information.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** High-level evaluation metrics, different from low-level ones, focus on evaluating downstream tasks of features.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** To systematically evaluate multi-modal memory, we use evaluation metrics ranging from low/pixel-level to high-level downstream tasks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Our proposed MultiModal Memory integrates Gaussian splatting with foundation models to efficiently store multimodal memory in a Gaussian structure. The feature maps rendered ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: A scene (V) is composed of both structure (S) and knowledge (I). To model these, we leverage multiple foundation models to extract multi-granularity ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3: Given a video sequence, we utilize foundation models (F) to extract raw features (R). These features are reduced using Algorithm 1, producing principal ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4: The UMAP visu- alization of model embed- ding manifolds reveals dis- tinct shapes, reflecting dif- ferent focus. Extract Multi-Granularity Scene Knowledge. Upon preparing ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5: Illustration of patch-level visual embedding extraction their applications. Compress Scene Knowledge to Memory. While the scene knowledge is extracted from foundation models F ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Feature Distance in comparison with distillation methods that use similar or higher budgets across datasets and foundation models. CLIP SigLIP
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: Feature/RGB metrics for all foundation models and scene. only distill a few (2-3) models. Specifically, as provided in Sec. 3.3, we employ 6 ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Ablation on the number of foundation models in M3. Degree # Params Iteration CLIP SigLIP DINOv2 SEEM

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To support extensive quantitative and qualitative evaluation, we perform experiments using several existing scene datasets [3; 18; 10] and collected a custom robot dataset ... | embodiment, simulator version and control stack | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Task/environment | For the M3-Robot dataset, we collect images using two mobile robots. | reset, timeout, object/scene variation | p. 6 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3 METHOD), p. 4 (3 METHOD) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3 METHOD), p. 2 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| M3 demonstrates superior downstream task accuracy with reduced training costs and shows practical utility when deployed on a real robot. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| In compensate, we use point-based loss, where we sample 2000 points ranging from both predict and ground truth features for distance loss computation. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Previous methods [26; 51] compute the patch-wise distance loss on the rendered features, this not only has a high volume of GPU memory consumption ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| M3 consistently demonstrates superior performance across diverse datasets as shown in Fig. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Images in the Geisel sequence are collected by a tele-operated DJI Mini4-Pro drone. | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| The Table-Top sequence is collected from a RealSense 405D camera mounted on the end effector of a Unitree Z1 robot arm on a Unitree ... | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| This demonstrates M3's capability to capture both 8 | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| We also deployed M3 on a quadruped robot platform to demonstrate the potential real world applications of our model. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 4.2 QUANTITATIVE RESULTS Baseline Implementation For quantitative experiments, we compare M3 with two recent distillation-based feature GS methods [26; 51]. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| Our method, M3, outperforms F-Splat while reducing significantly compute than F-3DGS. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| Compared to grounding performance, M3 performs much better than F-3DGS on retrieval results. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| Figure 5: Illustration of patch-level visual embedding extraction their applications. Compress Scene Knowledge to Memory. While the scene knowledge is extracted from foundation models ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| For fair comparisons, we train all the methods in approximately 30,000 iterations (29,993 iterations for M3 due to last-batch data loader roundoffs). | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 3 shows the ablation of the number of foundation models involved in M3. | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Cosine↓ L2↓ Cosine↓ L2↓ Cosine↓ L2↓ Cosine↓ L2↓ Cosine↓ L2↓ Cosine↓ L2↓ Tabletop +CLIP 21.91 ∼6 0.3100 0.2956 - - - - - - ... | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Figure 3: Given a video sequence, we utilize foundation models (F) to extract raw features (R). These features are reduced using Algorithm 1, producing ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Specifically, we propose to store the original high-dimensional 2D feature maps in a memory bank called principal scene components and use the low-dimensional principal ... | Our method, M3, outperforms F-Splat while reducing significantly compute than F-3DGS. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Primary metric/result | The table clearly shows that increasing the number degree will generally improve the performance on all metrics. | numeric claim only at cited anchor | p. 8 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** In compensate, we use point-based loss, where we sample 2000 points ranging from both predict and ground truth features for distance loss computation.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** While having 16 degrees for each foundation model is enough to obtain a reasonable performance.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | SEEM and LLaMA3 features extraction failed on FSplat, which we assume was mainly due to the ground truth feature extraction procedure, where duplication was ... | p. 8 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Previous methods [26; 51] compute the patch-wise distance loss on the rendered features, this not only has a high volume of GPU memory consumption ... | p. 7 (4 EXPERIMENTS) |
| 1, where the average training time and the auxiliary low-level metrics are reported. | p. 8 (4 EXPERIMENTS) |
| While maintaining a very efficient training time, our method has independent results from different foundation models. | p. 8 (4 EXPERIMENTS) |
| For distillation-based methods, we follow F-Splat [26] to render a latent feature and then decode the latent features to the embedding 7 | p. 7 (4 EXPERIMENTS) |
| We tested with the query "yellow bath duck" on the decoded CLIP feature, and as shown in Fig. | p. 9 (4 EXPERIMENTS) |
| After memorizing the scene with M3, the robot is able to locate and grasp any object with text query on decoded CLIP feature. | p. 9 (4 EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** SEEM and LLaMA3 features extraction failed on FSplat, which we assume was mainly due to the ground truth feature extraction procedure, where duplication was performed ...

- **PDF anchors reviewed:** datasets p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), metrics p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), baselines p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 6 (Figure/Table caption), p. 7 (4 EXPERIMENTS), results p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
