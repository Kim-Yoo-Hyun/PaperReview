# HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2026/hash/82ad13ec01f9fe44c01cb91814fd7b8c-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/245878. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Jiaming Liu, Hao Chen, Zhuoyang Liu, Pengju An, Renrui Zhang, Chenyang Gu, Xiaoqi Li, Ziyu Guo, Sixiang Chen, Mengzhen Liu, Chengkai Hou, Mengdi Zhao, KC Zhou, Pheng-Ann Heng, Shanghang Zhang
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics, Diffusion
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/82ad13ec01f9fe44c01cb91814fd7b8c-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2026/file/82ad13ec01f9fe44c01cb91814fd7b8c-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

HybridVLA는 하나의 언어 모델 백본에서 이산 행동의 자기회귀 예측과 연속 행동의 확산 예측을 함께 학습한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/82ad13ec01f9fe44c01cb91814fd7b8c-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** A central objective of manipulation policy design is to enable robots to comprehend human instructions and predict generalized actions in unstructured environments.
- **p. 1 / ABSTRACT - extractive body cue:** Recent autoregressive vision-language-action (VLA) approaches discretize actions into bins to exploit the pretrained reasoning and generation paradigms of visionlanguage models (VLMs).
- **p. 1 / ABSTRACT - extractive body cue:** While these models achieve efficient and scalable training, the discretization undermines the continuity required for precise control.
- **p. 1 / ABSTRACT - extractive body cue:** In contrast, diffusion-based VLA methods incorporate an additional diffusion head to predict continuous actions, but they rely solely on feature representations extracted from the VLM, ...
- **p. 1 / ABSTRACT - extractive body cue:** To integrate the complementary strengths of autoregressive and diffusion generation, we introduce HybridVLA, which innovatively leverages a shared LLM backbone to perform iterative action prediction ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Unlike prior diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a) that append an independent diffusion head after the LLM (Figure 1 (a)), ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Recent diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a; Wen et al., 2024a; Bjorck et al., 2025) incorporate a diffusion head after ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose HybridVLA, which innovatively leverages a single LLM backbone for iterative action prediction through both autoregressive and diffusion ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Unlike prior diffusion-based VLA methods (Black et al., 2024; Li et al., 2024a) that append an independent diffusion head after the LLM (Figure 1 (a)), ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Developing intelligent robots capable of performing manipulation tasks demands robust policies (Driess et al., 2023; Huang et al., 2023).
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Given these advantages and limitations, a question arises: "How can we elegantly construct a unified VLA model that integrates the strengths of both autoregressive and ...
- **p. 1 / ABSTRACT - extractive body cue:** In contrast, diffusion-based VLA methods incorporate an additional diffusion head to predict continuous actions, but they rely solely on feature representations extracted from the VLM, ...
- **p. 1 / ABSTRACT - extractive body cue:** A central objective of manipulation policy design is to enable robots to comprehend human instructions and predict generalized actions in unstructured environments.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A central objective of manipulation policy design is to enable robots to comprehend human instructions and predict generalized actions in unstructured environments. | image/video, language instruction, proprioception과 history | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |
| State/latent | central, objective, manipulation, policy, design, enable, robots, comprehend, human, instructions, predict, generalized | language-grounded task state와 action-policy context | p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| Output/action | Moreover, we demonstrate that the autoregressive discrete action outputs of HybridVLA can be replaced with language-based task planning without compromising the stability of diffusion-based action prediction. | continuous action, pose 또는 action chunk | p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective/outcome | Our contributions are as follows: • We propose HybridVLA, which innovatively leverages a single LLM backbone for iterative action prediction through both autoregressive and diffusion generation within a unified token sequence, harnessin ... | instruction following, task success, generalization과 latency | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 1 (ABSTRACT) |

## Main Claims and Actual Contribution

- 다음 토큰 예측 과정에 행동 잡음 제거를 포함하고 두 생성 방식의 학습 간섭을 줄이는 입력 순서와 주의 방식을 비교했다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/82ad13ec01f9fe44c01cb91814fd7b8c-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/82ad13ec01f9fe44c01cb91814fd7b8c-Paper-Conference.pdf#page=5)
- 두 경로가 제안한 행동을 적응적으로 결합하고, 시뮬레이션과 실물 조작에서 각 경로만 사용한 경우와 비교했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/82ad13ec01f9fe44c01cb91814fd7b8c-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/82ad13ec01f9fe44c01cb91814fd7b8c-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/82ad13ec01f9fe44c01cb91814fd7b8c-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (12.3 Hz), p. 7 (12.3 Hz) |
| Embodiment/environment | CAE indicates the collaborative action ensemble method, whereas LSP refers to large-scale pretraining on robotic datasets. | hardware/simulator version and reset protocol | p. 8 (12.3 Hz), p. 8 (12.3 Hz) |
| Dataset/benchmark | All methods maintain satisfactory performance, demonstrating that large-scale pretraining on robotic datasets enhances their generalization across diverse data distributions. | role, split, size and leakage | p. 8 (12.3 Hz), p. 8 (12.3 Hz), p. 10 (12.3 Hz), p. 6 (4 EXPERIMENT) |
| Metric | We train all methods in the multi-task setting (Shridhar et al., 2022) and report the success rates (S.R.) and variances (Var.). | definition, denominator, direction and uncertainty | p. 7 (4 EXPERIMENT), p. 7 (12.3 Hz), p. 8 (12.3 Hz) |
| Baseline/ablation | The results show that our method reduces the accuracy drop by approximately 5-16% compared to the baselines under generalization scenarios. | fair input/data/compute/action matching | p. 10 (12.3 Hz), p. 7 (12.3 Hz), p. 9 (12.3 Hz) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 12.3 Hz - extractive body cue:** Additional qualitative results and failure case analyses are provided in Appendix D and Appendix E, respectively, and execution videos are available in the supplementary materials.
- **p. 26 / Figure/Table caption - extractive body cue:** Figure 9: Single-arm Execution Visualization. We visualize key frames of the agent's execution process from the front perspective. E FAILURE CASE ANALYSIS. Through extensive real-world ...
- **p. 8 / 12.3 Hz - extractive body cue:** Due to space limitations, Appendix C.2 provides additional ablation studies on: (1) confidence thresholds in the collaborative action ensemble, (2) the influence of the diffusion-based ...
- **p. 10 / 12.3 Hz - extractive body cue:** One limitation of HybridVLA is that its inference speed is constrained by the slower autoregressive generation, similar to prior autoregressive VLA methods (Kim et al., ...
- **p. 10 / 12.3 Hz - extractive body cue:** 5 CONCLUSION AND LIMITATION In this paper, we introduce HybridVLA, a unified Vision-Language-Action (VLA) framework that equips a single LLM with both diffusion-based and autoregressive ...
- **p. 21 / Figure/Table caption - extractive body cue:** Figure 4: Real-World Assets and Experimental Settings. We provide visualizations of the assets used and the settings for single-arm FR3 robot tasks and dual-arm AgileX ...
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 5: The impact of denoising steps, where the x-axis and y-axis represent the denoising steps and manipulation success rate. that a ratio between AR ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION)이다.
