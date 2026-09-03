# Evaluation - PASG: A Closed-Loop Framework for Automated Geometric Primitive Extraction and Semantic Anchoring in Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_PASG_A_Closed-Loop_Framework_for_Automated_Geometric_Primitive_Extraction_and_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_PASG_A_Closed-Loop_Framework_for_Automated_Geometric_Primitive_Extraction_and_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. Manipulation Task Evaluation), p. 8 (4.3. Object-based Spatial-Semantic Reasoning), p. 7 (Figure/Table caption), p. 8 (4.3. Object-based Spatial-Semantic Reasoning), p. 1 (Figure/Table caption)): Results of this comparison are summarized in Table 2, the PASG-based policy achieves competitive performance compared to manual annotations, and even outperforms them in tasks such as "Block Hammer Beat" ...

## Evaluation Body Digest

- **p. 7 / 4.2. Manipulation Task Evaluation - extractive body cue:** RoboTwin provides standardized benchmarks that ensure both reproducibility and practical relevance.
- **p. 7 / 4.3. Object-based Spatial-Semantic Reasoning - extractive body cue:** This spatial-aware benchmark evaluates models' understanding of functional geometric primitives in robotic manipulation scenarios.
- **p. 6 / 4.1. Semantic-aware Object Dataset - extractive body cue:** RoboCasa provides over 2,500 high-quality 3D objects covering more than 150 categories in everyday tasks, whereas Objaverse is a large-scale open dataset containing over 800,000 ...
- **p. 6 / 4.1. Semantic-aware Object Dataset - extractive body cue:** Leveraging texture detection, we further refined our selection to obtain a high-quality dataset of 5,231 objects.
- **p. 8 / 4.3. Object-based Spatial-Semantic Reasoning - extractive body cue:** Spatial comprehension evaluation on our visual question-answer benchmark.
- **p. 8 / 4.3. Object-based Spatial-Semantic Reasoning - extractive body cue:** By constraining parameter updates to low-rank decomposition matrices, performance improvements can be causally attributed to knowledge distillation from the benchmark.
- **p. 7 / 4.2. Manipulation Task Evaluation - extractive body cue:** Task success rates (%) for different manipulation scenarios.
- **p. 7 / 4.2. Manipulation Task Evaluation - extractive body cue:** Quantitative Results We quantitatively compare the task success rates of PASG against a baseline involving manual annotations.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** language-conditioned robot task와 embodiment.
- **Input boundary:** image/video, language instruction, proprioception과 history.
- **Output/decision under evaluation:** continuous action, pose 또는 action chunk.
- **Primary target:** instruction following, task success, generalization과 latency.
- **Detected evaluation headings:** 4. Experiment (p. 6); 4.1. Semantic-aware Object Dataset (p. 6); 4.2. Manipulation Task Evaluation (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Manipulation Task Evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Results of this comparison are summarized in Table 2, the PASG-based policy achieves competitive performance compared to manual annotations, and even outperforms them in ... | p. 7 (4.2. Manipulation Task Evaluation) |
| 4.3. Object-based Spatial-Semantic Reasoning | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Fig 5, with only 5% data, the model achieved an absolute accuracy improvement of approximately 10% on both in-distribution and out-of-distribution ... | p. 8 (4.3. Object-based Spatial-Semantic Reasoning) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 2. Task success rates (%) for different manipulation scenarios. Bold highlights where PASG outperforms human annotations. Qualitative Results A key advantage of PASG ... | p. 7 (Figure/Table caption) |
| 4.3. Object-based Spatial-Semantic Reasoning | EMPIRICAL / SOURCE-REPORTED EVALUATION | When increasing the subset to 10%, the absolute accuracy further improved by 20%, achieving a 41.12% relative improvement over the baseline. | p. 8 (4.3. Object-based Spatial-Semantic Reasoning) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1. We propose PASG, an automated object-centric spatial-semantic enhancement framework for robotic manipulation. By for- malizing interaction primitives and establishing semantic-geometric correspondences, our ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 4.2. Manipulation Task Evaluation - extractive body cue:** RoboTwin provides standardized benchmarks that ensure both reproducibility and practical relevance.
- **p. 7 / 4.3. Object-based Spatial-Semantic Reasoning - extractive body cue:** This spatial-aware benchmark evaluates models' understanding of functional geometric primitives in robotic manipulation scenarios.
- **p. 6 / 4.1. Semantic-aware Object Dataset - extractive body cue:** RoboCasa provides over 2,500 high-quality 3D objects covering more than 150 categories in everyday tasks, whereas Objaverse is a large-scale open dataset containing over 800,000 ...
- **p. 6 / 4.1. Semantic-aware Object Dataset - extractive body cue:** Leveraging texture detection, we further refined our selection to obtain a high-quality dataset of 5,231 objects.
- **p. 8 / 4.3. Object-based Spatial-Semantic Reasoning - extractive body cue:** Spatial comprehension evaluation on our visual question-answer benchmark.
- **p. 8 / 4.3. Object-based Spatial-Semantic Reasoning - extractive body cue:** By constraining parameter updates to low-rank decomposition matrices, performance improvements can be causally attributed to knowledge distillation from the benchmark.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We propose PASG, an automated object-centric spatial-semantic enhancement framework for robotic manipulation. By for- malizing interaction primitives and establishing semantic-geometric correspondences, our approach ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. Normative interaction primitive and semantic coupling across different frameworks in robotic manipulation tasks: PASG as the first automated closed-loop framework with primitive extraction, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of PASG To further integrate operational task semantics, we cat- egorize interaction primitives into two functionally distinct classes based on manipulation requirements: ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Keypoints and Axes Annotated Output. This framework demonstrates the process of detecting, filtering, and semantically annotating functional keypoints and axes on 3D objects. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Task success rates (%) for different manipulation scenarios. Bold highlights where PASG outperforms human annotations. Qualitative Results A key advantage of PASG is ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Compared to manual annotation, PASG tends to generate a more diverse and semantically accurate set of interaction points.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Spatial comprehension evaluation on our visual question-answer benchmark. Numbers represent accuracy (%). training instances at both object and primitive levels. All images are ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Data Effectiveness Study Data Effectiveness To evaluate the effectiveness of fine- tuning data, we conducted a progressive scaling experi- ment: fine-tune the model ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | RoboTwin provides standardized benchmarks that ensure both reproducibility and practical relevance. | embodiment, simulator version and control stack | p. 7 (4.2. Manipulation Task Evaluation), p. 7 (4.3. Object-based Spatial-Semantic Reasoning) |
| Task/environment | This spatial-aware benchmark evaluates models' understanding of functional geometric primitives in robotic manipulation scenarios. | reset, timeout, object/scene variation | p. 7 (4.3. Object-based Spatial-Semantic Reasoning), p. 6 (4.1. Semantic-aware Object Dataset) |
| Observation/sensor | image/video, language instruction, proprioception과 history | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 3 (2.2. Spatial Reasoning for Manipulation) |
| Output/decision | continuous action, pose 또는 action chunk | action frame, controller and termination | p. 3 (3.1. Semantic Primitives in Robotic Manipulation), p. 4 (3.1. Semantic Primitives in Robotic Manipulation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Task success rates (%) for different manipulation scenarios. | definition/direction/unit from same section | p. 7 (4.2. Manipulation Task Evaluation) |
| Quantitative Results We quantitatively compare the task success rates of PASG against a baseline involving manual annotations. | definition/direction/unit from same section | p. 7 (4.2. Manipulation Task Evaluation) |
| Each question follows a single-choice format, and accuracy is used to evaluate performance across all sets. | definition/direction/unit from same section | p. 8 (4.3. Object-based Spatial-Semantic Reasoning) |
| Numbers represent accuracy (%). training instances at both object and primitive levels. | definition/direction/unit from same section | p. 8 (4.3. Object-based Spatial-Semantic Reasoning) |
| Figure 2. Overview of PASG To further integrate operational task semantics, we cat- egorize interaction primitives into two functionally distinct classes based on manipulation ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 3. Keypoints and Axes Annotated Output. This framework demonstrates the process of detecting, filtering, and semantically annotating functional keypoints and axes on 3D ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Results of this comparison are summarized in Table 2, the PASG-based policy achieves competitive performance compared to manual annotations, and even outperforms them in ... | comparison identity and matched condition | p. 7 (4.2. Manipulation Task Evaluation) |
| We selected several VLMs as baselines, including general-purpose large-scale vision language models and models with spatial awareness capabilities proposed in prior works, as shown ... | comparison identity and matched condition | p. 8 (4.3. Object-based Spatial-Semantic Reasoning) |
| Table 2. Task success rates (%) for different manipulation scenarios. Bold highlights where PASG outperforms human annotations. Qualitative Results A key advantage of PASG ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| When increasing the subset to 10%, the absolute accuracy further improved by 20%, achieving a 41.12% relative improvement over the baseline. | comparison identity and matched condition | p. 8 (4.3. Object-based Spatial-Semantic Reasoning) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Data Effectiveness Study Data Effectiveness To evaluate the effectiveness of finetuning data, we conducted a progressive scaling experiment: fine-tune the model with randomly sampled ... | component/input/data sensitivity | p. 8 (4.3. Object-based Spatial-Semantic Reasoning) |
| We first generate 6,979 questions from a designated pool of base objects, allocating 80% (5,583 questions) as the fine-tuning training set to establish a ... | component/input/data sensitivity | p. 7 (4.3. Object-based Spatial-Semantic Reasoning) |
| Finetune We fine-tuned Qwen-2.5VL [6] using Low-Rank Adaptation (LoRA) to assess whether the VQA benchmark supports knowledge transfer in primitive compositional reasoning. | component/input/data sensitivity | p. 8 (4.3. Object-based Spatial-Semantic Reasoning) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are as follows: • We propose a novel framework that automatically annotates hierarchical semantics for object interaction primitives, bridging the gap between ... | Results of this comparison are summarized in Table 2, the PASG-based policy achieves competitive performance compared to manual annotations, and even outperforms them in ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. Manipulation Task Evaluation), p. 8 (4.3. Object-based Spatial-Semantic Reasoning), p. 7 (Figure/Table caption), p. 8 (4.3. Object-based Spatial-Semantic Reasoning), p. 1 (Figure/Table caption) |
| Primary metric/result | As shown in Fig 5, with only 5% data, the model achieved an absolute accuracy improvement of approximately 10% on both in-distribution and out-of-distribution ... | numeric claim only at cited anchor | p. 8 (4.3. Object-based Spatial-Semantic Reasoning) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Semantic-aware Object Dataset - extractive body cue:** Leveraging texture detection, we further refined our selection to obtain a high-quality dataset of 5,231 objects.
- **p. 6 / 4.1. Semantic-aware Object Dataset - extractive body cue:** In total, we acquired a 5,231 object 3D dataset as well as an 41,848 image 2D dataset for subsequent semantic annotation.
- **p. 7 / 4.3. Object-based Spatial-Semantic Reasoning - extractive body cue:** The dataset comprises three question categories: Task 1 Type Identification (determining the functional category of spatial primitives from visual features), Task 2 Task Association (linking ...
- **p. 8 / 4.3. Object-based Spatial-Semantic Reasoning - extractive body cue:** Data Effectiveness Study Data Effectiveness To evaluate the effectiveness of finetuning data, we conducted a progressive scaling experiment: fine-tune the model with randomly sampled subsets ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | It overcomes key limitations in existing systems through geometry-aware feature aggregation, dynamic coupling of primitives with functional affordances, and selfcorrective mechanisms to reduce error ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | Table 1. Normative interaction primitive and semantic coupling across different frameworks in robotic manipulation tasks: PASG as the first automated closed-loop framework with primitive ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | PASG's ability to generate diverse interaction primitives enhances task flexibility and robustness, making it suitable for real-world applications. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Each task is executed 100 times using randomly initialized seeds to ensure robustness of the evaluation. | p. 7 (4.2. Manipulation Task Evaluation) |
| body limitation/failure cue | This diversity provides the manipulation policy with greater flexibility and enhances robustness to variations in task execution. | p. 7 (4.2. Manipulation Task Evaluation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Each task is executed 100 times using randomly initialized seeds to ensure robustness of the evaluation. | p. 7 (4.2. Manipulation Task Evaluation) |
| (e.g. the center of a mug's handle) • Actuation Point ( p_{act} ): The specific spot that triggers a mechanism or function when pressed ... | p. 4 (3.1. Semantic Primitives in Robotic Manipulation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** It overcomes key limitations in existing systems through geometry-aware feature aggregation, dynamic coupling of primitives with functional affordances, and selfcorrective mechanisms to reduce error propagation.
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. Normative interaction primitive and semantic coupling across different frameworks in robotic manipulation tasks: PASG as the first automated closed-loop framework with primitive extraction, ...
- **p. 8 / 5. Conclusion - extractive body cue:** PASG's ability to generate diverse interaction primitives enhances task flexibility and robustness, making it suitable for real-world applications.
- **p. 7 / 4.2. Manipulation Task Evaluation - extractive body cue:** Each task is executed 100 times using randomly initialized seeds to ensure robustness of the evaluation.
- **p. 7 / 4.2. Manipulation Task Evaluation - extractive body cue:** This diversity provides the manipulation policy with greater flexibility and enhances robustness to variations in task execution.

- **Evidence anchors reviewed:** datasets p. 7 (4.2. Manipulation Task Evaluation), p. 7 (4.3. Object-based Spatial-Semantic Reasoning), p. 6 (4.1. Semantic-aware Object Dataset), p. 6 (4.1. Semantic-aware Object Dataset), p. 8 (4.3. Object-based Spatial-Semantic Reasoning), p. 8 (4.3. Object-based Spatial-Semantic Reasoning), metrics p. 7 (4.2. Manipulation Task Evaluation), p. 7 (4.2. Manipulation Task Evaluation), p. 8 (4.3. Object-based Spatial-Semantic Reasoning), p. 8 (4.3. Object-based Spatial-Semantic Reasoning), p. 4 (Figure/Table caption), p. 6 (Figure/Table caption), baselines p. 7 (4.2. Manipulation Task Evaluation), p. 8 (4.3. Object-based Spatial-Semantic Reasoning), p. 7 (Figure/Table caption), p. 8 (4.3. Object-based Spatial-Semantic Reasoning), results p. 7 (4.2. Manipulation Task Evaluation), p. 8 (4.3. Object-based Spatial-Semantic Reasoning), p. 7 (Figure/Table caption), p. 8 (4.3. Object-based Spatial-Semantic Reasoning), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
