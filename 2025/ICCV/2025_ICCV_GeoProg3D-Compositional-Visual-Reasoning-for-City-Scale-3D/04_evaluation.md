# Evaluation - GeoProg3D: Compositional Visual Reasoning for City-Scale 3D Language Fields

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Yasuki_GeoProg3D_Compositional_Visual_Reasoning_for_City-Scale_3D_Language_Fields_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.2. Experimental results), p. 7 (5.2. Experimental results), p. 5 (Figure/Table caption), p. 8 (5.2. Experimental results), p. 8 (5.2. Experimental results), p. 1 (Figure/Table caption)): GeoProg3D further improved accuracy on both GoolgeEarth and UrbanScene3D.

## Evaluation Body Digest

- **p. 6 / 4. GeoEval3D Dataset - extractive body cue:** The dataset B = {(Di, Qi)}S i=1 consists of pairs multi-view image sets Di and task sets Qi, where S is the number of outdoor ...
- **p. 6 / 4. GeoEval3D Dataset - extractive body cue:** In this section, we present five tasks for evaluating understanding of city-scale 3D scenes, and introduce GeoEval3D, a dataset covering these tasks.
- **p. 7 / 5.1. Evaluation metrics - extractive body cue:** We perform experiments on five scenes across the two datasets: four scenes from GoogleEarth and one scene from UrbanScene3D.
- **p. 7 / 5.2. Experimental results - extractive body cue:** In addition, LangSplat caused a memory error with UrbanScene3D in our setting, which implies the efficiency of the tree structure for learning larger scenes [40].
- **p. 8 / 5.2. Experimental results - extractive body cue:** This shows the vital role of segmentation for landmark objects.
- **p. 8 / 5.2. Experimental results - extractive body cue:** The omission of SegAround impairs performance particularly in the SPR task.
- **p. 7 / 5.1. Evaluation metrics - extractive body cue:** Localization accuracy is measured at an IoU threshold of 0.15.
- **p. 7 / 5.1. Evaluation metrics - extractive body cue:** For the GRD task, we report localization accuracy for object localization and Intersection over Union (IoU) for segmentation following the previous study [53].

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. GeoEval3D Dataset (p. 6); 4.3. Dataset construction and statistics (p. 6); 5. Experiments (p. 7); 5.1. Evaluation metrics (p. 7); 5.2. Experimental results (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Experimental results | EMPIRICAL / SOURCE-REPORTED EVALUATION | GeoProg3D further improved accuracy on both GoolgeEarth and UrbanScene3D. | p. 7 (5.2. Experimental results) |
| 5.2. Experimental results | EMPIRICAL / SOURCE-REPORTED EVALUATION | These results underscore the superior performance of GeoProg3D in estimating quantities within large-scale 3D scenes and highlight the effectiveness of the program-based inference procedures. | p. 7 (5.2. Experimental results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 6. ICE and instruction prompt. form height by identifying horizontal planes from Gaussian variance directions, while 6) applies clustering to filter out noisy ... | p. 5 (Figure/Table caption) |
| 5.2. Experimental results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Lastly, omitting the LargestSeg module affected the CMP performance, reducing the score to 44.74. | p. 8 (5.2. Experimental results) |
| 5.2. Experimental results | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results in Table 7 show the significance of each component in maximizing the model's performance. | p. 8 (5.2. Experimental results) |

## Dataset / Benchmark Role

- **p. 6 / 4. GeoEval3D Dataset - extractive body cue:** The dataset B = {(Di, Qi)}S i=1 consists of pairs multi-view image sets Di and task sets Qi, where S is the number of outdoor ...
- **p. 6 / 4. GeoEval3D Dataset - extractive body cue:** In this section, we present five tasks for evaluating understanding of city-scale 3D scenes, and introduce GeoEval3D, a dataset covering these tasks.
- **p. 7 / 5.1. Evaluation metrics - extractive body cue:** We perform experiments on five scenes across the two datasets: four scenes from GoogleEarth and one scene from UrbanScene3D.
- **p. 7 / 5.2. Experimental results - extractive body cue:** In addition, LangSplat caused a memory error with UrbanScene3D in our setting, which implies the efficiency of the tree structure for learning larger scenes [40].
- **p. 8 / 5.2. Experimental results - extractive body cue:** This shows the vital role of segmentation for landmark objects.
- **p. 8 / 5.2. Experimental results - extractive body cue:** The omission of SegAround impairs performance particularly in the SPR task.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Overview of the proposed compositional geographic reasoning task. This task enables natural language interaction with city-scale 3D scenes, supporting diverse geographic reasoning scenarios. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Framework overview. Given a user query, GeoProg3D generates a visual program via LLM in-context learning. The program operates GCLF by combining Geographical Vision ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. GCLF structure. (a) Coarse-to-fine tree structure to represent 3D scenes. Each node represents a pair of a 3D Gaussian and a language embedding. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1. Number of Gaussians and inference speed. Geo-visual integration. To effectively integratevisual and geographic data, we train our language embeddings to align with CLIP ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. The results of object detection using GroundingDINO. Training. Given a set of multi-view images D = {xi}N i=1 for training, a GCLF is ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. Execution example. (a) Program code generated from the query "Red-letter billboard within 100 meters of The View." that consists of three steps. (b) ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6. ICE and instruction prompt. form height by identifying horizontal planes from Gaussian variance directions, while 6) applies clustering to filter out noisy activations ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. How to call the nine functions of the GV-APIs and their roles. Task Query examples GRD U-shaped building to the west of Liberty ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset B = {(Di, Qi)}S i=1 consists of pairs multi-view image sets Di and task sets Qi, where S is the number of ... | embodiment, simulator version and control stack | p. 6 (4. GeoEval3D Dataset), p. 6 (4. GeoEval3D Dataset) |
| Task/environment | In this section, we present five tasks for evaluating understanding of city-scale 3D scenes, and introduce GeoEval3D, a dataset covering these tasks. | reset, timeout, object/scene variation | p. 6 (4. GeoEval3D Dataset), p. 7 (5.1. Evaluation metrics) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 6 (4.3. Dataset construction and statistics) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Localization accuracy is measured at an IoU threshold of 0.15. | definition/direction/unit from same section | p. 7 (5.1. Evaluation metrics) |
| For the GRD task, we report localization accuracy for object localization and Intersection over Union (IoU) for segmentation following the previous study [53]. | definition/direction/unit from same section | p. 7 (5.1. Evaluation metrics) |
| Lastly, omitting the LargestSeg module affected the CMP performance, reducing the score to 44.74. | definition/direction/unit from same section | p. 8 (5.2. Experimental results) |
| Specifically, the CNT and MES tasks are not included in the experiment because they cannot be evaluated by accuracy rate, and the dedicated modules ... | definition/direction/unit from same section | p. 8 (5.2. Experimental results) |
| Figure 6. ICE and instruction prompt. form height by identifying horizontal planes from Gaussian variance directions, while 6) applies clustering to filter out noisy ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Figure 5. Execution example. (a) Program code generated from the query "Red-letter billboard within 100 meters of The View." that consists of three steps. ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Given a query qk describing a question, this task requires models to accurately measure the height (MES-H) and distance (MES-D) of buildings. | definition/direction/unit from same section | p. 6 (4.1. Task Definition) |
| Figure 1. Overview of the proposed compositional geographic reasoning task. This task enables natural language interaction with city-scale 3D scenes, supporting diverse geographic reasoning ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We observed that GCLF outperforms baselines on GoogleEarth. | comparison identity and matched condition | p. 7 (5.2. Experimental results) |
| We compare our methods with baselines, including LangSplat [53], which is the SOTA method for high-resolution 3D scene localization. | comparison identity and matched condition | p. 7 (5.2. Experimental results) |
| Note that these comparison VLN-based baselines do not support pixel-level inference, so the GRD task is not evaluated. | comparison identity and matched condition | p. 8 (5.2. Experimental results) |
| It is scaled up more than 10 times compared to the datasets used in previous works, and contains many more words [26, 53] (Appendix ... | comparison identity and matched condition | p. 6 (4.3. Dataset construction and statistics) |
| See appendix B for more ablation studies. | comparison identity and matched condition | p. 8 (5.2. Experimental results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To assess the impact of each component of GeoProg3D, we conducted an ablation study to investigate the three tasks of GoogleEarth's GRD, SPR, and ... | component/input/data sensitivity | p. 8 (5.2. Experimental results) |
| See appendix B for more ablation studies. | component/input/data sensitivity | p. 8 (5.2. Experimental results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions are threefold: • We propose GeoProg3D, a framework for compositional reasoning over city-scale 3D language fields, where visual programming can ... | GeoProg3D further improved accuracy on both GoolgeEarth and UrbanScene3D. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.2. Experimental results), p. 7 (5.2. Experimental results), p. 5 (Figure/Table caption), p. 8 (5.2. Experimental results), p. 8 (5.2. Experimental results), p. 1 (Figure/Table caption) |
| Primary metric/result | These results underscore the superior performance of GeoProg3D in estimating quantities within large-scale 3D scenes and highlight the effectiveness of the program-based inference procedures. | numeric claim only at cited anchor | p. 7 (5.2. Experimental results) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 7. Qualitative results and failure cases. The Ground Truth region for the GRD task is delineated by the yellow frame. localization that is ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Ablation study of different Geographical Vision APIs. itative examples and failure cases. | p. 8 (5.2. Experimental results) |
| body limitation/failure cue | Note that MES-H and CMP are not evaluated in UrbanScene3D because Ground Truth for height cannot be obtained. | p. 7 (5.1. Evaluation metrics) |
| body limitation/failure cue | These results demonstrate the limitations of localization using 3D language fields alone in 3D urban scenes and the effectiveness of GV-APIs and visual programming ... | p. 7 (5.2. Experimental results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For the SPR and CMP tasks, exact match criteria are applied to determine correctness to compute accuracy. | p. 7 (5.1. Evaluation metrics) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7. Qualitative results and failure cases. The Ground Truth region for the GRD task is delineated by the yellow frame. localization that is independent ...
- **p. 8 / 5.2. Experimental results - extractive body cue:** Ablation study of different Geographical Vision APIs. itative examples and failure cases.
- **p. 7 / 5.1. Evaluation metrics - extractive body cue:** Note that MES-H and CMP are not evaluated in UrbanScene3D because Ground Truth for height cannot be obtained.
- **p. 7 / 5.2. Experimental results - extractive body cue:** These results demonstrate the limitations of localization using 3D language fields alone in 3D urban scenes and the effectiveness of GV-APIs and visual programming in ...

- **Evidence anchors reviewed:** datasets p. 6 (4. GeoEval3D Dataset), p. 6 (4. GeoEval3D Dataset), p. 7 (5.1. Evaluation metrics), p. 7 (5.2. Experimental results), p. 8 (5.2. Experimental results), p. 8 (5.2. Experimental results), metrics p. 7 (5.1. Evaluation metrics), p. 7 (5.1. Evaluation metrics), p. 8 (5.2. Experimental results), p. 8 (5.2. Experimental results), p. 5 (Figure/Table caption), p. 5 (Figure/Table caption), baselines p. 7 (5.2. Experimental results), p. 7 (5.2. Experimental results), p. 8 (5.2. Experimental results), p. 6 (4.3. Dataset construction and statistics), p. 8 (5.2. Experimental results), results p. 7 (5.2. Experimental results), p. 7 (5.2. Experimental results), p. 5 (Figure/Table caption), p. 8 (5.2. Experimental results), p. 8 (5.2. Experimental results), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
