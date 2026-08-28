# Problem — RoboNet: Large-Scale Multi-Robot Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2019 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Dataset, multi-robot, manipulation
- Official paper: https://proceedings.mlr.press/v100/dasari20a.html
- Code/Project: https://www.robonet.wiki/
- Source audit: official proceedings abstract and project page checked; dataset statistics and experiment details remain UNVERIFIED.

## Target Problem and Assumptions

한 로봇/환경에서 수집한 data가 다른 embodiment와 viewpoint로 잘 transfer되지 않는 문제를 다룬다.

## Closed-Loop Position

camera observations, robot actions와 embodiment context를 future prediction 및 planning-based control로 연결한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
