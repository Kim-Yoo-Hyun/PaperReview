# Method — AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2024 / arXiv
- Category: Robot Learning and Data
- Tags: Robotics, robot data, Foundation Models, Fleet Learning, Google DeepMind
- Official paper: https://deepmind.google/research/publications/48151/
- Code/Project: not identified
- Source audit: official DeepMind publication page and abstract checked; deployment statistics remain UNVERIFIED.

## Pipeline

VLM/LLM 기반 scene understanding과 task generation을 robot policy 및 safety checks와 결합한다.

## Interface

scene observations를 candidate language tasks, safety decision과 robot-policy invocation으로 연결한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
