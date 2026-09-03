# Chain of Semantics Programming in 3D Gaussian Splatting Representation for 3D Vision Grounding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, semantic, grounding
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This oversight in capturing the connection and conditionality of spatial relationships results in a significant performance gap in grounding between these zero-shot methods and the current stateof-the-art supervised approaches.를 문제로 두고, Our contributions are summarized as follows: • We propose a chain of semantics programming method with the grounded-aware self-check mechanism for enhanced grounded reasoning in the 3DVG task. • We introduce a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D Vision Grounding (3DVG) is a fundamental research area that enables agents to perceive and interact with the 3D world.
- **p. 1 / Abstract - extractive body cue:** The challenge of the 3DVG task lies in understanding fine-grained semantics and spatial relationships within both the utterance and 3D scene.
- **p. 1 / Abstract - extractive body cue:** To address this challenge, we propose a zero-shot neuro-symbolic framework that utilizes a large language model (LLM) as neurosymbolic functions to ground the object within ...
- **p. 1 / Abstract - extractive body cue:** By utilizing 3DGS representation, we can dynamically render high-quality 2D images from various viewpoints to enrich the semantic information.
- **p. 1 / Abstract - extractive body cue:** Given the complexity of spatial relationships, we construct a relationship graph and chain of semantics that decouple spatial relationships and facilitate step-bystep reasoning within 3DGS ...
- **p. 2 / 1. Introduction - extractive body cue:** This oversight in capturing the connection and conditionality of spatial relationships results in a significant performance gap in grounding between these zero-shot methods and the ...
- **p. 1 / 1. Introduction - extractive body cue:** Since the representation of the 3D scene is often based on the point cloud, which is semantically sparse and subject to noise interference, the 3DVG ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We propose a chain of semantics programming method with the grounded-aware self-check mechanism for enhanced grounded reasoning in ...
- **p. 2 / 1. Introduction - extractive body cue:** This method constructs a relationship graph and facilitates a chain of semantics programming, enabling multi-step object grounding. • We first use 3DGS to reconstruct the ...
- **p. 3 / 3. Methodology - extractive body cue:** In this section, we introduce our proposed zero-shot neurosymbolic framework that employs a LLM as a neurosymbolic function for object grounding.
- **p. 3 / 3. Methodology - extractive body cue:** To enhance the effectiveness and robustness of the programming and reasoning process, we propose a grounded-aware self-check mechanism that reflects on the reasoning results.
- **p. 5 / 3.3. Chain of Semantics Programming - extractive body cue:** Through the chain of semantics programming, our framework can explicitly account for the conditionality of relationships and connections among multiple relationships, utilizing fine-grained semantics and ...
- **p. 4 / 3.2. Dynamic Interaction in 3DGS Representation - extractive body cue:** Then, based on the given utterance and the 3D scene, use the LLM to explore the 3DGS representation, identify a suitable viewpoint for observation, and ...
- **p. 4 / 3.3. Chain of Semantics Programming - extractive body cue:** We use the chain of semantics to guide the process of programming: \ mathcal {L }_p=\ text {programmer} \xleftarrow {\text {guide}} \mathcal {C}(\mathcal {U}) (11) ...
- **p. 3 / 3. Methodology - extractive body cue:** We then reconstruct the 3D scene using the 3DGS representation to enable exploration in 3D worlds and render free-viewing 2D images, as shown in Figure ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This method constructs a relationship graph and facilitates a chain of semantics programming, enabling multi-step object grounding. • We first use 3DGS to reconstruct the 3D representation, which enables interactive reasoning by ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| State/latent | constructs, relationship, graph, facilitates, chain, semantics, programming, enabling, multi-step, object, grounding, first | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.2. Dynamic Interaction in 3DGS Representation) |
| Output/action | Furthermore, the quality of 2D images derived from point clouds is frequently low or incomplete, hindering the extraction of clean, fine-grained semantics in diverse scenes and also limiting the reasoning of spatial ... | point map, pose, scene graph, affordance 또는 query result | p. 1 (1. Introduction), p. 4 (3.2. Dynamic Interaction in 3DGS Representation), p. 3 (3.2. Dynamic Interaction in 3DGS Representation) |
| Objective/outcome | For instance, if the user intends to locate a single object but two are returned, or if the execution yields no results (e.g., no object is located), or if syntax errors are ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.4. Grounded-aware Self-Check Mechanism), p. 5 (3.4. Grounded-aware Self-Check Mechanism) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are summarized as follows: • We propose a chain of semantics programming method with the grounded-aware self-check mechanism for enhanced grounded reasoning in ...
- **p. 2 / 1. Introduction - extractive body cue:** This method constructs a relationship graph and facilitates a chain of semantics programming, enabling multi-step object grounding. • We first use 3DGS to reconstruct the ...
- **p. 3 / 3. Methodology - extractive body cue:** In this section, we introduce our proposed zero-shot neurosymbolic framework that employs a LLM as a neurosymbolic function for object grounding.
- **p. 3 / 3. Methodology - extractive body cue:** To enhance the effectiveness and robustness of the programming and reasoning process, we propose a grounded-aware self-check mechanism that reflects on the reasoning results.
- **p. 5 / 3.3. Chain of Semantics Programming - extractive body cue:** Through the chain of semantics programming, our framework can explicitly account for the conditionality of relationships and connections among multiple relationships, utilizing fine-grained semantics and ...
- **p. 7 / 4.4. Ablation study - extractive body cue:** This mechanism achieves improvements of 4.5% on Nr3D and 1.8% on Sr3D.
- **p. 5 / 4.3. Comparison to Prior Works - extractive body cue:** In Table 2, we find that our method outperforms the current state-of-the-art zeroshot methods on the Nr3D dataset and approaches the performance of the best-supervised ...
- **p. 6 / 4.4. Ablation study - extractive body cue:** Utilizing only the Chain of Semantics on the Nr3D dataset results in an improvement of 2.2% compared to dialogue and 1.9% compared to programming.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.4. Ablation study), p. 5 (4.3. Comparison to Prior Works) |
| Embodiment/environment | Sr3D comprises 83.5K template-based utterances that leverage spatial relationships among fine-grained object classes to localize a referred object in a scene, and Nr3D includes 41.5K natural, free-form utterances collected by deploying ... | hardware/simulator version and reset protocol | p. 5 (4.1. Datasets), p. 7 (4.4. Ablation study) |
| Dataset/benchmark | In the context of object grounding through programming, the Chain of Semantics yields beneficial improvements across both datasets, particularly on Sr3D, where the gap between Easy and Hard samples reduces from 6.9% ... | role, split, size and leakage | p. 5 (4.1. Datasets), p. 7 (4.4. Ablation study), p. 7 (4.4. Ablation study), p. 5 (4.3. Comparison to Prior Works) |
| Metric | The introduction of this mechanism enhances the accuracy of the generated code and deepens the reasoning regarding spatial relationships 24566 | definition, denominator, direction and uncertainty | p. 7 (4.4. Ablation study), p. 6 (4.4. Ablation study), p. 7 (4.4. Ablation study) |
| Baseline/ablation | With limited train data for the supervised models, our zero-shot method outperforms all compared models in both two datasets, as shown in Figure 3. | fair input/data/compute/action matching | p. 5 (4.3. Comparison to Prior Works), p. 5 (4.3. Comparison to Prior Works), p. 7 (4.4. Ablation study) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** We show that chain of semantics programming enhances the understanding of complex spatial relationships, and the 3D Gaussian Splatting representation provides fine-grained 2D semantics, overcoming ...
- **p. 8 / 4.5. Qualitative results - extractive body cue:** The fifth image illustrates a failure case where dense object grounding becomes more prone to confusion, increasing the difficulty of grounding to the correct object.
- **p. 7 / 4.4. Ablation study - extractive body cue:** Without this mechanism, when errors occur during code execution, the only option is to reattempt reasoning, failing to learn from previous mistakes.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This oversight in capturing the connection and conditionality of spatial relationships results in a significant performance gap in grounding between these zero-shot methods and the current stateof-the-art supervised approaches.를 문제로 두고, Our contributions are summarized as follows: • We propose a chain of semantics programming method with the grounded-aware self-check mechanism for enhanced grounded reasoning in the 3DVG task. • We introduce a ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Dynamic Interaction in 3DGS Representation), p. 4 (3.3. Chain of Semantics Programming) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
