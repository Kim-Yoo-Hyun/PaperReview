# Problem — RLBench: The Robot Learning Benchmark & Learning Environment

- Year/Venue: 2020 / RA-L
- Category: Benchmarks and Datasets
- Tags: Robotics, Benchmark, Imitation Learning, Reinforcement Learning, multi-task manipulation, 3D Vision
- Official paper: https://arxiv.org/abs/1909.12271
- Official PDF: https://arxiv.org/pdf/1909.12271
- Code/Project: https://github.com/stepjam/RLBench
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Target Problem

Few-shot, multi-task, imitation, reinforcement learning과 classical planning을 넓은 manipulation task 집합에서 비교할 공통 environment가 필요하다.

## Core Assumptions

- CoppeliaSim의 sensing와 dynamics가 연구 질문에 충분한 physics를 제공한다.
- Waypoint motion planner가 만든 demonstration이 learned policy 평가의 적절한 expert data다.

## Closed-Loop Position

이 논문은 현재 robotics loop에서 `RLBench → PerAct / RVT / SUGAR → EquAct and 3D-aware VLA evaluation` 연결을 담당한다. 실제 정독 시 observation/state/action/control 중 어느 interface를 고정하고 어느 부분을 학습하는지 확인한다.

## Falsification Question

논문마다 task subset과 action mode가 달라 headline success를 직접 비교하기 어렵다.
