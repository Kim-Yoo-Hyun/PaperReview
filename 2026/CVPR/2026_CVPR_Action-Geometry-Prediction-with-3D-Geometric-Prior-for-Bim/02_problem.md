# Action-Geometry Prediction with 3D Geometric Prior for Bimanual Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

양팔 조작은 물체와 두 팔의 geometry 변화를 함께 예측해야 한다.

## Bottleneck and Changed Formulation

3D foundation latent·2D semantic feature·proprioception을 합쳐 action chunk와 미래 3D latent를 공동 예측한다.

## System and Robotics Loop

RGB·proprioception → action chunk 및 dense point map으로 해석할 미래 latent. RL exploration covariance와 별개다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

미래 geometry target·3D foundation freeze 여부·양팔 action frame·data budget.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

RoboTwin simulation과 실세계 양팔 조작에서 성공·협응·공간 예측을 비교한다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Action-Geometry_Prediction_with_3D_Geometric_Prior_for_Bimanual_Manipulation_CVPR_2026_paper.pdf) · [저자 project/code](https://github.com/Chongyang-99/GAP). Exact objective, constraints, success definition은 본문 수동 확인 필요.
