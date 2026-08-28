# Method — MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2021 / arXiv
- Category: Robot Learning and Data
- Tags: Robotics, Reinforcement Learning, Multi-Task Learning, robot data, Google DeepMind
- Official paper: https://arxiv.org/abs/2104.08212
- Code/Project: not identified
- Source audit: arXiv abstract and official Google research material checked; full tables remain UNVERIFIED.

## Pipeline

multi-task off-policy RL, task conditioning과 data-sharing/relabeling을 large distributed robot fleet에 적용한다.

## Interface

vision, task identity와 robot state를 continuous manipulation action/value prediction으로 매핑한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
