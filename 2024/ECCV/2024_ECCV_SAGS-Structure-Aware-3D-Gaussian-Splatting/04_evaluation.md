# Evaluation

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_SAGS-Structure-Aware-3D-Gaussian-Splatting/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- AP
- PSNR
- SSIM
- LPIPS

## Evaluation Protocol and Results
- We compared the proposed method with NeRF- and 3D-GS-based state-of-the-art works in novel-view synthesis, including the Mip-NeRF360 , Plenoxels , iNGP , 3D-GS along with the recent Scaffold-GS ...
- To evaluate the proposed method, on par with the 3D-GS , we utilized 13 scenes including nine scenes from Mip-NeRF360 , two scenes from Tanks&Temples and two scenes ...
- We evaluate the proposed SAGS model in terms of rendering quality, structure preservation, and rendering performance.
- In this work, we propose a structure-aware Gaussian Splatting method (SAGS) that implicitly encodes the geometry of the scene, which reflects to state-of-the-art rendering performance and reduced storage ...
- Extensive experiments across multiple benchmark datasets demonstrate the superiority of SAGS compared to state-of-theart 3D-GS methods under both rendering quality and model size.

## Baselines
- We compared the proposed method with NeRF- and 3D-GS-based state-of-the-art works in novel-view synthesis, including the Mip-NeRF360 , Plenoxels , iNGP , 3D-GS along with the recent Scaffold-GS ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
