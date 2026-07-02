# Evaluation

- Year/Venue: 2019 / TOG
- Category: Foundations: 3D Representation Learning
- Tags: point cloud, 3D Vision
- Paper link: ./2019/TOG/2019_TOG_Dynamic-Graph-CNN-for-Learning-on-Point-Clouds/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- S3DIS
- ModelNet40
- ShapeNet
- ShapeNetPart

## Metrics
- accuracy
- mIoU
- IoU
- mAP

## Evaluation Protocol and Results
- Our baseline model using the fixed k-NN graph outperforms the previous state-of-the-art PointNet++ by 1.0% accuracy, at the same time being 7 times faster.
- Our model achieves the best results on this dataset.
- An advanced version including dynamical graph recomputation achieves the best results on this dataset.
- A more advanced version of our model including a dynamically-updated graph computation outperforms PointNet++, PCNN by 2.2% and 0.6% respectively, while being much ACM Trans.
- Our baseline model using the fixed k-NN graph outperforms the previous state-of-the-art PointNet++ by 1.0% accuracy, at the same time being 7 times faster.
- Our model achieves the best results on this dataset.

## Baselines
- Our baseline model using the fixed k-NN graph outperforms the previous state-of-the-art PointNet++ by 1.0% accuracy, at the same time being 7 times faster.
- 2015] classification experiment to compare the complexity of our model to previous state-of-the-art.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
