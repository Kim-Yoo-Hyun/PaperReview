# Reinforcement learning in robotics: A survey

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2013 / IJRR
- Authors: Jens Kober, J. Andrew Bagnell, Jan Peters
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: reinforcement-learning, Robotics, survey, sample-efficiency
- Aliases: Kober robotics RL survey
- Official paper: https://api.crossref.org/works/10.1177/0278364913495721
- Venue verification: https://journals.sagepub.com/doi/abs/10.1177/0278364913495721
- Code/Project: https://www.ias.informatik.tu-darmstadt.de/Publications/BibTex?id=10613
- Code: not_identified
- Full-text retrieval: https://www.jenskober.de/publications/Kober2013IJRR.pdf
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

로봇 강화학습 서베이로, 실제 상호작용의 비용과 고차원 제어 문제를 알고리즘·표현·사전지식의 선택이 어떻게 다루는지 정리했다. [PDF 1쪽](https://www.jenskober.de/publications/Kober2013IJRR.pdf#page=1) · [PDF 3쪽](https://www.jenskober.de/publications/Kober2013IJRR.pdf#page=3)

## Core Idea and Contribution

- 가치함수 기반 방법과 정책 탐색을 비교하고, 학습한 동역학 모형을 활용해 실물 상호작용을 절약하는 접근을 정리했다. [PDF 9쪽](https://www.jenskober.de/publications/Kober2013IJRR.pdf#page=9) · [PDF 10쪽](https://www.jenskober.de/publications/Kober2013IJRR.pdf#page=10) · [PDF 11쪽](https://www.jenskober.de/publications/Kober2013IJRR.pdf#page=11) · [PDF 22쪽](https://www.jenskober.de/publications/Kober2013IJRR.pdf#page=22)
- 공을 컵에 넣는 과제를 사례로 동작 표현, 시연·사전지식, 시뮬레이션과 실물 학습의 역할을 추적했다. [PDF 25쪽](https://www.jenskober.de/publications/Kober2013IJRR.pdf#page=25) · [PDF 26쪽](https://www.jenskober.de/publications/Kober2013IJRR.pdf#page=26) · [PDF 27쪽](https://www.jenskober.de/publications/Kober2013IJRR.pdf#page=27) · [PDF 28쪽](https://www.jenskober.de/publications/Kober2013IJRR.pdf#page=28)

## Observation–State–Action Interface

센싱·상태 표현·정책·행동·feedback의 연구 설계 요소를 비교한다.

## Evaluation Scope and Claim Boundary

기존 로봇 학습 사례를 종합한다. 단일 benchmark의 새 성능 표나 VLA 실험은 아니다.

근거: [공식 paper/abstract](https://journals.sagepub.com/doi/abs/10.1177/0278364913495721) · [저자 project/code](https://www.ias.informatik.tu-darmstadt.de/Publications/BibTex?id=10613).

## Why This Paper Is Here — Researcher Interpretation

로봇 문제의 제약에서 연구 질문을 세우기 위한 기반 survey로 최신 VLA 방법의 전제 점검에 필요하다.

## Verification Boundary

본문에서 확인할 항목: 사례별 실제 로봇 여부·상호작용 정의·수동 설계·재개 조건. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
