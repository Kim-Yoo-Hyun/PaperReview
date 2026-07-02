# Evaluation

- Year/Venue: 2025 / NeurIPS spotlight
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_OnlineSplatter-Pose-Free-Online-3D-Reconstruction-for-Free/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- Objaverse

## Metrics
- accuracy
- PSNR
- SSIM
- LPIPS

## Evaluation Protocol and Results
- This section evaluates our approach by outlining the evaluation protocol, describing the datasets for training and testing, comparing against state-of-the-art baselines, and conducting ablation studies to analyze each ...
- We therefore design a stage-wise evaluation protocol that examines performance across three distinct phases: 1) Early Stage (Tearly := {1 ≤ t ≤ 4}): Tests the model’s ability ...
- 4.1 Experimental settings Evaluation Protocol To properly evaluate our online object reconstruction framework, we need to assess how well it performs at different stages of observation accumulation.
- Evaluations on real-world datasets demonstrate that OnlineSplatter significantly outperforms state-of-the-art pose-free reconstruction baselines, consistently improving with more observations while maintaining constant memory and runtime.
- This section evaluates our approach by outlining the evaluation protocol, describing the datasets for training and testing, comparing against state-of-the-art baselines, and conducting ablation studies to analyze each ...

## Baselines
- This section evaluates our approach by outlining the evaluation protocol, describing the datasets for training and testing, comparing against state-of-the-art baselines, and conducting ablation studies to analyze each ...
- We then compare these renders against the corresponding frames Vv .

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
