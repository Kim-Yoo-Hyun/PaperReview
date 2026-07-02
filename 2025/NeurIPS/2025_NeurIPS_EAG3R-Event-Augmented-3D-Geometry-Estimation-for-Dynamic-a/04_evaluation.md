# Evaluation

- Year/Venue: 2025 / NeurIPS spotlight
- Category: 3D Representation Learning and Foundation Models
- Tags: 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_EAG3R-Event-Augmented-3D-Geometry-Estimation-for-Dynamic-a/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- accuracy
- mAP
- ATE
- RPE
- RMSE

## Evaluation Protocol and Results
- We compare EAG3R with state-of-the-art pose free learning-based reconstruction method, including DUSt3R , MonST3R , and Easi3R .
- We report results using standard metrics: Absolute Relative Error (Abs Rel ↓), Scale-invariant RMSE log (RMSE log ↓), and the threshold accuracy δ < 1.25 (↑), where lower ...
- However, applying RetinexFormer, a widely used image enhancement network, as a preprocessing light-up step (denoted as (LightUp)) does not yield significant improvements and, in some cases, degrades performance, ...
- Fine-tuning MonST3R improves its performance across
- Extensive experiments demonstrate that EAG3R significantly outperforms state-of-the-art RGB-only baselines across monocular depth estimation, camera pose tracking, and dynamic reconstruction tasks.
- We compare EAG3R with state-of-the-art pose free learning-based reconstruction method, including DUSt3R , MonST3R , and Easi3R .

## Baselines
- We compare EAG3R with state-of-the-art pose free learning-based reconstruction method, including DUSt3R , MonST3R , and Easi3R .
- 4.1 Experiment Details For training, we fine-tune the MonST3R baseline by training its ViT-Base decoder, DPT heads, Enhancement Net, and the Event Adapter.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
