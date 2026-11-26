# Clipped Action Policy Gradient

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2018 / ICML
- Authors: Yasuhiro Fujita, Shin-ichi Maeda
- Category: Robotics Foundations: Robot Learning
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: RL, evaluation, learning-foundation, policy-gradient
- Aliases: CAPG
- Official paper: https://proceedings.mlr.press/v80/fujita18a.html
- Venue verification: https://proceedings.mlr.press/v80/fujita18a.html
- Code/Project: https://github.com/pfnet-research/capg
- Code: https://github.com/pfnet-research/capg
- Full-text retrieval: https://proceedings.mlr.press/v80/fujita18a/fujita18a.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

CAPG는 행동 범위를 넘는 정책 출력을 실행 전에 경곗값으로 자르는 연속제어에서, 실제로 실행된 행동에 맞춰 정책 경사를 추정한다. [PDF 1쪽](https://proceedings.mlr.press/v80/fujita18a/fujita18a.pdf#page=1) · [PDF 2쪽](https://proceedings.mlr.press/v80/fujita18a/fujita18a.pdf#page=2)

## Core Idea and Contribution

- 경계 밖 표본의 개별 점수 대신 꼬리 확률의 경사를 이용하며, 논문의 가정에서 기존 추정량과 기대값이 같고 분산이 더 크지 않음을 보인다. [PDF 2쪽](https://proceedings.mlr.press/v80/fujita18a/fujita18a.pdf#page=2) · [PDF 3쪽](https://proceedings.mlr.press/v80/fujita18a/fujita18a.pdf#page=3) · [PDF 4쪽](https://proceedings.mlr.press/v80/fujita18a/fujita18a.pdf#page=4)
- MuJoCo 연속제어 과제에서 같은 PPO·TRPO에 경사 추정량만 바꿔 학습 곡선과 최종 성능을 비교했다. [PDF 6쪽](https://proceedings.mlr.press/v80/fujita18a/fujita18a.pdf#page=6) · [PDF 7쪽](https://proceedings.mlr.press/v80/fujita18a/fujita18a.pdf#page=7) · [PDF 8쪽](https://proceedings.mlr.press/v80/fujita18a/fujita18a.pdf#page=8)

## Observation–State–Action Interface

Unbounded policy sample → clip → bounded executed action·gradient.

## Evaluation Scope and Claim Boundary

Continuous control의 이론·실험 비교를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v80/fujita18a.html) · [저자 project/code](https://github.com/pfnet-research/capg).

## 검색 태그 근거

가우시안 정책에서 행동이 허용 범위 끝으로 잘리는 확률 질량을 적분해 정책 기울기를 추정한다. MuJoCo에서 TRPO·PPO에 적용했으며, 여기서 다루는 클리핑은 환경의 행동 한계다. [원문 3쪽](https://proceedings.mlr.press/v80/fujita18a/fujita18a.pdf#page=3) · [원문 6쪽](https://proceedings.mlr.press/v80/fujita18a/fujita18a.pdf#page=6)

## Why This Paper Is Here — Researcher Interpretation

C3에서 실행 동치 action의 확률 질량을 합치는 원리의 foundation이다.

## Verification Boundary

clipping preimage, policy family, gradient unbiasedness 조건을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
