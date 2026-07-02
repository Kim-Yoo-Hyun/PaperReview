# Evaluation

- Year/Venue: 2025 / CVPR
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, geometry, Transformer
- Paper link: ./2025/CVPR/2025_CVPR_VGGT-Visual-Geometry-Grounded-Transformer/paper.pdf
- Code/Project: https://github.com/facebookresearch/vggt
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- Replica
- KITTI
- Objaverse
- DTU
- ETH3D
- Habitat

## Metrics
- accuracy
- mAP
- Chamfer
- PSNR
- SSIM
- LPIPS

## Evaluation Protocol and Results
- The network achieves state-of-the-art results in multiple 3D tasks, including camera parameter estimation, multi-view depth estimation, dense point cloud reconstruction, and 3D point tracking.
- MASt3R have shown promising results in this direction, but these networks can only process two images at once and rely on post-processing to reconstruct more images, fusing pairwise ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
