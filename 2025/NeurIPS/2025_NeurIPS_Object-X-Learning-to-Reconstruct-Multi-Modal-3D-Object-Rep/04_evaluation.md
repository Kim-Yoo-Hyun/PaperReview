# Evaluation

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Representation Learning and Foundation Models
- Tags: 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Object-X-Learning-to-Reconstruct-Multi-Modal-3D-Object-Rep/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- 3RScan

## Metrics
- accuracy
- mAP
- PSNR
- SSIM
- LPIPS

## Evaluation Protocol and Results
- Next, we will provide experiments on various tasks benefiting from Object-X.
- All experiments are conducted on a machine with an A100 GPU with 80GB of RAM.
- To evaluate the geometric accuracy, we extract a triangle mesh from the optimized 3D Gaussians, following the procedure from 2DGS (41).
- Ablation studies, more visuals, and detailed descriptions of baselines are provided in the supplementary material.
- Evaluations on two challenging real-world datasets demonstrate that Object-X achieves high-fidelity novel-view synthesis comparable to standard 3D Gaussian Splatting, while significantly improving geometric accuracy.
- Moreover, Object-X achieves competitive performance with specialized methods in scene alignment and localization.

## Baselines
- Ablation studies, more visuals, and detailed descriptions of baselines are provided in the supplementary material.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
