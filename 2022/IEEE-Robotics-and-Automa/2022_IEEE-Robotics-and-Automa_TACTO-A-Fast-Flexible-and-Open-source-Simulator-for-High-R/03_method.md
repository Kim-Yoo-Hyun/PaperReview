# Method — TACTO: A Fast, Flexible, and Open-source Simulator for High-Resolution Vision-based Tactile Sensors

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / IEEE Robotics and Automation Letters
- Category: Benchmarks and Datasets
- Tags: Robotics, tactile sensing, simulation, contact
- Official paper: https://doi.org/10.1109/LRA.2022.3146945
- Code/Project: https://github.com/facebookresearch/tacto
- Source audit: publisher metadata, abstract, and official code repository checked; fidelity results remain UNVERIFIED.

## Pipeline

physics simulator contact와 graphics rendering을 결합해 여러 vision-based tactile sensor output을 생성한다.

## Interface

simulated contact state를 tactile RGB/image observation으로 변환한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
