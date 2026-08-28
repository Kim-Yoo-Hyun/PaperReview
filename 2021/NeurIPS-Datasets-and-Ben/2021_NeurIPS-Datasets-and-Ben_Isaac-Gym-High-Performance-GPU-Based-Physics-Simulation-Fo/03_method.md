# Method — Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2021 / NeurIPS Datasets and Benchmarks
- Category: Benchmarks and Datasets
- Tags: Robotics, simulation, GPU, Reinforcement Learning, NVIDIA
- Official paper: https://research.nvidia.com/labs/srl/publication/makoviychuk-2021-isaac/
- Code/Project: not identified
- Source audit: official NVIDIA research page and abstract checked; throughput details remain UNVERIFIED.

## Pipeline

GPU physics simulation, observation/reward computation과 policy learning을 end-to-end device-resident pipeline으로 구성한다.

## Interface

대량의 parallel robot states/actions를 batched simulator transitions와 policy updates로 연결한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
