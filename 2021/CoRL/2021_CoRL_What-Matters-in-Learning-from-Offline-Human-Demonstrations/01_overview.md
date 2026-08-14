# What Matters in Learning from Offline Human Demonstrations for Robot Manipulation

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2021 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, offline learning, robot dataset, Benchmark, robomimic
- Official paper: https://proceedings.mlr.press/v164/mandlekar22a.html
- Official PDF: https://proceedings.mlr.press/v164/mandlekar22a/mandlekar22a.pdf
- Code/Project: https://robomimic.github.io/
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Why This Paper Is Here

MimicGen·DROID 이전의 mixed-quality offline demonstration과 reproducible IL 기준점.

## Problem

Offline human demonstration에서 algorithm, history, data quality와 checkpoint selection 중 무엇이 실제 manipulation 성능을 좌우하는지 재현 가능하게 비교해야 한다.

## Core Idea

- 여러 imitation learning과 batch offline RL 방법을 공통 codebase에서 비교한다.
- Proficient-human, multi-human과 machine-generated data 등 demonstration quality를 분리한다.
- History-dependent policy와 policy selection 문제를 체계적으로 분석한다.

## Observation / State / Action Interface

RGB/state observation history에서 continuous robot action을 예측하는 offline policy learning benchmark다.

## Evaluation Scope

- 공식 PMLR 기록은 5개 simulated, 3개 real-world multi-stage manipulation task와 서로 다른 quality의 dataset을 보고한다.
- Algorithm뿐 아니라 demonstration quality와 stopping criterion에 민감하다는 점을 평가한다.

## Limitations to Verify

- 현대 VLA scale과 cross-embodiment data를 직접 다루지는 않는다.
- Success-only benchmark는 failure onset과 recovery quality를 충분히 나타내지 않는다.

## Reading Lineage

`Behavior cloning / offline RL → RoboMimic → MimicGen / DROID / generalist robot data`
