# Method — Dense Object Nets: Learning Dense Visual Object Descriptors By and For Robotic Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2018 / CoRL
- Category: Robotics-Enabling 3D Perception
- Tags: Robotics, manipulation, Dense Descriptors, representation learning
- Official paper: https://proceedings.mlr.press/v87/florence18a.html
- Code/Project: https://dense-object-nets.github.io/
- Source audit: official proceedings abstract and project page checked; training/evaluation details remain UNVERIFIED.

## Pipeline

self-supervised multi-view RGB-D data로 pixel-level dense descriptors를 학습하고 correspondence 기반 manipulation을 수행한다.

## Interface

camera observation을 object surface descriptor/correspondence로 변환해 grasping·manipulation target을 제공한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
