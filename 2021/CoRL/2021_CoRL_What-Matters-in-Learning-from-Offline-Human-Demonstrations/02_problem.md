# Problem — What Matters in Learning from Offline Human Demonstrations for Robot Manipulation

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2021 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, offline learning, robot dataset, Benchmark, robomimic
- Official paper: https://proceedings.mlr.press/v164/mandlekar22a.html
- Official PDF: https://proceedings.mlr.press/v164/mandlekar22a/mandlekar22a.pdf
- Code/Project: https://robomimic.github.io/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Target Problem

Offline human demonstration에서 algorithm, history, data quality와 checkpoint selection 중 무엇이 실제 manipulation 성능을 좌우하는지 재현 가능하게 비교해야 한다.

## Core Assumptions

- Offline dataset이 deployment state와 task를 충분히 덮는다.
- Simulation과 제한된 real-robot task에서 얻은 설계 결론이 다른 embodiment에도 유효하다.

## Closed-Loop Position

이 논문은 현재 robotics loop에서 `Behavior cloning / offline RL → RoboMimic → MimicGen / DROID / generalist robot data` 연결을 담당한다. 실제 정독 시 observation/state/action/control 중 어느 interface를 고정하고 어느 부분을 학습하는지 확인한다.

## Falsification Question

현대 VLA scale과 cross-embodiment data를 직접 다루지는 않는다.
