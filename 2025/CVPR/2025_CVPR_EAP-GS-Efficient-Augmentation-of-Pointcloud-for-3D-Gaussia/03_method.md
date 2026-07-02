# Method

- Year/Venue: 2025 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, point cloud, 3D Vision
- Paper link: ./2025/CVPR/2025_CVPR_EAP-GS-Efficient-Augmentation-of-Pointcloud-for-3D-Gaussia/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Specifically, we introduce an Attentional Pointcloud Augmentation (APA) technique, which retains two-view tracks as an option for pointcloud generation.
- To address this, we propose EAP-GS, a method to enhance initialization for fast, accurate, and stable few-shot scene reconstruction.
- The training strategy of original 3DGS is not suitable for few-shot reconstruction, leading to severe overfitting.

## 원리적 동기
- In practice, a sufficient number of images are often difficult to obtain due to various limitations.
- Furthermore, our APA can be framed as a modular augmentation to existing methods with minimal overhead.
- Specifically, we introduce an Attentional Pointcloud Augmentation (APA) technique, which retains two-view tracks as an option for pointcloud generation.

## 핵심 방법론
- The training strategy of original 3DGS is not suitable for few-shot reconstruction, leading to severe overfitting.
- In contrast, DRGS mitigates training time through an early-stop strategy, but this may lead to insufficient training.
- In comparison, our augmented pointcloud inherently encodes depth information, providing a good guidance for Gaussian generation.
