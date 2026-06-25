# AIDE: Improving 3D Open-Vocabulary Semantic Segmentation by Aligned Vision-Language Learning

- Year/Venue: 2025 / WACV 2025
- Category: Open-Vocabulary 3D Mapping
- Tags: open-vocabulary, semantic, alignment
- Authors: Yimu Wang, Krzysztof Czarnecki ; Proceedings of the Winter Conference on Applications of Computer Vision (WACV), 2025, pp. 2674-2685
- Paper: https://openaccess.thecvf.com/content/WACV2025/html/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
3D semantic perception은 라벨 공간이 제한적이고 long-tail 객체/속성/affordance를 다루기 어려워 foundation model alignment가 필요하다.

## Core Idea
핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다.

## Paper-Specific Cues
- Topic cue: 3D open-vocabulary semantic segmentation aims at recognizing countless categories beyond the limited set of annotations used in traditional settings.
- Method cue: In this paper to address these issues and improve generalization performance we propose an AlIgned 3D Open-Vocabulary SEmantic Segmentation framework called AIDE with two ...
- Result cue: In this paper to address these issues and improve generalization performance we propose an AlIgned 3D Open-Vocabulary SEmantic Segmentation framework called AIDE with two ...

## Input / Output
Input: image/3D observations and natural language. Output: aligned representation, answer, reasoning trace, caption, or grounded decision.

## Main Claims
- 논문은 `open-vocabulary 3D semantic understanding`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
2D foundation model에서 온 semantic feature가 3D geometry와 완벽히 정렬되지 않으며, long-tail 관계/속성 평가는 여전히 어렵다.

## Contribution
- open-vocabulary 3D semantic understanding 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: open-vocabulary, semantic, alignment.
- 초록에서 확인되는 주요 cue: Due, VLMs, However, Moreover, AlIgned, Open-Vocabulary, SEmantic, Segmentation.
