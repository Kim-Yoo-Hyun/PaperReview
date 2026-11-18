# GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

반응형 2D VLA가 정밀한 3D 상태 변화와 미래 움직임을 충분히 다루지 못한다.

## Bottleneck and Changed Formulation

로봇 keypoint trajectory와 3D Gaussian geometry 예측을 학습 supervision으로 사용한다.

## System and Robotics Loop

Motion history·영상에서 action을 생성하며 3D decoding은 학습용이다. 배포 query token과 native 3D reconstruction을 구별한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

Depth supervision·keypoint target·배포 추가 token 비용·baseline data fairness.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

RoboCasa Human-50·LIBERO·실세계 조작에서 geometry 관련 이득을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Qian_GeoPredict_Leveraging_Predictive_Kinematics_and_3D_Gaussian_Geometry_for_Precise_CVPR_2026_paper.html) · [저자 project/code](https://github.com/jingjingqian75/GeoPredict). Exact objective, constraints, success definition은 본문 수동 확인 필요.
