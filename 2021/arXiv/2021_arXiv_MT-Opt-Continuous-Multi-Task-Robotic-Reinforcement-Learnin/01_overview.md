# MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2021 / arXiv
- Category: Robot Learning and Data
- Tags: Robotics, Reinforcement Learning, Multi-Task Learning, robot data, Google DeepMind
- Official paper: https://arxiv.org/abs/2104.08212
- Code/Project: not identified
- Source audit: arXiv abstract and official Google research material checked; full tables remain UNVERIFIED.

## Why This Paper Is Here

Google의 large-scale real-robot multi-task RL lineage를 보여 주며 QT-Opt에서 generalist robot learning으로 이어지는 핵심 bridge다.

## Problem

다수 manipulation tasks의 불균형한 real-robot data에서 knowledge transfer와 scalable policy improvement를 수행한다.

## Core Idea

multi-task off-policy RL, task conditioning과 data-sharing/relabeling을 large distributed robot fleet에 적용한다.

## Interface

vision, task identity와 robot state를 continuous manipulation action/value prediction으로 매핑한다.

## Evaluation Scope

large real-robot manipulation dataset과 multi-task success를 평가하며 정확한 task/trial 수는 정독 후 기록한다.
