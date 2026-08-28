# Problem — Perpetual Humanoid Control for Real-time Simulated Avatars

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2023 / ICCV
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, whole-body control, motion imitation
- Official paper: https://openaccess.thecvf.com/content/ICCV2023/html/Luo_Perpetual_Humanoid_Control_for_Real-time_Simulated_Avatars_ICCV_2023_paper.html
- Code/Project: https://zhengyiluo.github.io/PHC-Site/
- Source audit: official CVF abstract and project page checked; controller/training details remain UNVERIFIED.

## Target Problem and Assumptions

다양한 motion을 장시간 안정적으로 따라가면서 perturbation/fall로 인한 tracking failure를 줄인다.

## Closed-Loop Position

reference human motion과 simulated humanoid proprioception을 joint control actions로 매핑한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
