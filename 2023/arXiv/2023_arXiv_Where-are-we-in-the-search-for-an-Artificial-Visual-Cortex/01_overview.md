# Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence?

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2023 / arXiv
- Category: Robot Learning and Data
- Tags: Robotics, representation learning, Embodied AI, Benchmark
- Official paper: https://arxiv.org/abs/2303.18240
- Code/Project: https://eai-vc.github.io/
- Source audit: arXiv abstract and official project page checked; full benchmark tables remain UNVERIFIED.

## Why This Paper Is Here

VC-1과 함께 embodied task 전반에서 visual representation을 체계적으로 비교한 주요 benchmark/foundation study다.

## Problem

서로 다른 pretraining objective와 dataset의 visual encoder가 embodied control에 얼마나 보편적으로 transfer되는지 평가한다.

## Core Idea

대규모 embodied evaluation suite와 통일된 adaptation protocol로 여러 representation을 비교하고 VC-1을 학습한다.

## Interface

visual observation encoder를 navigation/manipulation policy의 perception front-end로 사용한다.

## Evaluation Scope

다양한 embodied tasks, adaptation regimes와 representation baselines를 포괄한다.
