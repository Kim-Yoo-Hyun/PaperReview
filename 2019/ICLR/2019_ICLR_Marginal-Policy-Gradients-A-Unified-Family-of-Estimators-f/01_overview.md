# Marginal Policy Gradients: A Unified Family of Estimators for Bounded Action Spaces with Applications

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2019 / ICLR
- Authors: Carson Eisenach, Haichuan Yang, Ji Liu, Han Liu
- Category: Robotics Foundations: Robot Learning
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: RL, evaluation, learning-foundation
- Aliases: MPG
- Official paper: https://arxiv.org/abs/1806.05134
- Venue verification: https://openreview.net/pdf?id=HkgqFiAcFm
- Code/Project: not identified
- Code: not_identified
- Full-text retrieval: https://arxiv.org/pdf/1806.05134v3
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

Marginal Policy Gradients는 표본 행동이 변환된 뒤 실행될 때, 실제로 같은 행동을 만드는 표본들을 주변화해 정책 경사의 분산을 줄인다. [PDF 1쪽](https://arxiv.org/pdf/1806.05134v3#page=1) · [PDF 4쪽](https://arxiv.org/pdf/1806.05134v3#page=4)

## Core Idea and Contribution

- 방향만 제어하는 각도 정책 경사를 유도하고, 방향 정규화와 범위 클리핑을 같은 분산 분해로 설명한다. [PDF 4쪽](https://arxiv.org/pdf/1806.05134v3#page=4) · [PDF 6쪽](https://arxiv.org/pdf/1806.05134v3#page=6) · [PDF 7쪽](https://arxiv.org/pdf/1806.05134v3#page=7)
- 방향 행동을 사용하는 내비게이션과 실시간 전략 게임에서 각도 정책 경사와 표준 정책 경사의 학습 결과를 비교했다. [PDF 8쪽](https://arxiv.org/pdf/1806.05134v3#page=8) · [PDF 9쪽](https://arxiv.org/pdf/1806.05134v3#page=9)

## Observation–State–Action Interface

Raw action distribution → execution transform → marginal score.

## Evaluation Scope and Claim Boundary

RTS와 navigation task 및 variance 분석을 보고한다.

근거: [공식 paper/abstract](https://openreview.net/forum?id=HkgqFiAcFm).

## Why This Paper Is Here — Researcher Interpretation

C3의 action equivalence 주장을 제한하는 가장 직접적인 이론 계보다.

## Verification Boundary

transform measurability, discrete/continuous 차이, action-slot weighting을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
