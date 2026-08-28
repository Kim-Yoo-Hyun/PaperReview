# Method — Hybrid Position/Force Control of Manipulators

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1981 / Journal of Dynamic Systems, Measurement, and Control
- Category: Robotics Foundations: Contact and Whole-Body Control
- Tags: Robotics, force control, contact, manipulation
- Official paper: https://doi.org/10.1115/1.3139652
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; controller derivation details remain UNVERIFIED.

## Pipeline

task space를 position-controlled subspace와 force-controlled subspace로 분해해 hybrid feedback law를 구성한다.

## Interface

end-effector pose/velocity와 contact force를 받아 joint actuation 명령으로 연결한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
