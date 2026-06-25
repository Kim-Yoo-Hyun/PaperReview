# SpatialStack: Layered Geometry-Language Fusion for 3D VLM Spatial Reasoning

- Year/Venue: 2026 / CVPR
- Category: 3D Large Multimodal Models
- Tags: geometry, VLM, spatial reasoning
- Authors: Jian Zhang, Shijie Zhou, Bangya Liu, Achuta Kadambi, Zhiwen Fan ; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2026, pp. 38678-38688
- Paper: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_SpatialStack_Layered_Geometry-Language_Fusion_for_3D_VLM_Spatial_Reasoning_CVPR_2026_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
VLM/LLM은 강한 semantic prior를 갖지만 3D 위치, 거리, 관점, affordance 같은 metric spatial reasoning에는 취약하다.

## Core Idea
핵심은 2D/3D visual tokens, point/scene representation, language model을 정렬해 공간 질의와 embodied reasoning을 한 모델에서 처리하는 것이다.

## Paper-Specific Cues
- Topic cue: Large vision-language models (VLMs) still struggle with reliable 3D spatial reasoning, a core capability for embodied and physical AI systems.
- Method cue: To overcome this, we propose SpatialStack, a general hierarchical fusion framework that progressively aligns vision, geometry, and language representations across the model hierarchy.
- Result cue: Building upon this framework, we develop VLM-SpatialStack, a model that achieves state-of-the-art performance on multiple 3D spatial reasoning benchmarks.

## Input / Output
Input: 2D/3D observations, point/scene tokens, and natural-language prompts. Output: spatial answer, grounding result, caption, plan, or embodied reasoning response.

## Main Claims
- 논문은 `3D vision-language spatial reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- 3D vision-language spatial reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: geometry, VLM, spatial reasoning.
- 초록에서 확인되는 주요 cue: Large, VLMs, This, While, SpatialStack, Moving, Building, VLM-SpatialStack.
