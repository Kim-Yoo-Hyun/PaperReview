# Evaluation

- Year/Venue: 2021 / CoRL
- Category: Equivariance, Diffusion, and 3D Action
- Tags: Robotics, equivariant, 3D geometry, manipulation
- Paper link: ./2021/CoRL/2021_CoRL_Neural-Descriptor-Fields-SE3-Equivariant-Object-Representa/paper.pdf
- Code/Project: https://github.com/anthonysimeonov/ndf_robot
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ShapeNet

## Metrics
- accuracy
- mAP
- success rate
- collision

## Evaluation Protocol and Results
- We propose to achieve this objective by searching (via optimization) for the pose whose descriptor matches that observed in the demonstration.
- Our performance generalizes across both object instances and 6-DoF object poses, and significantly outperforms a recent baseline that relies on 2D descriptors.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
