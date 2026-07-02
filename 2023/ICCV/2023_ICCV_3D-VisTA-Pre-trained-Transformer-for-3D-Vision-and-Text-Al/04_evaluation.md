# Evaluation

- Year/Venue: 2023 / ICCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision-Language, alignment, Transformer
- Paper link: ./2023/ICCV/2023_ICCV_3D-VisTA-Pre-trained-Transformer-for-3D-Vision-and-Text-Al/paper.pdf
- Code/Project: https://3d-vista.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- ScanNet
- 3RScan
- Objaverse
- ScanRefer
- ReferIt3D
- Nr3D
- Sr3D
- SQA3D
- ScanQA

## Metrics
- BLEU
- accuracy
- IoU
- mAP
- SR

## Evaluation Protocol and Results
- It achieves state-of-the-art results on various 3D-VL tasks, ranging from visual grounding and dense captioning to question answering and situated reasoning.
- Moreover, 3D-VisTA demonstrates superior data efficiency, obtaining strong performance even with limited annotations during downstream task fine-tuning.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
