# RT-1: Robotics Transformer for Real-World Control at Scale

- Year/Venue: 2022 / arxiv
- Category: Foundations: Vision-Language-Action and Robotics
- Tags: VLA, Robotics, Imitation Learning
- Authors: Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Joseph Dabis, Chelsea Finn
- Paper: https://arxiv.org/abs/2212.06817
- PDF status: downloaded
- GitHub/Project: https://robotics-transformer1.github.io/

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: By transferring knowledge from large, diverse, task-agnostic datasets, modern machine learning models can solve specific downstream tasks either zero-shot or with small task-specific datasets ...
- Method cue: In this paper, we present a model class, dubbed Robotics Transformer, that exhibits promising scalable model properties.
- Result cue: While this capability has been demonstrated in other fields such as computer vision, natural language processing or speech recognition, it remains to be shown ...

## Input / Output
Input/Output follows the foundational formulation: tokens, images, point sets, trajectories, or scene coordinates mapped to reusable representations or predictions.

## Main Claims
- 논문은 `vision or vision-language foundation model pretraining`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- vision or vision-language foundation model pretraining 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: VLA, Robotics, Imitation Learning.
- 초록에서 확인되는 주요 cue: While, Robotics, Transformer, The.
