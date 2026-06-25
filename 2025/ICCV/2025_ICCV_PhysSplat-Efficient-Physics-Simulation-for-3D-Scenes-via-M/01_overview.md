# PhysSplat: Efficient Physics Simulation for 3D Scenes via MLLM-Guided Gaussian Splatting

- Year/Venue: 2025 / ICCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting
- Authors: Haoyu Zhao, Hao Wang, Xingyue Zhao, Hao Fei, Hongqiu Wang, Chengjiang Long, Hua Zou ; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2025, pp. 5242-5252
- Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Zhao_PhysSplat_Efficient_Physics_Simulation_for_3D_Scenes_via_MLLM-Guided_Gaussian_ICCV_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다.

## Core Idea
핵심은 Gaussian primitive 또는 rendered feature에 language-aligned semantic feature를 부여하여 3DGS를 질의 가능한 장면 표현으로 확장하는 것이다.

## Paper-Specific Cues
- Topic cue: Recent advancements in 3D generation models have opened new possibilities for simulating dynamic 3D object movements and customizing behaviors, yet creating this content remains ...
- Method cue: Inspired by human visual reasoning, we propose MLLM-based Physical Property Perception (MLLM-P3) to predict the mean physical properties of objects in a zero-shot manner.
- Result cue: Extensive experiments and user studies demonstrate that our PhysSplat achieves more realistic motion than state-of-the-art methods within 2 minutes on a single GPU.

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
- 초록에서 확인되는 주요 cue: Recent, Current, MLLM, PhysSplat, Inspired, MLLM-based, Physical, Property.
