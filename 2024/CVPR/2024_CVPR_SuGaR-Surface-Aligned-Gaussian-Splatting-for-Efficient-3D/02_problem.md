# Problem

- Year/Venue: 2024 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_SuGaR-Surface-Aligned-Gaussian-Splatting-for-Efficient-3D/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- We propose a method to allow precise and extremely fast mesh extraction from 3D Gaussian Splatting .
- Gaussian Splatting has recently become very popular as it yields realistic rendering while being significantly faster to train than NeRFs.
- It is however challenging to extract a mesh from the millions of tiny 3D Gaussians as these Gaussians tend to be unorganized after optimization and no method has ...

## 해결하려는 문제
- We propose a method to allow precise and extremely fast mesh extraction from 3D Gaussian Splatting .
- Finally, we introduce an optional refinement strategy that binds Gaussians to the surface of the mesh, and jointly optimizes these Gaussians and the mesh through Gaussian splatting rendering.
- Retrieving such an editable mesh for realistic rendering is done within minutes with our method, compared to hours with the state-of-the-art method on SDFs, while providing a better ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
