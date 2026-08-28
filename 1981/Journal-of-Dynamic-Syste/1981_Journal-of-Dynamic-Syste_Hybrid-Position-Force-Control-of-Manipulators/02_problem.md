# Problem — Hybrid Position/Force Control of Manipulators

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1981 / Journal of Dynamic Systems, Measurement, and Control
- Category: Robotics Foundations: Contact and Whole-Body Control
- Tags: Robotics, force control, contact, manipulation
- Official paper: https://doi.org/10.1115/1.3139652
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; controller derivation details remain UNVERIFIED.

## Target Problem and Assumptions

환경 constraint가 있는 manipulation에서 모든 방향을 position control하는 방식의 한계를 해결한다.

## Closed-Loop Position

end-effector pose/velocity와 contact force를 받아 joint actuation 명령으로 연결한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
