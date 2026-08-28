# Problem — Eureka: Human-Level Reward Design via Coding Large Language Models

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2024 / ICLR
- Category: Robot Learning and Data
- Tags: Robotics, Reinforcement Learning, Reward Design, Large Language Model, NVIDIA
- Official paper: https://openreview.net/forum?id=IEduRUO55F
- Code/Project: https://eureka-research.github.io/
- Source audit: official OpenReview abstract and project page checked; task-level results remain UNVERIFIED.

## Target Problem and Assumptions

복잡한 robot skill의 dense reward를 사람이 반복 설계하는 비용과 전문성 병목을 줄인다.

## Closed-Loop Position

task description와 environment source/context를 executable reward code로 바꾸고 RL training 결과를 feedback한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
