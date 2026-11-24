# HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/icra55743.2025.11128549.
> PDF retrieval source: https://research.nvidia.com/labs/lpr/publication/he2025hover/. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICRA
- Authors: Tairan He, Wenli Xiao, Toru Lin, Zhengyi Luo, Zhenjia Xu, Zhenyu Jiang, Jan Kautz, Changliu Liu, Guanya Shi, Xiaolong Wang, Linxi Jim Fan, Yuke Zhu
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, humanoid, whole-body control, Reinforcement Learning, NVIDIA
- Official paper: https://api.crossref.org/works/10.1109/icra55743.2025.11128549
- Full-text retrieval: https://arxiv.org/pdf/2410.21229v2
- Code/Project: https://hover-versatile-humanoid.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://arxiv.org/pdf/2410.21229v2) 기준이다.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Why This Paper Is Here

HOVER는 전신 동작 모방을 공통 교사로 삼고 다양한 명령 방식의 휴머노이드 제어를 하나의 정책으로 증류한다. [PDF 1쪽](https://arxiv.org/pdf/2410.21229v2#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Humanoid whole-body control requires adapting to diverse tasks such as navigation, loco-manipulation, and tabletop manipulation, each demanding a different mode of control.
- **p. 1 / Abstract - extractive body cue:** For example, navigation relies on root velocity or position tracking, while tabletop manipulation prioritizes upperbody joint angle tracking.
- **p. 1 / Abstract - extractive body cue:** Existing approaches typically train individual policies tailored to a specific command space, limiting their transferability across modes.
- **p. 1 / Abstract - extractive body cue:** We present the key insight that full-body kinematic motion imitation can serve as a common abstraction for all these tasks and provide generalpurpose motor skills ...
- **p. 1 / Abstract - extractive body cue:** Building on this, we propose HOVER (Humanoid Versatile Controller), a multi-mode policy distillation framework that consolidates diverse control modes into a unified policy.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This is a non-trivial challenge, as each mode operates within a distinct command space, making direct integration impractical.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This versatile command space covers most modes used in prior works [9, 10, 12, 13].

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** To summarize, our contributions are threefold: 1) we present HOVER, a unified neural controller for humanoid whole-body control supporting multiple control modes; 2) we show ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To this end, we present HOVER, a unified neural controller for humanoid whole-body control that supports diverse control modes as shown in Figure 1, including ...
- **p. 3 / II. METHOD - extractive body cue:** In our framework, as shown in Figure 1, a one-hot masking vector is introduced to specify which components of the command space are activated for ...
- **p. 3 / II. METHOD - extractive body cue:** This space consists of two primary control regions-upper-body and lower-body control-and incorporates three distinct control modes: • Kinematic Position Tracking: target 3D positions of key ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** 1: HOVER enables versatile humanoid control with a unified multi-mode command space.
- **p. 4 / II. METHOD - extractive body cue:** The student policy πstudent is then updated by minimizing the loss function: L = ∥ˆat -at∥2 2, where ˆat is the reference action from the ...
- **p. 3 / II. METHOD - extractive body cue:** We use the same policy network structure with [9], a three-layer MLP with layer dimensions of [512, 256, 128].
- **원문 대조:** 보상은 proprioceptive state와 goal state의 함수 R(s_t^p,s_t^g)로 정의한다. 정책 action은 19차원 목표 관절 위치이며 PD controller에 전달한다. 보상 정의 자체가 recovery 절차를 명시하는 것은 아니다. ([PDF p. 2](https://hover-versatile-humanoid.github.io/resources/HOVER_paper.pdf#page=2), §II-A Goal-Conditioned RL for Humanoid Control).

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Using these oracle states, we query the oracle teacher policy πoracle(ˆat/sp-oracle t , sg-oracle t ) to obtain the reference action ˆat. | proprioception, reference pose/motion, visual or language command | p. 4 (II. METHOD), p. 2 (II. METHOD) |
| State/latent | oracle, states, query, teacher, policy, at/sp-oracle, sg-oracle, obtain, reference, action, agent, proprioception | whole-body pose, balance/contact state와 skill/mode | p. 4 (II. METHOD), p. 2 (II. METHOD), p. 3 (II. METHOD) |
| Output/action | 원문 대조: 보상은 proprioceptive state와 goal state의 함수 R(s_t^p,s_t^g)로 정의한다. 정책 action은 19차원 목표 관절 위치이며 PD controller에 전달한다. 보상 정의 자체가 recovery 절차를 명시하는 것은 아니다. ([PDF p. 2](https://hover-versatile-humanoid.github.io/resources/HOVER_paper.pdf#page=2), §II-A Goal-Conditioned RL for Humanoid Control) | 19차원 목표 관절 위치 → PD controller | [PDF p. 2](https://hover-versatile-humanoid.github.io/resources/HOVER_paper.pdf#page=2), §II-A Goal-Conditioned RL for Humanoid Control |
| Objective/outcome | We employ the proximal policy optimization (PPO) algorithm [18] to maximize the cumulative discounted reward E hPT t=1 γt-1rt i . | tracking, balance, skill/task success와 recovery | p. 2 (II. METHOD), p. 4 (II. METHOD), p. 2 (II. METHOD) |

## Main Claims and Actual Contribution

- 명령에서 신체 일부의 목표를 가리는 방식으로 속도·몸통·상체 등 서로 다른 제어 입력을 통합한다. [PDF 2쪽](https://arxiv.org/pdf/2410.21229v2#page=2) · [PDF 3쪽](https://arxiv.org/pdf/2410.21229v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2410.21229v2#page=4)
- 시뮬레이션에서 모드별 전문 정책과 비교하고 실물 휴머노이드에서 자세 추종과 제어 모드 전환을 시험했다. [PDF 4쪽](https://arxiv.org/pdf/2410.21229v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2410.21229v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2410.21229v2#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 4 (III. EXPERIMENT), p. 5 (III. EXPERIMENT) |
| Embodiment/environment | In this section, we present extensive experimental results in both IsaacGym [23] and the real-world Unitree H1 [24] robot to address the following questions: • Q1: Can HOVER as a generalist policy ... | hardware/simulator version and reset protocol | p. 4 (III. EXPERIMENT), p. 5 (III. EXPERIMENT) |
| Dataset/benchmark | In simulation, we evaluate using the retargeted AMASS dataset ˆQ. | role, split, size and leakage | p. 4 (III. EXPERIMENT), p. 5 (III. EXPERIMENT), p. 4 (III. EXPERIMENT), p. 5 (III. EXPERIMENT) |
| Metric | Fig. 4: We assess the tracking accuracy of two multi-mode control policies-HOVER (green) and Multi-Mode RL (purple)-across eight distinct humanoid control modes. The comparison is visual- ized across four key performance metrics ... | definition, denominator, direction and uncertainty | p. 5 (Figure/Table caption), p. 5 (III. EXPERIMENT), p. 2 (Figure/Table caption) |
| Baseline/ablation | To address Q2 (does HOVER outperform other methods of training a multi-mode humanoid controller?), we compare HOVER with a multi-mode RL baseline that follows the (a) Root RPY (d) Global Body Position ... | fair input/data/compute/action matching | p. 5 (III. EXPERIMENT), p. 5 (III. EXPERIMENT), p. 4 (III. EXPERIMENT) |

## Explicit Limitations and Failure Boundary

- **p. 6 / V. CONCLUSIONS - extractive body cue:** Future work will explore further developing an automated mode-switching module for real-world applications.
- **p. 6 / III. EXPERIMENT - extractive body cue:** The results demonstrate that HOVER can smoothly track motions across different modes, showcasing its robustness for real-world scenarios (e.g., when there are occlusions in the ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (II. METHOD), p. 3 (II. METHOD)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** This is a non-trivial challenge, as each mode operates within a distinct command space, making direct integration impractical. (p. 1, I. INTRODUCTION).
- **Actual contribution:** To summarize, our contributions are threefold: 1) we present HOVER, a unified neural controller for humanoid whole-body control supporting multiple control modes; 2) we show that, through policy distillation, HOVER ... (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** In this section, we present extensive experimental results in both IsaacGym [23] and the real-world Unitree H1 [24] robot to address the following questions: • Q1: Can HOVER as a ... (p. 4, III. EXPERIMENT).
- **Explicit failure boundary:** The results demonstrate that HOVER can smoothly track motions across different modes, showcasing its robustness for real-world scenarios (e.g., when there are occlusions in the reference motions). (p. 6, III. EXPERIMENT).
