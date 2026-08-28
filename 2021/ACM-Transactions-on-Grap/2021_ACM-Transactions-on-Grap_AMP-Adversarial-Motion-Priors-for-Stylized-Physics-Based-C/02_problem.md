# Problem — AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2021 / ACM Transactions on Graphics
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, Reinforcement Learning, motion imitation, whole-body control
- Official paper: https://doi.org/10.1145/3450626.3459670
- Code/Project: https://xbpeng.github.io/projects/AMP/
- Source audit: publisher abstract and official project page checked; reward/training details remain UNVERIFIED.

## Target Problem and Assumptions

physics-based character가 task를 수행하면서 reference motion의 자연스러운 style을 폭넓게 재현하도록 학습한다.

## Closed-Loop Position

proprioceptive state와 task goal을 joint actions로 매핑하고 motion prior가 policy behavior를 regularize한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
