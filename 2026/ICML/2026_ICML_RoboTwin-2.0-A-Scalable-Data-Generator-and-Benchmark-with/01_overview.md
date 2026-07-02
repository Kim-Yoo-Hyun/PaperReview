# RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation

- Year/Venue: 2026 / ICML
- Category: Benchmarks and Datasets
- Tags: VLA, Robotics, Benchmark
- Paper link: ./2026/ICML/2026_ICML_RoboTwin-2.0-A-Scalable-Data-Generator-and-Benchmark-with/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, existing synthetic datasets remain insufficient for robust bimanual manipulation due to two key challenges: (1) the lack of an autonomous self-correcting mechanism to resolve execution failures in ...
- While recent Vision–Language–Action (VLA) (Zheng et al., 2025; Bi et al., 2025; Team, 2025a; Intelligence et al., 2025a; Li et al., 2025; Cai et al., 2026; Wu et ...

## Core Idea
- To this end, we present RoboTwin 2.0, a scalable simulation framework that enables closed-loop, automated, large-scale generation of diverse and realistic data, along with unified evaluation protocols for ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- our synthetic data achieve a 3.6× improvement in few-shot real-world transfer (over a 10-demo baseline) and a 2.2× gain in zero-shot generalization.
- VLA models pre-trained on RoboTwin 2.0 data achieve a 3.6× improvement in few-shot real-world transfer and a 2.2× gain in zero-shot generalization compared to baselines trained on real-world ...
- The framework comprises: (1) an automated expert pipeline that integrates MLLMs with simulation feedback to validate and iteratively refine task execution code; (2) comprehensive domain randomization over language, ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- our synthetic data achieve a 3.6× improvement in few-shot real-world transfer (over a 10-demo baseline) and a 2.2× gain in zero-shot generalization.
- To this end, we present RoboTwin 2.0, a scalable simulation framework that enables closed-loop, automated, large-scale generation of diverse and realistic data, along with unified evaluation protocols for ...
- However, existing synthetic datasets remain insufficient for robust bimanual manipulation due to two key challenges: (1) the lack of an autonomous self-correcting mechanism to resolve execution failures in ...

## Abstract Cue
- our synthetic data achieve a 3.6× improvement in few-shot real-world transfer (over a 10-demo baseline) and a 2.2× gain in zero-shot generalization.
