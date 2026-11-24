# PD-VLA: Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2503.02310.
> PDF retrieval source: https://arxiv.org/pdf/2503.02310. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / IROS
- Authors: Wenxuan Song, Jiayi Chen, Pengxiang Ding, Han Zhao, Wei Zhao, Zhide Zhong, Zongyuan Ge, Zhijun Li, Donglin Wang, Lujia Wang, Jun Ma, Haoang Li
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model
- Official paper: https://arxiv.org/abs/2503.02310
- Full-text retrieval: https://arxiv.org/pdf/2503.02310
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

PD-VLA는 행동 청크를 생성하는 자기회귀 VLA에서 여러 토큰 위치를 병렬 갱신해 재학습 없이 디코딩 시간을 줄인다. [PDF 1쪽](https://arxiv.org/pdf/2503.02310v2#page=1) · [PDF 2쪽](https://arxiv.org/pdf/2503.02310v2#page=2)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models demonstrate remarkable potential for generalizable robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** The performance of VLA models can be improved by integrating with action chunking, a critical technique for effective control.
- **p. 1 / Abstract - extractive body cue:** However, action chunking linearly scales up action dimensions in VLA models with increased chunking sizes.
- **p. 1 / Abstract - extractive body cue:** This reduces the inference efficiency.
- **p. 1 / Abstract - extractive body cue:** Therefore, accelerating VLA integrated with action chunking is an urgent need.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The pursuit of robust and generalizable robotic manipulation policies remains a fundamental challenge in embodied AI research [1].
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address the above challenges, we present a novel parallel decoding framework for the mainstream VLA model with action chunking, called Parallel Decoding for VLA ...

## Core Idea

- **p. 3 / III. METHOD - extractive body cue:** In this section, we introduce the details of our method PD-VLA.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our primary contributions include: • We propose the first parallel decoding framework for VLA models integrated with action chunking.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Accordingly, our method enables friendly deployment, compared with existing methods, i.e., it achieves training-free acceleration without redesign and modification of models (see Table I).
- **p. 3 / III. METHOD - extractive body cue:** Finally, we present parallel decoding to accelerate inference in subsection III-C.
- **p. 4 / III. METHOD - extractive body cue:** (6) This enables updates of all action tokens in every single iteration.
- **p. 3 / III. METHOD - extractive body cue:** Parallel Decoding for VLA Models To meet the demands of a more efficient decoding algorithm, we propose parallel decoding for VLA models integrated with action ...
- **p. 3 / III. METHOD - extractive body cue:** LLaVA mainly consists of a large language model LLM and a vision encoder fencoder.
- **p. 4 / III. METHOD - extractive body cue:** We first randomly initialize an action token sequence of equal length to the decoding horizon n.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It takes two images as input, a static image Istatic and a gripper image Igripper, to get a comprehensive observation. | image/video, language instruction, proprioception과 history | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| State/latent | takes, images, input, static, image, Istatic, gripper, Igripper, comprehensive, observation, Along, text | language-grounded task state와 action-policy context | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Output/action | Along with the input images, the text instructions and proprioceptive input are first concatenated into a unified instruction S, which is then tokenized into tokens hS via a tokenizer T. | continuous action, pose 또는 action chunk | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective/outcome | 병렬 반복으로 자기회귀 토큰열의 고정점을 구한다. | 청크 디코딩 시간과 과제 성공률 | 토큰 갱신은 식 (5)를 따른다. [PDF 4쪽](https://arxiv.org/pdf/2503.02310v2#page=4) |

## Main Claims and Actual Contribution

- 순차적인 다음 토큰 결정을 연립 고정점 문제로 표현하고 직전 반복의 접두 토큰으로 각 위치를 동시에 갱신한다. [PDF 3쪽](https://arxiv.org/pdf/2503.02310v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2503.02310v2#page=4)
- 청크와 디코딩 설정을 바꾸어 실행 빈도와 조작 성공률을 따로 비교하고 실물 과제에서도 적용을 시험했다. [PDF 5쪽](https://arxiv.org/pdf/2503.02310v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2503.02310v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2503.02310v2#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Embodiment/environment | The CALVIN benchmark [35] is built on top of the PyBullet [46] simulator and involves a Franka Panda Robot arm that manipulates the scene. | hardware/simulator version and reset protocol | p. 4 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Dataset/benchmark | Can PD-VLA be effectively deployed in real-world robotic systems? | role, split, size and leakage | p. 4 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Metric | Compared with prior stateof-the-art approaches, PD-VLA achieves the best average performance, attaining a 91.7% success rate on the most challenging LIBERO-Long benchmark. | definition, denominator, direction and uncertainty | p. 6 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Baseline/ablation | For a comprehensive comparison, we include various baselines, such as the official MCIL [35] model and other prevalent models like HULC [36] and RT-1 [4]. | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Notably, our PD-VLA does not incur extra training costs.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** All tasks include distractors to validate the robustness of the model.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** For the task "pour water", LLaVA-VLA failed to complete this task, while PD-VLA has a 50% higher success rate.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD)이다.
