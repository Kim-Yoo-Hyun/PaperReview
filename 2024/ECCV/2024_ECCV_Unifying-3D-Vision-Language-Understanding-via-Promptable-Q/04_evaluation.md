# Evaluation

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_Unifying-3D-Vision-Language-Understanding-via-Promptable-Q/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet200
- Replica
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
- AP
- SPL
- success rate

## Evaluation Protocol and Results
- 1 shows a summary of the datasets used for the multitask training of PQ3D.
- This is achieved through three key innovations: (1) unifying various 3D scene representations (i.e., voxels, point clouds, multi-view images) into a shared 3D coordinate space by segment-level grouping, ...
- Particularly, PQ3D improves the state-ofthe-art on ScanNet200 by 4.9% (AP25), ScanRefer by 5.4% (acc@0.5), Multi3DRefer by 11.7% (F1@0.5), and Scan2Cap by 13.4% (CIDEr@0.5).

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
