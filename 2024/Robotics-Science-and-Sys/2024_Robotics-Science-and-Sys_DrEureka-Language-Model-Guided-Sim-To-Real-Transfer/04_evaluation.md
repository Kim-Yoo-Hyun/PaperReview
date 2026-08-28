# Evaluation — DrEureka: Language Model Guided Sim-To-Real Transfer

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2024 / Robotics: Science and Systems
- Category: Robot Learning and Data
- Tags: Robotics, sim-to-real, Reinforcement Learning, Large Language Model, NVIDIA
- Official paper: https://www.roboticsproceedings.org/rss20/p094.html
- Code/Project: https://eureka-research.github.io/dr-eureka/
- Source audit: official RSS proceedings abstract and project page checked; hardware trial details remain UNVERIFIED.

## Protocol

quadruped locomotion 및 dexterous manipulation의 sim-to-real demonstrations가 보고된다.

## Limitations and Reproducibility

LLM-selected ranges의 safety, hardware damage risk와 task-specific manual context 의존성을 확인해야 한다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
