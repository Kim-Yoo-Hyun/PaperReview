# A State-Distribution Matching Approach to Non-Episodic Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2022 / ICML
- Authors: Archit Sharma, Rehaan Ahmad, Chelsea Finn
- Category: Robotics Foundations: Robot Learning
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: RL, evaluation, learning-foundation
- Aliases: MEDAL
- Official paper: https://proceedings.mlr.press/v162/sharma22a.html
- Venue verification: https://proceedings.mlr.press/v162/sharma22a.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

비에피소드 RL에서 backward policy가 어떤 분포로 reset할지 정한다.

## Core Idea and Contribution

시연 state 분포를 맞추는 backward policy로 task-relevant reset을 학습한다.

## Observation–State–Action Interface

Demonstration states → reset policy → forward learner.

## Evaluation Scope and Claim Boundary

EARL의 sparse-reward continuous control task를 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v162/sharma22a.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C5의 reset-induced state distribution 자체가 신규 문제가 아님을 보여준다.

## Verification Boundary

demonstration 접근, forward/backward budget, independent evaluation을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
