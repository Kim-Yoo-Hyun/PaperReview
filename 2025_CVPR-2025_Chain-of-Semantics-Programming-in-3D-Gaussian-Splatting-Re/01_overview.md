# Chain of Semantics Programming in 3D Gaussian Splatting Representation for 3D Vision Grounding

- Year/Venue: 2025 / CVPR 2025
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, semantic, grounding
- Authors: Jiaxin Shi, Mingyue Xiang, Hao Sun, Yixuan Huang, Zhi Weng ; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2025, pp. 24560-24569
- Paper: https://openaccess.thecvf.com/content/CVPR2025/html/Shi_Chain_of_Semantics_Programming_in_3D_Gaussian_Splatting_Representation_for_CVPR_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다.

## Core Idea
핵심은 Gaussian primitive 또는 rendered feature에 language-aligned semantic feature를 부여하여 3DGS를 질의 가능한 장면 표현으로 확장하는 것이다.

## Paper-Specific Cues
- Topic cue: 3D Vision Grounding (3DVG) is a fundamental research area that enables agents to perceive and interact with the 3D world.
- Method cue: To address this challenge, we propose a zero-shot neuro-symbolic framework that utilizes a large language model (LLM) as neuro-symbolic functions to ground the object ...
- Result cue: Notably, our method surpasses current state-of-the-art zero-shot methods on the Nr3D dataset.

## Input / Output
Input: multi-view images/poses or reconstructed scenes plus language query. Output: language-queryable 3D field, mask, grounding, rendering, or scene edit.

## Main Claims
- 논문은 `language-aware Gaussian/implicit 3D scene representation`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
3DGS/NeRF 기반 방법은 scene reconstruction 품질, 카메라 포즈, memory/runtime, dynamic scene 처리에 민감하다.

## Contribution
- language-aware Gaussian/implicit 3D scene representation 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Gaussian Splatting, semantic, grounding.
- 초록에서 확인되는 주요 cue: Vision, Grounding, The, LLM, Gaussian, Splatting, Given, Additionally.
