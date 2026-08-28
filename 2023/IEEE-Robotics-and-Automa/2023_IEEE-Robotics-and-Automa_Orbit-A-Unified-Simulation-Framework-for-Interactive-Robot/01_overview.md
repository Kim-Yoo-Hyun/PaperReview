# Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2023 / IEEE Robotics and Automation Letters
- Category: Benchmarks and Datasets
- Tags: Robotics, simulation, Robot Learning, Benchmark, NVIDIA
- Official paper: https://doi.org/10.1109/LRA.2023.3270034
- Code/Project: https://isaac-orbit.github.io/
- Source audit: publisher metadata, abstract, and official project page checked; benchmark details remain UNVERIFIED.

## Why This Paper Is Here

Isaac Sim 위에서 locomotion·manipulation 학습 환경을 modular하게 구성한 framework로 Isaac Lab의 직접 전신이다.

## Problem

서로 다른 robot tasks와 learning workflow를 scalable simulator 위에서 재사용·구성하기 어렵다는 문제를 다룬다.

## Core Idea

scene, robot, sensor, task, reward와 environment vectorization을 modular configuration framework로 통합한다.

## Interface

Isaac Sim assets/sensors와 batched RL/IL environments를 연결한다.

## Evaluation Scope

locomotion, manipulation 및 sim-to-real examples를 통해 framework 범위를 보인다.
