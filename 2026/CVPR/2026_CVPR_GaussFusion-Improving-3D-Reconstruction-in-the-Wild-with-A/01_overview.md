# GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator

- Year/Venue: 2026 / CVPR
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_GaussFusion-Improving-3D-Reconstruction-in-the-Wild-with-A/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We plan to release our code and model. [Project Page] Photorealistic 3D reconstruction and novel-view synthesis are fundamental problems in computer vision, with applications in virtual reality, autonomous ...
- Given an existing reconstruction, we render a Gaussian primitives video buffer encoding depth, normals, opacity, and covariance, which the generator refines to produce temporally coherent, artifact-free frames.
- To address these limitations, several methods have explored leveraging generative priors to enhance 3D reconstruction by generating dense novel-view images.

## Core Idea
- Introduction We present GaussFusion, a novel approach for improving 3D Gaussian splatting (3DGS) reconstructions in the wild through geometry-informed video generation.
- Unlike prior RGB-based approaches limited to a single reconstruction pipeline, our method introduces a geometryinformed video-to-video generator that refines 3DGS renderings across both optimization-based and feed-forward methods.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- GaussFusion achieves state-of-the-art performance on novel view synthesis benchmarks, and an efficient variant runs in real time at 16 FPS while maintaining similar performance, enabling interactive 3D applications.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Introduction We present GaussFusion, a novel approach for improving 3D Gaussian splatting (3DGS) reconstructions in the wild through geometry-informed video generation.
- GaussFusion achieves state-of-the-art performance on novel view synthesis benchmarks, and an efficient variant runs in real time at 16 FPS while maintaining similar performance, enabling interactive 3D applications.
- Given an existing reconstruction, we render a Gaussian primitives video buffer encoding depth, normals, opacity, and covariance, which the generator refines to produce temporally coherent, artifact-free frames.

## Abstract Cue
- Introduction We present GaussFusion, a novel approach for improving 3D Gaussian splatting (3DGS) reconstructions in the wild through geometry-informed video generation.
