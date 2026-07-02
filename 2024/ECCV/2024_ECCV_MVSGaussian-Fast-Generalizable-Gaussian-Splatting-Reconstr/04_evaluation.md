# Evaluation

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_MVSGaussian-Fast-Generalizable-Gaussian-Splatting-Reconstr/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- DTU
- Tanks and Temples

## Metrics
- accuracy
- mAP
- PSNR
- SSIM
- LPIPS

## Evaluation Protocol and Results
- We compare our method with state-of-the-art generalizable NeRF methods , as well as the recent generalizable Gaussian method .
- For the generalization comparison, we follow the same experimental settings as and borrow some results reported in .
- For per-scene optimization experiments, we include NeRF and 3D-GS for comparison.
- Following MVSNeRF , we train the generalizable model on the DTU training set and evaluate it on the DTU test set.
- Compared with previous generalizable NeRF-based methods, which typically require minutes of fine-tuning and seconds of rendering per image, MVSGaussian achieves real-time rendering with better synthesis quality for each ...
- Compared with the vanilla 3D-GS, MVSGaussian achieves better view synthesis with less training computational cost.

## Baselines
- We compare our method with state-of-the-art generalizable NeRF methods , as well as the recent generalizable Gaussian method .
- For the generalization comparison, we follow the same experimental settings as and borrow some results reported in .

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
