# NeRF Is a Valuable Assistant for 3D Gaussian Splatting

- Year/Venue: 2025 / ICCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, NeRF, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_NeRF-Is-a-Valuable-Assistant-for-3D-Gaussian-Splatting/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- This framework leverages the inherent continuous spatial representation of NeRF to mitigate several limitations of 3DGS, including sensitivity to Gaussian initialization, limited spatial awareness, and weak inter-Gaussian correlations, ...
- Experimental results on benchmark datasets show that NeRF-GS surpasses existing methods and achieves state-of-the-art performance.

## Core Idea
- We introduce NeRF-GS, a novel framework that jointly optimizes Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS).
- Nonetheless, the reliance on Gaussian initialization and limited spatial perception can lead to instability in 3DGS training .

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experimental results on benchmark datasets show that NeRF-GS surpasses existing methods and achieves state-of-the-art performance.
- NeRF-GS establishes a bridge of communication between NeRF and 3DGS, leveraging information sharing, modeling of distinct characteristics, and joint optimization to enable 3DGS to achieve higher fidelity representation.
- In this case, NeRF-GS outperforms the vanilla 3DGS by 1.8dB in PSNR.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experimental results on benchmark datasets show that NeRF-GS surpasses existing methods and achieves state-of-the-art performance.
- We introduce NeRF-GS, a novel framework that jointly optimizes Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS).
- Nonetheless, the reliance on Gaussian initialization and limited spatial perception can lead to instability in 3DGS training .

## Abstract Cue
- We introduce NeRF-GS, a novel framework that jointly optimizes Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS).
