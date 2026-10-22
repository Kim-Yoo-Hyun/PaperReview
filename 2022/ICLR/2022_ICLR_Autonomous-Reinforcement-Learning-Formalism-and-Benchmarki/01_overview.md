# Autonomous Reinforcement Learning: Formalism and Benchmarking

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2022 / ICLR
- Category: Robotics Foundations: Robot Learning
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: RL, evaluation, learning-foundation
- Aliases: EARL
- Official paper: https://openreview.net/forum?id=nkaba3ND7B5
- Venue verification: https://iclr.cc/Downloads/2022
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. OpenReview live challenge; ICLR 공식 Downloads/2022 목록의 exact title와 기존 accepted manuscript 기록을 교차 대조했다. 현재 content는 arXiv abstract 기준.

## Problem and Importance

Human reset에 의존하는 episodic RL을 연속적으로 변하는 환경의 자율 학습으로 확장한다.

## Core Idea and Contribution

Autonomous RL formalism과 최소 개입을 평가하는 EARL benchmark를 제안한다.

## Observation–State–Action Interface

연속 환경 상호작용·개입 budget → 학습 policy → 별도 평가.

## Evaluation Scope and Claim Boundary

다양한 simulated task에서 reset 의존성과 기존 방법 한계를 분석한다.

근거: [공식 paper/abstract](https://openreview.net/forum?id=nkaba3ND7B5). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C5의 continuing/deployed 평가와 human intervention 기준을 제공한다.

## Verification Boundary

reset 정의, intervention 비용, 평가 rollout의 학습 유입, denominator을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
