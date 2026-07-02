# Evaluation

- Year/Venue: 2022 / ECCV
- Category: Foundations: 3D Representation Learning
- Tags: point cloud, 3D Vision
- Paper link: ./2022/ECCV/2022_ECCV_Point-MAE-Masked-Autoencoders-for-Point-Cloud-Self-supervi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ModelNet40
- ShapeNet
- ShapeNetPart

## Metrics
- accuracy
- mIoU
- IoU
- Chamfer
- ECE

## Evaluation Protocol and Results
- On the hardest variant PB-T50-RS, our model achieves 85.18% accuracy, outperforming Point-BERT by 2.11%.
- Specifically, our approach with standard Transformers backbone surpasses IAE that uses a more powerful DGCNN as the backbone (As shown in Table 2, when training from scratch, DGCNN ...
- We conduct the following experiments with our Point-MAE. a) We pre-train our model on ShapeNet training set. b) We evaluate our pre-trained model on various downstream tasks, including ...
- To demonstrate the effectiveness of our method, we visualize reconstruction results on ShapeNet validation set in Figure 4.
- Specifically, our pre-trained models achieve 85.18% accuracy on ScanObjectNN and 94.04% accuracy on ModelNet40, outperforming all the other self-supervised learning methods.
- On the hardest variant PB-T50-RS, our model achieves 85.18% accuracy, outperforming Point-BERT by 2.11%.

## Baselines
- Our Point-MAE largely improves the baseline by 10.16%, 7.74%, and 7.94% for three variants respectively.
- Furthermore, our method speeds up pre-training by 1.7× compared to Point-BERT .

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
