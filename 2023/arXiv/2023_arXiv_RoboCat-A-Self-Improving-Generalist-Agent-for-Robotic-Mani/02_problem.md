# Problem

- Year/Venue: 2023 / arXiv
- Category: Robot Learning and Data
- Tags: Robotics, generalist policy, cross-embodiment, self-improvement, robot manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://deepmind.google/discover/blog/robocat-a-self-improving-robotic-agent/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- This is because, even though the cost of task design and robot experience generation is very high, leveraging heterogeneous robot data at scale has remained a challenging problem ...

## 해결하려는 문제
- We also show how a trained model itself can be used to generate data for subsequent training iterations, thus providing a basic building block for an autonomous improvement ...
- We find that as we grow and diversify its training data, RoboCat not only shows signs of cross-task transfer, but also becomes more efficient at adapting to new ...
- Inspired by recent advances in foundation models for vision and language, we propose a multi-embodiment, multi-task generalist agent for robotic manipulation.

## 선행 연구 / 배경 단서
- This is because, even though the cost of task design and robot experience generation is very high, leveraging heterogeneous robot data at scale has remained a challenging problem ...
- The advent of high-capacity models, such as the transformer model (Vaswani et al., 2017), has enabled recent successes for multi-task learning in language and vision.
