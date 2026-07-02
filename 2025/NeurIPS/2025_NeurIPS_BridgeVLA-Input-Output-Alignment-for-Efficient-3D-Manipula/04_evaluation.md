# Evaluation

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_BridgeVLA-Input-Output-Alignment-for-Efficient-3D-Manipula/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- RLBench

## Metrics
- mAP
- SR
- success rate
- collision

## Evaluation Protocol and Results
- BridgeVLA outperforms all existing state-of-the-art 3D manipulation methods on both benchmarks, addressing Q3 and Q4.
- We compare BridgeVLA with multiple baselines. (1) Image-BC (CNN) and Image-BC (ViT) are two 2D baseline methods which predict the actions directly from 2D images using CNN and ...
- Through the experiments, we aim to answer five questions: Q1: How effectively does BridgeVLA learn 3D robot manipulation compared to state-of-the-art methods when sufficient data is available?
- 4.1.2 Experiments on COLOSSEUM & GemBench To further evaluate the generalization capabilities of BridgeVLA, we conduct experiments on the COLOSSEUM benchmark and GemBench .
- BridgeVLA outperforms state-of-the-art baselines across three simulation benchmarks.
- BridgeVLA outperforms all existing state-of-the-art 3D manipulation methods on both benchmarks, addressing Q3 and Q4.

## Baselines
- We compare BridgeVLA with multiple baselines. (1) Image-BC (CNN) and Image-BC (ViT) are two 2D baseline methods which predict the actions directly from 2D images using CNN and ...
- Through the experiments, we aim to answer five questions: Q1: How effectively does BridgeVLA learn 3D robot manipulation compared to state-of-the-art methods when sufficient data is available?

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
