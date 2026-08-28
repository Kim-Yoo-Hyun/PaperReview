# Method — Eureka: Human-Level Reward Design via Coding Large Language Models

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2024 / ICLR
- Category: Robot Learning and Data
- Tags: Robotics, Reinforcement Learning, Reward Design, Large Language Model, NVIDIA
- Official paper: https://openreview.net/forum?id=IEduRUO55F
- Code/Project: https://eureka-research.github.io/
- Source audit: official OpenReview abstract and project page checked; task-level results remain UNVERIFIED.

## Pipeline

LLM code generation, simulator feedback와 evolutionary refinement를 반복해 reward functions를 탐색한다.

## Interface

task description와 environment source/context를 executable reward code로 바꾸고 RL training 결과를 feedback한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
