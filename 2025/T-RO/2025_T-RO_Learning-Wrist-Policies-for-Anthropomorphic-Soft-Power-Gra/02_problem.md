# Learning Wrist Policies for Anthropomorphic Soft Power Grasping in Handle and Door Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

손잡이의 위치와 방향이 불확실할 때 순응하는 손목을 이용해 접촉을 유지하는 문제다.

## Bottleneck and Changed Formulation

손·팔을 하나의 임피던스 제어기로 다루며, 손목 임피던스와 손바닥·손가락 힘을 함께 조절하는 정책을 학습한다.

## System and Robotics Loop

손과 팔 기구의 제어 설정을 하나의 정책에서 정해 손잡이 잡기와 회전에 사용한다.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

손의 구동 형태와 문 유형별 시험 조건 및 힘·속도 제어 기준선.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

시뮬레이션에서 학습하고 완전 구동 손과 부족 구동 손을 장착한 서비스 휴머노이드에서 손잡이·문 조작을 검증했다.

## Evidence Anchor

[공식 paper/abstract](https://portal.fis.tum.de/en/publications/learning-wrist-policies-for-anthropomorphic-soft-power-grasping-i/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
