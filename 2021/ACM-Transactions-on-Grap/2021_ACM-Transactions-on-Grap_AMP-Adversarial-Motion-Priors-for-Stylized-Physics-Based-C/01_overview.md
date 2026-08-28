# AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2021 / ACM Transactions on Graphics
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, Reinforcement Learning, motion imitation, whole-body control
- Official paper: https://doi.org/10.1145/3450626.3459670
- Code/Project: https://xbpeng.github.io/projects/AMP/
- Source audit: publisher abstract and official project page checked; reward/training details remain UNVERIFIED.

## Why This Paper Is Here

motion dataset를 adversarial style prior로 사용해 task reward와 자연스러운 whole-body motion을 결합한 humanoid/control 대표 foundation이다.

## Problem

physics-based character가 task를 수행하면서 reference motion의 자연스러운 style을 폭넓게 재현하도록 학습한다.

## Core Idea

motion discriminator가 제공하는 adversarial imitation reward를 task reward와 함께 RL policy에 사용한다.

## Interface

proprioceptive state와 task goal을 joint actions로 매핑하고 motion prior가 policy behavior를 regularize한다.

## Evaluation Scope

다수의 simulated character skills와 interactive tasks를 평가하며 robot transfer 범위는 별도 확인이 필요하다.
