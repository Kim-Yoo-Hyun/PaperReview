# Method — Masked Visual Pre-training for Motor Control

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / arXiv
- Category: Robot Learning and Data
- Tags: Robotics, representation learning, Visual Pretraining, Imitation Learning
- Official paper: https://arxiv.org/abs/2203.06173
- Code/Project: https://mvp-playground.github.io/
- Source audit: arXiv abstract and project page checked; full experimental tables remain UNVERIFIED.

## Pipeline

대규모 image data에서 masked autoencoding으로 pretrained ViT representation을 얻고 motor-control policy에 fine-tune한다.

## Interface

RGB observation을 policy용 visual embedding으로 변환하고 downstream action learner와 결합한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
