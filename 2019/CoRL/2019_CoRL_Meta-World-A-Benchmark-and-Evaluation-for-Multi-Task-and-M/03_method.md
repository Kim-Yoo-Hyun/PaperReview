# Method — Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2019 / CoRL
- Category: Benchmarks and Datasets
- Tags: Robotics, Benchmark, Reinforcement Learning, manipulation
- Official paper: https://proceedings.mlr.press/v100/yu20a.html
- Code/Project: https://meta-world.github.io/
- Source audit: official proceedings abstract and project page checked; task/protocol details remain UNVERIFIED.

## Pipeline

공통 robot/workspace에서 다수의 manipulation task와 train/test split evaluation protocol을 제공한다.

## Interface

MuJoCo state/observation과 continuous actions, task goals와 success predicates를 정의한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
