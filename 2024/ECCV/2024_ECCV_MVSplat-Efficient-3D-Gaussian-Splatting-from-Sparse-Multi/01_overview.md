# MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_MVSplat-Efficient-3D-Gaussian-Splatting-from-Sparse-Multi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, reconstructing a 3D scene from a single image is inherently ill-posed and ambiguous, posing a significant challenge when applied to a more general and larger scene, which ...
- We consider the problem of 3D scene reconstruction and novel view synthesis from very sparse (i.e., as few as two) images in just one forward pass of a ...
- With our cost volume representation, the task is formulated as learning to perform feature matching to identify the Gaussian centers, unlike the data-driven 3D regression from image features ...

## Core Idea
- For better efficiency, we use Swin Transformer’s local window attention in our Transformer architecture.
- Then, we use a multi-view Transformer with selfand cross-attention layers to exchange information between different views.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- On the large-scale RealEstate10K and ACID benchmarks, MVSplat achieves state-of-the-art performance with the fastest feed-forward inference speed (22 fps).
- We demonstrate the importance of the cost volume representation in learning feed-forward Gaussians via extensive experimental evaluations.
- Following pixelSpalt , we evaluate all methods on three target novel viewpoints for each test

## Limitation
- Our model might produce unreliable results for reflective surfaces like glasses and windows, which are currently open challenges for existing methods (detailed in the supplementary material Appendix A).

## Contribution
- We introduce MVSplat, an efficient model that, given sparse multi-view images as input, predicts clean feed-forward 3D Gaussians.
- On the large-scale RealEstate10K and ACID benchmarks, MVSplat achieves state-of-the-art performance with the fastest feed-forward inference speed (22 fps).
- We demonstrate the importance of the cost volume representation in learning feed-forward Gaussians via extensive experimental evaluations.

## Abstract Cue
- We introduce MVSplat, an efficient model that, given sparse multi-view images as input, predicts clean feed-forward 3D Gaussians.
