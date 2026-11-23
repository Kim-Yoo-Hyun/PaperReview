# Clipped Action Policy Gradient

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2018 / ICML
- Authors: Yasuhiro Fujita, Shin-ichi Maeda
- Category: Robotics Foundations: Robot Learning
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: RL, evaluation, learning-foundation
- Aliases: CAPG
- Official paper: https://proceedings.mlr.press/v80/fujita18a.html
- Venue verification: https://proceedings.mlr.press/v80/fujita18a.html
- Code/Project: https://github.com/pfnet-research/capg
- Code: https://github.com/pfnet-research/capg
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

Action clipping을 무시한 policy gradient의 불필요한 분산을 줄인다.

## Core Idea and Contribution

실행 action이 clipping되는 사실을 이용한 unbiased estimator를 제안한다.

## Observation–State–Action Interface

Unbounded policy sample → clip → bounded executed action·gradient.

## Evaluation Scope and Claim Boundary

Continuous control의 이론·실험 비교를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v80/fujita18a.html) · [저자 project/code](https://github.com/pfnet-research/capg). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C3에서 실행 동치 action의 확률 질량을 합치는 원리의 foundation이다.

## Verification Boundary

clipping preimage, policy family, gradient unbiasedness 조건을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
