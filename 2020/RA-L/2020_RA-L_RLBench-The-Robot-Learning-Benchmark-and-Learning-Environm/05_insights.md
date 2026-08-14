# Insights — RLBench: The Robot Learning Benchmark & Learning Environment

- Year/Venue: 2020 / RA-L
- Category: Benchmarks and Datasets
- Tags: Robotics, Benchmark, Imitation Learning, Reinforcement Learning, multi-task manipulation, 3D Vision
- Official paper: https://arxiv.org/abs/1909.12271
- Official PDF: https://arxiv.org/pdf/1909.12271
- Code/Project: https://github.com/stepjam/RLBench
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Paper-Supported Direction

PerAct/RVT/EquAct/SUGAR 계열을 같은 task family에서 해석하기 위한 manipulation benchmark 원 논문.

## Researcher Interpretation

- Foundation/frontier connection: `RLBench → PerAct / RVT / SUGAR → EquAct and 3D-aware VLA evaluation`
- 가장 먼저 반박할 가정: CoppeliaSim의 sensing와 dynamics가 연구 질문에 충분한 physics를 제공한다.
- 현재 gap과 연결할 때 success만 보지 않고 downstream control 또는 evaluation protocol의 변화를 확인한다.

## Limitations / Failure Modes to Audit

- 논문마다 task subset과 action mode가 달라 headline success를 직접 비교하기 어렵다.
- Simulation success가 contact robustness와 real-robot safety를 보장하지 않는다.

## Minimum Experiment

Reach, open-drawer, insert 계열 3개 task에 고정 demo 수와 variation split을 정해 2D와 3D policy를 비교한다.

## Status

`UNREAD` — 이 노트는 official abstract 기반의 reading scaffold이며 정독 완료를 의미하지 않는다.
