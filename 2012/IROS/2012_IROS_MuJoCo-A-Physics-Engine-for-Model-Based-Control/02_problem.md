# Problem — MuJoCo: A Physics Engine for Model-Based Control

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2012 / IROS
- Category: Benchmarks and Datasets
- Tags: Robotics, simulation, Physics Engine, Control
- Official paper: https://doi.org/10.1109/IROS.2012.6386109
- Code/Project: https://mujoco.org/
- Source audit: publisher metadata, official project page, and abstract checked; solver details remain UNVERIFIED.

## Target Problem and Assumptions

model-based control과 optimization에 필요한 빠르고 정확한 articulated rigid-body/contact simulation을 제공한다.

## Closed-Loop Position

robot model과 control input을 simulated state transition, contact와 sensor output으로 변환한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
