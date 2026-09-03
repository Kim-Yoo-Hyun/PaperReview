# Evaluation - LightSplat: Fast and Memory-Efficient Open-Vocabulary 3D Scene Understanding in Five Seconds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Bang_LightSplat_Fast_and_Memory-Efficient_Open-Vocabulary_3D_Scene_Understanding_in_Five_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Bang_LightSplat_Fast_and_Memory-Efficient_Open-Vocabulary_3D_Scene_Understanding_in_Five_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. 3D Semantic Segmentation), p. 1 (Figure/Table caption), p. 5 (4.2. 3D Object Selection), p. 5 (4.2. 3D Object Selection), p. 6 (4.3. 3D Semantic Segmentation), p. 6 (4.2. 3D Object Selection)): With context-aware 3D clustering, our method achieves detailed object boundaries while offering significantly faster performance than other methods.

## Evaluation Body Digest

- **p. 5 / 4.1. Experimental Setup - extractive body cue:** The dataset covers a wide range of object scales, distances, and scene complexities across four scenes (park, road, shop, and office), with categories containing varying ...
- **p. 8 / 4.3. 3D Semantic Segmentation - extractive body cue:** Compared to other methods, our approach more effectively captures both object (e.g., door) and large-area semantics (e.g., wall), demonstrating robustness across diverse real-world scenes and ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** The second is ScanNet, a largescale RGB-D dataset containing 1,500 indoor scenes, each with reconstructed point clouds and per-point semantic labels.
- **p. 6 / 4.2. 3D Object Selection - extractive body cue:** Quantitative comparison for 3D Object Selection on the LERF-OVS dataset.
- **p. 6 / 4.2. 3D Object Selection - extractive body cue:** Methods 19 classes 15 classes 10 classes FD Time Runtime Memory mIoU mAcc mIoU mAcc mIoU mAcc (second) (byte) LangSplat 2.61 10.11 4.08 13.22 6.30 ...
- **p. 7 / 4.3. 3D Semantic Segmentation - extractive body cue:** Qualitative comparison for 3D Object Selection on the DL3DV-OVS dataset.
- **p. 7 / 4.3. 3D Semantic Segmentation - extractive body cue:** We visualize model behavior on large and complex scenes in DL3DV-OVS, covering both indoor and outdoor environments.
- **p. 8 / 4.3. 3D Semantic Segmentation - extractive body cue:** Ablation Study on LERF-OVS dataset.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Setup (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. 3D Semantic Segmentation | EMPIRICAL / REAL-ROBOT OR HARDWARE | With context-aware 3D clustering, our method achieves detailed object boundaries while offering significantly faster performance than other methods. | p. 7 (4.3. 3D Semantic Segmentation) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 1. Comprehensive comparison of speed, performance, and memory overhead. We evaluate recent open-vocabulary 3D scene understanding models in terms of distillation time (x-axis), ... | p. 1 (Figure/Table caption) |
| 4.2. 3D Object Selection | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 2, our approach also achieves strong performance on DL3DV-OVS, a dataset with large and 19816 | p. 5 (4.2. 3D Object Selection) |
| 4.2. 3D Object Selection | EMPIRICAL / REAL-ROBOT OR HARDWARE | Even without training, our method achieves SOTA performance on LERF-OVS, with a 50× speedup over recent models, as shown in Table 1. | p. 5 (4.2. 3D Object Selection) |
| 4.3. 3D Semantic Segmentation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method achieves the best performance across all settings. | p. 6 (4.3. 3D Semantic Segmentation) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experimental Setup - extractive body cue:** The dataset covers a wide range of object scales, distances, and scene complexities across four scenes (park, road, shop, and office), with categories containing varying ...
- **p. 8 / 4.3. 3D Semantic Segmentation - extractive body cue:** Compared to other methods, our approach more effectively captures both object (e.g., door) and large-area semantics (e.g., wall), demonstrating robustness across diverse real-world scenes and ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** The second is ScanNet, a largescale RGB-D dataset containing 1,500 indoor scenes, each with reconstructed point clouds and per-point semantic labels.
- **p. 6 / 4.2. 3D Object Selection - extractive body cue:** Quantitative comparison for 3D Object Selection on the LERF-OVS dataset.
- **p. 6 / 4.2. 3D Object Selection - extractive body cue:** Methods 19 classes 15 classes 10 classes FD Time Runtime Memory mIoU mAcc mIoU mAcc mIoU mAcc (second) (byte) LangSplat 2.61 10.11 4.08 13.22 6.30 ...
- **p. 7 / 4.3. 3D Semantic Segmentation - extractive body cue:** Qualitative comparison for 3D Object Selection on the DL3DV-OVS dataset.
- **p. 7 / 4.3. 3D Semantic Segmentation - extractive body cue:** We visualize model behavior on large and complex scenes in DL3DV-OVS, covering both indoor and outdoor environments.
- **p. 8 / 4.3. 3D Semantic Segmentation - extractive body cue:** Ablation Study on LERF-OVS dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Comprehensive comparison of speed, performance, and memory overhead. We evaluate recent open-vocabulary 3D scene understanding models in terms of distillation time (x-axis), segmentation ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overall framework of LightSplat. From multi-view images, we obtain SAM masks and corresponding CLIP features. We align them to the 3D scene via ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Fast inference via cluster-feature mapping. During inference, the text query is compared with a compact set of cluster features instead of all Gaussians ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparison for 3D Object Selection on the LERF-OVS dataset. Red and orange highlight the best and second- best results in each column. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Quantitative comparison for 3D Object Selection on the DL3DV-OVS dataset. Red and orange highlight the best and second- best results in each column. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Quantitative comparison for 3D Semantic Segmentation on the ScanNet dataset. Red and orange highlight the best and second-best results in each column. FD ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative comparison for 3D Object Selection on the LERF-OVS dataset. We visualize model performance across different scenes and text queries in LERF-OVS. With ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative comparison for 3D Object Selection on the DL3DV-OVS dataset. We visualize model behavior on large and complex scenes in DL3DV-OVS, covering both ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset covers a wide range of object scales, distances, and scene complexities across four scenes (park, road, shop, and office), with categories containing ... | embodiment, simulator version and control stack | p. 5 (4.1. Experimental Setup), p. 8 (4.3. 3D Semantic Segmentation) |
| Task/environment | Compared to other methods, our approach more effectively captures both object (e.g., door) and large-area semantics (e.g., wall), demonstrating robustness across diverse real-world scenes ... | reset, timeout, object/scene variation | p. 8 (4.3. 3D Semantic Segmentation), p. 5 (4.1. Experimental Setup) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.3. Indexed Feature Injection), p. 1 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 3 (3.1. Overview) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 1. Comprehensive comparison of speed, performance, and memory overhead. We evaluate recent open-vocabulary 3D scene understanding models in terms of distillation time (x-axis), ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| The results demonstrate that each component not only boosts performance, but also directly contributes to the fast FD time of our method. | definition/direction/unit from same section | p. 8 (4.3. 3D Semantic Segmentation) |
| We evaluate performance on two standard tasks. | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| For robustness evaluation beyond limited indoor environments, we introduce the DL3DV-OVS dataset. | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| Our method achieves the best performance across all settings. | definition/direction/unit from same section | p. 6 (4.3. 3D Semantic Segmentation) |
| Such results highlight the flexibility and robustness of our method across diverse object scales and scene complexities. | definition/direction/unit from same section | p. 6 (4.2. 3D Object Selection) |
| We visualize model performance across different scenes and text queries in LERF-OVS. | definition/direction/unit from same section | p. 7 (4.3. 3D Semantic Segmentation) |
| With context-aware 3D clustering, our method achieves detailed object boundaries while offering significantly faster performance than other methods. | definition/direction/unit from same section | p. 7 (4.3. 3D Semantic Segmentation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 3. Fast inference via cluster-feature mapping. During inference, the text query is compared with a compact set of cluster features instead of all ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| Compared to other methods, our approach more effectively captures both object (e.g., door) and large-area semantics (e.g., wall), demonstrating robustness across diverse real-world scenes ... | comparison identity and matched condition | p. 8 (4.3. 3D Semantic Segmentation) |
| Even without training, our method achieves SOTA performance on LERF-OVS, with a 50× speedup over recent models, as shown in Table 1. | comparison identity and matched condition | p. 5 (4.2. 3D Object Selection) |
| For fair comparison on ScanNet, we follow the evaluation protocol of OpenGaussian and use the same 10 scenes. | comparison identity and matched condition | p. 5 (4.1. Experimental Setup) |
| Quantitative comparison for 3D Object Selection on the LERF-OVS dataset. | comparison identity and matched condition | p. 6 (4.2. 3D Object Selection) |
| 5 present the qualitative comparison on the LERF-OVS and DL3DV-OVS dataset. | comparison identity and matched condition | p. 6 (4.2. 3D Object Selection) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conduct an ablation study by removing each component individually. | component/input/data sensitivity | p. 8 (4.4. Ablation Study) |
| Even without training, our method achieves SOTA performance on LERF-OVS, with a 50× speedup over recent models, as shown in Table 1. | component/input/data sensitivity | p. 5 (4.2. 3D Object Selection) |
| Ablation Study on LERF-OVS dataset. | component/input/data sensitivity | p. 8 (4.3. 3D Semantic Segmentation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our main contributions are as follows: • We propose LightSplat, a simple, training-free framework for open-vocabulary 3D scene understanding eliminating exhaustive iterative ... | With context-aware 3D clustering, our method achieves detailed object boundaries while offering significantly faster performance than other methods. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. 3D Semantic Segmentation), p. 1 (Figure/Table caption), p. 5 (4.2. 3D Object Selection), p. 5 (4.2. 3D Object Selection), p. 6 (4.3. 3D Semantic Segmentation), p. 6 (4.2. 3D Object Selection) |
| Primary metric/result | Figure 1. Comprehensive comparison of speed, performance, and memory overhead. We evaluate recent open-vocabulary 3D scene understanding models in terms of distillation time (x-axis), ... | numeric claim only at cited anchor | p. 1 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** For fair comparison on ScanNet, we follow the evaluation protocol of OpenGaussian and use the same 10 scenes.
- **p. 6 / 4.2. 3D Object Selection - extractive body cue:** Methods 19 classes 15 classes 10 classes FD Time Runtime Memory mIoU mAcc mIoU mAcc mIoU mAcc (second) (byte) LangSplat 2.61 10.11 4.08 13.22 6.30 ...
- **p. 7 / 4.3. 3D Semantic Segmentation - extractive body cue:** In addition, our approach reduces feature distillation to only 4.1 seconds and improves memory efficiency by up to 64×, while supporting fast inference at 500 ...
- **p. 4 / 3.3. Indexed Feature Injection - extractive body cue:** Our approach significantly reduces memory usage by 1024 times compared to storing CLIP features directly, reducing the size from 4×512 bytes to just 2 bytes ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Removing semantic-aware clustering decreases performance by over 50%, as the model cannot identify semantically corresponding masks across views for merging. | p. 8 (4.4. Ablation Study) |
| body limitation/failure cue | Since Dr.Splat does not provide inference code, we adopt the reported inference results from its paper and measure all other results ourselves. | p. 5 (4.1. Experimental Setup) |
| body limitation/failure cue | For robustness evaluation beyond limited indoor environments, we introduce the DL3DV-OVS dataset. | p. 5 (4.1. Experimental Setup) |
| body limitation/failure cue | Such results highlight the flexibility and robustness of our method across diverse object scales and scene complexities. | p. 6 (4.2. 3D Object Selection) |
| body limitation/failure cue | Our method shows robust performance on the road scene with multiple distant cars and the office scene with repeated objects such as chairs and ... | p. 6 (4.2. 3D Object Selection) |
| body limitation/failure cue | Since these methods use semantics at the level of individual Gaussians, they fail to form mean19818 | p. 7 (4.3. 3D Semantic Segmentation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| FD Time, Runtime, and Memory indicate the feature distillation time, average inference time per text query, and feature size per Gaussian, respectively. | p. 6 (4.2. 3D Object Selection) |
| Since Dr.Splat does not provide inference code, we adopt the reported inference results from its paper and measure all other results ourselves. | p. 5 (4.1. Experimental Setup) |
| Methods 19 classes 15 classes 10 classes FD Time Runtime Memory mIoU mAcc mIoU mAcc mIoU mAcc (second) (byte) LangSplat 2.61 10.11 4.08 13.22 ... | p. 6 (4.2. 3D Object Selection) |
| In addition, our approach reduces feature distillation to only 4.1 seconds and improves memory efficiency by up to 64×, while supporting fast inference at ... | p. 7 (4.3. 3D Semantic Segmentation) |
| Most of the computation lies in evaluating Gaussian contributions to the 2D masks, which is inherently required, while the remaining steps add only negligible ... | p. 8 (4.4. Ablation Study) |
| The pipeline begins by extracting 2D object masks and their corresponding CLIP features from multi-view images us- "curtain" Text CLIP Cluster ID Field Feature ... | p. 3 (3.1. Overview) |
| To assign semantics only to Gaussians that significantly contribute to the rendered image, we compute their pixel-wise contributions using alphablending weights from the rendering ... | p. 4 (3.3. Indexed Feature Injection) |
| It is computed by accumulating the occlusion effects from all preceding Gaussians along the same ray: T (l) n (u, v) = n-1 Y ... | p. 4 (3.3. Indexed Feature Injection) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.4. Ablation Study - extractive body cue:** Removing semantic-aware clustering decreases performance by over 50%, as the model cannot identify semantically corresponding masks across views for merging.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** Since Dr.Splat does not provide inference code, we adopt the reported inference results from its paper and measure all other results ourselves.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** For robustness evaluation beyond limited indoor environments, we introduce the DL3DV-OVS dataset.
- **p. 6 / 4.2. 3D Object Selection - extractive body cue:** Such results highlight the flexibility and robustness of our method across diverse object scales and scene complexities.
- **p. 6 / 4.2. 3D Object Selection - extractive body cue:** Our method shows robust performance on the road scene with multiple distant cars and the office scene with repeated objects such as chairs and monitors.
- **p. 7 / 4.3. 3D Semantic Segmentation - extractive body cue:** Since these methods use semantics at the level of individual Gaussians, they fail to form mean19818

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Experimental Setup), p. 8 (4.3. 3D Semantic Segmentation), p. 5 (4.1. Experimental Setup), p. 6 (4.2. 3D Object Selection), p. 6 (4.2. 3D Object Selection), p. 7 (4.3. 3D Semantic Segmentation), metrics p. 1 (Figure/Table caption), p. 8 (4.3. 3D Semantic Segmentation), p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.3. 3D Semantic Segmentation), p. 6 (4.2. 3D Object Selection), baselines p. 3 (Figure/Table caption), p. 8 (4.3. 3D Semantic Segmentation), p. 5 (4.2. 3D Object Selection), p. 5 (4.1. Experimental Setup), p. 6 (4.2. 3D Object Selection), p. 6 (4.2. 3D Object Selection), results p. 7 (4.3. 3D Semantic Segmentation), p. 1 (Figure/Table caption), p. 5 (4.2. 3D Object Selection), p. 5 (4.2. 3D Object Selection), p. 6 (4.3. 3D Semantic Segmentation), p. 6 (4.2. 3D Object Selection).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
