# EC-Flow: Enabling Versatile Robotic Manipulation from Action-Unlabeled Videos via Embodiment-Centric Flow

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Object-centric flow만으로는 가려짐·변형 물체·변위 없는 조작을 표현하기 어렵다.

## Bottleneck and Changed Formulation

Embodiment-centric flow와 goal alignment를 학습하고 URDF 제약으로 행동에 변환한다.

## System and Robotics Loop

영상·지시 → embodiment flow → kinematic 제약 기반 robot action.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

URDF만으로 해결되는 변환 범위, calibration, 동역학·접촉 정보 의존성.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Meta-World와 실제 가림·변형·비변위 조작을 평가한다.

## Evidence Anchor

[공식 paper/abstract](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_EC-Flow_Enabling_Versatile_Robotic_Manipulation_from_Action-Unlabeled_Videos_via_Embodiment-Centric_ICCV_2025_paper.html) · [저자 project/code](https://ec-flow1.github.io/) · [공식 code](https://github.com/YixiangChen515/EC-Flow). Exact objective, constraints, success definition은 본문 수동 확인 필요.
