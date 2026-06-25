# MM-Spatial: Exploring 3D Spatial Understanding in Multimodal LLMs

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision
- Authors: Erik Daxberger, Nina Wenzel, David Griffiths, Haiming Gang, Justin Lazarow, Gefen Kohavi, Kai Kang, Marcin Eichner, Yinfei Yang, Afshin Dehghan, Peter Grasch ; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2025, pp. 7395-7408
- Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Daxberger_MM-Spatial_Exploring_3D_Spatial_Understanding_in_Multimodal_LLMs_ICCV_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
VLM/LLM은 강한 semantic prior를 갖지만 3D 위치, 거리, 관점, affordance 같은 metric spatial reasoning에는 취약하다.

## Core Idea
핵심은 2D/3D visual tokens, point/scene representation, language model을 정렬해 공간 질의와 embodied reasoning을 한 모델에서 처리하는 것이다.

## Paper-Specific Cues
- Topic cue: Multimodal large language models (MLLMs) excel at 2D visual understanding but remain limited in their ability to reason about 3D space.
- Method cue: 초록에서 명시적 propose/present 문장을 자동 추출하지 못함.
- Result cue: We show that CA-VQA enables us to train MM-Spatial, a strong generalist MLLM that also achieves state-of-the-art performance on 3D spatial understanding benchmarks, including ...

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
- 초록에서 확인되는 주요 cue: Multimodal, MLLMs, Our, Cubify, Anything, VQA, CA-VQA, MM-Spatial.
