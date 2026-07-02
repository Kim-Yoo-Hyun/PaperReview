# Evaluation

- Year/Venue: 2023 / RSS
- Category: Open-Vocabulary 3D Mapping
- Tags: CLIP, Robotics, semantic, NeRF
- Paper link: ./2023/RSS/2023_RSS_CLIP-Fields-Weakly-Supervised-Semantic-Fields-for-Robotic/paper.pdf
- Code/Project: https://mahis.life/clip-fields/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- COCO
- ScanNet200
- Habitat
- HM3D
- RxR
- ScanRefer
- ScanQA

## Metrics
- accuracy
- IoU
- AP
- mAP

## Evaluation Protocol and Results
- When compared to baselines like Mask-RCNN, our method outperforms on few-shot instance identification or semantic segmentation on the HM3D dataset with only a fraction of the examples.
- Importantly, we show that this mapping can be trained with supervision coming only from webimage and web-text trained models such as CLIP, Detic, and Sentence-BERT; and thus uses ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
