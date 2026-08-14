# Method

- Year/Venue: 2025 / CoRL Poster
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, locomotion, end-effector stabilization, multi-rate control
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://lecar-lab.github.io/SoFTA/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- To address this, we propose SoFTA, a Slow-Fast Two-Agent framework that decouples upper-body and lower-body control into separate agents operating at different frequencies and with distinct rewards.
- During training, reward functions, termination conditions, and curriculum design are consistent and frequency-agnostic across all comparisons.

## 원리적 동기
- While humanoids are increasingly featured in flashy demos—dancing, delivering packages, traversing rough terrain—fine-grained control during locomotion remains a significant challenge.
- To address this, we propose SoFTA, a Slow-Fast Two-Agent framework that decouples upper-body and lower-body control into separate agents operating at different frequencies and with distinct rewards.

## 핵심 방법론
- During training, reward functions, termination conditions, and curriculum design are consistent and frequency-agnostic across all comparisons.
