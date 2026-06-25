# SpatialLLM: A Compound 3D-Informed Design towards Spatially-Intelligent Large Multimodal Models

- Year/Venue: 2025 / CVPR 2025
- Category: 3D Large Multimodal Models
- Tags: LLM, spatial reasoning, 3D Vision
- Authors: Wufei Ma, Luoxin Ye, Celso M de Melo, Alan Yuille, Jieneng Chen ; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2025, pp. 17249-17260
- Paper: https://openaccess.thecvf.com/content/CVPR2025/html/Ma_SpatialLLM_A_Compound_3D-Informed_Design_towards_Spatially-Intelligent_Large_Multimodal_Models_CVPR_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
VLM/LLM은 강한 semantic prior를 갖지만 3D 위치, 거리, 관점, affordance 같은 metric spatial reasoning에는 취약하다.

## Core Idea
핵심은 2D/3D visual tokens, point/scene representation, language model을 정렬해 공간 질의와 embodied reasoning을 한 모델에서 처리하는 것이다.

## Paper-Specific Cues
- Topic cue: Humans naturally understand 3D spatial relationships, enabling complex reasoning like predicting collisions of vehicles from different directions.
- Method cue: To address data limitations, we develop two types of 3D-informed training datasets: (1) 3D-informed probing data focused on object's 3D location and orientation, and ...
- Result cue: 초록에서 result claim 문장을 자동 추출하지 못함.

## Input / Output
Input: 2D/3D observations, point/scene tokens, and natural-language prompts. Output: spatial answer, grounding result, caption, plan, or embodied reasoning response.

## Main Claims
- 논문은 `3D vision-language spatial reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- 3D vision-language spatial reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: LLM, spatial reasoning, 3D Vision.
- 초록에서 확인되는 주요 cue: Humans, Current, LMMs, This, SpatialLLM, Notably, VQA, Furthermore.
