# PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Robot action에 따라 3D scene이 어떻게 변하는지 예측하여 새로운 manipulation task의 계획에 활용하는 문제다.

## Bottleneck and Changed Formulation

State와 robot action을 3D point flow 공간에서 연결하고 action-conditioned scene dynamics를 학습한다.

## System and Robotics Loop

RGB-D capture + robot action의 point-flow 표현 → scene 3D point flow → MPC action selection.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

RGB-D calibration, point-flow action 변환, partial observability와 MPC cost 정의.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

CVF abstract/저자 project는 real/sim training data와 Franka의 pushing·deformable/articulated manipulation·tool use 평가를 설명한다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_PointWorld_Scaling_3D_World_Models_for_In-The-Wild_Robotic_Manipulation_CVPR_2026_paper.pdf) · [저자 project/code](https://point-world.github.io/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
