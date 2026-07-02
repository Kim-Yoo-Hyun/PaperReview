# Problem

- Year/Venue: 2026 / ICML
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_EnerGS-Energy-Based-Gaussian-Splatting-under-Partial-Geome/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- In such sparse-view regimes, the reconstruction problem becomes inherently ill-posed.
- To address this challenge, we model partially observable geometry as a continuous energy field induced by geometric evidence and propose EnerGS.
- 3D Gaussian Splatting (3DGS) has been widely adopted for scene reconstruction, where training inherently constitutes a highly coupled and nonconvex optimization problem.

## 해결하려는 문제
- Extensive experiments on large-scale outdoor scenes demonstrate that, under both sparse multi-view and monocular settings, EnerGS consistently improves photometric quality and geometric stability, while effectively mitigating overfitting during ...
- 3D Gaussian Splatting (3DGS) has been widely adopted for scene reconstruction, where training inherently constitutes a highly coupled and nonconvex optimization problem.
- EnerGS addresses this limitation by partitioning space into occupied, free, and unknown regions and guiding the spatial distribution of Gaussians with a geometric energy field, enabling more stable ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
