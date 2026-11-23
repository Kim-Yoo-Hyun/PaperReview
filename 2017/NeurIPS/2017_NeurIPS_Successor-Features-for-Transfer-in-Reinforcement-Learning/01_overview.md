# Successor Features for Transfer in Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2017 / NeurIPS
- Authors: Andre Barreto, Will Dabney, Remi Munos, Jonathan J. Hunt, Tom Schaul, Hado van Hasselt, David Silver
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: reinforcement-learning, transfer, successor-features, policy-improvement
- Aliases: Successor Features, GPI
- Official paper: https://proceedings.neurips.cc/paper/2017/hash/350db081a661525235354dd3e19b8c05-Abstract.html
- Venue verification: https://proceedings.neurips.cc/paper/2017/hash/350db081a661525235354dd3e19b8c05-Abstract.html
- Code/Project:
- Code: not_identified
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 환경 동역학이 같고 보상만 달라지는 과제에서 기존 정책이 예측한 미래 특징을 재사용해 새 과제에 전이한다. [PDF 1쪽](https://proceedings.neurips.cc/paper/2017/file/350db081a661525235354dd3e19b8c05-Paper.pdf#page=1)

## Core Idea and Contribution

- 가치를 할인된 미래 특징의 기대값과 보상 가중치로 분해하고, 여러 정책의 가치 추정을 이용하는 일반화된 정책 개선에 대해 성능 보장을 유도했다. [PDF 3쪽](https://proceedings.neurips.cc/paper/2017/file/350db081a661525235354dd3e19b8c05-Paper.pdf#page=3) · [PDF 5쪽](https://proceedings.neurips.cc/paper/2017/file/350db081a661525235354dd3e19b8c05-Paper.pdf#page=5)
- 보상 조건이 바뀌는 2차원 내비게이션과 시뮬레이션 로봇팔에서 새 과제를 처음 만났을 때와 추가 학습한 뒤의 전이를 평가했다. [PDF 6쪽](https://proceedings.neurips.cc/paper/2017/file/350db081a661525235354dd3e19b8c05-Paper.pdf#page=6) · [PDF 7쪽](https://proceedings.neurips.cc/paper/2017/file/350db081a661525235354dd3e19b8c05-Paper.pdf#page=7)

## Observation–State–Action Interface

상태·동작 → successor feature; 새 보상 가중치 → 정책 집합에서 행동 선택.

## Evaluation Scope and Claim Boundary

전이 성능 정리와 navigation·시뮬레이션 robot arm 실험을 보고한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper/2017/hash/350db081a661525235354dd3e19b8c05-Abstract.html). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

보상 전이와 로봇 동역학 전이를 혼동하지 않게 하는 명확한 이론·로봇 비교 기준이다.

## Verification Boundary

본문에서 확인할 항목: 공유 동역학·보상 선형성·feature 근사·정책 coverage. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
