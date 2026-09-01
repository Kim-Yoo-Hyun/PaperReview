# Evaluation - SpatialLLM: A Compound 3D-Informed Design towards Spatially-Intelligent Large Multimodal Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Ma_SpatialLLM_A_Compound_3D-Informed_Design_towards_Spatially-Intelligent_Large_Multimodal_Models_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Ma_SpatialLLM_A_Compound_3D-Informed_Design_towards_Spatially-Intelligent_Large_Multimodal_Models_CVPR_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. Results), p. 7 (4.2. Results), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption)): Comparison with the state-of-the-arts including proprietary and open source models. ably, our model achieves a performance of 62.7%, outperforming the top proprietary model by 8.7% and the best open-source model ...

## Evaluation Body Digest

- **p. 4 / 3.2.2. SpatialVQA for Evaluation - extractive PDF cue:** We build our SpatialVQA on images from Omni3D [11], with 3D bounding box annotations on diverse objects from both urban [12, 21] and indoor scenes ...
- **p. 4 / 3.2.2. SpatialVQA for Evaluation - extractive PDF cue:** Early datasets on spatial reasoning were built on 3D scans rather than images [6, 64].
- **p. 7 / 4.2. Results - extractive PDF cue:** In terms of 3D-informed data and training, we find that 3Dinformed instruction tuning with our proposed 3DI-Ft1M dataset yields a substantial performance boost of +10.7%.
- **p. 7 / 4.1. Experimental setup - extractive PDF cue:** Our training setup is built upon LLaVA-v1.5 [39] and all hyperparameters remain unchanged unless explicitly stated otherwise.
- **p. 4 / 3.2.2. SpatialVQA for Evaluation - extractive PDF cue:** We follow [16, 58] and develop rule-based methods to generate visual question-answer pairs from the 3D groundtruths.
- **p. 4 / 3.2.2. SpatialVQA for Evaluation - extractive PDF cue:** Recent visual-language benchmarks on spatial reasoning either focused on 2D spatial relationships [14, 16], e.g., left or right in the image plane, or only on ...
- **p. 7 / 4.2. Results - extractive PDF cue:** We analyze the results and elaborate the findings detailed below.
- **p. 7 / 4.2. Results - extractive PDF cue:** The human-annotated ImageNet3D provides more accurate 3D orientation of objects.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3.2.2. SpatialVQA for Evaluation (p. 4); 4. Experiments (p. 7); 4.1. Experimental setup (p. 7); 4.2. Results (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Comparison with the state-of-the-arts including proprietary and open source models. ably, our model achieves a performance of 62.7%, outperforming the top proprietary model by ... | p. 7 (4.2. Results) |
| 4.2. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | In terms of architecture, integrating a mixed vision encoder can improve overall performance especially for the 3D orientation. | p. 7 (4.2. Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 6. We modernize a standard LLaVA-v1.5 towards the de- sign of a 3D-informed LMM. The bars are the answer accuracies on the SpatialVQA ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 5. Design instantiation and comparison. (a) Architecture and Training of our proposed design. We investigate the 3D-awareness of mixed visual encoders, and incorporate ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 2. Thorough exploration of the design space and roadmap progression. We systematically examine the 3D-informed design space from the aspects of data, architecture ... | p. 8 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 4 / 3.2.2. SpatialVQA for Evaluation - extractive PDF cue:** We build our SpatialVQA on images from Omni3D [11], with 3D bounding box annotations on diverse objects from both urban [12, 21] and indoor scenes ...
- **p. 4 / 3.2.2. SpatialVQA for Evaluation - extractive PDF cue:** Early datasets on spatial reasoning were built on 3D scans rather than images [6, 64].
- **p. 7 / 4.2. Results - extractive PDF cue:** In terms of 3D-informed data and training, we find that 3Dinformed instruction tuning with our proposed 3DI-Ft1M dataset yields a substantial performance boost of +10.7%.
- **p. 7 / 4.1. Experimental setup - extractive PDF cue:** Our training setup is built upon LLaVA-v1.5 [39] and all hyperparameters remain unchanged unless explicitly stated otherwise.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. 3D spatial reasoning is crucial for LMMs to ground ob- jects in 3D space and infer their 3D spatial relationships, such as distance, ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Examples from our SpatialVQA benchmark featuring a broad range of questions that require 3D spatial reasoning. modern LMMs, the lack of 3D awareness ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Design space for LMMs capable of spatial reason- ing. The dashed boxes and lines highlight our new design space compared to LLaVA-v1.5. This ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Comparison of data cards showcasing the curation pro- cess and data types: standard LLaVA data (left) vs. our 3D- informed data (right). For ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Design instantiation and comparison. (a) Architecture and Training of our proposed design. We investigate the 3D-awareness of mixed visual encoders, and incorporate 3D-informed ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 6. We modernize a standard LLaVA-v1.5 towards the de- sign of a 3D-informed LMM. The bars are the answer accuracies on the SpatialVQA benchmark, ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison with the state-of-the-arts including pro- prietary and open source models. ably, our model achieves a performance of 62.7%, outper- forming the top ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2. Thorough exploration of the design space and roadmap progression. We systematically examine the 3D-informed design space from the aspects of data, architecture and ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We build our SpatialVQA on images from Omni3D [11], with 3D bounding box annotations on diverse objects from both urban [12, 21] and indoor ... | embodiment, simulator version and control stack | p. 4 (3.2.2. SpatialVQA for Evaluation), p. 4 (3.2.2. SpatialVQA for Evaluation) |
| Task/environment | Early datasets on spatial reasoning were built on 3D scans rather than images [6, 64]. | reset, timeout, object/scene variation | p. 4 (3.2.2. SpatialVQA for Evaluation), p. 7 (4.2. Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.2.1. Challenges of 3D spatial reasoning), p. 3 (3.1. Preliminary of LMMs) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3.3. Compound 3D-Informed Design), p. 6 (3.3.1. Design space) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We follow [16, 58] and develop rule-based methods to generate visual question-answer pairs from the 3D groundtruths. | definition/direction/unit from same section | p. 4 (3.2.2. SpatialVQA for Evaluation) |
| Recent visual-language benchmarks on spatial reasoning either focused on 2D spatial relationships [14, 16], e.g., left or right in the image plane, or only ... | definition/direction/unit from same section | p. 4 (3.2.2. SpatialVQA for Evaluation) |
| We analyze the results and elaborate the findings detailed below. | definition/direction/unit from same section | p. 7 (4.2. Results) |
| The human-annotated ImageNet3D provides more accurate 3D orientation of objects. | definition/direction/unit from same section | p. 7 (4.2. Results) |
| Figure 7. Our model is capable of answering question correctly that needs accurate reasoning on spatial distance and 3D orienta- tion, while GPT-4o either ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Table 2. Thorough exploration of the design space and roadmap progression. We systematically examine the 3D-informed design space from the aspects of data, architecture ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 1. 3D spatial reasoning is crucial for LMMs to ground ob- jects in 3D space and infer their 3D spatial relationships, such as ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 4. Comparison of data cards showcasing the curation pro- cess and data types: standard LLaVA data (left) vs. our 3D- informed data (right). ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Comparison with the state-of-the-arts including proprietary and open source models. ably, our model achieves a performance of 62.7%, outperforming the top proprietary model by ... | comparison identity and matched condition | p. 7 (4.2. Results) |
| Interestingly, although SpatialVLM [14] (implemented in SpaceLLaVA [2]) outperforms other open-source models in overall performance, it falls short in 3D orientation reasoning compared to ... | comparison identity and matched condition | p. 7 (4.2. Results) |
| Figure 3. Design space for LMMs capable of spatial reason- ing. The dashed boxes and lines highlight our new design space compared to LLaVA-v1.5. ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| Table 2. Thorough exploration of the design space and roadmap progression. We systematically examine the 3D-informed design space from the aspects of data, architecture ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Figure 5. Design instantiation and comparison. (a) Architecture and Training of our proposed design. We investigate the 3D-awareness of mixed visual encoders, and incorporate ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 4. Comparison of data cards showcasing the curation pro- cess and data types: standard LLaVA data (left) vs. our 3D- informed data (right). ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 2. Thorough exploration of the design space and roadmap progression. We systematically examine the 3D-informed design space from the aspects of data, architecture ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 5. Design instantiation and comparison. (a) Architecture and Training of our proposed design. We investigate the 3D-awareness of mixed visual encoders, and incorporate ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| 3D-informed pretraining of vision encoder? | component/input/data sensitivity | p. 7 (4.2. Results) |
| We observe that pre-pretraining in stage 0 reduces performance, suggesting that tuning vi17255 | component/input/data sensitivity | p. 7 (4.2. Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Second, we propose a novel compound 3D-informed design that introduces improvements across multiple dimensions, leading to our proposed SpatialLLM model. | Comparison with the state-of-the-arts including proprietary and open source models. ably, our model achieves a performance of 62.7%, outperforming the top proprietary model by ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. Results), p. 7 (4.2. Results), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | In terms of architecture, integrating a mixed vision encoder can improve overall performance especially for the 3D orientation. | numeric claim only at cited anchor | p. 7 (4.2. Results) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our SpatialVQA distinguishes itself from all previous spatial reasoning benchmarks in the sense that all questions require different levels of 3D awareness and cannot ... | p. 4 (3.2.2. SpatialVQA for Evaluation) |
| body limitation/failure cue | Interestingly, although SpatialVLM [14] (implemented in SpaceLLaVA [2]) outperforms other open-source models in overall performance, it falls short in 3D orientation reasoning compared to ... | p. 7 (4.2. Results) |
| body limitation/failure cue | We will consider models with additional inputs in future work. | p. 7 (4.2. Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 3D-informed pretraining of vision encoder? | p. 7 (4.2. Results) |
| Our training setup is built upon LLaVA-v1.5 [39] and all hyperparameters remain unchanged unless explicitly stated otherwise. | p. 7 (4.1. Experimental setup) |
| A standard LMM [39, 41] consists of a visual encoder to process the image, a multimodal connector to transform the visual feature to visual ... | p. 3 (3.1. Preliminary of LMMs) |
| We review these architectural components as below. • Vision encoder: Most LMMs rely on languagesupervised models like CLIP [48], leveraging web-scale noisy image-text data. | p. 3 (3.1. Preliminary of LMMs) |
| 3D awareness refers to the ability of a visual encoder to represent 3D-aware features such as 3D object shapes and 3D orientations. | p. 4 (3.2.1. Challenges of 3D spatial reasoning) |
| 3.2.1, we consider two main aspects in our compound 3D-informed design - the architecture design that leads to visual encoders with strong 3D awareness ... | p. 4 (3.3. Compound 3D-Informed Design) |
| In a multimodal LLM, a pre-trained CLIP visual encoder extracts grid features from the input image. | p. 5 (3.3.1. Design space) |
| Inspired by Probe3D [19] which probes the 3D-awareness of visual foundation models, we study the design of visual encoder to enable better 3D spatial ... | p. 5 (3.3.1. Design space) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / 3.2.2. SpatialVQA for Evaluation - extractive PDF cue:** Our SpatialVQA distinguishes itself from all previous spatial reasoning benchmarks in the sense that all questions require different levels of 3D awareness and cannot be ...
- **p. 7 / 4.2. Results - extractive PDF cue:** Interestingly, although SpatialVLM [14] (implemented in SpaceLLaVA [2]) outperforms other open-source models in overall performance, it falls short in 3D orientation reasoning compared to LLaVA, ...
- **p. 7 / 4.2. Results - extractive PDF cue:** We will consider models with additional inputs in future work.

- **PDF anchors reviewed:** datasets p. 4 (3.2.2. SpatialVQA for Evaluation), p. 4 (3.2.2. SpatialVQA for Evaluation), p. 7 (4.2. Results), p. 7 (4.1. Experimental setup), metrics p. 4 (3.2.2. SpatialVQA for Evaluation), p. 4 (3.2.2. SpatialVQA for Evaluation), p. 7 (4.2. Results), p. 7 (4.2. Results), p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), baselines p. 7 (4.2. Results), p. 7 (4.2. Results), p. 5 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (Figure/Table caption), results p. 7 (4.2. Results), p. 7 (4.2. Results), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
