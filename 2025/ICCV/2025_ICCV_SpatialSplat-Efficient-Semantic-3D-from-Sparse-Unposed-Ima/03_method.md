# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Semantic Understanding and Alignment
- Tags: Gaussian Splatting, geometry, semantic, alignment, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_SpatialSplat-Efficient-Semantic-3D-from-Sparse-Unposed-Ima/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- 3, our method is faster than LSM thanks to its streamlined architecture, requiring only 40% of the storage size and 65% of primitive number.
- Notably, since Replica is a synthetic dataset with a different data modality from our training set, this underscores the strong generalization ability of our approach.
- Moreover, we propose a selective Gaussian mechanism, which retains only essential Gaussians in the scene, effectively eliminating redundant primitives.

## 원리적 동기
- To further incorporate semantics while avoiding the significant memory and storage costs of high-dimensional semantic features, existing methods extend this paradigm by associating each primitive with a compressed ...
- However, these methods have two major limitations: (a) the naively compressed feature compromises expressiveness, affecting the model’s ability to capture finegrained semantics, and (b) the pixel-wise primitive prediction ...
- 3, our method is faster than LSM thanks to its streamlined architecture, requiring only 40% of the storage size and 65% of primitive number.

## 핵심 방법론
- 3, our method is faster than LSM thanks to its streamlined architecture, requiring only 40% of the storage size and 65% of primitive number.
- Notably, since Replica is a synthetic dataset with a different data modality from our training set, this underscores the strong generalization ability of our approach.
- Additionally, we introduce a Selective Gaussian Mechanism that directly identifies redundant Gaussians caused by pixel-wise predictions without requiring geometric priors.
- We present an efficient feed-forward network that generates compact yet high-performance representations for 3D reconstruction and scene understanding from sparse, unposed images.
- Remarkably, our approach requires even fewer Gaussians parameters than NoPoSplat, which lacks semantic awareness.
