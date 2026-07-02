# Problem

- Year/Venue: 2025 / ICCV
- Category: 3D Semantic Understanding and Alignment
- Tags: Gaussian Splatting, geometry, semantic, alignment, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_SpatialSplat-Efficient-Semantic-3D-from-Sparse-Unposed-Ima/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- To further incorporate semantics while avoiding the significant memory and storage costs of high-dimensional semantic features, existing methods extend this paradigm by associating each primitive with a compressed ...
- However, these methods have two major limitations: (a) the naively compressed feature compromises expressiveness, affecting the model’s ability to capture finegrained semantics, and (b) the pixel-wise primitive prediction ...
- Introduction Reconstructing and understanding 3D scenes from 2D images is a fundamental topic in computer vision, aiming to obtain semantic-aware 3D structure from low-cost devices, i.e., RGB cameras.

## 해결하려는 문제
- We conduct extensive experiments to evaluate our method, demonstrating a remarkable 60% reduction in scene representation parameters while achieving superior performance over state-of-the-art methods.
- Moreover, we propose a selective Gaussian mechanism, which retains only essential Gaussians in the scene, effectively eliminating redundant primitives.
- To this end, we introduce SpatialSplat, a feedforward framework that produces redundancy-aware Gaussians and capitalizes on a dual-field semantic representation.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
