# PASG: A Closed-Loop Framework for Automated Geometric Primitive Extraction and Semantic Anchoring in Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_PASG_A_Closed-Loop_Framework_for_Automated_Geometric_Primitive_Extraction_and_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_PASG_A_Closed-Loop_Framework_for_Automated_Geometric_Primitive_Extraction_and_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, semantic
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_PASG_A_Closed-Loop_Framework_for_Automated_Geometric_Primitive_Extraction_and_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_PASG_A_Closed-Loop_Framework_for_Automated_Geometric_Primitive_Extraction_and_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This limitation stems from insufficient semantic understanding of object canonical spaces-for instance, manually annotated "handle centers" for teapots lack contextual semantics (such as functional descriptions and usage scenarios), lea ...를 문제로 두고, Our contributions are as follows: • We propose a novel framework that automatically annotates hierarchical semantics for object interaction primitives, bridging the gap between low-level geometric features and high-level task semantics. ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The fragmentation between high-level task semantics and low-level geometric features remains a persistent challenge in robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** While vision-language models (VLMs) have shown promise in generating affordanceaware visual representations, the lack of semantic grounding in canonical spaces and reliance on manual annotations ...
- **p. 1 / Abstract - extractive body cue:** To address these, we propose Primitive-Aware Semantic Grounding (PASG), a closed
- **p. 1 / Abstract - extractive body cue:** We demonstrate PASG's effectiveness in practical robotic manipulation tasks across diverse scenarios, achieving performance comparable to manual annotations.
- **p. 1 / Abstract - extractive body cue:** PASG achieves a finer-grained semantic-affordance understanding of objects, establishing a unified paradigm for bridging geometric primitives with task semantics in robotic manipulation.
- **p. 2 / 1. Introduction - extractive body cue:** This limitation stems from insufficient semantic understanding of object canonical spaces-for instance, manually annotated "handle centers" for teapots lack contextual semantics (such as functional descriptions ...
- **p. 2 / 1. Introduction - extractive body cue:** Nevertheless, such frameworks exhibit two systemic weaknesses: (1) Automated detection methods (e.g., SAM [28], DINOV2 [43]) lack verification mechanisms, propagating errors from undetected or misaligned ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are as follows: • We propose a novel framework that automatically annotates hierarchical semantics for object interaction primitives, bridging the gap between low-level ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, as shown in Fig 1, we propose PASG, a closed-loop framework establishing the mapping between spatial primitives and functional semantics.
- **p. 3 / Method - extractive body cue:** OmniManip employs computational constraint optimization and scene rendering for VLM validation, while our method directly detects annotation-primitive misalignment for efficient self-correction. addresses this limitation by ...
- **p. 5 / 3.3. Task-Oriented Semantic Annotation - extractive body cue:** Experiments demonstrate that our method achieves a 98% matching success rate on our dataset and effectively mitigates error propagation from poor segmentation.
- **p. 6 / 3.4. Semantic-guide Reasoning in Manipulation - extractive body cue:** Beyond generating geometrically annotated object datasets, our framework facilitates the integration of spatial semantics into manipulation tasks.
- **p. 4 / 3.2. Geometry Primitive Extraction - extractive body cue:** To enable this, we first acquire multi-view RGB images ( \ math cal {I} = \{I_1,...,I_n\} ) from the object's 3D mesh data, which are ...
- **p. 5 / 3.3. Task-Oriented Semantic Annotation - extractive body cue:** Specifically, we use VLMs to analyze geometric and physical features from multi-view images ( \mathcal {I} ) to infer potential manipulation tasks ( \ math ...
- **p. 3 / Method - extractive body cue:** Normative interaction primitive and semantic coupling across different frameworks in robotic manipulation tasks: PASG as the first automated closed-loop framework with primitive extraction, semantic anchoring, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our contributions are as follows: • We propose a novel framework that automatically annotates hierarchical semantics for object interaction primitives, bridging the gap between low-level geometric features and high-level task semantics. ... | image/video, language instruction, proprioception과 history | p. 2 (1. Introduction), p. 3 (2.2. Spatial Reasoning for Manipulation) |
| State/latent | contributions, follows, novel, framework, automatically, annotates, hierarchical, semantics, object, interaction, primitives, bridging | language-grounded task state와 action-policy context | p. 2 (1. Introduction), p. 3 (2.2. Spatial Reasoning for Manipulation), p. 3 (3.1. Semantic Primitives in Robotic Manipulation) |
| Output/action | Spatial reasoning in manipulation involves inferring interaction constraints from object's spatial primitives to guide robot actions. | continuous action, pose 또는 action chunk | p. 3 (2.2. Spatial Reasoning for Manipulation), p. 3 (3.1. Semantic Primitives in Robotic Manipulation), p. 4 (3.1. Semantic Primitives in Robotic Manipulation) |
| Objective/outcome | OmniManip employs computational constraint optimization and scene rendering for VLM validation, while our method directly detects annotation-primitive misalignment for efficient self-correction. addresses this limitation by proposing di ... | instruction following, task success, generalization과 latency | p. 3 (Method), p. 3 (2.2. Spatial Reasoning for Manipulation), p. 4 (3.1. Semantic Primitives in Robotic Manipulation) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are as follows: • We propose a novel framework that automatically annotates hierarchical semantics for object interaction primitives, bridging the gap between low-level ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, as shown in Fig 1, we propose PASG, a closed-loop framework establishing the mapping between spatial primitives and functional semantics.
- **p. 3 / Method - extractive body cue:** OmniManip employs computational constraint optimization and scene rendering for VLM validation, while our method directly detects annotation-primitive misalignment for efficient self-correction. addresses this limitation by ...
- **p. 5 / 3.3. Task-Oriented Semantic Annotation - extractive body cue:** Experiments demonstrate that our method achieves a 98% matching success rate on our dataset and effectively mitigates error propagation from poor segmentation.
- **p. 6 / 3.4. Semantic-guide Reasoning in Manipulation - extractive body cue:** Beyond generating geometrically annotated object datasets, our framework facilitates the integration of spatial semantics into manipulation tasks.
- **p. 7 / 4.2. Manipulation Task Evaluation - extractive body cue:** Results of this comparison are summarized in Table 2, the PASG-based policy achieves competitive performance compared to manual annotations, and even outperforms them in tasks ...
- **p. 8 / 4.3. Object-based Spatial-Semantic Reasoning - extractive body cue:** As shown in Fig 5, with only 5% data, the model achieved an absolute accuracy improvement of approximately 10% on both in-distribution and out-of-distribution test ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Task success rates (%) for different manipulation scenarios. Bold highlights where PASG outperforms human annotations. Qualitative Results A key advantage of PASG is ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.2. Manipulation Task Evaluation), p. 8 (4.3. Object-based Spatial-Semantic Reasoning) |
| Embodiment/environment | RoboTwin provides standardized benchmarks that ensure both reproducibility and practical relevance. | hardware/simulator version and reset protocol | p. 7 (4.2. Manipulation Task Evaluation), p. 7 (4.3. Object-based Spatial-Semantic Reasoning) |
| Dataset/benchmark | RoboCasa provides over 2,500 high-quality 3D objects covering more than 150 categories in everyday tasks, whereas Objaverse is a large-scale open dataset containing over 800,000 annotated 3D objects. | role, split, size and leakage | p. 7 (4.2. Manipulation Task Evaluation), p. 7 (4.3. Object-based Spatial-Semantic Reasoning), p. 6 (4.1. Semantic-aware Object Dataset), p. 6 (4.1. Semantic-aware Object Dataset) |
| Metric | Task success rates (%) for different manipulation scenarios. | definition, denominator, direction and uncertainty | p. 7 (4.2. Manipulation Task Evaluation), p. 7 (4.2. Manipulation Task Evaluation), p. 8 (4.3. Object-based Spatial-Semantic Reasoning) |
| Baseline/ablation | Results of this comparison are summarized in Table 2, the PASG-based policy achieves competitive performance compared to manual annotations, and even outperforms them in tasks such as "Block Hammer Beat" and "Empty ... | fair input/data/compute/action matching | p. 7 (4.2. Manipulation Task Evaluation), p. 8 (4.3. Object-based Spatial-Semantic Reasoning), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** It overcomes key limitations in existing systems through geometry-aware feature aggregation, dynamic coupling of primitives with functional affordances, and selfcorrective mechanisms to reduce error propagation.
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. Normative interaction primitive and semantic coupling across different frameworks in robotic manipulation tasks: PASG as the first automated closed-loop framework with primitive extraction, ...
- **p. 8 / 5. Conclusion - extractive body cue:** PASG's ability to generate diverse interaction primitives enhances task flexibility and robustness, making it suitable for real-world applications.
- **p. 7 / 4.2. Manipulation Task Evaluation - extractive body cue:** Each task is executed 100 times using randomly initialized seeds to ensure robustness of the evaluation.
- **p. 7 / 4.2. Manipulation Task Evaluation - extractive body cue:** This diversity provides the manipulation policy with greater flexibility and enhances robustness to variations in task execution.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This limitation stems from insufficient semantic understanding of object canonical spaces-for instance, manually annotated "handle centers" for teapots lack contextual semantics (such as functional descriptions and usage scenarios), lea ...를 문제로 두고, Our contributions are as follows: • We propose a novel framework that automatically annotates hierarchical semantics for object interaction primitives, bridging the gap between low-level geometric features and high-level task semantics. ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Geometry Primitive Extraction), p. 5 (3.3. Task-Oriented Semantic Annotation), p. 3 (Method), p. 3 (2.2. Spatial Reasoning for Manipulation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
