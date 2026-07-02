# Method

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Semantic Understanding and Alignment
- Tags: Gaussian Splatting, semantic, alignment, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_VA-GS-Enhancing-the-Geometric-Representation-of-Gaussian-S/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this work, we propose a novel method that enhances the geometric representation of 3D Gaussians through view alignment (VA).
- To enforce geometric consistency across views, we introduce a visibility-aware photometric alignment loss that models occlusions and encourages accurate spatial relationships among Gaussians.
- To address this limitation, we propose an edge-aware image reconstruction loss that encourages the model to better preserve sharp structures and boundary details: LI = (1 − β1 ...

## 원리적 동기
- This limitation stems from the inherent discrete and unstructured nature of Gaussians, which makes it difficult to enforce global surface consistency or capture fine geometric details, particularly under ...
- Accurate surface reconstruction from multi-view images is a long-standing problem in computer vision, fundamental to applications such as 3D modeling, AR/VR, and robotics.
- In this work, we propose a novel method that enhances the geometric representation of 3D Gaussians through view alignment (VA).

## 핵심 방법론
- To address this limitation, we propose an edge-aware image reconstruction loss that encourages the model to better preserve sharp structures and boundary details: LI = (1 − β1 ...
- We introduce novel constraints to enable accurate surface reconstruction while preserving high-quality novel view synthesis.
- 2 illustrates the overall framework of our approach.
- Given a set of posed RGB images, our goal is to learn a bunch of 3D Gaussian functions with associated attributes, such as color, opacity, position and shape, ...
- However, in boundary regions, the Gaussian primitives often exhibit ambiguous normal directions due to insufficient local support, which can lead to inaccurate geometry reconstruction across different surfaces.
