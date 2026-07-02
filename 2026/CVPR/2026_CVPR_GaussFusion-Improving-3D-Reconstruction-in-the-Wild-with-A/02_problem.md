# Problem

- Year/Venue: 2026 / CVPR
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_GaussFusion-Improving-3D-Reconstruction-in-the-Wild-with-A/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- We plan to release our code and model. [Project Page] Photorealistic 3D reconstruction and novel-view synthesis are fundamental problems in computer vision, with applications in virtual reality, autonomous ...
- Given an existing reconstruction, we render a Gaussian primitives video buffer encoding depth, normals, opacity, and covariance, which the generator refines to produce temporally coherent, artifact-free frames.
- To address these limitations, several methods have explored leveraging generative priors to enhance 3D reconstruction by generating dense novel-view images.

## 해결하려는 문제
- Introduction We present GaussFusion, a novel approach for improving 3D Gaussian splatting (3DGS) reconstructions in the wild through geometry-informed video generation.
- GaussFusion achieves state-of-the-art performance on novel view synthesis benchmarks, and an efficient variant runs in real time at 16 FPS while maintaining similar performance, enabling interactive 3D applications.
- Given an existing reconstruction, we render a Gaussian primitives video buffer encoding depth, normals, opacity, and covariance, which the generator refines to produce temporally coherent, artifact-free frames.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
