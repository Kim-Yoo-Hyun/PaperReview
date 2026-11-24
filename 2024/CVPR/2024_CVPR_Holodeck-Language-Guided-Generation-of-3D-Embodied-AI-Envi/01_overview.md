# Holodeck: Language Guided Generation of 3D Embodied AI Environments

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: Yue Yang, Fan-Yun Sun, Luca Weihs, Eli Vanderbilt, Alvaro Herrasti, Winson Han, Jiajun Wu, Nick Haber, Ranjay Krishna, Lingjie Liu, Chris Callison-Burch, Mark Yatskar, Aniruddha Kembhavi, Christopher Clark
- 저자 판본: CVPR 게재본 표제면의 네 번째 저자 Eli Vanderbilt 표기를 반영했다. [표제면](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf#page=1) · [학회 서지](https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.html)
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Generation, 3D scene, Embodied AI
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf)

## Why This Paper Is Here

Holodeck은 자연어로 묘사한 실내 환경을 물체 자산과 공간 제약을 갖춘 상호작용 가능한 시뮬레이션 장면으로 생성한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D simulated environments play a critical role in Embodied AI, but their creation requires expertise and extensive manual effort, restricting their diversity and scope.
- **p. 1 / Abstract - extractive body cue:** To mitigate this limitation, we present HOLODECK, a system that generates 3D environments to match a user-supplied prompt fully automatedly.
- **p. 1 / Abstract - extractive body cue:** HOLODECK can generate diverse scenes, e.g., arcades, spas, and museums, adjust the designs for *Equal technical contribution.
- **p. 1 / Abstract - extractive body cue:** HOLODECK leverages a large language model (i.e., GPT-4) for common sense knowledge about what the scene might look like and uses a large collection of ...
- **p. 1 / Abstract - extractive body cue:** To address the challenge of positioning objects correctly, we prompt GPT-4 to generate spatial relational constraints between objects and then optimize the layout to satisfy ...
- **p. 2 / 1. Introduction - extractive body cue:** However, these models often produce scenes with significant artifacts, such as mesh distortions, and lack the interactivity necessary for Embodied AI.
- **p. 2 / 1. Introduction - extractive body cue:** To move beyond these limitations, recent works adapt 2D foundational models to generate 3D scenes from text [10, 16, 53].

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are three-fold: (1) We propose HOLODECK, a language-guided system capable of generating diverse, customized, and interactive 3D environments based on textual ...
- **p. 2 / 1. Introduction - extractive body cue:** In light of these challenges, we present HOLODECK, a language-guided system built upon AI2-THOR [23], to automatically generate diverse, customized, and interactive 3D embodied environments ...
- **p. 5 / 3. HOLODECK - extractive body cue:** To address this, instead of letting LLM directly operate on numerical values, we propose a novel constraint-based approach that employs LLM to generate spatial relations ...
- **p. 1 / Abstract - extractive body cue:** To mitigate this limitation, we present HOLODECK, a system that generates 3D environments to match a user-supplied prompt fully automatedly.
- **p. 3 / 3. HOLODECK - extractive body cue:** In the following sections, we introduce our prompting approach that converts high-level user natural language specifications into a series of language model queries for constructing ...
- **p. 5 / 3. HOLODECK - extractive body cue:** The algorithm first uses LLM to identify an anchor object and then explores placements for the anchor object.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Example outputs of HOLODECK-a large language model powered system, which can generate diverse types of environments (arcade, spa, museum), customize for styles (Victorian-style), and understand ...
- **p. 3 / 3. HOLODECK - extractive body cue:** We then provide a detailed overview of each module shown in Figure 2 and how they contribute to the final scene.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Example outputs of HOLODECK-a large language model powered system, which can generate diverse types of environments (arcade, spa, museum), customize for styles (Victorian-style), and understand fine-grained requirements ("has a cat", "f ... | camera/depth stream, pose, map와 language goal | p. 1 (Body text (section not recovered)), p. 4 (3. HOLODECK) |
| State/latent | Example, outputs, HOLODECK-a, large, language, model, powered, system, generate, diverse, types, environments | robot pose, free-space/semantic map와 local goal | p. 1 (Body text (section not recovered)), p. 4 (3. HOLODECK), p. 2 (Abstract) |
| Output/action | An LLM prompt is designed for each module with three elements: (1) Task Description: outlines the context and goals of the task; (2) Output Format: specifies the expected structure and type of ... | collision-free trajectory 또는 velocity command | p. 4 (3. HOLODECK), p. 2 (Abstract), p. 2 (1. Introduction) |
| Objective/outcome | To address the challenge of positioning objects correctly, we prompt GPT-4 to generate spatial relational constraints between objects and then optimize the layout to satisfy those constraints. | goal reach, safety, localization error와 replanning latency | p. 1 (Abstract), p. 2 (1. Introduction), p. 5 (3. HOLODECK) |

## Main Claims and Actual Contribution

- 언어 모델로 평면도와 배치 제약을 만들고 자산을 검색해 물체끼리의 관계와 제약을 고려한 배치를 구한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf#page=5)
- 사람의 장면 선호 평가와 생성한 장면을 사용한 물체 목표 내비게이션의 시뮬레이션 일반화를 각각 측정했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf#page=8)

## Evaluation Scope

사람의 선호와 에이전트 성능은 별도 실험이다. NOVELTYTHOR 시뮬레이션의 ObjectNav 표 2에서 ProcTHOR 사전학습 후 Holodeck으로 미세조정한 모델의 평균 성공률은 20.40%, SPL은 0.127이다. [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Yang_Holodeck_Language_Guided_Generation_of_3D_Embodied_AI_Environments_CVPR_2024_paper.pdf#page=8)

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.3. Ablation Study on Layout Design - extractive body cue:** The ABSOLUTE method performs no better than RANDOM due to its tendency to create scenes with collision and boundary errors (see examples in the supplement), ...
- **p. 7 / 4.3. Ablation Study on Layout Design - extractive body cue:** We present humans with four shuffled top-down images from each layout strategy and ask them to rank the four layouts considering out-of-boundary, object collision, reachable ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 5 (3. HOLODECK), p. 3 (3. HOLODECK), p. 1 (Body text (section not recovered))이다.
