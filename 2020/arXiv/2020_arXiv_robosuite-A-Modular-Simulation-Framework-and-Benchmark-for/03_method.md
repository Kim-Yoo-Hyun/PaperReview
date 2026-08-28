# Method — robosuite: A Modular Simulation Framework and Benchmark for Robot Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2020 / arXiv
- Category: Benchmarks and Datasets
- Tags: Robotics, Benchmark, simulation, manipulation
- Official paper: https://arxiv.org/abs/2009.12293
- Code/Project: https://robosuite.ai/
- Source audit: arXiv abstract and official documentation checked; benchmark result details remain UNVERIFIED.

## Pipeline

MuJoCo 위에 modular robot models, grippers, controllers, manipulation tasks와 interfaces를 제공한다.

## Interface

state/RGB observations와 multiple control modes를 simulated robot actions 및 task success로 연결한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
