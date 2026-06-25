# Egocentric Action-aware Inertial Localization in Point Clouds with Vision-Language Guidance

- Year/Venue: 2025 / ICCV 2025
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model
- Authors: Mingfang Zhang, Ryo Yonetani, Yifei Huang, Liangyang Ouyang, Ruicong Liu, Yoichi Sato ; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2025, pp. 27209-27219
- Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Egocentric_Action-aware_Inertial_Localization_in_Point_Clouds_with_Vision-Language_Guidance_ICCV_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
VLM/LLM은 강한 semantic prior를 갖지만 3D 위치, 거리, 관점, affordance 같은 metric spatial reasoning에는 취약하다.

## Core Idea
핵심은 2D/3D visual tokens, point/scene representation, language model을 정렬해 공간 질의와 embodied reasoning을 한 모델에서 처리하는 것이다.

## Paper-Specific Cues
- Topic cue: This paper presents a novel inertial localization framework named Egocentric Action-aware Inertial Localization (EAIL), which leverages egocentric action cues from head-mounted IMU signals to ...
- Method cue: 초록에서 명시적 propose/present 문장을 자동 추출하지 못함.
- Result cue: The learning process is enhanced using concurrently collected vision and language signals to improve multimodal alignment.

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
- 초록에서 확인되는 주요 cue: This, Egocentric, Action-aware, Inertial, Localization, EAIL, IMU, Human.
