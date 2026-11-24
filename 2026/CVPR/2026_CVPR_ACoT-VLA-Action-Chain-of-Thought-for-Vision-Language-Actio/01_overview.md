# ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhong_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhong_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Linqing Zhong, Yi Liu, Yifei Wei, Ziyu Xiong, Si Liu, Guanghui Ren
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Chain-of-Thought, Planning
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Zhong_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhong_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf
- Code/Project: https://github.com/AgibotTech/ACoT-VLA
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhong_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf) 기준이다.

## Why This Paper Is Here

ACoT-VLA는 행동 공간에서 먼저 거친 기준 궤적을 추론하고 이를 이용해 로봇이 실행할 세밀한 행동을 생성한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhong_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action models have emerged as essential generalist robot policies for diverse manipulation tasks, conventionally relying on directly translating multimodal inputs into actions via Vision-Language Model ...
- **p. 1 / Abstract - extractive body cue:** Recent advancements have introduced explicit intermediary reasoning-such as sub-task prediction (language) or goal image synthesis (vision)-to guide action generation.
- **p. 1 / Abstract - extractive body cue:** However, these intermediate reasoning are often indirect and inherently limited in their capacity to convey the full, granular information required for precise action execution.
- **p. 1 / Abstract - extractive body cue:** Instead, we posit that the most effective form of reasoning is one that deliberates directly in the action space.
- **p. 1 / Abstract - extractive body cue:** We introduce Action Chain-of-Thought (ACoT), a paradigm where the reasoning process itself is formulated as a structured sequence of coarse action intents that guide the ...
- **p. 2 / 1. Introduction - extractive body cue:** This foundational shift, however, introduces a critical and distinct research challenge: How can we robustly and efficiently synthesize the complex, high-dimensional motion cues required for ...
- **p. 1 / 1. Introduction - extractive body cue:** Despite the promising trajectory set by these paradigms, a critical challenge persists: existing generalist policies think predominantly in the vision-language (input) space, often failing to ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our main contributions are as follows: • Conceptually, we introduce Action Chain of Thought (ACoT), a new paradigm for generalist robot policies.
- **p. 2 / 1. Introduction - extractive body cue:** Subsequently, through jointly leveraging both EAR and IAR, we develop ACoT-VLA, an integrated Action Chain-of-Thought framework that enables grounded generalist robot policy learning.
- **p. 3 / 3. Methodology - extractive body cue:** The core of our method lies in two distinct action reasoners introduced in Sec.
- **p. 3 / 3. Methodology - extractive body cue:** In this section, we present a detailed investigation into how to generate effective action space guidance and integrate it into robotic policy learning.
- **p. 4 / 3.3. Implicit Action Reasoner - extractive body cue:** To this end, we introduce an Implicit Action Reasoner (IAR), which directly operates on the VLM's key-value cache.
- **p. 4 / 3.4. Action-Guided Prediction - extractive body cue:** Building upon the explicit action embedding Zex produced by EAR and implicit action-related feature Zim obtained in IAR, in this section, we introduce the Action-Guided ...
- **p. 4 / 3.3. Implicit Action Reasoner - extractive body cue:** (8) Then, through aggregating these representations across layers, we obtain implicit action-related feature Zim, which serves as implicit action-space guidance gim action, complementing the explicit ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** Given a natural language instruction l and current visual observation ot, the generalist robot policy πθ aims to predict action sequences at:t+H-1 that accomplishes the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (a) Pre-trained VLM Action Policy Instruction Sub-tasks Observation Actions (b) World Model Action Policy Instruction Goal-image Observation Actions (c) Pre-trained VLM Action Policy Instruction Observation Actions Reference Actions Fig ... | image/video, language instruction, proprioception과 history | p. 1 (1. Introduction), p. 3 (3.1. Problem Formulation) |
| State/latent | Pre-trained, VLM, Action, Policy, Instruction, Sub-tasks, Observation, Actions, World, Model, Goal-image, Reference | language-grounded task state와 action-policy context | p. 1 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 2 (1. Introduction) |
| Output/action | Given a natural language instruction l and current visual observation ot, the generalist robot policy πθ aims to predict action sequences at:t+H-1 that accomplishes the specified task. | continuous action, pose 또는 action chunk | p. 3 (3.1. Problem Formulation), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | The entire framework is optimized under a standard flow-matching mean-squared error (MSE) objective. | instruction following, task success, generalization과 latency | p. 5 (3.4. Action-Guided Prediction), p. 5 (3.4. Action-Guided Prediction), p. 4 (3.2. Explicit Action Reasoner) |

## Main Claims and Actual Contribution

- 명시적 추론기가 제안한 기준 궤적과 암시적 행동 표현을 결합해 최종 행동 생성을 안내한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhong_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhong_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf#page=4)
- LIBERO 계열과 VLABench, 실물 조작에서 성공률을 비교하고 행동 수준의 중간 추론이 주는 효과를 분석했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhong_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhong_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhong_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhong_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.4. Real-World Deployment), p. 6 (4.2. Simulation Experiments) |
| Embodiment/environment | For simulation experiments, we strictly follow the official training splits provided by the corresponding benchmark (LIBERO [32], LIBERO-Plus [15], and VLABench [58]), and train our models exclusively on their standard demonstration dat ... | hardware/simulator version and reset protocol | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Dataset/benchmark | We evaluate our approach on LIBERO benchmark, which targets four distinct robot capabilities: spatial awareness (Spatial), object manipulation (Object), goal completion (Goal), and long-horizon reasoning (Long). | role, split, size and leakage | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Simulation Experiments), p. 7 (4.2. Simulation Experiments) |
| Metric | Furthermore, our method maintains exceptional performance under the Supervised Fine-Tuning setting, reaching an 88.0% average success rate. | definition, denominator, direction and uncertainty | p. 7 (4.2. Simulation Experiments), p. 7 (4.3. Ablation Study), p. 8 (4.4. Real-World Deployment) |
| Baseline/ablation | Table 6. Comparison of KV-cache interaction strategies in IAR. shown in Table 4, Table 5, and Table 6. Note that we adopt π0.5 as the "Baseline" method. More ablations in different benchmarks ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 8 (4.3. Ablation Study), p. 6 (4.2. Simulation Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.2. Simulation Experiments - extractive body cue:** Concretely, LIBERO-Plus introduces 7 perturbation dimensions, i.e., camera-viewpoints (Camera), robot-initialstates (Robot), language-variations (Language), lightingconditions (Light), background-textures (Background), sensor-noise (Noi ...
- **p. 7 / 4.2. Simulation Experiments - extractive body cue:** Specifically, under the Zero-Shot regime, our approach demonstrates pronounced robustness against distribution shifts such as robot initial-state perturbations (+3.2%) and language variations (+4.2%), where existing ...
- **p. 6 / 4.2. Simulation Experiments - extractive body cue:** Through leveraging actions as intermediate reasoning, the model feeds the action head with structured action guidance, which significantly enhances the robustness in long-horizon manipulation tasks.
- **p. 7 / 4.2. Simulation Experiments - extractive body cue:** These results highlight the effectiveness of our action-space reasoning in improving generalization and robust policy learning.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 4 (3.4. Action-Guided Prediction)이다.
