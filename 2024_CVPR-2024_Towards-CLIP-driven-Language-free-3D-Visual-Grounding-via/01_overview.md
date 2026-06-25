# Towards CLIP-driven Language-free 3D Visual Grounding via 2D-3D Relational Enhancement and Consistency

- Year/Venue: 2024 / CVPR 2024
- Category: 3D Vision-Language Grounding
- Tags: 3D visual grounding, CLIP, consistency
- Authors: Yuqi Zhang, Han Luo, Yinjie Lei ; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2024, pp. 13063-13072
- Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Towards_CLIP-driven_Language-free_3D_Visual_Grounding_via_2D-3D_Relational_Enhancement_CVPR_2024_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: 3D visual grounding plays a crucial role in scene understanding with extensive applications in AR/VR.
- Method cue: To tackle the above issues in this paper we introduce a language-free training framework for 3D visual grounding.
- Result cue: Extensive experiments demonstrate that our proposed language-free 3D visual grounding approach can obtain promising performance across three widely used datasets --ScanRefer Nr3D and Sr3D.

## Input / Output
Input: 3D scene representation plus free-form natural language. Output: target object, 3D box, mask, or referring expression result.

## Main Claims
- 논문은 `vision-language alignment and multimodal reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- vision-language alignment and multimodal reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D visual grounding, CLIP, consistency.
- 초록에서 확인되는 주요 cue: Despite, Nevertheless, Neighboring, Relation-aware, Modeling, Cross-modality, Relation, Consistency.
