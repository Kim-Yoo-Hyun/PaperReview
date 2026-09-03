# Evaluation - RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Song_RoboSpatial_Teaching_Spatial_Understanding_to_2D_and_3D_Vision-Language_Models_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Song_RoboSpatial_Teaching_Spatial_Understanding_to_2D_and_3D_Vision-Language_Models_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 2 (Dataset), p. 8 (4.3. Real Robot Experiments), p. 6 (4.1.3. Cross-Dataset Generalization Evaluation), p. 8 (4.2. Results), p. 6 (Figure/Table caption), p. 2 (Dataset)): Results demonstrate that models trained on ROBOSPATIAL exhibit significantly improved spatial reasoning capabilities, consistently outperforming baseline methods on the evaluation benchmark ROBOSPATIAL-Val, a held-out validation subset ...

## Evaluation Body Digest

- **p. 3 / Dataset - extractive body cue:** We make the data and code for generating the dataset from 3D annotated scenes publicly available1. • VLMs trained on ROBOSPATIAL demonstrate superior spatial reasoning, ...
- **p. 2 / Dataset - extractive body cue:** Applying our methodology to existing indoor scene and tabletop datasets, we generate both a comprehensive training dataset and a benchmark for spatial question answering in ...
- **p. 2 / Dataset - extractive body cue:** These benchmarks rigorously test spatial reasoning skills in practical robotic tasks, including object rearrangement and contextual question answering in indoor environments, while also examining the ...
- **p. 5 / 4.1. Setup - extractive body cue:** We retrieve 3D bounding box annotations and embodied images from EmbodiedScan [58], and generate a large-scale spatial reasoning dataset covering Dataset Type Splits Images QA ...
- **p. 3 / Dataset - extractive body cue:** Our contributions are threefold: • A new training dataset, ROBOSPATIAL, comprising images and 3D scans paired with spatial questions and answers, accompanied by an evaluation ...
- **p. 6 / 4.1.4. Out-of-Domain Evaluation - extractive body cue:** ROBOSPATIAL-Home contains 350 manually written spatial questions over diverse real-world RGBD scenes captured with an iPhone equipped with a depth sensor.
- **p. 4 / 3.2. Dataset Generation - extractive body cue:** The pipeline takes as input a scene dataset Ds that contains RGB images, camera poses (both extrinsic and intrinsic parameters), and oriented 3D bounding box ...
- **p. 5 / 4.1. Setup - extractive body cue:** Detailed data statistics are in the Appendix. diverse indoor environments: larger scenes for navigation and smaller object-centric setups for manipulation.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** Dataset (p. 2); 3.2. Dataset Generation (p. 4); 4. Experiments (p. 5); 4.1.2. Spatial Understanding Evaluation (p. 5); 4.1.3. Cross-Dataset Generalization Evaluation (p. 6); 4.1.4. Out-of-Domain Evaluation (p. 6); 4.2. Results (p. 7); 4.3. Real Robot Experiments (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Dataset | EMPIRICAL / REAL-ROBOT OR HARDWARE | Results demonstrate that models trained on ROBOSPATIAL exhibit significantly improved spatial reasoning capabilities, consistently outperforming baseline methods on the evaluation benchmark ROBOSPATIAL-Val, a held-out ... | p. 2 (Dataset) |
| 4.3. Real Robot Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Experiments show that LLaVA-NeXT fine-tuned on ROBOSPATIAL achieves the highest success rate across all models. | p. 8 (4.3. Real Robot Experiments) |
| 4.1.3. Cross-Dataset Generalization Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Despite differing object distributions and scene layouts, we observe a positive synergy between indoor and tabletop environments: training on one environment type improves spatial ... | p. 6 (4.1.3. Cross-Dataset Generalization Evaluation) |
| 4.2. Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | 3 suggest that 3D VLMs tend to outperform 2D counterparts in spatial reasoning tasks, likely due to their ability to directly utilize depth information. | p. 8 (4.2. Results) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4. Results on an out-of-domain test split comparing prior art VLMs. The results show improved (") spatial understanding capabilities on similar domains. Bolded ... | p. 6 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 3 / Dataset - extractive body cue:** We make the data and code for generating the dataset from 3D annotated scenes publicly available1. • VLMs trained on ROBOSPATIAL demonstrate superior spatial reasoning, ...
- **p. 2 / Dataset - extractive body cue:** Applying our methodology to existing indoor scene and tabletop datasets, we generate both a comprehensive training dataset and a benchmark for spatial question answering in ...
- **p. 2 / Dataset - extractive body cue:** These benchmarks rigorously test spatial reasoning skills in practical robotic tasks, including object rearrangement and contextual question answering in indoor environments, while also examining the ...
- **p. 5 / 4.1. Setup - extractive body cue:** We retrieve 3D bounding box annotations and embodied images from EmbodiedScan [58], and generate a large-scale spatial reasoning dataset covering Dataset Type Splits Images QA ...
- **p. 3 / Dataset - extractive body cue:** Our contributions are threefold: • A new training dataset, ROBOSPATIAL, comprising images and 3D scans paired with spatial questions and answers, accompanied by an evaluation ...
- **p. 6 / 4.1.4. Out-of-Domain Evaluation - extractive body cue:** ROBOSPATIAL-Home contains 350 manually written spatial questions over diverse real-world RGBD scenes captured with an iPhone equipped with a depth sensor.
- **p. 4 / 3.2. Dataset Generation - extractive body cue:** The pipeline takes as input a scene dataset Ds that contains RGB images, camera poses (both extrinsic and intrinsic parameters), and oriented 3D bounding box ...
- **p. 5 / 4.1. Setup - extractive body cue:** Detailed data statistics are in the Appendix. diverse indoor environments: larger scenes for navigation and smaller object-centric setups for manipulation.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. ROBOSPATIAL dataset facilitates 3D spatial reason- ing for robotic manipulation. This illustration demonstrates how a model trained on ROBOSPATIAL enables human-aligned spa- tial ...
- **p. 2 / Figure/Table caption - extractive body cue:** Table 1. Comparison with other spatial reasoning datasets that include object-centric spatial relationships. action. Several recent efforts aim to address this by explic- itly training ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. This paper hypothesizes that a primary bottleneck lim- iting the effectiveness of VLMs in robotics is the scarcity of suitable training data, as ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the ROBOSPATIAL dataset. We auto- matically generate spatial relationship annotations from existing datasets with 3D point clouds, egocentric images, and 3D ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Dataset splits for indoor and tabletop dataset. Detailed data statistics are in the Appendix. diverse indoor environments: larger scenes for navigation and smaller ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Results of existing 2D/3D VLMs on a held-out validation split (ROBOSPATIAL-Val) of images and scans. All methods, for all tasks, perform better (") ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 4. Results on an out-of-domain test split comparing prior art VLMs. The results show improved (") spatial understanding capabilities on similar domains. Bolded number ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. In-domain (ROBOSPATIAL-Val, top) and out-of-domain (ROBOSPATIAL-Home, BLINK [15], middle and bottom) results for ROBOSPATIAL-trained models. Two models shown: SL (SpaceLLaVA [5]) and RP ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We make the data and code for generating the dataset from 3D annotated scenes publicly available1. • VLMs trained on ROBOSPATIAL demonstrate superior spatial ... | embodiment, simulator version and control stack | p. 3 (Dataset), p. 2 (Dataset) |
| Task/environment | Applying our methodology to existing indoor scene and tabletop datasets, we generate both a comprehensive training dataset and a benchmark for spatial question answering ... | reset, timeout, object/scene variation | p. 2 (Dataset), p. 2 (Dataset) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.2. Dataset Generation), p. 4 (3.2. Dataset Generation) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 5 (3.2.3. Question-Answer Generation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Experiments show that LLaVA-NeXT fine-tuned on ROBOSPATIAL achieves the highest success rate across all models. | definition/direction/unit from same section | p. 8 (4.3. Real Robot Experiments) |
| For yes/no questions, we report accuracy. | definition/direction/unit from same section | p. 5 (4.1.2. Spatial Understanding Evaluation) |
| We also observe that spatial failures in 2D VLMs often stem from errors in projecting 2D predictions into 3D. | definition/direction/unit from same section | p. 8 (4.3. Real Robot Experiments) |
| The goal of the data construction pipeline is to generate a large-scale, high-accuracy spatial relationship dataset with minimal human intervention, using automatic heuristics grounded ... | definition/direction/unit from same section | p. 4 (3.2. Dataset Generation) |
| This auxiliary dataset does not contribute to spatial reasoning performance. | definition/direction/unit from same section | p. 5 (4.1. Setup) |
| We curated this benchmark to evaluate generalization to novel indoor settings with previously unseen objects. | definition/direction/unit from same section | p. 6 (4.1.4. Out-of-Domain Evaluation) |
| Although ROBOSPATIAL consists of template-generated QA pairs with a fixed set of spatial prepositions, we observe in Tab. | definition/direction/unit from same section | p. 7 (4.2. Results) |
| These rely on the 3D bounding box layout and calibrated camera parameters to map spatial relationships into image coordinates. | definition/direction/unit from same section | p. 4 (3.2. Dataset Generation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We evaluate the following VLMs: LLaVA-NeXT [35] and RoboPoint [62], both with and without ROBOSPATIAL training; and two strong baselines, Molmo [9] and GPT-4o ... | comparison identity and matched condition | p. 8 (4.3. Real Robot Experiments) |
| We make the data and code for generating the dataset from 3D annotated scenes publicly available1. • VLMs trained on ROBOSPATIAL demonstrate superior spatial ... | comparison identity and matched condition | p. 3 (Dataset) |
| Across all benchmarks, models trained on ROBOSPATIAL consistently outperformed baseline methods, demonstrating the broad utility of the dataset. | comparison identity and matched condition | p. 2 (Dataset) |
| Results demonstrate that models trained on ROBOSPATIAL exhibit significantly improved spatial reasoning capabilities, consistently outperforming baseline methods on the evaluation benchmark ROBOSPATIAL-Val, a held-out ... | comparison identity and matched condition | p. 2 (Dataset) |
| We also include GPT-4o [42] as a closedsource baseline. | comparison identity and matched condition | p. 5 (4.1. Setup) |
| 3 suggest that 3D VLMs tend to outperform 2D counterparts in spatial reasoning tasks, likely due to their ability to directly utilize depth information. | comparison identity and matched condition | p. 8 (4.2. Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| (See Appendix for ablation experiments.) | component/input/data sensitivity | p. 5 (4.1. Setup) |
| We evaluate the following VLMs: LLaVA-NeXT [35] and RoboPoint [62], both with and without ROBOSPATIAL training; and two strong baselines, Molmo [9] and GPT-4o ... | component/input/data sensitivity | p. 8 (4.3. Real Robot Experiments) |
| It also demonstrates sensitivity to object scale, as in the task "place in front of the orange juice box," where the model places the ... | component/input/data sensitivity | p. 8 (4.3. Real Robot Experiments) |
| However, these models lack understanding of real-world constraints, such as inferring object-centric reference frames for perspectiveinvariant reasoning, or accounting for the space required to ... | component/input/data sensitivity | p. 2 (Dataset) |
| We evaluate models in both zero-shot and fine-tuned settings, using ROBOSPATIAL to fine-tune opensource models. | component/input/data sensitivity | p. 5 (4.1. Setup) |
| Two models shown: SL (SpaceLLaVA [5]) and RP (RoboPoint [62]); the -FT suffix indicates fine-tuning on ROBOSPATIAL. | component/input/data sensitivity | p. 7 (4.1.4. Out-of-Domain Evaluation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The output is a spatial reasoning dataset D, where each entry di = hIi, qi, ai, lii consists of an image Ii, a question ... | Results demonstrate that models trained on ROBOSPATIAL exhibit significantly improved spatial reasoning capabilities, consistently outperforming baseline methods on the evaluation benchmark ROBOSPATIAL-Val, a held-out ... | PDF body cue; verify exact table/figure and matched conditions | p. 2 (Dataset), p. 8 (4.3. Real Robot Experiments), p. 6 (4.1.3. Cross-Dataset Generalization Evaluation), p. 8 (4.2. Results), p. 6 (Figure/Table caption), p. 2 (Dataset) |
| Primary metric/result | Experiments show that LLaVA-NeXT fine-tuned on ROBOSPATIAL achieves the highest success rate across all models. | numeric claim only at cited anchor | p. 8 (4.3. Real Robot Experiments) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Setup - extractive body cue:** We retrieve 3D bounding box annotations and embodied images from EmbodiedScan [58], and generate a large-scale spatial reasoning dataset covering Dataset Type Splits Images QA ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | To mitigate failure cases arising from poor object grounding, we also include an auxiliary grounding dataset during training, which provides additional supervision for object ... | p. 5 (4.1. Setup) |
| body limitation/failure cue | We also observe that spatial failures in 2D VLMs often stem from errors in projecting 2D predictions into 3D. | p. 8 (4.3. Real Robot Experiments) |
| body limitation/failure cue | Nonetheless, models trained on ROBOSPATIAL produce more accurate predictions, reducing these failure cases and showing the benefit of dataset-driven improvements. | p. 8 (4.3. Real Robot Experiments) |
| body limitation/failure cue | Several recent efforts aim to address this by explicitly training VLMs on spatial reasoning tasks, yet many fall short of the demands posed by ... | p. 2 (Dataset) |
| body limitation/failure cue | Questions fall into two categories: binary yes/no questions and coordinate prediction tasks. | p. 5 (4.1.2. Spatial Understanding Evaluation) |
| body limitation/failure cue | Although the method does not require point clouds or meshes, it relies on camera intrinsics and extrinsics to project between 2D and 3D and ... | p. 4 (3.2. Dataset Generation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We make the data and code for generating the dataset from 3D annotated scenes publicly available1. • VLMs trained on ROBOSPATIAL demonstrate superior spatial ... | p. 3 (Dataset) |
| We use oriented 3D bounding boxes, provided by the source dataset, to compute spatial relationships. | p. 4 (3.2. Dataset Generation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 4.1. Setup - extractive body cue:** To mitigate failure cases arising from poor object grounding, we also include an auxiliary grounding dataset during training, which provides additional supervision for object reference ...
- **p. 8 / 4.3. Real Robot Experiments - extractive body cue:** We also observe that spatial failures in 2D VLMs often stem from errors in projecting 2D predictions into 3D.
- **p. 8 / 4.3. Real Robot Experiments - extractive body cue:** Nonetheless, models trained on ROBOSPATIAL produce more accurate predictions, reducing these failure cases and showing the benefit of dataset-driven improvements.
- **p. 2 / Dataset - extractive body cue:** Several recent efforts aim to address this by explicitly training VLMs on spatial reasoning tasks, yet many fall short of the demands posed by embodied ...
- **p. 5 / 4.1.2. Spatial Understanding Evaluation - extractive body cue:** Questions fall into two categories: binary yes/no questions and coordinate prediction tasks.
- **p. 4 / 3.2. Dataset Generation - extractive body cue:** Although the method does not require point clouds or meshes, it relies on camera intrinsics and extrinsics to project between 2D and 3D and to ...

- **Evidence anchors reviewed:** datasets p. 3 (Dataset), p. 2 (Dataset), p. 2 (Dataset), p. 5 (4.1. Setup), p. 3 (Dataset), p. 6 (4.1.4. Out-of-Domain Evaluation), metrics p. 8 (4.3. Real Robot Experiments), p. 5 (4.1.2. Spatial Understanding Evaluation), p. 8 (4.3. Real Robot Experiments), p. 4 (3.2. Dataset Generation), p. 5 (4.1. Setup), p. 6 (4.1.4. Out-of-Domain Evaluation), baselines p. 8 (4.3. Real Robot Experiments), p. 3 (Dataset), p. 2 (Dataset), p. 2 (Dataset), p. 5 (4.1. Setup), p. 8 (4.2. Results), results p. 2 (Dataset), p. 8 (4.3. Real Robot Experiments), p. 6 (4.1.3. Cross-Dataset Generalization Evaluation), p. 8 (4.2. Results), p. 6 (Figure/Table caption), p. 2 (Dataset).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Results demonstrate that models trained on ROBOSPATIAL exhibit significantly improved spatial reasoning capabilities, consistently outperforming baseline methods on the evaluation benchmark ROBOSPATIAL-Val, a held-out validation subset ... (p. 2, Dataset).
- **Metric evidence:** For yes/no questions, we report accuracy. (p. 5, 4.1.2. Spatial Understanding Evaluation).
- **Baseline/ablation evidence:** We evaluate the following VLMs: LLaVA-NeXT [35] and RoboPoint [62], both with and without ROBOSPATIAL training; and two strong baselines, Molmo [9] and GPT-4o [42]. (p. 8, 4.3. Real Robot Experiments).
- **Failure/negative evidence:** To mitigate failure cases arising from poor object grounding, we also include an auxiliary grounding dataset during training, which provides additional supervision for object reference resolution. (p. 5, 4.1. Setup).
