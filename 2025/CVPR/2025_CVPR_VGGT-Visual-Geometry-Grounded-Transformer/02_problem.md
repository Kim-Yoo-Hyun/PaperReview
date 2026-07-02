# Problem

- Year/Venue: 2025 / CVPR
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, geometry, Transformer
- Paper link: ./2025/CVPR/2025_CVPR_VGGT-Visual-Geometry-Grounded-Transformer/paper.pdf
- Code/Project: https://github.com/facebookresearch/vggt
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Introduction We consider the problem of estimating the 3D attributes of a scene, captured in a set of images, utilizing a feedforward neural network.
- Even so, visual geometry still plays a major role in 3D reconstruction, which increases complexity and computational cost.

## 해결하려는 문제
- The network achieves state-of-the-art results in multiple 3D tasks, including camera parameter estimation, multi-view depth estimation, dense point cloud reconstruction, and 3D point tracking.
- Recent contributions like DUSt3R and its evolution We present VGGT, a feed-forward neural network that directly infers all key 3D attributes of a scene, including camera parameters, point ...
- MASt3R have shown promising results in this direction, but these networks can only process two images at once and rely on post-processing to reconstruct more images, fusing pairwise ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
