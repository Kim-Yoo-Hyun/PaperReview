# Towards Generalizable Safety in Crowd Navigation via Conformal Uncertainty Handling

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, evaluation, robustness
- Aliases:
- Official paper: https://proceedings.mlr.press/v305/yao25a.html
- Venue verification: https://proceedings.mlr.press/v305/yao25a.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다.

## Problem and Importance

군중 행동 분포가 바뀌면 학습된 navigation policy 안전성이 저하될 수 있다.

## Core Idea and Contribution

Adaptive conformal prediction의 불확실성을 관측에 넣고 constrained RL로 행동을 조절한다.

## Observation–State–Action Interface

Pedestrian 예측·uncertainty → navigation policy → 이동 행동.

## Evaluation Scope and Claim Boundary

속도·행동 정책·집단 변화 및 실로봇 군중 navigation을 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/yao25a.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

GAP-P 계열에서 uncertainty 추가 자체를 새로운 navigation 기여로 삼지 않게 하는 직접 선행이다.

## Verification Boundary

보장의 단위, reactive crowd, calibration update와 intervention 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
