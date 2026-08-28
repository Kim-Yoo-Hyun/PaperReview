# Problem — Hierarchical Task and Motion Planning in the Now

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2011 / ICRA
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, Planning, task and motion planning, manipulation
- Official paper: https://doi.org/10.1109/ICRA.2011.5980391
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; algorithmic details remain UNVERIFIED.

## Target Problem and Assumptions

긴 symbolic plan 전체를 미리 확정하면 geometric infeasibility와 실행 중 변화에 취약한 문제를 다룬다.

## Closed-Loop Position

symbolic state/goals와 robot geometry를 executable motion/action sequence로 연결한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
