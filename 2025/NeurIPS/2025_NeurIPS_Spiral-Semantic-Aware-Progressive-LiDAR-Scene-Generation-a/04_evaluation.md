# Evaluation

- Year/Venue: 2025 / NeurIPS poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, semantic, alignment, Diffusion, Generation, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Spiral-Semantic-Aware-Progressive-LiDAR-Scene-Generation-a/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- SemanticKITTI
- nuScenes

## Metrics
- accuracy
- mIoU
- mAP

## Evaluation Protocol and Results
- Despite having the smallest parameter size of only 61M, Spiral achieves the best performance across all semantic-aware metrics, outperforming the two-step method, R2DM & SPVCNN++ , by 31.03%, ...
- Compared with the second best method (R2DM & RangeNet++ ), Spiral achieves improvements of 49.03%, 67.84%, and 46.79% on S-FRD, S-FPD, and S-JSD, respectively.
- For the previous metrics that evaluate only the unlabeled LiDAR scenes, Spiral outperforms R2DM on most metrics, indicating that the additional semantic prediction task does not compromise the ...
- To obtain semantic labels for the generated unlabeled LiDAR scenes, we use RangeNet++ with official pretrained weights and SPVCNN++ , an improved implementation of SPVCNN provided in UniSeg ...
- Experiments on the SemanticKITTI and nuScenes datasets demonstrate that S PIRAL achieves state-of-the-art performance with the smallest parameter size, outperforming two-step methods that combine the generative and segmentation ...
- Despite having the smallest parameter size of only 61M, Spiral achieves the best performance across all semantic-aware metrics, outperforming the two-step method, R2DM & SPVCNN++ , by 31.03%, ...

## Baselines
- For the generative models in two-step baseline methods, including LiDARGen , LiDM , and R2DM , we follow the official training settings.
- Using SPVCNN++ as the segmentation backbone, we compare Spiral with R2DM & RangeNet++ under different ratios of available real labeled data.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
