# Gaussian Splatting Visual MPC for Granular Media Manipulation

- Year/Venue: 2025 / ICRA
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Robotics, Gaussian Splatting
- Authors: Wei-Cheng Tseng, Ellina Zhang, Krishna Murthy Jatavallabhula, Florian Shkurti
- Paper: https://www.proceedings.com/content/081/081087webtoc.pdf
- PDF status: downloaded
- GitHub/Project: not identified from venue audit

## Problem
NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다.

## Core Idea
핵심은 Gaussian primitive 또는 rendered feature에 language-aligned semantic feature를 부여하여 3DGS를 질의 가능한 장면 표현으로 확장하는 것이다.

## Paper-Specific Cues
- Topic cue: Recent advancements in learned 3D representations have enabled significant progress in solving complex robotic manipulation tasks, particularly for rigid-body objects.
- Method cue: In this work, we propose a novel approach that learns a visual dynamics model over Gaussian splatting representations of scenes and leverages this model ...
- Result cue: We also show significant prediction and manipulation performance improvements compared to existing granular media manipulation methods.

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `language-aware Gaussian/implicit 3D scene representation`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
3DGS/NeRF 기반 방법은 scene reconstruction 품질, 카메라 포즈, memory/runtime, dynamic scene 처리에 민감하다.

## Contribution
- language-aware Gaussian/implicit 3D scene representation 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Robotics, Gaussian Splatting.
- 초록에서 확인되는 주요 cue: Recent, However, Current, Gaussian, Model-Predictive, Control, Our.
