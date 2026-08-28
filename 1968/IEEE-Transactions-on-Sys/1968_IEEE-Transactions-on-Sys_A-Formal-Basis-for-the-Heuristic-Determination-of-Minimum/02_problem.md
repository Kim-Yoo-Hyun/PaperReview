# Problem — A Formal Basis for the Heuristic Determination of Minimum Cost Paths

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1968 / IEEE Transactions on Systems Science and Cybernetics
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, Planning, graph search, A*
- Official paper: https://doi.org/10.1109/TSSC.1968.300136
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; proof details and experimental claims remain UNVERIFIED.

## Target Problem and Assumptions

비용 그래프에서 목표까지의 잔여 비용을 추정하는 heuristic을 이용해 최소비용 경로를 효율적으로 찾는 문제를 다룬다.

## Closed-Loop Position

명시적 graph state와 transition cost를 받아 discrete plan을 출력하는 task/planning 계층이다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
