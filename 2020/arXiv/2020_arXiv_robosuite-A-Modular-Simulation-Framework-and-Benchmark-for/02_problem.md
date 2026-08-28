# Problem — robosuite: A Modular Simulation Framework and Benchmark for Robot Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2020 / arXiv
- Category: Benchmarks and Datasets
- Tags: Robotics, Benchmark, simulation, manipulation
- Official paper: https://arxiv.org/abs/2009.12293
- Code/Project: https://robosuite.ai/
- Source audit: arXiv abstract and official documentation checked; benchmark result details remain UNVERIFIED.

## Target Problem and Assumptions

robot learning 연구마다 simulation setup과 controller가 달라 algorithm 비교와 재사용이 어려운 문제를 다룬다.

## Closed-Loop Position

state/RGB observations와 multiple control modes를 simulated robot actions 및 task success로 연결한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
