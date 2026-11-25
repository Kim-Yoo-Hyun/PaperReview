# WorldGym: World Model as An Environment for Policy Evaluation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://iclr.cc/virtual/2026/poster/10008029.
> PDF retrieval source: https://arxiv.org/pdf/2506.00613. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: Julian Quevedo, Ansh Kumar Sharma, Yixiang Sun, Varad Suryavanshi, Percy Liang, Sherry Yang
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, VLA, world model, policy evaluation, video prediction
- Official paper: https://iclr.cc/virtual/2026/poster/10008029
- Full-text retrieval: https://arxiv.org/pdf/2506.00613
- Code/Project: https://world-model-eval.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

WorldGym은 실제 초기 영상에서 출발해 정책을 영상 세계 모델 안에서 실행하고 그 결과로 실물 정책 성능을 가늠한다. [PDF 1쪽](https://arxiv.org/pdf/2506.00613#page=1)

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Evaluating robot control policies is difficult: real-world testing is costly, and handcrafted simulators require manual effort to improve in realism and generality.
- **p. 1 / ABSTRACT - extractive body cue:** We propose a world-model-based policy evaluation environment (WorldGym), an autoregressive, action-conditioned video generation model which serves as a proxy to real world environments.
- **p. 1 / ABSTRACT - extractive body cue:** Policies are evaluated via Monte Carlo rollouts in the world model, with a vision-language model providing rewards.
- **p. 1 / ABSTRACT - extractive body cue:** We evaluate a set of VLA-based real-robot policies in the world model using only initial frames from real robots, and show that policy success rates ...
- **p. 1 / ABSTRACT - extractive body cue:** Moreoever, we show that WorldGym is able to preserve relative policy rankings across different policy versions, sizes, and training checkpoints.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** As a result, the sim-to-real gap has hindered progress in robotics (Zhao et al., 2020; Salvato et al., 2021; Dulac-Arnold et al., 2019).
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, most of the existing work in model-based RL considers single-task settings, which puts itself at a disadvantage compared to model-free RL, since learning a ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Key contributions of this paper include: • We propose to use video world model to evaluate robot policies across different robot morphologies, and perform a ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Inspired by this observation, we propose a world-model-based policy evaluation environment (WorldGym), as shown in Figure 1.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** To ensure the world model is fully controllable by robot actions, we propose to randomly drop out actions for entire video clips, and use classifier-free ...
- **p. 4 / 1 INTRODUCTION - extractive body cue:** We propose setting the horizon equal to the policy's action chunk size, /apred/.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** Specifically, the OpenVLA Bridge evaluation consists of 17 challenging tasks which are not present in the Bridge V2 (Walke et al., 2023) dataset.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** First, the world model is initialized with an initial observation o0, which is then passed as input to a policy π which produces a chunk ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 3.1 BUILDING THE WORLD MODEL First, we describe the architecture and key implementation details, followed by our proposed inference scheme for policy rollouts.
- **p. 1 / ABSTRACT - extractive body cue:** We propose a world-model-based policy evaluation environment (WorldGym), an autoregressive, action-conditioned video generation model which serves as a proxy to real world environments.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | First, the world model is initialized with an initial observation o0, which is then passed as input to a policy π which produces a chunk of actions apred. | observation, uncertainty/risk estimate와 task command | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| State/latent | First, world, model, initialized, initial, observation, then, passed, input, policy, produces, chunk | safe set, recovery state 또는 constraint margin | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/action | This makes it possible to learn a single world model that, in principle, can be used as an interactive environment to evaluate any policies on any tasks. o0 o1 Policy o2 o3 ... | shielded, recovery 또는 safe action | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective/outcome | Policies are evaluated via Monte Carlo rollouts in the world model, with a vision-language model providing rewards. | task return과 violation/failure probability | p. 1 (ABSTRACT), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION) |

## Main Claims and Actual Contribution

