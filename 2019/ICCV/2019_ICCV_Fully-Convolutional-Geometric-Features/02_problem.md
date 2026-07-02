# Problem

- Year/Venue: 2019 / ICCV
- Category: 3D Equivariance, Calibration, and Registration
- Tags: 3D Vision, registration, 3D geometry, representation
- Paper link: ./2019/ICCV/2019_ICCV_Fully-Convolutional-Geometric-Features/paper.pdf
- Code/Project: https://github.com/chrischoy/FCGF
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Existing learning-based features rely on low-level geometric characteristics as input: e.g., angular deviation , point distributions , or volumetric distance functions .
- This process is computationally expensive and features are extracted only at downsampled interest points, thus lowering the spatial resolution for subsequent registration steps.

## 해결하려는 문제
- Fullyconvolutional geometric features achieve state-of-the-art accuracy without requiring prepossessing, are compact (32 dimensions), and are 290 times faster than the most accurate prior method.
- In this work, we present fully-convolutional geometric features, computed in a single pass by a 3D fully-convolutional network.
- We experimentally validate our approach on both indoor and outdoor datasets.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
