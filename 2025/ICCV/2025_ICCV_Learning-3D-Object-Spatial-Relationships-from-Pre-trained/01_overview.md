# Learning 3D Object Spatial Relationships from Pre-trained 2D Diffusion Models

- Year/Venue: 2025 / ICCV
- Category: 3D Generative Modeling and Diffusion
- Tags: Diffusion, Generation, 3D Vision
- Authors: not extracted
- Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Baik_Learning_3D_Object_Spatial_Relationships_from_Pre-trained_2D_Diffusion_Models_ICCV_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
생성 모델 또는 policy 모델이 3D 구조와 물리 제약을 보존하지 못하면 로봇 실행이나 3D 장면 생성에서 일관성이 깨진다.

## Core Idea
핵심은 diffusion score/denoising process를 action, 3D generation, 또는 structured scene representation에 적용하면서 geometry prior를 넣는 것이다.

## Paper-Specific Cues
- Topic cue: 초록 cue를 자동 추출하지 못함.
- Method cue: 초록에서 명시적 propose/present 문장을 자동 추출하지 못함.
- Result cue: 초록에서 result claim 문장을 자동 추출하지 못함.

## Input / Output
Input/Output follows the paper task formulation; see PDF for the exact interface.

## Main Claims
- 논문은 `diffusion-based generation or policy learning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- diffusion-based generation or policy learning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Diffusion, Generation, 3D Vision.
