# Problem

- Year/Venue: 2022 / CVPR
- Category: Foundations: 3D Scene Representations
- Tags: NeRF, 3D Vision, representation, geometry
- Paper link: ./2022/CVPR/2022_CVPR_Mip-NeRF-360-Unbounded-Anti-Aliased-Neural-Radiance-Fields/paper.pdf
- Code/Project: https://jonbarron.info/mipnerf360/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- We present an extension of mip-NeRF (a NeRF variant that addresses sampling and aliasing) that uses a non-linear scene parameterization, online distillation, and a novel distortion-based regularizer to ...
- In this setting, existing NeRF-like models often produce blurry or low-resolution renderings (due to the unbalanced detail and scale of nearby and distant objects), are slow to train, ...
- Large and detailed scenes require more network capacity, but densely querying a large MLP along each ray during training is expensive.

## 해결하려는 문제
- We present an extension of mip-NeRF (a NeRF variant that addresses sampling and aliasing) that uses a non-linear scene parameterization, online distillation, and a novel distortion-based regularizer to ...
- Though neural radiance fields (NeRF) have demonstrated impressive view synthesis results on objects and small bounded regions of space, they struggle on “unbounded” scenes, where the camera may ...
- Large and detailed scenes require more network capacity, but densely querying a large MLP along each ray during training is expensive.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
