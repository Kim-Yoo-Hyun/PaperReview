# MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Fixed-base VLA의 도달 범위를 mobile manipulation으로 확장한다.

## Bottleneck and Changed Formulation

VLA의 end-effector waypoint와 base–arm bi-level trajectory optimization을 연결한다.

## System and Robotics Loop

언어·관측 → waypoint → base/arm trajectory.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

waypoint frame, solver budget, controller, real-robot split.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

OVMM 및 실제 로봇 평가를 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_MoManipVLA_Transferring_Vision-language-action_Models_for_General_Mobile_Manipulation_CVPR_2025_paper.html) · [저자 project/code](https://gary3410.github.io/momanipVLA/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
