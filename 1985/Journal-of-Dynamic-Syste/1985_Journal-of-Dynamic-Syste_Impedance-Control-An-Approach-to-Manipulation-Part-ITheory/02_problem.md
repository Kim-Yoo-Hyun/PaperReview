# Problem — Impedance Control: An Approach to Manipulation: Part I—Theory

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1985 / Journal of Dynamic Systems, Measurement, and Control
- Category: Robotics Foundations: Contact and Whole-Body Control
- Tags: Robotics, Impedance Control, contact, manipulation
- Official paper: https://doi.org/10.1115/1.3140702
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; stability derivations remain UNVERIFIED.

## Target Problem and Assumptions

uncertain environment와 접촉할 때 motion 또는 force 하나만 직접 추종해서는 robust interaction을 만들기 어렵다는 문제를 다룬다.

## Closed-Loop Position

pose/velocity와 external wrench feedback을 actuation으로 매핑하는 low-level interaction-control 계층이다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
