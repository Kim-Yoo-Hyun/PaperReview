# Method — Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2023 / IEEE Robotics and Automation Letters
- Category: Benchmarks and Datasets
- Tags: Robotics, simulation, Robot Learning, Benchmark, NVIDIA
- Official paper: https://doi.org/10.1109/LRA.2023.3270034
- Code/Project: https://isaac-orbit.github.io/
- Source audit: publisher metadata, abstract, and official project page checked; benchmark details remain UNVERIFIED.

## Pipeline

scene, robot, sensor, task, reward와 environment vectorization을 modular configuration framework로 통합한다.

## Interface

Isaac Sim assets/sensors와 batched RL/IL environments를 연결한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
