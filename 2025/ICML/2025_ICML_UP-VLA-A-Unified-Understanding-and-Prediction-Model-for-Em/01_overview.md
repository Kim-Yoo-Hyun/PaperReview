# UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v267/zhang25w.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/168156. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: Jianke Zhang, Yanjiang Guo, Yucheng Hu, Xiaoyu Chen, Xiang Zhu, Jianyu Chen
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model
- Official paper: https://proceedings.mlr.press/v267/zhang25w.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25w/zhang25w.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

UP-VLA는 영상·언어 이해와 미래 관측 예측을 함께 학습해 의미 정보와 세밀한 공간 정보를 로봇 행동 생성에 활용한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/zhang25w/zhang25w.pdf#page=1)

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

- 이해 과제와 미래 영상 예측의 토큰을 하나의 학습 흐름에서 처리하고, 예측 과정의 표현을 행동 출력에 연결한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/zhang25w/zhang25w.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/zhang25w/zhang25w.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/zhang25w/zhang25w.pdf#page=5)
- CALVIN의 학습 외 환경과 실물 조작에서 성능을 측정하고, 미래 예측 또는 이해 학습을 제외하면 성공률이 어떻게 달라지는지 비교했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/zhang25w/zhang25w.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/zhang25w/zhang25w.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/zhang25w/zhang25w.pdf#page=8)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries), p. 4 (4.3. Enhancing Action Learning with Joint Prediction)이다.
