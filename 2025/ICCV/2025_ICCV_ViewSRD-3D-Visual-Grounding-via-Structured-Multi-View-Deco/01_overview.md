# ViewSRD: 3D Visual Grounding via Structured Multi-View Decomposition

- Year/Venue: 2025 / ICCV
- Category: 3D Vision-Language Grounding
- Tags: 3D Vision
- Authors: Ronggang Huang, Haoxin Yang, Yan Cai, Xuemiao Xu, Huaidong Zhang, Shengfeng He ; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2025, pp. 9726-9736
- Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Huang_ViewSRD_3D_Visual_Grounding_via_Structured_Multi-View_Decomposition_ICCV_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: 3D visual grounding aims to identify and localize objects in a 3D space based on textual descriptions.
- Method cue: However, existing methods struggle with disentangling targets from anchors in complex multi-anchor queries and resolving inconsistencies in spatial descriptions caused by perspective variations.To tackle ...
- Result cue: Finally, a Textual-Scene Reasoning module synthesizes multi-view predictions into a unified and robust 3D visual grounding.Experiments on 3D visual grounding datasets show that ViewSRD ...

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
- 초록에서 확인되는 주요 cue: However, ViewSRD, First, Simple, Relation, Decoupling, SRD, These.
