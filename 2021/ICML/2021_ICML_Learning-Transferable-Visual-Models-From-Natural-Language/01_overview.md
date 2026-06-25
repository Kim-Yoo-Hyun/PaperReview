# Learning Transferable Visual Models From Natural Language Supervision

- Year/Venue: 2021 / ICML
- Category: Foundations: Vision-Language Models
- Tags: CLIP, Vision-Language Model, alignment
- Authors: Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal
- Paper: https://arxiv.org/abs/2103.00020
- PDF status: downloaded
- GitHub/Project: https://github.com/openai/CLIP

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories.
- Method cue: 초록에서 명시적 propose/present 문장을 자동 추출하지 못함.
- Result cue: State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories.

## Input / Output
Input/Output follows the foundational formulation: tokens, images, point sets, trajectories, or scene coordinates mapped to reusable representations or predictions.

## Main Claims
- 논문은 `vision or vision-language foundation model pretraining`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- vision or vision-language foundation model pretraining 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: CLIP, Vision-Language Model, alignment.
- 초록에서 확인되는 주요 cue: State-of-the-art, This, Learning, SOTA, After, OCR, The, For.
