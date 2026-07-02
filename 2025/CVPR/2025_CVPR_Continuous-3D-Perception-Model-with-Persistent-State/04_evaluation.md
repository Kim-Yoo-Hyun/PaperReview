# Evaluation

- Year/Venue: 2025 / CVPR
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, SLAM, representation
- Paper link: ./2025/CVPR/2025_CVPR_Continuous-3D-Perception-Model-with-Persistent-State/paper.pdf
- Code/Project: https://cut3r.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- Matterport3D
- KITTI
- Waymo

## Metrics
- accuracy
- mAP
- ATE
- RPE

## Evaluation Protocol and Results
- We evaluate our method on various 3D/4D tasks and demonstrate competitive or state-of-the-art performance in each.
- In addition to reconstructing a scene from images, our method can also infer structure for unseen parts of the scene, given a virtual camera query (shown in blue). ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
