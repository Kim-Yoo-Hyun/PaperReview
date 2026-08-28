# Method — RoboNet: Large-Scale Multi-Robot Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2019 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Dataset, multi-robot, manipulation
- Official paper: https://proceedings.mlr.press/v100/dasari20a.html
- Code/Project: https://www.robonet.wiki/
- Source audit: official proceedings abstract and project page checked; dataset statistics and experiment details remain UNVERIFIED.

## Pipeline

heterogeneous multi-robot interaction dataset과 conditioned video prediction/control 모델을 구축한다.

## Interface

camera observations, robot actions와 embodiment context를 future prediction 및 planning-based control로 연결한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
