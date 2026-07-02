# Evaluation

- Year/Venue: 2024 / CVPR
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, semantic, alignment, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_SG-PGM-Partial-Graph-Matching-Network-with-Semantic-Geomet/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 3RScan

## Metrics
- accuracy
- mAP
- Chamfer

## Evaluation Protocol and Results
- Experiments show that our method improves the alignment accuracy by 10∼20% in low-overlap and random transformation scenarios and outperforms the existing work in multiple downstream tasks.
- Subsequent downstream tasks such as point cloud registration are achieved by running a pre-trained registration network within the matched regions.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
