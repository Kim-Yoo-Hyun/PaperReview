# Evaluation

- Year/Venue: 2002 / AAAI
- Category: 3D Geometry, Reconstruction, and SLAM
- Tags: Robotics, SLAM, particle filter, state estimation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- accuracy
- AP
- mAP

## Evaluation Protocol and Results
- In a set of experiments specifically aimed to elucidate the scaling properties of the approach, we evaluated the map and robot pose errors as a function of the ...
- Overall, the results indicate favorably scaling to large number of landmarks and small particle sets.
- The results are graphically depicted in Figure 6.
- Real-world experiments were complimented by systematic simulation experiments, to investigate the scaling abilities of the approach.
- Experimental results demonstrate the advantages and limitations of the FastSLAM algorithm on both simulated and realworld data.
- In a set of experiments specifically aimed to elucidate the scaling properties of the approach, we evaluated the map and robot pose errors as a function of the ...

## Baselines
- FastSLAM resulted in an average residual map error of 8.3 centimeters, when compared to the manually generated map.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
