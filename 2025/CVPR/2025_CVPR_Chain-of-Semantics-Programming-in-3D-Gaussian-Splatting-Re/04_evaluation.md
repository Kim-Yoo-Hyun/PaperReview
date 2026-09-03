# Evaluation - Chain of Semantics Programming in 3D Gaussian Splatting Representation for 3D Vision Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.4. Ablation study), p. 5 (4.3. Comparison to Prior Works), p. 5 (4.3. Comparison to Prior Works), p. 6 (4.4. Ablation study), p. 7 (4.4. Ablation study), p. 8 (4.4. Ablation study)): This mechanism achieves improvements of 4.5% on Nr3D and 1.8% on Sr3D.

## Evaluation Body Digest

- **p. 5 / 4.1. Datasets - extractive body cue:** Sr3D comprises 83.5K template-based utterances that leverage spatial relationships among fine-grained object classes to localize a referred object in a scene, and Nr3D includes 41.5K ...
- **p. 7 / 4.4. Ablation study - extractive body cue:** Programming improves object grounding by 10.11% on the Nr3D dataset and 20.42% on the Sr3D dataset, demonstrating its beneficial impact.
- **p. 7 / 4.4. Ablation study - extractive body cue:** In the context of object grounding through programming, the Chain of Semantics yields beneficial improvements across both datasets, particularly on Sr3D, where the gap between ...
- **p. 5 / 4.3. Comparison to Prior Works - extractive body cue:** We compare our method with previous works on the Nr3D and Sr3D datasets.
- **p. 6 / 4.4. Ablation study - extractive body cue:** Performance comparison of our method and prior data efficient supervised model, with 5%, 15%, 25% train data on Nr3D dataset.
- **p. 6 / 4.4. Ablation study - extractive body cue:** On the Sr3D dataset, there is a decrease of 4.0% relative to dialogue; however, it shows an increase of 1.3% when compared to programming.
- **p. 8 / 4.4. Ablation study - extractive body cue:** Ablation study of LLM/VLM on Nr3D dataset.
- **p. 8 / 4.5. Qualitative results - extractive body cue:** In Figure 5, we visualize examples of scenes reconstructed with 3DGS.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Datasets (p. 5); 4.2. Evaluation Configuration (p. 5); 4.5. Qualitative results (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.4. Ablation study | EMPIRICAL / SOURCE-REPORTED EVALUATION | This mechanism achieves improvements of 4.5% on Nr3D and 1.8% on Sr3D. | p. 7 (4.4. Ablation study) |
| 4.3. Comparison to Prior Works | EMPIRICAL / SOURCE-REPORTED EVALUATION | Achieve zero-shot state-of-the-art grounding performance. | p. 5 (4.3. Comparison to Prior Works) |
| 4.3. Comparison to Prior Works | EMPIRICAL / SOURCE-REPORTED EVALUATION | In Table 2, we find that our method outperforms the current state-of-the-art zeroshot methods on the Nr3D dataset and approaches the performance of the ... | p. 5 (4.3. Comparison to Prior Works) |
| 4.4. Ablation study | EMPIRICAL / SOURCE-REPORTED EVALUATION | Utilizing only the Chain of Semantics on the Nr3D dataset results in an improvement of 2.2% compared to dialogue and 1.9% compared to programming. | p. 6 (4.4. Ablation study) |
| 4.4. Ablation study | EMPIRICAL / SOURCE-REPORTED EVALUATION | The introduction of 3DGS enhances grounding accuracy in both datasets, with improvements of 1.2% on Nr3D and 3.5% on Sr3D. | p. 7 (4.4. Ablation study) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Datasets - extractive body cue:** Sr3D comprises 83.5K template-based utterances that leverage spatial relationships among fine-grained object classes to localize a referred object in a scene, and Nr3D includes 41.5K ...
- **p. 7 / 4.4. Ablation study - extractive body cue:** Programming improves object grounding by 10.11% on the Nr3D dataset and 20.42% on the Sr3D dataset, demonstrating its beneficial impact.
- **p. 7 / 4.4. Ablation study - extractive body cue:** In the context of object grounding through programming, the Chain of Semantics yields beneficial improvements across both datasets, particularly on Sr3D, where the gap between ...
- **p. 5 / 4.3. Comparison to Prior Works - extractive body cue:** We compare our method with previous works on the Nr3D and Sr3D datasets.
- **p. 6 / 4.4. Ablation study - extractive body cue:** Performance comparison of our method and prior data efficient supervised model, with 5%, 15%, 25% train data on Nr3D dataset.
- **p. 6 / 4.4. Ablation study - extractive body cue:** On the Sr3D dataset, there is a decrease of 4.0% relative to dialogue; however, it shows an increase of 1.3% when compared to programming.
- **p. 8 / 4.4. Ablation study - extractive body cue:** Ablation study of LLM/VLM on Nr3D dataset.
- **p. 8 / 4.5. Qualitative results - extractive body cue:** In Figure 5, we visualize examples of scenes reconstructed with 3DGS.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Our proposed zero-shot framework enables interaction and retrieval within a 3D Gaussian Splatting representation to ob- tain fine-grained semantics and supports multi-step spatial ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The pipeline for grounding an object is as follows: (a), parse the semantics of the utterance into a chain of semantics and a ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Comparison of Nr3D and Sr3D datasets. our framework to understand text and images and perform reasoning. This framework is generalizable and applicable to ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Comparison of our zero-shot method with data- efficiency supervised model. Compared to data-efficiency models with limited data. Moreover, some advanced supervised methods demonstrate ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Grounding performance on Nr3D. Our method surpasses existing zero-shot methods and approaches the performance of recent supervised models. †employs a grounded-aware self-check mechanism. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Grounding performance on Sr3D. Our method surpasses recent supervised models. †employs a grounded-aware self-check mechanism. Train Data
- **p. 6 / Figure/Table caption - extractive body cue:** Table 4. Performance comparison of our method and prior data ef- ficient supervised model, with 0.5%, 5%, 10% train data on Sr3D
- **p. 6 / Figure/Table caption - extractive body cue:** Table 5. Performance comparison of our method and prior data efficient supervised model, with 5%, 15%, 25% train data on Nr3D

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Sr3D comprises 83.5K template-based utterances that leverage spatial relationships among fine-grained object classes to localize a referred object in a scene, and Nr3D includes ... | embodiment, simulator version and control stack | p. 5 (4.1. Datasets), p. 7 (4.4. Ablation study) |
| Task/environment | Programming improves object grounding by 10.11% on the Nr3D dataset and 20.42% on the Sr3D dataset, demonstrating its beneficial impact. | reset, timeout, object/scene variation | p. 7 (4.4. Ablation study), p. 7 (4.4. Ablation study) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.2. Dynamic Interaction in 3DGS Representation), p. 3 (3.2. Dynamic Interaction in 3DGS Representation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The introduction of this mechanism enhances the accuracy of the generated code and deepens the reasoning regarding spatial relationships 24566 | definition/direction/unit from same section | p. 7 (4.4. Ablation study) |
| The object grounding accuracy results from the ablation study of Nr3D and Sr3D are shown in Table 6 and Table 7, respectively. | definition/direction/unit from same section | p. 6 (4.4. Ablation study) |
| This underscores the importance of incorporating viewpointrelated fine-grained semantics. | definition/direction/unit from same section | p. 7 (4.4. Ablation study) |
| Moreover, some advanced supervised methods demonstrate superior data efficiency, maintaining good grounding performance even with less train data. | definition/direction/unit from same section | p. 5 (4.3. Comparison to Prior Works) |
| Especially on the easy and view-independent samples, different LLMs demonstrate similar performance. | definition/direction/unit from same section | p. 8 (4.4. Ablation study) |
| Figure 1. Our proposed zero-shot framework enables interaction and retrieval within a 3D Gaussian Splatting representation to ob- tain fine-grained semantics and supports multi-step ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Achieve zero-shot state-of-the-art grounding performance. | definition/direction/unit from same section | p. 5 (4.3. Comparison to Prior Works) |
| Performance comparison of our method and prior data efficient supervised model, with 5%, 15%, 25% train data on Nr3D dataset. | definition/direction/unit from same section | p. 6 (4.4. Ablation study) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| With limited train data for the supervised models, our zero-shot method outperforms all compared models in both two datasets, as shown in Figure 3. | comparison identity and matched condition | p. 5 (4.3. Comparison to Prior Works) |
| In Table 2, we find that our method outperforms the current state-of-the-art zeroshot methods on the Nr3D dataset and approaches the performance of the ... | comparison identity and matched condition | p. 5 (4.3. Comparison to Prior Works) |
| However, in Sr3D, the view-dependent grounding accuracy decreases by 12.8% (without Chain of Semantics) and 15.6% (with Chain of Semantics) compared to dialogue. | comparison identity and matched condition | p. 7 (4.4. Ablation study) |
| On the Sr3D dataset, there is a decrease of 4.0% relative to dialogue; however, it shows an increase of 1.3% when compared to programming. | comparison identity and matched condition | p. 6 (4.4. Ablation study) |
| Utilizing only the Chain of Semantics on the Nr3D dataset results in an improvement of 2.2% compared to dialogue and 1.9% compared to programming. | comparison identity and matched condition | p. 6 (4.4. Ablation study) |
| The scenes reconstructed with 3DGS possess richer details compared to the meshes. | comparison identity and matched condition | p. 8 (4.5. Qualitative results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The object grounding accuracy results from the ablation study of Nr3D and Sr3D are shown in Table 6 and Table 7, respectively. | component/input/data sensitivity | p. 6 (4.4. Ablation study) |
| In this section, we conduct an ablation study on both two datasets to analyze the influence of our proposed method, containing Chain of semantics ... | component/input/data sensitivity | p. 6 (4.4. Ablation study) |
| Without this mechanism, when errors occur during code execution, the only option is to reattempt reasoning, failing to learn from previous mistakes. | component/input/data sensitivity | p. 7 (4.4. Ablation study) |
| However, in Sr3D, the view-dependent grounding accuracy decreases by 12.8% (without Chain of Semantics) and 15.6% (with Chain of Semantics) compared to dialogue. | component/input/data sensitivity | p. 7 (4.4. Ablation study) |
| We used only 3D point clouds, images, and corresponding camera parameters for the reconstruction, without utilizing depth information or 3D meshes. | component/input/data sensitivity | p. 8 (4.5. Qualitative results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as follows: • We propose a chain of semantics programming method with the grounded-aware self-check mechanism for enhanced grounded reasoning ... | This mechanism achieves improvements of 4.5% on Nr3D and 1.8% on Sr3D. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.4. Ablation study), p. 5 (4.3. Comparison to Prior Works), p. 5 (4.3. Comparison to Prior Works), p. 6 (4.4. Ablation study), p. 7 (4.4. Ablation study), p. 8 (4.4. Ablation study) |
| Primary metric/result | Achieve zero-shot state-of-the-art grounding performance. | numeric claim only at cited anchor | p. 5 (4.3. Comparison to Prior Works) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We show that chain of semantics programming enhances the understanding of complex spatial relationships, and the 3D Gaussian Splatting representation provides fine-grained 2D semantics, ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | The fifth image illustrates a failure case where dense object grounding becomes more prone to confusion, increasing the difficulty of grounding to the correct ... | p. 8 (4.5. Qualitative results) |
| body limitation/failure cue | Without this mechanism, when errors occur during code execution, the only option is to reattempt reasoning, failing to learn from previous mistakes. | p. 7 (4.4. Ablation study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In the context of programming, generating erroneous code is a common occurrence. | p. 7 (4.4. Ablation study) |
| This challenge is particularly pronounced in Nr3D, where semantic complexity makes generating correct code more difficult. | p. 7 (4.4. Ablation study) |
| The chair to the far left hand side of the taller desk with the computer monitor on it The blackish pillow under another blue ... | p. 8 (4.4. Ablation study) |
| The generated code will be executed and will employ a grounded-aware self-check mechanism to reevaluate the response and re-ground the object if necessary. then ... | p. 4 (3.2. Dynamic Interaction in 3DGS Representation) |
| As shown in the left part of Figure 2 (a), the utterance has been split into three reasoning steps: C(U) ={There are two cabinets ... | p. 3 (3.1. Utterance Semantics Parsing) |
| We then generate Python code using the utterance U, 3D scene 24563 | p. 4 (3.3. Chain of Semantics Programming) |
| Additionally, the complexity of multi-step reasoning increases the difficulty for LLM in generating correct executable code. | p. 5 (3.4. Grounded-aware Self-Check Mechanism) |
| For instance, if the user intends to locate a single object but two are returned, or if the execution yields no results (e.g., no ... | p. 5 (3.4. Grounded-aware Self-Check Mechanism) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** We show that chain of semantics programming enhances the understanding of complex spatial relationships, and the 3D Gaussian Splatting representation provides fine-grained 2D semantics, overcoming ...
- **p. 8 / 4.5. Qualitative results - extractive body cue:** The fifth image illustrates a failure case where dense object grounding becomes more prone to confusion, increasing the difficulty of grounding to the correct object.
- **p. 7 / 4.4. Ablation study - extractive body cue:** Without this mechanism, when errors occur during code execution, the only option is to reattempt reasoning, failing to learn from previous mistakes.

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Datasets), p. 7 (4.4. Ablation study), p. 7 (4.4. Ablation study), p. 5 (4.3. Comparison to Prior Works), p. 6 (4.4. Ablation study), p. 6 (4.4. Ablation study), metrics p. 7 (4.4. Ablation study), p. 6 (4.4. Ablation study), p. 7 (4.4. Ablation study), p. 5 (4.3. Comparison to Prior Works), p. 8 (4.4. Ablation study), p. 1 (Figure/Table caption), baselines p. 5 (4.3. Comparison to Prior Works), p. 5 (4.3. Comparison to Prior Works), p. 7 (4.4. Ablation study), p. 6 (4.4. Ablation study), p. 6 (4.4. Ablation study), p. 8 (4.5. Qualitative results), results p. 7 (4.4. Ablation study), p. 5 (4.3. Comparison to Prior Works), p. 5 (4.3. Comparison to Prior Works), p. 6 (4.4. Ablation study), p. 7 (4.4. Ablation study), p. 8 (4.4. Ablation study).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
