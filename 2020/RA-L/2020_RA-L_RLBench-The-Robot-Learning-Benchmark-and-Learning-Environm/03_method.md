# Method — RLBench: The Robot Learning Benchmark & Learning Environment

- Year/Venue: 2020 / RA-L
- Category: Benchmarks and Datasets
- Tags: Robotics, Benchmark, Imitation Learning, Reinforcement Learning, multi-task manipulation, 3D Vision
- Official paper: https://arxiv.org/abs/1909.12271
- Official PDF: https://arxiv.org/pdf/1909.12271
- Code/Project: https://github.com/stepjam/RLBench
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Pipeline

- 100개 hand-designed manipulation task와 task variation을 제공한다.
- RGB, depth, segmentation과 proprioception을 포함한 multi-modal observation을 지원한다.
- Motion-planned demonstration 생성과 새 task 검증 도구를 제공한다.

## Interface

Task environment가 observation, action mode, demonstration과 success condition을 제공하는 robot-learning API다.

## Implementation Audit

- Objective, horizon, control rate와 architecture detail은 full text 정독 후 확정한다.
- Official abstract가 지지하지 않는 loss, data size 또는 hardware detail은 추정하지 않는다.
- 후속 구현에서는 `RLBench → PerAct / RVT / SUGAR → EquAct and 3D-aware VLA evaluation`의 앞뒤 논문과 공통 interface를 먼저 맞춘다.
