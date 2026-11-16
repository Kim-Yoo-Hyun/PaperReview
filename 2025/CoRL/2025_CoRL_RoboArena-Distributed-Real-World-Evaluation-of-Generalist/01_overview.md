# RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, Benchmark, real-robot, pairwise-evaluation
- Aliases: RoboArena
- Official paper: https://proceedings.mlr.press/v305/atreya25a.html
- Venue verification: https://proceedings.mlr.press/v305/atreya25a.html
- Code/Project: https://robo-arena.github.io/
- Code: https://github.com/pranavatreya/roboarena_backend
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다.

## Problem and Importance

기관마다 task·환경이 달라 generalist policy의 실로봇 순위를 비교하기 어렵다.

## Core Idea and Contribution

분산 평가자가 두 정책을 double-blind로 비교하고 선호 결과를 통합한다.

## Observation–State–Action Interface

같은 평가 상황의 두 정책 rollout → 선호 비교 → 전체 정책 순위.

## Evaluation Scope and Claim Boundary

DROID 플랫폼을 사용하는 여러 기관에서 generalist policy를 실로봇으로 비교한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/atreya25a.html) · [저자 project/code](https://robo-arena.github.io/) · [공식 code](https://github.com/pranavatreya/roboarena_backend). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

LIBERO-Plus·THE COLOSSEUM의 고정 benchmark와 구별되는 실환경 평가 기준을 보완한다.

## Verification Boundary

pairwise reset 조건, task 선택 편향, 선호 aggregation과 불확실성을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
