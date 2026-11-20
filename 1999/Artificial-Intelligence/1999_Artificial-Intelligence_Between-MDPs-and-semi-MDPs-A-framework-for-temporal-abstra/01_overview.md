# Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Richard S. Sutton, Doina Precup, Satinder Singh
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: reinforcement-learning, temporal-abstraction, options, semi-MDP
- Aliases: Options framework
- Official paper: https://api.crossref.org/works/10.1016/S0004-3702(99)00052-1
- Venue verification: https://www.sciencedirect.com/science/article/pii/S0004370299000521
- Code/Project:
- Code: not_identified
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

서로 다른 시간 길이의 행동과 정책을 같은 RL 형식으로 다룬다.

## Core Idea and Contribution

여러 step 동안 실행되는 closed-loop option과 SMDP를 연결하고 중단·intra-option 학습을 분석한다.

## Observation–State–Action Interface

상태 → option 선택 → 내부 정책 실행 → 종료 또는 중단 → 다음 결정.

## Evaluation Scope and Claim Boundary

시간 추상화의 이론과 학습·계획 예제를 다룬다. VLA chunk가 자동으로 option이라는 주장은 없다.

근거: [공식 paper/abstract](https://www.sciencedirect.com/science/article/pii/S0004370299000521). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

가변 chunk·재계획·중단을 해석할 기본 formulation을 보완하며 계층형 주제로 전환하라는 의미는 아니다.

## Verification Boundary

본문에서 확인할 항목: initiation·termination·closed-loop 조건·물리 시간 할인. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
