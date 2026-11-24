# FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/icra57385.2026.11695889.
> PDF retrieval source: https://arxiv.org/pdf/2602.02142. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICRA
- Authors: Ruiteng Zhao, Wenshuo Wang, Yicheng Ma, Xiaocong Li, Francis E.H. Tay, Marcelo H. Ang, Haiyue Zhu
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://api.crossref.org/works/10.1109/icra57385.2026.11695889
- Full-text retrieval: https://arxiv.org/pdf/2602.02142
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

FD-VLA는 학습 때 계측한 힘의 표현을 시각·로봇 상태로 예측하게 해 배포 시 힘 센서 없이 접촉 조작을 수행한다. [PDF 1쪽](https://arxiv.org/pdf/2602.02142v2#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Force sensing is a crucial modality for VisionLanguage-Action (VLA) frameworks, as it enables fine-grained perception and dexterous manipulation in contact-rich tasks.
- **p. 1 / Abstract - extractive body cue:** We present Force-Distilled VLA (FD-VLA), a novel framework that integrates force awareness into contact-rich manipulation without relying on physical force sensors.
- **p. 1 / Abstract - extractive body cue:** The core of our approach is a Force Distillation Module (FDM), which distills force by mapping a learnable query token, conditioned on visual observations and ...
- **p. 1 / Abstract - extractive body cue:** During inference, this distilled force token is injected into the pretrained VLM, enabling force-aware reasoning while preserving the integrity of its vision-language semantics.
- **p. 1 / Abstract - extractive body cue:** This design provides two key benefits: first, it allows practical deployment across a wide range of robots that lack expensive or fragile force-torque sensors, thereby ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables practical deployment on a wide range of robot platforms that lack force sensors, reducing hardware cost and ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Moreover, the late-fusion mechanism limits fine-grained forcevision-state interactions, reducing tight perception-action coupling and generalization.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the main contributions of this work are summarized as follows: • We propose the FD-VLA framework that injects a distilled force token into ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose a novel FD-VLA framework that incorporates a distilled force token, rather than raw sensor signals, into the VLA model to ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** Motivated by these challenges, we propose FD-VLA guided by three design principles: (i) leverage predicted force tokens obtained through distillation with actual force signals during ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** The realization of FDM consists of two parallel branches, i.e., the prediction branch and actual force branch.
- **p. 4 / III. METHODOLOGY - extractive body cue:** Rather than directly incorporating the raw force measurements into the VLM, we introduce the Force Distillation Module (FDM) that can predict a latent force representation ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Force Distillation Module (FDM) Our FDM generates a compact, state-aware force representation that can be seamlessly integrated into the VLA pipeline without requiring specialized tactile ...
- **p. 5 / III. METHODOLOGY - extractive body cue:** Overall Training Objective The overall objective of our FD-VLA framework combines two complementary components, i.e., a standard policy learning loss and a force-distillation loss, which ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** Motivation The objective of this work is to explore an effective and data-efficient approach to incorporate additional force modality into VLA model for contact-rich manipulation.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The multimodal inputs of VLA include language instruction L, visual observation Vt, robot state St, and force Ft, where t denotes the timestamp. | image/video, language instruction, proprioception과 history | p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION) |
| State/latent | multimodal, inputs, VLA, include, language, instruction, visual, observation, robot, state, force, where | language-grounded task state와 action-policy context | p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/action | This allows them to map RGB inputs and natural-language instructions directly to low-level robot commands, while benefiting from strong This research is supported by National Robotics Programme (NRP) 2.0 funding initiative "Domain-speci ... | continuous action, pose 또는 action chunk | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHODOLOGY) |
| Objective/outcome | Overall Training Objective The overall objective of our FD-VLA framework combines two complementary components, i.e., a standard policy learning loss and a force-distillation loss, which is defined as L = Lτ(θ) + ... | instruction following, task success, generalization과 latency | p. 5 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |

## Main Claims and Actual Contribution

- 학습 가능한 질의로 예측한 토큰을 측정 힘의 잠재 표현에 맞춘 뒤 행동 생성기의 입력에 포함한다. [PDF 3쪽](https://arxiv.org/pdf/2602.02142v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2602.02142v2#page=4)
- 실물 접촉 과제에서 예측한 힘 토큰, 센서 측정값을 입력한 정책, 힘 정보를 제거한 조건을 비교했다. [PDF 5쪽](https://arxiv.org/pdf/2602.02142v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2602.02142v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2602.02142v2#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (IV. EXPERIMENTS), p. 6 (Figure/Table caption) |
| Embodiment/environment | Results are averaged over 30 evaluation episodes per task. | hardware/simulator version and reset protocol | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Dataset/benchmark | This section presents an extensive evaluation of the FDVLA model through real-world experiments and analytical studies. | role, split, size and leakage | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Metric | Across all the tasks, our FD-VLA achieves the highest overall performance with a mean success rate of 61.1%, substantially outperforming both SmolVLA without force encoding (23.3%), DP3 (11.1%) and even π0 without ... | definition, denominator, direction and uncertainty | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 2 (Figure/Table caption) |
| Baseline/ablation | DP3 is selected as a strong diffusion-based control framework with a parameter scale comparable to ours, which provides a capacity-matched baseline that excels at generating precise motion trajectories. π0 represents the state-of-the-ar ... | fair input/data/compute/action matching | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Overview of differentiate architectures of force VLAs. (Left) Tactile-VLA with tactile encoder directly encode tactile information. (Middle) Force-VLA with MoE module between VLM ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** This architecture allows our system to leverage the semantic richness of pretrained VLM while introducing stable, taskrelevant physical reasoning through force distillation, achieving both robustness ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Finally, FDM mitigates the noise and instability of raw sensor signals by learning a supervised latent embedding that serves as a denoised, taskrelevant proxy for ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Our model achieves consistently higher performance, which highlights the benefit of force distillation for accurate and robust manipulation.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** For evaluation, each task was trained using a set of 50 demonstrations and subsequently evaluated over 30 independent test trials to ensure statistical robustness.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 3 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 5 (III. METHODOLOGY)이다.
