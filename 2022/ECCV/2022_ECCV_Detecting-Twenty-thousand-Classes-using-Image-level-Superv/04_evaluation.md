# Evaluation

- Year/Venue: 2022 / ECCV
- Category: Open-Vocabulary 3D Mapping
- Tags: Vision-Language Model, open-vocabulary, detection, semantic
- Paper link: ./2022/ECCV/2022_ECCV_Detecting-Twenty-thousand-Classes-using-Image-level-Superv/paper.pdf
- Code/Project: https://github.com/facebookresearch/Detic
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- COCO

## Metrics
- accuracy
- IoU
- AP
- mAP

## Evaluation Protocol and Results
- We mainly use the open-vocabulary setting proposed by Gu et al. , and also report results on the standard LVIS setting.
- For ease of training and evaluation, most of our experiments use the 997 classes that overlap with the LVIS vocabulary and denote this subset as IN-L.
- See Appendix B for results of directly using captions.
- We evaluate Detic on the large-vocabulary object detection dataset LVIS .
- Our results show that Detic yields excellent detectors even for classes without box annotations.
- It outperforms prior work on both open-vocabulary and long-tail detection benchmarks.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
