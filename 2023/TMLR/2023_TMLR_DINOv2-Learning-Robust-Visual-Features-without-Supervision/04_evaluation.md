# Evaluation

- Year/Venue: 2023 / TMLR
- Category: Foundations: Vision Foundation Models
- Tags: self-supervised, representation
- Paper link: ./2023/TMLR/2023_TMLR_DINOv2-Learning-Robust-Visual-Features-without-Supervision/paper.pdf
- Code/Project: https://github.com/facebookresearch/dinov2
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- KITTI

## Metrics
- accuracy
- mIoU
- mAP
- RMSE
- ADE

## Evaluation Protocol and Results
- First, we show that our self-supervised features outperform the current state of the art by a very large margin.
- In Table 5, we show that the Top-1 accuracy on the validation set of ImageNet-1k improves by more than +2% when the backbone is finetuned.
- We also want to validate that our features are competitive with state-of-the-art open-source weakly supervised models.
- We see the components proposed in this work lead to a very significant improvement (+4.2%) over the previous state of the art (iBOT ViT-L/16 trained on ImageNet-22k) on ...
- First, we show that our self-supervised features outperform the current state of the art by a very large margin.
- In Table 5, we show that the Top-1 accuracy on the validation set of ImageNet-1k improves by more than +2% when the backbone is finetuned.

## Baselines
- In our comparisons, we use two kinds of models as baselines.
- We compare to the best performing self-supervised models that are openly available.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
