# Constraint-Grounded Reinforcement Learning for Variable Impedance Control in Contact-Rich Robotic Insertion

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: variable-impedance, reinforcement-learning, insertion, force-limit
- Aliases: CG-RL
- Official paper: https://arxiv.org/abs/2609.13516
- Venue verification: https://arxiv.org/abs/2609.13516
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-09: official abstract/project 및 metadata 확인. v1 abstract 확인. 실물 검증·VLA·언어 일반화 결과로 확대하지 않는다. 새 5-note는 abstract 기반이며 전체 본문/실행/사용자 정독을 뜻하지 않는다.

## Problem and Importance

삽입의 force limit과 controller gain이 달라질 때 수동 재조정이 필요하다.

## Core Idea and Contribution

Force-limit 조건부 RL이 motion·insertion rate·gain을 요청하고 controller가 gain 범위로 투영한다.

## Observation–State–Action Interface

접촉 feedback·force limit → residual motion·속도·요청 gain.

## Evaluation Scope and Claim Boundary

Simulated oblique insertion을 평가한다. Gain 범위 보장과 force-limit 경험적 만족은 구별한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.13516). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

동작·강성 공동 RL 자체가 새롭지 않음을 보이는 controller 비교 자료다.

## Verification Boundary

Projection과 actor 범위, force constraint의 경험적/형식적 보장 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
