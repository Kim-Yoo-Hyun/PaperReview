# Problem

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_Gaussian-Grouping-Segment-and-Edit-Anything-in-3D-Scenes/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Existing methods rely on manually-labeled datasets, which are both costly and limited in scope, or require accurately scanned point clouds as input.
- Open-world 3D scene understanding is an essential challenge, with far-reaching implications for robotics, AR / VR, and autonomous driving.
- By taking multi-view captures, existing NeRF-based methods lift 2D masks or distill CLIP / DINO features via neural fields rendering.

## 해결하려는 문제
- To address this issue, we propose Gaussian Grouping, which extends Gaussian Splatting to jointly reconstruct and segment anything in open-world 3D scenes.
- The recent Gaussian Splatting achieves high-quality and realtime novel-view synthesis of the 3D scenes.
- Based on Gaussian Grouping, we further propose a local Gaussian Editing scheme, which shows efficacy in versatile scene editing applications, including 3D object removal, inpainting, colorization, style transfer ...

## 선행 연구 / 배경 단서
- Existing methods rely on manually-labeled datasets, which are both costly and limited in scope, or require accurately scanned point clouds as input.
- Open-world 3D scene understanding is an essential challenge, with far-reaching implications for robotics, AR / VR, and autonomous driving.
- By taking multi-view captures, existing NeRF-based methods lift 2D masks or distill CLIP / DINO features via neural fields rendering.
