# ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=72UR53jN7T.
> PDF retrieval source: https://arxiv.org/pdf/2507.16815. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model
- Official paper: https://openreview.net/forum?id=72UR53jN7T
- Full-text retrieval: https://arxiv.org/pdf/2507.16815
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 While this manner enables long-form reasoning without step-level supervision, the reliance on QA-style reward signals limits their ability to support long-horizon planning and makes it difficult to connect reasoning with real-world acti ...를 문제로 두고, Our main contributions are summarized as follows: • We propose ThinkAct, a dual-system framework that mutually enhances action execution and visualgrounded embodied reasoning connected by visual latent planning. • We leverage the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-language-action (VLA) reasoning tasks require agents to interpret multimodal instructions, perform long-horizon planning, and act adaptively in dynamic environments.
- **p. 1 / Abstract - extractive body cue:** Existing approaches typically train VLA models in an end-to-end fashion, directly mapping inputs to actions without explicit reasoning, which hinders their ability to plan over ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose ThinkAct, a dual-system framework that bridges high-level reasoning with low-level action execution via reinforced visual latent planning.
- **p. 1 / Abstract - extractive body cue:** ThinkAct trains a multimodal LLM to generate embodied reasoning plans guided by reinforcing action-aligned visual rewards based on goal completion and trajectory consistency.
- **p. 1 / Abstract - extractive body cue:** These reasoning plans are compressed into a visual plan latent that conditions a downstream action model for robust action execution on target environments.
- **p. 2 / 1. Introduction - extractive body cue:** While this manner enables long-form reasoning without step-level supervision, the reliance on QA-style reward signals limits their ability to support long-horizon planning and makes it ...
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** To tackle this problem, we propose ThinkAct, a unified framework that aims to leverage an MLLM ℱ𝜃to reason the high-level plans while connecting with an ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We propose ThinkAct, a dual-system framework that mutually enhances action execution and visualgrounded embodied reasoning connected by ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose ThinkAct, which aims to enable MLLMs with the capability to reason before acting in physical environments.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** To tackle this problem, we propose ThinkAct, a unified framework that aims to leverage an MLLM ℱ𝜃to reason the high-level plans while connecting with an ...
- **p. 4 / 3.2. Reinforced Visual Latent Planning for Embodied Reasoning - extractive body cue:** As a result, to encourage the model to anticipate visual goal completetion, we introduce the goal reward for comparing predicted start and end positions with ...
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** Note that, during inference, 𝜋𝜑and ℱ𝜃could operate asynchronously to enable slow thinking and fast control for VLA reasoning tasks. our ThinkAct enables long-horizon reasoning and ...
- **p. 6 / 3.4. Learning Strategy and Inference - extractive body cue:** During reasoning-enhanced action adaptation, we freeze ℱ𝜃while updating the action model 𝜋𝜑with state encoder and latent projector on the target environment by conditioning on the ...
- **p. 6 / 3.4. Learning Strategy and Inference - extractive body cue:** At inference time, given a visual observation 𝑜𝑡and instruction 𝑙, ThinkAct produces a visual plan latent 𝑐𝑡= ℱ𝜃(𝑜𝑡, 𝑙), which conditions the action module 𝜋𝜑to ...
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** 2. then put the picked strawberry ... </think> <answer> </answer> Reasoning MLLM "Put the strawberry in the drawer." Action Model Action-Aligned Visual Reward GRPO Optimization ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (2023)), which predicts actions based on the current state composed of visual observations and language instructions. | image/video, language instruction, proprioception과 history | p. 5 (3.3. Reasoning-Enhanced Action Adaptation), p. 3 (3.1. Problem Formulation) |
| State/latent | predicts, actions, current, state, composed, visual, observations, language, instructions, timestep, model, receives | language-grounded task state와 action-policy context | p. 5 (3.3. Reasoning-Enhanced Action Adaptation), p. 3 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation) |
| Output/action | At each timestep 𝑡, the model receives a visual observation 𝑜𝑡and a textual instruction 𝑙, with the goal of predicting an action 𝑎𝑡, which can be a textual command or a 7-DOF ... | continuous action, pose 또는 action chunk | p. 3 (3.1. Problem Formulation), p. 4 (3.1. Problem Formulation), p. 6 (3.4. Learning Strategy and Inference) |
| Objective/outcome | Thus, we optimize ℱ𝜃by maximizing the following objective: 𝒥GRPO(𝜃) = 1 𝑀 𝑀 ∑︁ 𝑖=1 ( ℱ𝜃(𝑧𝑖/𝑜𝑡, 𝑙) ℱ𝜃old(𝑧𝑖/𝑜𝑡, 𝑙)𝐴𝑖-𝛽𝐷𝐾𝐿(ℱ𝜃(𝑧𝑖/𝑜𝑡, 𝑙) ‖ ℱ𝜃old(𝑧𝑖/𝑜𝑡, 𝑙))), (4) where 𝐴𝑖= 𝑟𝑖-mean({𝑟1, . . . , ... | instruction following, task success, generalization과 latency | p. 5 (3.2. Reinforced Visual Latent Planning for Embodied Reasoning), p. 4 (3.1. Problem Formulation), p. 5 (3.2. Reinforced Visual Latent Planning for Embodied Reasoning) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We propose ThinkAct, a dual-system framework that mutually enhances action execution and visualgrounded embodied reasoning connected by ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose ThinkAct, which aims to enable MLLMs with the capability to reason before acting in physical environments.
- **p. 3 / 3.1. Problem Formulation - extractive body cue:** To tackle this problem, we propose ThinkAct, a unified framework that aims to leverage an MLLM ℱ𝜃to reason the high-level plans while connecting with an ...
- **p. 4 / 3.2. Reinforced Visual Latent Planning for Embodied Reasoning - extractive body cue:** As a result, to encourage the model to anticipate visual goal completetion, we introduce the goal reward for comparing predicted start and end positions with ...
- **p. 4 / 3.1. Problem Formulation - extractive body cue:** Note that, during inference, 𝜋𝜑and ℱ𝜃could operate asynchronously to enable slow thinking and fast control for VLA reasoning tasks. our ThinkAct enables long-horizon reasoning and ...
- **p. 7 / 4.2. Quantitative Evaluation - extractive body cue:** On the LIBERO benchmark, ThinkAct achieves the best overall success rate of 84.4%, outperforming DiT-Policy and recent state-of-the-art CoT-VLA Zhao et al.
- **p. 10 / 4.5. Analysis of ThinkAct - extractive body cue:** 5, ThinkAct consistently outperforms state-of-the-art methods, achieving the highest success rates across all tasks.
- **p. 10 / 4.4. Ablation Study - extractive body cue:** Method SimplerEnv EgoPlan RoboVQA ThinkAct (Ours) 60.1 48.2 59.8 Ours w/o 𝑟traj 59.2 47.9 58.5 Ours w/o 𝑟goal 59.1 47.6 58.9 Ours w/o 𝑟traj, 𝑟goal ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.2. Quantitative Evaluation), p. 10 (4.5. Analysis of ThinkAct) |
| Embodiment/environment | Okay, I'm ready to give the final trajectory: move to eggplant, lift it, and place it in basket. </think> "Pick up the book and place it in the back compartm." "Put eggplant ... | hardware/simulator version and reset protocol | p. 8 (4.2. Quantitative Evaluation), p. 6 (4.1. Experimental Setup) |
| Dataset/benchmark | We evaluate ThinkAct on two robot manipulation and three embodied reasoning benchmarks. | role, split, size and leakage | p. 8 (4.2. Quantitative Evaluation), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 10 (4.5. Analysis of ThinkAct) |
| Metric | (2023) with long-horizon tasks are evaluated using task success rate. | definition, denominator, direction and uncertainty | p. 6 (4.1. Experimental Setup), p. 7 (4.2. Quantitative Evaluation), p. 10 (4.5. Analysis of ThinkAct) |
| Baseline/ablation | On the LIBERO benchmark, ThinkAct achieves the best overall success rate of 84.4%, outperforming DiT-Policy and recent state-of-the-art CoT-VLA Zhao et al. | fair input/data/compute/action matching | p. 7 (4.2. Quantitative Evaluation), p. 7 (4.2. Quantitative Evaluation), p. 10 (4.5. Analysis of ThinkAct) |

## Explicit Limitations and Failure Boundary

- **p. 11 / 5. Conclusion - extractive body cue:** Through extensive experiments across embodied reasoning and robot manipulation benchmarks, we demonstrated strong long-horizon planning, few-shot adaptation, and emergent behaviors such as failure detection and ...
- **p. 12 / 5. Conclusion - extractive body cue:** (2023) The RoboFail dataset captures robot manipulation failures in both simulation and real-world scenarios.
- **p. 12 / 5. Conclusion - extractive body cue:** It includes 100 simulated failure cases in the AI2THOR environment and 30 real-world cases collected via UR5e teleoperation.
- **p. 15 / 5. Conclusion - extractive body cue:** The MLLM detects the failure and replans the pickup, leading to successful completion.
- **p. 11 / 4.5. Analysis of ThinkAct - extractive body cue:** Reasoning Elicit Self-Correction Failure detection and self-correction are critical for robust robot manipulation Liu et al.
- **p. 15 / 5. Conclusion - extractive body cue:** A8(a), the robot fails to grasp a mug.
- **p. 10 / 4.4. Ablation Study - extractive body cue:** The reasoning MLLM identifies the failure and generates a revised plan that guides the gripper back to regrasp the object.

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 While this manner enables long-form reasoning without step-level supervision, the reliance on QA-style reward signals limits their ability to support long-horizon planning and makes it difficult to connect reasoning with real-world acti ...를 문제로 두고, Our main contributions are summarized as follows: • We propose ThinkAct, a dual-system framework that mutually enhances action execution and visualgrounded embodied reasoning connected by visual latent planning. • We leverage the ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 3 (3.1. Problem Formulation), p. 6 (3.4. Learning Strategy and Inference), p. 6 (3.4. Learning Strategy and Inference), p. 4 (3.1. Problem Formulation), p. 4 (3.2. Reinforced Visual Latent Planning for Embodied Reasoning) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
