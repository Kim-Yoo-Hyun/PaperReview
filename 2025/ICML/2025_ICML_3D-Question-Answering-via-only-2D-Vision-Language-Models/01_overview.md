# 3D Question Answering via only 2D Vision-Language Models

- Year/Venue: 2025 / ICML Poster
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, 3D Vision
- Authors: FENGYUN WANG, Sicheng Yu, Jiawei Wu, Jinhui Tang, Hanwang Zhang, Qianru Sun
- Paper: https://openreview.net/forum?id=IkhJApkJQ3
- PDF status: downloaded
- GitHub/Project: not identified from OpenReview

## Problem
VLM/LLM은 강한 semantic prior를 갖지만 3D 위치, 거리, 관점, affordance 같은 metric spatial reasoning에는 취약하다.

## Core Idea
핵심은 2D/3D visual tokens, point/scene representation, language model을 정렬해 공간 질의와 embodied reasoning을 한 모델에서 처리하는 것이다.

## Paper-Specific Cues
- Topic cue: Large vision-language models (LVLMs) have significantly advanced numerous fields.
- Method cue: We propose cdViews, a novel approach to automatically selecting critical and diverse Views for 3D-QA. cdViews consists of two key components: viewSelector prioritizing critical ...
- Result cue: We evaluate cdViews on the widely-used ScanQA and SQA benchmarks, demonstrating that it achieves state-of-the-art performance in 3D-QA while relying solely on 2D models ...

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
- 초록에서 확인되는 주요 cue: Large, LVLMs, Due, Specifically, When, LLAVA-OV, Views, ScanQA.
