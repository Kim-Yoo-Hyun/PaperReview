# Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 1999 / Artificial Intelligence
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
- Full-text retrieval: https://ics.uci.edu/~dechter/courses/ics-295/winter-2018/papers/Sutton-Precup-Singh-AIJ99.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

옵션은 여러 시간 단계에 걸친 폐루프 행동을 하나의 선택으로 나타내며, MDP 위에서 옵션을 고르는 문제를 준마르코프 결정 과정으로 기술할 수 있다. [PDF 1쪽](https://ics.uci.edu/~dechter/courses/ics-295/winter-2018/papers/Sutton-Precup-Singh-AIJ99.pdf#page=1) · [PDF 6쪽](https://ics.uci.edu/~dechter/courses/ics-295/winter-2018/papers/Sutton-Precup-Singh-AIJ99.pdf#page=6)

## Core Idea and Contribution

- 시작 상태 집합·내부 정책·종료 규칙으로 옵션을 정의하고 시간 추상화를 포함하는 계획과 가치 학습을 전개했다. [PDF 6쪽](https://ics.uci.edu/~dechter/courses/ics-295/winter-2018/papers/Sutton-Precup-Singh-AIJ99.pdf#page=6) · [PDF 7쪽](https://ics.uci.edu/~dechter/courses/ics-295/winter-2018/papers/Sutton-Precup-Singh-AIJ99.pdf#page=7) · [PDF 8쪽](https://ics.uci.edu/~dechter/courses/ics-295/winter-2018/papers/Sutton-Precup-Singh-AIJ99.pdf#page=8)
- 실행 중 다른 옵션으로 전환하는 조건과, 옵션 전체가 끝날 때까지 기다리지 않고 부분 경험으로 옵션 모형을 학습하는 방법을 제시했다. [PDF 17쪽](https://ics.uci.edu/~dechter/courses/ics-295/winter-2018/papers/Sutton-Precup-Singh-AIJ99.pdf#page=17) · [PDF 21쪽](https://ics.uci.edu/~dechter/courses/ics-295/winter-2018/papers/Sutton-Precup-Singh-AIJ99.pdf#page=21) · [PDF 22쪽](https://ics.uci.edu/~dechter/courses/ics-295/winter-2018/papers/Sutton-Precup-Singh-AIJ99.pdf#page=22)

## Observation–State–Action Interface

상태 → option 선택 → 내부 정책 실행 → 종료 또는 중단 → 다음 결정.

## Evaluation Scope and Claim Boundary

시간 추상화의 이론과 학습·계획 예제를 다룬다. VLA chunk가 자동으로 option이라는 주장은 없다.

근거: [공식 paper/abstract](https://www.sciencedirect.com/science/article/pii/S0004370299000521).

## 검색 태그 근거

옵션은 시작할 수 있는 상태 집합, 내부 정책, 종료 조건으로 정의된다. 방 사이를 이동하는 격자 예제로 옵션 단위 계획·가치학습을 설명하고, 실행 중 옵션을 중단할 수 있는 조건도 분석했다. [원문 6쪽](https://ics.uci.edu/~dechter/courses/ics-295/winter-2018/papers/Sutton-Precup-Singh-AIJ99.pdf#page=6) · [원문 12쪽](https://ics.uci.edu/~dechter/courses/ics-295/winter-2018/papers/Sutton-Precup-Singh-AIJ99.pdf#page=12) · [원문 18쪽](https://ics.uci.edu/~dechter/courses/ics-295/winter-2018/papers/Sutton-Precup-Singh-AIJ99.pdf#page=18)

## Why This Paper Is Here — Researcher Interpretation

가변 chunk·재계획·중단을 해석할 기본 formulation을 보완하며 계층형 주제로 전환하라는 의미는 아니다.

## Verification Boundary

본문에서 확인할 항목: initiation·termination·closed-loop 조건·물리 시간 할인. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
