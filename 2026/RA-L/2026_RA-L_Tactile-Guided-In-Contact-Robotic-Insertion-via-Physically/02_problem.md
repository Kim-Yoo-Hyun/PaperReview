# Tactile-Guided In-Contact Robotic Insertion via Physically Consistent Force-Array Representation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

접촉 뒤 시야가 가려지면 커넥터의 작은 정렬 오차를 영상에서 판독하기 어렵다.

## Bottleneck and Changed Formulation

접촉 후 시연에서 힘 분포 표현을 관측하는 diffusion policy를 학습하고 합력·모멘트만 쓰는 경우와 대조한다.

## System and Robotics Loop

접촉 중의 촉각 입력을 삽입 동작으로 바꾼다. 센서 배열은 국소 하중의 분포를 보존한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

센서 교정, 커넥터별 시행 수, 실물 분포 신호를 재현할 수 있는 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

IEEE 초록은 학습 분포 안에서 합력·모멘트만 쓴 변형이 약간 우세했고, 새 2·3핀과 USB·HDMI 커넥터 전이에서는 분포 표현이 유리했다고 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://ieeexplore.ieee.org/document/11692602/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
