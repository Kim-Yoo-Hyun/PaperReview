# LangRef3DGS: Natural Language-Guided 3D Referential Segmentation from Partial Observations via 3D Gaussian Splatting

- Year/Venue: 2026 / CVPR
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, referring segmentation, language
- Authors: Xulun Ye, Qin Zhang, Kun Zhou ; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2026, pp. 38595-38605
- Paper: https://openaccess.thecvf.com/content/CVPR2026/html/Ye_LangRef3DGS_Natural_Language-Guided_3D_Referential_Segmentation_from_Partial_Observations_via_CVPR_2026_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다.

## Core Idea
핵심은 Gaussian primitive 또는 rendered feature에 language-aligned semantic feature를 부여하여 3DGS를 질의 가능한 장면 표현으로 확장하는 것이다.

## Paper-Specific Cues
- Topic cue: Language-guided 3D segmentation is crucial for linking 3D perception with semantic understanding, yet it remains vulnerable to the sparse and occluded views common in ...
- Method cue: To overcome this, we present a real-time framework that leverages 3D Gaussian Splatting (3DGS) to build a semantically continuous and differentiable embedding field from ...
- Result cue: Extensive experiments on challenging benchmarks demonstrate that our method achieves strong performance, exhibiting superior accuracy, robustness to partial inputs, and a powerful capacity for ...

## Input / Output
Input: multi-view images/poses or reconstructed scenes plus language query. Output: language-queryable 3D field, mask, grounding, rendering, or scene edit.

## Main Claims
- 논문은 `language-aware Gaussian/implicit 3D scene representation`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
3DGS/NeRF 기반 방법은 scene reconstruction 품질, 카메라 포즈, memory/runtime, dynamic scene 처리에 민감하다.

## Contribution
- language-aware Gaussian/implicit 3D scene representation 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Gaussian Splatting, referring segmentation, language.
- 초록에서 확인되는 주요 cue: Language-guided, RGB-D, Gaussian, Splatting, Our, Dirichlet, Process, This.
