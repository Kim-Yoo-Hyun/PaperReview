# SpatioLM: Towards General Physical Spatial Intelligence in Vision-Language Models

- Year/Venue: 2026 / ICML 2026 Spotlight
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, 3D Vision
- Authors: jing wu, Jianhua Wu, Jiayi Guan, Jiahong Chen, Jinghui Lu, Hangjun Ye, Bingzhao Gao, Long Chen
- Paper: https://openreview.net/forum?id=CHavqrN1X9
- PDF status: downloaded
- GitHub/Project: not identified from OpenReview

## Problem
VLM/LLM은 강한 semantic prior를 갖지만 3D 위치, 거리, 관점, affordance 같은 metric spatial reasoning에는 취약하다.

## Core Idea
핵심은 2D/3D visual tokens, point/scene representation, language model을 정렬해 공간 질의와 embodied reasoning을 한 모델에서 처리하는 것이다.

## Paper-Specific Cues
- Topic cue: Vision-Language Models (VLMs) perform well on commonsense reasoning tasks but struggle with visual spatial reasoning.
- Method cue: To this end, we propose a parameter-efficient \textit{\textbf{Spatio}-vision \textbf{L}anguage \textbf{M}odels (SpatioLM)}, that enhances spatial intelligence without extra 3D prior inputs or third-party spatial encoders.
- Result cue: Extensive experiments show that SpatioLM achieves significant improvements in diverse tasks, including spatial perception and understanding while effectively limiting the degradation of general capabilities.

## Input / Output
Input: 2D/3D observations, point/scene tokens, and natural-language prompts. Output: spatial answer, grounding result, caption, plan, or embodied reasoning response.

## Main Claims
- 논문은 `3D vision-language spatial reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- 3D vision-language spatial reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Vision-Language Model, 3D Vision.
- 초록에서 확인되는 주요 cue: Vision-Language, Models, VLMs, Most, Spatio, SpatioLM, Concretely, Furthermore.
