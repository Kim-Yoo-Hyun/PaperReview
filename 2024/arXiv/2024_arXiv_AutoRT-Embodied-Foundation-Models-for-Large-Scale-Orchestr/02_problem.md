# Problem — AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2024 / arXiv
- Category: Robot Learning and Data
- Tags: Robotics, robot data, Foundation Models, Fleet Learning, Google DeepMind
- Official paper: https://deepmind.google/research/publications/48151/
- Code/Project: not identified
- Source audit: official DeepMind publication page and abstract checked; deployment statistics remain UNVERIFIED.

## Target Problem and Assumptions

다양한 실제 환경에서 여러 로봇이 유용하고 안전한 embodied data를 자율적으로 대규모 수집하게 한다.

## Closed-Loop Position

scene observations를 candidate language tasks, safety decision과 robot-policy invocation으로 연결한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
