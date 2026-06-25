# ORION: A Holistic End-to-End Autonomous Driving Framework by Vision-Language Instructed Action Generation

- Year/Venue: 2025 / ICCV
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model
- Authors: Haoyu Fu, Diankun Zhang, Zongchuang Zhao, Jianfeng Cui, Dingkang Liang, Chong Zhang, Dingyuan Zhang, Hongwei Xie, Bing Wang, Xiang Bai ; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2025, pp. 24823-24834
- Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
VLM/LLM은 강한 semantic prior를 갖지만 3D 위치, 거리, 관점, affordance 같은 metric spatial reasoning에는 취약하다.

## Core Idea
핵심은 2D/3D visual tokens, point/scene representation, language model을 정렬해 공간 질의와 embodied reasoning을 한 모델에서 처리하는 것이다.

## Paper-Specific Cues
- Topic cue: End-to-end (E2E) autonomous driving methods still struggle to make correct decisions in interactive closed-loop evaluation due to limited causal reasoning capability.
- Method cue: To tackle this issue, we propose ORION, a holistic E2E autonomous driving framework by vision-language instructed action generation.ORION uniquely combines a QT-Former to aggregate ...
- Result cue: Our method achieves an impressive closed-loop performance of 77.47 Driving Score (DS) and 54.62% Success Rate (SR) on the challenge Bench2Drive datasets, which outperforms ...

## Input / Output
Input: 2D/3D observations, point/scene tokens, and natural-language prompts. Output: spatial answer, grounding result, caption, plan, or embodied reasoning response.

## Main Claims
- 논문은 `3D vision-language spatial reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- 3D vision-language spatial reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Vision-Language Model.
- 초록에서 확인되는 주요 cue: End-to-end, E2E, Current, Vision-Language, Models, VLMs, However, ORION.
