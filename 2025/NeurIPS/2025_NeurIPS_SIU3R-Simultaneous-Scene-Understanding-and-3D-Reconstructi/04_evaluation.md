# Evaluation

- Year/Venue: 2025 / NeurIPS spotlight
- Category: 3D Semantic Understanding and Alignment
- Tags: 3D reconstruction, semantic, alignment, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_SIU3R-Simultaneous-Scene-Understanding-and-3D-Reconstructi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet

## Metrics
- accuracy
- mIoU
- mAP
- PSNR
- SSIM
- LPIPS
- AbsRel
- RMSE

## Evaluation Protocol and Results
- 4.1 Experimental Setup Implementation Details.
- We utilize ScanNet for training and validation, the largest public dataset that concurrently provides multi-view images with dense semantic/instance segmentation labels and text-referred segmentation labels.
- We conduct training on 8 NVIDIA GeForce RTX
- Extensive experiments demonstrate that our method achieves state-of-the-art performance not only on the individual tasks of 3D reconstruction and understanding, but also on the task of simultaneous understanding ...
- To achieve this, recent approaches resort to 2D-to-3D feature alignment paradigm, which leads to limited 3D understanding capability and potential semantic information loss.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
