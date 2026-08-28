# Problem — Dense Object Nets: Learning Dense Visual Object Descriptors By and For Robotic Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2018 / CoRL
- Category: Robotics-Enabling 3D Perception
- Tags: Robotics, manipulation, Dense Descriptors, representation learning
- Official paper: https://proceedings.mlr.press/v87/florence18a.html
- Code/Project: https://dense-object-nets.github.io/
- Source audit: official proceedings abstract and project page checked; training/evaluation details remain UNVERIFIED.

## Target Problem and Assumptions

texture·view 변화에도 물체 표면의 task-relevant point correspondence를 얻는다.

## Closed-Loop Position

camera observation을 object surface descriptor/correspondence로 변환해 grasping·manipulation target을 제공한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
