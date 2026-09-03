# UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=V7JPraxi5j.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/168156. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model
- Official paper: https://openreview.net/forum?id=V7JPraxi5j
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/168156
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 These limitations are largely attributed to the pre-training paradigm of VLMs (Wen et al., 2024; Chen et al., 2024a), which prioritizes multi-modal understanding tasks, such as Visual Question Answering (VQA), that enhance ...를 문제로 두고, We introduce a novel training paradigm for VLA models that combines both vision-language understanding and future prediction objectives, enabling the capture of both high-level semantic and low-level visual patterns essential for embodi ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent advancements in Vision-Language-Action (VLA) models have leveraged pre-trained VisionLanguage Models (VLMs) to improve the generalization capabilities.
- **p. 1 / Abstract - extractive body cue:** VLMs, typically pretrained on vision-language understanding tasks, provide rich semantic knowledge and reasoning abilities.
- **p. 1 / Abstract - extractive body cue:** However, prior research has shown that VLMs often focus on high-level semantic content and neglect low-level features, limiting their ability to capture detailed visual and ...
- **p. 1 / Abstract - extractive body cue:** These aspects, which are crucial for robotic control tasks, remain underexplored in existing pre-training paradigms.
- **p. 1 / Abstract - extractive body cue:** In this paper, we investigate the training paradigm for VLAs, and introduce UP-VLA, a Unified VLA model training with both multi-modal Understanding and future Prediction ...
- **p. 1 / 1. Introduction - extractive body cue:** These limitations are largely attributed to the pre-training paradigm of VLMs (Wen et al., 2024; Chen et al., 2024a), which prioritizes multi-modal understanding tasks, such ...
- **p. 1 / 1. Introduction - extractive body cue:** (2024) pointed out that pretrained VLMs lack spatial understanding and fail to capture low-level details such as distance and size differences.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We introduce a novel training paradigm for VLA models that combines both vision-language understanding and future prediction objectives, enabling the capture of both high-level semantic ...
- **p. 2 / 1. Introduction - extractive body cue:** Inspired by prior papers on visual pre-training (Wu et al., 2023; Guo et al., 2024), we introduce a novel training paradigm for VLA models that ...
- **p. 3 / 4.2. Bridging Visual Prediction and Multi-modal - extractive body cue:** Meanwhile, we introduce a new special token PRE to denote this new task.
- **p. 4 / 4.3. Enhancing Action Learning with Joint Prediction - extractive body cue:** To address this limitation, we propose a joint predictionand-understanding action learning mechanism.
- **p. 1 / 1. Introduction - extractive body cue:** This method enables VLA models to inherit the semantic knowledge and reasoning capabilities encoded in powerful VLMs, thereby enhancing decision-making in unknown environments.
- **p. 4 / 4.3. Enhancing Action Learning with Joint Prediction - extractive body cue:** Finally, we generate actions via joint prediction: ( ˆOt+∆t, ˆAt:t+∆t) = πP RE θ (Ot, L′) We use a small policy head to output low-level ...
- **p. 4 / 4.2. Bridging Visual Prediction and Multi-modal - extractive body cue:** It takes the current visual scene and language instructions as inputs, produces a high-level understanding of the scene, and subsequently predicts future images and robotic ...
- **p. 5 / 4.4.2. TRAINING OBJECTIVE - extractive body cue:** For the future image prediction task, given M current image tokens vt = {vi}M i=0 N and instruction tokens l = {li}N i=0, we use ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It takes the current visual scene and language instructions as inputs, produces a high-level understanding of the scene, and subsequently predicts future images and robotic actions based on these understanding tokens. same ... | image/video, language instruction, proprioception과 history | p. 4 (4.2. Bridging Visual Prediction and Multi-modal), p. 4 (4.2. Bridging Visual Prediction and Multi-modal) |
| State/latent | takes, current, visual, scene, language, instructions, inputs, produces, high-level, understanding, subsequently, predicts | language-grounded task state와 action-policy context | p. 4 (4.2. Bridging Visual Prediction and Multi-modal), p. 4 (4.2. Bridging Visual Prediction and Multi-modal), p. 3 (3. Preliminaries) |
| Output/action | Robot Pose Continuous image tokens Discrete image tokens Text tokens Action Token UP-VLA Model VQ-GAN Codebook Instruction Tokenizer Copy Language Answer Autoregressive Generate Direct Generation UP-VLA Model Autoregressive Generate UP- ... | continuous action, pose 또는 action chunk | p. 4 (4.2. Bridging Visual Prediction and Multi-modal), p. 3 (3. Preliminaries), p. 3 (4.2. Bridging Visual Prediction and Multi-modal) |
| Objective/outcome | Given M visual tokens u = {ui}M i=0 and N text tokens l = {li}N i=0, we maximize the likelihood of the next token using cross-entropy loss: LMMU = X i log ... | instruction following, task success, generalization과 latency | p. 5 (4.4.2. TRAINING OBJECTIVE), p. 5 (4.4.2. TRAINING OBJECTIVE), p. 3 (4.2. Bridging Visual Prediction and Multi-modal) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** We introduce a novel training paradigm for VLA models that combines both vision-language understanding and future prediction objectives, enabling the capture of both high-level semantic ...
- **p. 2 / 1. Introduction - extractive body cue:** Inspired by prior papers on visual pre-training (Wu et al., 2023; Guo et al., 2024), we introduce a novel training paradigm for VLA models that ...
- **p. 3 / 4.2. Bridging Visual Prediction and Multi-modal - extractive body cue:** Meanwhile, we introduce a new special token PRE to denote this new task.
- **p. 4 / 4.3. Enhancing Action Learning with Joint Prediction - extractive body cue:** To address this limitation, we propose a joint predictionand-understanding action learning mechanism.
- **p. 1 / 1. Introduction - extractive body cue:** This method enables VLA models to inherit the semantic knowledge and reasoning capabilities encoded in powerful VLMs, thereby enhancing decision-making in unknown environments.
- **p. 6 / 5.2. Simulation Evaluation - extractive body cue:** Compared to UPVLA-RT-2, which uses only action learning and achieves a completion length of 1.44, UP-VLA with visual prediction significantly improves the length to 4.08.
- **p. 6 / 5.2. Simulation Evaluation - extractive body cue:** Compared to other baselines, which perform significantly worse on ABC→D than on ABCD→D, UP-VLA achieves higher completion lengths in both scenarios, indicating that our method ...
- **p. 7 / 5.2. Simulation Evaluation - extractive body cue:** UP-VLA achieves the best performance, demonstrating that our approach exhibits strong generalization capabilities in simulated environments.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (5.2. Simulation Evaluation), p. 6 (5.2. Simulation Evaluation) |
| Embodiment/environment | For real-world experimental results, we train RT-1 (Brohan et al., 2022), Diffusion Policy (Chi et al., 2023) on our datasets (using the open-source code and testing them on the same physical hardware). | hardware/simulator version and reset protocol | p. 7 (5.3. Real Robot Evaluation), p. 6 (5. Experiments) |
| Dataset/benchmark | Our real-world experiments involve multiple table-top manipulation tasks on the Franka-Emika Panda robot, including picking and placing, routing cables, pressing buttons, and opening drawers. | role, split, size and leakage | p. 7 (5.3. Real Robot Evaluation), p. 6 (5. Experiments), p. 6 (5.1. Experiment Setup and baseline), p. 7 (5.3. Real Robot Evaluation) |
| Metric | We report the success rate of each task over 20 attempts during real-world roll-out. | definition, denominator, direction and uncertainty | p. 7 (5.3. Real Robot Evaluation), p. 6 (5.2. Simulation Evaluation), p. 6 (5.2. Simulation Evaluation) |
| Baseline/ablation | Compared to other baselines, which perform significantly worse on ABC→D than on ABCD→D, UP-VLA achieves higher completion lengths in both scenarios, indicating that our method has better multitask learning and generalization capabilitie ... | fair input/data/compute/action matching | p. 6 (5.2. Simulation Evaluation), p. 6 (5.2. Simulation Evaluation), p. 7 (5.3. Real Robot Evaluation) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 5.2. Simulation Evaluation - extractive body cue:** Our method addresses this limitation by incorporating visual prediction into the original VLA framework.
- **p. 6 / 5.2. Simulation Evaluation - extractive body cue:** Unlike UP-VLA, UP-VLA-phi-w/o-mmu does not include multi-modal understanding training, nor does it incorporate 6
- **p. 7 / 5.4. Ablation Studies - extractive body cue:** We compare the full UP-VLA with the following methods: UP-VLA-w/o-MMU, which does not utilize the LLava tuning dataset for multi-modal understanding, UPVLA-w/o-Bridge-Pretrain, which skips visual ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 These limitations are largely attributed to the pre-training paradigm of VLMs (Wen et al., 2024; Chen et al., 2024a), which prioritizes multi-modal understanding tasks, such as Visual Question Answering (VQA), that enhance ...를 문제로 두고, We introduce a novel training paradigm for VLA models that combines both vision-language understanding and future prediction objectives, enabling the capture of both high-level semantic and low-level visual patterns essential for embodi ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries), p. 4 (4.3. Enhancing Action Learning with Joint Prediction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
