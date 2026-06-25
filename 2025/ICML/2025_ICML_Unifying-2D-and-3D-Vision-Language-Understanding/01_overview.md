# Unifying 2D and 3D Vision-Language Understanding

- Year/Venue: 2025 / ICML Poster
- Category: 3D Vision-Language Grounding
- Tags: Vision-Language Model, 3D Vision
- Authors: Ayush Jain, Alexander Swerdlow, Yuzhou Wang, Sergio Arnaud, Ada Martin, Alexander Sax, Franziska Meier, Katerina Fragkiadaki
- Paper: https://openreview.net/forum?id=FcTeo26AfZ
- PDF status: downloaded
- GitHub/Project: not identified from OpenReview

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: Progress in 3D vision-language learning has been hindered by the scarcity of large-scale 3D datasets.
- Method cue: We introduce UniVLG, a unified architecture for 2D and 3D vision-language understanding that bridges the gap between existing 2D-centric models and the rich 3D ...
- Result cue: We propose a novel language-conditioned mask decoder shared across 2D and 3D modalities to ground objects effectively in both RGB and RGB-D images, outperforming ...

## Input / Output
Input: 3D scene representation plus free-form natural language. Output: target object, 3D box, mask, or referring expression result.

## Main Claims
- 논문은 `vision-language alignment and multimodal reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- vision-language alignment and multimodal reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Vision-Language Model, 3D Vision.
- 초록에서 확인되는 주요 cue: Progress, UniVLG, Our, RGB, RGB-D, With, Furthermore, Code.
