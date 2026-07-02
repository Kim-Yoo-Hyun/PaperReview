# Problem

- Year/Venue: 2025 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, point cloud, 3D Vision
- Paper link: ./2025/CVPR/2025_CVPR_UniPre3D-Unified-Pre-training-of-3D-Point-Cloud-Models-wit/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Enc The scale diversity of point cloud data presents significant challenges in developing unified representation learning techniques for 3D vision.
- A key challenge lies in the greater scale diversity of point clouds compared to images.
- Currently, there are few unified 3D models, and no existing pre-training method is equally effective for both object- and scene-level point clouds.

## 해결하려는 문제
- In this paper, we introduce UniPre3D, the first unified pretraining method that can be seamlessly applied to point clouds of any scale and 3D models of any architecture.
- Our approach predicts Gaussian primitives as the pre-training task and employs differentiable Gaussian splatting to render images, enabling precise pixel-level supervision and end-to-end optimization.
- We propose a unified pre-training method that is applicable and effective to both object- and scene-level point clouds and models.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
