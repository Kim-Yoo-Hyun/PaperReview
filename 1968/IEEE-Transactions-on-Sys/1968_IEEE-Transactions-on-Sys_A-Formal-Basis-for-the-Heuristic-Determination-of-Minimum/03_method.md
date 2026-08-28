# Method — A Formal Basis for the Heuristic Determination of Minimum Cost Paths

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1968 / IEEE Transactions on Systems Science and Cybernetics
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, Planning, graph search, A*
- Official paper: https://doi.org/10.1109/TSSC.1968.300136
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; proof details and experimental claims remain UNVERIFIED.

## Pipeline

누적 비용과 추정 잔여 비용을 결합해 후보 노드를 우선 확장하며, heuristic 조건 아래 최적 경로 탐색 성질을 분석한다.

## Interface

명시적 graph state와 transition cost를 받아 discrete plan을 출력하는 task/planning 계층이다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
