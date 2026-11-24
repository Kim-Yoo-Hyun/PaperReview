# Chain of Semantics Programming in 3D Gaussian Splatting Representation for 3D Vision Grounding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CVPR
- Authors: Jiaxin Shi, Mingyue Xiang, Hao Sun, Yixuan Huang, Zhi Weng
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, semantic, grounding
- Official paper: https://openaccess.thecvf.com/content/CVPR2025/html/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2025/papers/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2025/papers/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.pdf)

## Why This Paper Is Here

Chain-of-Semantics는 가우시안 장면에서 언어가 가리키는 물체를 찾기 위해 여러 뷰의 영상과 공간 관계를 순서대로 판별한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.pdf#page=3)

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

- 장면을 여러 시점에서 렌더링하고 관계 그래프와 언어 모델의 의미 단계를 이용해 후보를 좁힌 뒤 선택 결과를 자체 점검한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.pdf#page=5)
- Nr3D와 Sr3D에서 주석된 지시 대상의 식별 정확도를 비교하고 학습을 추가하지 않는 조건에서 공간 추론을 평가했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.pdf#page=6)

## Evaluation Scope

표 2·3에서 자체 점검을 포함한 방법의 정답 물체 식별 정확도는 Nr3D 60.8%, Sr3D 91.4%다. 두 값의 단위는 지시 표현에서 맞는 물체를 선택한 비율이다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2025/papers/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.pdf#page=6)

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** We show that chain of semantics programming enhances the understanding of complex spatial relationships, and the 3D Gaussian Splatting representation provides fine-grained 2D semantics, overcoming ...
- **p. 8 / 4.5. Qualitative results - extractive body cue:** The fifth image illustrates a failure case where dense object grounding becomes more prone to confusion, increasing the difficulty of grounding to the correct object.
- **p. 7 / 4.4. Ablation study - extractive body cue:** Without this mechanism, when errors occur during code execution, the only option is to reattempt reasoning, failing to learn from previous mistakes.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.2. Dynamic Interaction in 3DGS Representation), p. 4 (3.3. Chain of Semantics Programming)이다.
