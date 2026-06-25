# Mamba-3VL: Taming State Space Model for 3D Vision Language Learning

- Year/Venue: 2025 / ICCV 2025
- Category: 3D Large Multimodal Models
- Tags: 3D Vision
- Authors: Yuan Wang, Yuxin Chen, Zhongang Qi, Lijun Liu, Jile Jiao, Xuetao Feng, Yujia Liang, Ying Shan, Zhipeng Zhang ; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2025, pp. 6273-6283
- Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Mamba-3VL_Taming_State_Space_Model_for_3D_Vision_Language_Learning_ICCV_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
VLM/LLM은 강한 semantic prior를 갖지만 3D 위치, 거리, 관점, affordance 같은 metric spatial reasoning에는 취약하다.

## Core Idea
핵심은 2D/3D visual tokens, point/scene representation, language model을 정렬해 공간 질의와 embodied reasoning을 한 모델에서 처리하는 것이다.

## Paper-Specific Cues
- Topic cue: 3D vision-language (3D-VL) reasoning, connecting natural language with 3D physical world, represents a milestone in advancing spatial intelligence.
- Method cue: In this paper, we propose Mamba-3VL, a pioneering 3D-VL framework to model complex intra- and inter-modality correlations and enhance spatial relation reasoning, while guaranteeing ...
- Result cue: Despite its potential, straightforward adoption of Mamba to 3D-VL tasks encounters two obstacles: (1) how to perceive the position of 3D objects and understand ...

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
- 초록에서 확인되는 주요 cue: While, State, Space, Models, SSM, Despite, Mamba, Mamba-3VL.
