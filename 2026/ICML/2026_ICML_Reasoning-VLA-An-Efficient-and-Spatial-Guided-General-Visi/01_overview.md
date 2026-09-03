# Reasoning-VLA: An Efficient and Spatial-Guided General Vision-Language-Action Reasoning Model for Autonomous Driving

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=0.917); canonical paper source: https://openreview.net/forum?id=c4iSIrb6Iv.
> PDF retrieval source: https://openreview.net/pdf/2958fe5249a1a673a414d689de7784b306b2a02a.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics, 3D Vision, Reinforcement Learning
- Official paper: https://openreview.net/forum?id=c4iSIrb6Iv
- Full-text retrieval: https://openreview.net/pdf/2958fe5249a1a673a414d689de7784b306b2a02a.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=0.917)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 2) Current VLA methods lack robust generalization to new vehicle platforms or unseen driving scenarios.를 문제로 두고, To summarize, the main contributions are as follows: • We propose Reasoning-VLA, an efficient and fast VLA framework that employs learnable action queries to interact with reasoning-enhanced vision-language representations, enabling one ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have recently shown strong decision-making capabilities in autonomous driving.
- **p. 1 / Abstract - extractive body cue:** However, existing VLAs often struggle with achieving efficient inference and generalizing to novel autonomous vehicle configurations and driving scenarios.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose Reasoning-VLA, a general and fast action-generation VLA framework.
- **p. 1 / Abstract - extractive body cue:** The proposed model employs a set of learnable action queries, initialized via Gaussian sampling from ground-truth trajectories within the training corpus.
- **p. 1 / Abstract - extractive body cue:** These learnable queries interact with reasoning-enhanced vision-language features to generate continuous action trajectories in parallel.
- **p. 1 / 1. Introduction - extractive body cue:** 2) Current VLA methods lack robust generalization to new vehicle platforms or unseen driving scenarios.
- **p. 1 / 1. Introduction - extractive body cue:** These limitations hinder their generalization ability to new driving scenarios.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, the main contributions are as follows: • We propose Reasoning-VLA, an efficient and fast VLA framework that employs learnable action queries to interact ...
- **p. 3 / 3. Method - extractive body cue:** In the following sections, we present a detailed description of our approach to developing a VLA framework for autonomous driving and highlight key insights.
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we propose ReasoningVLA, an efficient and generalist VLA framework that establishes a new state-of-the-art for autonomous driving.
- **p. 3 / 3. Method - extractive body cue:** 1, the Reasoning-VLA framework comprises three main components: (1) a reasoningenhanced vision-language model (VLM) backbone, (2) an action module that interacts with the VLM and ...
- **p. 4 / 3.5. Action Refinement Module - extractive body cue:** To further enhance the representation quality and accuracy of the predicted action trajectories, we introduce an Action Refinement Module (ARM).
- **p. 4 / 3.4. How Do Actions Interact with Vision-Language - extractive body cue:** Since the action queries are not tied to the VLM's token representations, they first perform self-attention and then interact with the VLM through cross-attention, as ...
- **p. 3 / 3. Method - extractive body cue:** Qwen2.5-VL incorporates several architectural innovations: a redesigned Vision Transformer (ViT) with 2D-RoPE and windowed attention for computational efficiency; an MLP-based vision-language merger that compresses visual ...
- **p. 3 / 3.2. The Structure of Reasoning-VLA - extractive body cue:** 1, the learnable action queries are designed with the same feature dimensionality as the Qwen2.5-VL reasoning model.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | VLM Question CoT Reasoning Prompt Refinement Parallel Action VLto A Interaction Ego Status Prompt ...... <answer></answer> N Hidden States Gaussian Distribution Initializing CoT Reasoning Text x1, y1, ...... xn, yn myvla Pipeline ... | image/video, language instruction, proprioception과 history | p. 2 (1. Introduction), p. 4 (3.5. Action Refinement Module) |
| State/latent | VLM, Question, CoT, Reasoning, Prompt, Refinement, Parallel, Action, VLto, Interaction, Ego, Status | language-grounded task state와 action-policy context | p. 2 (1. Introduction), p. 4 (3.5. Action Refinement Module), p. 3 (3.2. The Structure of Reasoning-VLA) |
| Output/action | Specifically, the ARM takes the selected hidden states of the action queries as input and refines them through a combination of multilayer perceptron (MLP) and attention mechanisms. | continuous action, pose 또는 action chunk | p. 4 (3.5. Action Refinement Module), p. 3 (3.2. The Structure of Reasoning-VLA), p. 4 (3.3.1. Learnable Action Queries) |
| Objective/outcome | This design establishes a dynamic constraint optimization objective that ensures physically feasible and stable motion trajectories. | instruction following, task success, generalization과 latency | p. 5 (3.7. Reward Functions), p. 5 (3.7. Reward Functions), p. 3 (3.2. The Structure of Reasoning-VLA) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, the main contributions are as follows: • We propose Reasoning-VLA, an efficient and fast VLA framework that employs learnable action queries to interact ...
- **p. 3 / 3. Method - extractive body cue:** In the following sections, we present a detailed description of our approach to developing a VLA framework for autonomous driving and highlight key insights.
- **p. 1 / 1. Introduction - extractive body cue:** To address these challenges, we propose ReasoningVLA, an efficient and generalist VLA framework that establishes a new state-of-the-art for autonomous driving.
- **p. 3 / 3. Method - extractive body cue:** 1, the Reasoning-VLA framework comprises three main components: (1) a reasoningenhanced vision-language model (VLM) backbone, (2) an action module that interacts with the VLM and ...
- **p. 4 / 3.5. Action Refinement Module - extractive body cue:** To further enhance the representation quality and accuracy of the predicted action trajectories, we introduce an Action Refinement Module (ARM).
- **p. 7 / 5.2.1. Open-loop Evaluation - extractive body cue:** As shown in the last row of Table 1, the additional fine-tuning further improves performance across all time intervals: Reasoning-VLA-7B+ achieves increases of 4.3% and ...
- **p. 7 / 5.2.1. Open-loop Evaluation - extractive body cue:** Reasoning-VLA-3B also achieves results comparable to state-of-the-art methods.
- **p. 6 / 4. Unified Datasets - extractive body cue:** To capture diverse driving scenarios and further improve generalization, we specifically selected eight widely used autonomous driving datasets as the foundation for our unified dataset: ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (5.2.1. Open-loop Evaluation), p. 7 (5.2.1. Open-loop Evaluation) |
| Embodiment/environment | When fine-tuned with GRPO on specific datasets (i.e., selected nuScenes training clips from the unified dataset), our generalized model demonstrates excellent task-specific performance. | hardware/simulator version and reset protocol | p. 7 (5.2.1. Open-loop Evaluation), p. 6 (4. Unified Datasets) |
| Dataset/benchmark | The open-loop performance on the nuScenes dataset is summarized in Table 1. | role, split, size and leakage | p. 7 (5.2.1. Open-loop Evaluation), p. 6 (4. Unified Datasets), p. 7 (5.2.1. Open-loop Evaluation), p. 8 (5.2.2. Closed-loop Evaluation) |
| Metric | Methods NeuroNCAP Score ↑ Collision Rate (%) ↓ Stationary Frontal Side Avg. | definition, denominator, direction and uncertainty | p. 7 (5.1. Experiment Setups), p. 7 (5.2.2. Closed-loop Evaluation), p. 8 (5.2.2. Closed-loop Evaluation) |
| Baseline/ablation | Reasoning-VLA-3B also achieves results comparable to state-of-the-art methods. | fair input/data/compute/action matching | p. 7 (5.2.1. Open-loop Evaluation), p. 7 (5.2.2. Closed-loop Evaluation), p. 8 (5.2.2. Closed-loop Evaluation) |

