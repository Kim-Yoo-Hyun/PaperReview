# Masked Visual Pre-training for Motor Control

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2022 / arXiv
- Category: Robot Learning and Data
- Tags: Robotics, representation learning, Visual Pretraining, Imitation Learning
- Official paper: https://arxiv.org/abs/2203.06173
- Code/Project: https://mvp-playground.github.io/
- Source audit: arXiv abstract and project page checked; full experimental tables remain UNVERIFIED.

## Why This Paper Is Here

masked image pretraining을 embodied motor control로 transfer한 MVP 계열 foundation으로 robot representation baseline을 보강한다.

## Problem

작은 robot demonstration set에서 visual encoder를 처음부터 학습할 때의 data inefficiency를 줄인다.

## Core Idea

대규모 image data에서 masked autoencoding으로 pretrained ViT representation을 얻고 motor-control policy에 fine-tune한다.

## Interface

RGB observation을 policy용 visual embedding으로 변환하고 downstream action learner와 결합한다.

## Evaluation Scope

simulation 및 real-robot manipulation에서 scratch와 다른 pretrained representations를 비교한다.
