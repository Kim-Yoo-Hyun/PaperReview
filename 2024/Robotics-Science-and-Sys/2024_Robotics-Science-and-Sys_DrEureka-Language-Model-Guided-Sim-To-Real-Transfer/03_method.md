# Method — DrEureka: Language Model Guided Sim-To-Real Transfer

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2024 / Robotics: Science and Systems
- Category: Robot Learning and Data
- Tags: Robotics, sim-to-real, Reinforcement Learning, Large Language Model, NVIDIA
- Official paper: https://www.roboticsproceedings.org/rss20/p094.html
- Code/Project: https://eureka-research.github.io/dr-eureka/
- Source audit: official RSS proceedings abstract and project page checked; hardware trial details remain UNVERIFIED.

## Pipeline

LLM이 reward와 physics randomization 범위를 제안하고 simulator feedback을 이용해 transfer configuration을 구성한다.

## Interface

task/environment description와 simulation diagnostics를 reward/randomization code 및 deployable policy training으로 연결한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
