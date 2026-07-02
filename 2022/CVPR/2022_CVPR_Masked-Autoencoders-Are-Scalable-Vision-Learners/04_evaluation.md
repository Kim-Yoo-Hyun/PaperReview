# Evaluation

- Year/Venue: 2022 / CVPR
- Category: Foundations: Vision Foundation Models
- Tags: Vision Foundation Model, self-supervised, representation
- Paper link: ./2022/CVPR/2022_CVPR_Masked-Autoencoders-Are-Scalable-Vision-Learners/paper.pdf
- Code/Project: https://github.com/facebookresearch/mae
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- COCO

## Metrics
- accuracy
- mIoU
- AP

## Evaluation Protocol and Results
- Transfer performance in downstream tasks outperforms supervised pretraining and shows promising scaling behavior. encoder decoder input target .... .... arXiv:2111.06377v3 [cs.CV] 19 Dec 2021 Facebook AI Research (FAIR) ...
- Our scalable approach allows for learning high-capacity models that generalize well: e.g., a vanilla ViT-Huge model achieves the best accuracy (87.8%) among methods that use only ImageNet-1K data.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
