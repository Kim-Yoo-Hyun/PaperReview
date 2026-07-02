# Evaluation

- Year/Venue: 2026 / ICLR Poster
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, 3D Vision
- Paper link: ./2026/ICLR/2026_ICLR_GPT4Scene-Understand-3D-Scenes-from-Videos-with-Vision-Lan/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- Matterport3D
- Replica
- Habitat
- HM3D
- EmbodiedScan
- ScanRefer
- ReferIt3D
- SQA3D
- ScanQA

## Metrics
- BLEU
- accuracy
- IoU
- mAP

## Evaluation Protocol and Results
- Here we emphasize that post-training with the GPT4Scene framework, the model achieves accurate QA performance using only pure video input, thereby demonstrating GPT4Scene’s effectiveness in enhancing visual comprehension ...
- E F ULL Q UANTITIVE R ESULTS Here, we present the complete metrics for all five benchmarks.
- Qwen2-VL Ours MMBench-ENval Liu et al. (2024c) MMBench-CNval Liu et al. (2024c) MMStar Chen et al. (2024a) RealWorldQA xAI (2024) 82.4 81.7 60.7 70.1 81.2 79.9 57.6 68.5 ...
- Here we emphasize that post-training with the GPT4Scene framework, the model achieves accurate QA performance using only pure video input, thereby demonstrating GPT4Scene’s effectiveness in enhancing visual comprehension ...
- E F ULL Q UANTITIVE R ESULTS Here, we present the complete metrics for all five benchmarks.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
