# Successor Features for Transfer in Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Problem and Bottleneck

동역학이 같고 보상만 달라지는 과제 사이의 전이를 다룬다.

## Formulation and Robotics Loop

상태·동작 → successor feature; 새 보상 가중치 → 정책 집합에서 행동 선택.

미래 feature 방문을 보상 가중치와 분리하고 generalized policy improvement로 기존 정책들을 재사용한다.

## Assumptions to Verify

공유 동역학·보상 선형성·feature 근사·정책 coverage.

위 항목은 연구자의 확인 질문이며 논문이 명시한 가정·실패로 확정한 것이 아니다.

## Prior Work and Why It Matters

UVFA·policy improvement → successor features → 목표/보상 전이와 cross-embodiment의 조건 비교.

보상 전이와 로봇 동역학 전이를 혼동하지 않게 하는 명확한 이론·로봇 비교 기준이다.

## Evidence Boundary

[공식 paper/abstract](https://proceedings.neurips.cc/paper/2017/hash/350db081a661525235354dd3e19b8c05-Abstract.html). 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
