# Isaac Gym: High Performance GPU Based Physics Simulation For Robot Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2021 / NeurIPS Datasets and Benchmarks
- Category: Benchmarks and Datasets
- Tags: Robotics, simulation, GPU, Reinforcement Learning, NVIDIA
- Official paper: https://research.nvidia.com/labs/srl/publication/makoviychuk-2021-isaac/
- Code/Project: not identified
- Source audit: official NVIDIA research page and abstract checked; throughput details remain UNVERIFIED.

## Why This Paper Is Here

simulation과 RL tensor computation을 GPU에 통합해 massive-parallel robot learning을 가능하게 한 NVIDIA 계보의 핵심 infrastructure paper다.

## Problem

CPU simulation과 GPU learning 사이의 data transfer 및 제한된 environment parallelism이 RL training을 느리게 하는 문제를 다룬다.

## Core Idea

GPU physics simulation, observation/reward computation과 policy learning을 end-to-end device-resident pipeline으로 구성한다.

## Interface

대량의 parallel robot states/actions를 batched simulator transitions와 policy updates로 연결한다.

## Evaluation Scope

locomotion/manipulation RL의 simulation throughput과 training time을 비교한다.
