# CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory

- Year/Venue: 2023 / RSS
- Category: Open-Vocabulary 3D Mapping
- Tags: CLIP, Robotics, semantic, NeRF
- Authors: not extracted
- Paper: https://arxiv.org/abs/2210.05663
- PDF status: downloaded
- GitHub/Project: https://mahis.life/clip-fields/

## Problem
NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다.

## Core Idea
핵심은 radiance field의 공간 좌표/뷰 의존 표현에 CLIP/VLM feature를 결합해 3D 위치에서 언어적 의미를 조회할 수 있게 하는 것이다.

## Paper-Specific Cues
- Topic cue: 초록 cue를 자동 추출하지 못함.
- Method cue: 초록에서 명시적 propose/present 문장을 자동 추출하지 못함.
- Result cue: 초록에서 result claim 문장을 자동 추출하지 못함.

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `language-aware neural radiance field representation`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
3DGS/NeRF 기반 방법은 scene reconstruction 품질, 카메라 포즈, memory/runtime, dynamic scene 처리에 민감하다.

## Contribution
- language-aware neural radiance field representation 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: CLIP, Robotics, semantic, NeRF.
