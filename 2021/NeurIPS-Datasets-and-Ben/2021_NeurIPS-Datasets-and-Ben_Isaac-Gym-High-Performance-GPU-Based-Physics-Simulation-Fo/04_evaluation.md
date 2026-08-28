# Evaluation — Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2021 / NeurIPS Datasets and Benchmarks
- Category: Benchmarks and Datasets
- Tags: Robotics, simulation, GPU, Reinforcement Learning, NVIDIA
- Official paper: https://research.nvidia.com/labs/srl/publication/makoviychuk-2021-isaac/
- Code/Project: not identified
- Source audit: official NVIDIA research page and abstract checked; throughput details remain UNVERIFIED.

## Protocol

locomotion/manipulation RL의 simulation throughput과 training time을 비교한다.

## Limitations and Reproducibility

sim-to-real fidelity, GPU memory와 simulator-specific contact modeling의 영향을 별도 검증해야 한다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
