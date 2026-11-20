# Colored Noise in PPO: Improved Exploration and Performance through Correlated Action Sampling

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Jakob Hollenstein, Georg Martius, Justus Piater
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: PPO, exploration, temporal correlation, action noise
- Aliases: Colored Noise PPO
- Official paper: https://ojs.aaai.org/index.php/AAAI/article/view/29139
- Venue verification: https://ojs.aaai.org/index.php/AAAI/article/view/29139
- Code/Project: https://github.com/jkbjh/cn-ppo-paper-code
- Code: https://github.com/jkbjh/cn-ppo-paper-code
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 직접 HTML 접근 제한은 공식 사이트의 검색 색인 abstract/BibTeX 및 저자 abstract/project 자료로 교차 확인; HTML 전면 열람으로 기록하지 않음.

## Problem and Importance

PPO의 시간적으로 독립적인 action noise가 탐색 trajectory의 구조를 놓칠 수 있다.

## Core Idea and Contribution

시간 상관을 갖는 colored noise로 stochastic action sampling을 바꾸고 noise color와 병렬 환경 수의 영향을 비교한다.

## Observation–State–Action Interface

On-policy stochastic actor의 action sampling을 바꾼다. VLA나 양팔 관계 학습을 직접 제안한 것은 아니다.

## Evaluation Scope and Claim Boundary

On-policy RL의 correlated/white noise와 병렬 data 수집 조건을 비교한다. 이 조사에서 실제 로봇 trial은 확인하지 않았다.

근거: [공식 paper/abstract](https://ojs.aaai.org/index.php/AAAI/article/view/29139) · [저자 project/code](https://github.com/jkbjh/cn-ppo-paper-code). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

복잡한 관계 noise 학습 전에 비교해야 할 단순 시간 상관 탐색 baseline이다.

## Verification Boundary

행동 likelihood와 trajectory correlation·noise 재사용·seed/환경 수을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
