# CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Jinming Li, Yichen Zhu, Zhibin Tang, Junjie Wen, Minjie Zhu, Xiaoyu Liu, Chengmeng Li, Ran Cheng, Yaxin Peng, Yan Peng, Feifei Feng
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html
- PDF title variant: CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance [원문 표제면](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf#page=1) · [공식 서지](https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html)
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

CoA-VLA는 행동을 예측하기 전에 대상 물체, 잡을 부분, 놓을 위치, 이동 경로를 시각·텍스트 단서로 표현한다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Robot foundation models, particularly Vision-LanguageAction (VLA) models, have garnered significant attention for their ability to enhance robot policy learning, greatly improving robot's generalization and robustness.
- **p. 1 / Abstract - extractive body cue:** OpenAI's recent model, O1, showcased impressive capabilities in solving complex problems by utilizing extensive reasoning chains.
- **p. 1 / Abstract - extractive body cue:** This prompts an important question: can robot models achieve better performance in multi-task, complex environments by reviewing prior observations and then providing task-specific reasoning to ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce Chain-of-Affordance (CoAVLA), a novel approach to scaling robot models by incorporating reasoning in the format of sequential robot affordances to ...
- **p. 1 / Abstract - extractive body cue:** Specifically, we prompt the model to consider the following four types of affordances before taking action: (1) object affordance - what object to manipulate and ...
- **p. 2 / 1. Introduction - extractive body cue:** However, current approaches often rely heavily on high-level planning or task decomposition by off-the-shelf Large language models(LLMs) or Vision language models (VLMs), limiting models from ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In this work, we propose Chain-of-Affordance, namely CoA-VLA, a novel perspective on generalizing model reasoning at test-time, and leverage such generated reasoning to facilitate the ...
- **p. 2 / 1. Introduction - extractive body cue:** Our method leverages visual affordance in robot learning, conceptualizing various actions and interactions with objects or the environment that a robot can perform based on ...
- **p. 3 / 4. Methodology - extractive body cue:** In Section 4.2, we present two formats for representing the chain of affordances: a text format and an image format.
- **p. 4 / 4.1. Definition of Chain-of-Affordance - extractive body cue:** In our framework, spatial affordance is operationalized as actionable destinations-discrete 2D coordinates representing feasible interaction zones.
- **p. 4 / 4.1. Definition of Chain-of-Affordance - extractive body cue:** By employing a dynamic affordance selection mechanism, our method avoids generating redundant affordances at every timestep. object to interact with and where it is located, ...
- **p. 5 / 4.1. Definition of Chain-of-Affordance - extractive body cue:** This module bridges the gap between abstract language-based reasoning and pixel-level visual context, enabling the policy model to synergistically leverage both modalities for robust, context-aware ...
- **p. 3 / 4. Methodology - extractive body cue:** We then discuss how these representations can be integrated into the policy learning process.
- **p. 5 / 4.1. Definition of Chain-of-Affordance - extractive body cue:** For textual affordances, we use the last embedding from the VLM models and add an MLP layer to tokenize it.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our objective is to learn an intermediate language output z : O ↑G ↓Z that maps observations and task descriptions to affordance reasoning in natural language. | image/video, language instruction, proprioception과 history | p. 3 (4.1. Definition of Chain-of-Affordance), p. 5 (4.1. Definition of Chain-of-Affordance) |
| State/latent | objective, learn, intermediate, language, output, maps, observations, task, descriptions, affordance, reasoning, natural | language-grounded task state와 action-policy context | p. 3 (4.1. Definition of Chain-of-Affordance), p. 5 (4.1. Definition of Chain-of-Affordance), p. 5 (4.1. Definition of Chain-of-Affordance) |
| Output/action | This module bridges the gap between abstract language-based reasoning and pixel-level visual context, enabling the policy model to synergistically leverage both modalities for robust, context-aware action generation. | continuous action, pose 또는 action chunk | p. 5 (4.1. Definition of Chain-of-Affordance), p. 5 (4.1. Definition of Chain-of-Affordance), p. 2 (1. Introduction) |
| Objective/outcome | Our objective is to learn an intermediate language output z : O ↑G ↓Z that maps observations and task descriptions to affordance reasoning in natural language. | instruction following, task success, generalization과 latency | p. 3 (4.1. Definition of Chain-of-Affordance), p. 4 (4.1. Definition of Chain-of-Affordance), p. 4 (4.1. Definition of Chain-of-Affordance) |

## Main Claims and Actual Contribution

- 네 종류의 행동 가능성을 순서대로 표현한 자료를 만들고 두 양식의 정보를 정책에 함께 제공하는 모듈을 학습했다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf#page=5)
- 실물 조작과 LIBERO에서 정책을 비교하고 시각 단서와 텍스트 단서를 각각 사용했을 때의 차이를 분석했다. [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 7 (5.2. Evaluation on Simulation), p. 7 (5.2. Evaluation on Simulation) |
| Embodiment/environment | LIBERO is a robot learning benchmark comprising over 130 language-conditioned manipulation tasks. | hardware/simulator version and reset protocol | p. 7 (5.2. Evaluation on Simulation), p. 7 (5. Experiments) |
| Dataset/benchmark | CoAVLA can avoid obstacles and operate safely. robot is presented with a plate on which three distinct objects are already placed, and it is instructed to add a piece of bread onto ... | role, split, size and leakage | p. 7 (5.2. Evaluation on Simulation), p. 7 (5. Experiments), p. 8 (5.3. More Experiments), p. 8 (5.3. More Experiments) |
| Metric | We report the success rate and standard error for four task suites. | definition, denominator, direction and uncertainty | p. 8 (5.3. More Experiments), p. 7 (5.2. Evaluation on Simulation), p. 8 (5.3. More Experiments) |
| Baseline/ablation | Compared to our baseline model, which employs vanilla reasoning, our method achieves a 14.29% increase in accuracy. | fair input/data/compute/action matching | p. 7 (5.1. Evaluation on Real Robot), p. 7 (5. Experiments), p. 8 (5.3. More Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5.3. More Experiments - extractive body cue:** Our approach successfully completed all three scenarios, demonstrating robust collision avoidance and spatial adaptability.
- **p. 8 / 5.3. More Experiments - extractive body cue:** Collision avoidance is essential for safe and effective physical interactions, as improper maneuvers can lead to significant damage or even catastrophic outcomes.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 5 (4.1. Definition of Chain-of-Affordance), p. 3 (4. Methodology), p. 3 (4.1. Definition of Chain-of-Affordance), p. 6 (4.3. Generating Chain-of-Affordance Data)이다.
