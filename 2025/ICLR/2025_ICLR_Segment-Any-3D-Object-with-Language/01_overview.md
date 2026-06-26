# Segment Any 3D Object with Language

- Year/Venue: 2025 / ICLR Poster
- Category: 3D Representation Learning and Foundation Models
- Tags: 3D Vision
- Authors: Seungjun Lee, Yuyang Zhao, Gim Hee Lee
- Paper: https://openreview.net/forum?id=ENv1CeTwxc
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: In this paper, we investigate Open-Vocabulary 3D Instance Segmentation (OV-3DIS) with free-form language instructions.
- Method cue: To the end, we introduce Segment any 3D Object with LanguagE ($\textbf{SOLE}$), which is a semantic and geometric-aware visual-language learning framework with strong generalizability ...
- Result cue: Our SOLE outperforms previous methods by a large margin on ScanNetv2, ScanNet200, and Replica benchmarks, and the results are even closed to the fully-supervised ...

## Input / Output
Input/Output follows the paper task formulation; see PDF for the exact interface.

## Main Claims
- 논문은 `3D vision and embodied AI`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- 3D vision and embodied AI 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D Vision.
- 초록에서 확인되는 주요 cue: Open-Vocabulary, Instance, Segmentation, OV-3DIS, Earlier, However, Instead, Segment.
