# Problem — Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2019 / CoRL
- Category: Benchmarks and Datasets
- Tags: Robotics, Benchmark, Reinforcement Learning, manipulation
- Official paper: https://proceedings.mlr.press/v100/yu20a.html
- Code/Project: https://meta-world.github.io/
- Source audit: official proceedings abstract and project page checked; task/protocol details remain UNVERIFIED.

## Target Problem and Assumptions

algorithm별 서로 다른 environment 때문에 multi-task/meta-RL generalization을 공정하게 비교하기 어렵다는 문제를 다룬다.

## Closed-Loop Position

MuJoCo state/observation과 continuous actions, task goals와 success predicates를 정의한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
