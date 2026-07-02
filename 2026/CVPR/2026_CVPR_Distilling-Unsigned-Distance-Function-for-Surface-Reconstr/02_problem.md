# Problem

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_Distilling-Unsigned-Distance-Function-for-Surface-Reconstr/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- To tackle these challenges, we distill a patch-based UDF predictor, trained on synthetic ground-truth surfaces, into a student UDF module that is optimized jointly with the Gaussian splatting ...
- Existing methods for UDF learning generally fall into two families: NeRF-based frameworks and 3D Gaussian Splatting (3DGS) based methods .

## 해결하려는 문제
- To tackle these challenges, we distill a patch-based UDF predictor, trained on synthetic ground-truth surfaces, into a student UDF module that is optimized jointly with the Gaussian splatting ...
- Existing methods for UDF learning generally fall into two families: NeRF-based frameworks and 3D Gaussian Splatting (3DGS) based methods .
- First, there is no ground-truth surface for supervision; training must rely primarily on multi-view photometric consistency, which is indirect and sensitive to occlusion, view-dependence, and illumination changes.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
