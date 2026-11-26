# A State-Distribution Matching Approach to Non-Episodic Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2022 / ICML
- Authors: Archit Sharma, Rehaan Ahmad, Chelsea Finn
- Category: Robotics Foundations: Robot Learning
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: RL, evaluation, learning-foundation, reset-free learning
- Aliases: MEDAL
- Official paper: https://proceedings.mlr.press/v162/sharma22a.html
- Venue verification: https://proceedings.mlr.press/v162/sharma22a.html
- Code/Project: not identified
- Code: not_identified
- Full-text retrieval: https://proceedings.mlr.press/v162/sharma22a/sharma22a.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

MEDAL은 외부에서 매번 초기화해 주기 어려운 연속제어 과제에서 역방향 정책이 소수 전문가 시연의 상태 분포로 로봇을 되돌리도록 학습한다. [PDF 1쪽](https://proceedings.mlr.press/v162/sharma22a/sharma22a.pdf#page=1) · [PDF 3쪽](https://proceedings.mlr.press/v162/sharma22a/sharma22a.pdf#page=3)

## Core Idea and Contribution

- 시연과 현재 상태를 구분하는 판별기에서 역방향 보상을 얻고, 정방향 정책과 역방향 정책을 번갈아 실행한다. [PDF 4쪽](https://proceedings.mlr.press/v162/sharma22a/sharma22a.pdf#page=4) · [PDF 5쪽](https://proceedings.mlr.press/v162/sharma22a/sharma22a.pdf#page=5)
- EARL의 탁상 물체 이동, 문 닫기, 못 삽입에서 재시작 분포를 달리하는 방법들과 정방향 과제 성능을 비교했다. [PDF 6쪽](https://proceedings.mlr.press/v162/sharma22a/sharma22a.pdf#page=6) · [PDF 7쪽](https://proceedings.mlr.press/v162/sharma22a/sharma22a.pdf#page=7)

## Observation–State–Action Interface

Demonstration states → reset policy → forward learner.

## Evaluation Scope and Claim Boundary

EARL의 sparse-reward continuous control task를 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v162/sharma22a.html).

## 검색 태그 근거

MEDAL은 시연과 에이전트 방문 상태를 구별하는 판별기로 역방향 보상을 구성한다. 순·역 정책을 번갈아 학습해 Sawyer 문 열기·페그 과제 등의 연속 상호작용을 평가한다. [원문 5쪽](https://proceedings.mlr.press/v162/sharma22a/sharma22a.pdf#page=5) · [원문 7쪽](https://proceedings.mlr.press/v162/sharma22a/sharma22a.pdf#page=7)

## Why This Paper Is Here — Researcher Interpretation

C5의 reset-induced state distribution 자체가 신규 문제가 아님을 보여준다.

## Verification Boundary

demonstration 접근, forward/backward budget, independent evaluation을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
