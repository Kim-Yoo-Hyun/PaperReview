# Method — What Matters in Learning from Offline Human Demonstrations for Robot Manipulation

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2021 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, offline learning, robot dataset, Benchmark, robomimic
- Official paper: https://proceedings.mlr.press/v164/mandlekar22a.html
- Official PDF: https://proceedings.mlr.press/v164/mandlekar22a/mandlekar22a.pdf
- Code/Project: https://robomimic.github.io/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Pipeline

- 여러 imitation learning과 batch offline RL 방법을 공통 codebase에서 비교한다.
- Proficient-human, multi-human과 machine-generated data 등 demonstration quality를 분리한다.
- History-dependent policy와 policy selection 문제를 체계적으로 분석한다.

## Interface

RGB/state observation history에서 continuous robot action을 예측하는 offline policy learning benchmark다.

## Implementation Audit

- Objective, horizon, control rate와 architecture detail은 full text 정독 후 확정한다.
- Official abstract가 지지하지 않는 loss, data size 또는 hardware detail은 추정하지 않는다.
- 후속 구현에서는 `Behavior cloning / offline RL → RoboMimic → MimicGen / DROID / generalist robot data`의 앞뒤 논문과 공통 interface를 먼저 맞춘다.
