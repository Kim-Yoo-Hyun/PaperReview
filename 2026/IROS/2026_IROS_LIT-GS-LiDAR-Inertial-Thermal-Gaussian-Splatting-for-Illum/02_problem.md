# Problem

- Year/Venue: 2026 / IROS
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting
- Paper link: ./2026/IROS/2026_IROS_LIT-GS-LiDAR-Inertial-Thermal-Gaussian-Splatting-for-Illum/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- This efficiency has rapidly motivated radiance-field mapping for robotics and large-scale environments, yet most existing 3DGS-based mapping pipelines still depend heavily on RGB imagery and Structure-from-Motion (SfM) to ...
- Reliance on visible imagery poses a fundamental limitation.
- — Gaussian Splatting has enabled real-time neural rendering, yet existing LiDAR–inertial–visual (LIV) Gaussian mapping pipelines remain fragile under illumination changes and texture-deficient scenes due to their reliance on ...

## 해결하려는 문제
- Experiments on proprietary sequences and public datasets demonstrate that LIT-GS consistently improves geometric accuracy and rendering quality over state-of-the-art LIV-based Gaussian Splatting baselines, particularly in challenging lighting conditions.
- We present LIT-GS, a LiDAR–inertial–thermal Gaussian Splatting framework that injects LiDAR-derived plane geometry as an explicit constraint in both pose/structure refinement and Gaussian optimization.
- — Gaussian Splatting has enabled real-time neural rendering, yet existing LiDAR–inertial–visual (LIV) Gaussian mapping pipelines remain fragile under illumination changes and texture-deficient scenes due to their reliance on ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
