# VIMA: Robot Manipulation with Multimodal Prompts

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v202/jiang23b.html.
> PDF retrieval source: https://arxiv.org/pdf/2210.03094. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / ICML
- Authors: Yunfan Jiang, Agrim Gupta, Zichen Zhang, Guanzhi Wang, Yongqiang Dou, Yanjun Chen, Li Fei-Fei, Anima Anandkumar, Yuke Zhu, Linxi Fan
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Vision-Language-Action, Imitation Learning, Robotics
- Official paper: https://proceedings.mlr.press/v202/jiang23b.html
- Full-text retrieval: https://arxiv.org/pdf/2210.03094
- Code/Project: https://vimalabs.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 4. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Why This Paper Is Here

문제 관련 발췌 — To enable a single agent with all these capabilities, we make three key contributions in this work: 1) a novel multimodal prompting formulation that converts a wide spectrum of robot manipulation tasks ...

방법 관련 발췌 — To enable a single agent with all these capabilities, we make three key contributions in this work: 1) a novel multimodal prompting formulation that converts a wide spectrum of robot manipulation tasks ...

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Prompt-based learning has emerged as a successful paradigm in natural language processing, where a single general-purpose language model can be instructed to perform any task ...
- **p. 1 / Abstract - extractive body cue:** Yet task specification in robotics comes in various forms, such as imitating oneshot demonstrations, following language instructions, and reaching visual goals.
- **p. 1 / Abstract - extractive body cue:** They are often considered different tasks and tackled by specialized models.
- **p. 1 / Abstract - extractive body cue:** We show that a wide spectrum of robot manipulation tasks can be expressed with multimodal prompts, interleaving textual and visual tokens.
- **p. 1 / Abstract - extractive body cue:** Accordingly, we develop a new simulation benchmark that consists of thousands of procedurally-generated tabletop tasks with multimodal prompts, 600K+ expert trajectories for imitation learning, and ...
- **p. 1 / 1. Introduction - extractive body cue:** To enable a single agent with all these capabilities, we make three key contributions in this work: 1) a novel multimodal prompting formulation that converts ...
- **p. 2 / 1. Introduction - extractive body cue:** We introduce VIMA, an embodied agent capable of processing mulitimodal prompts (left) and controlling a robot arm to solve the task (right). procedures (Aceituno et ...

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** To enable a single agent with all these capabilities, we make three key contributions in this work: 1) a novel multimodal prompting formulation that converts ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we introduce the VisuoMotor Attention agent (VIMA) to learn robot manipulation from multimodal prompts.
- **p. 2 / 1. Introduction - extractive body cue:** We introduce VIMA, an embodied agent capable of processing mulitimodal prompts (left) and controlling a robot arm to solve the task (right). procedures (Aceituno et ...
- **p. 1 / Abstract - extractive body cue:** Accordingly, we develop a new simulation benchmark that consists of thousands of procedurally-generated tabletop tasks with multimodal prompts, 600K+ expert trajectories for imitation learning, and ...
- **p. 3 / 6. Visual reasoning - extractive body cue:** (2020), which consists of primitive motor skills like "pick and place" and "wipe".
- **p. 4 / 4. Novel task generalization. New tasks with novel - extractive body cue:** To learn an effective multi-task robot policy, we propose VIMA, a robot agent with a multi-task encoderdecoder architecture and object-centric design (Fig.
- **p. 6 / 5.1. Baselines - extractive body cue:** Because there is no prior method that works out of the box with our multimodal prompting setup, we make our best effort to select a ...
- **p. 2 / 1. Introduction - extractive body cue:** The model architecture follows the encoderdecoder transformer design proven to be effective and scalable in NLP (Raffel et al., 2020).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 정책은 multimodal prompt P와 관측·행동 이력 H=[o₁,a₁,o₂,a₂,…,oₜ]에 조건화된다. | Prompt와 object-centric visual tokens 및 interaction history | PDF p. 4, §4 / Fig. 3; DOC-QA2 |
| State/latent | Concretely, learn, robot, policy, at/P, where, denotes, past, interaction, history, observations, actions | language-grounded task state와 action-policy context | p. 4 (4. Novel task generalization. New tasks with novel), p. 2 (1. Introduction), p. 6 (5.1. Baselines) |
| Output/action | VIMA encodes an input sequence of interleaving textual and visual prompt tokens with a pre-trained language model (Tsimpoukelli et al., 2021) and decodes robot control actions autoregressively for each environment interaction step. | continuous action, pose 또는 action chunk | p. 2 (1. Introduction), p. 6 (5.1. Baselines), p. 1 (1. Introduction) |
| Objective/outcome | We follow behavioral cloning to train our models by minimizing the negative log-likelihood of predicted actions. | instruction following, task success, generalization과 latency | p. 5 (4. Novel task generalization. New tasks with novel), p. 1 (1. Introduction), p. 1 (1. Introduction) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** To enable a single agent with all these capabilities, we make three key contributions in this work: 1) a novel multimodal prompting formulation that converts ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we introduce the VisuoMotor Attention agent (VIMA) to learn robot manipulation from multimodal prompts.
- **p. 2 / 1. Introduction - extractive body cue:** We introduce VIMA, an embodied agent capable of processing mulitimodal prompts (left) and controlling a robot arm to solve the task (right). procedures (Aceituno et ...
- **p. 1 / Abstract - extractive body cue:** Accordingly, we develop a new simulation benchmark that consists of thousands of procedurally-generated tabletop tasks with multimodal prompts, 600K+ expert trajectories for imitation learning, and ...
- **p. 3 / 6. Visual reasoning - extractive body cue:** (2020), which consists of primitive motor skills like "pick and place" and "wipe".
- **p. 6 / 5.2. Evaluation Results - extractive body cue:** Although models like VIMA-Gato and VIMA-Flamingo show improved performance with bigger model sizes, VIMA consistently achieves superior performance over all model sizes.
- **p. 6 / 5.2. Evaluation Results - extractive body cue:** We note that this can only be achieved with both cross-attention and object token sequence representations - altering any component will significantly degrade the performance, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4: Scaling model and data. Top: We compare performance of different methods with model sizes ranging from 2M to 200M parameters. Across all model ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (5.2. Evaluation Results), p. 6 (5.2. Evaluation Results) |
| Embodiment/environment | We compare VIMA against the baseline variants on four levels of generalization provided in our benchmark for different model and training dataset sizes. | hardware/simulator version and reset protocol | p. 6 (5.2. Evaluation Results), p. 7 (5.2. Evaluation Results) |
| Dataset/benchmark | VIMA: General Robot Manipulation with Multimodal Prompts Ours ViT Object Perceiver Perceiver Image Perceiver Image Patches ViT Perceiver Single Image ViT Ours (Oracle) ViT L1 L2 L3 L4 0 10 20 30 ... | role, split, size and leakage | p. 6 (5.2. Evaluation Results), p. 7 (5.2. Evaluation Results), p. 7 (5.2. Evaluation Results), p. 6 (5.2. Evaluation Results) |
| Metric | VIMA: General Robot Manipulation with Multimodal Prompts Ours ViT Object Perceiver Perceiver Image Perceiver Image Patches ViT Perceiver Single Image ViT Ours (Oracle) ViT L1 L2 L3 L4 0 10 20 30 ... | definition, denominator, direction and uncertainty | p. 7 (5.2. Evaluation Results), p. 6 (5.2. Evaluation Results), p. 6 (5.2. Evaluation Results) |
| Baseline/ablation | Figure 4: Scaling model and data. Top: We compare performance of different methods with model sizes ranging from 2M to 200M parameters. Across all model sizes and generalization levels, VIMA outperforms baseline ... | fair input/data/compute/action matching | p. 5 (Figure/Table caption), p. 7 (5.2. Evaluation Results), p. 6 (5.2. Evaluation Results) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Multimodal prompts for task specification. We observe that many robot manipulation tasks can be expressed as multimodal prompts that interleave language and image/video ...
- **p. 9 / 7. Conclusion - extractive body cue:** Therefore, we recommend our agent design as a solid starting point for future work.
- **p. 6 / 5.2. Evaluation Results - extractive body cue:** We note that this can only be achieved with both cross-attention and object token sequence representations - altering any component will significantly degrade the performance, ...
- **p. 7 / 5.2. Evaluation Results - extractive body cue:** In contrast, the baselines can degrade as much as 20%, particularly in more difficult generalization scenarios.
- **p. 7 / 5.2. Evaluation Results - extractive body cue:** These results suggest that VIMA has developed a more generalizable policy and robust representations than the alternative approaches.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (4. Novel task generalization. New tasks with novel), p. 6 (5.1. Baselines)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (48 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** To enable a single agent with all these capabilities, we make three key contributions in this work: 1) a novel multimodal prompting formulation that converts a wide spectrum of robot ... (p. 1, 1. Introduction).
- **Actual contribution:** To enable a single agent with all these capabilities, we make three key contributions in this work: 1) a novel multimodal prompting formulation that converts a wide spectrum of robot ... (p. 1, 1. Introduction).
- **Evaluation boundary:** Figure 4: Scaling model and data. Top: We compare performance of different methods with model sizes ranging from 2M to 200M parameters. Across all model sizes and generalization levels, VIMA ... (p. 5, Figure/Table caption).
- **Explicit failure boundary:** To make VIMA robust to detection inaccuracies and failures, we apply object augmentation by randomly injecting false-positive detection outputs. (p. 5, 4. Novel task generalization. New tasks with novel).
