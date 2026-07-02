# Urban-GS: A Unified 3D Gaussian Splatting Framework for Compact and High-Fidelity Aerial-to-Street Reconstruction

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_Urban-GS-A-Unified-3D-Gaussian-Splatting-Framework-for-Com/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, seamless integration of both aerial and street view images to model urban scenes remains a significant challenge for 3DGS.
- This limitation highlights the necessity of jointly reconstructing scenes using aerial and street view imagery, as the complementary perspe

## Core Idea
- In this work, we present Urban-GS, a novel framework built upon Gaussian Splatting for the compact unified reconstruction and high-fidelity rendering of urban scenes from both aerial and ...
- Furthermore, we propose a Global-to-Local Optimization strategy to refine the reconstruction of under-optimized regions resulting from imbalanced view distributions.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments across diverse urban scene datasets demonstrate that Urban-GS significantly outperforms the state-of-theart method in novel-view rendering quality, while simultaneously reducing storage overhead by an average of 41%.
- Building on this foundation, recent advances have substantially improved the scalability and rendering fidelity of Gaussian Splatting for urban scenes using either aerial [14–16, 24] or street view ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this work, we present Urban-GS, a novel framework built upon Gaussian Splatting for the compact unified reconstruction and high-fidelity rendering of urban scenes from both aerial and ...
- Experiments across diverse urban scene datasets demonstrate that Urban-GS significantly outperforms the state-of-theart method in novel-view rendering quality, while simultaneously reducing storage overhead by an average of 41%.
- Building on this foundation, recent advances have substantially improved the scalability and rendering fidelity of Gaussian Splatting for urban scenes using either aerial [14–16, 24] or street view ...

## Abstract Cue
- Recently, 3D Gaussian Splatting (3DGS) has revolutionized radiance field reconstruction, enabling efficient and highfidelity novel view synthesis.
