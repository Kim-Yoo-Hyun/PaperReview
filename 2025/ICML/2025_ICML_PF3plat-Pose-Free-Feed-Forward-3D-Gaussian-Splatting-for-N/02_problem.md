# Problem

- Year/Venue: 2025 / ICML poster
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, geometry, 3D Vision
- Paper link: ./2025/ICML/2025_ICML_PF3plat-Pose-Free-Feed-Forward-3D-Gaussian-Splatting-for-N/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- We tackle the problem of view synthesis from sparse, unposed images in a single feed-forward pass.
- However, the main challenge arises from the parametrization of pixel-aligned 3D Gaussians, as their misalignments inevitably yield noisy or sparse gradients that destabilize training.
- To address some of these limitations, recent efforts (Yu et al., 2021; Johari et al., 2022; Chen et al., 2021; Yang et al., 2023) have introduced generalized view ...

## 해결하려는 문제
- Extensive experiments on largescale real-world datasets confirm that PF3plat achieves state-of-the-art performance across all benchmarks, with ablation studies validating our design choices.
- However, the main challenge arises from the parametrization of pixel-aligned 3D Gaussians, as their misalignments inevitably yield noisy or sparse gradients that destabilize training.
- Among these methods, particularly those utilizing 3DGS (Charatan et al., 2023; Chen et al., 2024), have demonstrated remarkable rendering speed and efficiency, alongside impressive reconstruction and view synthesis ...

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
