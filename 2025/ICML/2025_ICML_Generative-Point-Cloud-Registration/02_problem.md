# Problem

- Year/Venue: 2025 / ICML poster
- Category: 3D Equivariance, Calibration, and Registration
- Tags: geometry, Diffusion, Generation, point cloud, 3D Vision
- Paper link: ./2025/ICML/2025_ICML_Generative-Point-Cloud-Registration/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Unlike geometry-only matching in previous methods, our approach introduces MatchControlNet, a matching-specific 2D generative model that generates cross-view images pairs from point cloud data, providing rich color cues ...
- Introduction Point cloud registration is a problem of finding the optimal rigid transformation, comprising a 3D rotation and a 3D translation, which aligns the source and target point ...
- Existing 3D registration methods can be roughly categorized into traditional approaches and data-driven deep methods.

## 해결하려는 문제
- Unlike geometry-only matching in previous methods, our approach introduces MatchControlNet, a matching-specific 2D generative model that generates cross-view images pairs from point cloud data, providing rich color cues ...
- Recent RGB-D registration studies (Yuan et al., 2023; Mu et al., 2024) have shown images would significantly enhance the distinctiveness of point cloud descriptors, leading to improved matching ...
- However, real-world Despite the impressive performance achieved by current point cloud registration methods, their robustness remains limited in challenging scenarios that contain low overlap, repetitive patterns, or noisy ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
