# Method

- Year/Venue: 2026 / ICML
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_WorldMirror-Universal-3D-World-Reconstruction-with-Any-Pri/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present WorldMirror, a unified feed-forward model for comprehensive 3D geometric prediction tasks.
- Model Training Our model is trained end-to-end by minimizing a composite loss function L that integrates supervision for all prediction
- Benefiting from our unified multi-task architecture, WorldMirror achieves a true ”one-for-all” paradigm where a single feed-forward pass simultaneously predicts a comprehensive spectrum of heterogeneous 3D representations, including point ...

## 원리적 동기
- Unlike existing methods constrained to image-only inputs or customized for a specific task, our framework flexibly integrates diverse geometric priors, including camera poses, intrinsics, and depth maps, while ...
- Traditional SfM (Schonberger & Frahm, 2016) and MVS rely on costly iterative optimization.
- We present WorldMirror, a unified feed-forward model for comprehensive 3D geometric prediction tasks.

## 핵심 방법론
- Model Training Our model is trained end-to-end by minimizing a composite loss function L that integrates supervision for all prediction
- Benefiting from our unified multi-task architecture, WorldMirror achieves a true ”one-for-all” paradigm where a single feed-forward pass simultaneously predicts a comprehensive spectrum of heterogeneous 3D representations, including point ...
- We then incorporate the normal prediction task into the joint training scheme.
- We observe that training all tasks jointly makes it difficult for the model to disentangle geometry from appearance, resulting in suboptimal performance.
- During training, we employ a systematic decoupled sequential training designed to optimize training efficiency and enhance performance by progressing from simple to complex across task sequencing.
