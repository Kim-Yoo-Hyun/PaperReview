# EyeRobot 2.0: Active Gaze for Precise Manipulation without Wrist Cameras

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Problem in One Sentence

Wrist camera 없이 정밀 manipulation을 위한 gaze를 구성한다.

## Bottleneck and Changed Formulation

Stereo fixation 기반 표현과 gaze/행동 제어를 연결한다.

## System and Robotics Loop

Stereo 시선·관측 → fixation-relative 표현 → manipulation.

이 interface에서 관측·내부 상태·학습 target·실행 action을 분리해서 읽는다. 정확한 controller 경계와 timing은 아래 질문으로 확인한다.

## Assumptions to Verify — Researcher Interpretation

물리/가상 gaze 경계, stereo calibration, RL/BC supervision, robot 범위.

해당 조건을 실제 논문의 가정으로 확정하려면 formulation과 experiment를 대조해야 한다.

## Evaluation Target

Simulation 및 실제 bimanual manipulation을 보고한다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2610.03710) · [저자 project/code](https://eyerobot2.github.io/). Exact objective, constraints, success definition은 본문 수동 확인 필요.
