# NG-GS: NeRF-guided 3D Gaussian Splatting Segmentation

- Year/Venue: 2026 / CVPR
- Category: 3D Semantic Understanding and Alignment
- Tags: Gaussian Splatting, NeRF, semantic, alignment, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_NG-GS-NeRF-guided-3D-Gaussian-Splatting-Segmentation/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Our approach begins by automatically identifying ambiguous Gaussians at object boundaries using mask variance analysis.

## Core Idea
- Similar to COB-GS, we use a mask loss to supervise the mask label training process, but add NeRF density generation weights to optimize edge Gaussian continuity learning: mAcc ...
- Our method leverages the continuous representation capacity of NeRF to refine boundary Gaussians, effectively mitigating discontinuities and achieving superior segmentation performance.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments on NVOS, LERF-OVS, and ScanNet benchmarks demonstrate that our method achieves state-of-theart performance, with significant gains in boundary mIoU.
- This negligence leads to the abrupt changes on the boundaries during scene segmentation, resulting in inaccurate segmentation characterized by edge artifacts, as shown in Figure 1.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments on NVOS, LERF-OVS, and ScanNet benchmarks demonstrate that our method achieves state-of-theart performance, with significant gains in boundary mIoU.
- Our approach begins by automatically identifying ambiguous Gaussians at object boundaries using mask variance analysis.
- Our method leverages the continuous representation capacity of NeRF to refine boundary Gaussians, effectively mitigating discontinuities and achieving superior segmentation performance.

## Abstract Cue
- Recent advances in 3D Gaussian Splatting (3DGS) have enabled highly efficient and photorealistic novel view synthesis.
