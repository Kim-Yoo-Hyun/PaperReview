# Problem — DrEureka: Language Model Guided Sim-To-Real Transfer

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2024 / Robotics: Science and Systems
- Category: Robot Learning and Data
- Tags: Robotics, sim-to-real, Reinforcement Learning, Large Language Model, NVIDIA
- Official paper: https://www.roboticsproceedings.org/rss20/p094.html
- Code/Project: https://eureka-research.github.io/dr-eureka/
- Source audit: official RSS proceedings abstract and project page checked; hardware trial details remain UNVERIFIED.

## Target Problem and Assumptions

simulation에서 학습한 policy를 실제 robot에 옮길 때 reward와 dynamics randomization을 수작업으로 조정하는 병목을 다룬다.

## Closed-Loop Position

task/environment description와 simulation diagnostics를 reward/randomization code 및 deployable policy training으로 연결한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
