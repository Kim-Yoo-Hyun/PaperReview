# Evaluation

- Year/Venue: 2024 / ECCV
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D geometry, matching, calibration
- Paper link: ./2024/ECCV/2024_ECCV_Grounding-Image-Matching-in-3D-with-MASt3R/paper.pdf
- Code/Project: https://github.com/naver/mast3r
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- COCO
- ScanNet
- KITTI
- Waymo
- DTU
- CO3D
- Habitat

## Metrics
- accuracy
- mAP
- Chamfer

## Evaluation Protocol and Results
- Extensive experiments show that our approach, coined MASt3R, significantly outperforms the state of the art on multiple matching tasks.
- We introduce a fast reciprocal matching scheme that not only accelerates matching by orders of magnitude, but also comes with theoretical guarantees and, lastly, yields improved results.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
