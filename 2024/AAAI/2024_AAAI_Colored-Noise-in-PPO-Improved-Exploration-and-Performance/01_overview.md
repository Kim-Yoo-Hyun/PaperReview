# Colored Noise in PPO: Improved Exploration and Performance through Correlated Action Sampling

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2024 / AAAI
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
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 직접 HTML 접근 제한은 공식 사이트의 검색 색인 abstract/BibTeX 및 저자 abstract/project 자료로 교차 확인; HTML 전면 열람으로 기록하지 않음. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 PPO가 연속 행동을 표집할 때 탐색 잡음의 시간적 상관을 조절하면 학습 성능이 어떻게 달라지는지 평가한다. [PDF 1쪽](https://ojs.aaai.org/index.php/AAAI/article/download/29139/30155#page=1)

## Core Idea and Contribution

- 평균·분산을 조절하는 정책에 시간 상관이 있는 잡음 과정을 적용해 백색에서 분홍색 잡음까지 서로 다른 상관 수준을 비교했다. [PDF 2쪽](https://ojs.aaai.org/index.php/AAAI/article/download/29139/30155#page=2) · [PDF 3쪽](https://ojs.aaai.org/index.php/AAAI/article/download/29139/30155#page=3)
- 시뮬레이션에서 평균적으로 백색과 분홍색 사이의 상관이 유리했고, 한 번에 자료를 모으는 병렬 환경 수를 늘리면 더 강한 상관이 유리해지는 경향을 보고했다. [PDF 4쪽](https://ojs.aaai.org/index.php/AAAI/article/download/29139/30155#page=4) · [PDF 5쪽](https://ojs.aaai.org/index.php/AAAI/article/download/29139/30155#page=5) · [PDF 6쪽](https://ojs.aaai.org/index.php/AAAI/article/download/29139/30155#page=6)

## Observation–State–Action Interface

On-policy stochastic actor의 action sampling을 바꾼다. VLA나 양팔 관계 학습을 직접 제안한 것은 아니다.

## Evaluation Scope and Claim Boundary

On-policy RL의 correlated/white noise와 병렬 data 수집 조건을 비교한다. 이 조사에서 실제 로봇 trial은 확인하지 않았다.

근거: [공식 paper/abstract](https://ojs.aaai.org/index.php/AAAI/article/view/29139) · [저자 project/code](https://github.com/jkbjh/cn-ppo-paper-code). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

복잡한 관계 noise 학습 전에 비교해야 할 단순 시간 상관 탐색 baseline이다.

## Verification Boundary

행동 likelihood와 trajectory correlation·noise 재사용·seed/환경 수을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
