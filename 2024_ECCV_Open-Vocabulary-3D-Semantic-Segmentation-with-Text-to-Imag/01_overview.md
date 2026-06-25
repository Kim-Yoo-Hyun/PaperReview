# Open-Vocabulary 3D Semantic Segmentation with Text-to-Image Diffusion Models

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision, Diffusion, semantic
- Authors: Xiaoyu Zhu*, Hao Zhou, Pengfei Xing, Long Zhao, Hao Xu, Junwei Liang, Alexander G. Hauptmann, Ting Liu, Andrew Gallagher
- Paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4252_ECCV_2024_paper.php
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
VLM/LLM은 강한 semantic prior를 갖지만 3D 위치, 거리, 관점, affordance 같은 metric spatial reasoning에는 취약하다.

## Core Idea
핵심은 2D/3D visual tokens, point/scene representation, language model을 정렬해 공간 질의와 embodied reasoning을 한 모델에서 처리하는 것이다.

## Paper-Specific Cues
- Topic cue: "In this paper, we investigate the use of diffusion models which are pre-trained on large-scale image-caption pairs for open-vocabulary 3D semantic understanding.
- Method cue: We propose a novel method, namely Diff2Scene, which leverages frozen representations from text-image generative models, along with salient-aware and geometric-aware masks, for open-vocabulary 3D ...
- Result cue: We show that it outperforms competitive baselines and achieves significant improvements over state-of-the-art methods.

## Input / Output
Input: 2D/3D observations, point/scene tokens, and natural-language prompts. Output: spatial answer, grounding result, caption, plan, or embodied reasoning response.

## Main Claims
- 논문은 `3D vision-language spatial reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- 3D vision-language spatial reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D Vision, Diffusion, semantic.
- 초록에서 확인되는 주요 cue: Diff2Scene, ScanNet200.
