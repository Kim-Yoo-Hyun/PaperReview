# GroundFlow: A Plug-in Module for Temporal Reasoning on 3D Point Cloud Sequential Grounding

- Year/Venue: 2025 / ICCV
- Category: 3D Vision-Language Grounding
- Tags: 3D Vision
- Authors: Zijun Lin, Shuting He, Cheston Tan, Bihan Wen ; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2025, pp. 28774-28784
- Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Lin_GroundFlow_A_Plug-in_Module_for_Temporal_Reasoning_on_3D_Point_ICCV_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: Sequential grounding in 3D point clouds (SG3D) refers to locating sequences of objects by following text instructions for a daily activity with detailed steps.
- Method cue: To fill this gap, we propose GroundFlow -- a plug-in module for temporal reasoning on 3D point cloud sequential grounding.
- Result cue: Due to the lack of an effective module for collecting related historical information, state-of-the-art 3DVG methods face significant challenges in adapting to the SG3D ...

## Input / Output
Input: 3D scene representation plus free-form natural language. Output: target object, 3D box, mask, or referring expression result.

## Main Claims
- 논문은 `vision-language alignment and multimodal reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- vision-language alignment and multimodal reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D Vision.
- 초록에서 확인되는 주요 cue: Sequential, SG3D, Current, However, This, Due, GroundFlow, Firstly.
