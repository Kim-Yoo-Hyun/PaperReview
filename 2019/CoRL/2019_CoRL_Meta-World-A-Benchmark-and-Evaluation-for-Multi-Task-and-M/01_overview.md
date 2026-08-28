# Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2019 / CoRL
- Category: Benchmarks and Datasets
- Tags: Robotics, Benchmark, Reinforcement Learning, manipulation
- Official paper: https://proceedings.mlr.press/v100/yu20a.html
- Code/Project: https://meta-world.github.io/
- Source audit: official proceedings abstract and project page checked; task/protocol details remain UNVERIFIED.

## Why This Paper Is Here

multi-task/meta-RL robot manipulation을 공통 task family와 protocol로 평가하는 대표 simulation benchmark다.

## Problem

algorithm별 서로 다른 environment 때문에 multi-task/meta-RL generalization을 공정하게 비교하기 어렵다는 문제를 다룬다.

## Core Idea

공통 robot/workspace에서 다수의 manipulation task와 train/test split evaluation protocol을 제공한다.

## Interface

MuJoCo state/observation과 continuous actions, task goals와 success predicates를 정의한다.

## Evaluation Scope

multi-task 및 meta-learning benchmark protocols와 baseline 결과를 제공한다.