## Explicit Limitations and Failure Boundary

- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Statistical distribution of the unified dataset. However, these constraints exert a non-negligible influence on the vehicle's behavior and overall driving safety. To ad- ...
- **p. 7 / 5.1. Experiment Setups - extractive body cue:** Methods NeuroNCAP Score ↑ Collision Rate (%) ↓ Stationary Frontal Side Avg.
- **p. 7 / 5.2.2. Closed-loop Evaluation - extractive body cue:** The generalized model, Reasoning-VLA-7B, substantially outperforms prior methods in terms of NeuroNCAP Score and Collision Rate, achieving an average NeuroNCAP Score of 2.25 and an ...
- **p. 8 / 5.2.2. Closed-loop Evaluation - extractive body cue:** NAVSIM[9] 0.05 0.18 0.43 0.22 0.04 0.18 0.41 0.21 nuScenes[4] 0.06 0.23 0.48 0.26 0.05 0.20 0.44 0.23 Waymo[40] 0.04 0.15 0.44 0.21 0.03 0.14 ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 7. Generalization performance on the Open-loop Metrics. Methods L2 (m) ↓ Collision Rate (%) ↓ 1s 2s 3s Avg.
- **p. 8 / 5.2.3. Generalized Performance - extractive body cue:** These results indicate that our method maintains robust generalization across different driving scenarios and vehicle configurations.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 2) Current VLA methods lack robust generalization to new vehicle platforms or unseen driving scenarios.를 문제로 두고, To summarize, the main contributions are as follows: • We propose Reasoning-VLA, an efficient and fast VLA framework that employs learnable action queries to interact with reasoning-enhanced vision-language representations, enabling one ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.4. How Do Actions Interact with Vision-Language), p. 3 (3. Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
