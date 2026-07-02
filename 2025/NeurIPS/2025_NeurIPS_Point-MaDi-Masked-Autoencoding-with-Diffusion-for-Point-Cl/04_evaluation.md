# Evaluation

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Generative Modeling and Diffusion
- Tags: Diffusion, Generation, point cloud, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Point-MaDi-Masked-Autoencoding-with-Diffusion-for-Point-Cl/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- S3DIS
- ModelNet40
- ShapeNet
- ShapeNetPart

## Metrics
- accuracy
- mIoU
- IoU
- AP
- Chamfer

## Evaluation Protocol and Results
- Our Point-MaDi achieves superior performance on all subsets, reaching 95.52%, 93.46%, and 89.52% accuracies, respectively.
- While diffusion-based methods like PointDif may not consistently dominate on the relatively clean and less diverse ModelNet40 dataset, our Point-MaDi still achieves 93.8% accuracy, demonstrating strong generalization without ...
- Compared to the previous Point-MAE , our diffusion-based Point-MaDi yields consistent improvements of 5.50%, 5.17%, and 4.34% on OBJ-BG, OBJ-ONLY, and PB-T50-RS, respectively.
- We take the overall accuracy (OA) on ScanObjectNN subsets as the evaluation metric and summarize experiment results as in Tab.
- Extensive experiments on ScanObjectNN, ModelNet40, ShapeNetPart, S3DIS, and ScanNet demonstrate that Point-MaDi achieves superior performance across downstream tasks, surpassing Point-MAE by 5.50% on OBJ-BG, 5.17% on OBJ-ONLY, and ...
- Our Point-MaDi achieves superior performance on all subsets, reaching 95.52%, 93.46%, and 89.52% accuracies, respectively.

## Baselines
- Compared to the previous Point-MAE , our diffusion-based Point-MaDi yields consistent improvements of 5.50%, 5.17%, and 4.34% on OBJ-BG, OBJ-ONLY, and PB-T50-RS, respectively.
- Following previous research, we randomly sample 2,048 points from each input instance and adopt the same segmentation head for the fair comparison, which concatenates the global features with ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
