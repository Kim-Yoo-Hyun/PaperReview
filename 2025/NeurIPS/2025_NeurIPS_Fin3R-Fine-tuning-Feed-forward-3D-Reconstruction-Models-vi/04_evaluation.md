# Evaluation

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, depth, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Fin3R-Fine-tuning-Feed-forward-3D-Reconstruction-Models-vi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- KITTI
- DTU
- ETH3D

## Metrics
- accuracy
- mAP

## Evaluation Protocol and Results
- The table shows that our integrated models consistently achieve lower relative depth error and higher δ1 scores.
- After fine-tuning, our method improves the model’s ability to capture fine details and complex surfaces such as transparent ones.
- Fine-tuned VGGT performs almost as well as the state-of-the-art expert model, MoGe.
- Best results in each session are highlighted in bold.
- The table shows that our integrated models consistently achieve lower relative depth error and higher δ1 scores.
- The fine-tuned models consistently deliver sharper boundaries, recover complex structures, and achieve higher geometric accuracy in both single- and multi-view settings, while adding only the tiny LoRA weights, ...

## Baselines
- Interestingly, we observe that although DUSt3R’s depth estimates rank last among the evaluated models, they exhibit the sharpest boundaries compared with the other two baseline models.
- Fine-tuned VGGT performs almost as well as the state-of-the-art expert model, MoGe.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
