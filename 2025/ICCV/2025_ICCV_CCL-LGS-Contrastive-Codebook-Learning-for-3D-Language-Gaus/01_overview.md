# CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting

- Year/Venue: 2025 / ICCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting
- Authors: Lei Tian, Xiaomin Li, Liqian Ma, Hao Yin, Zirui Zheng, Hefei Huang, Taiqing Li, Huchuan Lu, Xu Jia ; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2025, pp. 9855-9864
- Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Tian_CCL-LGS_Contrastive_Codebook_Learning_for_3D_Language_Gaussian_Splatting_ICCV_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다.

## Core Idea
핵심은 Gaussian primitive 또는 rendered feature에 language-aligned semantic feature를 부여하여 3DGS를 질의 가능한 장면 표현으로 확장하는 것이다.

## Paper-Specific Cues
- Topic cue: Recent advances in 3D reconstruction techniques and vision-language models have fueled significant progress in 3D semantic understanding, a capability critical to robotics, autonomous driving, ...
- Method cue: To mitigate this limitation, we propose CCL-LGS, a novel framework that enforces view-consistent semantic supervision by integrating multi-view semantic cues.
- Result cue: Extensive experiments demonstrate that CCL-LGS outperforms previous state-of-the-art methods.

## Input / Output
Input: multi-view images/poses or reconstructed scenes plus language query. Output: language-queryable 3D field, mask, grounding, rendering, or scene edit.

## Main Claims
- 논문은 `language-aware Gaussian/implicit 3D scene representation`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
3DGS/NeRF 기반 방법은 scene reconstruction 품질, 카메라 포즈, memory/runtime, dynamic scene 처리에 민감하다.

## Contribution
- language-aware Gaussian/implicit 3D scene representation 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D Vision, Gaussian Splatting.
- 초록에서 확인되는 주요 cue: Recent, However, These, Gaussian, CCL-LGS, Specifically, SAM-generated, Next.
