# Evaluation — Masked Visual Pre-training for Motor Control

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / arXiv
- Category: Robot Learning and Data
- Tags: Robotics, representation learning, Visual Pretraining, Imitation Learning
- Official paper: https://arxiv.org/abs/2203.06173
- Code/Project: https://mvp-playground.github.io/
- Source audit: arXiv abstract and project page checked; full experimental tables remain UNVERIFIED.

## Protocol

simulation 및 real-robot manipulation에서 scratch와 다른 pretrained representations를 비교한다.

## Limitations and Reproducibility

static-image pretraining과 action relevance의 간극, tactile/state feedback 부재를 확인해야 한다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
