# Evaluation — Perpetual Humanoid Control for Real-time Simulated Avatars

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2023 / ICCV
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, whole-body control, motion imitation
- Official paper: https://openaccess.thecvf.com/content/ICCV2023/html/Luo_Perpetual_Humanoid_Control_for_Real-time_Simulated_Avatars_ICCV_2023_paper.html
- Code/Project: https://zhengyiluo.github.io/PHC-Site/
- Source audit: official CVF abstract and project page checked; controller/training details remain UNVERIFIED.

## Protocol

대규모 motion dataset의 tracking, robustness와 real-time avatar control을 평가한다.

## Limitations and Reproducibility

simulated avatar setting과 real humanoid dynamics/actuation 사이의 transfer는 직접 보장되지 않는다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
