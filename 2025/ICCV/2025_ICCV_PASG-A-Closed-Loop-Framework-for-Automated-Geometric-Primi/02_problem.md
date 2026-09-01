# Problem - PASG: A Closed-Loop Framework for Automated Geometric Primitive Extraction and Semantic Anchoring in Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_PASG_A_Closed-Loop_Framework_for_Automated_Geometric_Primitive_Extraction_and_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_PASG_A_Closed-Loop_Framework_for_Automated_Geometric_Primitive_Extraction_and_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): This limitation stems from insufficient semantic understanding of object canonical spaces-for instance, manually annotated "handle centers" for teapots lack contextual semantics (such as functional descriptions and usage scenarios), lea ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** The fragmentation between high-level task semantics and low-level geometric features remains a persistent challenge in robotic manipulation.
- **p. 1 / Abstract - extractive PDF cue:** While vision-language models (VLMs) have shown promise in generating affordanceaware visual representations, the lack of semantic grounding in canonical spaces and reliance on manual annotations ...
- **p. 1 / Abstract - extractive PDF cue:** To address these, we propose Primitive-Aware Semantic Grounding (PASG), a closed- *Equal Contribution. †Yao Mu and Yaohui Jin are the corresponding authors loop framework that ...
- **p. 1 / Abstract - extractive PDF cue:** We demonstrate PASG's effectiveness in practical robotic manipulation tasks across diverse scenarios, achieving performance comparable to manual annotations.
- **p. 1 / Abstract - extractive PDF cue:** PASG achieves a finer-grained semantic-affordance understanding of objects, establishing a unified paradigm for bridging geometric primitives with task semantics in robotic manipulation.
- **p. 2 / 1. Introduction - extractive PDF cue:** This limitation stems from insufficient semantic understanding of object canonical spaces-for instance, manually annotated "handle centers" for teapots lack contextual semantics (such as functional descriptions ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Nevertheless, such frameworks exhibit two systemic weaknesses: (1) Automated detection methods (e.g., SAM [28], DINOV2 [43]) lack verification mechanisms, propagating errors from undetected or misaligned ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This limitation stems from insufficient semantic understanding of object canonical spaces-for instance, manually annotated "handle centers" for teapots lack contextual semantics (such ... | language-conditioned robot task와 embodiment | body wording is the source claim |
| Observation / input | Our contributions are as follows: • We propose a novel framework that automatically annotates hierarchical semantics for object interaction primitives, bridging the ... | image/video, language instruction, proprioception과 history | exact sensor/frame/preprocessing from PDF |
| State / latent | contributions, follows, novel, framework, automatically, annotates, hierarchical, semantics, object, interaction | language-grounded task state와 action-policy context | notation and tensor shape require body check |
| Output / action | robotic, manipulation, tasks, spatial, primitives, objects, serve, fundamental | continuous action, pose 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | instruction-conditioned task success | instruction following, task success, generalization과 latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | multimodal context o,l,p/history; body terms: contributions, follows, novel, framework, automatically, annotates, hierarchical, semantics, object, interaction | p. 2 (1. Introduction), p. 3 (2.2. Spatial Reasoning for Manipulation), p. 3 (3.1. Semantic Primitives in Robotic Manipulation) |
| Decision / output variable | action, pose, option or chunk a; body terms: contributions, follows, novel, framework, automatically, annotates, hierarchical, semantics | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (Method) |
| Objective / loss / cost | policy/action modeling objective; cue terms: OmniManip, employs, computational, constraint, optimization, scene, rendering, VLM | p. 3 (2.2. Spatial Reasoning for Manipulation), p. 3 (3.1. Semantic Primitives in Robotic Manipulation), p. 4 (3.1. Semantic Primitives in Robotic Manipulation), p. 5 (3.3. Task-Oriented Semantic Annotation), p. 5 (3.3. Task-Oriented Semantic Annotation) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3.3. Task-Oriented Semantic Annotation), p. 5 (3.3. Task-Oriented Semantic Annotation), p. 4 (3.1. Semantic Primitives in Robotic Manipulation) |
| Success / guarantee | instruction-conditioned task success | p. 7 (4.2. Manipulation Task Evaluation), p. 7 (4.2. Manipulation Task Evaluation), p. 8 (4.3. Object-based Spatial-Semantic Reasoning) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** Nevertheless, such frameworks exhibit two systemic weaknesses: (1) Automated detection methods (e.g., SAM [28], DINOV2 [43]) lack verification mechanisms, propagating errors from undetected or misaligned ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (Method), p. 5 (3.3. Task-Oriented Semantic Annotation), p. 6 (3.4. Semantic-guide Reasoning in Manipulation)): Our contributions are as follows: • We propose a novel framework that automatically annotates hierarchical semantics for object interaction primitives, bridging the gap between low-level geometric features and high-level task ...

- **p. 2 / 1. Introduction - extractive PDF cue:** To address these challenges, as shown in Fig 1, we propose PASG, a closed-loop framework establishing the mapping between spatial primitives and functional semantics.
- **p. 3 / Method - extractive PDF cue:** OmniManip employs computational constraint optimization and scene rendering for VLM validation, while our method directly detects annotation-primitive misalignment for efficient self-correction. addresses this limitation by ...
- **p. 5 / 3.3. Task-Oriented Semantic Annotation - extractive PDF cue:** Experiments demonstrate that our method achieves a 98% matching success rate on our dataset and effectively mitigates error propagation from poor segmentation.
- **p. 6 / 3.4. Semantic-guide Reasoning in Manipulation - extractive PDF cue:** Beyond generating geometrically annotated object datasets, our framework facilitates the integration of spatial semantics into manipulation tasks.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | It overcomes key limitations in existing systems through geometry-aware feature aggregation, dynamic coupling of primitives with functional affordances, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Table 1. Normative interaction primitive and semantic coupling across different frameworks in robotic manipulation tasks: PASG as the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | PASG's ability to generate diverse interaction primitives enhances task flexibility and robustness, making it suitable for real-world applications. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Each task is executed 100 times using randomly initialized seeds to ensure robustness of the evaluation. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

vla writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1. Introduction), p. 3 (2.2. Spatial Reasoning for Manipulation), p. 3 (3.1. Semantic Primitives in Robotic Manipulation), p. 4 (3.1. Semantic Primitives in Robotic Manipulation). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 2 (1. Introduction), p. 3 (2.2. Spatial Reasoning for Manipulation), p. 3 (3.1. Semantic Primitives in Robotic Manipulation), p. 4 (3.1. Semantic Primitives in Robotic Manipulation), objective p. 3 (2.2. Spatial Reasoning for Manipulation), p. 3 (3.1. Semantic Primitives in Robotic Manipulation), p. 4 (3.1. Semantic Primitives in Robotic Manipulation), p. 5 (3.3. Task-Oriented Semantic Annotation), p. 5 (3.3. Task-Oriented Semantic Annotation).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
