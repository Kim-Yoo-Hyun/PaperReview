# Problem

- Year/Venue: 2020 / ECCV
- Category: Foundations: 3D Representation Learning
- Tags: 3D Vision, point cloud, representation, self-supervised
- Paper link: ./2020/ECCV/2020_ECCV_PointContrast-Unsupervised-Pre-training-for-3D-Point-Cloud/paper.pdf
- Code/Project: https://github.com/facebookresearch/PointContrast
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Different from previous works, we focus on high-level scene understanding tasks.

## 해결하려는 문제
- Our findings are extremely encouraging: using a unified triplet of architecture, source dataset, and contrastive loss for pre-training, we achieve improvement over recent best results in segmentation and ...
- Furthermore, the improvement was similar to supervised pre-training, suggesting that future efforts should favor scaling data collection over more detailed annotation.
- To this end, we select a suite of diverse datasets and tasks to measure the effect of unsupervised pre-training on a large source set of 3D scenes.

## 선행 연구 / 배경 단서
- In 2D vision, the finding that pre-training a network on a rich source set (e.g.
- A particularly important setting is when the pre-training stage is unsupervised, as this opens up the possibility to utilize a practically infinite ?
