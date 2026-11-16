# Policy invariance under reward transformations: Theory and application to reward shaping

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 1999 / ICML
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: reinforcement-learning, reward-shaping, policy-invariance, potential-function
- Aliases: Potential-Based Reward Shaping, PBRS
- Official paper: https://people.eecs.berkeley.edu/~russell/papers/icml99-shaping.pdf
- Venue verification: https://people.eecs.berkeley.edu/~russell/publications
- Code/Project:
- Code: not_identified
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 저자 원문 abstract와 Russell의 ICML-99 publication 기록 확인. PDF는 웹에서 확인했으며 local cache는 저장하지 않았다. ACM endpoint는 403으로 접근 실패해 DOI를 추정하지 않았다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

학습을 돕는 보상 변경이 원래 최적 정책을 바꾸는 조건을 묻는다.

## Core Idea and Contribution

상태 potential의 차이로 구성하는 보상 변환의 정책 보존 조건과 그 필요성을 분석한다.

## Observation–State–Action Interface

MDP의 상태 전이·원 보상 → potential 기반 shaping → 정책 최적화.

## Evaluation Scope and Claim Boundary

정책 불변성 분석과 거리·부분 목표 potential의 학습 예제를 제시한다. VLA 평가 논문은 아니다.

근거: [공식 paper/abstract](https://people.eecs.berkeley.edu/~russell/papers/icml99-shaping.pdf). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLM progress·단계 보상·접촉 보상으로 목표를 변경하는지 판단할 공통 이론 원전이므로 CORE다.

## Verification Boundary

본문에서 확인할 항목: 할인율·종료 potential·Markov 상태·history 의존 보상. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
