# Evaluation — MuJoCo: A Physics Engine for Model-Based Control

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2012 / IROS
- Category: Benchmarks and Datasets
- Tags: Robotics, simulation, Physics Engine, Control
- Official paper: https://doi.org/10.1109/IROS.2012.6386109
- Code/Project: https://mujoco.org/
- Source audit: publisher metadata, official project page, and abstract checked; solver details remain UNVERIFIED.

## Protocol

simulation speed·accuracy와 control application이 중심이며 최신 GPU simulator와의 비교는 후속 연구에서 확인한다.

## Limitations and Reproducibility

simulator fidelity, contact parameterization과 sim-to-real gap은 별도 검증이 필요하다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
