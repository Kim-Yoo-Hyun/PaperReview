# Method

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_MS-GS-Multi-Appearance-Sparse-View-3D-Gaussian-Splatting-i/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To eliminate unreliable depth estimation in the alignment process, we propose an SfM-prompted Semantic Alignment scheme.
- Then, to introduce multi-view constraints, we propose a series of geometry-guided supervision steps at virtual views in pixel and feature levels to encourage 3D consistency and reduce overfitting.
- SfM-prompted semantic alignment We propose finding semantic regions enclosed by depth discontinuity using projected SfM points and performing individual alignment.

## 원리적 동기
- To overcome the limitation of the sparse SfM point cloud with limited views, we draw knowledge from the monocular depth estimators that have rapidly progressed.
- High-quality scene reconstruction and novel view synthesis from images is a long-standing research problem with wide-ranging applications in AR/VR, 3D site modeling, autonomous driving, robotics, etc.
- To eliminate unreliable depth estimation in the alignment process, we propose an SfM-prompted Semantic Alignment scheme.

## 핵심 방법론
- To eliminate unreliable depth estimation in the alignment process, we propose an SfM-prompted Semantic Alignment scheme.
- SfM-prompted semantic alignment We propose finding semantic regions enclosed by depth discontinuity using projected SfM points and performing individual alignment.
- To encourage 3D consistency and appearance regularization, our method, illustrated in Fig.
- To improve its robustness in sparse-view synthesis and multi-appearance modeling, MS-GS consists of two parts: Semantic Depth Alignment first constructs a dense point cloud by expanding SfM points ...
- Consequently, overfitting, where the model memorizes the sparse training images instead of learning view-invariant geometry, becomes more severe than in the single appearance setting, as the SoTA methods ...
