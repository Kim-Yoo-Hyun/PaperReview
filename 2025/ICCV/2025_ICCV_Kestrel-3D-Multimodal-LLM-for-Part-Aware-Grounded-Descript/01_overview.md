# Kestrel: 3D Multimodal LLM for Part-Aware Grounded Description

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision
- Authors: Mahmoud Ahmed, Junjie Fei, Jian Ding, Eslam Mohamed Bakr, Mohamed Elhoseiny ; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2025, pp. 8973-8983
- Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Ahmed_Kestrel_3D_Multimodal_LLM_for_Part-Aware_Grounded_Description_ICCV_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
VLM/LLM은 강한 semantic prior를 갖지만 3D 위치, 거리, 관점, affordance 같은 metric spatial reasoning에는 취약하다.

## Core Idea
핵심은 2D/3D visual tokens, point/scene representation, language model을 정렬해 공간 질의와 embodied reasoning을 한 모델에서 처리하는 것이다.

## Paper-Specific Cues
- Topic cue: In this paper, we introduce Part-Aware Point Grounded Description (PaPGD), a challenging task aimed at advancing 3D multimodal learning for fine-grained, part-aware segmentation grounding ...
- Method cue: In this paper, we introduce Part-Aware Point Grounded Description (PaPGD), a challenging task aimed at advancing 3D multimodal learning for fine-grained, part-aware segmentation grounding ...
- Result cue: The extensive experiments demonstrate that Kestrel effectively bridges the gap between part-aware language understanding and 3D segmentation grounding, paving the way for more robust ...

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
- 초록에서 확인되는 주요 cue: Part-Aware, Point, Grounded, Description, PaPGD, Existing, Instructions, GrIn.
