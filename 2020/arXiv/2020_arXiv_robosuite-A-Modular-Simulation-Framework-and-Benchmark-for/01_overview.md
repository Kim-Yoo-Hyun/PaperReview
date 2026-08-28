# robosuite: A Modular Simulation Framework and Benchmark for Robot Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2020 / arXiv
- Category: Benchmarks and Datasets
- Tags: Robotics, Benchmark, simulation, manipulation
- Official paper: https://arxiv.org/abs/2009.12293
- Code/Project: https://robosuite.ai/
- Source audit: arXiv abstract and official documentation checked; benchmark result details remain UNVERIFIED.

## Why This Paper Is Here

표준화된 controller·robot·task 조합을 제공해 manipulation learning 실험의 재현성을 높이는 기반 simulator framework다.

## Problem

robot learning 연구마다 simulation setup과 controller가 달라 algorithm 비교와 재사용이 어려운 문제를 다룬다.

## Core Idea

MuJoCo 위에 modular robot models, grippers, controllers, manipulation tasks와 interfaces를 제공한다.

## Interface

state/RGB observations와 multiple control modes를 simulated robot actions 및 task success로 연결한다.

## Evaluation Scope

suite 자체의 task/controller 사용성과 learning baselines를 제공하며 버전별 protocol 차이를 확인해야 한다.
