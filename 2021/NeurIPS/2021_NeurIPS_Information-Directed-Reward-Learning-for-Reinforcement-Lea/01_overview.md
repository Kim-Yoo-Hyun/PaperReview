# Information Directed Reward Learning for Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: David Lindner, Matteo Turchetta, Sebastian Tschiatschek, Kamil Ciosek, Andreas Krause
- Category: Robotics Foundations: Robot Learning
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: reward-learning, robot-learning, evaluation
- Aliases: IDRL
- Official paper: https://proceedings.neurips.cc/paper/2021/hash/1fa6269f58898f0e809575c9a48747ef-Abstract.html
- Venue verification: https://proceedings.neurips.cc/paper/2021/hash/1fa6269f58898f0e809575c9a48747ef-Abstract.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

Reward 정확도 대신 정책 결정에 유용한 expert query를 고른다.

## Core Idea and Contribution

잠재 최적 정책 간 return 차이에 대한 information gain으로 query를 선택한다.

## Observation–State–Action Interface

Bayesian reward belief·policy 후보 → query → expert feedback.

## Evaluation Scope and Claim Boundary

여러 환경과 query 유형에서 label efficiency를 평가한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper/2021/hash/1fa6269f58898f0e809575c9a48747ef-Abstract.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C4의 decision-relevant reward audit 주장의 직접 foundation이다.

## Verification Boundary

reward prior, policy 후보 생성, expert noise, compute 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
