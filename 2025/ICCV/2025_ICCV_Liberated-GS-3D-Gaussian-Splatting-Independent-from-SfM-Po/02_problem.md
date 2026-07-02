# Problem

- Year/Venue: 2025 / ICCV
- Category: 3D Equivariance, Calibration, and Registration
- Tags: Gaussian Splatting, geometry, point cloud, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_Liberated-GS-3D-Gaussian-Splatting-Independent-from-SfM-Po/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- To address this limitation, we propose a novel initialization pipeline, achieving highfidelity reconstruction from dense image sequences without relying on SfM-derived point clouds.
- While 3DGS effectively addresses the slow rendering problem caused by radiance fields, it introduces additional input requirements.
- However, it heavily relies on high-quality initial sparse points from Structure-from-Motion (SfM), which often struggles in textureless regions, degrading the geometry and visual quality of 3DGS.

## 해결하려는 문제
- Extensive experiments demonstrate the superiority of our method over previous approaches and its compatibility with other advanced 3D Gaussian models.
- Notably, our method outperforms the SfM-based method by a 14.4% improvement in LPIPS on 1.
- To address this limitation, we propose a novel initialization pipeline, achieving highfidelity reconstruction from dense image sequences without relying on SfM-derived point clouds.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
