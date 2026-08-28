# Problem — Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2021 / NeurIPS Datasets and Benchmarks
- Category: Benchmarks and Datasets
- Tags: Robotics, simulation, GPU, Reinforcement Learning, NVIDIA
- Official paper: https://research.nvidia.com/labs/srl/publication/makoviychuk-2021-isaac/
- Code/Project: not identified
- Source audit: official NVIDIA research page and abstract checked; throughput details remain UNVERIFIED.

## Target Problem and Assumptions

CPU simulation과 GPU learning 사이의 data transfer 및 제한된 environment parallelism이 RL training을 느리게 하는 문제를 다룬다.

## Closed-Loop Position

대량의 parallel robot states/actions를 batched simulator transitions와 policy updates로 연결한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
