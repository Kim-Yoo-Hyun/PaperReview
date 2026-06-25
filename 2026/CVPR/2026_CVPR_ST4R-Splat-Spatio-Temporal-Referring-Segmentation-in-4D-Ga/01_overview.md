# ST4R-Splat: Spatio-Temporal Referring Segmentation in 4D Gaussian Splatting

- Year/Venue: 2026 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, 4D, referring segmentation
- Authors: Yuming Meng, Dong Wu, Hongbin Zha ; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2026, pp. 17598-17608
- Paper: https://openaccess.thecvf.com/content/CVPR2026/html/Meng_ST4R-Splat_Spatio-Temporal_Referring_Segmentation_in_4D_Gaussian_Splatting_CVPR_2026_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다.

## Core Idea
핵심은 Gaussian primitive 또는 rendered feature에 language-aligned semantic feature를 부여하여 3DGS를 질의 가능한 장면 표현으로 확장하는 것이다.

## Paper-Specific Cues
- Topic cue: Understanding objects in dynamic 4D environments via natural language is crucial yet underexplored.
- Method cue: We introduce Spatio-Temporal Referring Segmentation in 4D Gaussian Splatting (STRS-4DGS), a novel task aiming to jointly identify and segment a target instance across space ...
- Result cue: Evaluated on our newly constructed STRS-4DGS benchmark, our method significantly outperforms adapted state-of-the-art baselines across both time-agnostic and time-sensitive metrics, establishing a strong foundation ...

## Input / Output
Input: multi-view images/poses or reconstructed scenes plus language query. Output: language-queryable 3D field, mask, grounding, rendering, or scene edit.

## Main Claims
- 논문은 `language-aware Gaussian/implicit 3D scene representation`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
3DGS/NeRF 기반 방법은 scene reconstruction 품질, 카메라 포즈, memory/runtime, dynamic scene 처리에 민감하다.

## Contribution
- language-aware Gaussian/implicit 3D scene representation 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Gaussian Splatting, 4D, referring segmentation.
- 초록에서 확인되는 주요 cue: Understanding, While, Spatio-Temporal, Referring, Segmentation, Gaussian, Splatting, STRS-4DGS.
