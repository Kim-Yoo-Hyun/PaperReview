# SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding

- Year/Venue: 2025 / CVPR
- Category: 3D Vision-Language Grounding
- Tags: 3D visual grounding, zero-shot, open-vocabulary
- Authors: Rong Li, Shijie Li, Lingdong Kong, Xulei Yang, Junwei Liang ; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2025, pp. 3707-3717
- Paper: https://openaccess.thecvf.com/content/CVPR2025/html/Li_SeeGround_See_and_Ground_for_Zero-Shot_Open-Vocabulary_3D_Visual_Grounding_CVPR_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
3D semantic perception은 라벨 공간이 제한적이고 long-tail 객체/속성/affordance를 다루기 어려워 foundation model alignment가 필요하다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: 3D Visual Grounding (3DVG) aims to locate objects in 3D scenes based on textual descriptions, essential for applications like augmented reality and robotics.
- Method cue: To overcome these limitations, we introduce SeeGround, a zero-shot 3DVG framework leveraging 2D Vision-Language Models (VLMs) trained on large-scale 2D data.
- Result cue: Extensive experiments on ScanRefer and Nr3D demonstrate that our approach outperforms existing zero-shot methods by large margins.

## Input / Output
Input: 3D scene representation plus free-form natural language. Output: target object, 3D box, mask, or referring expression result.

## Main Claims
- 논문은 `open-vocabulary 3D semantic understanding`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
2D foundation model에서 온 semantic feature가 3D geometry와 완벽히 정렬되지 않으며, long-tail 관계/속성 평가는 여전히 어렵다.

## Contribution
- open-vocabulary 3D semantic understanding 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D visual grounding, zero-shot, open-vocabulary.
- 초록에서 확인되는 주요 cue: Visual, Grounding, Traditional, SeeGround, Vision-Language, Models, VLMs, Perspective.
