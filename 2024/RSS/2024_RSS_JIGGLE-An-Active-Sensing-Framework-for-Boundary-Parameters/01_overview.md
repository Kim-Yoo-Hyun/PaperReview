# JIGGLE: An Active Sensing Framework for Boundary Parameters Estimation in Deformable Surgical Environments

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2024 / RSS
- Authors: Nikhil Uday Shinde, Xiao Liang, Fei Liu, Yutong Zhang, Florian Richter, Sylvia Lee Herbert, Michael C. Yip
- 저자 판본: 학회 서지와 표기가 다른 저자의 인쇄명은 Sylvia Herbert이다. [PDF 1쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=1) · [학회 서지](https://www.roboticsproceedings.org/rss20/p007.html)
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, evaluation, manipulation, active perception, state estimation
- Aliases:
- Official paper: https://www.roboticsproceedings.org/rss20/p007.html
- Venue verification: https://www.roboticsproceedings.org/rss20/p007.html
- Code/Project: not identified
- Code: not_identified
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p007.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다. 평가 조건은 04_evaluation.md에 쪽수와 함께 기록했다.

## Problem and Importance

JIGGLE은 조직을 움직일 때 보이는 변형으로 숨은 부착 부위를 추정하고, 다음 조작에서 얻을 정보와 조직에 가해지는 비용을 함께 고려한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=1) · [PDF 3쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=3)

## Core Idea and Contribution

- 미분 가능한 연체 시뮬레이터와 확장 칼만 필터로 부착 파라미터의 분포를 갱신하고 정보 이득과 안전 비용으로 탐색 동작을 정한다. [PDF 4쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=4) · [PDF 5쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=5) · [PDF 8쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=8)
- 절단·봉합으로 부착 상태가 변하는 시뮬레이션과 동물 조직의 스테레오 내시경 관측으로 추정 결과를 평가했다. 추정한 부착 강도의 척도는 시뮬레이터 파라미터다. [PDF 2쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=2) · [PDF 10쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=10) · [PDF 11쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=11) · [PDF 12쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=12)

## Observation–State–Action Interface

Stereo 관측·조작 → attachment 추정 → sensing action.

## Evaluation Scope and Claim Boundary

절단과 봉합으로 부착 관계가 변하는 실험은 시뮬레이션에서 수행했다. 동물 조직 실험은 스테레오 내시경 영상에서 봉합으로 고정된 부위를 추정하는 과제였다. [PDF 2쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=2) · [PDF 10쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=10) · [PDF 11쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=11) · [PDF 12쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=12)

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss20/p007.html).

## 검색 태그 근거

JIGGLE은 변형 관측으로 조직의 부착 위치를 필터링하고, 변형 에너지와 정보 이득으로 다음 탐색 동작을 계획한다. 전체 능동 탐색은 시뮬레이션에서 시험하고 실물 조직 영상에서는 부착 위치 추정을 평가했다. [원문 8쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=8) · [원문 11쪽](https://www.roboticsproceedings.org/rss20/p007.pdf#page=11)

## Why This Paper Is Here — Researcher Interpretation

물성·boundary 식별과 task-oriented probing을 구별하는 GAP-DE의 직접 선행이다.

## Verification Boundary

재료 모델과 attachment 가정, 안전 비용 정의을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
