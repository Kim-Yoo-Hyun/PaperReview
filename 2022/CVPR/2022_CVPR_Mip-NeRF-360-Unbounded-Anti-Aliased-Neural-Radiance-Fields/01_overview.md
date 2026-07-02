# Mip-NeRF 360: Unbounded Anti-Aliased Neural Radiance Fields

- Year/Venue: 2022 / CVPR
- Category: Foundations: 3D Scene Representations
- Tags: NeRF, 3D Vision, representation, geometry
- Paper link: ./2022/CVPR/2022_CVPR_Mip-NeRF-360-Unbounded-Anti-Aliased-Neural-Radiance-Fields/paper.pdf
- Code/Project: https://jonbarron.info/mipnerf360/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We present an extension of mip-NeRF (a NeRF variant that addresses sampling and aliasing) that uses a non-linear scene parameterization, online distillation, and a novel distortion-based regularizer to ...
- In this setting, existing NeRF-like models often produce blurry or low-resolution renderings (due to the unbalanced detail and scale of nearby and distant objects), are slow to train, ...
- Large and detailed scenes require more network capacity, but densely querying a large MLP along each ray during training is expensive.

## Core Idea
- We present an extension of mip-NeRF (a NeRF variant that addresses sampling and aliasing) that uses a non-linear scene parameterization, online distillation, and a novel distortion-based regularizer to ...
- Large and detailed scenes require more network capacity, but densely querying a large MLP along each ray during training is expensive.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Though neural radiance fields (NeRF) have demonstrated impressive view synthesis results on objects and small bounded regions of space, they struggle on “unbounded” scenes, where the camera may ...
- See the supplemental video for additional results. raises three critical issues: 1.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We present an extension of mip-NeRF (a NeRF variant that addresses sampling and aliasing) that uses a non-linear scene parameterization, online distillation, and a novel distortion-based regularizer to ...
- Though neural radiance fields (NeRF) have demonstrated impressive view synthesis results on objects and small bounded regions of space, they struggle on “unbounded” scenes, where the camera may ...
- Large and detailed scenes require more network capacity, but densely querying a large MLP along each ray during training is expensive.

## Abstract Cue
- Though neural radiance fields (NeRF) have demonstrated impressive view synthesis results on objects and small bounded regions of space, they struggle on “unbounded” scenes, where the camera may point in any direction and content may exist at any distance.
