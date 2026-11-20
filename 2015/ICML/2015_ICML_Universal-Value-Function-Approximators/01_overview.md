# Universal Value Function Approximators

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Tom Schaul, Daniel Horgan, Karol Gregor, David Silver
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: reinforcement-learning, goal-conditioning, value-function, transfer
- Aliases: UVFA
- Official paper: https://proceedings.mlr.press/v37/schaul15.html
- Venue verification: https://proceedings.mlr.press/v37/schaul15.html
- Code/Project:
- Code: not_identified
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

상태뿐 아니라 목표가 달라질 때도 하나의 가치함수를 일반화한다.

## Core Idea and Contribution

상태와 목표를 입력으로 받는 가치함수와 분리된 embedding 학습을 제안하고 보상 기반 RL로 연결한다.

## Observation–State–Action Interface

상태 s·목표 g → 공유 가치 추정 V(s,g) → 목표 조건부 행동 선택.

## Evaluation Scope and Claim Boundary

학습하지 않은 목표로 가치와 정책을 일반화하는 실험을 보고한다. 언어 지시나 다중 embodiment 보장은 아니다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v37/schaul15.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

HER·HIQL·목표 조건부 critic과 단일 VLA의 지시별 가치 표현을 이해하는 원전이므로 CORE다.

## Verification Boundary

본문에서 확인할 항목: 목표 표현·목표 holdout·목표별 coverage·value와 policy 일반화의 구분. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
