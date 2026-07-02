# Evaluation

- Year/Venue: 2025 / ICCV
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, Diffusion, Generation, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_Distilling-Diffusion-Models-to-Efficient-3D-LiDAR-Scene-Co/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- KITTI
- SemanticKITTI

## Metrics
- accuracy
- Chamfer

## Evaluation Protocol and Results
- Extensive experiments demonstrate that ScoreLiDAR significantly accelerates the completion time from 30.55 to 5.37 seconds per frame (>5×) on SemanticKITTI and achieves superior performance compared to state-of-the-art 3D ...
- This paper proposes a novel distillation method tailored for 3D LiDAR scene completion models, dubbed ScoreLiDAR, which achieves efficient yet high-quality scene completion.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
