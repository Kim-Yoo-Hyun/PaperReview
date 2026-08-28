# Method — Impedance Control: An Approach to Manipulation: Part I—Theory

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1985 / Journal of Dynamic Systems, Measurement, and Control
- Category: Robotics Foundations: Contact and Whole-Body Control
- Tags: Robotics, Impedance Control, contact, manipulation
- Official paper: https://doi.org/10.1115/1.3140702
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; stability derivations remain UNVERIFIED.

## Pipeline

motion과 interaction force 사이의 목표 동적 관계를 inertia-damping-stiffness 형태로 설계한다.

## Interface

pose/velocity와 external wrench feedback을 actuation으로 매핑하는 low-level interaction-control 계층이다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
