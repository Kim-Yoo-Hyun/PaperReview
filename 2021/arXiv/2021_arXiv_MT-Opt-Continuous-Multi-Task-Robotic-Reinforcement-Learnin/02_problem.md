# Problem — MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2021 / arXiv
- Category: Robot Learning and Data
- Tags: Robotics, Reinforcement Learning, Multi-Task Learning, robot data, Google DeepMind
- Official paper: https://arxiv.org/abs/2104.08212
- Code/Project: not identified
- Source audit: arXiv abstract and official Google research material checked; full tables remain UNVERIFIED.

## Target Problem and Assumptions

다수 manipulation tasks의 불균형한 real-robot data에서 knowledge transfer와 scalable policy improvement를 수행한다.

## Closed-Loop Position

vision, task identity와 robot state를 continuous manipulation action/value prediction으로 매핑한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
