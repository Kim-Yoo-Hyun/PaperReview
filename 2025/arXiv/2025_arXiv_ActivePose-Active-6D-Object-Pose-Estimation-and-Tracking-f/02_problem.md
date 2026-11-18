# ActivePose: Active 6D Object Pose Estimation and Tracking for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

고정 카메라와 pose ambiguity가 물체 이동·가림 상황의 추정과 추적을 불안정하게 한다.

## Bottleneck and Changed Formulation

CAD virtual view와 FoundationPose 기반 정보로 VLM이 모호성을 평가하고 다음 camera view를 선택한다.

## System and Robotics Loop

RGB 관측·CAD 기반 가상 시점 → ambiguity score·NBV·pose tracking으로 이어진다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

VLM score calibration·CAD render 조건·물리 camera 비용·task success 기준.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

공식 초록은 로봇 조작을 위한 active pose estimation/tracking을 다룬다. Task별 성공률과 camera 이동 비용은 본문 확인 필요다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2509.11364). Exact objective, constraints, success definition은 본문 수동 확인 필요.
