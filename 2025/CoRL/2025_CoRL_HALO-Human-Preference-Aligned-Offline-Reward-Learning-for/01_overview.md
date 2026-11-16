# HALO : Human Preference Aligned Offline Reward Learning for Robot Navigation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: reward-learning, human-preference, Navigation, offline-RL
- Aliases: HALO
- Official paper: https://proceedings.mlr.press/v305/seneviratne25a.html
- Venue verification: https://proceedings.mlr.press/v305/seneviratne25a.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

항법 경로의 인간 선호를 단순 성공 보상으로 표현하기 어렵다.

## Core Idea and Contribution

Expert 행동 주변 후보의 선호 순위를 학습해 시각 reward를 구성한다.

## Observation–State–Action Interface

자아시점 영상·행동 후보 → 선호 보상 → offline 정책 또는 MPC.

## Evaluation Scope and Claim Boundary

실제 Clearpath Husky 항법에서 성공·경로 특성을 비교한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/seneviratne25a.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

항법 VLA-RL에 인간 선호 보상을 붙일 때 참고할 구체적 reward-learning 대안이다.

## Verification Boundary

선호 query 생성·annotation 비용, 후보 sampling 분포, offline/online 데이터 경계을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
