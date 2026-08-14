# Evaluation — RLBench: The Robot Learning Benchmark & Learning Environment

- Year/Venue: 2020 / RA-L
- Category: Benchmarks and Datasets
- Tags: Robotics, Benchmark, Imitation Learning, Reinforcement Learning, multi-task manipulation, 3D Vision
- Official paper: https://arxiv.org/abs/1909.12271
- Official PDF: https://arxiv.org/pdf/1909.12271
- Code/Project: https://github.com/stepjam/RLBench
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Verified Evaluation Scope

- 원 논문은 100개 task와 large-scale few-shot challenge를 정의한다.
- 후속 논문 비교 시 사용 task subset, camera, action mode, demo 수와 evaluation variation을 반드시 기록한다.

## Required Comparison Fields

- Embodiment/task와 simulation/real-robot 여부
- Observation, action representation, action horizon과 control rate
- Data source, demonstration quality와 train/test generalization split
- Success뿐 아니라 latency, intervention, failure severity와 reproducibility cost

## Reproducible Minimum

Reach, open-drawer, insert 계열 3개 task에 고정 demo 수와 variation split을 정해 2D와 3D policy를 비교한다.

## Manual Review Needed

- Exact trial count, uncertainty interval, baseline configuration와 ablation은 full text에서 확인한다.
