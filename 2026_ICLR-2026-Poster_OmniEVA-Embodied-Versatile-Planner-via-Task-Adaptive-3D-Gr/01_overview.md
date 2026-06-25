# OmniEVA: Embodied Versatile Planner via Task-Adaptive 3D-Grounded and Embodiment-aware Reasoning

- Year/Venue: 2026 / ICLR 2026 Poster
- Category: 3D Large Multimodal Models
- Tags: 3D Vision
- Authors: Yuecheng Liu, DaFeng Chi, Shiguang Wu, Zhanguang Zhang, Yuzheng Zhuang, Bowen Yang, He Zhu, Lingfeng Zhang
- Paper: https://openreview.net/forum?id=tkEmIJv1tB
- PDF status: downloaded
- GitHub/Project: not identified from OpenReview

## Problem
VLM/LLM은 강한 semantic prior를 갖지만 3D 위치, 거리, 관점, affordance 같은 metric spatial reasoning에는 취약하다.

## Core Idea
핵심은 2D/3D visual tokens, point/scene representation, language model을 정렬해 공간 질의와 embodied reasoning을 한 모델에서 처리하는 것이다.

## Paper-Specific Cues
- Topic cue: Recent advances in multimodal large language models (MLLMs) have opened new opportunities for embodied intelligence, enabling multimodal understanding, reasoning, and interaction, as well as ...
- Method cue: Second, **Embodiment Constraint Gap**: prior work often neglects the physical constraints of real robots, resulting in task plans that are theoretically valid but practically ...
- Result cue: Extensive experiments show that OmniEVA achieves state-of-the-art performance on 7 of 8 embodied reasoning benchmarks and excels in downstream tasks such as object navigation ...

## Input / Output
Input: 2D/3D observations, point/scene tokens, and natural-language prompts. Output: spatial answer, grounding result, caption, plan, or embodied reasoning response.

## Main Claims
- 논문은 `3D vision-language spatial reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- 3D vision-language spatial reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D Vision.
- 초록에서 확인되는 주요 cue: Recent, MLLMs, Nevertheless, MLLM-based, First, Geometric, Adaptability, Gap.
