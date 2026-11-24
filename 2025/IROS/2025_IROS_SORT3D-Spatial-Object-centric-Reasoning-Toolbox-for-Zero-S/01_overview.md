# SORT3D: Spatial Object-centric Reasoning Toolbox for Zero-Shot 3D Grounding Using Large Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2504.18684.
> PDF retrieval source: https://arxiv.org/pdf/2504.18684. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / IROS
- Authors: Nader Zantout, Haochen Zhang, Pujith Kachana, Jinkai Qiu, Guofei Chen, Ji Zhang, Wenshan Wang
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://arxiv.org/abs/2504.18684
- Full-text retrieval: https://arxiv.org/pdf/2504.18684
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11246145)

## Why This Paper Is Here

SORT3D는 시점과 물체 속성이 포함된 자연어 지시를 공간 검색 함수로 풀어 미리 관측한 3D 장면에서 목표 물체를 선택한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11246145#page=1) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11246145#page=4)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Interpreting object-referential language and grounding objects in 3D with spatial relations and attributes is essential for robots operating alongside humans.
- **p. 1 / Abstract - extractive body cue:** However, this task is often challenging due to the diversity of scenes, large number of fine-grained objects, and complex free-form nature of language references.
- **p. 1 / Abstract - extractive body cue:** Furthermore, in the 3D domain, obtaining large amounts of natural language training data is difficult.
- **p. 1 / Abstract - extractive body cue:** Thus, it is important for methods to learn from little data and zero-shot generalize to new environments.
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we propose SORT3D, an approach that utilizes rich object attributes from 2D data and merges a heuristics-based spatial reasoning toolbox with ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Resolving natural language expressions referring to specific objects using semantic object attributes and inter-object spatial relations-the core challenge of 3D referential grounding-remains difficult despite being ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Second, training end-to-end learning-based methods on 3D referential grounding requires a large amount of annotated data aligning language references to a 3D scene, which the ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** To this end, we propose SORT3D, a Spatial Object-centric Reasoning Toolbox for 3D Grounding Using LLMs, shown.
- **p. 2 / I. INTRODUCTION - extractive body cue:** As a result, our method only requires a single in-context example of the toolbox usage and no other training data.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We evaluate our method on standard 3D object referential grounding benchmarks, ReferIt3D [1] and IRef-VLA [17], and demonstrate performance competitive with SOTA on complex view-dependent ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** This component is the only pipeine change required for our method to be deployed in the real-world.
- **p. 3 / III. METHODOLOGY - extractive body cue:** The input to the grounding pipeline consists of perception information from the scene and a free-form referring expression in natural language.
- **p. 3 / III. METHODOLOGY - extractive body cue:** Instance-level Semantic Mapping For our real-world experiments, we use an object instancelevel semantic mapping module running in real-time to obtain the 3D bounding boxes to ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Given an input command like "The nightstand to the right of the bed", the first query extracts object nouns and modifiers (e.g. nightstand and bed), ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** The usage of open-vocabulary 2D foundation models allows our semantic mapping module to generalize to new environments as we show in our real-world experiments (section ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3D referential grounding additionally acts as a precursor to downstream tasks such as object-goal navigation, multi-action instruction-following, and scene visual question answering (VQA). | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| State/latent | referential, grounding, additionally, acts, precursor, downstream, tasks, object-goal, navigation, multi-action, instruction-following, scene | geometry, map, object/relationship state | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Output/action | The input to the grounding pipeline consists of perception information from the scene and a free-form referring expression in natural language. | point map, pose, scene graph, affordance 또는 query result | p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |
| Objective/outcome | We use Qwen2-VL-7B [27] as our VLM as we found it to perform best in generating accurate and concise descriptions following our template, and the quantized version of Qwen2.5-VL-Instruct-3B for system deployment ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |

## Main Claims and Actual Contribution

- 여러 뷰의 물체 설명을 지도에 모으고, 언어 모델이 거리·방향·시점 관계에 맞는 검색 함수를 순차적으로 호출하게 한다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11246145#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11246145#page=4) · [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11246145#page=5)
- 3D 지시 대상 식별 벤치마크의 정확도를 평가하고 두 실제 이동 플랫폼에서 구축한 지도를 이용해 목표 물체로 이동하는 예를 제시했다. [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11246145#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11246145#page=7) · [PDF 8쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11246145#page=8)

## Evaluation Scope

실물 시연에서는 로봇이 먼저 환경을 주행해 지도를 만든 뒤 물체 지시를 받았다. 벤치마크의 지시 대상 식별 정확도와 두 이동 플랫폼의 내비게이션 시연은 별도 평가다. [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11246145#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11246145#page=7)

## Explicit Limitations and Failure Boundary

- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** We see that SORT3D is able to explainably resolve complex view-dependent relations with multiple anchors and complex semantic descriptions (Figure 4-a), while also providing explainable ...
- **p. 6 / V. RESULTS AND DISCUSSION - extractive body cue:** In the bottom right, the model fails at pragmatics, picking out the rightmost pillow, instead of recognizing that the sentence implies choosing a pillow on ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY)이다.
