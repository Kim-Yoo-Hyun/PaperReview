# EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite Towards Embodied AI

- Year/Venue: 2024 / CVPR
- Category: Benchmarks and Datasets
- Tags: 3D Vision, Embodied AI, dataset
- Authors: not extracted
- Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Wang_EmbodiedScan_A_Holistic_Multi-Modal_3D_Perception_Suite_Towards_Embodied_AI_CVPR_2024_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: 초록 cue를 자동 추출하지 못함.
- Method cue: 초록에서 명시적 propose/present 문장을 자동 추출하지 못함.
- Result cue: 초록에서 result claim 문장을 자동 추출하지 못함.

## Input / Output
Input: benchmark-specific observations/instructions. Output: standardized labels, tasks, or evaluation scores for comparing models.

## Main Claims
- 논문은 `3D vision and embodied AI`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- 3D vision and embodied AI 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D Vision, Embodied AI, dataset.
