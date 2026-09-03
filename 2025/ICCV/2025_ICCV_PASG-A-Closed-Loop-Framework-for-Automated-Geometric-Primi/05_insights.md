# Insights — PASG: A Closed-Loop Framework for Automated Geometric Primitive Extraction and Semantic Anchoring in Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_PASG_A_Closed-Loop_Framework_for_Automated_Geometric_Primitive_Extraction_and_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_PASG_A_Closed-Loop_Framework_for_Automated_Geometric_Primitive_Extraction_and_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are as follows: • We propose a novel framework that automatically annotates hierarchical semantics for object interaction primitives, bridging the gap between low-level ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, as shown in Fig 1, we propose PASG, a closed-loop framework establishing the mapping between spatial primitives and functional semantics.
- **p. 3 / Method - extractive body cue:** OmniManip employs computational constraint optimization and scene rendering for VLM validation, while our method directly detects annotation-primitive misalignment for efficient self-correction. addresses this limitation by ...
- **p. 5 / 3.3. Task-Oriented Semantic Annotation - extractive body cue:** Experiments demonstrate that our method achieves a 98% matching success rate on our dataset and effectively mitigates error propagation from poor segmentation.
- **p. 6 / 3.4. Semantic-guide Reasoning in Manipulation - extractive body cue:** Beyond generating geometrically annotated object datasets, our framework facilitates the integration of spatial semantics into manipulation tasks.
- **p. 4 / 3.2. Geometry Primitive Extraction - extractive body cue:** To enable this, we first acquire multi-view RGB images ( \ math cal {I} = \{I_1,...,I_n\} ) from the object's 3D mesh data, which are ...
- **p. 5 / 3.3. Task-Oriented Semantic Annotation - extractive body cue:** Specifically, we use VLMs to analyze geometric and physical features from multi-view images ( \mathcal {I} ) to infer potential manipulation tasks ( \ math ...
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (Method), p. 5 (3.3. Task-Oriented Semantic Annotation), p. 6 (3.4. Semantic-guide Reasoning in Manipulation), p. 4 (3.2. Geometry Primitive Extraction)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** This limitation stems from insufficient semantic understanding of object canonical spaces-for instance, manually annotated "handle centers" for teapots lack contextual semantics (such as functional descriptions ...
- **p. 2 / 1. Introduction - extractive body cue:** Nevertheless, such frameworks exhibit two systemic weaknesses: (1) Automated detection methods (e.g., SAM [28], DINOV2 [43]) lack verification mechanisms, propagating errors from undetected or misaligned ...
- **p. 8 / 5. Conclusion - extractive body cue:** It overcomes key limitations in existing systems through geometry-aware feature aggregation, dynamic coupling of primitives with functional affordances, and selfcorrective mechanisms to reduce error propagation.
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. Normative interaction primitive and semantic coupling across different frameworks in robotic manipulation tasks: PASG as the first automated closed-loop framework with primitive extraction, ...
- **p. 8 / 5. Conclusion - extractive body cue:** PASG's ability to generate diverse interaction primitives enhances task flexibility and robustness, making it suitable for real-world applications.
- **p. 7 / 4.2. Manipulation Task Evaluation - extractive body cue:** Each task is executed 100 times using randomly initialized seeds to ensure robustness of the evaluation.
- **p. 7 / 4.2. Manipulation Task Evaluation - extractive body cue:** This diversity provides the manipulation policy with greater flexibility and enhances robustness to variations in task execution.
- **Boundary to test:** It overcomes key limitations in existing systems through geometry-aware feature aggregation, dynamic coupling of primitives with functional affordances, and selfcorrective mechanisms to reduce error propagation.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Our contributions are as follows: • We propose a novel framework that automatically annotates hierarchical semantics for object interaction primitives, bridging the gap between low-level geometric features and high-level task semantics. ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Results of this comparison are summarized in Table 2, the PASG-based policy achieves competitive performance compared to manual annotations, and even outperforms them in tasks such as "Block Hammer Beat" and "Empty ... | p. 7 (4.2. Manipulation Task Evaluation), p. 8 (4.3. Object-based Spatial-Semantic Reasoning) |
| Failure/limitation | It overcomes key limitations in existing systems through geometry-aware feature aggregation, dynamic coupling of primitives with functional affordances, and selfcorrective mechanisms to reduce error propagation. | p. 8 (5. Conclusion), p. 3 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `image/video, language instruction, proprioception과 history → language-grounded task state와 action-policy context → continuous action, pose 또는 action chunk`.
- 이 논문의 재사용 가능한 지점은 Our contributions are as follows: • We propose a novel framework that automatically annotates hierarchical semantics for object interaction primitives, bridging the gap between low-level geometric features and high-level task semantics. ...를 Spatial reasoning in manipulation involves inferring interaction constraints from object's spatial primitives to guide robot actions.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 language-grounded task state와 action-policy context가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 It overcomes key limitations in existing systems through geometry-aware feature aggregation, dynamic coupling of primitives with functional affordances, and selfcorrective mechanisms to reduce error propagation.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Our contributions are as follows: • We propose a novel framework that automatically annotates hierarchical semantics for object interaction primitives, bridging the gap between low-level geometric features and high-level task semantics. ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `VLA and generalist robot policies`; tags: `Robotics, semantic`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** It overcomes key limitations in existing systems through geometry-aware feature aggregation, dynamic coupling of primitives with functional affordances, and selfcorrective mechanisms to reduce error propagation.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: RoboTwin provides standardized benchmarks that ensure both reproducibility and practical relevance..
3. Compare against the body-reported baseline or a matched simpler baseline: Results of this comparison are summarized in Table 2, the PASG-based policy achieves competitive performance compared to manual annotations, and even outperforms them in tasks such as "Block Hammer Beat" and "Empty ....
4. Report the body metric and its denominator/aggregation: Task success rates (%) for different manipulation scenarios..
5. Re-run the body-reported ablation/failure condition: Data Effectiveness Study Data Effectiveness To evaluate the effectiveness of finetuning data, we conducted a progressive scaling experiment: fine-tune the model with randomly sampled subsets of 1% (55 samples), 5% (279 samples), ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.2. Geometry Primitive Extraction), p. 5 (3.3. Task-Oriented Semantic Annotation), p. 3 (Method); the primary result is directionally consistent at p. 7 (4.2. Manipulation Task Evaluation), p. 8 (4.3. Object-based Spatial-Semantic Reasoning), p. 7 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 contributions, follows, novel mechanism이 Results of this comparison are summarized in Table 2, the PASG-based policy achieves competitive performance compared ... 대비 Task success rates (%) for different manipulation scenarios.을 개선하고, It overcomes key limitations in existing systems through geometry-aware feature aggregation, dynamic coupling of primitives with ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
