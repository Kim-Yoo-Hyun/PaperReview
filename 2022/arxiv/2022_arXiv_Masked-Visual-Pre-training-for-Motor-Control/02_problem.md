# Problem — Masked Visual Pre-training for Motor Control

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / arXiv
- Category: Robot Learning and Data
- Tags: Robotics, representation learning, Visual Pretraining, Imitation Learning
- Official paper: https://arxiv.org/abs/2203.06173
- Code/Project: https://mvp-playground.github.io/
- Source audit: arXiv abstract and project page checked; full experimental tables remain UNVERIFIED.

## Target Problem and Assumptions

작은 robot demonstration set에서 visual encoder를 처음부터 학습할 때의 data inefficiency를 줄인다.

## Closed-Loop Position

RGB observation을 policy용 visual embedding으로 변환하고 downstream action learner와 결합한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
