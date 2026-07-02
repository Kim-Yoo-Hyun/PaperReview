# Evaluation

- Year/Venue: 2014 / NeurIPS
- Category: Foundations: Monocular Geometry
- Tags: 3D Vision, monocular depth, geometry
- Paper link: ./2014/NeurIPS/2014_NeurIPS_Depth-Map-Prediction-from-a-Single-Image-using-a-Multi-Sca/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- KITTI

## Metrics
- accuracy
- mAP
- RMSE

## Evaluation Protocol and Results
- We train our model on the raw versions both NYU Depth v2 and KITTI .
- The raw distributions contain many additional images collected from the same scenes as in the more commonly used small distributions, but with no preprocessing; in particular, points for ...
- However, our model’s natural ability to handle such gaps as well as its demand for large training sets make these fitting sources of data.
- 4.1 NYU Depth The NYU Depth dataset is composed of 464 indoor scenes, taken as video sequences using a Microsoft Kinect camera.
- By leveraging the raw datasets as large sources of training data, our method achieves boundaries without the need for superpixelation.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
