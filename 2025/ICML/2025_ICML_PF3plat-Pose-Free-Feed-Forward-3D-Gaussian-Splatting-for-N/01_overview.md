# PF3plat: Pose-Free Feed-Forward 3D Gaussian Splatting for Novel View Synthesis

- Year/Venue: 2025 / ICML poster
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, geometry, 3D Vision
- Paper link: ./2025/ICML/2025_ICML_PF3plat-Pose-Free-Feed-Forward-3D-Gaussian-Splatting-for-N/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We tackle the problem of view synthesis from sparse, unposed images in a single feed-forward pass.
- However, the main challenge arises from the parametrization of pixel-aligned 3D Gaussians, as their misalignments inevitably yield noisy or sparse gradients that destabilize training.
- To address some of these limitations, recent efforts (Yu et al., 2021; Johari et al., 2022; Chen et al., 2021; Yang et al., 2023) have introduced generalized view ...

## Core Idea
- Our method builds on 3DGS and relaxes common requirements such as dense views, accurate camera poses or depth, and large image overlaps.
- In other words, we cannot train our approach on their dataset, nor can they train theirs on ours. *: We also include a MASt3R variant that omits iterative ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments on largescale real-world datasets confirm that PF3plat achieves state-of-the-art performance across all benchmarks, with ablation studies validating our design choices.
- Among these methods, particularly those utilizing 3DGS (Charatan et al., 2023; Chen et al., 2024), have demonstrated remarkable rendering speed and efficiency, alongside impressive reconstruction and view synthesis ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments on largescale real-world datasets confirm that PF3plat achieves state-of-the-art performance across all benchmarks, with ablation studies validating our design choices.
- However, the main challenge arises from the parametrization of pixel-aligned 3D Gaussians, as their misalignments inevitably yield noisy or sparse gradients that destabilize training.
- Among these methods, particularly those utilizing 3DGS (Charatan et al., 2023; Chen et al., 2024), have demonstrated remarkable rendering speed and efficiency, alongside impressive reconstruction and view synthesis ...

## Abstract Cue
- 2024), and substantial image overlaps (Yu et al., 2021; Johari et al., 2022), which limit their practical applicability.
