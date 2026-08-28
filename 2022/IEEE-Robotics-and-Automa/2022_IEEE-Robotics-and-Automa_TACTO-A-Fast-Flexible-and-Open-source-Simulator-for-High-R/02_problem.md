# Problem — TACTO: A Fast, Flexible, and Open-source Simulator for High-Resolution Vision-based Tactile Sensors

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / IEEE Robotics and Automation Letters
- Category: Benchmarks and Datasets
- Tags: Robotics, tactile sensing, simulation, contact
- Official paper: https://doi.org/10.1109/LRA.2022.3146945
- Code/Project: https://github.com/facebookresearch/tacto
- Source audit: publisher metadata, abstract, and official code repository checked; fidelity results remain UNVERIFIED.

## Target Problem and Assumptions

고해상도 tactile rendering의 계산 비용과 sensor configuration 재사용 문제를 다룬다.

## Closed-Loop Position

simulated contact state를 tactile RGB/image observation으로 변환한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
