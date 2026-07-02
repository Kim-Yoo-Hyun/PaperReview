# Problem

- Year/Venue: 2026 / CVPR
- Category: 3D Equivariance, Calibration, and Registration
- Tags: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_BA-GS-Bayesian-Adaptive-Gaussian-Splatting-for-SFM-Free-3D/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Recent works attempt to address this limitation by leveraging pre-trained image matching models to generate Gaussian primitives but overlook the probabilistic uncertainty embedded in both the initial primitive ...
- By robustly handling initialization and optimization noise, our work paves the way for scalable 3D scene reconstruction from sparse image captures. synthesis and scene reconstruction.
- However, its reliance on Structure-from-Motion preprocessing may lead to degraded performance under sparse-view scenarios.

## 해결하려는 문제
- Experiments across multiple benchmark datasets including Tanks and Temples, MVimgNet, and LLFF demonstrate that our method consistently outperforms existing approaches.
- Hence, we propose BA-GS, a Bayesian framework that models both the global distribution and local uncertainty of Gaussian primitives.
- 3D Gaussian Splatting (3DGS) has demonstrated exceptional performance in reconstruction and novel view synthesis tasks.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
