# OpenGS-Fusion: Open-Vocabulary Dense Mapping with Hybrid 3D Gaussian Splatting for Refined Object-Level Understanding

- Year/Venue: 2025 / IROS 2025
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting, semantic
- Authors: Dianyi Yang, Xihan Wang, Yu Gao, Shiyang Liu, Bohan Ren, Yufeng Yue
- Paper: https://arxiv.org/abs/2508.01150
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다.

## Core Idea
핵심은 Gaussian primitive 또는 rendered feature에 language-aligned semantic feature를 부여하여 3DGS를 질의 가능한 장면 표현으로 확장하는 것이다.

## Paper-Specific Cues
- Topic cue: Recent advancements in 3D scene understanding have made significant strides in enabling interaction with scenes using open-vocabulary queries, particularly for VR/AR and robotic applications.
- Method cue: In this paper, we present OpenGS-Fusion, an innovative open-vocabulary dense mapping framework that improves semantic modeling and refines object-level understanding.
- Result cue: In this paper, we present OpenGS-Fusion, an innovative open-vocabulary dense mapping framework that improves semantic modeling and refines object-level understanding.

## Input / Output
Input: multi-view images/poses or reconstructed scenes plus language query. Output: language-queryable 3D field, mask, grounding, rendering, or scene edit.

## Main Claims
- 논문은 `language-aware Gaussian/implicit 3D scene representation`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
3DGS/NeRF 기반 방법은 scene reconstruction 품질, 카메라 포즈, memory/runtime, dynamic scene 처리에 민감하다.

## Contribution
- language-aware Gaussian/implicit 3D scene representation 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D Vision, Gaussian Splatting, semantic.
- 초록에서 확인되는 주요 cue: Recent, Nevertheless, OpenGS-Fusion, Gaussian, Truncated, Signed, Distance, Field.
