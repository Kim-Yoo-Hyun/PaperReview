# Language Embedded 3D Gaussians for Open-Vocabulary Scene Understanding

- Year/Venue: 2024 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, open-vocabulary, semantic
- Authors: Jin-Chuan Shi, Miao Wang, Hao-Bin Duan, Shao-Hua Guan ; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2024, pp. 5333-5343
- Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Shi_Language_Embedded_3D_Gaussians_for_Open-Vocabulary_Scene_Understanding_CVPR_2024_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다.

## Core Idea
핵심은 Gaussian primitive 또는 rendered feature에 language-aligned semantic feature를 부여하여 3DGS를 질의 가능한 장면 표현으로 확장하는 것이다.

## Paper-Specific Cues
- Topic cue: Open-vocabulary querying in 3D space is challenging but essential for scene understanding tasks such as object localization and segmentation.
- Method cue: In this work we introduce Language Embedded 3D Gaussians a novel scene representation for open-vocabulary query tasks.
- Result cue: Instead of embedding high-dimensional raw semantic features on 3D Gaussians we propose a dedicated quantization scheme that drastically alleviates the memory requirement and a ...

## Input / Output
Input: multi-view images/poses or reconstructed scenes plus language query. Output: language-queryable 3D field, mask, grounding, rendering, or scene edit.

## Main Claims
- 논문은 `language-aware Gaussian/implicit 3D scene representation`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
3DGS/NeRF 기반 방법은 scene reconstruction 품질, 카메라 포즈, memory/runtime, dynamic scene 처리에 민감하다.

## Contribution
- language-aware Gaussian/implicit 3D scene representation 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Gaussian Splatting, open-vocabulary, semantic.
- 초록에서 확인되는 주요 cue: Open-vocabulary, Language-embedded, However, Although, Gaussians, Language, Embedded, Instead.
