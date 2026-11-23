# PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / CVPR
- Authors: Wenlong Huang, Yu-Wei Chao, Arsalan Mousavian, Ming-Yu Liu, Dieter Fox, Kaichun Mo, Li Fei-Fei
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: 3D-point-flow, action-conditioned-dynamics, MPC
- Aliases: PointWorld
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.html
- Venue verification: https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.pdf
- Code/Project: https://point-world.github.io/
- Code: https://github.com/NVlabs/PointWorld
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요.

## Problem and Importance

Robot action에 따라 3D scene이 어떻게 변하는지 예측하여 새로운 manipulation task의 계획에 활용하는 문제다.

## Core Idea and Contribution

State와 robot action을 3D point flow 공간에서 연결하고 action-conditioned scene dynamics를 학습한다.

## Observation–State–Action Interface

RGB-D capture + robot action의 point-flow 표현 → scene 3D point flow → MPC action selection.

## Evaluation Scope and Claim Boundary

CVF abstract/저자 project는 real/sim training data와 Franka의 pushing·deformable/articulated manipulation·tool use 평가를 설명한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.pdf) · [저자 project/code](https://point-world.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Current trend / action-relevant 3D. State와 action을 3D point flow로 표현하고 예측을 manipulation MPC에 연결한다. DP3/3D-VLA 이후 explicit geometry와 world model을 비교할 직접적인 연결이다. 본문 평가의 보장 범위와 calibration 의존성은 추가 확인 대상이다.

## Verification Boundary

RGB-D calibration, point-flow action 변환, partial observability와 MPC cost 정의을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