- 행동 조건부 자기회귀 영상 모델에서 여러 롤아웃을 생성한 뒤 시각·언어 모델로 과제 보상을 추정한다. [PDF 3쪽](https://arxiv.org/pdf/2506.00613#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2506.00613#page=4)
- 시험한 정책 버전·규모·체크포인트에서 예측한 성공률과 순위를 실제 로봇 측정치와 대조했다. [PDF 6쪽](https://arxiv.org/pdf/2506.00613#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2506.00613#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 17 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Embodiment/environment | We suspect that OpenVLA consistently outperforms Octo and RT-1-X on OOD language tasks due to its strong VLM backbone and richer robot pretraining dataset (Kim et al.). | hardware/simulator version and reset protocol | p. 8 (1 INTRODUCTION), p. 8 (1 INTRODUCTION) |
| Dataset/benchmark | Task RT-1-X Octo OpenVLA Move Pot Into Drying Rack 3 0 7 Move The Pot To The Counter 0 0 1 Put Plate On Drying Rack 4 2 8 Put Yellow Corn ... | role, split, size and leakage | p. 8 (1 INTRODUCTION), p. 8 (1 INTRODUCTION), p. 9 (1 INTRODUCTION), p. 9 (1 INTRODUCTION) |
| Metric | Table 3: Performance of VLM as reward (mean and standard error across 4 runs) on videos from RT-1 (Brohan et al., 2022) using ground truth task success labels. GPT-4o achieves high true ... | definition, denominator, direction and uncertainty | p. 17 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Baseline/ablation | We suspect that OpenVLA consistently outperforms Octo and RT-1-X on OOD language tasks due to its strong VLM backbone and richer robot pretraining dataset (Kim et al.). | fair input/data/compute/action matching | p. 8 (1 INTRODUCTION), p. 22 (Figure/Table caption), p. 8 (1 INTRODUCTION) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 1 INTRODUCTION - extractive body cue:** Pick Carrot Pick Carrot Pick Carrot Pick Cat Pick Cat Pick Taylor Swift Pick Square Figure 10: OOD: Failure modes.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 10: OOD: Failure modes. Left: We add a laptop to the scene, which displays an image of a carrot. In 15% of trials, OpenVLA ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 1: Policy Evaluations Results on Bridge OOD Language Tasks. "Move the pot to the counter" is perhaps the most challenging because the Bridge dataset ...
- **p. 9 / 1 INTRODUCTION - extractive body cue:** We use an image editing model to add distractor objects to the Bridge evaluation suite, finding that RT-1X drops in performance by 51%, Octo by ...
- **p. 17 / Figure/Table caption - extractive body cue:** Table 3: Performance of VLM as reward (mean and standard error across 4 runs) on videos from RT-1 (Brohan et al., 2022) using ground truth ...
- **p. 24 / Figure/Table caption - extractive body cue:** Table 6: Detailed Bridge OOD Image task results. OpenVLA appears to be more robust across the different OOD settings of object generalization, distractions and classification. ...
- **p. 24 / Figure/Table caption - extractive body cue:** Table 7: Policy rollout performance comparison in the presence of unrelated distractions. OpenVLA is more robust to distractions over RT-1-X and Octo. However, all policies ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 8 (1 INTRODUCTION)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (25 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, most of the existing work in model-based RL considers single-task settings, which puts itself at a disadvantage compared to model-free RL, since learning a dynamics model can be much ... (p. 1, 1 INTRODUCTION).
- **Actual contribution:** Key contributions of this paper include: • We propose to use video world model to evaluate robot policies across different robot morphologies, and perform a comprehensive set of studies to ... (p. 2, 1 INTRODUCTION).
- **Evaluation boundary:** Table 1: Policy Evaluations Results on Bridge OOD Language Tasks. "Move the pot to the counter" is perhaps the most challenging because the Bridge dataset does not contain trajectories which ... (p. 9, Figure/Table caption).
- **Explicit failure boundary:** Notably, GPT-4o achieves very low false positives (i.e., the rollout is a failure but the VLM thinks it is a success), which is highly useful in policy evaluation. (p. 18, B.2 VALIDATING VLM SUCCESS PREDICTIONS).

## 원문과 공개 자료

- 코드 · 정책을 시험하는 학습 환경의 영상 예측 모델 구현 · src/world_model_eval/model.py [배포 파일](https://raw.githubusercontent.com/world-model-eval/world-model-eval/738510dd7d3b6f09846732acd757f0329f4851b3/src/world_model_eval/model.py)
- 가중치 · 여러 로봇의 시각 전이를 예측하는 세계 모델 · mixed_openx_9robots_20frames_0p1actiondropout_580ksteps.pt [배포 파일](https://drive.google.com/file/d/1uiRP2BuavapMsyP9Cbr25mi_ymk9SEJb/view)
- 데이터 · Bridge 평가용 시퀀스 표본 · sample_data/bridge/test/000000002.npz [배포 파일](https://raw.githubusercontent.com/world-model-eval/world-model-eval/738510dd7d3b6f09846732acd757f0329f4851b3/sample_data/bridge/test/000000002.npz)
