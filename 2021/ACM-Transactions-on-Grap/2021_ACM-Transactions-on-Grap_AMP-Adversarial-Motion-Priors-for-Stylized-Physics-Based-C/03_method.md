# Method — AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2021 / ACM Transactions on Graphics
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, Reinforcement Learning, motion imitation, whole-body control
- Official paper: https://doi.org/10.1145/3450626.3459670
- Code/Project: https://xbpeng.github.io/projects/AMP/
- Source audit: publisher abstract and official project page checked; reward/training details remain UNVERIFIED.

## Pipeline

motion discriminator가 제공하는 adversarial imitation reward를 task reward와 함께 RL policy에 사용한다.

## Interface

proprioceptive state와 task goal을 joint actions로 매핑하고 motion prior가 policy behavior를 regularize한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
