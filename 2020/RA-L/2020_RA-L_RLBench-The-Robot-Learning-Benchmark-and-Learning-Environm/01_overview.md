# RLBench: The Robot Learning Benchmark & Learning Environment

- Year/Venue: 2020 / RA-L
- Category: Benchmarks and Datasets
- Tags: Robotics, Benchmark, Imitation Learning, Reinforcement Learning, multi-task manipulation, 3D Vision
- Official paper: https://arxiv.org/abs/1909.12271
- Official PDF: https://arxiv.org/pdf/1909.12271
- Code/Project: https://github.com/stepjam/RLBench
- Source audit: official abstract/proceedings reviewed on 2026-08-12; full text manual review required for exact implementation and numeric claims.

## Why This Paper Is Here

PerAct/RVT/EquAct/SUGAR 계열을 같은 task family에서 해석하기 위한 manipulation benchmark 원 논문.

## Problem

Few-shot, multi-task, imitation, reinforcement learning과 classical planning을 넓은 manipulation task 집합에서 비교할 공통 environment가 필요하다.

## Core Idea

- 100개 hand-designed manipulation task와 task variation을 제공한다.
- RGB, depth, segmentation과 proprioception을 포함한 multi-modal observation을 지원한다.
- Motion-planned demonstration 생성과 새 task 검증 도구를 제공한다.

## Observation / State / Action Interface

Task environment가 observation, action mode, demonstration과 success condition을 제공하는 robot-learning API다.

## Evaluation Scope

- 원 논문은 100개 task와 large-scale few-shot challenge를 정의한다.
- 후속 논문 비교 시 사용 task subset, camera, action mode, demo 수와 evaluation variation을 반드시 기록한다.

## Limitations to Verify

- 논문마다 task subset과 action mode가 달라 headline success를 직접 비교하기 어렵다.
- Simulation success가 contact robustness와 real-robot safety를 보장하지 않는다.

## Reading Lineage

`RLBench → PerAct / RVT / SUGAR → EquAct and 3D-aware VLA evaluation`
