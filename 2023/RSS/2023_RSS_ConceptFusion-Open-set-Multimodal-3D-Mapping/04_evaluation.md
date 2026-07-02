# Evaluation

- Year/Venue: 2023 / RSS
- Category: Open-Vocabulary 3D Mapping
- Tags: sensor fusion, open-vocabulary, SLAM, Robotics
- Paper link: ./2023/RSS/2023_RSS_ConceptFusion-Open-set-Multimodal-3D-Mapping/paper.pdf
- Code/Project: https://concept-fusion.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- COCO
- ScanNet
- Replica
- KITTI
- SemanticKITTI
- AI2-THOR
- ScanRefer

## Metrics
- accuracy
- mIoU
- IoU
- mAP

## Evaluation Protocol and Results
- This enables effective zero-shot spatial reasoning, not needing any additional training or finetuning, and retains long-tailed concepts better than supervised approaches, outperforming them by more than 40% margin ...
- We demonstrate that pixel-aligned open-set features can be fused into 3D maps via traditional SLAM and multi-view fusion approaches.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
