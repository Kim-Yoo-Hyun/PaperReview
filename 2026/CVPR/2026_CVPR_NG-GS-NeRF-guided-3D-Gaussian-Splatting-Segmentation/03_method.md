# Method

- Year/Venue: 2026 / CVPR
- Category: 3D Semantic Understanding and Alignment
- Tags: Gaussian Splatting, NeRF, semantic, alignment, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_NG-GS-NeRF-guided-3D-Gaussian-Splatting-Segmentation/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Similar to COB-GS, we use a mask loss to supervise the mask label training process, but add NeRF density generation weights to optimize edge Gaussian continuity learning: mAcc ...
- Our method leverages the continuous representation capacity of NeRF to refine boundary Gaussians, effectively mitigating discontinuities and achieving superior segmentation performance.
- Our approach begins by automatically identifying ambiguous Gaussians at object boundaries using mask variance analysis.

## 원리적 동기
- Our approach begins by automatically identifying ambiguous Gaussians at object boundaries using mask variance analysis.
- Similar to COB-GS, we use a mask loss to supervise the mask label training process, but add NeRF density generation weights to optimize edge Gaussian continuity learning: mAcc ...

## 핵심 방법론
- Similar to COB-GS, we use a mask loss to supervise the mask label training process, but add NeRF density generation weights to optimize edge Gaussian continuity learning: mAcc ...
- For evaluation, we use the Neural Volumetric Object Selection (NVOS) , LERF-OVS , and ScanNet .
- NVOS consists of eight scenes picked from the LLFF dataset.
- The overall loss function during the joint optimization period is as follows: Ltotal = Lalign + λm Lmask + λc Lcont + λs Lsmth , B-mIoU B-mIoU mAcc ...
