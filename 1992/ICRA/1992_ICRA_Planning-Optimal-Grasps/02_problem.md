# Problem — Planning Optimal Grasps

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1992 / ICRA
- Category: Robotics Foundations: Contact and Whole-Body Control
- Tags: Robotics, Grasp Planning, manipulation, contact
- Official paper: https://doi.org/10.1109/ROBOT.1992.219918
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; optimization formulation details remain UNVERIFIED.

## Target Problem and Assumptions

물체를 안정적으로 제어할 수 있는 contact configuration과 finger placement를 선택하는 문제를 다룬다.

## Closed-Loop Position

object geometry와 friction/contact model을 grasp/contact plan으로 변환한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
