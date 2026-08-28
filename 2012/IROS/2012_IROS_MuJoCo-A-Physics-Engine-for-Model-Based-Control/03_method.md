# Method — MuJoCo: A Physics Engine for Model-Based Control

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2012 / IROS
- Category: Benchmarks and Datasets
- Tags: Robotics, simulation, Physics Engine, Control
- Official paper: https://doi.org/10.1109/IROS.2012.6386109
- Code/Project: https://mujoco.org/
- Source audit: publisher metadata, official project page, and abstract checked; solver details remain UNVERIFIED.

## Pipeline

generalized-coordinate dynamics와 contact/constraint 처리를 결합한 physics engine을 설계한다.

## Interface

robot model과 control input을 simulated state transition, contact와 sensor output으로 변환한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
