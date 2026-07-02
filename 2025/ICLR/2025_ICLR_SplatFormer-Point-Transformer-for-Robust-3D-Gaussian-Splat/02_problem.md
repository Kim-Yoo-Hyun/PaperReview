# Problem

- Year/Venue: 2025 / ICLR Spotlight
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, point cloud, 3D Vision
- Paper link: ./2025/ICLR/2025_ICLR_SplatFormer-Point-Transformer-for-Robust-3D-Gaussian-Splat/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- V-dimensional feature vectors vk ∈ RV : K {vk }K k=1 = fθ ({Gk }k=1 ), (4) which encapsulate key details of the 3D primitives.
- The feature decoder gθ then transforms this latent representation into splat attribute residuals K {∆Gk = (∆pk , ∆sk , ∆αk , ∆qk , ∆ak )}K k=1 = ...
- Our 3DGS splat encoder is based on the PTv3 framework (Wu et al., 2024b).

## 해결하려는 문제
- The feature decoder gθ then transforms this latent representation into splat attribute residuals K {∆Gk = (∆pk , ∆sk , ∆αk , ∆qk , ∆ak )}K k=1 = ...
- This hierarchical architecture models contextual relationships among ne
- Then another 4 stages of attention blocks and upsampling grid pooling layers are used to restore the resolution.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
