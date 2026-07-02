# MonoScene: Monocular 3D Semantic Scene Completion

- Year/Venue: 2022 / CVPR
- Category: Foundations: 3D Semantic Occupancy
- Tags: 3D Vision, semantic, occupancy, monocular geometry
- Paper link: ./2022/CVPR/2022_CVPR_MonoScene-Monocular-3D-Semantic-Scene-Completion/paper.pdf
- Code/Project: https://github.com/cv-rits/MonoScene
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Different from the SSC literature, relying on 2.5 or 3D input, we solve the complex problem of 2D to 3D scene reconstruction while jointly inferring its semantics.
- To solve this challenging problem, we project 2D features along their line of sight, inspired by optics, bridging 2D and 3D networks while letting the 3D network self-discover ...
- Introduction Estimating 3D from an image is a problem that goes back to the roots of computer vision .

## Core Idea
- Along with architectural contributions, we introduce novel global scene and local frustums losses.
- We report the performance on semantic scene completion (SSC mIoU) and scene completion (SC - IoU) for RGB-inferred baselines and our method.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments show we outperform the literature on all metrics and datasets while hallucinating plausible scenery even beyond the camera field of view.
- Importantly, the IoU is improved or on par (+3.87 and +0.16) which demonstrates our network captures the scene geometry while avoiding naively increasing the mIoU by lowering the ...
- On both datasets we outperform all methods by a significant mIoU margin of +4.03 on NYUv2 (Tab.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments show we outperform the literature on all metrics and datasets while hallucinating plausible scenery even beyond the camera field of view.
- Along with architectural contributions, we introduce novel global scene and local frustums losses.
- 1, where it outperformed all comparable baselines and even some 3D input baselines.

## Abstract Cue
- Outside FOV MonoScene proposes a 3D Semantic Scene Completion (SSC) framework, where the dense geometry and semantics of a scene are inferred from a single monocular RGB image.
