# Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / CoRL
- Authors: Mitsuhiko Nakamoto, Oier Mees, Aviral Kumar, Sergey Levine
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: value-guidance, offline-RL, generalist-policy
- Aliases: V-GPS
- Official paper: https://proceedings.mlr.press/v270/nakamoto25a.html
- Venue verification: https://proceedings.mlr.press/v270/nakamoto25a.html
- Code/Project: https://nakamotoo.github.io/V-GPS
- Code: https://github.com/nakamotoo/V-GPS
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  CoRL 2024 event; PMLR volume 270 published 2025. Registry year uses event year. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

범용 정책의 혼합 품질 시연에는 더 나은 행동을 선별할 가치 정보가 부족하다.

## Core Idea and Contribution

Offline RL로 학습한 value를 사용하여 범용 정책이 생성한 행동 후보를 추론 시 선택한다.

## Observation–State–Action Interface

고정 정책의 action samples → 학습 value scoring → 실행 행동. 정책 가중치 갱신과 구분한다.

## Evaluation Scope and Claim Boundary

서로 다른 다섯 정책과 여러 실제 로봇·조작 과제에서 value guidance를 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/nakamoto25a.html) · [저자 project/code](https://nakamotoo.github.io/V-GPS) · [공식 code](https://github.com/nakamotoo/V-GPS). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

단일 정책을 RL로 갱신하는 방법이 추론 후보 선택보다 필요한 이유를 검증할 직접 대조군이다.

## Verification Boundary

후보 수와 latency, value 데이터 범위, 정책별 action normalization을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
