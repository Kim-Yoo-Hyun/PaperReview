# VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://neurips.cc/virtual/2025/poster/118121.
> PDF retrieval source: https://arxiv.org/pdf/2502.02175. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: Siyu Xu, Yunke Wang, Chenghao Xia, Dihao Zhu, Tao Huang, Chang Xu
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://neurips.cc/virtual/2025/poster/118121
- Published PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/f062da1973ac9ac61fc6d44dd7fa309f-Paper-Conference.pdf
- Full-text retrieval at original review: https://arxiv.org/pdf/2502.02175
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

VLA-Cache는 인접 영상 간에 거의 변하지 않은 시각 토큰의 키와 값을 재사용해 추가 훈련 없이 로봇 정책의 추론을 줄인다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/f062da1973ac9ac61fc6d44dd7fa309f-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language-Action (VLA) models have demonstrated strong multi-modal reasoning capabilities, enabling direct action generation from visual perception and language instructions in an end-to-end manner.
- **p. 1 / Abstract - extractive body cue:** However, their substantial computational cost poses a challenge for real-time robotic control, where rapid decision-making is essential.
- **p. 1 / Abstract - extractive body cue:** This paper introduces VLA-Cache, a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames.
- **p. 1 / Abstract - extractive body cue:** Exploiting the temporal continuity in robotic manipulation, VLA-Cache identifies minimally changed tokens between adjacent frames and reuses their cached key-value representations, thereby circumventing redundant computations.
- **p. 1 / Abstract - extractive body cue:** Additionally, to maintain action precision, VLA-Cache selectively re-computes task-relevant tokens that are environmentally sensitive, ensuring the fidelity of critical visual information.
- **p. 1 / 1 Introduction - extractive body cue:** While effective to some extent, these methods often require architectural modifications or retraining, and more importantly, they lack task-specific design tailored to the intrinsic characteristics ...
- **p. 1 / 1 Introduction - extractive body cue:** Learning a robust and generalizable policy for robotic manipulation through policy learning has long been a challenging problem [1], with traditional reinforcement learning approaches [2, ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** To address the inefficiency introduced by repeatedly processing static visual information, we present VLA-Cache, a training-free inference acceleration method that exploits temporal continuity in robotic ...
- **p. 3 / 3 Methodology - extractive body cue:** To address this, we propose a method that identifies visually static tokens and filters out semantically important ones based on attention scores from the VLA ...
- **p. 3 / 3 Methodology - extractive body cue:** In the following sections, we introduce its core mechanisms: static token selection, task-relevance filtering, and layer-adaptive reuse to accelerate VLA inference while preserving action accuracy.
- **p. 2 / 1 Introduction - extractive body cue:** This consistency allows for caching the computations of these tokens from the previous step.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | However, most existing Vision-Language-Action (VLA) 3 | image/video, language instruction, proprioception과 history | p. 3 (3 Methodology), p. 3 (3 Methodology) |
| State/latent | However, most, existing, Vision-Language-Action, VLA, While, caching, effective, language, decoding, within, single | language-grounded task state와 action-policy context | p. 3 (3 Methodology), p. 3 (3 Methodology), p. 1 (1 Introduction) |
| Output/action | (3) While KV caching is effective for language decoding within a single query in vision-language models, this technique does not address redundancy in the visual stream, especially in Vision-Language-Action (VLA) models. | continuous action, pose 또는 action chunk | p. 3 (3 Methodology), p. 1 (1 Introduction), p. 1 (1 Introduction) |
| Objective/outcome | In robotic action prediction, most visual tokens remain static across frames except for key regions like the manipulator or target object. | instruction following, task success, generalization과 latency | p. 3 (3 Methodology), p. 3 (3 Methodology) |

## Main Claims and Actual Contribution

- 변화가 작아도 과제에 중요한 토큰은 다시 계산하고, 디코더 층별 주의 분포에 맞춰 재사용하는 비율을 조절한다. [PDF 3쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/f062da1973ac9ac61fc6d44dd7fa309f-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/f062da1973ac9ac61fc6d44dd7fa309f-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/f062da1973ac9ac61fc6d44dd7fa309f-Paper-Conference.pdf#page=5)
- LIBERO·SIMPLER와 실제 로봇에서 과제 성공을 확인하고 GPU 추론 지연과 로봇 제어 빈도를 구분해 속도 효과를 측정했다. [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/f062da1973ac9ac61fc6d44dd7fa309f-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/f062da1973ac9ac61fc6d44dd7fa309f-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/f062da1973ac9ac61fc6d44dd7fa309f-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 8 (5 Experiment) |
| Embodiment/environment | (Hz) ↑ PickPot PlaceCube PutSausage WipeTable Average OpenVLA 95.0% 83.3% 80.0% 70.0% 82.1% 1.814 64.16 4.02 + VLA-Cache 90.0% 90.0% 85.0% 73.3% 84.6% 1.303 51.85 4.21 5.4 Results on Real Robot Table ... | hardware/simulator version and reset protocol | p. 9 (5 Experiment), p. 7 (5 Experiment) |
| Dataset/benchmark | In simulation, we evaluate VLA-Cache on three open-source VLA models: OpenVLA [11], OpenVLA-OFT [20] and CogAct [19], using the LIBERO benchmark [17] and SIMPLER environment [18], respectively. | role, split, size and leakage | p. 9 (5 Experiment), p. 7 (5 Experiment), p. 7 (5 Experiment), p. 8 (5 Experiment) |
| Metric | Figure 4: Visualization of VLA-Cache token reuse across settings. (a) LIBERO simulation with OpenVLA. (b) Real-world task under dynamic background. (c) and (d) Main and wrist camera views from OpenVLA-OFT. Blue: static ... | definition, denominator, direction and uncertainty | p. 9 (Figure/Table caption), p. 7 (5 Experiment), p. 9 (5 Experiment) |
| Baseline/ablation | Specifically, we adopt two state-of-the-art token-level acceleration techniques SparseVLM [30] and FastV [29] on OpenVLA as compared methods in the LIBERO benchmark. | fair input/data/compute/action matching | p. 7 (5 Experiment), p. 15 (Figure/Table caption), p. 7 (5 Experiment) |

## Explicit Limitations and Failure Boundary

- **p. 18 / Figure/Table caption - extractive body cue:** Table 11: Real-world results with trial counts and success rates. Results with Counts and Rates. Table 11 reports per-task successes and failures, along with the ...
- **p. 8 / 5 Experiment - extractive body cue:** In contrast, FastV and SparseVLM fail to improve inference speed and often degrade task performance.
- **p. 8 / 5 Experiment - extractive body cue:** It performs robustly across tasks and exceeds the baseline on goal-oriented manipulation.
- **p. 9 / 5 Experiment - extractive body cue:** As shown in Table 7, success rate of baseline dropped from 95% to 80% under noise.
- **p. 9 / 5 Experiment - extractive body cue:** To assess robustness, we introduced background motion (e.g., human hands and moving objects) in the PickPot task.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Methodology)이다.
