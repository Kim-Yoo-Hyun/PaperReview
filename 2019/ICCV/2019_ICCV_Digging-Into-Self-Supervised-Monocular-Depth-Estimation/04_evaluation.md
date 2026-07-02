# Evaluation

- Year/Venue: 2019 / ICCV
- Category: Foundations: Monocular Geometry
- Tags: 3D Vision, monocular depth, self-supervised, geometry
- Paper link: ./2019/ICCV/2019_ICCV_Digging-Into-Self-Supervised-Monocular-Depth-Estimation/paper.pdf
- Code/Project: https://github.com/nianticlabs/monodepth2
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- KITTI

## Metrics
- accuracy
- mAP
- SSIM
- RMSE

## Evaluation Protocol and Results
- We demonstrate the effectiveness of each component in isolation, and show high quality, state-of-the-art results on the KITTI benchmark.
- In this paper, we propose a set of improvements, which together result in both quantitatively and qualitatively improved depth maps compared to competing self-supervised methods.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
