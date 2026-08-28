# Problem — Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2023 / IEEE Robotics and Automation Letters
- Category: Benchmarks and Datasets
- Tags: Robotics, simulation, Robot Learning, Benchmark, NVIDIA
- Official paper: https://doi.org/10.1109/LRA.2023.3270034
- Code/Project: https://isaac-orbit.github.io/
- Source audit: publisher metadata, abstract, and official project page checked; benchmark details remain UNVERIFIED.

## Target Problem and Assumptions

서로 다른 robot tasks와 learning workflow를 scalable simulator 위에서 재사용·구성하기 어렵다는 문제를 다룬다.

## Closed-Loop Position

Isaac Sim assets/sensors와 batched RL/IL environments를 연결한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
