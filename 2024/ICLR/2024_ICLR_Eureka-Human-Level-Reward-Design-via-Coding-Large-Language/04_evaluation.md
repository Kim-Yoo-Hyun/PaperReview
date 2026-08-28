# Evaluation — Eureka: Human-Level Reward Design via Coding Large Language Models

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2024 / ICLR
- Category: Robot Learning and Data
- Tags: Robotics, Reinforcement Learning, Reward Design, Large Language Model, NVIDIA
- Official paper: https://openreview.net/forum?id=IEduRUO55F
- Code/Project: https://eureka-research.github.io/
- Source audit: official OpenReview abstract and project page checked; task-level results remain UNVERIFIED.

## Protocol

Isaac Gym의 다수 tasks와 dexterous manipulation에서 human-designed rewards와 비교한다.

## Limitations and Reproducibility

simulator reward hacking, code safety, LLM/model dependence와 real-world objective alignment 문제가 남는다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
