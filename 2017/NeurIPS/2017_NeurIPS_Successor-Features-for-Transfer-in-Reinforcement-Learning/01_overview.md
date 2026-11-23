# Successor Features for Transfer in Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
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
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

동역학이 같고 보상만 달라지는 과제 사이의 전이를 다룬다.

## Core Idea and Contribution

미래 feature 방문을 보상 가중치와 분리하고 generalized policy improvement로 기존 정책들을 재사용한다.

## Observation–State–Action Interface

상태·동작 → successor feature; 새 보상 가중치 → 정책 집합에서 행동 선택.

## Evaluation Scope and Claim Boundary

전이 성능 정리와 navigation·시뮬레이션 robot arm 실험을 보고한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper/2017/hash/350db081a661525235354dd3e19b8c05-Abstract.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

보상 전이와 로봇 동역학 전이를 혼동하지 않게 하는 명확한 이론·로봇 비교 기준이다.

## Verification Boundary

본문에서 확인할 항목: 공유 동역학·보상 선형성·feature 근사·정책 coverage. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
