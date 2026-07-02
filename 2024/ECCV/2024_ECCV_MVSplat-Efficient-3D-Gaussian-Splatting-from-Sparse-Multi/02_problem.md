# Problem

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_MVSplat-Efficient-3D-Gaussian-Splatting-from-Sparse-Multi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- However, reconstructing a 3D scene from a single image is inherently ill-posed and ambiguous, posing a significant challenge when applied to a more general and larger scene, which ...
- We consider the problem of 3D scene reconstruction and novel view synthesis from very sparse (i.e., as few as two) images in just one forward pass of a ...
- With our cost volume representation, the task is formulated as learning to perform feature matching to identify the Gaussian centers, unlike the data-driven 3D regression from image features ...

## 해결하려는 문제
- We introduce MVSplat, an efficient model that, given sparse multi-view images as input, predicts clean feed-forward 3D Gaussians.
- On the large-scale RealEstate10K and ACID benchmarks, MVSplat achieves state-of-the-art performance with the fastest feed-forward inference speed (22 fps).
- We demonstrate the importance of the cost volume representation in learning feed-forward Gaussians via extensive experimental evaluations.

## 선행 연구 / 배경 단서
- However, reconstructing a 3D scene from a single image is inherently ill-posed and ambiguous, posing a significant challenge when applied to a more general and larger scene, which ...
- We consider the problem of 3D scene reconstruction and novel view synthesis from very sparse (i.e., as few as two) images in just one forward pass of a ...
- With our cost volume representation, the task is formulated as learning to perform feature matching to identify the Gaussian centers, unlike the data-driven 3D regression from image features ...
