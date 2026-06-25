# LightSplat: Fast and Memory-Efficient Open-Vocabulary 3D Scene Understanding in Five Seconds

- Year/Venue: 2026 / CVPR 2026
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, open-vocabulary, efficiency
- Authors: Jaehun Bang, Jinhyeok Kim, Minji Kim, Seungheon Jeong, Kyungdon Joo ; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2026, pp. 19812-19821
- Paper: https://openaccess.thecvf.com/content/CVPR2026/html/Bang_LightSplat_Fast_and_Memory-Efficient_Open-Vocabulary_3D_Scene_Understanding_in_Five_CVPR_2026_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다.

## Core Idea
핵심은 Gaussian primitive 또는 rendered feature에 language-aligned semantic feature를 부여하여 3DGS를 질의 가능한 장면 표현으로 확장하는 것이다.

## Paper-Specific Cues
- Topic cue: Open-vocabulary 3D scene understanding enables users to segment novel objects in complex 3D environments through natural language.
- Method cue: To address this, we propose LightSplat, a fast and memory-efficient training-free framework that injects compact 2-byte semantic indices into 3D representations from multi-view images.
- Result cue: As a result, LightSplat achieves state-of-the-art performance with up to 50-400x speedup and 64x lower memory, enabling scalable language-driven 3D understanding.

## Input / Output
Input: multi-view images/poses or reconstructed scenes plus language query. Output: language-queryable 3D field, mask, grounding, rendering, or scene edit.

## Main Claims
- 논문은 `language-aware Gaussian/implicit 3D scene representation`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
3DGS/NeRF 기반 방법은 scene reconstruction 품질, 카메라 포즈, memory/runtime, dynamic scene 처리에 민감하다.

## Contribution
- language-aware Gaussian/implicit 3D scene representation 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Gaussian Splatting, open-vocabulary, efficiency.
- 초록에서 확인되는 주요 cue: Open-vocabulary, However, Gaussian, LightSplat, LERF-OVS, ScanNet, DL3DV-OVS, For.
