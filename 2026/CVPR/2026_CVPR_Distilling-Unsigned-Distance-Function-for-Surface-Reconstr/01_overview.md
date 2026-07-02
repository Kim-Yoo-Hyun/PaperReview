# Distilling Unsigned Distance Function for Surface Reconstruction from 3D Gaussian Splatting

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_Distilling-Unsigned-Distance-Function-for-Surface-Reconstr/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To tackle these challenges, we distill a patch-based UDF predictor, trained on synthetic ground-truth surfaces, into a student UDF module that is optimized jointly with the Gaussian splatting ...
- Existing methods for UDF learning generally fall into two families: NeRF-based frameworks and 3D Gaussian Splatting (3DGS) based methods .

## Core Idea
- We compare our method against both SDF-based and UDFbased surface reconstruction approaches across all scenes.
- This mismatch produces noisy or biased gradients and leads to unstable training, over-smoothing, and the loss of fine surface details.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- iFLYTEK Research can represent open geometry directly, attractive for objects or scenes containing thin sheets, partial scans, or incomplete observations .
- Despite the representational flexibility of UDFs, learning them from calibrated multi-view images is more challenging than learning SDFs for two reasons.
- First, there is no ground-truth surface for supervision; training must rely primarily on multi-view photometric consistency, which is indirect and sensitive to occlusion, view-dependence, and illumination changes.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To tackle these challenges, we distill a patch-based UDF predictor, trained on synthetic ground-truth surfaces, into a student UDF module that is optimized jointly with the Gaussian splatting ...
- Existing methods for UDF learning generally fall into two families: NeRF-based frameworks and 3D Gaussian Splatting (3DGS) based methods .
- First, there is no ground-truth surface for supervision; training must rely primarily on multi-view photometric consistency, which is indirect and sensitive to occlusion, view-dependence, and illumination changes.

## Abstract Cue
- iFLYTEK Research can represent open geometry directly, attractive for objects or scenes containing thin sheets, partial scans, or incomplete observations .
