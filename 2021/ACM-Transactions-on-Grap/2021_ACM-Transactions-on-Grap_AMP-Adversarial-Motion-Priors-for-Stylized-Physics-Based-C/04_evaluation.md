# Evaluation — AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2021 / ACM Transactions on Graphics
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, Reinforcement Learning, motion imitation, whole-body control
- Official paper: https://doi.org/10.1145/3450626.3459670
- Code/Project: https://xbpeng.github.io/projects/AMP/
- Source audit: publisher abstract and official project page checked; reward/training details remain UNVERIFIED.

## Protocol

다수의 simulated character skills와 interactive tasks를 평가하며 robot transfer 범위는 별도 확인이 필요하다.

## Limitations and Reproducibility

simulation motion quality와 physical robot robustness 사이의 gap, mocap coverage 의존성이 남는다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
